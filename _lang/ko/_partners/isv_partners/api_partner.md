---
nav_title: API 파트너 통합
alias: /api_partner_integration/
hidden: true
---

# API 파트너 통합

Alloys ISV 파트너는 API 요청의 `partner` 필드에 파트너 이름을 추가해야 합니다. 이를 통해 Braze는 파트너로부터 들어오는 요청 등 API 파트너의 사용 현황을 추적할 수 있습니다. 구현을 개발할 때 다음 [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트 구조를 참조하세요.

## 파트너 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
   "partner" : (required, string)
}
```