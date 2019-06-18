import pymongo as client
client = client.MongoClient(host='localhost:27017')
db = client["landmaster-database"]
data = db.data
arr_data =[
    {
        'X coordinate': 4.000, 
        'Y courdinate': 7.000,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },
    {   
        'X coordinate': 4.500, 
        'Y courdinate': 7.500,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
         
    },
    {
    
        'X coordinate': 5.000, 
        'Y courdinate': 8.000,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },
    {
        
        'X coordinate': 5.500, 
        'Y courdinate': 8.500,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 6.000, 
        'Y courdinate': 8.000,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 6.500, 
        'Y courdinate': 8.500,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 7.000, 
        'Y courdinate': 9.000,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 7.500, 
        'Y courdinate': 9.500,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 8.000, 
        'Y courdinate': 10.000,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 8.500, 
        'Y courdinate': 10.5,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },{
        
        'X coordinate': 9.000, 
        'Y courdinate': 11.000,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    },
    {
        
        'X coordinate': 9.500, 
        'Y courdinate': 11.500,
        'name of town': "Kumasi",
        'Region': 'Ashanti'
    }
]
result = data.insert_many(arr_data)
print(result.inserted_ids)