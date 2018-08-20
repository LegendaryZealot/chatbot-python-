#!/usr/local/bin/python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Ron Obvious")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
while 1>0:
 str = input("Enter your input: ");
 response = chatbot.get_response(str)
 print(response)
