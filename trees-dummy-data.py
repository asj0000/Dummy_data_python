import pandas as pd
from faker import Faker
import json


# Initialize the Faker library
fake = Faker()

# Function to generate dummy data
def generate_trees_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            
            # "id": fake.random_int(min=100000, max=999999) ,
            "sapling_id": "098000",
            "plant_type_id": 3,
            "plot_id": 1,
            "images": None,
            "tags": None,
            "location": {},
            "planted_by": None,
            "mapped_to_user": 3,
            "mapped_to_group": 1,
            "mapped_at": None,
            "sponsored_by_user": 3,
            "sponsored_by_group": 1,
            "gifted_by": 3,
            "gifted_to": 3,
            "assigned_at": None,
            "assigned_to": None,
            "user_tree_images": None,
            "mongo_id": None,
            "tree_type": None,
            "plot": None,
            "description": None,
            "event_id": None,
            "status": None,
            "status_message": None,
            "last_system_updated_at": None,
            "created_at": None,
            "updated_at": None,
            "memory_images": None,
            "status": None,
            "status_message":None,
            "last_system_updated_at":None,
            "created_at":None,
            "updated_at":None,
            "tree_status":None
           
        }
        data.append(record)
    return data

# Number of records to generate
num_records = 1

# Generate data
trees_dummy_data = generate_trees_data(num_records)

# Create a DataFrame
df = pd.DataFrame(trees_dummy_data)

# Save DataFrame to CSV
csv_file = 'trees_dummy_data-8.csv'
df.to_csv(csv_file, index=False)

print(f'Dummy data saved to {csv_file}')
print("Trees dummy data : " , trees_dummy_data)

