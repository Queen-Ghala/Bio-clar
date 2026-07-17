import streamlit as st
import PyPDF2
import google.generativeai as genai

# إعداد المكتبة
genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("BioClar - مساعد الأحياء الذكي 🧬")

uploaded_file = st.file_uploader("ارفعي ملف PDF للدرس", type="pdf")

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    if st.button("تلخيص الدرس بذكاء"):
        with st.spinner("جاري التفكير والتلخيص..."):
            prompt = f"لخصي هذا النص الخاص بمادة الأحياء بأسلوب مبسط للطالبات، وقسميه لفقرات، وفي نهاية كل فقرة ضعي سؤالاً تفاعلياً واحداً. النص هو: {text}"
            response = model.generate_content(prompt)
            st.write(response.text)
