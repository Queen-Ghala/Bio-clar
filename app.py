import streamlit as st
from PyPDF2 import PdfReader

st.title("BioClar - تبسيط الأحياء")

uploaded_file = st.file_uploader("ارفع ملف دروسك (PDF) هنا", type=['pdf'])

def get_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if uploaded_file is not None:
    st.write("جاري تحليل ملفك...")
    file_text = get_text_from_pdf(uploaded_file)
    
    # هنا سنعرض ملخصاً بسيطاً (كمثال)
    st.subheader("الملخص المقترح:")
    st.write("هذا الملف يحتوي على: " + file_text[:500] + "... (هذا عرض سريع للنص)")
    
    st.success("تم استخراج النص بنجاح! الخطوة القادمة هي الربط مع محرك ذكاء اصطناعي للتلخيص.")
