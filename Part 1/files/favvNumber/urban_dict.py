from pathlib import Path
import json
def get_usr():
    get_path = Path('usr_info.json')
    store_data = {}
    if not get_path.exists():
        get_usr_name = input('Welcome to our Website\nEnter your username:\n')
        get_email_id = input('Enter your email id with which you wanna register:\n')
        get_phone_numba = input('Enter your phone number so we could send you a verification code\n')
        store_data['usr_name'] = get_usr_name
        store_data['usr_email'] = get_email_id
        store_data['usr_phone_no'] = get_phone_numba

        get_path.write_text(json.dumps(store_data))

        print(store_data)

        
    else:
        stored_data = json.loads(get_path.read_text())
        get_welcome = input('welcome back!\n Enter your username:\n')
        if get_welcome == stored_data['usr_name']:
            print(f"Welcome Back!! {stored_data['usr_name']}")
        else:
            print('Your ass is fake')
    
get_usr()
