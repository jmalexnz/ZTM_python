import requests
import hashlib
import sys

# password = password123
# may want to read from txt file instead of cmd argument
# as some cmd tools store what is entered.
# store passwords in hashes instead of plaintext
# k-anonymity 
# only give first 5 characters of hashed passwords
# then the API will never know the full hash
# we can then figure out which refer to our password

def request_api_data(query_char):
    '''
    get response from website from 5-char hash

    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    '''
    read response
    '''
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    '''
    convert password to sha1
    '''
    # convert to required format
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    num_leaks = get_password_leaks_count(response, tail)
    return num_leaks

def main(args):
    '''
    Iterate over the passwords
    '''
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You should probably change it.')
        else:
            print(f"{password} not found. Carry on.")
    print('Password checks complete.')
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
