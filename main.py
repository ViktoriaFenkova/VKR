from click import password_option
from streamlit import button

from Functions import выбор_шаблона_streamlit, заполнение_шаблона_streamlit
import json
import streamlit as st
import os

# Конфигурация страницы
st.set_page_config(
    page_title="ПВК",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

a = '''

# Логотип и заголовок
logo_url = "https://cdn-icons-png.flaticon.com/512/3243/3243363.png"#как заменить изображение
st.image(logo_url, width=100)
st.title("📃 Конструктор ПВК")

# Роль
with st.sidebar:
    selected_section = st.radio("Управление пользовательскими ролями:", ["Пользователь (User)", "Администратор (Admin)"], index=0)

# Навигации слева
menu = ["📎 Главная", "📝 Конструктор ПВК", "🌐 Новости ПОД/ФТ", "📚 Обучение по ПОД/ФТ"]
choice = st.sidebar.selectbox("Навигация", menu)

# Содержимое главной страницы
if choice == "📎 Главная":
    st.subheader("Разработайте оптимальные правила внутреннего контроля для вашей компании легко и быстро")
    st.info("Здесь можно познакомиться с возможностями платформы.")

# Новости ПОД/ФТ
elif choice == "🌐 Новости ПОД/ФТ":
    st.subheader("Анализируемые данные")
    # Константы
    DATA_DIR = "./data/"
    DEFAULT_DOC_NAME = "README.md"

    # Определение функций
    @st.cache_resource(ttl=60 * 60)  # Кэшируем чтение файла на час
    def load_document(filename):
        """Читает содержимое документа."""
        filepath = DATA_DIR + filename
        ext = os.path.splitext(filepath)[1].lower()
        if ext == ".md":
            with open(filepath, encoding="utf-8") as f:
                return f.read(), "Markdown"
        elif ext == ".pdf":
            return filepath, "PDF"
        else:
            raise ValueError(f"Невозможно прочитать файл формата {ext}.")


    # Главное окно приложения st.set_page_config(page_title="База знаний по ПОД/ФТ", layout="wide")

    # Чтение всех доступных документов
    files = sorted(os.listdir(DATA_DIR))  # сортируем алфавитно
    doc_names = files or [DEFAULT_DOC_NAME]

    # Выбор темы
    selected_doc = st.sidebar.selectbox("Выберите тему:", doc_names)
    content, format_type = load_document(selected_doc)

    # Отображение выбранного материала
    if format_type == "Markdown":
        st.markdown(content)
    elif format_type == "PDF":
        st.write(f"[Открыть PDF файл]({content})")
    else:
        st.warning("Формат файла не поддерживается.")

    # Дополнительные секции
    st.divider()
    st.write("## Справочная информация")




# Конструктор ПВК
elif choice == "📝 Конструктор ПВК":
    st.subheader("_")
    st.write("""
    Проект предназначен для демонстрации возможностей Streamlit.\n
    Автор: Ваша фамилия\n
    Дата публикации: Сегодняшний день""")

# Примечания по оформлению
    st.markdown("<br><center>Copyright © 2023 Все права защищены.</center>", unsafe_allow_html=True)



# Обучение по ПОД/ФТ
elif choice == "📚 Обучение по ПОД/ФТ":
    st.subheader("Обучение по ПОД/ФТ")
    st.write("Здесь можно подготовить учебные материалы по вопросам противодействия легализации доходов, полученных преступным путем, и финансирования терроризма.")
    
# Функция, создающая презентацию из введённого текста

    def create_presentation(text):
    # Создаем объект презентации
    prs = Presentation()

    # Используем первый шаблон слайда (заголовочный слайд)
    title_slide_layout = prs.slide_layouts[0]
    first_slide = prs.slides.add_slide(title_slide_layout)
    title = first_slide.shapes.title
    title.text = "Презентация от Streamlit"

    # Остальные слайды будут содержать сам вводимый текст
    lines = text.split("\n")  # разбиение текста на строки
    content_slide_layout = prs.slide_layouts[1]

    for line in lines:
        if len(line.strip()) > 0:
            new_slide = prs.slides.add_slide(content_slide_layout)
            left = top = width = height = Inches(1.0)
            txBox = new_slide.shapes.add_textbox(left, top, width, height)
            tf = txBox.text_frame
            tf.text = line

    # Возвращаем готовую презентацию
    return prs


# Интерфейс Streamlit
st.title("Генерация презентации для проведения обучения")
input_text = st.text_area("Введите ваш текст:")
generate_button = st.button("Создать презентацию")

if generate_button:
    try:
        # Создаем презентацию
        presentation = create_presentation(input_text)

        # Преобразовываем презентацию в байтовый поток для скачивания
        output_buffer = BytesIO()
        presentation.save(output_buffer)
        output_buffer.seek(0)

        # Предлагает пользователю скачать созданный файл
        st.success("Презентация создана!")
        st.download_button(label="Скачать презентацию",
                           data=output_buffer.getvalue(),
                           file_name="mypresentation.pptx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
    except Exception as e:
        st.error(f"Произошла ошибка: {e}")'''







user_regime = st.sidebar.button("Режим заполнения шаблона")
print(user_regime)
if user_regime == True: # можно просто if e (результат нажатия кнопки):
    st.session_state.regime = "user_regime" # при каждом нажатии на кнопку перезаписывается
if "regime" not in st.session_state: #st.session_state - хранилище всех переменных, которые мы туда положили и они должны сохраняться при взаимодействии со страницей (пример - st.session_state.regime)
    st.session_state.regime = "user_regime" # это если пользователь не нажал вообще никакую кнопку
print(st.session_state.regime)

admin_regime = st.sidebar.button("Режим редактирования шаблона")
print(admin_regime)
if admin_regime == True: # можно просто if e (результат нажатия кнопки):
    st.session_state.regime = "admin_regime" # при каждом нажатии на кнопку перезаписывается



переменная = """
templates = { 
    'ПВК': { - словарь (с 10 по 13 стр) ключ - название шаблона
        'template': "./Data/Templates/PVK Template.docx", -  - параметр словаря "ПВК" , путь к файлу шаблона
        'parameters': {
            'client': 'наименование компании'
            },
        'description': 'Описание ПВК для Депозитария'
    },
    'ПВК для ИП': {
        'template': './Data/Templates/ПВК для ИП.docx',
        'parameters': {
            'client': 'наименование ИП'
            },
        'description': 'Описание ПВК для ИП'
    }}
"""

#with open("./Data/формы_шаблонов.json", "w") as templates_file:
    #json.dump(templates, templates_file)

with open("./Data/формы_шаблонов.json", "r") as templates_file: #with испозуется чтобы открыть файл прочитать его и закрыть
    templates = json.load(templates_file)

if "users_db" not in st.session_state:
    st.session_state.users_db = {} # Пустой словарь для хранения данных пользователей

    st.session_state.username = None
    st.session_state.password = None
# Функция для регистрации пользователя
def register_user(username, password):
    if username in st.session_state.users_db:
        st.error("Пользователь с таким именем уже существует.")
    else:
        st.session_state.users_db[username] = {"admin" : True, # любой пользователь - админ
                                               "password": password}
        st.success("Регистрация прошла успешно!")

# Функция для входа пользователя
def login_user(username, password):
    if username in st.session_state.users_db and st.session_state.users_db[username]["password"] == password:
        st.success("Вход выполнен успешно!")
    else:
        st.error("Неверное имя пользователя или пароль.")

if not (st.session_state.username in st.session_state.users_db and st.session_state.users_db[st.session_state.username] ["password"] == st.session_state.password):
    st.title("Форма регистрации и входа") # Заголовок формы регистрации и входа

    option = st.selectbox("Выберите действие", ["Регистрация", "Вход"])

    if option == "Регистрация":
        st.header("Регистрация")
        st.session_state.username = st.text_input("Имя пользователя")
        st.session_state.password = st.text_input("Пароль", type="password")

        if st.button("Зарегистрироваться"):
            register_user( st.session_state.username, st.session_state.password)

    elif option == "Вход":
        st.header("Вход")
        st.session_state.username = st.text_input("Имя пользователя")
        st.session_state.password = st.text_input("Пароль", type="password")

        if st.button("Войти"):
            login_user( st.session_state.username, st.session_state.password)

print(st.session_state.username)
print(st.session_state.users_db)
#st.session_state - хранение переменных в рамках одной сессии
if st.session_state.username in st.session_state.users_db and st.session_state.users_db[st.session_state.username]["password"] == st.session_state.password:
    if st.session_state.regime == "user_regime":
        template_name = выбор_шаблона_streamlit(templates) #вызов функции с параметрами tempiates  и после этого функция возращает результат и он записывается в перемменную template_name

        template_dict = templates[template_name] # template -это словарь, ключи в этом словаре - наименования шаблонов, template_name-наименование конкретного шаблона, выбранного пользователем
        template_path = template_dict['template'] # в template_path записывается 'template': './Data/Templates/ПВК для ИП.docx',
    # with open(template_path, 'r', encoding='utf-8') as template_file:
    # template = template_file.read()

        заполненный_шаблон = заполнение_шаблона_streamlit(template_dict, template_path)
        print(заполненный_шаблон) #самопроверка (но можно сделать через чекпоинт - черз дебак режим)
        with open("шаблон_клиента.docx", "w") as шаблон_файл:
            шаблон_файл.write(заполненный_шаблон)# retern - только с не готовыми функциями
        with open("шаблон_клиента.docx", "r") as шаблон_файл:
            st.download_button("Скачать документ", шаблон_файл, file_name= template_name +".docx")


d = '''import streamlit as st
from pptx import Presentation
from pptx.util import Inches
from io import BytesIO


# Функция, создающая презентацию из введённого текста
def create_presentation(text):
    # Создаем объект презентации
    prs = Presentation()

    # Используем первый шаблон слайда (заголовочный слайд)
    title_slide_layout = prs.slide_layouts[0]
    first_slide = prs.slides.add_slide(title_slide_layout)
    title = first_slide.shapes.title
    title.text = "Презентация от Streamlit"

    # Остальные слайды будут содержать сам вводимый текст
    lines = text.split("\n")  # разбиение текста на строки
    content_slide_layout = prs.slide_layouts[1]

    for line in lines:
        if len(line.strip()) > 0:
            new_slide = prs.slides.add_slide(content_slide_layout)
            left = top = width = height = Inches(1.0)
            txBox = new_slide.shapes.add_textbox(left, top, width, height)
            tf = txBox.text_frame
            tf.text = line

    # Возвращаем готовую презентацию
    return prs


# Интерфейс Streamlit
st.title("Генерация презентации для проведения обучения")
input_text = st.text_area("Введите ваш текст:")
generate_button = st.button("Создать презентацию")

if generate_button:
    try:
        # Создаем презентацию
        presentation = create_presentation(input_text)

        # Преобразовываем презентацию в байтовый поток для скачивания
        output_buffer = BytesIO()
        presentation.save(output_buffer)
        output_buffer.seek(0)

        # Предлагает пользователю скачать созданный файл
        st.success("Презентация создана!")
        st.download_button(label="Скачать презентацию",
                           data=output_buffer.getvalue(),
                           file_name="mypresentation.pptx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
    except Exception as e:
        st.error(f"Произошла ошибка: {e}")'''






