import requests
import sys
from collections import OrderedDict
from urllib.parse import urlencode
requests.packages.urllib3.disable_warnings()


def get_info(question):
    """
    Args:
        question (str): question to ask user for input
    
    Returns:
        string of user input
    """
    while True:
        value = input(question)
        if value == '':
            continue
        else:
            return value

def login(tenant_id, client_key, secret_key):
    """
    Args:
        tenant_id (str): Under: Azure Active Directory | 
                         Properties | labeled "Directory ID"
                         
        client_key (str): Under app registration and labeled 
                           "Application ID"

        secret_key (str): Accessible only one time after the 
                           App has been registered
    """
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    auth_url = 'https://login.microsoftonline.com/{}/oauth2/token'.format(tenant_id)
    resource = 'https://manage.office.com'
    data = ('grant_type=client_credentials&client_id={}'
            '&client_secret={}&resource={}'.format(client_key,
                                                     secret_key,
                                                     resource))
    r = requests.post(auth_url, headers=headers, data=data, verify=False)
    resp = r.json()

    try:
        headers['Authorization'] = 'bearer ' + resp['access_token']
        return headers
    except KeyError:
        print('Authentication failure: ', resp)
        sys.exit(1)

def get_sub_status(headers, tenant_id):        
    """
    Args:
        headers (dict): auth headers
        tenant_id (str): Under: Azure Active Directory | 
                           Properties | labeled "Directory ID"
    """
    list_subs_url = ('https://manage.office.com/api/v1.0/{}'
                     '/activity/feed/subscriptions/list'.format(tenant_id))
    status = requests.get(list_subs_url, headers=headers, verify=False)
    return status.json()

def set_sub_status(tenant_id, headers, ctype_stat):
    """
    Args:
        headers (dict): authentication headers for session
        ctype_stat (tuple): content type, status (enabled | disabled)
    
    Returns:
        dict 
    """
    if ctype_stat[1] == 'enabled':
        action = 'stop'
    elif ctype_stat[1] == 'disabled':
        action = 'start'

    sub_url = ('https://manage.office.com/api/v1.0/{}'
                 '/activity/feed/subscriptions/{}'
                 '?contentType={}'.format(tenant_id, action, ctype_stat[0]))
    status = requests.post(sub_url, headers=headers, verify=False)
    
def main():
            
    print('=' * 60)
    print('This script will enable or disable Office 365 subscriptions.')
    print('=' * 60)
    print('Please enter the required data.\n')

    print(('The Tenant ID is listed under Azure Active Directory | '
            'Properties and labeled "Directory ID".\nExample: '
            'cb6997bf-4029-455f-9f7a-e76fee8881da\n'))
    tenant_id = get_info('Enter Tenant ID: ')
            
    print(('\nThe Client Key is available after app registration and labeled "Application ID"'
            'App Registrations | <ESM App Name> | Application ID'
            '\nExample: '
            '553dd2ba-251b-47d5-893d-2f7ab26adf19\n'))
    client_key = get_info('Enter Client Key: ')
    
    print(('\nThe Secret Key is accessible only one time after the App has been registered:'
            '\nExample: '
            'D8perHbL9gAqx4vx5YbuffCDsvz2Pbdswey72FYRDNk=\n'))
    secret_key = get_info("Enter Secret Key: ")
    secret_key = secret_key.replace('+', '%2B')
    
    headers = login(tenant_id, client_key, secret_key)

    c = OrderedDict()
    while True:
        c['Audit.AzureActiveDirectory'] = 'disabled'
        c['Audit.Exchange'] = 'disabled'
        c['Audit.General'] = 'disabled' 
        c['Audit.SharePoint'] = 'disabled'
        c['DLP.All'] ='disabled'                

        status = get_sub_status(headers, tenant_id)
        if status != '':
            try:
                for s in status:
                    c[s['contentType']] = s['status']
            except (KeyError, TypeError):
                print('Error: ', status['error']['message'])
                sys.exit(1)
            
        print('\nEnter 1-5 to enable/disable subscriptions or 0 to exit')
        for idx, (c_type, status) in enumerate(c.items(), 1):
            print('{}. {}: {}'.format(idx, c_type, status))
        
        try:
            choice = int(get_info('Enter 0-5: '))
        except ValueError:
            continue
        menu = list(c.items())        
        if 1 <= choice <= 5:
            set_sub_status(tenant_id, headers, menu[choice - 1])
            continue
        elif choice == 6:
            continue
        elif choice == 0:
            break
        else:
            continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Control-C Pressed, stopping...")
        sys.exit()
