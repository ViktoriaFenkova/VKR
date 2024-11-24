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
for template_key in templates:
    print("название шаблона: " + template_key)
    templates [template_key]
    print(templates[template_key] ["description"] +
          "\n")
while True:
    template_name = input("введите наименование шаблона ПВК; ")
    if template_name in templates:
        break
    else:
        print("выберите верное название шаблона: ", templates.keys())
template_dict = templates[template_name]

template_path = template_dict['template']
# with open(template_path, 'r', encoding='utf-8') as template_file:
# template = template_file.read()

from docx import Document

document = Document(template_path)

# Using a for loop to construct the full text
template = ""
for paragraph in document.paragraphs:
    template += paragraph.text + "\n"  # Add each paragraph and a newline

# Remove the last unnecessary newline, if desired
template = template.rstrip()

parameters = template_dict['parameters']
user_inputs = {}
for parameters_name in parameters:  # for parameter_name in parameters.keys():(второй вариант)
    user_inputs[parameters_name] = input(parameters[parameters_name] + ": ")

template.format(**user_inputs)
print(template.format(**user_inputs))
