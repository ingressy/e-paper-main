# needs an .env file with the login data

import datetime, os, webuntis.objects, logging
from dotenv import load_dotenv

#loading data from the .env
load_dotenv()
SRV = os.getenv('SRV')
USR = os.getenv('USR')
PWD = os.getenv('PWD')
SHO = os.getenv('SHO')
USRA = os.getenv('USRA')

time = datetime.datetime.now()
chtime = (time.strftime("%H%M"))
chdate = (time.strftime("%Y-%m-%d"))
start = datetime.datetime.now()
end = start + datetime.timedelta(days=5)

def main():
    pass

if __name__ == "__main__":
    main()