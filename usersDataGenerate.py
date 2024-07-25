import pandas as pd
from faker import Faker
import json

# Initialize the Faker library
fake = Faker()

# Function to generate dummy data
def generate_users_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'name': fake.name(),         
            'email': fake.email(),
            
           
        }
        data.append(record)
    return data

# Number of records to generate
num_records = 10

# Generate data
users_dummy_data = generate_users_data(num_records)

#create json data
jsonData = json.dumps(users_dummy_data, ensure_ascii=False, indent=4)

# Save the JSON data to a file
with open('users-dummy-data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(jsonData)

# Create a DataFrame
# df = pd.DataFrame(jsonData)

# # Save DataFrame to CSV
# csv_file = 'users-dummy-data.csv'
# df.to_csv(csv_file, index=False)

# print(f'Dummy data saved to {csv_file}')
print(f'Dummy data in json {jsonData}')
