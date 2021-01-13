import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200 :
       raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_passord_leask_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    
def pwned_api_check(password):
    sha1pass = hashlib.sha1(str(password).encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pass[:5],sha1pass[5:]
    # print(get_passord_leask_count(request_api_data(first5_char),tail))
    return get_passord_leask_count(request_api_data(first5_char),tail)

def main(args):
    print(f'************************ \t starting program ... \t ************************')
    for password in args:
        count = pwned_api_check(password)
        if(count):
            print(f'{password} has been found {count} time ... You shoud probably change it\n')
        else:
            print(f'{password} not found ... you are good to go\n')
    print(f'************************ \t done ! \t ************************')
main(sys.argv[1:])