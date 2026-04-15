# API

기본 prefix는 `/api/v1`입니다.

이미지 검색의 전체 설계 흐름은 [이미지 검색 흐름](image-search-flow.md)을 참고합니다.

## Health

```http
GET /health
```

응답:

```json
{
  "status": "ok",
  "service": "playground-clip",
  "environment": "local"
}
```

## Products

```http
GET /api/v1/products
```

응답:

```json
{
  "items": []
}
```

## Categories

```http
GET /api/v1/categories
```

응답:

```json
{
  "items": []
}
```

## Image Search

```http
POST /api/v1/image-search
Content-Type: application/json

{
  "image_url": "https://example.com/product.jpg",
  "top_k": 10,
  "category_id": null
}
```

응답:

```json
{
  "items": []
}
```
