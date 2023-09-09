import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "눈떠기"
)

menu = st.selectbox("MENU", ["자기소개", "학교소개", "취미"])

if menu == "자기소개":
    st.title("자기소개")
    image = Image.open("AI.png")
    st.image(image, caption="")
    st.subheader("저는 청구고등학교에 재학중인 정윤석 입니다")
    st.subheader("인공지능 분야를 진로로 희망하고 이것을 바탕으로 사람들을 돕고 싶습니다.")

elif menu == "학교소개":
    st.title("학교소개")
    image = Image.open("청구고등학교2.png")
    st.image(image, caption="청구고등학교")
    image2 = Image.open("청구고등학교.png")
    st.image(image2, caption="청구고등학교")
    st.subheader("청구고등학교는 1963년 12월 24일에 설립되었으며 2023년 기준 학생수는 703명 입니다.  ")
    st.subheader("대구광역시 동구 국채보상로 827에 위치하고 있고 대구 도시철도 1호선 신천역 5번 출구에서 남쪽으로 800m 거리에 위치하고 있습니다.")

elif menu ==  "취미":
    st.title("취미")
    st.video("https://www.youtube.com/watch?v=uXKaoX4mkNg")
    st.subheader("저는 시간날때마다 음악을 듣는 취미가 있는데 여러 음악중 Queen의 Love Of My Life를 많이 듣습니다.")
