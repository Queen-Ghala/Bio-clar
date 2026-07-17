import streamlit as st

st.title("BioClar")
st.write("مرحباً بك في BioClar - برنامجك لتبسيط دروس الأحياء.")

uploaded_file = st.file_uploader("ارفع ملف دروسك هنا", type=['txt', 'pdf'])

if uploaded_file is not None:
    st.write("تم رفع الملف بنجاح! جاري المعالجة...")
    # هنا لاحقاً سنضيف كود التلخيص
