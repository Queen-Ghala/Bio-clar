import streamlit as st
import PyPDF2
import google.generativeai as genai

# ضعي مفتاحكِ السري مكان الكلمة الموجودة بين القوسين
apiimport os
os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6JhMEhVqcUPTcJtL1QQMAmacRuL9tFg1SWd2F-ZjLOT3Q"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model

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
