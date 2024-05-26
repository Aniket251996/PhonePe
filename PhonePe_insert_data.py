import pandas as pd
import json
import os
# To fetch data for Aggregated_Transaction
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
agg_state_list = os.listdir(path)

#list to store 
clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

Agg_state_list=os.listdir(path)
Agg_state_list

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)

#Aggregated_User
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\aggregated\\user\\country\\india\\state\\"
Agg_state_list = os.listdir(path)

# List to store data
clm = {'State': [], 'Year': [], 'Quarter': [], 'Registered_Users': [], 'Count_App_Opens': [],
       'Brand': [], 'Brand_Count': [], 'Brand_Percentage': []}

for i in Agg_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as file:
                D = json.load(file)
                data = D['data']  # Access the 'data' key
                Reg_user = data['aggregated']['registeredUsers']
                App_open = data['aggregated']['appOpens']
                users_by_device = data.get('usersByDevice')  # Check if 'usersByDevice' exists
                if users_by_device and isinstance(users_by_device, list):
                    for device in users_by_device:
                        brand = device['brand']
                        brand_count = device['count']
                        brand_percentage = device['percentage']
                        clm['Registered_Users'].append(Reg_user)
                        clm['Count_App_Opens'].append(App_open)
                        clm['Brand'].append(brand)
                        clm['Brand_Count'].append(brand_count)
                        clm['Brand_Percentage'].append(brand_percentage)
                        clm['State'].append(i)
                        clm['Year'].append(j)
                        clm['Quarter'].append(int(k.strip('.json')))


# Successfully created a DataFrame
Agg_user = pd.DataFrame(clm)

#To fetch data Map_Transaction
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"
agg_state_list = os.listdir(path)

#list to store 
clm={'State':[], 'Year':[],'Quater':[],'District_Name':[], 'No_Of_Transaction':[], 'Transaction_Amount':[]}

Agg_state_list=os.listdir(path)
Agg_state_list

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm['District_Name'].append(Name)
              clm['No_Of_Transaction'].append(count)
              clm['Transaction_Amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
map_Trans=pd.DataFrame(clm)

# To fetch data for Map_Use
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
agg_state_list = os.listdir(path)

# list to store
clm = {'State': [], 'Year': [], 'Quater': [], 'District_Name': [], 'registeredUsers': [], 'appOpens': []}

for i in agg_state_list:
    p_i = path + i + "/"
    agg_yr = os.listdir(p_i)
    for j in agg_yr:
        p_j = p_i + j + "/"
        agg_yr_list = os.listdir(p_j)
        for k in agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as file:
                data = json.load(file)
                hover_data = data['data']['hoverData']
                for district, values in hover_data.items():
                    name = district
                    count = values['registeredUsers']
                    amount = values['appOpens']
                    clm['District_Name'].append(name)
                    clm['registeredUsers'].append(count)
                    clm['appOpens'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Successfully created a dataframe
map_user = pd.DataFrame(clm)

# Fetch the data for Top_Transaction
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\top\\transaction\\country\\india\\state\\"
agg_state_list = os.listdir(path)

# list to store 
clm = {'State': [], 'Year': [], 'Quater': [], 'District_Name': [], 'Transaction_Count': [], 'Transaction_Amount': []}

for i in agg_state_list:
    p_i = path + i + "/"
    agg_yr = os.listdir(p_i)
    for j in agg_yr:
        p_j = p_i + j + "/"
        agg_yr_list = os.listdir(p_j)
        for k in agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as file:
                data = json.load(file)
                districts = data['data']['districts']
                for district_data in districts:
                    district_name = district_data['entityName']
                    count = district_data['metric']['count']
                    amount = district_data['metric']['amount']
                    clm['District_Name'].append(district_name)
                    clm['Transaction_Count'].append(count)
                    clm['Transaction_Amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Successfully created a dataframe
top_Trans = pd.DataFrame(clm)

# Fetch data for Top_User
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\top\\user\\country\\india\\state\\"
agg_state_list = os.listdir(path)

# list to store 
clm = {'State': [], 'Year': [], 'Quater': [], 'District_Name': [], 'Registered_Users': []}

for i in agg_state_list:
    p_i = path + i + "/"
    agg_yr = os.listdir(p_i)
    for j in agg_yr:
        p_j = p_i + j + "/"
        agg_yr_list = os.listdir(p_j)
        for k in agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as file:
                data = json.load(file)
                districts = data['data']['districts']
                for district_data in districts:
                    district_name = district_data['name']
                    registered_users = district_data['registeredUsers']
                    clm['District_Name'].append(district_name)
                    clm['Registered_Users'].append(registered_users)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Successfully created a dataframe
top_user = pd.DataFrame(clm)

# To fetch data for Top_Insurance
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\top\\insurance\\country\\india\\state\\"
agg_state_list = os.listdir(path)

# List to store 
clm = {'State': [], 'Year': [], 'Quater': [], 'District_Name': [], 'Insurance_Count': [], 'Insurance_Value': []}

for i in agg_state_list:
    p_i = path + i + "/"
    agg_yr = os.listdir(p_i)
    for j in agg_yr:
        p_j = p_i + j + "/"
        agg_yr_list = os.listdir(p_j)
        for k in agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as file:
                data = json.load(file)
                districts = data['data']['districts']
                for district_data in districts:
                    district_name = district_data['entityName']
                    insurance_count = district_data['metric']['count']
                    insurance_amount = district_data['metric']['amount']
                    clm['District_Name'].append(district_name)
                    clm['Insurance_Count'].append(insurance_count)
                    clm['Insurance_Value'].append(insurance_amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Create a DataFrame
top_Insu = pd.DataFrame(clm)

# To fetch data for Map_Insurance
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\map\\insurance\\hover\\country\\india\\state\\"
agg_state_list = os.listdir(path)

# List to store 
clm = {'State': [], 'Year': [], 'Quater': [], 'District_Name': [], 'Insurance_Count': [], 'Insurance_Value': []}

for i in agg_state_list:
    p_i = path + i + "/"
    agg_yr = os.listdir(p_i)
    for j in agg_yr:
        p_j = p_i + j + "/"
        agg_yr_list = os.listdir(p_j)
        for k in agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as file:
                data = json.load(file)
                hover_data_list = data['data']['hoverDataList']
                for hover_data in hover_data_list:
                    district_name = hover_data['name']
                    insurance_count = hover_data['metric'][0]['count']
                    insurance_amount = hover_data['metric'][0]['amount']
                    clm['District_Name'].append(district_name)
                    clm['Insurance_Count'].append(insurance_count)
                    clm['Insurance_Value'].append(insurance_amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Create a DataFrame
map_insu = pd.DataFrame(clm)

# To fetch data for Aggerated_Insurance
path = "\\Users\\ronit\\OneDrive\\Desktop\\project\\pulse\\data\\aggregated\\insurance\\country\\india\\state\\"
agg_state_list = os.listdir(path)

# List to store 
clm = {'State': [], 'Year': [], 'Quater': [], 'Payment_Category': [], 'Transactions_Count': [], 'Transaction_Value': []}

for i in agg_state_list:
    p_i = path + i + "/"
    agg_yr = os.listdir(p_i)
    for j in agg_yr:
        p_j = p_i + j + "/"
        agg_yr_list = os.listdir(p_j)
        for k in agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as file:
                data = json.load(file)
                transaction_data = data['data']['transactionData']
                for transaction in transaction_data:
                    payment_category = transaction['name']
                    number_of_transactions = transaction['paymentInstruments'][0]['count']
                    total_value = transaction['paymentInstruments'][0]['amount']
                    clm['Payment_Category'].append(payment_category)
                    clm['Transactions_Count'].append(number_of_transactions)
                    clm['Transaction_Value'].append(total_value)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Create a DataFrame
agg_insu = pd.DataFrame(clm)

# To map data with Geo data so updating the state based on data sheet used for geomapping
import pandas as pd
from fuzzywuzzy import process

# Sample DataFrame with incorrect state names
 
Agg_Trans_new =Agg_Trans
Agg_user_new =Agg_user
agg_insu_new =agg_insu
map_Trans_new =map_Trans
map_user_new =map_user
map_insu_new =map_insu
top_Trans_new =top_Trans
top_user_new =top_user
top_Insu_new =top_Insu

# Correct list of state names
correct_state_names = [
    'Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
    'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana',
    'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Madhya Pradesh',
    'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
    'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'
]

# Function to find the best match for each state name
def find_best_match(state_name):
    return process.extractOne(state_name, correct_state_names)[0]

# Replace incorrect state names with correct names using approximate matching
Agg_Trans_new['State'] = Agg_Trans_new['State'].apply(find_best_match)
Agg_user_new['State'] = Agg_user_new['State'].apply(find_best_match)
agg_insu_new['State'] = agg_insu_new['State'].apply(find_best_match)
map_Trans_new['State'] = map_Trans_new['State'].apply(find_best_match)
map_user_new ['State'] = map_user_new ['State'].apply(find_best_match)
map_insu_new['State'] = map_insu_new['State'].apply(find_best_match)
top_Trans_new['State'] = top_Trans_new['State'].apply(find_best_match)
top_user_new['State'] = top_user_new['State'].apply(find_best_match)
top_Insu_new['State'] = top_Insu_new['State'].apply(find_best_match)

import mysql.connector
import pandas as pd
import numpy as np

# Establish connection to MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root',
    database='project'
)

cursor = mydb.cursor()

#TABLE Aggregated_Transaction

# Convert all columns to Python native types
Agg_Trans_new['Year'] = Agg_Trans_new['Year'].astype('int')
Agg_Trans_new['Quater'] = Agg_Trans_new['Quater'].astype('int')
Agg_Trans_new['Transaction_count'] = Agg_Trans_new['Transaction_count'].astype('int')
Agg_Trans_new['Transaction_amount'] = Agg_Trans_new['Transaction_amount'].astype('float')

# Create table query
query = """
    CREATE TABLE Aggregated_Transaction (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quarter INT,
        Transaction_type VARCHAR(256),
        Transaction_count INT,
        Transaction_amount FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Insert data into MySQL table
for i in range(len(Agg_Trans_new['State'])):
    insert_query = "INSERT INTO Aggregated_Transaction (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (
        Agg_Trans_new.iloc[i]['State'],
        int(Agg_Trans_new.iloc[i]['Year']),  # Convert to Python int type
        int(Agg_Trans_new.iloc[i]['Quater']),  # Convert to Python int type
        Agg_Trans_new.iloc[i]['Transaction_type'],
        int(Agg_Trans_new.iloc[i]['Transaction_count']),  # Convert to Python int type
        float(Agg_Trans_new.iloc[i]['Transaction_amount'])  # Convert to Python float type
    )
    cursor.execute(insert_query, data)

# Commit the changes
mydb.commit()

#TABLE Aggregated_User
# Create table query
query = """
    CREATE TABLE Aggregated_User (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quarter VARCHAR(256),
        Registered_Users INT,
        Count_App_Opens INT,
        Brand VARCHAR(256),
        Brand_Count INT,
        Brand_Percentage FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Convert numeric columns to Python int or float
Agg_user_new['Year'] = Agg_user_new['Year'].astype(int)
Agg_user_new['Registered_Users'] = Agg_user_new['Registered_Users'].astype(int)
Agg_user_new['Count_App_Opens'] = Agg_user_new['Count_App_Opens'].astype(int)
Agg_user_new['Brand_Count'] = Agg_user_new['Brand_Count'].astype(int)
Agg_user_new['Brand_Percentage'] = Agg_user_new['Brand_Percentage'].astype(float)

# Insert data into MySQL table
for i in range(len(Agg_user_new)):
    insert_query = """INSERT INTO Aggregated_User (State, Year, Quarter, Registered_Users, 
                    Count_App_Opens, Brand, Brand_Count, Brand_Percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    data = (
        str(Agg_user_new.iloc[i]['State']),
        int(Agg_user_new.iloc[i]['Year']),  
        str(Agg_user_new.iloc[i]['Quarter']),  
        int(Agg_user_new.iloc[i]['Registered_Users']),
        int(Agg_user_new.iloc[i]['Count_App_Opens']),  
        str(Agg_user_new.iloc[i]['Brand']),
        int(Agg_user_new.iloc[i]['Brand_Count']),  
        float(Agg_user_new.iloc[i]['Brand_Percentage'])
    )
    cursor.execute(insert_query, data)
    mydb.commit()

#TABLE Aggregated_insurance
# Create table query
query = """
    CREATE TABLE Aggregated_insurance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        Payment_Category varchar(256),
        Transactions_Count INT,
        Transaction_Value FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Convert numeric columns to Python int or float
agg_insu_new['Year'] = agg_insu_new['Year'].astype(int)
agg_insu_new['Transactions_Count'] = agg_insu_new['Transactions_Count'].astype(int)
agg_insu_new['Transaction_Value'] = agg_insu_new['Transaction_Value'].astype(float)

# Insert data into MySQL table
for i in range(len(agg_insu_new)):
    insert_query = """INSERT INTO Aggregated_insurance (State, Year, Quater, Payment_Category, 
                    Transactions_Count, Transaction_Value) VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (
        str(agg_insu_new.iloc[i]['State']),
        int(agg_insu_new.iloc[i]['Year']),  
        int(agg_insu_new.iloc[i]['Quater']),  # Corrected column name
        str(agg_insu_new.iloc[i]['Payment_Category']),
        int(agg_insu_new.iloc[i]['Transactions_Count']),  
        float(agg_insu_new.iloc[i]['Transaction_Value'])
    )
    cursor.execute(insert_query, data)
    mydb.commit()
	
#TABLE Map_Transaction
# Convert all columns to Python native types
map_Trans_new['Year'] = map_Trans_new['Year'].astype('int')
map_Trans_new['Quater'] = map_Trans_new['Quater'].astype('int')
map_Trans_new['No_Of_Transaction'] = map_Trans_new['No_Of_Transaction'].astype('int')
map_Trans_new['Transaction_Amount'] = map_Trans_new['Transaction_Amount'].astype('float')

# Create table query
query = """
    CREATE TABLE Map_Transaction (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        District_Name VARCHAR(256),
        Transaction_count INT,
        Transaction_amount FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Insert data into MySQL table
for i in range(len(map_Trans_new['State'])):
    insert_query = "INSERT INTO Map_Transaction (State, Year, Quater, District_Name, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (
        str(map_Trans_new.iloc[i]['State']),
        int(map_Trans_new.iloc[i]['Year']),  # Convert to Python int type
        int(map_Trans_new.iloc[i]['Quater']),  # Convert to Python int type
        str(map_Trans_new.iloc[i]['District_Name']),
        int(map_Trans_new.iloc[i]['No_Of_Transaction']),  # Convert to Python int type
        float(map_Trans_new.iloc[i]['Transaction_Amount'])  # Convert to Python float type
    )
    cursor.execute(insert_query, data)
    mydb.commit()

#TABLE Map_User
# Create table query
query = """
    CREATE TABLE Map_User (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        District_Name VARCHAR(256),
        Registered_Users INT,
        Count_App_Opens INT
    )
"""

# Execute table creation query
cursor.execute(query)

# Convert numeric columns to Python int or float
map_user_new['Year'] = map_user_new['Year'].astype(int)
map_user_new['registeredUsers'] = map_user_new['registeredUsers'].astype(int)
map_user_new['appOpens'] = map_user_new['appOpens'].astype(int)

# Insert data into MySQL table
for i in range(len(map_user_new)):
    insert_query = """INSERT INTO Map_User (State, Year, Quater,District_Name, Registered_Users, 
                    Count_App_Opens) VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (
        str(map_user_new.iloc[i]['State']),
        int(map_user_new.iloc[i]['Year']),  
        str(map_user_new.iloc[i]['Quater']),
        str(map_user_new.iloc[i]['District_Name']),
        int(map_user_new.iloc[i]['registeredUsers']),
        int(map_user_new.iloc[i]['appOpens'])
    )
    cursor.execute(insert_query, data)
    mydb.commit()

#TABLE Map_insurance
# Create table query
query = """
    CREATE TABLE Map_insurance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        District_Name varchar(256),
        Insurance_Count INT,
        Insurance_Value FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Convert numeric columns to Python int or float
map_insu_new['Year'] = map_insu_new['Year'].astype(int)
map_insu_new['Insurance_Count'] = map_insu_new['Insurance_Count'].astype(int)
map_insu_new['Insurance_Value'] = map_insu_new['Insurance_Value'].astype(float)

# Insert data into MySQL table
for i in range(len(map_insu_new)):
    insert_query = """INSERT INTO Map_insurance (State, Year, Quater, District_Name, 
                    Insurance_Count,Insurance_Value) VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (
        str(map_insu_new.iloc[i]['State']),
        int(map_insu_new.iloc[i]['Year']),  
        int(map_insu_new.iloc[i]['Quater']), 
        str(map_insu_new.iloc[i]['District_Name']),
        int(map_insu_new.iloc[i]['Insurance_Count']),  
        float(map_insu_new.iloc[i]['Insurance_Value'])
    )
    cursor.execute(insert_query, data)
    mydb.commit()

#TABLE Top_Transaction
# Convert all columns to Python native types
top_Trans_new['Year'] = top_Trans_new['Year'].astype('int')
top_Trans_new['Quater'] =top_Trans_new['Quater'].astype('int')
top_Trans_new['Transaction_Count'] = top_Trans_new['Transaction_Count'].astype('int')
top_Trans_new['Transaction_Amount'] = top_Trans_new['Transaction_Amount'].astype('float')

# Create table query
query = """
    CREATE TABLE Top_Transaction (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        District_Name VARCHAR(256),
        Transaction_count INT,
        Transaction_amount FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Insert data into MySQL table
for i in range(len(top_Trans_new['State'])):
    insert_query = "INSERT INTO Top_Transaction (State, Year, Quater, District_Name, Transaction_Count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (
        str(top_Trans_new.iloc[i]['State']),
        int(top_Trans_new.iloc[i]['Year']),  # Convert to Python int type
        int(top_Trans_new.iloc[i]['Quater']),  # Convert to Python int type
        str(top_Trans_new.iloc[i]['District_Name']),
        int(top_Trans_new.iloc[i]['Transaction_Count']),  # Convert to Python int type
        float(top_Trans_new.iloc[i]['Transaction_Amount'])  # Convert to Python float type
    )
    cursor.execute(insert_query, data)
    mydb.commit()

#TABLE Top_User
# Create table query
query = """
    CREATE TABLE Top_User (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        District_Name VARCHAR(256),
        Registered_Users INT
    )
"""

# Execute table creation query
cursor.execute(query)

# Convert numeric columns to Python int or float
top_user_new['Year'] = top_user_new['Year'].astype(int)
top_user_new['Registered_Users'] = top_user_new['Registered_Users'].astype(int)

# Insert data into MySQL table
for i in range(len(top_user_new)):
    insert_query = """INSERT INTO Top_User (State, Year, Quater,District_Name, Registered_Users) 
                     VALUES (%s, %s, %s, %s, %s)"""
    data = (
        str(top_user_new.iloc[i]['State']),
        int(top_user_new.iloc[i]['Year']),  
        int(top_user_new.iloc[i]['Quater']),
        str(top_user_new.iloc[i]['District_Name']),
        int(top_user_new.iloc[i]['Registered_Users'])
    )
    cursor.execute(insert_query, data)
    mydb.commit()

#TABLE Top_insurance
# Create table query
query = """
    CREATE TABLE Top_insurance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        State VARCHAR(256),
        Year INT,
        Quater INT,
        District_Name varchar(256),
        Insurance_Count INT,
        Insurance_Value FLOAT
    )
"""

# Execute table creation query
cursor.execute(query)

# Convert numeric columns to Python int or float
top_Insu_new['Year'] = top_Insu_new['Year'].astype(int)
top_Insu_new['Insurance_Count'] = top_Insu_new['Insurance_Count'].astype(int)
top_Insu_new['Insurance_Value'] = top_Insu_new['Insurance_Value'].astype(float)

# Insert data into MySQL table
for i in range(len(top_Insu_new)):
    insert_query = """INSERT INTO Top_insurance (State, Year, Quater, District_Name, 
                    Insurance_Count,Insurance_Value) VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (
        str(top_Insu_new.iloc[i]['State']),
        int(top_Insu_new.iloc[i]['Year']),  
        int(top_Insu_new.iloc[i]['Quater']), 
        str(top_Insu_new.iloc[i]['District_Name']),
        int(top_Insu_new.iloc[i]['Insurance_Count']),  
        float(top_Insu_new.iloc[i]['Insurance_Value'])
    )
    cursor.execute(insert_query, data)
    mydb.commit()
