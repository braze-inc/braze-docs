---
nav_title: 사용자 업데이트
article_title: 사용자 업데이트 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "이 참조 문서에서는 사용자 업데이트 구성 요소와 캔버스에서 이를 사용하는 방법에 대해 설명합니다."
tool: Canvas
---

# 사용자 업데이트 

> 사용자 업데이트 컴포넌트를 사용하면 JSON 컴포저에서 사용자의 속성, 이벤트 및 구매를 업데이트할 수 있으므로 API 키와 같은 민감한 정보를 포함할 필요가 없습니다.

## 이 구성 요소의 작동 방식

"프리미엄 회원입니다" 속성을 "true"로 업데이트하는 "로열티 업데이트"라는 이름의 사용자 업데이트 단계입니다.]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

캔버스에서 이 구성 요소를 사용하는 경우 업데이트는 분당 요청 수( `/users/track` ) 제한에 포함되지 않습니다. 대신 이러한 업데이트는 일괄 처리되므로 Braze 간 웹훅보다 더 효율적으로 처리할 수 있습니다. 이 컴포넌트는 청구할 수 없는 데이터 포인트(예: 구독 그룹)를 업데이트하는 데 사용될 때는 [데이터 포인트를]({{site.baseurl}}/user_guide/data/data_points/) 기록하지 않습니다.

사용자는 관련 사용자 업데이트가 완료된 후에만 다음 캔버스 단계로 진행할 수 있습니다. 즉, 이러한 사용자 업데이트에 의존하는 모든 후속 메시징은 다음 단계가 실행될 때 최신 상태로 유지됩니다.

## 사용자 업데이트 만들기

사이드바에서 컴포넌트를 드래그 앤 드롭하거나 배리언트 또는 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **사용자 업데이트를** 선택합니다. 

기존 고객 프로필 정보를 업데이트하거나, 새로 추가하거나, 삭제할 수 있는 세 가지 옵션이 있습니다. 워크스페이스의 사용자 업데이트 단계를 모두 합치면 분당 최대 200,000개의 고객 프로필을 업데이트할 수 있습니다.

{% alert tip %}
사용자를 검색하고 변경 사항을 적용하여 이 구성 요소로 변경한 내용을 테스트할 수도 있습니다. 그러면 사용자가 업데이트됩니다.
{% endalert %}

### 커스텀 속성 업데이트하기

커스텀 속성을 추가하거나 업데이트하려면 속성 목록에서 속성 이름을 선택하고 키 값을 입력합니다.

!"로열티 회원" 및 "로열티 프로그램" 두 속성을 "true"로 업데이트하는 사용자 업데이트 단계입니다.]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### 커스텀 속성 제거하기

커스텀 속성을 제거하려면 드롭다운을 사용하여 속성 이름을 선택합니다. [고급 JSON 작성기로](#advanced-json-composer) 전환하여 추가로 편집할 수 있습니다. 

!"로열티 회원" 속성을 제거하는 사용자 업데이트 단계입니다.]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### 값 증가 및 감소

사용자 업데이트 단계는 속성 값을 높이거나 낮출 수 있습니다. 속성을 선택하고 **증분** **기준** 또는 **감산을** 선택한 다음 숫자를 입력합니다. 

#### 주간 진행 상황 추적

이벤트를 추적하는 커스텀 속성을 증가시켜 사용자가 일주일 동안 수강한 수업 수를 추적할 수 있습니다. 이 구성 요소를 사용하면 주 초에 수업 수를 재설정하고 추적을 다시 시작할 수 있습니다. 

사용자 업데이트 단계는 "class_count" 속성을 1씩 증가시킵니다.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### 오브젝트 배열 업데이트하기

[오브젝트 배열은]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) 데이터가 풍부한 사용자 프로필에 저장된 커스텀 속성을 말합니다. 이를 통해 브랜드와 사용자의 상호작용에 대한 기록을 생성할 수 있습니다. 이를 통해 구매 내역 또는 총 생애주기 가치와 같이 계산된 필드인 커스텀 속성을 기반으로 세그먼트를 만들 수 있습니다.

사용자 업데이트 단계에서는 이 오브젝트 배열에 속성을 추가하거나 제거할 수 있습니다. 배열을 업데이트하려면 속성 목록에서 배열 속성 이름을 선택하고 키 값을 입력합니다.

#### 사용 사례: 사용자의 위시리스트 업데이트하기

배열에 항목을 추가하거나 제거하면 사용자의 위시리스트가 업데이트됩니다.

\![기여도 속성에 "선블록" 항목을 추가하는 사용자 업데이트 단계 "items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### 사용 사례: 장바구니 총액 계산

사용자가 장바구니에 품목이 있는 시기, 새 품목을 추가하거나 품목을 삭제하는 시기, 총 장바구니 금액을 추적합니다. 

1. `shopping_cart` 라는 커스텀 오브젝트 배열을 만듭니다. 다음 예시는 이 속성이 어떤 모습일 수 있는지 보여줍니다. 각 항목에는 고유한 `product_id` 이 있으며, `price` 을 포함하여 자체 중첩된 오브젝트 배열에 더 복잡한 데이터가 있습니다.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2\. 사용자가 장바구니에 상품을 추가할 때 기록되는 `add_item_to_cart` 이라는 이름의 [커스텀 이벤트를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 생성합니다.
3\. 이 커스텀 이벤트로 타겟 오디언스 사용자로 캔버스를 생성하세요. 이제 사용자가 장바구니에 아이템을 추가하면 이 캔버스가 트리거됩니다. 그런 다음 해당 사용자에게 직접 메시징을 타겟팅하여 특정 지출에 도달했거나 특정 시간 동안 장바구니를 유기한 경우 또는 사용 사례에 맞는 다른 모든 경우에 쿠폰 코드를 제공할 수 있습니다. 

`shopping_cart` 속성은 모든 품목의 총 비용, 장바구니의 총 품목 수, 장바구니에 선물이 포함된 경우 등 다양한 커스텀 이벤트의 총합을 전달합니다. 다음과 같이 보일 수 있습니다:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"]
         "gift": yes,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## 캔버스 항목 속성을 기여도 속성으로 설정하기

사용자 업데이트 단계를 사용하여 `canvas_entry_property`. 카트에 품목이 추가될 때 트리거되는 이벤트가 있다고 가정해 보겠습니다. 가장 최근에 장바구니에 추가한 품목의 ID를 저장하여 리마케팅 캠페인에 사용할 수 있습니다. 개인화 기능을 사용하여 캔버스 항목 속성을 검색하고 속성에 저장할 수 있습니다.

!!! 속성을 업데이트하는 사용자 업데이트 단계 "most_recent_cart_item" 아이템 ID를 업데이트합니다.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### 개인화

캔버스에 대한 트리거 이벤트 속성을 속성으로 저장하려면 개인화 모달을 사용하여 캔버스 항목 속성을 추출하여 저장합니다. 사용자 업데이트는 다음과 같은 개인화 기능도 지원합니다: 
* [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [항목 속성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Liquid 로직( [메시지 중단]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) 포함)
* 개체당 여러 속성 또는 이벤트 업데이트

{% alert warning %}
이 단계 유형에는 분당 200,000건의 요청 속도 제한이 있으므로 사용자 업데이트 단계에서 연결된 콘텐츠 Liquid 개인화를 신중하게 사용하는 것이 좋습니다. 이 요금 제한은 캔버스 요금 제한보다 우선합니다.
{% endalert %}

## 진행 중인 JSON 컴포저

JSON 작성기에 속성, 이벤트 또는 구매 JSON 객체를 최대 65,536자까지 추가할 수 있습니다. 사용자의 [글로벌 구독]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) 및 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) 상태도 설정할 수 있습니다.

\![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

고급 작성기를 사용하면 **미리보기 및 테스트** 탭을 사용하여 고객 프로필이 변경 사항으로 업데이트되는지 미리 보고 테스트할 수도 있습니다. 무작위 사용자를 선택하거나 특정 사용자를 검색할 수 있습니다. 그런 다음 사용자에게 테스트를 보낸 후 생성된 링크를 사용하여 고객 프로필을 확인합니다.

\![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### 고려 사항

플랫폼에서 자동으로 제공되므로 JSON 컴포저를 사용하는 동안 API 키와 같은 민감한 데이터를 포함할 필요가 없습니다. 따라서 다음 필드는 필요하지 않으므로 JSON 컴포저에서 사용해서는 안 됩니다:
* 외부 사용자 ID
* API 키
* Braze 클러스터 URL
* 푸시 토큰 가져오기 관련 필드

{% raw %}
### 커스텀 이벤트 기록하기

JSON 컴포저를 사용하여 커스텀 이벤트를 기록할 수도 있습니다. 이를 위해서는 ISO 형식의 타임스탬프가 필요하므로 처음에 Liquid로 시간과 날짜를 지정해야 합니다. 시간이 있는 이벤트를 기록하는 이 예시를 살펴보세요.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

다음 예제는 선택적 속성이 있는 커스텀 이벤트와 `app_id` 을 사용하여 이벤트를 특정 앱에 연결합니다.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### 구독 상태 편집

JSON 작성기 내에서 사용자의 구독 상태를 편집할 수도 있습니다. 예를 들어 다음은 `opted_in` 로 업데이트된 사용자의 구독 상태를 보여줍니다. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### 구독 그룹 업데이트하기 

이 캔버스 단계를 사용하여 구독 그룹을 업데이트할 수도 있습니다. 다음 예는 구독 그룹에 대한 업데이트를 보여줍니다. 하나 또는 여러 개의 구독 그룹 업데이트를 수행할 수 있습니다.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

