import crypt                                #importing the crypt lybrary
hash_salt= input("Enter hash salt: ")       #user inputs the hash salt
full_hash= input("Enter full hash: ")       #user inputs the full hashed passcode
f = open("password.txt", "r")               #reffers to a file 'password.txt' which contains various nuber of sample passwords
for word in f.readlines():
    word = word.strip("\n")                 #differenciate each passcode on the basis of line break
    hash= crypt.crypt(word, hash_salt)
    if hash == full_hash :                  #compares the hash salt with the full hash
        print("Password: ", word)
        break                                #terminates when the password matches the decrypted hash
    else:
        print("Searching..")
