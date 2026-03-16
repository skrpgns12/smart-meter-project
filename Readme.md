# 💧 스마트 미터 온디바이스(On-device) 누수 감지 시스템
> **비전공자 관점의 딥러닝 한계 극복 및 경량 머신러닝 최적화 프로젝트**

## 🎯 프로젝트 개요
상수도 스마트 미터 데이터를 활용하여 현장형 기기(저사양 CPU)에서 실시간으로 누수 및 이상 징후를 진단하는 AI 모델을 구축했습니다.

## 🚀 핵심 성과 (Key Results)
1. **모델 전략 수정:** 딥러닝(TSMixer)의 과도한 스무딩 문제를 **LightGBM**으로 해결하여 피크 재현력 확보
2. **실무형 알람 최적화:** 30분 지속성 필터(Persistence Filter) 도입으로 알람 횟수 62% 감소 (**262회 → 99회**)
3. **온디바이스 최적화:** PyTorch 등 무거운 라이브러리 없이 **LGBM + Isolation Forest** 조합으로 1ms 이내 추론 실현
4. **이중 검증 시스템:** 통계적 기법(Z-score)과 기계학습(Isolation Forest)의 교차 검증으로 오탐지(False Positive) 최소화

## 🛠 기술 스택 (Tech Stack)
- **Language:** Python 3.11
- **Models:** LightGBM, Isolation Forest, EWMA
- **Frameworks:** Darts (Baseline Study), Scikit-learn, Pandas, Joblib

## 📂 프로젝트 구조
- `/notebooks`: 
  - `01_data_load.ipynb`: 데이터 전처리 및 음수(Negative) 유량 보정
  - `02_model_tsmixer.ipynb`: 딥러닝 기반 성능 기준점 수립
  - `03_model_lightweight.ipynb`: 현장용 경량 모델 및 실무 필터 튜닝 (최종본)
- `/models`: 학습 완료된 배포용 모델 (.pkl)
- `inference.py`: 현장 기기용 실시간 추론 스크립트

## 📈 분석 인사이트
- 상수도 데이터는 계절적/시간적 패턴이 강해 단순 임계치 방식보다 **과거 데이터(Lag)**를 활용한 예측 모델이 유효함.
- 누수는 일시적인 이상치(Noise)와 구별되어야 하므로 **30분 연속 이상 발생 조건**이 현장 신뢰도를 높이는 결정적 요인이 됨." " 
" " 
