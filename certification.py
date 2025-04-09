import streamlit as st

# 正しいIDとパスワード
VALID_ID = "hirakegoma"
VALID_PASSWORD = "opensesami"

# セッション状態を初期化
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ログインフォーム
st.title("ログインページ")

if not st.session_state.authenticated:
    with st.form("login_form"):
        user_id = st.text_input("ユーザーID")
        password = st.text_input("パスワード", type="password")
        submitted = st.form_submit_button("ログイン")

        if submitted:
            if user_id == VALID_ID and password == VALID_PASSWORD:
                st.session_state.authenticated = True
                st.success("ログイン成功！")
                st.rerun()
            else:
                st.error("ユーザーIDまたはパスワードが違います。")

# 認証後のページ
if st.session_state.authenticated:
    st.subheader("ようこそ！")
    st.write("このページは認証されたユーザーのみが閲覧できます。")

    # 🔗 Notion 外部リンクを表示
    st.markdown(
        '[🔗 アンケート分析AIページへアクセス](https://quixotic-periwinkle-c66.notion.site/AI-1a7efde925ec8049ad41edec7031812e?pvs=4)',
        unsafe_allow_html=True
    )

    # ログアウトボタン
    if st.button("ログアウト"):
        st.session_state.authenticated = False
        st.rerun()
