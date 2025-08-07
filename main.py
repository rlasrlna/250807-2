import streamlit as st
import pandas as pd
import altair as alt

# 제목
st.title("MBTI 유형별 전 세계 평균 비율 분석")

# CSV 파일 읽기 (현재 경로에 존재한다고 가정)
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 열만 추출 (첫 번째 열은 'Country')
mbti_cols = df.columns[1:]

# MBTI 평균 계산
mbti_avg = df[mbti_cols].mean().reset_index()
mbti_avg.columns = ['MBTI', 'Average']

# 평균값 내림차순 정렬
mbti_avg = mbti_avg.sort_values(by='Average', ascending=False)

# 결과 출력
st.subheader("전 세계 MBTI 유형별 평균 비율 (%)")
st.dataframe(mbti_avg.style.format({'Average': '{:.2%}'}))

# Altair 막대그래프
chart = alt.Chart(mbti_avg).mark_bar().encode(
    x=alt.X('MBTI', sort='-y'),
    y=alt.Y('Average', title='평균 비율'),
    tooltip=
