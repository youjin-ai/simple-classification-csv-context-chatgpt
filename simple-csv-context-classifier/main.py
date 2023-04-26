import requests
import json
import csv

url = "" # OpenAI ChatGPT URL


# Read CSV data and transform it to string
csv_data = []
with open("dataset/your-file.csv", newline="") as csvfile: # Replace with your CSV file
    reader = csv.reader(csvfile)
    for row in reader:
        csv_data.append(row)

# Format the CSV data as a table string
table_string = ""
for row in csv_data:
    table_string += "|".join(row) + "\n"

downgraded_classifications = [] # Replace with your classifications that should be negatively weighted or avoided

# Input string
input_string = "This is my sentence that I wish to be classified "


content = f"""

Please recommend the top 3 'Classifications' with score (from 0 to 1) for every recommendations for the following sentence. The scores should add up to 100%: {input_string}.

The available contextual data is {table_string}.

However, '{', '.join(downgraded_classifications)}' should be considered less relevant and only be selected when no other category is suitable.
"""

# print('content', content)

# Define the data to be sent in the POST body as a Python dictionary
data = {
    "messages": [
        {"role": "user", "content": content},
    ]
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Set the headers for the request, including specifying the content type as JSON
headers = {
    "api-key": "", # Replace with your OpenAI API key
    "Content-Type": "application/json"
}

# Send the POST request with the JSON body and headers
response = requests.post(url, data=json_data, headers=headers)

# Check if the request was successful (status code 200-299)
if response.ok:
    # Parse the JSON response
    response_json = response.json()
    print("Response JSON:", response_json)
else:
    print("Request failed with status code:", response.status_code)
