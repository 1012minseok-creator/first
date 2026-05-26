import streamlit as st
st.title('첫번째 웹어플 만들기!!')
"# 이건 부제목 #"
"## 부제목 맞아? ##"
'''### magic 적용 예시
1. ordered item
-강조하려면: **unordered item**
-기울이려면:*unordered item*
-강조와 기울임 동시에:***unordered item***
2. ordered item
3. ordered item
# 비즈니스 모델 분석
[네이버](https://www.naver.com)  
[홍익대학교](https://www.hongik.ac.kr)  
이것이 일반 본문임 밑에와 비교해보기  
:red[빨간색으로 표현할래] :green[초록색으로 표현할래]
'''
'''python  
import streamlit as st  
print('코드 블록')
'''
with st.echo():
    #이 블록의 코드와 결과를 출력한다는 의미 들여쓰기의 범위에 대해서
    name='mslee'
    st.write('hello',name)

st.caption('캡션(작고 흐린 글씨로 표현됨):st.caption()')

'#### :orange[이미지:st.image()]'
st.image('./data/이미지 원본.png',caption='파이썬 로고',width=500)

'#### :orange[오디오:st.audio()]'
st.audio('./data/음원.mp3',format='audio/mpeg',loop=True)

'#### :orange[동영상:st.video()]'
# 'rb': 바이너리 모드로 파일 열기
video_file= open('./data/영상.mp4','rb')
video_bytes=video_file.read()
st.video(video_bytes)

