"""
import tensorflow as tf
from tensorflow import keras
import numpy as np



# dowload the data but the data will be download with integer encodded 
data = keras.datasets.imdb


(train_data, train_lable), (test_data,test_lable) = data.load_data(num_words=88000)


# this will print an array of encoded words each integer represent a perticaler world
#print(train_data[0])


# loading the text encoded map form tensorflow 

words_index = data.get_word_index()

# Asign the value of the key with it's value +3 cause we will use the first 4 index to print a spicific words

words_index = {k:(v+3) for k,v in words_index.items()}

# START fpr the start of the words PAD mean the movie is suck don't fucking watch it UNK for Unknown char and UNUSD for unused
words_index['<START>'] = 1
words_index['<PAD>'] = 0
words_index["<UNK>"] = 2
words_index["<UNUSD>"] = 3


# now the word_index dic used the word as a key and the encoded value as a value but to train our model we will use the integer value
# so we need to revarse the dict so the integer value will be the key and word will be the value



reversed_word_index = dict([(value,key)for key, value in words_index.items()])


# we will creat a function to decode the text using the reversed_word_index to make the data readable

# this function will print the word if exsist in reversed_word_inedx if not print ? for each word in the text  
def decode_text(text):
    return " ".join(reversed_word_index.get(i, "?") for i in text)

print(type(train_data[0]))


def encoded_text(text):
    encoded = []
    for word in text:
        encoded.append(words_index.get(word))
    return encoded
# now if we looked into the data length we will finde that each sample contain a diffirance length then the others

#print(len(test_data[0]),len(test_data[1]))


# we can't train NN with this data so we need to preprocessing
train_data = keras.preprocessing.sequence.pad_sequences(train_data,value=words_index['<PAD>'],padding='post',maxlen=250) 
test_data = keras.preprocessing.sequence.pad_sequences(test_data,value=words_index['<PAD>'], padding="post",maxlen=250)
print(len(test_data[0]),len(test_data[1]))

print((train_data[0].shape))

# creating the model


model = keras.Sequential()
model.add(keras.layers.Embedding(88000,20))
model.add(keras.layers.GlobalAvgPool1D( ))
model.add(keras.layers.Dense(20, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))


model.summary()


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

x_val = train_data[:10000]
y_val = train_lable[:10000]

train_data = train_data[10000:]
train_lable = train_lable[10000:]


model.fit(train_data,train_lable,epochs=100,batch_size=512,verbose=1, validation_data=(x_val,y_val))
model.save("model.h5")

"""
import tensorflow as tf
from tensorflow import keras
import numpy as np
data = keras.datasets.imdb
words_index = data.get_word_index()

# Asign the value of the key with it's value +3 cause we will use the first 4 index to print a spicific words

words_index = {k:(v+3) for k,v in words_index.items()}

# START fpr the start of the words PAD mean the movie is suck don't fucking watch it UNK for Unknown char and UNUSD for unused
words_index['<START>'] = 1
words_index['<PAD>'] = 0
words_index["<UNK>"] = 2
words_index["<UNUSD>"] = 3


def encoded_text(text):
    encoded = []
    for word in text:
        encoded.append(words_index.get(word))
    return encoded

text = "this was not a good movie it was very bad and i did not like it very very bad"
text = text.split()
encoded = encoded_text(text=text)

print(encoded)

encoded.append(words_index['<PAD>'])

if len(encoded) < 250:


    for i in range(250 -len(encoded)):
    
        encoded.append(words_index["<PAD>"])
encoded = keras.preprocessing.sequence.pad_sequences([encoded],value=words_index['<PAD>'],padding='post',maxlen=250) 


model = keras.models.load_model(r"C:\Users\ibrah\model.h5")


result = model.predict(encoded)

if result > 0.7:
    print("This is a good review ")

elif result >0.5 and result < 0.7:
    print("It is okey")

elif result <0.5:
    print("this is a bad review ")

