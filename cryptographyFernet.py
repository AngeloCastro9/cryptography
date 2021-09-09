from cryptography.fernet import Fernet

def send(message): 
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as keyFile:
        keyFile.write(key)
    cipherSuite = Fernet(key)
    cipherText = cipherSuite.encrypt(message)
    print('cipher message: ' + cipherText.decode('utf-8') + ' key: ' + key.decode('utf-8'))

def loadKey():  
    return open('secret.key', 'rb').read()
    
def receive(message, isKey):
    try: 
        if(isKey): Key = loadKey()
        else: Key = bytes(isKey, encoding= 'utf-8')

        cipherSuite = Fernet(Key)    
        plainText = cipherSuite.decrypt(message)

        print(plainText.decode('utf-8'))                
    except:
        print('Null')

while True:
    directionQuestion = input('Press 1 to send Message, 2 to receive message and 3 to exit: ')
    if directionQuestion == '1':
        message = input('Input your text ')
        send(bytes(message, encoding= 'utf-8'))

    if directionQuestion == '2':
        cipherMessage = input('Input your cipher message: ')
        key = input('Input your key or type "True" to use stored key: ')
        receive(bytes(cipherMessage, encoding= 'utf-8'), key)
        
    if directionQuestion == '3':
        break
