---
nav_title: "POST: 미디어 라이브러리에 자산을 업로드하세요."
article_title: "POST: 미디어 라이브러리에 자산을 업로드하세요."
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 `POST /media_library/create` 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 미디어 라이브러리에 자산을 업로드하세요.
{% apimethod post %}
/media_library/create
{% endapimethod %}

> 이 엔드포인트를 사용하여 외부 호스팅된 URL(`asset_url`) 또는 요청 본문에 전송된 이진 파일 데이터(`asset_file`)를 사용하여 [Braze 미디어 라이브러리](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library)에 자산을 추가하세요. 이 엔드포인트는 이미지와 이미지를 포함하는 ZIP 파일을 지원합니다.

## 필수 조건

이 엔드포인트를 사용하려면 `media_library.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

`asset_url`을 포함하면 엔드포인트가 URL에서 파일을 다운로드합니다. `asset_file`를 포함하면 엔드포인트가 요청 본문의 이진 데이터를 사용합니다.

`asset_url`에 대한 예제 요청 본문:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

`asset_file`에 대한 예제 요청 본문:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

요청 본문에는 다음 매개변수가 포함됩니다:

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Optional | 문자열 | Braze에 업로드할 자산의 공개적으로 접근 가능한 URL입니다. |
| `asset_file` | Optional | 이진 | 이진 파일 데이터입니다. |
| `name` | Optional | 문자열 | 이 자산에 대해 미디어 라이브러리에 표시될 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url`와 `asset_file`는 상호 배타적이며, API 요청에 둘 중 하나만 포함해야 합니다.
{% endalert %}

### 업로드된 파일 이름

이 섹션에서는 `name` 매개변수를 포함하는지 여부에 따라 엔드포인트가 업로드된 파일에 이름을 할당하는 방법을 설명합니다.

#### 단일 파일 업로드

| 시나리오 | 결과 |
| --- | --- |
| 제공된 `name` | `name` 값은 미디어 라이브러리에서 자산 이름으로 사용됩니다. |
| 제외된 `name` | URL 또는 업로드된 파일의 원래 파일 이름이 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### ZIP 파일 업로드

| 시나리오 | 결과 |
| --- | --- |
| 제공된 `name` | `name` 값은 접두사로 사용되며, 접미사로 증가하는 숫자가 추가됩니다 (예: "내 파일 1", "내 파일 2", "내 파일 3"). |
| 제외된 `name` | 각 파일은 ZIP 파일 내의 원래 파일 이름을 유지합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## 예시 요청

이 섹션에는 URL을 사용하여 자산을 추가하는 요청과 이진 파일 데이터를 사용하는 요청의 두 가지 예제 `curl` 요청이 포함되어 있습니다.

이 요청은 `asset_url`을 사용하여 미디어 라이브러리에 자산을 추가하는 예를 보여줍니다.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

이 요청은 `asset_file`을 사용하여 미디어 라이브러리에 자산을 추가하는 예를 보여줍니다.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### 오류 응답

이 섹션은 잠재적인 오류와 해당 메시지 및 설명을 나열합니다. 

#### 유효성 검사 오류

유효성 검사 오류는 다음과 같은 구조를 반환합니다:

```json
{
  "message": (String) Human-readable error description
}
```

이 표는 가능한 유효성 검사 오류를 나열합니다.

| HTTP 상태 | 메시지 | 설명 |
| --- | --- | --- |
| 400 | "asset_url 또는 asset_file 중 하나는 제공되어야 합니다." | 요청에 자산 매개변수가 제공되지 않았습니다. |
| 400 | "asset_url과 asset_file는 동시에 제공될 수 없습니다." "하나만 제공해 주세요." | 두 개의 자산 매개변수가 제공되었습니다; 하나만 허용됩니다. |
| 403 | "미디어 라이브러리 공개 API는 이 회사에 대해 활성화되어 있지 않습니다." | 이 작업 공간에 대해 미디어 라이브러리 기능이 활성화되어 있지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 처리 오류

처리 오류는 오류 코드와 함께 다른 응답을 반환합니다:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

이 표는 가능한 처리 오류를 나열합니다.

| 오류 코드 | HTTP 상태 | 설명 |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | 업로드된 파일 형식은 지원되지 않습니다. `meta` 객체에는 거부된 `file_type`가 포함되어 있습니다. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | 파일이 허용된 최대 크기를 초과했습니다. 이미지는 5MB 제한이 있습니다. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | 작업 공간은 최대 자산 수(무료 평가판 회사의 경우 기본적으로 200개, 그 외에는 무제한)에 도달했습니다. `meta` 객체에는 현재 `limit`가 포함되어 있습니다. |
| `ASSET_UPLOAD_FAILED` | 400 | 자산이 처리 문제로 인해 업로드에 실패했습니다. |
| `ZIP_UPLOAD_ERROR` | 400 | ZIP 파일이 손상되었거나 열 수 없습니다. `meta` 객체에는 `original_error` 메시지가 포함되어 있습니다. |
| `ZIP_FILE_TOO_LARGE` | 400 | ZIP 파일의 총 압축 해제 크기가 5MB 제한을 초과합니다. `meta` 객체에는 `zip_file_name`와 `zip_file_size`이 포함되어 있습니다. |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | ZIP 내부의 파일 항목에 이름이 없습니다. ZIP 파일이 손상되지 않았는지 확인하고 이름이 없는 파일 항목에 이름을 추가하세요. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | ZIP 파일에는 지원되지 않는 중첩 디렉토리가 포함되어 있습니다. 모든 파일은 ZIP의 루트 수준에 있어야 합니다. |
| `GENERIC_ERROR` | 500 | 업로드 중 예기치 않은 오류가 발생했습니다. `meta` 객체에는 디버깅을 위한 `original_error` 메시지가 포함되어 있습니다. 다시 시도하거나 [지원]({{site.baseurl}}/support_contact/)에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Response

이 엔드포인트에 대한 다섯 가지 상태 코드 응답이 있습니다: `200`, `400`, `403`, `429`, 및 `500`.

다음 JSON은 응답의 예상 형식을 보여줍니다.

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}
