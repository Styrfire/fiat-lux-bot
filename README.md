# Fiat Lux Bot

## Installing pm2

1. Update repos ```apt update && apt upgrade```
2. Make sure npm is installed ```npm --version```
    1. If not, install npm ```apt install npm```
3. Install pm2 ```npm install pm2 -g```

## Running (Do not follow these steps for deploying on the server):

1. Install required pip modules by running: ```pip install -r requirements.txt```
2. Create .env file and set environment variables:
    1. In the same directory as start.py, run ```echo > .env``` to create an empty .env file
    2. Edit this .env file to include the following lines:<br>
    BOT_TOKEN={bot token for server}<br>
3. Copy the files from the ```sqlite_templates``` folder to a new ```sqldb``` folder in the ```/root``` or ```~``` directory
4. Create the bot app in pm2: ```pm2 start start.py --name="bot" --interpreter="python3"```
- Start the bot with: ```pm2 start bot``` 
- Restart the bot with: ```pm2 restart bot```
- Stop the bot with ```pm2 stop bot```
- Delete the bot with ```pm2 delete bot```

## Available supported commands:
#### Anyone:
| command                  | description        |
|--------------------------|--------------------|
| ^example_command         | Does some stuff    |
| ^another_example_command | Does lots of stuff |
