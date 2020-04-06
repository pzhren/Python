# 参考项目：https://github.com/chamkank/flask-chatterbot


import os
import xlrd
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#创建机器人
bot = ChatBot("my chat") #创建机器人，名字
#测试训练
list_trainer = ListTrainer(bot)
list_trainer.train(['What is your name?', 'My name is Candice'])
list_trainer.train(['Who are you?', 'I am a bot, created by you'])

#训练一个较大的通用英语数据集
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")

#在自己的数据集上进行训练
data_path = './data/'
data = []
for files in os.listdir(data_path):
    xl = xlrd.open_workbook(data_path+files)
    table = xl.sheets()[0]
    for row_i in range(table.nrows):
        row_data = table.row_values(row_i)
        data += row_data
print('Number of training QA pairs: {}'.format(len(data)//2))
list_trainer.train(data) #在自己的数据集上进行训练

# chat feature，测试代码
# while True:
#     message=input('\t\t\tYou:')
#     if message.strip()!='Bye':
#         reply=bot.get_response(message)
#         print('Candice:',reply)
#     if message.strip()=='Bye':
#         print('Candice: Bye')
#         break


#定义网页前端部分
@app.route("/")
def home():
    return render_template("home.html") #创建home.html作为前端的网页

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

@app.route("/api/chat/<text>")
def get_bot_api(text):
    res = str(bot.get_response(text))
    return jsonify(res), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888) #可以让其他主机进行访问服务