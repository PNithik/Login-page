import streamlit as st
import re


st.title('My Streamlit Web App')
st.write('Welcome to my first Streamlit web app!')


def check_username(email):
    # regex for validation of correct email pattern
    pattern = r'^(?:[a-zA-Z][a-zA-Z0-9_-]{0,14}@[a-zA-Z0-9.-]+\.(?:com|in))?$'
    if re.match(pattern, email):
        return True
    else:
        return False


def check_password(password):
    # same as re for validation for password
    pattern = r'^(?=.*[A-Z])(?=.*[@$!%*#?&_-])(?=.*\d)[A-Za-z\d@$!%*#?&_-]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False


# for choose login
choose = st.selectbox(
    'Login / Signup /Forget Password', ['Login', 'Signup', 'Forget password'])
if choose == 'Login':
    email = st.text_input('Email Address', placeholder='Enter your Email')
    password = st.text_input("Password", type='password',
                             placeholder='Enter your password')
    if check_username(email) == True:
        if check_password(password) == True:
            st.button('Login')
            with open('database.txt', 'r') as ext:
                for line in ext:
                    if line.split()[0] == email:
                        if line.split()[1] == password:
                            st.write(f'Welcome Back "{email}"')
# for forget password

if choose == 'Forget password':
    email = st.text_input("Enter Email")
    np = st.text_input("Enter New Password", type='password')
    cp = st.text_input("Re-enter new password", type='password')
    if np and cp:
        if np == cp:
            if check_password(cp) == True:
                if st.button("Login Password"):
                    with open('database.txt', 'a') as no:
                        no.write(f'{email} {np}\n')
                    st.write('Password changed successfully')
if choose == 'Signup':
    user = st.text_input('Enter Username', placeholder='Enter your username')
    email = st.text_input('Email Address', placeholder='Enter your email')
    password = st.text_input(
        'New Password', type='password', placeholder='Enter your password')
    if check_username(email) == True:
        if check_password(password) == True:
            if st.button('Signup'):
                with open("database.txt", 'a') as new:
                    new.write(f'{user} {email} {password}\n')
                st.write(f'{user} "Signup Successfully"')
        else:
            st.error("Invalid Password")
    else:
        st.error("Invalid Email address")
