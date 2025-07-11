import streamlit as st
import joblib

model = joblib.load("rf_model.pkl")

st.title("ทำนายโอกาส PM2.5 เกินมาตรฐาน")

outdoor_pm25 = st.selectbox("ภายนอก PM2.5 > 25 µg/m³ หรือไม่?", [0, 1], format_func=lambda x: "ไม่เกิน" if x == 0 else "เกิน")
air_purifier = st.selectbox("เครื่องฟอกอากาศเปิด?", [0, 1], format_func=lambda x: "ปิด" if x == 0 else "เปิด")
activity = st.selectbox("มีกิจกรรมที่ก่อให้เกิดฝุ่น?", [0, 1], format_func=lambda x: "ไม่มี" if x == 0 else "มี")
open_window = st.selectbox("เปิดประตู/หน้าต่าง?", [0, 1], format_func=lambda x: "ปิด" if x == 0 else "เปิด")

if st.button("Predict"):
    X = [[outdoor_pm25, air_purifier, activity, open_window]]
    prob = model.predict_proba(X)[0][1]
    st.write(f"โอกาส PM2.5 เกินมาตรฐาน: {prob*100:.1f}%")
    if prob > 0.5:
        st.warning("เสี่ยง PM2.5 เกินมาตรฐาน ควรปิดหน้าต่าง/เปิดเครื่องฟอก")
    else:
        st.success("ความเสี่ยงต่ำ")