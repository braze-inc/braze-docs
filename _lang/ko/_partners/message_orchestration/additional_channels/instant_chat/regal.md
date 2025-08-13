---
nav_title: Regal
article_title: Regal
description: "이 참조 문서에서는 두 소스의 데이터를 사용하여 고객에게 개인화된 경험을 제공할 수 있는 전화 및 SMS 판매 솔루션인 Regal과 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io][6]는 더 많은 대화를 유도하여 성장 목표를 더 빨리 달성할 수 있도록 구축된 전화 및 SMS 영업 솔루션입니다.

Regal과 Braze를 통합하면 모든 고객 터치포인트에서 보다 일관되고 개인화된 경험을 제공할 수 있습니다.
- Regal과의 전화 대화 내용을 바탕으로 적절한 차선책 이메일 또는 Braze의 푸시 알림을 보내세요.
- 높은 가치의 고객이 Braze에서 보낸 마케팅 이메일을 클릭했지만 전환하지 않으면 Regal에서 통화를 트리거하세요.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Regal 계정 | 이 파트너십을 활용하려면 Regal 계정이 필요합니다. |
| Regal API 키 | Regal API 키를 사용하면 Braze에서 Regal로 이벤트를 보낼 수 있습니다.<br><br>이 키를 받으려면 [support@regal.io](mailto:support@regal.io)에 문의하세요. |
| Braze 데이터 변환 | 데이터 변환은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 고객 성공 매니저에게 문의하세요. 이는 Regal에서 데이터를 수신하는 데 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합: Braze에서 Regal로 데이터 전송

다음 섹션에서는 Braze 캔버스 또는 캠페인 웹훅을 사용하여 고객 프로필 및 이벤트 데이터를 Regal로 전송하는 소스로 Braze를 사용하는 방법을 설명합니다.

### 1단계: Regal에서 새 연락처 생성

Regal에서 전화와 문자를 받을 수 있는 새 연락처가 Braze에서 생성될 때마다 Regal에 웹훅으로 연결되는 캔버스 또는 캠페인을 구축합니다. 

1. 'Regal의 새 연락처 생성'이라는 제목의 캔버스 또는 캠페인을 생성하고 진입 유형으로 **실행 기반**을 선택합니다.

2. 트리거 로직을 **사용자 지정** 이벤트로 설정하고 전화번호가 있는 연락처가 생성될 때 실행되는 이벤트를 선택합니다. 또한 Regal은 전화 필드에 추가 필터를 추가하여 설정할 것을 권장합니다.

3. 새 웹훅 템플릿에서 다음 필드를 입력합니다:
   - **웹훅 URL**: <https://events.regalvoice.com/events>
   - **요청 본문**: 원시 텍스트

#### 요청 헤더 및 메서드

Regal.io에는 권한 부여용 HTTP 헤더와 HTTP 메서드도 필요합니다. 다음은 **설정** 탭에서 키-값 쌍으로 템플릿에 이미 포함되어 있습니다:
{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
    - **권한 부여**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

아래 필수 입력란은 `traits.phone` 속성뿐입니다. 나머지는 선택 사항입니다. 그러나 `optIn`을 포함할 경우 `optIn.channel` 및 `optIn.subscribed`를 포함해야 합니다.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

위의 페이로드 예제에서는 모든 연락처가 음성 및 SMS 옵트인을 수락했다고 가정합니다. 그렇지 않은 경우 위의 `optIn` 속성정보를 제거하고 `optIn` 수집 시 Regal에서 연락처를 업데이트하도록 별도의 캔버스 또는 캠페인을 설정할 수 있습니다.

### 2단계: 옵트인 정보 업데이트 

앱 사용자 경험의 여러 부분에서 옵트인 및 옵트아웃이 발생할 수 있는 경우, 사용자가 옵트인 또는 옵트아웃할 때 Regal을 업데이트하는 것이 중요합니다. 다음은 Regal에 최신 옵트인 정보를 전송하는 방법에 대한 권장 캔버스입니다. 이를 Braze 프로필 필드로 저장한다고 가정하지만, 그렇지 않은 경우 트리거는 사용자의 옵트인 또는 탈퇴를 나타내는 Braze 계정의 이벤트가 될 수도 있습니다. (아래 예제는 전화 옵트인용 예제이지만, 별도로 수집하는 경우 유사한 캔버스 또는 캠페인을 설정하여 SMS 옵트인용으로 설정할 수 있습니다.)

1. "리갈에 옵트인 또는 옵트아웃 보내기"라는 제목의 새 캔버스 또는 캠페인을 만듭니다.

2. 다음 트리거 옵션 중 하나를 선택하고 사용자의 옵트인 상태를 나타내는 필드를 선택합니다. 옵트인 또는 옵트아웃을 나타내기 위해 Braze에 이벤트를 발생시키는 경우, 해당 이벤트를 트리거로 사용하세요.
    - 사용자 프로필 필드 업데이트
    - 구독 그룹 상태 업데이트
    - 구독 상태

3. 새 웹훅 템플릿에서 다음 필드를 입력합니다:
   - **웹훅 URL**: <https://events.regalvoice.com/events>
   - **요청 본문**: 원시 텍스트

#### 요청 헤더 및 메서드

Regal.io에는 권한 부여용 HTTP 헤더와 HTTP 메서드도 필요합니다. 다음은 템플릿 내에 키-값 쌍으로 이미 포함되어 있지만 **설정** 탭에 있습니다:
{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
    - **권한 부여**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

더 많은 속성을 동시에 최신 상태로 유지하려는 경우 이 페이로드에 고객 프로필 속성을 추가할 수도 있습니다.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### 3단계: 사용자 지정 이벤트 보내기

마지막으로, Regal을 보내려는 각 주요 이벤트에 대한 캔버스 또는 캠페인을 설정합니다. Regal에서는 가입 또는 구매 흐름의 각 단계에 존재하는 이벤트와 같이 Regal에서 SMS 및 통화를 트리거하는 데 중요하거나 연락처가 Regal 캠페인에서 제외되는 종료 기준으로 사용되는 모든 이벤트를 보낼 것을 권장합니다.

예를 들어, 다음은 사용자가 신청의 첫 번째 단계를 완료할 때 Regal에 이벤트를 전송하는 워크플로입니다.

1. 'Regal에 신청 1단계 완료 이벤트 전송'이라는 제목의 새 캔버스 또는 캠페인을 생성합니다.

2. 트리거 노드 로직을 **사용자 지정** 이벤트로 설정하고 "신청 1단계 완료"와 같이 Regal에 전송할 이벤트 이름을 선택합니다.

3. 새 웹훅 템플릿에서 다음 필드를 입력합니다:
   - **웹훅 URL**: <https://events.regalvoice.com/events>
   - **요청 본문**: 원시 텍스트

#### 요청 헤더 및 메서드

Regal.io에는 권한 부여용 HTTP 헤더와 HTTP 메서드도 필요합니다. 다음은 템플릿 내에 키-값 쌍으로 이미 포함되어 있지만 **설정** 탭에 있습니다:
{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
    - **권한 부여**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

더 많은 속성을 동시에 최신 상태로 유지하려는 경우 이 페이로드에 고객 프로필 속성을 추가할 수도 있습니다.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### 최신 연락처 속성

필수는 아니지만, 이벤트 워크플로의 이벤트 페이로드에 있는 주요 고객 프로필 데이터 필드도 전송하여 주요 이벤트를 사용할 수 있는 시점에 Regal이 최신 연락처 속성에 액세스할 수 있도록 하는 것이 좋습니다.

{% alert note %}
어떤 이벤트를 Regal에 전송해야 하는지 또는 이러한 캔버스 및 캠페인을 가장 잘 설정하는 방법에 대해 궁금한 점이 있으면 support@regal.io로 문의하세요.
{% endalert %}

## 통합: Regal에서 Braze로 데이터 전송

이 섹션에서는 `SMS.sent` 및 `call.completed`와 같은 Regal 보고 벤트를 Braze로 가져와서 Braze 프로필에 표시하고 Braze 세분화 툴, 캔버스 및 캠페인에서 사용할 수 있도록 하는 방법을 설명합니다. 이 통합은 Regal 보고 웹훅과 Braze 데이터 변환을 사용하여 데이터 흐름을 자동화합니다.

### 1단계: Braze에서 데이터 혁신 만들기

{% alert important %}
데이터 변환은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

Braze에 전송하려는 Regal 웹훅에 따라 변환을 생성하는 것이 좋습니다. 

데이터 변환을 생성하려면 다음을 수행합니다.
1. Braze 대시보드에서 **변환** 페이지로 이동합니다.
2. 변환에 이름을 지정하고 **변환 생성**을 클릭합니다.
3. 변환 목록에서 <i class="fa-solid fa-ellipsis-vertical" title="작업 보기"></i> 을 클릭하고 **웹훅 URL 복사를** 선택합니다.

![][4]

### 2단계: Regal에서 보고 웹훅 활성화하기

보고 웹훅을 설정하려면 다음과 같이 하세요:
1. 리갈 앱으로 이동하여 **설정** 페이지를 엽니다.

2. **리포팅 웹훅** 섹션에서 **웹훅 생성**을 클릭합니다.

3. 웹훅 엔드포인트 입력에 연결된 데이터 변환에 대한 Braze 데이터 변환 웹훅 URL을 추가합니다.

![][5]{: style="max-width:60%;"}

#### 엔드포인트 업데이트하기
엔드포인트를 편집하면 캐시를 새로 고치고 대신 새 엔드포인트로 이벤트를 전송하는 데 최대 5분이 걸릴 수 있습니다.
#### 재시도
현재 이러한 이벤트에 대한 재시도는 없습니다. 5초 이내에 응답이 수신되지 않으면 이벤트가 삭제되고 재시도되지 않습니다. Regal은 향후 릴리스에서 재시도를 추가할 예정입니다.
#### 이벤트
Regal의 [보고 웹훅 가이드][7]에는 게시하는 보고 이벤트의 전체 목록이 포함되어 있습니다. 속성정보 정의와 샘플 페이로드도 확인할 수 있습니다.

### 3단계: 리갈 이벤트를 브레이즈 이벤트로 전환

The Braze [Data Transformation]({{site.baseurl}}/data_transformation) feature allows you to map incoming Regal events into the format necessary to be added as attributes, events, or purchases in Braze.

1. 데이터 변환에 이름을 지정합니다. 이벤트 웹훅별 데이터 변환을 설정하는 것이 좋습니다.

2. 연결을 테스트하려면 Regal 에이전트 데스크톱에서 휴대폰에 대한 아웃바운드 통화를 생성하고 대화 요약 양식을 제출하여 call.completed 이벤트를 생성합니다.

3. Regal 연락처를 Braze 프로필에 매핑하는 데 사용할 식별자를 결정합니다. Regal 이벤트에서 사용할 수 있는 식별자는 다음과 같습니다.
   - `userId` - 이전에 연락처에 대해 이 식별자를 보낸 적이 있는 경우에만 이벤트에서 설정됨
   - `traits.phone`
   - `traits.email` - 이전에 연락처에 대해 이 식별자를 보낸 적이 있는 경우에만 이벤트에서 설정됨

#### Braze 지원 식별자
- Braze는 식별자로 전화번호를 지원하지 않습니다. 이 정보를 식별자로 사용하려면 Braze에서 [사용자 별칭][8]으로 설정할 수 있습니다.
- Braze 데이터 변환을 사용할 때 이메일 주소를 식별자로 사용할 수 있습니다. 이메일 주소가 Braze 내에 프로필로 존재하는 경우 기존 프로필이 업데이트됩니다. 이메일 주소가 아직 Braze 내에 존재하지 않는 경우 이메일 전용 프로필이 생성됩니다.

## 사용 사례

{% tabs %}
{% tab 이메일 트리거 %}

**Regal의 통화 처리에 따라 Braze에서 이메일 트리거**

아래는 Regal의 `call.completed` 이벤트에 대한 페이로드 샘플입니다. 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

아래는 이를 Braze의 사용자 지정 이벤트에 매핑하는 데이터 변환 샘플입니다.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 프로필 속성 업데이트 %}

**Regal에서 `contact.attribute.edited` 이벤트를 기반으로 Braze에서 프로필 속성 업데이트**

아래는 Regal의 `contact.attribute.edited` 이벤트에 대한 페이로드 샘플입니다. 이 이벤트는 에이전트 중 한 명이 대화에서 새로운 내용을 알게 되어 연락처 프로필의 속성을 업데이트할 때마다 실행됩니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

다음은 새 커스텀 속성정보 값을 Braze 프로필의 관련 속성에 매핑하는 데이터 변환 예제입니다.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 실험을 동기화 상태로 유지 %}

**`contact.experiment.assigned` 이벤트를 사용하여 Braze와 Regal의 실험 동기화**

아래는 Regal의 `contact.experiment.assigned` 이벤트에 대한 페이로드 샘플입니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

아래는 이를 Braze의 사용자 지정 이벤트에 매핑하는 데이터 변환 샘플입니다.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab 연락처 구독 취소 %}

**Regal의 `contact.unsubscribed`에 따라 Braze에서 연락처 탈퇴**

아래는 Regal의 `contact.unsubscribed` 이벤트에 대한 페이로드 샘플입니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

다음은 Braze에서 연락처를 탈퇴시키는 데이터 변환 예제입니다.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

[2]: {% image_buster /assets/img/regal/webhook_rawtext.png %}
[3]: {% image_buster /assets/img/regal/request_header.png %}
[4]: {% image_buster /assets/img/regal/copy_webhook_url.png %}
[5]: {% image_buster /assets/img/regal/edit_webhook.png %}
[6]:https://regal.io
[7]:https://developer.regal.io/docs/reporting-webhooks#events
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases