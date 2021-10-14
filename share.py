import pyDH
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def cipherMode(key16, mode, iv = None): # Allows the use of some modes
    if mode == 'CBC': # supports IV
        cipher = AES.new(key16, AES.MODE_CBC, iv)
    elif mode == 'CFB': # supports IV
        cipher = AES.new(key16, AES.MODE_CFB, iv) # Establece el modo de encripcion
    elif mode == 'OFB': # supports IV
        cipher = AES.new(key16, AES.MODE_OFB, iv)
    else: # Si se ingresa un modo inadecuado, lo ejecuta con CBC
        cipher = AES.new(key16, AES.MODE_CBC, iv)

    return cipher

def AEScipher(key16, txtToCipher, txtToReturn, mode):
    cipher = cipherMode(key16, mode)
    iv = b64encode(cipher.iv).decode('utf-8')
    cipherTxt = open(txtToReturn,"w+")
    with open(txtToCipher) as a:
        for line in a:
            line = bytes(line, 'utf-8')
            ct_bytes = cipher.encrypt(pad(line, AES.block_size))
            ct = b64encode(ct_bytes).decode('utf-8')
            cipherTxt.write(ct + '\n')

    a.close()
    cipherTxt.close()

    return str(iv), cipher.iv

def AESdecrypt(key16, cipherTxt, returnTxt, iv, mode):
    cipher = cipherMode(key16, mode, iv)
    decryptedTxt = open(returnTxt, 'w+')

    # Ahora se obtiene el texto
    with open(cipherTxt) as ctxt:
        read = ctxt.read()
        lines = read.split('\n')
        for line in lines:
            if line:
                ct = b64decode(line)
                bt = unpad(cipher.decrypt(ct), AES.block_size)
                pt = bt.decode()
                decryptedTxt.write(pt)

    # Escribiendo en el txt y 
    ctxt.close()
    decryptedTxt.close()

# Se genera la llave por el txt 
def generateKeys(mode=14):
    private_key = pyDH.DiffieHellman(mode)
    public_key = private_key.gen_public_key()
    with open('public3.txt', 'w') as public:
        public.write(str(public_key))
    return private_key

# Genera la llave conjunta
def getSharedKey(private_key, txt):
    with open(txt, 'r') as file:
        other_public = int(file.read())
    return private_key.gen_shared_key(other_public)

if __name__ == '__main__':
    # Generar la llave
    option = ''
    shared_key = ''

    while (True):

        print('\n1. Generar llaves\n2. Generar compartida\n3. Encriptar txt\n4. Desencriptar')
        option = input('Ingrese su opcion: ')
        if (option == '1'):
            private_key = generateKeys()
        elif (option == '2'):
            shared_key = getSharedKey(private_key, 'public_key.txt')[:16]
        elif (option == '3'):
            byte = bytes(shared_key, 'utf-8')
            temp, iv = AEScipher(byte, 'pregunta.txt', 'chipher.txt', 'CBC')
        elif (option == '4'):
            byte = bytes(shared_key, 'utf-8')
            AESdecrypt(byte, 'respuesta.txt', 'desencriptado.txt', iv, 'CBC')
        elif (option == '5'):
            break
    