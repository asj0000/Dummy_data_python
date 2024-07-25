import pandas as pd
from faker import Faker
import json

# Initialize the Faker library
fake = Faker()

# Function to generate dummy data
def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'Name': fake.name(),         
            'Phone': fake.basic_phone_number(),
            'Email': fake.email(),
            'Company': fake.company(),
           
        }
        data.append(record)
    return data

# Number of records to generate
num_records = 10

# Generate data
dummy_data = generate_dummy_data(num_records)

#create json data
jsonData = json.dumps(dummy_data)

# Create a DataFrame
df = pd.DataFrame(dummy_data)

# Save DataFrame to CSV
csv_file = 'dummy_data-3-a.csv'
df.to_csv(csv_file, index=False)

print(f'Dummy data saved to {csv_file}')
print(f'Dummy data in json {jsonData}')
