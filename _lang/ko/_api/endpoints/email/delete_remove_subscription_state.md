---
nav_title: "DELETE: 이메일 주소 또는 전화번호로 구독 상태 삭제하기"
article_title: "DELETE: 이메일 주소 또는 전화번호로 구독 상태 삭제하기"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "이 기사는 이메일 주소 또는 전화번호 Braze 엔드포인트에 의한 구독 삭제 상태에 대한 세부 정보를 설명합니다."

---

{% api %}
# 이메일 주소 또는 전화번호로 구독 상태 삭제하기
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> 이 엔드포인트를 사용하여 이메일 주소 또는 전화번호를 기준으로 구독 상태 값을 삭제할 수 있습니다.

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `email` | 예 | 문자열 | 사용자의 이메일 주소(최소 1개, 최대 50개의 주소를 포함해야 함). |
| `phone` | 예 | 문자열 | 사용자의 전화번호(최소 1개에서 최대 50개의 전화번호를 포함해야 함). E.164 형식으로 제공하는 것이 좋습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## 응답

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}
