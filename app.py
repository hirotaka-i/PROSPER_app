
# Reference: https://github.com/mkhorasani/Streamlit-Authenticator

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

def show_registy_widget():
    # Register user widget
    try:
        if authenticator.register_user('参加登録', preauthorization=False):
            st.success('登録が完了いたしました。')
    except Exception as e:
        st.error(e)

# Login widget
authenticator.login('ログイン', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')

elif st.session_state["authentication_status"] is False:
    st.warning('''
[Username]か[Password]が違います'。
まだ参加されていない場合は、下記の[参加登録]からご登録ください。
               ''')
    show_registy_widget()

elif st.session_state["authentication_status"] is None:
    st.warning('''
[Username]と[Password]を入れてください.
まだ参加されていない方は、下記の[参加登録]からご登録ください。
               ''')
    show_registy_widget()