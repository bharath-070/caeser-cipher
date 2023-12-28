#caesar cipher logo
print("""                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          """)
print("""           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
   """)
#declaring the alphebets
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l",
           "m","n","o","p","q","r","s","t","u","v","w",
           "x","y","z"]
#decalre a empty list to store the shifted message
shifted_alpha=[]
#declar "again" to retry the program
again=1
#define the encrpytion function
def encode(message,shift,shifted_alpha):
  for i in range(0,length):
    for j in range(0,26):
      if message[i]==alphabets[j]:#check if the letter is in the alphabet
        shifted_alpha.append(alphabets[j+shift])#add the shifted letter to the list
  print("here is the encoded result:","".join(shifted_alpha))#here .join is used because
  #shifted_alpha is a list and we want to print it as a string, there are many ways to 
  #do this but this is the easy way
  del shifted_alpha[:]#delete or clear the list after printing
#define the decryption function
def decode(message,shift,shifted_alpha):
  for i in range(0,length):
    for j in range(0,26):
      if message[i]==alphabets[j]:
        shifted_alpha.append(alphabets[j-shift])
  print("here is the decoded result","".join(shifted_alpha))  
  del shifted_alpha[:]

while again==1:#while loop to repeat the program
  enc_or_dec=input("type 'encode' to encrypt and 'decode' to decrypt: ") 
  #ask if they want to encrypt or decrypt
  #take the inputs
  message=input("type your message: ").lower()#make the message lowercase
  shift=int(input("type the shift number: "))
  length=len(message)
  if enc_or_dec=="encode":#if they want to encrypt
    encode(message,shift,shifted_alpha)
  elif enc_or_dec=="decode":#if they want to decrypt
    decode(message,shift,shifted_alpha)
  else:
    print("invalid input")#if they type something else
  retry=input("do you want to try again? (y/n): ").lower()#ask if they want to retry
  again = 1 if retry == "y" else 0  # Replaced if-else block with ternary operator

    