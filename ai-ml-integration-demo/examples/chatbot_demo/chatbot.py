# Basic chatbot using intents
import json
from nltk.chat.util import Chat, reflections

with open('intents.json') as file:
    intents = json.load(file)

pairs = [(intent['patterns'], intent['responses'][0]) for intent in intents['intents']]
chatbot = Chat(pairs, reflections)
chatbot.converse()
