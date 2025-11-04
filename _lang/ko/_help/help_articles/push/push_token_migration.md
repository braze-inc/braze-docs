---
nav_title: 푸시 토큰 마이그레이션
article_title: 푸시 토큰 마이그레이션
page_order: 0

page_type: solution
description: "이 도움말 문서에서는 Braze로 전환한 후에도 사용자에게 푸시 메시지를 계속 보낼 수 있도록 푸시 토큰을 마이그레이션하는 방법을 설명합니다."
channel: push
---

# 푸시 토큰 마이그레이션

> [푸시 토큰]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/)은 앱의 알림을 전송할 위치를 지정하는 고유한 익명 식별자입니다. Braze는 Android용 Firebase 클라우드 메시징 서비스(FCM) 및 iOS용 Apple 푸시 알림 서비스(APN)와 같은 푸시 서비스 제공업체와 연결되며, 이러한 제공업체는 앱을 식별하는 고유 기기 토큰을 전송합니다. Braze를 통합하기 전에 자체적으로 또는 다른 제공업체를 통해 푸시 알림을 보내고 있었다면, 푸시 토큰 마이그레이션을 통해 등록된 푸시 토큰으로 사용자에게 푸시 알림을 계속 보낼 수 있습니다.

## SDK를 통한 자동 마이그레이션

[Braze SDK를 통합한]({{site.baseurl}}/developer_guide/sdk_integration/) 후에는 옵트인한 사용자의 푸시 토큰이 다음에 앱을 열 때 자동으로 마이그레이션됩니다. 그때까지는 해당 사용자에게 Braze를 통해 푸시 알림을 보낼 수 없습니다.

또는 [푸시 토큰을 수동으로 마이그레이션하여](#manual-migration-via-api) 사용자의 재참여를 더욱 신속하게 유도할 수 있습니다.

### 웹 토큰 고려 사항

웹 푸시 토큰의 특성상 웹용 푸시를 구현할 때 다음 사항을 고려해야 합니다:

|Consideration|세부 정보|
|----------------------|------------|
| **서비스 작업자**  | `manageServiceWorkerExternally` 또는 `serviceWorkerLocation` 와 같은 다른 옵션을 지정하지 않는 한 기본적으로 웹 SDK는 `./service-worker` 에서 서비스 워커를 찾습니다 . 서비스 워커가 제대로 설정되어 있지 않으면 사용자의 푸시 토큰이 만료될 수 있습니다. |
| **만료된 토큰**   | 사용자가 60일 이내에 웹 세션을 시작하지 않으면 푸시 토큰이 만료됩니다. Braze는 만료된 푸시 토큰을 마이그레이션할 수 없으므로, 다시 참여하려면 [푸시 프라이머를]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) 보내야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## API를 통한 수동 마이그레이션

수동 푸시 토큰 마이그레이션은 API를 통해 이전에 생성한 키를 Braze 플랫폼으로 가져오는 프로세스입니다.

[`users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하여 프로그래밍 방식으로 iOS(APN) 및 Android(FCM) 토큰을 플랫폼으로 마이그레이션합니다. 식별된 사용자(연결된 외부 ID가 있는 사용자)와 익명 사용자(외부 ID가 없는 사용자)를 모두 마이그레이션할 수 있습니다.

푸시 토큰 마이그레이션 중에 앱의 `app_id`를 지정하여 적절한 푸시 토큰을 적절한 앱에 연결합니다. 각 앱(iOS, Android 등)에는 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지의 **식별** 섹션에서 찾을 수 있는 고유한 `app_id` 이 있습니다. 올바른 플랫폼의 `app_id` 을 사용해야 합니다.

{% alert important %}
API를 통해 웹 푸시 토큰을 마이그레이션하는 것은 불가능합니다. 이는 웹 푸시 토큰이 다른 플랫폼과 동일한 스키마를 따르지 않기 때문입니다. 

<br>프로그래밍 방식으로 웹 푸시 토큰을 마이그레이션하려는 경우 `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send` 오류가 표시될 수 있습니다.

<br>
API 마이그레이션의 대안으로 SDK를 통합하여 토큰 기반이 자연스럽게 다시 채워질 수 있도록 하는 것이 좋습니다.
{% endalert %}

{% tabs local %}
{% tab 외부 ID 존재 %}
식별된 사용자의 경우 `push_token_import` 플래그를 `false`로 설정(또는 매개변수 생략)하고 사용자 `attributes` 오브젝트에 `external_id`, `app_id`, `token` 값을 지정합니다. 

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab 외부 ID 누락 %}
다른 시스템에서 푸시 토큰을 가져올 때 `external_id`를 항상 사용할 수 있는 것은 아닙니다. 이 경우 `push_token_import` 플래그를 `true`로 설정하고 `app_id` 및 `token` 값을 지정합니다. Braze는 각 토큰에 대해 임시 익명 고객 프로필을 생성하여 이러한 개인에게 계속 메시지를 보낼 수 있도록 합니다. 토큰이 이미 Braze에 존재하는 경우 요청은 무시됩니다.

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

가져온 후 익명 사용자가 Braze 지원 버전의 앱을 실행하면, Braze는 가져온 푸시 토큰을 자동으로 Braze 고객 프로필로 이동하고 임시 프로필을 정리합니다.

Braze는 한 달에 한 번씩 푸시 토큰이 없으며 `push_token_import` 플래그가 있는 익명 프로필을 확인합니다. 익명 프로필에 더 이상 푸시 토큰이 없는 경우 해당 프로필을 삭제합니다. 그러나 익명 프로필에 푸시 토큰이 남아 있어 실제 사용자가 아직 해당 푸시 토큰으로 기기에 로그인하지 않았다는 것을 암시하는 경에는 아무 조치도 취하지 않습니다.
{% endtab %}
{% endtabs %}

## Android 푸시 토큰 가져오기

{% alert important %}
다음 고려 사항은 Android 앱에만 적용됩니다. iOS 앱에는 푸시 표시를 위한 프레임워크가 하나만 있으며, Braze에 필요한 푸시 토큰과 인증서가 있는 한 푸시 알림이 즉시 렌더링되므로 이러한 단계가 필요하지 않습니다.
{% endalert %}

Braze SDK 통합이 완료되기 전에 사용자에게 Android 푸시 알림을 보내야 하는 경우 키-값 페어를 사용하여 푸시 알림의 유효성을 검사하세요. 

푸시 페이로드를 처리하고 표시하려면 수신기가 있어야 합니다. 수신자에게 푸시 페이로드를 알리려면 푸시 캠페인에 필요한 키-값 쌍을 추가합니다. 이 쌍의 값은 Braze 이전에 사용한 특정 푸시 파트너에 따라 달라집니다.

{% alert note %}
일부 푸시 알림 제공업체의 경우, Braze가 키-값 페어를 올바르게 해석할 수 있도록 평평하게 만들어야 합니다. 특정 Android 앱의 키-값 페어를 평평하게 하려면 고객 온보딩 또는 성공 매니저에게 문의하세요.
{% endalert %}

_마지막 업데이트: 2022년 12월 5일_
