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

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

> 사용자 업데이트 구성요소를 사용하면 JSON 작성기에서 사용자의 속성, 이벤트 및 구매를 업데이트할 수 있으므로 API 키와 같은 민감한 정보를 포함할 필요가 없습니다.

사용자 업데이트를 사용하면 업데이트는 분당 `/users/track` 요청 사용량 제한에 포함되지 않습니다. 대신, 이러한 업데이트는 일괄 처리되므로 Braze가 Braze-to-Braze 웹훅보다 더 효율적으로 처리할 수 있습니다. 이 구성요소는 청구할 수 없는 데이터 포인트(예: 구독 그룹)를 업데이트하는 데 사용할 때는 [데이터 포인트]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)를 소비하지 않습니다.

사용자는 관련 사용자 업데이트가 완료된 후에만 다음 캔버스 단계로 진행할 수 있습니다. 후속 메시징이 사용자 업데이트에 의존하는 경우 메시지를 보내기 전에 이러한 업데이트가 완료되었는지 확인할 수 있습니다.

## 사용자 업데이트 만들기

사이드바에서 구성요소를 끌어서 놓거나 배리언트 또는 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **사용자 업데이트**를 선택합니다. 

기존 사용자 프로필 정보를 업데이트하거나, 새로 추가하거나, 삭제할 수 있는 세 가지 옵션이 있습니다. 워크스페이스의 사용자 업데이트 단계를 모두 합치면 분당 최대 200,000개의 고객 프로필을 업데이트할 수 있습니다.

{% alert tip %}
사용자를 검색하고 변경 사항을 적용하여 이 구성 요소로 변경한 내용을 테스트할 수도 있습니다. 그러면 사용자가 업데이트됩니다.
{% endalert %}

### 사용자 지정 속성 업데이트

사용자 지정 속성을 추가하거나 업데이트하려면 속성 목록에서 속성 이름을 선택하고 키 값을 입력합니다.

![][4]{: style="max-width:90%;"}

### 사용자 지정 속성 제거하기

사용자 지정 속성을 제거하려면 드롭다운을 사용하여 속성 이름을 선택합니다. [고급 JSON 작성기로](#advanced-json-composer) 전환하여 추가로 편집할 수 있습니다. 

![][5]{: style="max-width:90%;"}

### 값 증가 및 감소

사용자 업데이트 단계에서는 속성 값을 늘리거나 줄일 수 있습니다. 속성을 선택하고 **증분 기준** 또는 **감산 기준**을 선택한 다음 숫자를 입력합니다. 

#### 주간 진행 상황 추적

이벤트를 추적하는 사용자 지정 속성을 증분하여 사용자가 일주일 동안 수강한 수업 수를 추적할 수 있습니다. 이 구성 요소를 사용하면 한 주가 시작될 때 수업 수를 재설정하고 추적을 다시 시작할 수 있습니다. 

![][7]{: style="max-width:90%;"}

### 개체 배열 업데이트하기

[개체 배열]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)은 데이터가 풍부한 고객 프로필에 저장된 커스텀 속성입니다. 이를 통해 브랜드와 사용자의 상호작용에 대한 기록을 생성할 수 있습니다. 이를 통해 구매 내역 또는 총 생애주기 가치와 같이 계산된 필드인 커스텀 속성을 기반으로 세그먼트를 만들 수 있습니다.

사용자 업데이트 단계에서는 이 개체 배열에 속성을 추가하거나 제거할 수 있습니다. 배열을 업데이트하려면 속성 목록에서 배열 속성 이름을 선택하고 키 값을 입력합니다.

#### 사용 사례: 사용자의 위시리스트 업데이트하기

배열에 항목을 추가하거나 제거하면 사용자의 위시리스트가 업데이트됩니다.

![][9]{: style="max-width:90%;"}

#### 사용 사례: 장바구니 총액 계산

사용자가 장바구니에 품목이 있는 시기, 새 품목을 추가하거나 품목을 삭제하는 시기, 총 장바구니 금액을 추적합니다. 

1. `shopping_cart` 라는 사용자 지정 개체 배열을 만듭니다. 다음 예는 이 속성이 어떻게 표시되는지 보여줍니다. 각 항목에는 고유한 `product_id`가 있으며, `price`를 포함하여 더 복잡한 데이터가 중첩된 자체 개체 배열에 포함되어 있습니다.

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
2\. 사용자가 장바구니에 품목을 추가할 때 기록되는 `add_item_to_cart`라는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)를 만듭니다.
3\. 이 커스텀 이벤트를 사용하여 타겟 오디언스가 있는 캔버스를 만듭니다. 이제 사용자가 장바구니에 아이템을 추가하면 이 캔버스가 트리거됩니다. 그런 다음 해당 사용자에게 직접 메시지를 타겟팅하여 특정 지출에 도달하거나 특정 시간 동안 장바구니를 이탈한 경우 또는 기타 사용 사례에 부합하는 모든 경우에 쿠폰 코드를 제공할 수 있습니다. 

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

## 캔버스 항목 속성을 속성으로 설정하기

사용자 업데이트 단계를 사용하여 `canvas_entry_property`를 지속할 수 있습니다. 카트에 품목이 추가될 때 트리거되는 이벤트가 있다고 가정해 보겠습니다. 가장 최근에 장바구니에 추가한 품목의 ID를 저장하여 리마케팅 캠페인에 사용할 수 있습니다. 개인화 기능을 사용하여 캔버스 항목 속성정보를 검색하고 속성정보에 저장합니다.

![][8]{: style="max-width:90%;"}

### 개인화

캔버스에 대한 트리거 이벤트의 속성을 속성으로 저장하려면 개인화 모달을 사용하여 캔버스 항목 속성을 추출하여 저장합니다. 사용자 업데이트는 다음과 같은 개인화 기능도 지원합니다: 
* [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [항목 속성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
* 리퀴드 로직( [메시지 중단]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) 포함)
* 개체당 여러 속성 또는 이벤트 업데이트

{% alert warning %}
이 단계 유형에는 분당 200,000건의 요청 사용량 제한이 있으므로 사용자 업데이트 단계에서 연결된 콘텐츠 Liquid 개인화를 신중하게 사용하는 것이 좋습니다. 이 사용량 제한은 캔버스 사용량 제한보다 우선합니다.
{% endalert %}

## 고급 JSON 작성기

JSON 작성기에 속성, 이벤트 또는 구매 JSON 개체를 최대 65,536자까지 추가할 수 있습니다. 사용자의 [글로벌 구독]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) 및 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) 상태도 설정할 수 있습니다.

![][2]{: style="max-width:90%;"}

고급 작성기를 사용하면 **미리보기 및 테스트** 탭을 사용하여 사용자 프로필이 변경 사항으로 업데이트되었는지 미리 보고 테스트할 수도 있습니다. 무작위 사용자를 선택하거나 특정 사용자를 검색할 수 있습니다. 그런 다음 사용자에게 테스트를 보낸 후 생성된 링크를 사용하여 사용자 프로필을 확인합니다.

![][6]{: style="max-width:90%;"}

### 고려 사항

JSON 컴포저를 사용할 때 API 키와 같은 민감한 데이터는 플랫폼에서 자동으로 제공되므로 포함할 필요가 없습니다. 따라서 다음 필드는 필요하지 않으므로 JSON 컴포저에서 사용해서는 안 됩니다.
* 외부 사용자 ID
* API 키
* 브레이즈 클러스터 URL
* 푸시 토큰 가져오기와 관련된 필드

{% raw %}
### 사용자 지정 이벤트 로그

JSON 작성기를 사용하여 사용자 지정 이벤트를 기록할 수도 있습니다. 여기에는 ISO 형식의 타임스탬프가 필요하므로 처음에 Liquid로 시간과 날짜를 지정해야 합니다. 시간이 있는 이벤트를 기록하는 이 예시를 살펴보세요.

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

다음 예제는 선택적 속성이 있는 커스텀 이벤트와 `app_id`를 사용하여 이벤트를 특정 앱에 연결하는 예제입니다.

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

### 구독 상태 수정

JSON 작성기 내에서 사용자의 구독 상태를 편집할 수도 있습니다. 예를 들어 다음은 `opted_in`으로 업데이트된 사용자의 구독 상태를 보여줍니다. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### 구독 그룹 업데이트 

이 캔버스 단계를 사용하여 구독 그룹을 업데이트할 수도 있습니다. 다음 예는 구독 그룹에 대한 업데이트를 보여줍니다. 하나 또는 여러 개의 정기구독 그룹 업데이트를 수행할 수 있습니다.

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

[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %}
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %}
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %}
[4]: {% image_buster /assets/img_archive/canvas_user_update_update.png %}
[5]: {% image_buster /assets/img_archive/canvas_user_update_remove.png %}
[6]: {% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}
[7]: {% image_buster /assets/img_archive/canvas_user_update_increment.png %}
[8]: {% image_buster /assets/img_archive/canvas_user_update_cep.png %}
[9]: {% image_buster /assets/img_archive/canvas_user_update_wishlist.png %} 
