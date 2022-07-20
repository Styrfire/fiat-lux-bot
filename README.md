# Fiat Lux Bot

## Installing pm2

1. Update repos ```apt update && apt upgrade```
2. Make sure npm is installed ```npm --version```
    1. If not, install npm ```apt install npm```
3. Install pm2 ```npm install pm2 -g```

## Installation and running on a server:

1. Install required pip modules by running: ```pip install -r requirements.txt```
2. Create .env file and set environment variables:
    1. In the same directory as start.py, run ```echo > .env``` to create an empty .env file
    2. Edit this .env file to include the following lines:<br>
    ```BOT_TOKEN={bot token for server}```<br>
3. Copy service account credentials json to ```fiat-lux-bot/google_credentials/service_account.json``` inside the project<br>
4. Create the bot app in pm2: ```pm2 start start.py --name="bot" --interpreter="python3"```
- Start the bot with: ```pm2 start bot``` 
- Restart the bot with: ```pm2 restart bot```
- Stop the bot with ```pm2 stop bot```
- Delete the bot with ```pm2 delete bot```

## Installation and running on PyCharm:

1. Clone repository into the workspace<br>
2. Install required pip modules<br>
3. In the Run Configuration Environment Variables add:<br>
   ```BOT_TOKEN={bot token for server}```<br>
4. Copy service account credentials json to ```fiat-lux-bot/google_credentials/service_account.json``` inside the project<br>
5. Stop any running Fiat Lux bot (if active on another server)
6. Run the bot!

## Available supported commands:
#### Anyone:
| command           | description                      |
|-------------------|----------------------------------|
| ^example_command  | Does some stuff                  |
| ^test_spreadsheet | Tests the google spreadsheet api |
