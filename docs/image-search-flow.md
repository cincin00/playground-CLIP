# 이미지 검색 흐름

## 목적

사용자가 입력한 이미지 또는 이미지 URL을 기준으로 유사 상품 후보를 찾고, 필터와 메타데이터 점수를 반영해 최종 검색 결과를 반환합니다.

현재 구현된 API는 `image_url` 요청을 받는 최소 엔드포인트입니다. 이미지 파일 업로드, 실제 CLIP 임베딩 생성, OpenSearch 검색, 재정렬은 설계 및 개발 예정 흐름입니다.

## 이미지 검색 기능 흐름

```mermaid
flowchart TD
    REQ[퍼스트몰로부터 검색 요청 수신] --> INPUTCHK[입력값 검증]
    INPUTCHK --> IMGLOAD[이미지 파일 수신 또는 URL 다운로드]
    IMGLOAD --> PRE[이미지 전처리]
    PRE --> QEMB[OpenCLIP 입력 이미지 임베딩 생성]

    QEMB --> TOPK[상품 벡터 Top-K 검색]
    TOPK --> FILTER[필터 조건 적용]
    FILTER --> SCORE[유사도 점수 + 메타데이터 점수 재계산]
    SCORE --> FINAL[최종 랭킹 결과 생성]
    FINAL --> RESP[퍼스트몰로 응답 반환]
```

## 개발 항목

- 이미지 입력 엔드포인트 개발
- 이미지 데이터 전처리 기능 개발
- CLIP 모델을 위한 이미지 데이터 서빙 구조 개발
- 벡터화 정보에 기반한 상품 검색 기능 개발

## 최종 점수 계산

```mermaid
flowchart LR
    QV[입력 이미지 벡터] --> ISIM[이미지 유사도 계산]
    TV[상품 텍스트 벡터] --> TSIM[텍스트 유사도 계산]
    META[브랜드/카테고리/가격/재고 메타데이터] --> MSCORE[메타데이터 점수 계산]

    ISIM --> FSCORE[최종 점수 계산]
    TSIM --> FSCORE
    MSCORE --> FSCORE

    FSCORE --> RANK[최종 상품 랭킹]
```

## 검색 시퀀스

```mermaid
sequenceDiagram
    autonumber
    actor User as 사용자
    participant FMUI as 퍼스트몰 솔루션 UI
    participant FMAPI as 퍼스트몰 솔루션 백엔드
    participant ISAPI as 이미지 검색 서비스 API
    participant PRE as 이미지 전처리 모듈
    participant CLIP as OpenCLIP 임베딩 모듈
    participant VDB as Vector DB / OpenSearch
    participant RANK as 재정렬 모듈

    User->>FMUI: 이미지 업로드 또는 이미지 URL 입력
    FMUI->>FMAPI: 이미지/URL 및 선택적 필터 전달
    FMAPI->>ISAPI: 이미지 검색 요청 전달

    alt 이미지 파일 전달
        ISAPI->>ISAPI: 이미지 바이너리 수신
    else 이미지 URL 전달
        ISAPI->>ISAPI: URL 기반 이미지 다운로드
    end

    ISAPI->>PRE: 이미지 전처리 요청
    PRE-->>ISAPI: 전처리 완료 이미지 반환

    ISAPI->>CLIP: 입력 이미지 임베딩 생성 요청
    CLIP-->>ISAPI: 입력 이미지 벡터 반환

    ISAPI->>VDB: 상품 벡터 Top-K 유사도 검색 요청
    VDB-->>ISAPI: 후보 상품 목록 및 유사도 점수 반환

    ISAPI->>RANK: 후보 상품 재정렬 요청
    Note over RANK: 이미지 유사도 + 텍스트 유사도 + 메타데이터 필터 반영
    RANK-->>ISAPI: 최종 추천 상품 목록 반환

    ISAPI-->>FMAPI: 유사 상품 결과 반환
    FMAPI-->>FMUI: 검색 결과 전달
    FMUI-->>User: 동일/유사 상품 노출
```
