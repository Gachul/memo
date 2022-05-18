import requests
import argparse

def azure_login(uid, upw):
    datas = {'username':uid, 'password':upw,
            'grant_type' : 'password', 'scope':'openid 485d3a94-71ca-4e75-8cb5-1c067b07f91b offline_access',
            'client_id':'485d3a94-71ca-4e75-8cb5-1c067b07f91b', 'response_type':'token id_token'}

    url_form = "https://{tenant}.b2clogin.com/{tenant}.onmicrosoft.com/{policy}/oauth2/v2.0/token"

    req_url = url_form.format(tenant = 'entrolink2', policy = 'B2C_1A_ROPC_Auth')

    req = requests.post(url = req_url, data = datas)

    return req.status_code
        
def main():
    arp = argparse.ArgumentParser(description = 'Azure Login Status')
    arp.add_argument('E', type = str, help = 'Azure Login ID', nargs = '+')
    
    args = arp.parse_args()
    
    azid, azpw = args.E[0], args.E[1]
    
    is_exist = azure_login(azid, azpw)
    
    print(is_exist)

    
main()