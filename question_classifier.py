#!/usr/bin/env python3
# coding: utf-8
# File: question_classifier.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

import os
import ahocorasick

class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        # Rutas de las palabras características
        self.disease_path = os.path.join(cur_dir, 'dict/disease.txt')
        self.department_path = os.path.join(cur_dir, 'dict/department.txt')
        self.check_path = os.path.join(cur_dir, 'dict/check.txt')
        self.drug_path = os.path.join(cur_dir, 'dict/drug.txt')
        self.food_path = os.path.join(cur_dir, 'dict/food.txt')
        self.producer_path = os.path.join(cur_dir, 'dict/producer.txt')
        self.symptom_path = os.path.join(cur_dir, 'dict/symptom.txt')
        self.deny_path = os.path.join(cur_dir, 'dict/deny.txt')
        # Cargar palabras características
        self.disease_wds= [i.strip() for i in open(self.disease_path) if i.strip()]
        self.department_wds= [i.strip() for i in open(self.department_path) if i.strip()]
        self.check_wds= [i.strip() for i in open(self.check_path) if i.strip()]
        self.drug_wds= [i.strip() for i in open(self.drug_path) if i.strip()]
        self.food_wds= [i.strip() for i in open(self.food_path) if i.strip()]
        self.producer_wds= [i.strip() for i in open(self.producer_path) if i.strip()]
        self.symptom_wds= [i.strip() for i in open(self.symptom_path) if i.strip()]
        self.region_words = set(self.department_wds + self.disease_wds + self.check_wds + self.drug_wds + self.food_wds + self.producer_wds + self.symptom_wds)
        self.deny_words = [i.strip() for i in open(self.deny_path) if i.strip()]
        # Construir actree del dominio
        self.region_tree = self.build_actree(list(self.region_words))
        # Construir diccionario
        self.wdtype_dict = self.build_wdtype_dict()
        # Palabras interrogativas
        self.symptom_qwds = ['síntoma', 'síntomas', 'indicio', 'fenómeno', 'manifestación', 'señal']
        self.cause_qwds = ['causa', 'razón', 'por qué', 'cómo es que', 'por que', 'motivo', 'causar', 'provocar']
        self.acompany_qwds = ['complicación', 'complicaciones', 'junto con', 'ocurrir juntos', 'aparecer juntos', 'acompañar', 'coexistir']
        self.food_qwds = ['dieta', 'beber', 'comer', 'comida', 'alimentación', 'alimento', 'plato', 'receta', 'suplemento']
        self.drug_qwds = ['medicina', 'medicamento', 'fármaco', 'pastilla', 'cápsula', 'jarabe']
        self.prevent_qwds = ['prevenir', 'prevención', 'evitar', 'proteger', 'esquivar', 'eludir', 'cómo no', 'qué hacer para no']
        self.lasttime_qwds = ['ciclo', 'cuánto tiempo', 'cuántos días', 'cuántos años', 'cuántas horas', 'duración']
        self.cureway_qwds = ['cómo curar', 'cómo tratar', 'tratamiento', 'terapia', 'qué hacer', 'cómo solucionar', 'método de curación']
        self.cureprob_qwds = ['probabilidad de cura', 'esperanza de cura', 'posibilidad', 'se puede curar', 'curable', 'porcentaje']
        self.easyget_qwds = ['grupo susceptible', 'quién se contagia', 'fácil de contagiar', 'quiénes', 'infectar', 'contraer']
        self.check_qwds = ['examen', 'revisión', 'chequeo', 'analítica', 'detectar', 'prueba']
        self.belong_qwds = ['a qué departamento', 'departamento', 'especialidad']
        self.cure_qwds = ['qué cura', 'para qué sirve', 'utilidad', 'uso', 'beneficio', 'qué trata']

        print('inicialización del modelo terminada ......')

        return

    '''Función principal de clasificación'''
    def classify(self, question):
        data = {}
        medical_dict = self.check_medical(question)
        if not medical_dict:
            return {}
        data['args'] = medical_dict
        # Recopilar los tipos de entidades involucradas en la pregunta
        types = []
        for type_ in medical_dict.values():
            types += type_
        question_type = 'others'

        question_types = []

        # Síntomas
        if self.check_words(self.symptom_qwds, question) and ('disease' in types):
            question_type = 'disease_symptom'
            question_types.append(question_type)

        if self.check_words(self.symptom_qwds, question) and ('symptom' in types):
            question_type = 'symptom_disease'
            question_types.append(question_type)

        # Causas
        if self.check_words(self.cause_qwds, question) and ('disease' in types):
            question_type = 'disease_cause'
            question_types.append(question_type)
        # Complicaciones
        if self.check_words(self.acompany_qwds, question) and ('disease' in types):
            question_type = 'disease_acompany'
            question_types.append(question_type)

        # Alimentos recomendados o prohibidos
        if self.check_words(self.food_qwds, question) and 'disease' in types:
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'disease_not_food'
            else:
                question_type = 'disease_do_food'
            question_types.append(question_type)

        # Encontrar enfermedad a partir de alimentos
        if self.check_words(self.food_qwds+self.cure_qwds, question) and 'food' in types:
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'food_not_disease'
            else:
                question_type = 'food_do_disease'
            question_types.append(question_type)

        # Medicamentos recomendados
        if self.check_words(self.drug_qwds, question) and 'disease' in types:
            question_type = 'disease_drug'
            question_types.append(question_type)

        # Enfermedad tratada por el medicamento
        if self.check_words(self.cure_qwds, question) and 'drug' in types:
            question_type = 'drug_disease'
            question_types.append(question_type)

        # Exámenes a realizar por la enfermedad
        if self.check_words(self.check_qwds, question) and 'disease' in types:
            question_type = 'disease_check'
            question_types.append(question_type)

        # Encontrar enfermedad a partir de exámenes
        if self.check_words(self.check_qwds+self.cure_qwds, question) and 'check' in types:
            question_type = 'check_disease'
            question_types.append(question_type)

        # Prevención
        if self.check_words(self.prevent_qwds, question) and 'disease' in types:
            question_type = 'disease_prevent'
            question_types.append(question_type)

        # Duración de la enfermedad
        if self.check_words(self.lasttime_qwds, question) and 'disease' in types:
            question_type = 'disease_lasttime'
            question_types.append(question_type)

        # Tratamiento
        if self.check_words(self.cureway_qwds, question) and 'disease' in types:
            question_type = 'disease_cureway'
            question_types.append(question_type)

        # Probabilidad de cura
        if self.check_words(self.cureprob_qwds, question) and 'disease' in types:
            question_type = 'disease_cureprob'
            question_types.append(question_type)

        # Población vulnerable
        if self.check_words(self.easyget_qwds, question) and 'disease' in types :
            question_type = 'disease_easyget'
            question_types.append(question_type)

        # Si no se encontró información externa relacionada, devolver la descripción de la enfermedad
        if question_types == [] and 'disease' in types:
            question_types = ['disease_desc']

        # Si no se encontró información externa relacionada, buscar enfermedad por síntoma
        if question_types == [] and 'symptom' in types:
            question_types = ['symptom_disease']

        # Agrupar múltiples resultados de clasificación en un diccionario
        data['question_types'] = question_types

        return data

    '''Construir los tipos correspondientes a las palabras'''
    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.disease_wds:
                wd_dict[wd].append('disease')
            if wd in self.department_wds:
                wd_dict[wd].append('department')
            if wd in self.check_wds:
                wd_dict[wd].append('check')
            if wd in self.drug_wds:
                wd_dict[wd].append('drug')
            if wd in self.food_wds:
                wd_dict[wd].append('food')
            if wd in self.symptom_wds:
                wd_dict[wd].append('symptom')
            if wd in self.producer_wds:
                wd_dict[wd].append('producer')
        return wd_dict

    '''Construir actree para acelerar el filtrado'''
    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''Filtrar preguntas'''
    def check_medical(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i:self.wdtype_dict.get(i) for i in final_wds}

        return final_dict

    '''Clasificar basándose en palabras características'''
    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('Ingrese una pregunta: ')
        data = handler.classify(question)
        print(data)