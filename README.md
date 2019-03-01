# Pocket to Slack

## Usage
1. Create an application  
    Set it like the image below.  
    Permissions is Retrieve, Platforms is Web.
    ![img](https://i.imgur.com/Kt7twnK.png)

2. Issue a request token  
    In order to obtain access token with Pocket API, consumer key attached at application creation and request token (code) issued using it are required.  
    [get_request_token.py](https://github.com/nazboost/pocket-to-slack/blob/master/tools/get_request_token.py) will help it.

3. Authentication by OAuth  
    Access to https://getpocket.com/auth/authorize?request_token=[request_token].

4. Acquire access token  
    Next, you issue access token using consumer key and request token.  
    [get_access_token.py](https://github.com/nazboost/pocket-to-slack/blob/master/tools/get_access_token.py) will help it.

5. Acquiring article information  
    Well, you are ready to hit the API, so you only send a request.  
    Looking at the [Pocket API Document](https://getpocket.com/developer/docs/v3/retrieve), it is written in an easy-to-use and easy-to-use manner.  
    In addition to the article title and URL this time, we also acquire the number of characters to calculate the time it takes to read.  
    By the way, although it seems that the number of characters that a Japanese can read in one minute is about 400 to 600 characters, assuming that skipping reading is 600 characters, you can calculate the time taken by dividing the number of characters by 600.

6. Obtain Slack webhook URL  
    After that it is Slack settings.  
    First of all it is acquisition of Webhook URL.  
    Create it from [Slack Incoming Webhook](https://slack.com/services/new/incoming-webhook), and add the Webhook URL to the environment variable as well.

7. Post to Slack  
    Since this application only posts, I used Python package: [slackweb](https://pypi.org/project/slackweb/).  
    Install like below:
    ```
    pip3 install slackweb
    ```
    You can use this so easy like below:  
    ```
    import slackweb

    webhook_url = 'foo.com'
    slack = slackweb.Slack(url=webhook_url)
    slack.notify(text='bar')
    ```

8. Prepare for deployment to Heroku  
When deploying to heroku you need the following additional files:  
    * requirements.txt
    * runtime.txt
    ```
    pip3 freeze > requirements.txt
    echo "python-3.6.7" > runtime.txt
    ```

9. Deploy to Heroku  
    Then, let's deploy to Heroku.  
    You need to install Heroku CLI like below:
    ```
    wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
    ```
    Log in this way:
    ```
    heroku login
    ```
    Finally, deploy like this way:
    ```
    heroku create [application_name]

    git add -A
    git commit -m "deploy"
    git push heroku master
    ```

10. Setting environment variables  
    When deployment is completed, set necessary environment variables.
    ```
    heroku config:set --app APP_NAME CONSUMER_KEY="[CONSUMER_KEY]" ACCESS_TOKEN="[ACCESS_TOKEN]" WEBHOOK_URL="[WEBHOOK_URL]"
    ```

11. Set schedule  
    Add add-in for scheduled execution:
    ```
    heroku addons:add scheduler:standard 
    ```
    Credit card information is necessary, but it is for overdelivery charge, and for one application it is enough for free.  
    Start the schedule like below:
    ```
    heroku addons:open scheduler
    ```
    And set command:
    ```
    python3 app.py
    ```

    Finally, if you set the time you want notifications, you are ready!