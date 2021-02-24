capital='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
small='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
space=' '
text=list(input('enter your text'))
print(text)
codSource=''
for j in range(len(text)):
    codNum=0
    for i in range(len(capital)):
        codNum+=1

        if(text[j]==' '):  
            codNum*=21
      
            break  
        
        elif(text[j]==small[i]):
            codNum*=12
       
            break

        if(text[j]==capital[i]):
            codNum*=10
            
            break
    codSource+=str(codNum)+","
            
print(codSource)
        

    

