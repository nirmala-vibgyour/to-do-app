import streamlit as st
import functions

todos = functions.get_todos()

st.title("Todo App")
st.subheader("This is a todo app.")
st.write("This app is to increase your productivity.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")