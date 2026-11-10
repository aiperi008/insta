import streamlit as st
import requests

st.title("InstaSMM AI — Контент Генератор")
st.write("Локалдык бренддер үчүн автоматтык SMM жардамчы")


niche = st.text_input("Бизнес нишасы (мисалы: Кофейня, Кийим дүкөнү):")
description = st.text_input("Бизнес же товар тууралуу кыскача маалымат:")

if st.button("Контент түзүү"):
    if not niche or not description:
        st.warning("Сураныч, бардык талааларды толтуруңуз!")
    else:
        with st.spinner("AI контент даярдап жатат..."):
            try:

                payload = {
                    "business_niche": niche,
                    "product_description": description
                }

                response = requests.post("http://127.0.0.1:8000/generate", json=payload)

                if response.status_code == 200:
                    result = response.json()["data"]

                    st.success("Контент ийгиликтүү даяр болду!")
                    st.subheader(" Күчтүү тараптар:")
                    st.write(result["strong_points"])

                    st.subheader(" Контент-план:")
                    st.write(result["content_plan"])

                    st.subheader("Посттун тексти:")
                    st.write(result["post_text"])

                    st.subheader(" Reels сценарийи:")
                    st.write(result["reels_script"])

                    st.subheader(" Жооп шаблондору:")
                    st.write(result["templates"])
                else:
                    st.error("Серверден ката кетти.")

            except requests.exceptions.ConnectionError:
                st.error(" FastAPI серверге туташа албай жатат! Алгач `main.py` файлын иштетиңиз.")