---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "이 참조 문서에서는 작업 결과를 Braze에 직접 작성할 수 있는 기업 고객 데이터 플랫폼인 Treasure Data와 Braze 커런츠 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner


---


# Treasure Data for Currents

> [Treasure Data][1]는 여러 소스로부터 정보를 수집하여 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼(CDP)입니다.

Braze와 Treasure Data의 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. 커런츠를 사용하면 데이터를 Treasure Data에 연결하여 전체 성장 스택에서 실행 가능한 데이터로 만들 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Treasure Data | 이 파트너십을 활용하려면 [Treasure Data 계정][0]이 필요합니다. |
| 커런츠 | 데이터를 Treasure Data로 다시 내보내려면 계정에 [Braze 커런츠][2]를 설정해야 합니다. |
| Treasure Data URL | 이 정보는 Treasure Data 대시보드로 이동하고 수집 URL을 복사하면 얻을 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
트레저데이터는 각 이벤트를 일괄적으로 기록합니다. 보물 데이터를 쿼리하여 이벤트 수를 가져오는 방법에 대한 자세한 내용은 [브레이즈 전류 가져오기 통합을](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration) 참조하세요.
{% endalert %}

## 통합

Treasure Data와 연결할 때 권장되는 방법은 포스트백 API를 사용하는 것입니다. 이 방법에는 기본 커넥터가 필요하지 않으며 푸시 접근 방식을 통해 데이터를 수신할 수 있습니다. 하나의 데이터 배치로 전송된 모든 이벤트는 JSON 배열에서 한 행의 한 필드 안에 있으며, 필요한 데이터를 얻기 위해 구문 분석이 필요합니다.

{% alert important %}
이벤트 수집기를 통한 Treasure Data 수집은 현재 실시간으로 수행되지 않으며 최대 5분이 소요될 수 있습니다.
{% endalert %}

### 1단계: Braze에서 Treasure Data 포스트백 API 설정

포스트백 API 생성에 대한 지침은 [트레저데이터 웹사이트에서][3] 확인할 수 있습니다. Braze는 이벤트 수집기를 통한 수집을 제외하고 업데이트된 이벤트를 실시간으로 보물 데이터로 직접 전송합니다. 완료되면 Treasure Data는 다음 단계에서 사용할 수 있도록 복사할 데이터 소스 URL을 제공합니다.

### 2단계: 현재 만들기

Braze에서 **커런츠** > **\+ 커런츠 생성** > **Treasure Data 내보내기**로 이동합니다. 통합 이름, 연락처 이메일, Treasure Data URL을 제공합니다. 그런 다음, 사용 가능한 이벤트 목록에서 추적할 이벤트를 선택하고 **커런츠 시작**을 클릭합니다.

Treasure Data로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 포함됩니다. 현재 Braze는 `external_user_id`를 설정하지 않은 사용자에 대해 이벤트 데이터를 Treasure Data로 전송하지 않습니다.

{% alert important %}
보물 데이터 URL을 최신 상태로 유지하세요. 커넥터의 URL이 올바르지 않으면 Braze에서 이벤트를 전송할 수 없습니다. 이 상태가 48시간 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

#### 이벤트 필드 값 예시
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### 수집된 뷰의 예

![4]{: style="max-width:70%;"}

## 통합 세부 정보

Braze는 [커런츠 이벤트 용어집에]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) 나열된 모든 데이터( [메시지 참여]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) 및 [고객 행동]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) 이벤트의 모든 속성 포함)를 트레저 데이터로 내보낼 수 있도록 지원합니다.

내보낸 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일하며, [커스텀 HTTP 커넥터의 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 확인할 수 있습니다.


[0]: https://console.treasuredata.com/users/sign_in
[1]: https://www.treasuredata.com/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents
[3]: https://docs.treasuredata.com/display/public/PD/Postback+API
[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
