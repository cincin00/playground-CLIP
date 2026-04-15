# 로컬 개발

## 개발 환경

| 기술스택분류 | 기술스택명 |
| --- | --- |
| 언어 | Python 3.13 |
| API 프레임워크 | FastAPI |
| ASGI 서버 | Uvicorn |
| 설정 관리 | Pydantic Settings |
| 데이터베이스 ORM | SQLAlchemy |
| 마이그레이션 | Alembic |
| 벡터 검색 엔진 | OpenSearch |
| OpenSearch 클라이언트 | opensearch-py |
| 캐시/작업 큐 기반 | Redis |
| 이미지/벡터 처리 | OpenCLIP, PyTorch, NumPy, Pillow |
| HTTP 클라이언트 | HTTPX |
| 컨테이너 | Docker, Docker Compose |
| 테스트 | pytest, pytest-asyncio |
| 린트/포맷 | Ruff |
| 타입 검사 | mypy |
| 커밋 전 검사 | pre-commit |

## 환경변수

```bash
cp .env.example .env
```

주요 설정:

- `APP_PORT`: API 노출 포트
- `DATABASE_URL`: SQLAlchemy DB URL
- `OPENSEARCH_HOST`: OpenSearch endpoint
- `OPENSEARCH_INDEX`: 상품 검색 인덱스명
- `CLIP_MODEL_NAME`: CLIP 모델명
- `CLIP_DEVICE`: `cpu` 또는 `cuda`

## Docker Compose

```bash
docker compose up --build
```

상태 확인:

```bash
curl http://localhost:8000/health
```

## Python 개발환경

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

API 실행:

```bash
scripts/run_api.sh
```

상품 색인 배치:

```bash
scripts/index_products.sh
```

테스트:

```bash
scripts/test.sh
ruff check .
mypy app
```
