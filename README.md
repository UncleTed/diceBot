# How to setup your environment
We are using Linux, python3 (3.6.7) and a python virtual enviroment. This whole setup is based on the tutorial found at: https://realpython.com/python-virtual-environments-a-primer/

## Install the Linux packages
```
apt install vscode
apt install python3-venv  
```
  

## Enable the python virtual environment
`python3 -m venv env`

In order to activate this vitrual environment in the shell, run the following command
`source env/bin/activate`

To deactivate it run `deactivate`

## Configure VSCode 
### Extensions
Use the File -> Preferences -> Extensions menu option to open the extensions panel. Search for the extension name and push the green install button. You may have to reload VSCode. Install the following extensions:
* Python  
* Code-Runner

### Settings
* Add the python virtual environment to VSCode  
Type the settings key (crtl ,) to open the settings window in VSCode. Or use the File -> Preferences -> Settings menu option. This will open two panels: User Settings and Workspace Settings. Click on Workspace Settings.
Search for _python.pythonpath_ and then enter the following: `env/bin/python`

* Change the default python command that Code-Runner uses to your virtual python environment
Open the workspace settings file located in .vscode/settings.json and add the json snippet:
```
"code-runner.executorMap": {
        "python":  "env/bin/python",
    }
```

* Configure VSCode to use the python unittest framework
Open the workspace settings file located in .vscode/settings.json and add the json snippet:
```
 "python.unitTest.unittestArgs": [
        "-v",
        "-s",
        "./test",
        "-p",
        "*_test.py"
    ],
    "python.unitTest.pyTestEnabled": false,
    "python.unitTest.nosetestsEnabled": false,
    "python.unitTest.unittestEnabled": true
```

## Required Python Packages
The file requirements.txt has the list of required python packages. Install the packages with the command: `pip install -r requirements.txt`

## User serverless to deploy the lamba
`sudo npm install -g serverless`

Add another AWS users (besides your root user) named serverless. Don't forget to download the access key and secret key for your new user. Grant them admistrator access IAM role. 

You can add another profile to your `~/.aws/credentials` file that looks like this
```
[serverless]
aws_access_key_id = ...
aws_secret_access_key = ...
```

Export the environment variables to set the aws profile you wish to use
`export AWS_PROFILe="serverless" && export AWS_DEFAULT_REGION=us-west-2`

Deploy your project with
`serverless deploy -r us-west-2` because sometime serverless doesn't obey and puts your lamba into the default us-east-1 region. jerk.



## Twitter commands
https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/api-reference/aaa-premium

Register a webhook:
webhook_endpoint = urllib.parse.quote_plus('https://fm0fxa866m.execute-api.us-west-2.amazonaws.com/dev/webhook')
https://api.twitter.com/1.1/account_activity/all/dev/webhooks.json?url={}'.format(webhook_endpoint)

Subscribe your webhook to the account activity API
https://api.twitter.com/1.1/account_activity/all/dev/subscriptions.json'


List your subscriptions
curl --request GET \
 --url https://api.twitter.com/1.1/account_activity/all/dev/subscriptions/list.json \
 --header 'authorization: Bearer Token'


## Bibliography
* https://realpython.com/python-virtual-environments-a-primer/
* https://medium.com/@nragusa/getting-started-with-the-twitter-account-activity-api-beta-395e9498af81







