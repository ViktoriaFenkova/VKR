from Functions import выбор_шаблона_streamlit, заполнение_шаблона_streamlit
import json
import streamlit as st
st.header("Конструктор ПВК") #отвечает на странице за заголовок


переменная = """
templates = {
    'ПВК': {
        'template': "./Data/Templates/PVK Template.docx",
        'parameters': {
            'client': 'наименование компании'},
        'description': 'Описание ПВК для Депозитария'
    },
    'ПВК для ИП': {
        'template': './Data/Templates/ПВК для ИП.docx',
        'parameters': {
            'client': 'наименование ИП'},
        'description': 'Описание ПВК для ИП'
    }}
"""

#with open("./Data/формы_шаблонов.json", "w") as templates_file:
    #json.dump(templates, templates_file)

with open("./Data/формы_шаблонов.json", "r") as templates_file: #with испозуется чтобы открыть файл прочитать его и закрыть
    templates = json.load(templates_file)

template_name = выбор_шаблона_streamlit(templates) #вызов функции с параметрами tempiates  и после этого функция возращает результат и он записывается в перемменную template_name

template_dict = templates[template_name] # template -это словарь, ключи в этом словаре - наименования шаблонов, template_name-наименование конкретного шаблона, выбранного пользователем
template_path = template_dict['template'] #относится к заполнению шаблона
# with open(template_path, 'r', encoding='utf-8') as template_file:
# template = template_file.read()


заполнение_шаблона_streamlit(template_dict, template_path)


