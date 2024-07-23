---
nav_title: "POST: 트리거 동기화"
article_title: "POST: 트리거 동기화"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "이 문서에서는 동기화 트리거 Braze 엔드포인트에 대한 세부정보를 설명합니다."

---
{% api %}
# 동기화 트리거
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 통합에 대한 동기화를 트리거합니다.

{% alert note %}
이 엔드포인트를 사용하려면 `cdi.integration_sync` 권한이 있는 API 키를 생성해야 합니다.
{% endalert %}

## 비율 제한

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `integration_id`| 필수 | 문자열 | 통합 ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 예시 요청

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

### 성공 응답 예시

`202` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나열되어 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `400 Invalid integration ID`| 당신의 `integration_id`유효합니다. |
| `404 Integration not found`| 해당 통합 ID에 대한 통합이 없습니다. 통합 ID가 유효한지 확인하세요. |
| `429 Another job is in progress`| 현재 이 통합에 대해 동기화가 실행 중입니다. 동기화가 완료된 후 다시 시도하세요. |
{: .reset-td-br-1 .reset-td-br-2}

추가 상태 코드 및 관련 오류 메시지는[심각한 오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

{% endapi %}
