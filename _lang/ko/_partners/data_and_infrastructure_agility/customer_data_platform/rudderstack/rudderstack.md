---
nav_title: RudderStack
article_title: RudderStack
description: "이 문서에서는 Android, iOS 및 웹 애플리케이션에서 원활한 Braze 통합을 제공하는 오픈 소스 고객 데이터 인프라인 Rudderstack 및 Braze 간의 파트너십을 간략히 설명합니다. RudderStack을 사용하면 상황별 분석을 위해 인앱 고객 이벤트 데이터를 Braze로 직접 전송할 수 있습니다."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack][1]은 오픈 소스 고객 데이터 인프라로, 고객 이벤트 데이터를 수집하고 선호하는 데이터 웨어하우스 및 Braze와 같은 수십 개의 다른 분석 제공업체로 라우팅합니다. 엔터프라이즈 준비가 되어 있으며, 이벤트 데이터를 실시간으로 처리할 수 있는 강력한 변환 프레임워크를 제공합니다.

Braze와 RudderStack 통합은 Android, iOS 및 웹 애플리케이션에서 기본 SDK 통합과 백엔드 서비스에서 서버 간 통합을 제공합니다.

## 전제 조건

| 요구 사항 | 설명 |
| --- | --- |
| RudderStack 계정 | 이 파트너십을 이용하려면 [RudderStack 계정이](https://app.rudderstack.com/) 필요합니다. |
| 구성된 소스 | [소스][3]는 기본적으로 웹사이트, 모바일 앱 또는 백엔드 서버와 같이 RudderStack으로 전송되는 모든 데이터의 출처입니다. RudderStack에서 Braze를 대상으로 설정하기 전에 소스를 구성해야 합니다. |
| Braze REST API 키 | `users.track`, `users.identify`, `users.delete`, `users.alias.new` 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 앱 키 | Braze 대시보드에서 앱 키를 받으려면 **설정** > **앱 설정** > **신원 확인으로** 이동하여 앱 이름을 찾습니다. 연결된 식별자 문자열을 저장합니다.
| 데이터 센터 | 데이터 센터는 Braze 대시보드 [인스턴스][15]에 맞춰 조정됩니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

### 1단계: 소스 추가

Braze로 데이터 전송을 시작하려면 먼저 RudderStack 앱에 소스가 설정되어 있는지 확인해야 합니다. 데이터 소스를 설정하는 방법을 알아보려면 [RudderStack][22] ]을 방문하세요.

### 2단계: 대상 구성

데이터 소스가 설정되었으므로 RudderStack 대시보드의 **대상** 아래에서 **대상 추가**를 선택합니다. 사용 가능한 대상 목록에서 **Braze**를 선택하고 **다음**을 클릭합니다.

Braze 대상에서 앱 키, Braze REST API 키, 데이터 클러스터, 기본 SDK 옵션(기기 모드만 해당)을 제공합니다. 기본 SDK 옵션이 켜져 있으면 Braze 기본 SDK를 사용하여 이벤트를 전송합니다. 

![][0]{: style="max-width:70%;margin-bottom:15px;border:none;"}

### 3단계: 통합 유형 선택

다음 접근 방식 중 하나를 사용하여 RudderStack의 웹 및 네이티브 클라이언트 측 라이브러리를 Braze와 통합하도록 선택할 수 있습니다:

- [병렬/기기 모드](#device-mode)**:** RudderStack은 클라이언트(브라우저 또는 모바일 애플리케이션)에서 직접 이벤트 데이터를 Braze로 전송합니다.
- [서버 간/클라우드 모드](#cloud-mode)**:** Braze SDK는 이벤트 데이터를 RudderStack으로 직접 전송하고, RudderStack은 이를 변환하여 Braze로 라우팅합니다.
- [하이브리드 모드](#hybrid-mode)**:** 하이브리드 모드를 사용하면 단일 연결을 통해 iOS 및 Android 자동 생성 이벤트와 사용자 생성 이벤트를 Braze에 전송할 수 있습니다.

{% alert note %}
RudderStack의 [연결 모드](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)와 각 모드의 장점을 자세히 알아보세요.
{% endalert %}

#### 병렬 통합(기기 모드) {#device-mode}

이 모드를 사용하면 웹사이트나 모바일 앱에 설정된 Braze SDK를 사용하여 이벤트를 Braze로 전송할 수 있습니다.

[지원되는 방법에](#supported-methods) 설명된 대로 Braze GitHub 리포지토리에서 플랫폼용 RudderStack SDK에 대한 매핑을 설정하세요:

- [Android][android]
- [iOS][ios]
- [Swift][swift]
- [웹][web]
- [React Native][react]
- [Flutter][flutter]

기기 모드 통합을 완료하려면 [프로젝트에 Braze를 추가](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)하기 위한 자세한 RudderStack 지침을 참조하세요.

#### 서버 간 통합(클라우드 모드) {#cloud-mode}

이 모드에서는 SDK가 이벤트 데이터를 RudderStack 서버로 직접 전송합니다. 그런 다음, Rudderstack은 이 데이터를 변환하여 원하는 대상으로 라우팅합니다. 이 변환은 RudderStack의 변환기 모듈을 사용하여 RudderStack 백엔드에서 수행됩니다.

통합을 활성화하려면 [지원되는 메소드](#supported-methods)에 설명된 대로 RudderStack 메소드를 Braze에 매핑해야 합니다.

{% alert note %}
RudderStack의 서버 측 SDK(Java, Python, Node.js, Go, Ruby)는 클라우드 모드만 지원합니다. 서버 측 SDK가 RudderStack 백엔드에서 작동하며 Braze 특정 SDK를 로드할 수 없기 때문입니다.
{% endalert %}

{% alert important %}
서버 간 통합은 푸시 알림 또는 인앱 메시징과 같은 Braze UI 기능을 지원하지 않습니다. 그러나 이러한 기능은 디바이스 모드 통합을 통해 지원됩니다.
{% endalert %}

#### 하이브리드 모드 {#hybrid-mode}

하이브리드 모드를 사용하면 iOS 및 Android 소스에서 모든 이벤트를 Braze로 전송할 수 있습니다. 

하이브리드 모드를 선택하여 이벤트를 Braze, RudderStack으로 전송하는 경우:
1. Braze SDK를 초기화합니다.
2. 사용자가 생성한 모든 이벤트(식별, 추적, 페이지, 화면, 그룹)를 클라우드 모드를 통해서만 Braze로 전송하고, 기기 모드에서는 전송을 차단합니다.
3. 기기 모드를 통해 자동 생성된 이벤트(인앱 메시지, Braze SDK가 필요한 푸시 알림)를 전송합니다.

[하이브리드 모드를 통해 이벤트를 전송](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)하려면 소스를 Braze 대상에 연결한 상태에서 하이브리드 모드 옵션을 사용합니다. 그런 다음 프로젝트에 Braze 통합 기능을 추가합니다.

## 4단계: 추가 설정 구성

초기 설정을 완료한 후, Braze에서 데이터를 올바르게 수신하려면 다음 설정을 구성합니다.

- **그룹 통화에서 구독 그룹 활성화**: 그룹 이벤트에서 구독 그룹 상태를 보내려면 이 설정을 활성화합니다. 자세한 내용은 [그룹](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group)을 참조하세요.
- **커스텀 속성 작업 사용**: Braze에서 [중첩된 사용자 지정 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) 기능을 사용하여 세그먼트를 만들고 사용자 지정 속성 개체를 사용하여 메시지를 개인화하려면 이 설정을 사용 설정합니다. 자세한 내용은 [사용자 특성을 중첩된 사용자 지정 속성으로 보내기를](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes) 참조하세요.
- **익명 사용자의 이벤트 추적**: 이 설정을 활성화하면 익명의 사용자 활동을 추적하고 이 정보를 Braze로 전송할 수 있습니다.

### 기기 모드 설정

다음 설정은 [디바이스 모드를](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode) 통해 이벤트를 Braze로 보내는 경우에만 적용됩니다:

- **클라이언트 측 이벤트 필터링**: 이 설정을 사용하면 어떤 이벤트를 차단하거나 Braze로 유입되도록 허용할지 지정할 수 있습니다. 이 설정에 대한 자세한 내용은 [클라이언트 측 이벤트 필터링](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)을 참조하세요.
- **중복 특성**: 이 설정을 활성화하여 [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) 호출에서 사용자 특성을 중복 제거합니다.
- **Braze 로그 표시**: 이 설정은 [JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)를 소스로 사용하는 경우에만 적용할 수 있습니다. 사용자에게 Braze 로그를 표시하도록 활성화합니다.
- **OneTrust 쿠키 카테고리**: 이 설정을 통해 [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) 쿠키 동의 그룹을 Braze에 연결할 수 있습니다.

## 지원되는 방법

Braze는 식별, 추적, 화면, 페이지, 그룹 및 별칭을 식별하는 RudderStack 메서드를 지원합니다.

{% tabs %}
{% tab 식별 %}

RudderStack [`identify` 메서드는](https://rudderstack.com/docs/destinations/marketing/braze/#identify) 사용자를 작업과 연결합니다. RudderStack은 고유한 사용자 ID와 이름, 이메일, IP 주소 등 해당 사용자와 관련된 선택적 특성을 캡처합니다.

**통화 식별을 위한 델타 관리**<br>
기기 모드를 통해 이벤트를 Braze로 전송하는 경우 `identify` 호출을 중복 제거하여 비용을 절감할 수 있습니다. 이렇게 하려면 특성 중복 제거 대시보드 설정을 활성화합니다. 그러면 RudderStack은 변경되거나 수정된 속성(특성)만 Braze로 전송합니다.

**사용자 삭제하기**<br>
RudderStack [데이터 규제 API](https://www.rudderstack.com/docs/api/data-regulation-api/)의 [삭제로 억제 규정](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation)을 사용하여 Braze에서 사용자를 삭제할 수 있습니다.

{% endtab %}
{% tab 추적 %}

RudderStack의 [`track` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#track)는 모든 사용자 활동 및 해당 활동과 관련된 속성정보를 캡처합니다.

**주문 완료**<br>
러더스택 이커머스 API][20] 를 사용하여 `Order Completed` 라는 이름의 이벤트에 대한 트랙 메서드를 호출하면, 러더스택은 해당 이벤트에 나열된 제품을 [`purchases`][21] 으로 Braze에 전송합니다.

{% endtab %}
{% tab 화면 %}

RudderStack의 [`screen` 메서드](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)를 사용하면 사용자가 조회한 화면에 대한 추가 정보와 함께 모바일 화면 조회 수를 기록할 수 있습니다.

{% endtab %}
{% tab 페이지 %}

RudderStack의 [`page` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#page)를 사용하면 웹사이트의 페이지 조회 수를 기록할 수 있습니다. 또한 해당 페이지에 대한 기타 관련 정보도 캡처합니다.

{% endtab %}
{% tab 그룹 %}

RudderStack의 [`group` 메서드](https://rudderstack.com/docs/destinations/marketing/braze/#group)를 사용하면 사용자를 그룹에 연결할 수 있습니다.

**구독 그룹 상태**<br>
구독 그룹 상태를 업데이트하려면 RudderStack 대시보드에서 '그룹 통화에서 구독 그룹 활성화' 설정을 활성화하고 그룹 통화에서 구독 그룹 상태를 전송합니다.

{% endtab %}
{% tab Alias %}

RudderStack의 [`alias` 메서드](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias)를 사용하면 알려진 사용자의 여러 ID를 병합할 수 있습니다. RudderStack은 클라우드 모드에서만 Braze에 대한 별칭 호출을 지원합니다.

{% endtab %}
{% endtabs %}

## 사용자 특성을 중첩된 사용자 지정 속성으로 보내기

사용자 특성을 중첩된 사용자 지정 속성으로 Braze에 전송하고 추가, 업데이트, 제거 작업을 수행할 수 있습니다. 이렇게 하려면 Braze 대상을 구성하는 동안 RudderStack에서 '커스텀 속성 작업 대시보드 사용' 설정을 활성화합니다. 이 기능은 클라우드 모드에서만 사용할 수 있습니다.

사용자 특성을 다음 형식의 `identify` 이벤트에서 중첩된 사용자 지정 속성으로 보낼 수 있습니다:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

`track`, `page` 또는 `screen` 호출을 통해 사용자 특성을 커스텀 사용자 속성으로 전송하려면 이벤트의 상황별 필드로 `traits`를 전달합니다.
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
업데이트 및 제거 작업의 경우 `identifier`는 필수 키입니다. 중첩 배열에 추가, 업데이트 또는 제거 작업이 없는 경우 RudderStack은 기본적으로 생성 작업을 사용하여 프로퍼티를 생성합니다. 중첩된 커스텀 속성 전송에 대한 자세한 내용은 [오브젝트 배열]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)을 참조하세요.
{% endalert %}

[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}
[1]:https://rudderstack.com/
[3]:https://www.rudderstack.com/docs/dashboard-guides/sources/
[15]: {{site.baseurl}}/api/basics/#endpoints
[20]:https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]:https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started
[android]: https://github.com/rudderlabs/rudder-integration-braze-android
[ios]: https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master
[swift]: https://github.com/rudderlabs/rudder-integration-braze-swift
[web]: https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze
[react]: https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native
[flutter]: https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter