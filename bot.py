#################################
#
#   This is Mr ASR
#   mrasr_@wearehackerone.com
#
#################################

import os
import random
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from email_validator import validate_email, EmailNotValidError

os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pilihsource = i1 = input(bcolors.OKGREEN + '\nPilih Data [1. listEmail.txt] [2. Random gmail] [3. Random homail] : ')
namafile = ''
if int(pilihsource) == 1 :
    namafile = input('Silahkan isi nama file [pastikan file ada ditempat yang sama] : ')
    try:
        with open(namafile, 'r') as file:
            email_addresses = [line.strip() for line in file]
    except:
        input(bcolors.FAIL + 'FILE ' + namafile + ' NOT FOUND! [Press any Keys to Quit]')
        quit()
num_requests = i1 = input(bcolors.OKGREEN + 'Isi jumlah request yang ingin dikirim : ')
reffcode = i1 = input(bcolors.OKGREEN + 'Kode Refferaal : ')

def generate_random_name():
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Sophia", "Daniel", "Olivia", "William", "Ava", "Ethan", "Emma", "Liam", "Mia", "Noah", "Isabella", "James", "Abigail", "Benjamin", "Charlotte", "Alexander", "Harper", "Henry", "Amelia", "Jackson", "Ella", "Sebastian", "Scarlett", "Aiden", "Luna", "Matthew", "Grace", "Samuel", "Chloe", "Joseph", "Victoria", "Gabriel", "Zoe", "Apple", "Tiger", "Rose", "Lion", "Daisy", "Bear", "Lily", "Eagle", "Poppy", "Wolf", "River", "Bee", "Phoenix", "Robin", "Hawk", "Sky", "Raven", "Ocean", "Fox", "Leaf", "Sunny", "Star", "Snow", "Maple", "Willow", "Breeze", "Rain", "Meadow", "Shadow", "Storm", "Hope", "Autumn", "Coco", "Sapphire", "Buddy", "Sunny", "Lucky", "Angel", "Frost", "Blue", "Ruby", "Dolphin", "Pearl", "Cheetah", "Cedar", "Rocky", "Jade", "Orca", "Maple", "Brick", "Falcon", "Rainbow", "Bamboo", "Blaze", "Wren", "Slate", "Willow", "Coral", "Phoenix", "Jasper", "Jane", "Michael", "Emily", "David", "Sophia", "Daniel", "Olivia", "William", "Ava", "Ethan", "Emma", "Liam", "Mia", "Noah", "Isabella", "James", "Abigail", "Benjamin", "Charlotte", "Alexander", "Harper", "Henry", "Amelia", "Jackson", "Ella", "Sebastian", "Scarlett", "Aiden", "Luna", "Matthew", "Grace", "Samuel", "Chloe", "Joseph", "Victoria", "Gabriel", "Zoe"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Taylor", "Anderson", "Hernandez", "Lopez", "Walker", "White", "Carter", "Wright", "Allen", "Young", "Scott", "Lee", "King", "Green", "Hall", "Adams", "Nelson", "Baker", "Hill", "Rivera", "Cook", "Mitchell", "Cruz", "Perez", "Roberts", "Turner", "Phillips", "Reed", "Campbell", "Evans", "Stewart"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"

def generate_random_email_ho(name):
    domain = "@wearehackerone.com"
    return name.replace(" ", "").lower() + domain

def generate_random_email_google(name):
    domain = "@gmail.com"
    num = random.randint(10,99)
    return name.replace(" ", "").lower() + str(num) + domain

for _ in range(int(num_requests)):
    url = 'https://getlaunchlist.com/s/QZhvlk?ref=' + str(reffcode)
    
    random_name = generate_random_name()

    try:
        data_email = ''
        if int(pilihsource) == 1 :
            random_email_2 = random.choice(email_addresses)
            data_email = random_email_2
        elif int(pilihsource) == 2 :
            random_email_1 = generate_random_email_google(random_name)
            data_email = random_email_1
        else :
            random_email_0 = generate_random_email_ho(random_name)
            data_email = random_email_0
        
        multipart_data = MultipartEncoder(
            fields={
                'email': data_email,
            }
        )
        emailinfo = validate_email(data_email, check_deliverability=True)
    except EmailNotValidError as e:
        input(str(e) + ' [Press any Keys to Exit]')
        break

    headers = {
        'Host': 'getlaunchlist.com',
        'Sec-Ch-Ua': '',
        'Accept': 'application/json',
        'Content-Type': multipart_data.content_type,
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36',
        'Sec-Ch-Ua-Platform': '',
        'Origin': 'https://wallet.joinfire.xyz',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://wallet.joinfire.xyz/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.post(url, data=multipart_data, headers=headers)
    print(bcolors.WARNING +'Send Request Success with email : ' + data_email + '\n' + bcolors.OKGREEN + response.json()["embeddedLink"])

input('Press any Key to Exit')
