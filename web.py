import streamlit as st
import functions
st.title("My Todo App")
st.subheader("This is my todo app")

for x in functions.get_todos():
    st.checkbox(x)

st.text_input(label="Enter a todo", placeholder="Add a new todo...", key="new_todo")