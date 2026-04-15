# 아키텍처

## 서비스 목표

이미지 또는 이미지 URL을 입력받아 보유 상품 이미지와 비교하고, 동일하거나 유사한 상품을 추천하는 검색 API를 제공합니다.

## 처리 흐름

1. 클라이언트가 이미지 URL과 검색 조건을 API에 전달합니다.
2. 이미지 검색 도메인이 CLIP adapter를 통해 이미지 임베딩을 생성합니다.
3. OpenSearch repository가 상품 벡터 인덱스에서 유사 상품을 조회합니다.
4. 도메인 서비스가 결과를 API 응답 모델로 정리합니다.

## 계층 구조

- `app/api`: FastAPI router와 endpoint
- `app/domain`: 상품, 카테고리, 이미지 검색 도메인 로직
- `app/infra`: DB, OpenSearch, CLIP, 외부 API adapter
- `app/core`: 설정, 로깅, 보안, DB 공통 설정
- `app/common`: 공통 예외, 응답, 유틸
- `app/jobs`: 상품 색인과 재색인 같은 배치 작업
- `migrations`: Alembic 마이그레이션

## 인프라

로컬 개발 기본 구성은 API, OpenSearch, Redis입니다. OpenSearch는 벡터 검색 인덱스를 담당하고, Redis는 캐시나 비동기 작업 큐 도입 시 사용합니다.
