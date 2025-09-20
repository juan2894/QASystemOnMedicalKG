#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

# Importa todas las clases y funciones de los módulos especificados.
# 导入指定模块中的所有类和函数。
from question_classifier import *
from question_parser import *
from answer_search import *

'''
Define la clase para el chatbot.
定义聊天机器人类。
'''
class ChatBotGraph:
    # Método de inicialización de la clase.
    # 类的初始化方法。
    def __init__(self):
        # Inicializa el clasificador de preguntas.
        # 初始化问题分类器。
        self.classifier = QuestionClassifier()
        # Inicializa el analizador de preguntas.
        # 初始化问题解析器。
        self.parser = QuestionPaser()
        # Inicializa el buscador de respuestas.
        # 初始化答案搜索器。
        self.searcher = AnswerSearcher()

    # Método principal para chatear.
    # 聊天主方法。
    def chat_main(self, sent):
        # Define una respuesta por defecto.
        # 定义一个默认答案。
        answer = '您好，我是小勇医药智能助理，希望可以帮到您。如果没答上来，可联系https://liuhuanyong.github.io/。祝您身体棒棒！'
        # Clasifica la pregunta del usuario.
        # 对用户的问题进行分类。
        res_classify = self.classifier.classify(sent)
        # Si la pregunta no se puede clasificar, devuelve la respuesta por defecto.
        # 如果问题无法分类，则返回默认答案。
        if not res_classify:
            return answer
        # Analiza la pregunta clasificada para generar una consulta SQL.
        # 解析分类后的问题以生成SQL查询。
        res_sql = self.parser.parser_main(res_classify)
        # Busca las respuestas finales en la base de datos.
        # 在数据库中搜索最终答案。
        final_answers = self.searcher.search_main(res_sql)
        # Si no se encuentran respuestas, devuelve la respuesta por defecto.
        # 如果未找到答案，则返回默认答案。
        if not final_answers:
            return answer
        # Si se encuentran respuestas, las une con un salto de línea y las devuelve.
        # 如果找到答案，则用换行符连接并返回。
        else:
            return '\n'.join(final_answers)

# Punto de entrada principal del programa.
# 程序主入口点。
if __name__ == '__main__':
    # Crea una instancia del chatbot.
    # 创建聊天机器人实例。
    handler = ChatBotGraph()
    # Inicia un bucle infinito para chatear.
    # 启动一个无限循环进行聊天。
    while 1:
        # Pide al usuario que introduzca una pregunta.
        # 提示用户输入问题。
        question = input('用户:')
        # Obtiene la respuesta del chatbot.
        # 获取聊天机器人的回答。
        answer = handler.chat_main(question)
        # Imprime la respuesta del chatbot.
        # 打印聊天机器人的回答。
        print('小勇:', answer)
