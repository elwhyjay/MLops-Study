# MLops란 무엇인가

Created: September 4, 2024 7:36 AM

## MLops 의 정의

**MLOps** 또는 **ML Ops**는 프로덕션 환경에서 [기계 학습](https://ko.wikipedia.org/wiki/%EA%B8%B0%EA%B3%84_%ED%95%99%EC%8A%B5) 모델을 안정적이고 효율적으로 배포하고 유지하는 것을 목표로 하는 패러다임이다.[[1]](https://ko.wikipedia.org/wiki/MLOps#cite_note-tds1-1) 이 단어는 "머신러닝"과 소프트웨어 분야 [데브옵스](https://ko.wikipedia.org/wiki/%EB%8D%B0%EB%B8%8C%EC%98%B5%EC%8A%A4)의 지속적인 개발 관행의 합성어이다. - from. Wikipedia

—> 그렇다면 데브옵스(Devops)란?

Development + Operation 의 합성어로 개발과 운영에대한 “방법론”,”패러다임”. 어떻게 개발과 운영을 잘할것인가

***—> 만병통치약은 없고 요구 상황에 따른 설계가 필요***

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image.png)

### MLops의 요소들

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%201.png)

![Sculley, D. et al. “Hidden Technical Debt in Machine Learning Systems.” *Neural Information Processing Systems* (2015).](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2024-09-04_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%258C%25E1%2585%25A5%25E1%2586%25AB_7.42.52.png)

Sculley, D. et al. “Hidden Technical Debt in Machine Learning Systems.” *Neural Information Processing Systems* (2015).

### 그렇다면 왜 MLops가 Devops와 별도로 존재해야할까?

Machine Learning System은 데이터를 기반으로하고 데이터는 고정되어있지 않기 때문. → 전통적인 소프트웨어 개발론(Devops) 만으로는 부족하다

- 데이터 의존성
- 재현성 부채
- 추상화 부채

…. 

구글에서 말하는 MLops의 주요특징

- 실험적 개발 : 지속적인 모델에 대한 다양한 테스트 → 코드 재사용성을 극대화하면서 재현성을 유지해야함
- 테스팅: 일반적인 소프트웨어보다 복잡한 테스팅 ( 데이터 검증, 모델 평가 및 검증, 일반적인 단위 및 통합테스트)
- 배포: 다단계의 복잡한 파이프라인
- 운영: 지속적으로 변하는 데이터를 모니터링해서 핸들링해야함

### ML project의 생명주기

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/1e0e07cf-2b4e-423f-872e-abbbaf0461ed.png)

- Data Collection/Preparation , Feature engineering
    - CT(continuous training), serving, model개발 등을 위한 데이터를 준비
    - 데이터 버전 관리
    - 배치, 스트림 관리
- Model Training / Model evaluation
    - ML framework와 runtime환경제공
    - 리소스관리 (분산처리)
    - 효율적인 하이퍼파라미터 튜닝과 최적화( AutoML)
    - 평가데이터에 대한 성능측정
    - Continuous Training 과정에서 예측 성능 추적
    - 다양한 버전의 모델 / 데이터셋에 대한 성능비교
    - 시각화, XAI(explainable ai) 제공
- Model Deployment / serving
    - Online serving(실시간 예측), 배치 서빙 ( 대용량 처리) 지원
    - 서빙 framework 지원
    - 예측결과의 후처리
    - 트래픽관리
    - 로깅
- Model monitoring
    - 지연시간, 모델의 효율성, 정확도를 추적관찰
- Model maintainance
- Etc CI/CD

각각의 생명주기에서 사용되는 도구들…

- Docker, K8s
- Jeckins,
- MLflow, verta..
- Airflow, Argo workflow, Kuberflow..

→ 위 단계들은 서비스에 따라 통합 분리 되서 운영될 수 가있음.

→ 회사별, 서비스별 수많은 workflow가 존재

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%202.png)

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%203.png)

→ 많은 도구들 다 익히기는 불가능. 

## 단계별 MLops (by google)

### level 0. Manual Process

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%204.png)

- 빌드, 배포가 모두 수동으로 이루어짐
- 머신러닝 팀과 운영 팀의 분리
    - 머신러닝 팀이 학습시킨 모델을 운영팀에게 전달. 운영팀은 이 모델을 배포
- 모델 배포가 드물고 비정기적
- 변경사항이 적음
- 모니터링, 로깅이 이루어지지 않음

### Level 1. ML pipeline automation

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%205.png)

- ML 파이프라인을 자동화하여 지속적으로 모델을 학습시킴.
- 파이프라인 트리거, 메타데이터관리, 자동화된 데이터 및 모델 검증 시스템
- 개발과 운영의 통합
- CT(continuous Training)의 도입을 위한 추가사항.
    - 데이터, 모델 검증
    - Feature store
        - 원시데이터를 처리 및 가공하여 저장
    - 메타데이터 관리
    - ML pipeline triggers

### Level2 CI/CD 파이프라인 자동화

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%206.png)

- CI/CD 의 단계
    - 개발실험
    - CI
    - CD
    - 자동화된트리거
    - 모델배포
    - 모니터링

![image.png](MLops%E1%84%85%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%84%8B%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%207f5970f583a34db6b53477d9828d3f79/image%207.png)

- CI(continuous integration) 소스코드가 커밋되고 푸시될때 빌드, 테스트, 패키징이 자동으로 이루어짐. 추가로 아래 사항들 역시 포함될 수 있음
    - feature engineering unit test
    - model convergence test
    - testing integration between pipeline components
- CD(continuous delivery) 새 파이프라인 구현을 지속적으로 배포. 역시 다음이 포함될 수 있음
    - API호출 테스트
    - 모델과 인프라호환성 테스트
    - 서버 부하테스트
    - 예측 성능 목표치 확인

# 그렇다면 어떻게 MLops를 공부할것 인가?

- 강의나 책으로 기초다지기
- 프로젝트 수행하기 ( CT를 중점으로)
- 다양한 디자인 패턴 학습하기

---

# Reference

- https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- https://www.slideshare.net/slideshow/mlops-kr-mlops-210605/249041533
- https://www.slideshare.net/slideshow/understanding-mlops/247948407
- https://blogs.nvidia.com/blog/what-is-mlops/
- [Sculley, D. et al. “Hidden Technical Debt in Machine Learning Systems.” *Neural Information Processing Systems* (2015).](https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)
- https://github.com/EthicalML/awesome-production-machine-learning
- https://mercari.github.io/ml-system-design-pattern/README_ko.html
- [https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf](https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf)
- https://ml-ops.org/
- https://mlops-for-mle.github.io/tutorial/