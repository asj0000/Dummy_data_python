import string
import psycopg2


#Connect to DB
def db_connect():
        conn = psycopg2.connect(database="defaultdb", 
                                      user="avnadmin", 
                                      password="",
                                      host="vivek-tree-vivek-tree.e.aivencloud.com", 
                                      port=15050)    
        return conn

#Function to delete dummy data
def delete_dummy_data(entity_name):
    conn = db_connect()
    
    if(entity_name == 'sites'):
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM "14trees_old".sites s WHERE s.id IN (select s.id from "14trees_old".sites s where s.name_marathi like \'Test Random Site%\' order by s.created_at desc limit 10)')
            print('Deleted dummy sites successfully')
            connection.close()
    
        except Exception as e:
            print(f"An error occured{e}")
            connection.close() 
    
    elif (entity_name == 'plots'):
          cursor = conn.cursor()
          try:
              cursor.execute('DELETE FROM "14trees_old".plots p WHERE p.id IN (select p.id from "14trees_old".plots p where p.plot_id  like \'dummy_plot_id%\' order by p.created_at desc limit 100)')
              print('Deleted Dummy Plots')
              connection.close()
           
          except Exception as e:
              print(f"An error occured {e}")
              connection.close()
    
    elif (entity_name == 'trees'):
          cursor = conn.cursor()   
          try:
              cursor.execute('DELETE FROM "14trees_old".trees t WHERE t.id IN (select t.id from "14trees_old".trees t where t.planted_by  like \'DataAutomation\' order by t.created_at desc limit 1000)')
              print("Deleted dummy trees ")
              connection.close()
          except Exception as e:
              print(f"An error occured {e}")
              connection.close()
              
    elif (entity_name == 'users'):
          cursor = conn.cursor()
          try:
              cursor.execute('DELETE FROM "14trees_old".users where u.user_id like \'dummy%\' order by u.created_at desc') 
              print("Deleted dummy users")
              connection.close()
          except Exception as e:
              print(f"An error occured {e}")
              connection.close()
              
    elif (entity_name == 'visits'):
          cursor= conn.cursor()
          try:
              cursor.execute('DELETE from "14trees_old".visits v where v.visit_name like \'dummy-visit%\' ')   
              print('Deleted dummy visits')
              connection.close()
          
          except Exception as e:
             print(f'An error occured {e}')
             connection.close()
             
    else:
         print('Provide a valid entity name')
         return         
         

