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
* Install the Python extension  
Use the File -> Preferences -> Extensions menu option to open the extensions panel. Search for the Python extension. Push the install button. You may have to reload VSCode.
### Settings
* Add the python virtual environment to VSCode  
Type the settings key (crtl ,) to open the settings window in VSCode. Or use the File -> Preferences -> Settings menu option. This will open two panels: User Settings and Workspace Settings. Click on Workspace Settings.
Search for _python.pythonpath_ and then enter the following: `env/bin/python`

## Required Python Packages
The file requirements.txt has the list of required python packages. Install the packages with the command: `pip install -r requirements.txt`


