# CodeClub Secretcode API Part 02
## The Legend of the Localhost:5000

Congratulations on making it this far! We're going to make our API do some heavy lifting in this section. Add the lines marked with a '+' but dont actually add the '+'

``` diff
from flask import Flask, request, Response, json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'My Super Secet Key'

+# Global vars
+alphabet = 'abcdefghijklmnopqrstuvwxyz'

# App Logic
@app.route('/', methods = ['GET','POST'])
def hello():
    return json.dumps({'Hello':'World'})

+@app.route('/bf-decode/<encrypted_string>', methods = ['GET'])
+def bruteForce(encrypted_string):
+    if request.method == 'GET':

# Run App
if __name__ == '__main__':
    app.run(debug=DEBUG)
```

 
The lines you have just added create a URL to your API, that you will be able to interact with, and then define a function that will be run when that URL is activated.

Remember your code from the Secret messages lesson I said you would need? Well now is when you need it, open it up and copy the loop from it plus the extra line i've added.

``` diff
# App Logic
@app.route('/', methods = ['GET','POST'])
def hello():
    return json.dumps({'Hello':'World'})

@app.route('/bf-decode/<encrypted_string>', methods = ['GET'])
def bruteForce(encrypted_string):
    if request.method == 'GET':

+        for key in range(26):
+            newMessage = ''
+            for character in encrypted_string:
+                if character in alphabet:
+                    position = alphabet.find(character)
+                    newPosition = (position - key) % 26
+                    newCharacter = alphabet[newPosition]
+                    newMessage += newCharacter
+                else:
+                    newMessage += character
+            decodedMessages[key] = newMessage


# Run App
if __name__ == '__main__':
    app.run(debug=DEBUG)
```

You can see that your program is now seriously growing in size, but thats ok, we dont have much more to go. We know what this code does, but were going to need to store the results from it somewhere, so lets add a dictionary to keep them in.  
Add the highlighted line in the location shown below

```diff
@app.route('/bf-decode/<encrypted_string>', methods = ['GET'])
def bruteForce(encrypted_string):
    if request.method == 'GET':

+       decodedMessages = {}

        for key in range(26):
            newMessage = ''
            for character in encrypted_string:
                if character in alphabet:
```

Let me try to explain exactly what is happening here then. 
```python
for key in range(26):
    newMessage = ''
```
Here we create a loop that will run 26 times.. exactly how many letter there are in the alphabet and then store the results from each loop into the newMessage varioable before overwriting it on the next loop

The rest of the code is identical to your Secret messages code until the last line of your nested loops

```python
decodedMessages[key] = newMessage
```

This line adds each of the 26 decrypted words to our dictionary we created along with the key used to encrypt it.

The final piece of the puzzle we need is to make the API respond to you when you interact with it.

Add the following lines to your code 

```diff
for key in range(26):
    newMessage = ''
    for character in encrypted_string:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position - key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    decodedMessages[key] = newMessage

+    response = Response(
+       response=json.dumps(decodedMessages),
+       status=200,
+       mimetype='application/json'
+       )
+    return response
```

This completes your Decryption API. you can interact with it by running your saved file and going to the following address. 

```http://localhost:5000/bf-decode/<encrypted string>```

You can replace the ```<encrypted string>``` with the results of your secret messages encryption program. The API will decrypt every possible key used to encrypt it and give you all the results back.

Here is the final code in full:

```python
#!/bin/python3
from flask import Flask, request, Response, json


# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b61GGh'

# Global vars
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# App Logic
@app.route('/bf-decode/<encrypted_string>', methods = ['GET'])
def bruteForce(encrypted_string):
    if request.method == 'GET':

        decodedMessages = {}

        for key in range(26):
            newMessage = ''
            for character in encrypted_string:
                if character in alphabet:
                    position = alphabet.find(character)
                    newPosition = (position - key) % 26
                    newCharacter = alphabet[newPosition]
                    newMessage += newCharacter
                else:
                    newMessage += character
            decodedMessages[key] = newMessage

        response = Response(
        response=json.dumps(decodedMessages),
        status=200,
        mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run(debug=True)
```