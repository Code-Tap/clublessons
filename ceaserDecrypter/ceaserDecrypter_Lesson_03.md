# CodeClub Secretcode API Part 03
## The Legend of the Localhost:5000

You've reached the final section of this guide, keep going!

Were going to add some code to the API that we've already created, this will enable it to process alot of encrypted messages all at once _programmatically_.  

The first thing that we're going to do is add another route to our app.
this will allow us to keep the work that we have already done, and let it work with the work we're about to do!

Firstly, you will need to add a new route to your API, like this:
``` python
@app.route('/bf-decode', methods = ['POST'])
def bruteForceList():
```
The 'POST' method means that this route will only respond to the POST tool we will create later on.

Next you will need to tell the route to do some work IF the request is receives is a POST:

``` python
if request.method == 'POST':

    data = request.data
    dataDict = json.loads(data)
```

This code makes sure it only does something if the request is a POST. If it is, it takes the request and loads it into a variable, and then converts it into a JSON object that we can loop through.



This completes your Decryption API. you can interact with it by running your saved file and going to the following address.

```http://localhost:5000/bf-decode/<encrypted string>```

You can replace the ```<encrypted string>``` with the results of your secret messages encryption program. The API will decrypt every possible key used to encrypt it and give you all the results back.

Here is the final code in full:

```python
#!/bin/python3
from flask import Flask, request, Response, json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'My Super Secet Key'

# Global vars
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# App Logic
@app.route('/', methods = ['GET','POST'])
def hello():
    return json.dumps({'Hello':'World'})

@app.route('/bf-decode/<encrypted_string>', methods = ['GET'])
def bruteForce(encrypted_string):
    if request.method == 'GET':
        decodedMessages = {}

        for key in range(26):
            newMessage = ''
            newkey = key + 1
            for character in encrypted_string:
                if character in alphabet:
                    position = alphabet.find(character)
                    newPosition = (position - newkey) % 26
                    newCharacter = alphabet[newPosition]
                    newMessage += newCharacter
                else:
                    newMessage += character
            decodedMessages[newkey] = newMessage

    response = Response(
       response=json.dumps(decodedMessages),
       status=200,
       mimetype='application/json'
       )
    return response

# Run App
if __name__ == '__main__':
    app.run(debug=DEBUG)
```
