import streamlit as st
import pandas as pd
import altair as alt

st.title("MBTI 유형별 직업 만족도 시각화")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # MBTI 열만 선택
    if 'MBTI' in df.columns and '직업 만족도' in df.columns:
        mbti_avg = df.groupby("MBTI")["직업 만족도"].mean().reset_index()

        st.subheader("MBTI별 직업 만족도 평균")
        chart = alt.Chart(mbti_avg).mark_bar().encode(
            x="MBTI:N",
            y="직업 만족도:Q",
            tooltip=["MBTI", "직업 만족도"]
        ).properties(width=600, height=400)

        st.altair_chart(chart, use_container_width=True)
    else:
        st.error("CSV 파일에 'MBTI'와 '직업 만족도' 열이 있어야 합니다.")
else:
    st.info("CSV 파일을 업로드해주세요.")
