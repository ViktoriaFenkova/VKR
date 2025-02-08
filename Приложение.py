import streamlit as st

st.header("Приветственное приложение")

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
    st.write(f"Спасибо!")
    if st.button("Отправить сообщение"):
        st.write("Сообщение отправлено")