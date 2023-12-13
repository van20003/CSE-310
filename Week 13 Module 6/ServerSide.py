"""
This is my Server Code for the project. The Api key was giving free from a hosting
website "app.tomorrow.io" This will allow my to ge the disired Data to send to the
client when they ping for the data. 

"""

import socket
import os
import json
import ssl

# For this to work you need a API key from a host. I choose "https://app.tomorrow.io/home"
# they provide a free key for you and free simple services.

API_KEY = 'RITsww9AtyQvuThPySWQZM4uj94l1h7R'
print(f"API Key: {API_KEY}")

# This is the function to retrieve the weather information asked by the user. It uses the 
# host via URL and uses their API key that was provided by them to obtain the information.

def get_weather_data(location):
    host = 'api.tomorrow.io'
    endpoint = f'/v4/weather/forecast?location={location}&apikey={API_KEY}'
    print(f"Endpoint: {endpoint}")

    request = f"GET {endpoint} HTTP/1.1\r\nHost: {host}\r\n\r\n"

    with socket.create_connection((host, 443)) as client_socket:
        context = ssl.create_default_context()
        secure_socket = context.wrap_socket(client_socket, server_hostname=host)
        secure_socket.send(request.encode())

        response = secure_socket.recv(4096).decode()

        headers, _, body = response.partition('\r\n\r\n')

        if '200 OK' in headers:
            print(f"Received JSON response: {body}") 
            
            try:
                weather_info = json.loads(body)
                return weather_info
            except json.JSONDecodeError as json_error:
                print(f"Error decoding JSON: {json_error}")
                return None
        else:
            return None

# To be able to use the Client's program, it needs a server to run on
# otherwise when they try to use the program it will not connect them to the api
# this function starts the server that works in between the API and the Client 
# to ensure that there is a connection between them both.

def start_server():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print("Server is up!")
        while True:
            try:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Connected to {addr}")

                    location = conn.recv(1024).decode('utf-8')
                    print(f"Received location: {location}")
                    weather_data = get_weather_data(location)

                    if weather_data:
                        conn.sendall(json.dumps(weather_data).encode('utf-8'))
                    else:
                        conn.sendall(b"Failed to get weather data.")
            except Exception as e:
                print(f"Error: {e}")

    pass

if __name__ == "__main__":
    start_server()
