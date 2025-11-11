---
nav_title: API 사용 사례
article_title: API 사용 사례
description: "이 참조 문서는 숙련된 개발자든 최소한의 개발자 리소스를 보유한 마케터든 관계없이 Braze REST API의 강력한 기능을 활용하여 다양한 작업을 수행하고 고객 참여 전략을 강화하는 방법을 이해하는 데 도움을 주기 위해 작성되었습니다."
page_type: reference
page_order: 4.8
---

# API 사용 사례

> [Braze REST API]({{site.baseurl}}/api/basics/)는 고객 참여 전략을 관리하고 최적화하는 데 도움이 되도록 설계된 다양한 엔드포인트를 제공합니다. 이 문서에서는 카탈로그, 이메일 목록 및 주소, 내보내기, 메시지, 환경설정 센터, SMS, 수신 그룹, 템플릿 및 사용자 데이터 등 각 엔드포인트 컬렉션의 여러 사용 사례를 살펴봅니다.<br><br>각 섹션에서는 단계별 가이드, 코드 샘플 및 예상 결과와 함께 시나리오를 소개합니다. 이 글을 마치면 Braze REST API를 사용하여 고객 참여 노력을 강화하는 방법을 더 잘 이해할 수 있을 것입니다.

## 카탈로그에서 여러 항목 삭제하기

주방용품 전문 리테일 브랜드인 키친어리에서 새해를 맞이하여 신제품을 출시합니다. Braze 대시보드에서 키친리에는 "식기류"라는 식기류 컬렉션에 대한 카탈로그가 설정되어 있습니다. 새해에는 식기 컬렉션에서 다음 제품도 제외됩니다.

* 플레인 비스크
* 진주 도자기
* 핑크 쉬머

이러한 제품을 카탈로그에서 제거하기 위해 Kitchener는 [`/catalogs/{catalog_name}/items` 엔드포인트를]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/) 사용하여 품목 ID를 전달할 수 있습니다.

다음은 요청 예시입니다:

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

이 페이로드를 전송한 후 다음 응답을 통해 Kitchenerie의 식기류 카탈로그에서 세 가지 컬렉션의 제거가 완료되었음을 확인할 수 있습니다.

```json
{
  "message": "success"
}
```

## Braze 스팸 목록에서 이메일 삭제하기

스트리밍 서비스 회사인 MovieCanon의 개발자 팀은 이메일 목록을 주기적으로 감사하여 이메일 캠페인에 가입한 사용자를 식별하고 유지하는 업무를 담당하고 있습니다. 이 감사의 일환으로 MovieCanon은 이 이메일 목록을 스팸 목록에서 삭제하려고 합니다:

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

이 작업을 수행하려면 개발자 팀에 `/email/spam/remove` 엔드포인트를 사용할 수 있는 `email.spam.remove` 권한이 있는 API 키가 필요합니다. 이 엔드포인트는 Braze 스팸 목록과 MovieCanon의 이메일 제공업체가 관리하는 스팸 목록에서 이메일 주소를 제거합니다.

이 요청을 보내려면 문자열 이메일 주소 또는 수정할 이메일 주소의 배열을 최대 50개까지 포함하세요. 제거할 이메일 목록이 50개 미만이므로 MovieCanon은 다음 요청 본문으로 이 작업을 수행할 수 있습니다:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

이 페이로드를 성공적으로 전송한 후 이 응답은 이메일이 MovieCanon의 스팸 목록에서 제거되었음을 확인합니다.

```json
{
  "message": "success"
}
```

## 모든 캔버스 감사

시즈 밸리 헬스는 수천 명의 환자를 진료하는 10개의 병원과 연구 센터를 운영하는 병원 시스템입니다. 마케팅 팀은 환자에게 독감 예방주사 예약을 상기시키기 위해 보낸 캔버스를 지난 3년간의 Braze 사용 기간과 비교하고자 합니다. 시즈 밸리 헬스의 마케팅 팀은 또한 캔버스 목록과 분석 요약을 모두 빠르고 효율적으로 볼 수 있는 방법을 원했습니다.

시즈 밸리 헬스에서 Braze 대시보드를 통해 필터링하지 않고 엔드포인트 조합을 사용하여 이 두 가지 작업을 수행하는 방법에 대해 자세히 알아보겠습니다.

캔버스를 감사하는 첫 번째 작업의 경우 [`/canvas/list` 엔드포인트를]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) 사용하여 이름과 태그가 포함된 캔버스 목록을 내보냅니다. 다음은 요청 예시입니다:

{% details Here’s the response that the Siege Valley Health marketing team would receive. %}
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      },
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      },
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

시즈 밸리 헬스의 캔버스 목록에서 첫 번째 캔버스에 대한 분석 요약을 보는 다음 작업으로 넘어가겠습니다. 이를 위해 다음 요청 매개변수와 함께 [`/canvas/data_summary` 엔드포인트를]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) 사용합니다:

* `canvas_id`: "canvas_identifier_2"
* `ending_at`: 2023-07-10T23:59:59
* `starting_at`: 2020-07-10T23:59:59

다음은 요청 예시입니다:

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 예정된 캠페인 및 캔버스 확인

온라인과 매장에서 의류 및 뷰티 제품을 판매하는 소매 브랜드인 Flash & Thread의 연중 가장 바쁜 시기가 빠르게 다가오고 있습니다. 마케팅팀은 2024년 3월 31일 오후 12시 이전에 Braze 대시보드에서 예정된 캠페인과 캔버스를 확인하고자 합니다. 이 작업은 [`/messages/scheduled_broadcasts` 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) 사용하여 수행할 수 있습니다. 

다음은 요청 예시입니다:

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

이 엔드포인트는 예정된 캠페인 및 캔버스 목록을 반환합니다. 여기에서 마케팅 팀은 응답의 캠페인 및 캔버스에 대한 `name` 필드를 참조하여 메시지 목록을 확인할 수 있습니다.

## 이전 환경설정 센터 보기

PoliterWeekly는 이메일을 통해 구독자에게 도달할 수 있는 디지털 매거진입니다. 마케팅 팀은 구독자의 사용자 여정을 더 잘 이해하기 위해 PoliterWeekly의 환경설정 센터에 대한 세부 정보를 검토하여 언제 생성되고 마지막으로 업데이트되었는지 확인하고자 합니다.

마케팅 팀은 [`/preference_center/v1/{preferenceCenterExternalID}` 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)를 사용하여 다음과 같이 환경설정 센터 외부 ID를 경로 매개 변수로 삽입하기만 하면 됩니다.

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Here’s the response the PoliterWeekly marketing team would receive. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Your preferences have been updated successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

이 응답을 통해 마케팅 팀은 환경설정 센터가 가장 최근에 업데이트되기 3년 전에 만들어졌음을 알 수 있습니다. 이 정보를 염두에 두고 마케팅 팀은 새로운 환경설정 센터를 만들어 출시할 수 있습니다.

{% enddetails %}

## 유효하지 않은 전화번호 제거하기

CashBlastr의 주요 목표는 사람들이 빠른 결제를 주고받을 수 있는 방법을 간소화하는 것입니다. 금융 서비스 회사로서 CashBlastr는 고객의 전화번호 목록을 최신의 정확한 상태로 유지하고자 합니다. 개발자 팀은 마케팅 팀의 SMS 메시지가 적절한 CashBlastr 고객에게 전달될 수 있도록 '유효하지 않음'으로 표시된 다음 전화번호 목록을 제거해야 하는 임무를 받았습니다.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

[`/sms/invalid_phone_numbers/remove` 엔드포인트로]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) 요청을 보내려면 전화 번호는 [e.164 형식의](https://en.wikipedia.org/wiki/E.164) 문자열 배열이어야 하며 요청당 최대 50개의 전화 번호가 포함되어야 합니다. 전화번호 목록이 50개를 넘지 않으므로 다음은 CashBlastr의 개발팀이 보내는 요청 본문의 예시입니다:

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

이 페이로드를 전송한 후, 다음 응답을 통해 CashBlastr의 유효하지 않은 전화번호가 Braze 유효하지 않은 목록에서 제거되었음을 확인할 수 있습니다.

```json
{
  "message": "success"
}
```

## 사용자의 구독 그룹 상태 보기

미국의 퀵서비스 레스토랑 체인인 SandwichEmperor의 마케팅 팀은 무작위로 선정된 사용자 목록에 대한 SMS 구독 그룹 상태를 확인하려고 합니다. [`/subscription/status/get` 엔드포인트를]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) 사용하면 샌드위치엠퍼러는 다음 예제 요청을 통해 개별 사용자에 대해 이 작업을 수행할 수 있습니다:

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

이 엔드포인트에는 이메일에 대한 사용자의 구독 그룹 상태도 나열되며 여러 사용자의 구독 그룹 상태를 확인하는 데 사용할 수 있습니다.

## 이메일 메시징용 HTML 템플릿 확인

다양한 업계 종사자 간의 인맥 형성을 돕는 소셜 네트워크인 WorkFriends의 마케팅 팀은 사용자에게 이메일 캠페인을 보내는 업무를 담당합니다. 이러한 캠페인에는 종종 지역 이벤트 알림, 주간 뉴스레터, 프로필 활동 하이라이트가 포함됩니다.

이 시나리오에서 WorkFriends는 지금까지 기존 브랜딩과 함께 단일 HTML 템플릿을 사용해 왔습니다. 브랜드 아이덴티티를 맞추기 위해 WorkFriends는 새 템플릿으로 전환하기 전에 이 HTML 템플릿에 활용할 수 있는 유용한 정보가 있는지 확인하고자 합니다.

{% details Here’s the response that the WorkFriends team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

이 템플릿 정보를 검토한 후 WorkFriends는 [`/templates/email/update` 엔드포인트를]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) 사용하여 API를 통해 이메일 템플릿을 업데이트할 수도 있습니다. Braze 대시보드의 이메일 템플릿에 이러한 편집 내용이 반영됩니다.
