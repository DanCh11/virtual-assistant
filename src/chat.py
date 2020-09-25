import random
import json
from numpy.lib.utils import source
import torch

import speech_recognition as sr

r = sr.Recognizer()

from .model import NeuralNetwork
from .nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('./src/data/data.json', 'r') as f:
    intents = json.load(f)

FILE = "./src/data/data.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']

all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)

model.load_state_dict(model_state)
model.eval()

bot_name = "Daycu"


while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            voice_data = tokenize(voice_data)
            x = bag_of_words(voice_data, all_words)
            x = x.reshape(1, x.shape[0])
            x = torch.from_numpy(x)

            output = model(x)
            _ ,predicted = torch.max(output, dim=1)
            tag = tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]

            if prob.item() > 0.75:
                for intent in intents["intents"]:
                    if tag == intent["tag"]:
                        print(f"{bot_name}: {random.choice(intent['responses'])}")

            else:
                print(f"{bot_name}: I do not understand...")

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Sorry, my speech service is down')
        


        


