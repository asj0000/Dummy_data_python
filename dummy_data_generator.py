import pandas as pd
from faker import Faker
import json
import string
import random

fake = Faker('en_IN')

# Function to generate dummy users
def generate_dummy_users(num_records):
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

# Function to generate dummy sites
def generate_dummy_sites(num_records):
    sites = []
    for i in range(num_records):
        record = {
   "name_marathi": "Test Random Site " + str(i+1),
    "name_english": "Test Random Site (English) " + str(i+1),
    "owner": fake.random_element(elements=[
        "Gram Panchayat (ग्राम पंचायत)",
        "Forest Dept. (वन विभाग)",
        "14 Trees (१४ ट्रीज)",
        "Govt. Dept. (सरकारी विभाग)",
        "NGO (संस्था)"
    ]),
    "land_type": fake.random_element(elements=[
        "Roadside (रस्ता)",
        "Barren (पडीक)",
        "Gairan (गायरान)"
    ]),
    "land_strata": fake.random_element(elements=[
        "Soil (माती)",
        "Murum (मुरूम)",
        "Rocky"
    ]),
    "district": fake.random_element(elements=[
        "Pune (पुणे)"
    ]),
    "taluka": fake.random_element(elements=[
        "Ambegaon (आंबेगाव)",
        "Khed (खेड)",
        "Nandura (नांदुरा)",
        "Motala (मोताळा)"
    ]),
    "village": fake.random_element(elements=[
        "Motala (मोताळा)",
        "Adivare",
        "Tekavadi (टेकवडी)"
    ]),
    "consent_letter": fake.random_element(elements=[
    "14T - संस्था पत्र",
    "14T - ग्राम पंचायत पत्र",
]),
    "maintenance_type": fake.random_element(elements=[
    "PLANTATION_ONLY",
    "FULL_MAINTENANCE", 
    "DISTRIBUTION_ONLY",
])
}
        sites.append(record)
    return sites

# Function to generate dummy trees
def generate_dummy_trees(num_records):
    data = []
    for _ in range(num_records):
        record = {
            
            # "id": fake.random_int(min=100000, max=999999) ,
            "sapling_id": "098000", # fix this: str(970000 + i)
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
            "memory_images": None,
            "status": None,
            "status_message":None,
            "last_system_updated_at":None,
            "created_at":None, # fix this
            "updated_at":None, # fix this
            "tree_status":None
           
        }
        data.append(record)
    return data

def convert_to_csv(records, file_name):
    df = pd.DataFrame(records)
    df.to_csv(file_name, index=False)
    print(f'Input data saved to {file_name}')

def main(): 
    print("hey there") 
    num_records = 10

    # dummy_users = generate_dummy_users(num_records)
    # print(f'Dummy Users Json: {json.dumps(dummy_users)}')
    # convert_to_csv(dummy_users, 'dummy_users.csv')

    # dummy_sites = generate_dummy_sites(num_records)
    # print(f'Dummy Sites Json: {json.dumps(dummy_sites, ensure_ascii=False, indent=4)}')
    # convert_to_csv(dummy_sites, 'dummy_sites.csv')




main()