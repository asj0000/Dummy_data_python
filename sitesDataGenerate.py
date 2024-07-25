import pandas as pd
from faker import Faker
import json


# Initialize the Faker library
fake = Faker()

# Function to generate dummy data
def generate_sites_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            
            "name_marathi": fake.name(),
            "name_english": fake.name(),
            "owner":fake.last_name(),
            "land_type":fake.name(),
            "land_strata":fake.name(),
            "district":fake.name(),
            "taluka":fake.name(),
            "village":fake.name(),
           
            "consent_letter":"14T - ग्राम पंचायत पत्र",
      
            "maintenance_type":"FULL_MAINTENANCE"
           
        }
        data.append(record)
    return data

# Number of records to generate
num_records = 10

# Generate data
sites_dummy_data = generate_sites_data(num_records)

#create json data
jsonData = json.dumps(sites_dummy_data)


# Save the JSON data to a file
with open('sites-dummy-data-5.json', 'w', encoding='utf-8') as json_file:
    json_file.write(jsonData)
    
# # Create a DataFrame
# df = pd.DataFrame(jsonData)

# # Save DataFrame to CSV
# csv_file = 'sites_dummy_data.csv'
# df.to_csv(csv_file, index=False)

# print(f'Dummy data saved to {csv_file}')
print(f'Dummy data in json {jsonData}')
