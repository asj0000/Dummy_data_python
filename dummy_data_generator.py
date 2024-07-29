import pandas as pd
from faker import Faker
import json
import string
import random
import numpy as np
import psycopg2
import random
from datetime import datetime
import os
from delete_dummy_data import delete_dummy_data
import subprocess

fake = Faker('en_IN')
db_url = 'vivek-tree-vivek-tree.e.aivencloud.com'
db_port = '15050'
db_user = 'avnadmin'
db_password = os.environ['DB_PASSWORD']
db_name = 'defaultdb'
db_schema = '14trees_2'

#Connect to DB
def get_db_connection():
        conn = psycopg2.connect(database=db_name, 
                                      user=db_user, 
                                      password=db_password,
                                      host=db_url, 
                                      port=db_port)    
        return conn


#Function to connect to server and get site_ids
def get_dummy_site_ids_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('select s.id from "14trees_2".sites s where s.name_marathi like \'Test Random Site%\' order by s.created_at desc limit 10')
    site_ids =  [row[0] for row in cursor.fetchall()]
   
    connection.close()
    return site_ids

#Function to connect to server and get plot_ids
def get_dummy_plot_ids_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('select p.id from "14trees_2".plots p where p.plot_id  like \'dummy_plot_id%\' order by p.created_at desc limit 100 ')
    plot_ids =  [row[0] for row in cursor.fetchall()]
    
    connection.close()
    return plot_ids

#Function to connect to server and get plant_type_ids
def get_dummy_plant_type_ids_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('select distinct pt.id  from "14trees_2".plant_types pt limit 10')
    plant_type_ids =  [row[0] for row in cursor.fetchall()]
    print(plant_type_ids)
    connection.close()
    return plant_type_ids

#Function to connect to server and get user_ids
def get_dummy_user_ids_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('select u.id  from "14trees_2".users u where u.user_id like \'dummy%\' ORDER BY u.created_at DESC limit 1000')
    user_ids =  [row[0] for row in cursor.fetchall()]
    print(user_ids)
    connection.close()
    return user_ids

#Function to connect to server and get visit_ids
def get_dummy_visit_ids_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('select v.id  from "14trees_2".visits v where v.visit_name like \'Dummy%\' ORDER BY v.id DESC limit 1000')
    visit_ids =  [row[0] for row in cursor.fetchall()]
    print(visit_ids)
    connection.close()
    return visit_ids

#Function to connect to server and get org_ids
def get_dummy_org_ids_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('select g.id  from "14trees_2"."groups" g where  g."name" like \'Dummy%\' ORDER BY g.created_at DESC limit 1000')
    group_ids =  [row[0] for row in cursor.fetchall()]
    print(group_ids)
    connection.close()
    return group_ids


#Function to generate dummy users
def generate_dummy_users(num_records):
    users = []
     
    for i in range(num_records):
            record = {
                
                "name": "Dummy User "+ str(i+1),
                "email": fake.email(),
                "user_id": "dummy-user-id-"+str(i+1) ,
                "phone": None,
                "birth_date": None,
                "mongo_id": None,                
                "status_message": None,
                "last_system_updated_at": None,
                "created_at": datetime.now().strftime('%D %H:%M:%S'),
                "updated_at": datetime.now().strftime('%D %H:%M:%S')
                            
            }
            users.append(record)
    return users


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
    "area_acres": None,
    "length_km": None,
    "tree_count": None,
    "unique_id": None,
    "photo_album": None,
    "grove_type": None,
    "album": None,
    "album_contains": None,
    "status": None,
    "remark": None,
    "hosted_at": None,
    "created_at": datetime.now().strftime('%D %H:%M:%S'),
    "updated_at": datetime.now().strftime('%D %H:%M:%S'),
    "consent_document_link": None,
    "google_earth_link": None,
    "trees_planted": None,
    "site_key_1": None,
    "site_key_2": None,
    "account": None,
    "data_errors": None,
    "date_planted": None,
    "consent_letter": fake.random_element(elements=[
    "14T - संस्था पत्र",
    "14T - ग्राम पंचायत पत्र",
]),
    "maintenance_type": fake.random_element(elements=[
    "PLANTATION_ONLY",
    "FULL_MAINTENANCE", 
    "DISTRIBUTION_ONLY",
]),
    "tags": None,
    "komoot_file_link": None
}
        sites.append(record)
    return sites


#Function to generate dummy plots
def generate_dummy_plots(num_records):
    plots = []
    site_ids = get_dummy_site_ids_from_db()
   
    for each_site_id in site_ids: 
        for i in range(num_records):
            record = {
                
                "name": "Test Random plot " + str(i+1),
                "plot_id":"dummy-plot-id-"+ str(each_site_id)+"-"+str(fake.random_int(min=1 , max=2500)) ,
                "tags": None,
                "boundaries": '{"type": "Polygon", "coordinates": [[[18.92883906964203, 73.7769217462353], [18.92705962338517, 73.77601906599243], [18.92691470408016, 73.77663242954684], [18.92764441915284, 73.77778245391168], [18.92883906964203, 73.7769217462353]]]}',
                "center": '{"type": "Point", "coordinates": [18.92883906964203, 73.7769217462353]}',
                "gat": None,
                "status": None,
                "land_type_mongo_id": None,
                "category_monogo_id": None,
                "land_type": None,
                "category": fake.random_element(elements=['Foundation' , 'Public']),
                "mongo_id": None,
                "created_at": datetime.now().strftime('%D %H:%M:%S'),
                "updated_at": datetime.now().strftime('%D %H:%M:%S'),
                "site_id": each_site_id
                
            }
            plots.append(record)
    return plots


# Function to generate dummy trees
def generate_dummy_trees(num_records):
    trees = [] 
    plot_ids = get_dummy_plot_ids_from_db()
    plant_type_ids = get_dummy_plant_type_ids_from_db()
    
    for ind, each_plot_id  in enumerate(plot_ids):
        for i in range(num_records):
            record = {
                
                "sapling_id": str(960000 + ind*num_records+ i + 1), 
                "plant_type_id": int(random.choice(plant_type_ids)),
                "plot_id": each_plot_id,
                # "images": None,
                "tags": None,
                "location": {},
                "planted_by": 'DataAutomation',
                "mapped_to_user": None,
                "mapped_to_group": None,
                "mapped_at": None,
                "sponsored_by_user": None,
                "sponsored_by_group": None,
                "gifted_by": None,
                "gifted_to": None,
                "assigned_at": None,
                "assigned_to": None,
                # "user_tree_images": None,
                "mongo_id": None,
                "tree_type": None,
                "plot": each_plot_id,
                "description": None,
                "event_id": None,
                "memory_images": None,
                "status": None,
                "status_message":None,
                "last_system_updated_at":None,
                "created_at":datetime.now().strftime('%D %H:%M:%S'),
                "updated_at":datetime.now().strftime('%D %H:%M:%S'), 
                "tree_status":None
            
            }
            trees.append(record)
    return trees

#Function to generate dummy visits
def generate_dummy_visits(num_records):
    visits = []
    site_ids = get_dummy_site_ids_from_db()
    for i in range(num_records):
            record = {
                
                "visit_name": "Dummy Visit-"+str(i+1),
                "visit_date": datetime.now().strftime('%D'),
                "site_id": random.choice(site_ids),
                "visit_type": fake.random_element(elements=['family' , 'corporate']),
                "created_at": datetime.now().strftime('%D %H:%M:%S'),
                "updated_at": datetime.now().strftime('%D %H:%M:%S')
            }
            visits.append(record)
    return visits


#Function to generate dummy visit users
def generate_dummy_visits_users(visit_ids, user_ids):
    visit_users_records = []
    print("User Ids passed: ", user_ids)
    for visit_id in visit_ids:
        user_count = random.randint(0, len(user_ids))
        visit_users = np.random.choice(user_ids, size=user_count, replace=False)
        print("Selected user ids for visit id: "+str(visit_id)+" are ", visit_users)

        for user_id in visit_users:
            record = { 
                "visit_id": visit_id,
                "user_id": int(user_id),
                "created_at": datetime.now().strftime('%D %H:%M:%S')
            }
            visit_users_records.append(record)
    return visit_users_records

#Function to generate dummy organisations
def generate_dummy_organisations(num_records):
    oraganisations = []
   
    for i in range(num_records):
            record = {
                
                "name": "Dummy Organisation-"+str(i+1),
                "type": "corporate",
                "description": None,
                "created_at": datetime.now().strftime('%D %H:%M:%S'),
                "updated_at": datetime.now().strftime('%D %H:%M:%S')
                            
            }
            oraganisations.append(record)
    return oraganisations

#Function to generate dummy org users
def generate_dummy_org_users(org_ids, user_ids):
    org_users_records = []
    print("User Ids passed: ", user_ids)
    for org_id in org_ids:
        user_count = random.randint(0, len(user_ids))
        org_users = np.random.choice(user_ids, size=user_count, replace=False)
        print("Selected user ids for org id: "+str(org_id)+" are ", org_users)

        for user_id in org_users:
            record = { 
                "user_id": int(user_id),
                "group_id": org_id,
                "created_at": datetime.now().strftime('%D %H:%M:%S')
            }
            org_users_records.append(record)
    return org_users_records

# Function to generate dummy donations
def generate_dummy_donations(num_records):
    donations = [] 
    
    for i in range(num_records):
            record = {
                "Status": None,
                "Timestamp": datetime.now().strftime('%D %H:%M:%S'),
                "Name": None,
                "Please mention number of trees you would like to sponsor": None,
                "Please select your preference (if you want to spread your trees": None,
                "I'm making my contribution via": None,
                "Kindly upload a screenshot of payment confirmation (screenshot": None,
                "PAN number needed to qualify for 80G benefit (and for audit an": None,
                "Phone": None,
                "Please share your e-mail address so that we can send you update": None,
                "I'd like my trees to be planted in the following names": None,
                "Comments, feedback, ideas for improvement.": None,
                "Besides making a monetary contribution, I'd also like to": None,
                "80g / 501 (c)/ FCRA matters": None,
                "Please indicate if you would like to make your contribution in": None,
                "(If you selected Foundation's land preserve) I'd like my trees": None,
                "Email Address": None,
                "r": None,
                "Pledged": None,
                "Amount received": None,
                "Amount received for General Purpose": None,
                "Trees paid": None,
                "Payment received": None,
                "Date received": None,
                "Second installment": None,
                "Land type": None,
                "Zone": None,
                "Grove": None,
                "Assigned plot": None,
                "Tree planted": None,
                "Assigner's dashboard": None,
                "Wire confirmation": None,
                "Originator": None,
                "Difference in no of trees paid and pledged": None,
                "Donation receipt number": None,
                "AMount as per DON file": None,
                "Amount Paid": None,
                "Empty": None,
                "Base": None,
                "Check": None,
                "CA remarks": None,
                "Action": None,
                "Payment Status": None,
                "Status remarks": None,
                "Status_2": None,
                "Donor Type": 'DataAutomation',
                "Inventory Qty": None,
                "Inventory Type": None,
                "Remarks for inventory": None
            }
            donations.append(record)
    return donations



def convert_to_csv(records, file_name):
    df = pd.DataFrame(records)
    df.to_csv(file_name, index=False,encoding='utf-8-sig')
    print(f'Input data saved to {file_name}')

def upload_csv_to_db(csv_file, db_url, db_port, dbuser, db_password, db_schema, table_name): 
    commands = '''
        export pg_str="postgresql://{dbuser}:{db_password}@{db_url}:{db_port}/defaultdb?sslmode=require"; 
        csvsql --db $pg_str --no-create --insert {csv_file} --db-schema "{db_schema}" --tables {table_name}
    '''.format(csv_file=csv_file, db_url=db_url, db_port=db_port, dbuser=dbuser, db_password=db_password, db_schema=db_schema, table_name=table_name)

    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    out, err = process.communicate(commands)
    print("Output: ", out)
    print("Error: ", err)

def create_data():
    num_records = 10
   
    # dummy_sites = generate_dummy_sites(num_records)
    # print(f'Dummy Sites Json: {json.dumps(dummy_sites, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_sites.csv'
    # table_name = 'sites'
    # convert_to_csv(dummy_sites, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)

    
    # dummy_plots = generate_dummy_plots(num_records)
    # print(f'Dummy Plots Json: {json.dumps(dummy_plots, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_plots.csv'
    # table_name = 'plots'
    # convert_to_csv(dummy_plots, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)


    # dummy_users = generate_dummy_users(num_records)
    # print(f'Dummy Users Json: {json.dumps(dummy_users, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_users.csv'
    # table_name = 'users'
    # convert_to_csv(dummy_users, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)

    # dummy_visits = generate_dummy_visits(num_records)
    # print(f'Dummy Visits Json: {json.dumps(dummy_visits, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_visits.csv'
    # table_name = 'visits'
    # convert_to_csv(dummy_visits, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)
    
    # dummy_visits_users = generate_dummy_visits_users(get_dummy_visit_ids_from_db(), get_dummy_user_ids_from_db())
    # print(f'Dummy Visit-Users Json: {json.dumps(dummy_visits_users, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_visit_users.csv'
    # table_name = 'visit_users'
    # convert_to_csv(dummy_visits_users, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)
    

    # dummy_trees = generate_dummy_trees(num_records)
    # print(f'Dummy Trees Json: {json.dumps(dummy_trees, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_trees.csv'
    # table_name = 'trees'
    # convert_to_csv(dummy_trees, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)
    
    dummy_organisations = generate_dummy_organisations(num_records)
    print(f'Dummy Organisations Json: {json.dumps(dummy_organisations, ensure_ascii=False, indent=4)}')
    csv_file = 'dummy_organisations.csv'
    table_name = 'groups'
    convert_to_csv(dummy_organisations, csv_file)
    upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)

    dummy_org_users = generate_dummy_org_users(get_dummy_org_ids_from_db(), get_dummy_user_ids_from_db())
    print(f'Dummy Org-Users Json: {json.dumps(dummy_org_users, ensure_ascii=False, indent=4)}')
    csv_file = 'dummy_org_users.csv'
    table_name = 'user_groups'
    convert_to_csv(dummy_org_users, csv_file)
    upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)
    
    # dummy_donations = generate_dummy_donations(num_records)
    # print(f'Dummy Donations Json: {json.dumps(dummy_donations, ensure_ascii=False, indent=4)}')
    # csv_file = 'dummy_donations.csv'
    # table_name = 'donations'
    # convert_to_csv(dummy_donations, csv_file)
    # upload_csv_to_db(csv_file, db_url, db_port, db_user, db_password,db_schema, table_name)

def delete_data():
    conn = get_db_connection()
    delete_dummy_data(conn, 'trees')
    delete_dummy_data(conn, 'plots')
    delete_dummy_data(conn, 'visit_users')
    delete_dummy_data(conn, 'visits')
    delete_dummy_data(conn,'sites')
    delete_dummy_data(conn, 'org_users')
    delete_dummy_data(conn, 'users')
    # delete_dummy_data(conn, 'donations')
    delete_dummy_data(conn, 'organisations')
    conn.close()

def main(): 
    delete_data()
    # create_data()
    # get_dummy_user_ids_from_db()
    
main()