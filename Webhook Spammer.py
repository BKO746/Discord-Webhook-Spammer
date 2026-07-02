import requests


art = """
                                                                      
 _ _ _     _   _           _        _____                             
| | | |___| |_| |_ ___ ___| |_     |   __|___ ___ _____ _____ ___ ___ 
| | | | -_| . |   | . | . | '_|    |__   | . | .'|     |     | -_|  _|
|_____|___|___|_|_|___|___|_,_|    |_____|  _|__,|_|_|_|_|_|_|___|_|  
                                         |_|                             
"""
print(art)
message = input("Enter your message: ")
webhook = input("Enter your webhook URL: ")
times = int(input("Enter the number of times to send the message: ")) 

payload = {
    'username': 'Administrator Bot',
    'content': message
}
for _ in range(times):
    requests.post(webhook, json=payload)