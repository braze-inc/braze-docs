# 사용 사례: 예약 알림 이메일 시스템

> Braze는 프로그래밍적으로 제어할 수 있도록 설계된 종합 고객 참여 플랫폼입니다. 이 사용 사례에서는 Braze가 제품과 마케팅의 교차점에 있는 사용 사례에 연결할 수 있는 기능을 제공하는 몇 가지 방법을 보여줍니다. 예를 들어 예약 시스템과 같은 경우입니다.

이 사용 사례는 Braze 기능을 사용하여 예약 알림 이메일 메시징 서비스를 구축하는 방법을 보여줍니다. 이 서비스는 사용자가 약속을 예약할 수 있도록 하며, 다가오는 약속에 대한 알림 메시지를 사용자에게 전송합니다. 이 사용 사례는 이메일 메시지를 사용하지만, 사용자 프로필에 대한 단일 업데이트를 기반으로 모든 채널 또는 여러 채널에서 메시지를 보낼 수 있습니다.

이 서비스를 생성하는 다른 이점은 다음과 같습니다:
- 전송된 메시지는 전체 추적 및 보고 기능을 갖습니다.
- 메시지 내용은 비기술적인 Braze 사용자에 의해 업데이트될 수 있습니다.
- 메시지는 캠페인 구성에 따라 사용자 프로필의 옵트인 및 옵트아웃 상태를 준수합니다.
- 예약 데이터와 메시지 상호작용 데이터 모두 추가 메시징을 위해 사용자를 세분화하고 타겟팅하는 데 사용할 수 있습니다. 예를 들어, 초기 알림 메시지를 열지 않은 사용자에게 약속 전에 추가 알림으로 리타겟팅할 수 있습니다.

이 사용 사례를 달성하기 위해 다음 단계를 따르세요:
1. [다가오는 예약 데이터를 Braze 사용자 프로필에 작성하기](#step-1)
2. [예약 알림 메시지를 설정하고 시작하기](#step-2)
3. [업데이트된 예약 및 취소 처리하기](#step-3)

## 1단계: 다가오는 예약 데이터를 Braze 사용자 프로필에 작성하기 {#step-1}

Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트를 사용하여 예약이 발생할 때마다 사용자 프로필에 [중첩 고객 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)을 작성하세요. 중첩 고객 속성에는 알림 메시지를 전송하고 개인화하는 데 필요한 모든 정보가 포함되어야 합니다. 이 사용 사례에서는 중첩 고객 속성을 "여행"이라고 명명합니다.

### 예약 추가

사용자가 예약을 생성할 때, Braze에 데이터를 전송하기 위해 `/users/track` 엔드포인트를 통해 객체 배열의 다음 구조를 사용하십시오.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

중첩 고객 속성 "여행"은 사용자 프로필에 다음과 같이 표시됩니다.

![런던 여행과 시드니 여행을 위한 두 개의 중첩 고객 속성입니다.][1]{: style="max-width:70%;"}

### 예약 업데이트
사용자가 예약을 업데이트할 때, Braze에 데이터를 전송하기 위해 `/users/track` 엔드포인트를 통해 객체 배열의 다음 구조를 사용하십시오.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### 예약 제거

{% tabs %}
{% tab /users/track 엔드포인트 %}
#### `/users/track` 엔드포인트를 통해 데이터 전송
사용자가 예약을 삭제할 때, Braze에 데이터를 전송하기 위해 `/users/track` 엔드포인트를 통해 객체 배열의 다음 구조를 사용하십시오.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### SDK를 통해 사용자 프로필에 중첩 속성을 작성하십시오.

앱, 웹사이트 또는 둘 다를 통해 예약을 수집하고 해당 데이터를 사용자 프로필에 직접 작성하려는 경우, Braze SDK를 사용하여 이 데이터를 전송할 수 있습니다. 다음은 웹 SDK를 활용한 예입니다:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

지정된 예약은 사용자 프로필의 중첩 고객 속성에서 제거되며 남아 있는 예약이 표시됩니다.

![런던 여행을 위한 중첩 고객 속성입니다.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## 2단계: 예약 알림 메시지 설정 및 시작 {#step-2}

### 2a 단계: 대상 오디언스 생성
다중 기준 세분화를 사용하여 알림을 받을 대상 오디언스를 생성하십시오. 예를 들어, 예약 날짜 이틀 전에 알림을 보내고 싶다면 다음을 선택하세요:

- 시작 날짜 **1일 이상** 및
- 시작 날짜 **2일 미만** 

![시작 날짜가 하루 이상이고 이틀 미만인 중첩 커스텀 속성 "trips"가 있는 경우.][3]

### 2b 단계: 메시지를 작성하세요

[커스텀 HTML로 이메일 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)의 단계를 따라 알림 이메일 메시지를 만드세요. Liquid를 사용하여 이 예제와 같이 생성한 커스텀 고객 속성(“trips”)의 데이터로 메시지를 개인화하세요.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}} 
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### 2c 단계: 캠페인을 시작하세요

알림 이메일 메시지 캠페인을 시작하세요. 이제 Braze가 “trips” 커스텀 속성을 받을 때마다, 각 예약 객체에 포함된 데이터에 따라 메시지가 예약됩니다.

## 3단계: 업데이트된 예약 업데이트 및 취소 처리 {#step-3}

이제 알림 메시지를 보내고 있으므로, 예약이 업데이트되거나 취소될 때 보낼 확인 메시지를 설정할 수 있습니다.

### 3a 단계: 업데이트된 데이터 전송

{% tabs %}
{% tab /users/track %}

#### `/users/track` 엔드포인트를 통해 데이터 전송
사용자가 예약을 업데이트하거나 취소할 때 커스텀 이벤트를 보내기 위해 Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트를 사용하세요. 그 이벤트에서 변경 사항을 확인할 수 있는 필요한 데이터를 이벤트 속성에 넣으세요. 

이 사용 사례에서 사용자가 시드니 여행 날짜를 업데이트했다고 가정해 보겠습니다. 이벤트는 다음과 같을 것입니다:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### SDK를 통해 사용자 프로필에 중첩 속성을 작성하십시오.

SDK를 통해 사용자 프로필에 커스텀 이벤트를 전송하세요. 예를 들어, 웹 SDK를 사용하고 있다면 다음과 같이 보낼 수 있습니다:

{% raw %}
```json
braze.logCustomEvent("trip_updated", { 
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 3b단계: 업데이트를 확인하는 메시지를 작성하세요

사용자에게 업데이트된 예약 확인을 보내기 위해 [행동 기반 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)을 생성하세요. 예약의 이름, 이전 시간 및 새로운 시간을 반영하는 이벤트 속성을 템플릿화하기 위해 [Liquid을 사용할 수 있습니다]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) (또는 취소인 경우 이름만 사용).

예를 들어, 다음과 같은 메시지를 작성할 수 있습니다:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### 3단계 c: 업데이트를 반영하도록 사용자 프로필을 수정하세요

마지막으로, 가장 최근 데이터에 따라 1단계 및 2단계에서 예약 알림을 보내기 위해 중첩된 커스텀 속성을 업데이트하여 예약의 변경 또는 취소를 반영하세요.

#### 업데이트된 예약

이 사용 사례에서 사용자가 시드니 여행을 업데이트한 경우, 다음과 같은 호출로 날짜를 변경하기 위해 `/users/track` 엔드포인트를 사용합니다:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### 취소된 예약

이 사용 사례에서 사용자가 시드니 여행을 취소한 경우, `/users/track` 엔드포인트에 다음 호출을 보냅니다:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

이 호출이 전송되고 사용자 프로필이 업데이트된 후, 예약 알림 메시지는 사용자의 예약 날짜에 대한 최신 데이터를 반영합니다.

[1]: {% image_buster /assets/img/use_cases/2_nested_attributes.png %}
[3]: {% image_buster /assets/img/use_cases/custom_nested_attribute.png %}