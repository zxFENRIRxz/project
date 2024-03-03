import streamlit as st
import csv

# Load existing data or create an empty list
try:
    with open('student_data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        student_data = list(reader)
except FileNotFoundError:
    student_data = []

# Function to add student and save to CSV
def add_student(name, surname, student_id, age):
    new_student = {'Name': name, 'Surname': surname, 'Student ID': student_id, 'Age': age}
    student_data.append(new_student)

    # Save the updated data to CSV file
    save_to_csv(student_data, 'student_data.csv')

# Function to delete student by Student ID and save to CSV
def delete_student(student_id):
    global student_data
    student_data = [student for student in student_data if student['Student ID'] != student_id]

    # Save the updated data to CSV file
    save_to_csv(student_data, 'student_data.csv')

# Function to save data to CSV using csv module
def save_to_csv(data, filename='student_data.csv'):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Surname', 'Student ID', 'Age']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to show main page with student list
def show_main_page():
    st.header("รายชื่อนักศึกษา")
    st.table(student_data)

# Streamlit app
def main():
    st.title("รายชื่อนักศึกษาสาขา DSSI ชั้นปีที่ 1 ปีการศึกษา 2566")

    # Sidebar menu
    menu = st.sidebar.radio("Menu", [":rainbow[Home]", "Add Student", "Delete Student"])

    if menu == ":rainbow[Home]":
        show_main_page()
    elif menu == "Add Student":
        st.header("Add Student Information")
        name = st.text_input("Name:")
        surname = st.text_input("Surname:")
        student_id = st.text_input("Student ID:")
        age = st.number_input("Age:", min_value=0, max_value=150, step=1)

        if st.button("Add Student"):
            add_student(name, surname, student_id, age)
            st.success("Student added successfully!")

        show_main_page()
    elif menu == "Delete Student":
        st.header("Delete Student Information")
        student_id_to_delete = st.text_input("Enter Student ID to delete:")

        if st.button("Delete Student"):
            delete_student(student_id_to_delete)
            st.success("Student deleted successfully!")

        show_main_page()

if __name__ == "__main__":
    main()
