'''crud de admin'''

'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)
 
UPDATE AND DELETE NEED A WHERE CLAUSE *
'''
from database import con
import os

def main_menu():
    print(":::MAIN MENU:::")
    print("[1]. Create user")
    print("[2]. List user")
    print("[3]. Salir")
    opt = int(input('Press any option: '))
    return opt
    
    
def create_user():
    new_user_query = '''
    INSERT INTO users (username, email, password)
        VALUES('Tatiana C', 'Tativas187@gmail.com', '12345')
    '''
    
    con.execute(new_user_query)
    con.commit()
    
    print('User create succesfully.') 
    os.system('pause')

    con.close()
    
create_user()