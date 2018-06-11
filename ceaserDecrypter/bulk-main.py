#!/bin/python3
from flask import Flask, request, Response, json
import dicttoxml


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b61GGh'

# Global vars
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# App Logic
@app.route('/', methods = ['GET','POST'])
def hello():
    return 'Hello world!'


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


@app.route('/bf-decode', methods = ['POST'])
def bruteForceList():
    if request.method == 'POST':

        data = request.data
        dataDict = json.loads(data)

        for item in dataDict:
            decodedMessages = []
            for key in range(26):
                newMessage = ''
                newkey = key + 1
                for character in item:
                    if character in alphabet:
                        position = alphabet.find(character)
                        newPosition = (position - newkey) % 26
                        newCharacter = alphabet[newPosition]
                        newMessage += newCharacter
                    else:
                        newMessage += character
                decodedMessages.append({'Decrption key':key, 'Result':newMessage})
            dataDict[item] = decodedMessages

        response = Response(
        response=json.dumps(dataDict),
        status=200,
        mimetype='application/json'
        )
        return response
        # return dicttoxml.dicttoxml(dataDict) #, attr_type=False)


if __name__ == '__main__':
    app.run(debug=DEBUG)
