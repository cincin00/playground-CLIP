# 이미지 기반 상품 검색 서비스

FastAPI, CLIP, OpenSearch를 기반으로 상품 이미지와 메타데이터를 활용해 유사 상품을 검색하는 API 서비스입니다.

## 빠른 실행

```bash
cp .env.example .env
docker compose up --build
```

API 상태 확인:

```bash
curl http://localhost:8000/health
```

## 로컬 개발

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
scripts/run_api.sh
```

테스트:

```bash
scripts/test.sh
```

## 주요 API

- `GET /health`: 서비스 상태 확인
- `GET /api/v1/products`: 상품 목록 조회
- `GET /api/v1/categories`: 카테고리 목록 조회
- `POST /api/v1/image-search`: 이미지 URL 기반 유사 상품 검색

## 문서

- [아키텍처](docs/architecture.md)
- [API](docs/api.md)
- [로컬 개발](docs/local-development.md)
