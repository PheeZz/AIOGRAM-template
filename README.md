# Setup

>Note: if you know how to setup venv go to step 4

1. Setup your virtualenv<br/>
`python -m venv .venv`

2. Next step activate it<br/>
 - On linux systems:<br/>
`source .venv/bin/activate`

 - On Windows:<br/>
`.venv\Scripts\activate`

3. Download required libs<br/>
`pip install -r requirements.txt`

4. Create .env file in `data\.env` with BOT_TOKEN

5. Launch bot in `app.py` file

6. Sample .service file
   
   Path: `/etc/systemd/system/telegram-bot.service` </br>
   Code: (if you using python 3.10)</br>
   ```
    [Unit]
    Description='Service for my new bot'
    After=network.target

    [Service]
    Type=idle
    Restart=on-failure
    User=root
    ExecStart=/bin/bash -c 'cd ~/telegram-bot/ && source .venv/bin/activate && python3.10 app.py'

    [Install]
    WantedBy=multi-user.target
   ```