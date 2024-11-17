templates = {
    'ПВК': {
        'template': "./Data/Templates/PVK Template.docx",
        'parameters': {
            'client': 'наименование компании'},
        'description': 'Описание ПВК для Депозитария'
    },
    'ПВК для ИП': {
        'template': 'ИП: Настоящие Правила внутреннего контроля в целях противодействия легализации (отмыванию) доходов, полученных преступным путем, и финансированию терроризма {client} устанавливаются в соответствии с положениями',
        'parameters': {
            'client': 'наименование ИП'},
        'description': 'Описание ПВК для ИП'
    }}
template_dict = templates['ПВК']

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
