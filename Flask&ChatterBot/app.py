# 参考项目：https://github.com/chamkank/flask-chatterbot


import os
import xlrd
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request, jsonify
import random

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
q_data = []
for files in os.listdir(data_path):
    xl = xlrd.open_workbook(data_path+files)
    table = xl.sheets()[0]
    for row_i in range(table.nrows):
        row_data = table.row_values(row_i)
        q_data += [row_data[0]]
        data += row_data
n_data = len(data)//2
print('Number of training QA pairs: {}'.format(n_data))
list_trainer.train(data) #在自己的数据集上进行训练
q_data_sel = random.sample(q_data,n_data//20) #随机挑出10分之一的问题作为比较语料库
def ld(str1, str2):
    #计算编辑距离
    m, n = len(str1) + 1, len(str2) + 1

    # 初始化矩阵
    matrix = [[0] * n for i in range(m)]
    matrix[0][0] = 0
    for i in range(1, m):
        matrix[i][0] = matrix[i - 1][0] + 1
        for j in range(1, n):
            matrix[0][j] = matrix[0][j - 1] + 1
    # 动态规划计算ld值
    for i in range(1, m):
        for j in range(1, n):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
    return matrix[m - 1][j - 1]


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
    dl_q = []
    Text = {}
    userText = str(request.args.get('msg')) #得到网页中msg中的文本
    bot_response = str(bot.get_response(userText))
    for com_text in q_data_sel:
        dl_q += [ld(userText,com_text)]
    dl_q_sort=sorted(enumerate(dl_q), key=lambda x:x[1],reverse=True) #降序排序
    q_data_re_top = ('<br>').join(q_data_sel[d[0]] for d in dl_q_sort[:3])
    # Text = bot_response + '<br><br> Related Questions : <br>'+ q_data_re_top
    Text['bot_response'] = bot_response
    Text['RQ'] = '<br>Related Questions :'
    Text['q_data_re_top'] = q_data_re_top.split('<br>')
    # Text['q_data_re_top'] = q_data_re_top
    return Text #返回bot的输出文本

@app.route("/api/chat/<text>")
def get_bot_api(text):
    res = str(bot.get_response(text))
    return jsonify(res), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8889) #可以让其他主机进行访问服务
    #http://10.15.15.89:8888