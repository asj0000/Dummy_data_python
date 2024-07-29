


#Function to delete dummy data
def delete_dummy_data(conn, entity_name):
    cursor = conn.cursor()

    if(entity_name == 'sites'):
        try:
            cursor.execute('DELETE FROM "14trees_2".sites s WHERE s.id IN (select s.id from "14trees_2".sites s where s.name_marathi like \'Test Random Site%\' order by s.created_at desc limit 10)')
            print('Deleted dummy sites successfully')
        except Exception as e:
            print(f"An error occured{e}")
    
    elif (entity_name == 'plots'):
          try:
              cursor.execute('DELETE FROM "14trees_2".plots p WHERE p.id IN (select p.id from "14trees_2".plots p where p.plot_id  like \'dummy_plot_id%\' order by p.created_at desc limit 100)')
              print('Deleted Dummy Plots')
           
          except Exception as e:
              print(f"An error occured {e}")
    
    elif (entity_name == 'trees'):
          try:
              cursor.execute('DELETE FROM "14trees_2".trees t WHERE t.planted_by =  \'DataAutomation\'')
              print("Deleted dummy trees ")
          except Exception as e:
              print(f"An error occured {e}")
              
    elif (entity_name == 'users'):
          try:
              cursor.execute('DELETE FROM "14trees_2".users u where u.user_id like \'dummy%\'') 
              print("Deleted dummy users")
          except Exception as e:
              print(f"An error occured {e}")
              
    elif (entity_name == 'visits'):
          try:
              cursor.execute('DELETE from "14trees_2".visits v where v.visit_name like \'Dummy%\' ')   
              print('Deleted dummy visits')
          
          except Exception as e:
             print(f'An error occured {e}')

    elif (entity_name == 'organisations'):
          try:
              cursor.execute('delete from "14trees_2"."groups" g where  g."name" like \'Dummy%\' ')   
              print('Deleted dummy organisations')
          
          except Exception as e:
             print(f'An error occured {e}')


    elif (entity_name == 'donations'):
          try:
              cursor.execute('delete from "14trees_2".donations d where  d."Name" like \'dummy%\'  ')   
              print('Deleted dummy donations')
          
          except Exception as e:
             print(f'An error occured {e}')

    elif (entity_name == 'visit_users'):
          try:
              cursor.execute('Delete FROM "14trees_2".visit_users v WHERE v.visit_id in (select v.id from "14trees_2".visits v where v.visit_name like \'Dummy%\')')   
              print('Deleted dummy visit users')
          
          except Exception as e:
             print(f'An error occured {e}')
             
            

    elif (entity_name == 'org_users'):
          try:
              cursor.execute('Delete FROM "14trees_2".user_groups ug WHERE ug.group_id in (select g.id from "14trees_2"."groups" g where  g."name" like \'Dummy%\' )')   
              print('Deleted dummy org users ')
          
          except Exception as e:
             print(f'An error occured {e}')
    
    elif (entity_name == 'ponds'):
          try:
              cursor.execute('Delete FROM "14trees_2".ponds p WHERE p.name like \'Test Random Pond%\' ')   
              print('Deleted dummy ponds ')
          
          except Exception as e:  
               print(f'An error occured {e}')  
               
    elif (entity_name == 'pond_water_level'):
          try:
              cursor.execute('Delete from "14trees_2".pond_water_level pwl  where pwl.pond_id  in (select p.id from "14trees_2".ponds p where p.name like \'Test Random Pond%\' order by p.created_at desc limit 1000 )')   
              print('Deleted dummy pond water level ')
          
          except Exception as e:
             print(f'An error occured {e}')            
               
    elif (entity_name == 'visit_images'):
          try:
              cursor.execute('Delete FROM "14trees_2".ponds p WHERE p.name like \'Test Random Pond%\' ')   
              print('Deleted dummy visit images ')
          
          except Exception as e:  
               print(f'An error occured {e}')
               
    elif (entity_name == 'tree_snapshots'):
          try:
              cursor.execute('Delete FROM "14trees_2".trees_snapshots ts WHERE ts.user_id in (select u.id from "14trees_2".users u where u.name like \'dummy%\' order by u.created_at DESC limit 1000) ')   
              print('Deleted dummy tree snapshots ')
          
          except Exception as e:  
               print(f'An error occured {e}')     
                                       
    else:
         print('Provide a valid entity name')
         return         
    
    conn.commit()
         

