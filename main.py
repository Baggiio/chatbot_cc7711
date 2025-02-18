#pip install nltk numpy tensorflow

from chatbot import ChatBot
myChatBot = ChatBot()


#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
#myChatBot.createModel()

print("\nBem vindo ao Chatbot! Como posso te ajudar?")


pergunta = input("Prompt: ")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print("Intenção: " + intencao[0]['intent'] + "\nResposta: " + resposta)

while (intencao[0]['intent']!="despedida"):
    print("\nPosso lhe ajudar com algo a mais?")
    pergunta = input("Prompt: ")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print("Intenção: " + intencao[0]['intent'] + "\nResposta: " + resposta)

print("\nFoi um prazer atendê-lo!")