---
nav_title: 익명 사용자
article_title: 익명 사용자
page_order: 0
page_type: reference
description: "이 문서는 익명 사용자 및 사용자 별명에 대한 개요를 제공하며, 그 중요성과 메시지에서 어떻게 활용할 수 있는지를 설명합니다."

---

# 익명 사용자

> 로그인하지 않고 웹사이트나 애플리케이션을 방문하는 사용자, 즉 게스트 방문자는 익명 사용자로 인식됩니다. 이 사용자들은 `external_ids`이 없으며, 이는 Braze API를 사용하여 사용자 프로필을 업데이트하는 데 사용되지만, 여전히 [데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)가 할당되어 있으며, 세그먼트에서 타겟팅할 수 있습니다.

익명 사용자가 웹사이트나 애플리케이션을 방문하면 Braze SDK가 그들에게 "익명" 사용자 프로필을 생성하고 할당합니다. 사용자가 탐색하는 동안 SDK는 사용 정보, 장치 정보 등과 같은 익명 사용자 프로필에 대한 데이터를 자동으로 캡처하며, 사용자 정의 속성과 사용자 정의 이벤트를 설정한 경우 더 많은 정보를 캡처할 수 있습니다.

캡처된 익명 사용자로 다음과 같은 작업을 수행할 수 있습니다:

- 사용자가 로그인하기 전에 메시지 전송
- 사용자가 로그인하기 전에 프로필을 수집하여 관련 데이터를 놓치지 않도록 합니다.
- 사용자가 프로필을 부분적으로만 완료했을 때 메시지를 통해 프로필 완성을 유도합니다.
- 사용자가 로그인할 때 프로필을 완성하여 다른 플랫폼에서의 메시징을 취소할 수 있습니다(예: 사용자가 이미 앱 주문을 한 경우 "첫 앱 주문 무료 배송" 메시지를 보내지 않음).
- 프로필을 생성하거나 장바구니를 확인하거나 다른 행동을 취하도록 유도하여 이탈 의사를 보이는 사용자와 소통합니다.

## 작동 방식

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## 사용자 별명 할당

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## 익명 사용자 병합  

때때로 익명 사용자 프로필은 다른 사용자 프로필과 동일한 전화번호나 이메일 주소를 가진 중복 항목입니다. 중복 항목 중 하나는 식별된 사용자 프로필일 수도 있습니다. 이 중복 항목은 [POST:를 사용하여 하나의 사용자 프로필로 병합할 수 있습니다. Braze 플랫폼에서 사용자 병합 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 또는 [규칙 기반 병합]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)과 같은 병합 도구 중 하나를 사용하세요.

## 사용 사례

### 세그먼트에서 익명 사용자 타겟팅

익명 사용자는 `external_id`이 없기 때문에 세그먼트 필터 **외부 사용자 ID가 비어 있음**를 사용하여 대량으로 타겟팅할 수 있습니다. 정확성을 높이기 위해 타겟팅하려는 익명 사용자에게 사용자 정의 속성을 추가할 수 있습니다.

각 익명 사용자 프로필에 사용자 정의 속성 "is_lead_profile"을(를) 할당한다고 가정해 보겠습니다. 다음 필터 중 하나 또는 둘 다로 이러한 프로필을 타겟팅할 수 있습니다:

- **외부 사용자 ID가 비어 있음**
- "is_lead_profile" **참**

\![비어 있는 외부 사용자 ID와 참 "is_lead_profile" 사용자 정의 속성에 대한 세그먼트 필터.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### 익명 사용자로부터 체크아웃 데이터 캡처

체크아웃 과정에서 사용자 별칭 프로필을 생성하여 익명 사용자(또는 게스트 방문자)로부터 체크아웃 데이터를 캡처할 수 있습니다. 익명 사용자가 웹 캡처 양식을 사용하여 체크아웃할 때, 사용자 별칭 프로필을 생성하고 구매 이벤트를 기록하기 위해 API 호출을 트리거하세요. 그런 다음 Braze API를 통해 생성된 사용자 프로필을 업데이트할 수 있습니다.

웹 캡처 양식이 제출될 때 생성될 예제 페이로드는 다음과 같습니다:

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

