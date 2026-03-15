📂 프로젝트 진행 상황 리포트
1. 데이터 준비 (Data Engineering)
-원본 데이터: L001_2504021029.txt (약 8개월치 스마트 미터 기록)
수행 작업:
-비정형 텍스트 데이터를 Pandas로 로드하여 컬럼명(ID, Timestamp, Flow_Instant, Pressure 등) 부여.
-날짜와 시간을 합쳐 정교한 시계열 타임스탬프 생성.
-AI 모델이 읽기 쉬운 정형 데이터인 smart_meter_data.csv로 변환 완료.
데이터 특징:
-기간: 2024-07-20 ~ 2025-04-02 (약 8.5개월)
-행 수: 36,864개 (약 10분 단위 수집 데이터)

2. 전략 수립 (AI Research via Perplexity Pro)
-예측 목표: 향후 7일(1주일) 치의 유량과 수압 수치 동시 예측.
-모델 선정: 최신 다변량 시계열 모델인 TSMixer 채택.
-이유: 유량과 수압의 강한 상관관계를 동시에 학습(Multi-task Learning)하여 정확도 향상.
-학습 설정:
--입력(Look-back Window): 과거 14~28일치 데이터를 보고 패턴 학습.
--출력(Horizon): 미래 7일치 데이터 생성.

3. 개발 환경 설정 (Environment)
-IDE: VS Code (Jupyter Notebook 확장 활용).
-하드웨어: CPU 기반 환경 (GPU 미사용).
-주요 라이브러리: Darts (시계열 전문 프레임워크), Pandas, PyTorch.

🚀 다음 단계 (Next Action)
이제 02_model_training.ipynb 파일을 만드시고, 제가 드린 TSMixer 학습 코드를 넣고 실행할 차례입니다.
실행 전 주의사항:
라이브러리 설치: 터미널에서 pip install darts matplotlib torch 명령어를 꼭 먼저 실행해 주세요.
경로 확인: pd.read_csv('../data/processed/smart_meter_data.csv') 경로가 실제 파일 위치와 맞는지 확인하세요.