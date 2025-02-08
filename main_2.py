from Functions import выбор_шаблона, заполнение_шаблона
import json
import streamlit as st
st.hedder("Test")


"""
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

with open("./Data/формы_шаблонов.json", "r") as templates_file:
    templates = json.load(templates_file)

template_name = выбор_шаблона(templates)

template_dict = templates[template_name]
template_path = template_dict['template']
# with open(template_path, 'r', encoding='utf-8') as template_file:
# template = template_file.read()


заполнение_шаблона(template_dict, template_path)