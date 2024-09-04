### **2차시: 영화 리뷰 감성 분석 모델 학습**

- **기술 스택**: Scikit-learn, Pandas, Joblib
- **학습 목표**:
    - **데이터셋 준비 및 전처리**: 영화 리뷰 데이터셋을 Pandas를 사용해 로드하고, 텍스트 전처리 과정을 거쳐 모델 학습에 적합한 형태로 변환하는 방법을 배웁니다.
    - **텍스트 벡터화**: Scikit-learn의 `CountVectorizer`를 사용해 텍스트 데이터를 벡터화하여 숫자 형태로 변환하는 방법을 학습합니다.
    - **모델 학습 및 평가**: Logistic Regression 모델을 학습시키고, 모델의 성능을 평가하는 방법을 학습합니다.
    - **모델 저장**: 학습된 모델을 Joblib을 사용해 파일로 저장하고, 이후 로딩하여 재사용하는 방법을 배웁니다.
- **실습 내용**:
    - **데이터셋 로딩**: Pandas를 사용해 CSV 파일로부터 영화 리뷰 데이터를 로드합니다.
    - **텍스트 전처리**: 텍스트 데이터를 소문자로 변환하고, 불필요한 문장 부호나 특수 문자를 제거하는 등의 전처리 과정을 수행합니다.
    - **모델 학습**: `CountVectorizer`를 사용해 텍스트 데이터를 벡터화하고, Logistic Regression 모델을 학습시킵니다.
    - **모델 저장 및 로딩**: 학습된 모델을 Joblib을 사용해 저장한 후, 저장된 모델을 다시 로딩해 성능을 테스트합니다.
# 참고 자료
[네이버 영화 리뷰 감성 분류하기](https://wikidocs.net/44249)
[영화리뷰 감성분석 (Sentiment Analysis)](https://yeong-jin-data-blog.tistory.com/entry/%EC%98%81%ED%99%94%EB%A6%AC%EB%B7%B0-%EA%B0%90%EC%84%B1%EB%B6%84%EC%84%9D-Sentiment-Analysis)
[아나콘다 환경에서 konlpy 사용시 jvm.dll 못찾는 오류](https://rural-mouse.tistory.com/5)
[Tensorflow LSTM 모델 (public score : 0.848)](https://dacon.io/competitions/official/235864/codeshare/4160)
