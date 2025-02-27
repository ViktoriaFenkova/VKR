import streamlit as st
from Functions import выбор_шаблона_streamlit, заполнение_шаблона
import json

st.header("Конструктор ПВК")
пример ="""
name = st.text_input("Введите ваше имя:")
if name:
    st.write(f"Привет, {name}!")

color = st.selectbox("Выберите ваш любимый цвет", ["Красный", "Зелёный", "Синий"])
st.write(f"Ваш любимый цвет: {color}")

if st.button("Показать сообщение"):
    st.write(f"Рад встрече, {name}! Цвет {color} — отличный выбор.")

st.sidebar.header("Меню")
st.sidebar.button("Боковая кнопка")

feedbeck = st.text_input("Обратная связь:")
if feedbeck:
    st.write(f"Спасибо!") #f используется что бы вставить в строку любой объект
    if st.button("Отправить сообщение"):
        st.write("Сообщение отправлено")
"""

with open("./Data/формы_шаблонов.json", "r") as templates_file:
    templates = json.load(templates_file)

шаблон = выбор_шаблона_streamlit(templates)
print(шаблон)

template_dict = templates[шаблон]
template_path = template_dict['template']
# with open(template_path, 'r', encoding='utf-8') as template_file:
# template = template_file.read()


заполнение_шаблона(template_dict, template_path)

import streamlit as st
from string import Template


def fill_template(template_str, data):
    """
    Заполняет шаблон данными.

    :param template_str: Шаблон в виде строки с плейсхолдерами
    :param data: Словарь с данными для заполнения шаблона
    :return: Заполненный шаблон
    """
    template = Template(template_str)
    return template.substitute(data)


def main():
    st.title("Заполнение шаблона")

    # Пример шаблона
    template_str = st.text_area("Введите шаблон:", "Привет, $name! Добро пожаловать в $place.")

    # Ввод данных для заполнения
    name = st.text_input("Введите имя:", "Иван")
    place = st.text_input("Введите место:", "Мир")

    # Кнопка для заполнения шаблона
    if st.button("Заполнить шаблон"):
        data = {
            'name': name,
            'place': place
        }
        filled_template = fill_template(template_str, data)
        st.write("Заполненный шаблон:")
        st.write(filled_template)


if __name__ == "__main__":
    main()