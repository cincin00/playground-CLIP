# 📌개요

상품 이미지로 보유한 이미지 데이터와 유사한 상품을 추천 또는 검색하는 서비스.

# 🎯목표

구매자가 전달한 이미지로 보유한 상품 이미지와 비교하여 최대한 정확도가 높은 상품을 검색하게 한다.

# 🤖모델

- ❌ **CLIP(Contrastive Language–Image Pretraining)**
    - **개요**
        - 이미지와 문장을 같은 좌표계에 놓고 학습한 신경망 모델.
    - **특징**
        - 직접적인 최적화 작업 없이도 이미지가 주어졌을 때 가장 관련 성 높은 텍스트 조각을 예측하도록 자연어로 학습 시킬 수 있다.
    - **참고**
        - https://arxiv.org/abs/2103.00020
        - https://github.com/openai/CLIP
- ✅ **OpenCLIP - 사유: CLIP 모델 기반으로 LAION 데이터셋을 학습했기 때문에 우수한 성능.**
    - **개요**
        - OpenAI CLIP 오픈소스 재구현
    - **특징**
        - 레이언(LAION ) 대규모 데이터로 재학습
            - 레이언 데이터 구조: `이미지 URL` + `텍스트 설명(Caption)`
            - 규모
                - LAION-400M → 4억 개
                - LAION-2B → 20억 개
                - LAION-5B → 약 58억 개

> 📖
> **LAION(레이언 / LAION, Large-scale Artificial Intelligence Open Network)**
> - 독일 기반 비영리 AI 단체.
> - 대규모 이미지 + 텍스트 데이터셋을 공개하는 조직

## 상세 모델

https://huggingface.co/openai/clip-vit-base-patch32

https://huggingface.co/openai/clip-vit-large-patch14

https://huggingface.co/patrickjohncyh/fashion-clip