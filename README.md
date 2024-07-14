<p style="text-align: center;">Windows Notification CLI</p>

# Usage

## Using Source

-> Download the files
-> Run the following command
```bash
py lib/ntf.py "this is title of the pop up" "content of the notification"
```
-> The notification stays active for 5s. This behaviour can be changed in the source code present inside the lib folder.
-> The code is commented for ease of customisation

## Using Compiled

-> For people who don't want to compile the python script everytime they need to show a notification
-> Following is the command for this method
```bash
lib/ntf.exe "this is title of the pop up" "content of the notification"
```
-> For paranoids and geeks, this project is compiled with PyInstaller, you can extract the source with pydumpck and decompyl6.


Thank You!