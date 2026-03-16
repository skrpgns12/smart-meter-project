import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# 1. 3대 핵심 모델 로드 (유량 예측, 수압 예측, 이상 탐지)
try:
    model_flow = joblib.load('./models/lgbm_leak_predictor.pkl')
    model_press = joblib.load('./models/pressure_predictor.pkl')
    iso_forest = joblib.load('./models/iso_forest_validator.pkl')
    print(f"[{datetime.now()}] ✅ 유량/수압 통합 진단 엔진 로드 완료")
except Exception as e:
    print(f"❌ 모델 로드 실패: {e}")

def run_inference(recent_features, current_actuals):
    """
    recent_features: 학습 시 사용한 features (Lag 데이터 등)
    current_actuals: [현재 유량, 현재 수압] 실측값
    """
    # 1. 유량(Flow) 및 수압(Pressure) 개별 예측
    pred_flow = model_flow.predict([recent_features])[0]
    pred_press = model_press.predict([recent_features])[0]
    
    # 2. 이상 탐지 엔진 검증 (Isolation Forest)
    is_anomaly = iso_forest.predict([current_actuals])[0] # -1이면 이상
    
    return {
        "flow_pred": pred_flow,
        "press_pred": pred_press,
        "is_anomaly": is_anomaly == -1
    }

if __name__ == "__main__":
    print("🚀 실시간 유량/수압 모니터링 가동 중...")
