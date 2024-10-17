import requests
import urllib.parse

# Function to load and decode all query strings from query.txt
def load_and_decode_queries(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines
    # Decode each line and return as a list
    return [urllib.parse.unquote(line.strip()) for line in lines]

# Load and decode data from query.txt
decoded_queries = load_and_decode_queries('query.txt')

# Debug: Print the decoded query strings
for i, decoded_query in enumerate(decoded_queries):
    print(f"Decoded Query String {i + 1}:", decoded_query)

# Define headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Origin': 'https://www.yescoin.gold',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://www.yescoin.gold/',
    'Accept': 'application/json, text/plain, */*'
}

# API endpoint
url = "https://api-backend.yescoin.gold/user/login"

# Send POST requests for each decoded query
for decoded_query in decoded_queries:
    payload = {
        "code": decoded_query
    }
    
    # Debug: Print the payload
    print("Payload:", payload)
    
    # Send POST request
    response = requests.post(url, json=payload, headers=headers)
    
    # Print response
    print("Response Code:", response.status_code)  # Print status code
    response_data = response.json()  # Print response as JSON
    print("Response Content:", response_data)
    
    # Check if the response is successful and contains the token
    if response.status_code == 200 and 'data' in response_data and 'token' in response_data['data']:
        token = response_data['data']['token']
        # Append the token to tokens.txt
        with open('tokens.txt', 'a') as token_file:
            token_file.write(token + '\n')  # Write the token to a new line
        print("Token written to tokens.txt:", token)
    else:
        print("Failed to retrieve token.")
