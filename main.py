from Functions import выбор_шаблона, заполнение_шаблона

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

template_name = выбор_шаблона(templates)

template_dict = templates[template_name]
template_path = template_dict['template']
# with open(template_path, 'r', encoding='utf-8') as template_file:
# template = template_file.read()


заполнение_шаблона(template_dict, template_path)