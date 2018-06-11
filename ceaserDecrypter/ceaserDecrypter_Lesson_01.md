# CodeClub Secretcode API
## The Legend of the Localhost:5000

In this session we will be turning our computers into API endpoints that you can send messages to and recieve responses from.

Once you have you computer booted up, I will require that you have Python installed and ready to go, you can get it from here:  

``` https://www.python.org/downloads ```

If you are doing this exercise on a Raspberry pi, then Good news, its already installed and youre good to go!
Once you are up and running, type in this code into the Terminal/CMD Prompt

If youre installing on Windows, you have to be sure to tick the box that installs it to the $PATH and the other box for all users.

![Select Path][winpath]
![For all Users][winallusers]

Raspberry Pi Open the terminal with CTRL-ALT-T and Type:
```
sudo python pip install flask requests
```  
Windows, to open powershell:
![powershell][powershell]


Windows Open Powershell and Type:
```
python -m pip install flask requests
```

Well done!! Thats everything you need installed! So lets get to the code...

You to complete this mission in the time we have, you will need to have completed the 'Secret Code' Python task. Go ahead and open up your completed code for that piece of work. It should look something like this

``` python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

message = input('Please enter a message: ')

key = input('Enter a key (1-26): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Your new message is: ', newMessage)
```

We will come back to this in a little while. in the meantime im going to need you to create a new file and add the following code

``` python
from flask import Flask, request, Response, json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'My Super Secet Key'

# App Logic
@app.route('/', methods = ['GET','POST'])
def hello():
    return json.dumps({'Hello':'World'})

# Run App
if __name__ == '__main__':
    app.run(debug=DEBUG)
```

Woah!! you're probbably thinking _"What is all this crazy stuff ive got to type in?!"_

Let me break it down for you a little
```python
from flask import Flask, request, Response, json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'My Super Secet Key'
```
This bit covers all of your imports. Imports are the things that your program will need to work. It also gets them ready to be used. You will need these lines every time you make an API with _flask_

Lets continue.

``` python
# App Logic
@app.route('/', methods = ['GET','POST'])
def hello():
    return json.dumps({'Hello':'World!'})
```
This part of the code is where your program does all the hard work. when you send it a message, it will reply to you with the contents of the return statement

``` python
# Run App
if __name__ == '__main__':
    app.run(debug=DEBUG)
```
This last bit is the part that starts the app on your computer to allow you to communicate with it.

You can now run your app, like you do any other python program from the terminal or CMD prompt:
```
python <name_of_your_saved_file>.py
```
and you will see the below printed to your screen in response:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 217-964-124
 ```
 Congratulations! You have successfully run your First API! you can connect to it with your browser by typing in the address:

 ```127.0.0.1:5000/``` Or ```localhost:5000/```

 You should see the words "Hello World!" Printed on the screen.

 [winpath]: http://arcade.academy/_images/setup_windows_1.png
 [winallusers]: http://arcade.academy/_images/setup_windows_3.png
 [powershell]: https://4sysops.com/wp-content/uploads/2015/10/PowerShell-ISE-is-hard-to-find-with-Start-Search.png
