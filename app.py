
# Reference: https://github.com/mkhorasani/Streamlit-Authenticator
# https://zenn.dev/karaage0703/articles/db8c663640c68b

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
authenticator.login('PROSPERログイン', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('ログアウト', 'main', key='unique_key')
    st.write(f'おかえりなさい *{st.session_state["name"]}*さん')
    st.title('質問票')
    st.write('下記の質問票にまだお答えいただいていない方は、お答えください。')
    st.markdown('[MDS-UPDRS Part I](https://docs.google.com/forms/d/e/1FAIpQLSdVD2MG9y0vPLnKvtblS6BaEGhQQ27hSOcz-9kxCShnYDZYWA/viewform)')
    st.markdown('[MDS-UPDRS Part II](https://forms.gle/s9rbb3XeHycWV5Fk6)')


elif st.session_state["authentication_status"] is False:
    st.warning('''
[ユーザーID]か[パスワード]が違います。
まだ参加されていない場合は、下記の[参加登録]からご登録ください。
               ''')
    show_registy_widget()

elif st.session_state["authentication_status"] is None:
    st.warning('''
[ユーザーID]と[パスワード]を入れてください.
まだ参加されていない方は、下記の[参加登録]からご登録ください。
               ''')
    show_registy_widget()