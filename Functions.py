import streamlit as st

def read_text(template_path):
    from docx import Document

    document = Document(template_path)

    # Using a for loop to construct the full text
    template = ""
    for paragraph in document.paragraphs:
        template += paragraph.text + "\n"  # Add each paragraph and a newline
    # Remove the last unnecessary newline, if desired
    template = template.rstrip()
    return template


def выбор_шаблона(templates):
    for template_key in templates:
        print("название шаблона: " + template_key)
        templates[template_key]
        print(templates[template_key]["description"] +
              "\n")
    while True:
        template_name = input("введите наименование шаблона ПВК; ")
        if template_name in templates:
            break
        else:
            print("выберите верное название шаблона: ", templates.keys())
    return template_name

def выбор_шаблона_streamlit(templates):
    шаблон = st.selectbox("Наименование шаблона", templates.keys()) # templates.keys())-возвращает список ключей словаря
    return шаблон # если не написать retern функция вернет None (null)

def заполнение_шаблона(template_dict, template_path):
    parameters = template_dict['parameters']
    user_inputs = {}
    for parameters_name in parameters:  # for parameter_name in parameters.keys():(второй вариант)
        user_inputs[parameters_name] = input(parameters[parameters_name] + ": ")
    template = read_text(template_path)
    template.format(**user_inputs)
    print(template.format(**user_inputs))

def заполнение_шаблона_streamlit(template_dict, template_path):
    parameters = template_dict['parameters']
    user_inputs = {}
    for parameters_name in parameters:  # for parameter_name in parameters.keys():(второй вариант); parameters_name = client
        user_inputs[parameters_name] = st.text_input(parameters[parameters_name] + ": ") # (parameters[parameters_name]) = наименование ИП
    template = read_text(template_path)# template_path-путь до шаблона
    template.format(**user_inputs)# функция подставления параметров в строку (функция ожидает получить содержимое объекта словаря); ** - распаковка словаря (тк функция не ожидает получить словарь в качестве параметра)
    st.write(template.format(**user_inputs))# st.write - функция показывает пользователю в интерфейсе результат
    #print(template.format(**user_inputs)) #вывод в терминал
    p = template.format(**user_inputs)
    return p

