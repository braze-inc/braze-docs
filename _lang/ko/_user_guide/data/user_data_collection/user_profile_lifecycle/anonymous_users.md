---
nav_title: 익명 사용자
article_title: 익명 사용자
page_order: 0
page_type: reference
description: "이 도움말에서는 익명 사용자와 사용자 별칭에 대한 개요와 함께 그 중요성 및 메시지에서 이를 활용하는 방법을 간략하게 설명합니다."

---

# 익명 사용자

> 게스트 방문자처럼 로그인하지 않고 웹사이트나 애플리케이션을 방문하는 사용자는 익명 사용자로 인식됩니다. 이러한 사용자에게는 Braze API로 사용자 프로필을 업데이트하는 데 사용되는 `external_ids` 이 없지만 여전히 [데이터 포인트가]({{site.baseurl}}/user_guide/data/data_points/) 할당되어 있으며 세그먼트에서 타겟팅할 수 있습니다.

익명의 사용자가 웹사이트나 애플리케이션을 방문하면 Braze SDK가 '익명' 사용자 프로필을 생성하여 할당합니다. 사용자가 브라우징하는 동안 사용자 지정 속성 및 사용자 지정 이벤트를 설정한 경우 SDK는 사용 정보, 디바이스 정보 등 익명 사용자 프로필에 대한 데이터를 자동으로 캡처합니다.

캡처한 익명 사용자로 다음을 수행할 수 있습니다:

- 로그인하기 전에 사용자에게 메시지 보내기
- 로그인하기 전에 사용자의 프로필을 수집하여 관련 데이터를 놓치지 마세요.
- 사용자가 프로필을 부분적으로만 작성한 경우 메시지로 프로필 작성을 독려하세요.
- 로그인 시 사용자의 프로필을 작성하면 다른 플랫폼에서 메시지를 취소할 수 있습니다(예: 사용자가 이미 앱을 주문한 경우 '첫 번째 앱 주문 시 무료 배송' 메시지를 보내지 않음).
- 이탈 의사를 보이는 사용자에게 프로필 생성, 장바구니 결제 또는 다른 조치를 취하도록 유도하여 참여를 유도하세요.

## How it works

{% multi_lang_include 익명 사용자/about_anonymous_users.md 섹션='user_guide' %}

## 사용자 별칭 할당

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## 익명 사용자 병합하기  

익명 사용자 프로필이 다른 사용자 프로필과 전화번호나 이메일 주소가 같은 중복 프로필인 경우가 있습니다. 중복된 항목 중 하나는 식별된 사용자 프로필일 수도 있습니다. 이러한 중복된 프로필은 [POST를 사용하여 하나의 사용자 프로필로 병합할 수 있습니다: 사용자 병합 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 또는 Braze 플랫폼의 병합 도구(예: [규칙 기반 병합]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)) 중 하나를 선택합니다.

## 사용 사례

### 세그먼트의 익명 사용자 타겟팅

익명 사용자는 `external_id` 이 없으므로 세분화 필터 **외부 사용자 ID가 비어 있음** 을 사용하여 일괄적으로 타겟팅할 수 있습니다. 정확도를 높이려면 타겟팅하려는 익명 사용자에 사용자 지정 속성을 추가하고 해당 속성을 필터링할 수 있습니다.

각 익명 사용자 프로필에 사용자 지정 속성 "is_lead_profile"을 할당한다고 가정해 보겠습니다. 이러한 필터 중 하나 또는 둘 모두를 사용하여 이러한 프로필을 타겟팅할 수 있습니다:

- **외부 사용자 ID가 비어 있습니다.**
- "IS_LEAD_PROFILE" **이 참입니다**.

![빈 외부 사용자 ID와 참 "is_lead_profile" 사용자 지정 속성에 대해 세그먼트 필터를 적용합니다.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### 익명 사용자의 결제 데이터 캡처

결제 프로세스 중에 사용자 별칭 프로필을 생성하여 익명 사용자(또는 게스트 방문자)의 결제 데이터를 캡처할 수 있습니다. 익명의 사용자가 웹 캡처 양식을 사용하여 결제할 때 API 호출 트리거를 사용하여 사용자 별칭 프로필을 생성하고 구매 이벤트를 기록합니다. 그런 다음 Braze API를 통해 생성된 사용자 프로필을 업데이트할 수 있습니다.

다음은 웹 캡처 양식이 제출될 때 생성되는 페이로드의 예시입니다:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}

