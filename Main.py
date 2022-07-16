from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbt = ChatBot("Alexa")
trainer = ChatterBotCorpusTrainer(chatbt)

trainer.train("chatterbot.corpus.english")

print("Hi I am Alexa")
while(True):
    print(">>>")
    print(chatbt.get_response(input()))

