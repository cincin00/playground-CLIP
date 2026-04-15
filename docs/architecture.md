# 아키텍처

## 서비스 목표

- 사용자가 업로드한 이미지 또는 이미지 URL을 기준으로 유사 상품을 검색합니다.
- 상품 이미지, 상품 텍스트, 메타데이터를 함께 활용해 검색 정확도를 높입니다.
- OpenCLIP 기반 임베딩을 사용해 이미지와 텍스트를 같은 벡터 검색 흐름에서 처리합니다.

## 서비스 정의

상품 이미지를 입력받아 쇼핑몰이 보유한 상품 이미지 및 상품 정보를 기반으로 동일하거나 유사한 상품을 찾아주는 검색 서비스입니다.

## 핵심 처리 방향

- 사용자 입력은 이미지 또는 이미지 URL입니다.
- 현재 구현된 API는 이미지 URL 입력을 기본으로 합니다.
- 검색은 이미지 임베딩을 기준으로 시작합니다.
- 이후 상품 텍스트와 메타데이터를 함께 반영해 결과를 재정렬하는 방향으로 확장합니다.
- 최종적으로 쇼핑몰 UI에 유사 상품 목록을 반환합니다.

## 전체 서비스 구성도

```mermaid
flowchart LR
    U[사용자] --> UI[퍼스트몰 이미지 검색 UI]

    UI -->|이미지 업로드 / URL 입력 / 필터 선택| ABE[퍼스트몰 백엔드]
    ABE -->|이미지 또는 URL + 필터 정보 전달| BAPI[이미지 검색 서비스 API]

    BAPI --> IMG[이미지 확보]
    IMG --> PRE[이미지 전처리]
    PRE --> QEMB[OpenCLIP 입력 이미지 임베딩 생성]

    QEMB --> VSEARCH[벡터 검색 엔진]
    VSEARCH --> RERANK[메타데이터 필터링 및 재정렬]
    RERANK --> RES[유사 상품 결과 생성]

    RES --> ABE
    ABE --> UI
    UI --> U

    IDX[상품 색인 파이프라인] --> VSEARCH
```

## 컨테이너 구성도

```mermaid
flowchart LR
    UA[사용자 브라우저] --> WA[퍼스트몰 웹 서버]
    WA --> AA[퍼스트몰 API 서버]
    AA --> BS[이미지 검색 서비스]

    BS --> REDIS[(Redis Cache)]
    BS --> VDB[(OpenSearch / Vector DB)]
    BS --> OBJ[(Object Storage)]
    BS --> MODEL[OpenCLIP Inference Runtime]

    IDXJOB[상품 색인 배치 작업] --> MODEL
    IDXJOB --> VDB
    IDXJOB --> OBJ

    ADM[운영자 / 배치 스케줄러] --> IDXJOB
```

## 현재 코드 계층

- `app/api`: FastAPI router와 endpoint
- `app/domain`: 상품, 카테고리, 이미지 검색 도메인 로직
- `app/infra`: DB, OpenSearch, CLIP, 외부 API adapter
- `app/core`: 설정, 로깅, 보안, DB 공통 설정
- `app/common`: 공통 예외, 응답, 유틸
- `app/jobs`: 상품 색인과 재색인 같은 배치 작업
- `migrations`: Alembic 마이그레이션

## 인프라

로컬 개발 기본 구성은 API, OpenSearch, Redis입니다. OpenSearch는 벡터 검색 인덱스를 담당하고, Redis는 캐시나 비동기 작업 큐 도입 시 사용합니다.
