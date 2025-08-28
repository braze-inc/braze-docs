---
nav_title: 키-값 쌍
article_title: 키-값 쌍
page_order: 4
description: "이 참조 문서에서는 키-값 페어와 이를 사용하여 사용자 기기에 추가 데이터 페이로드를 보내는 방법을 다룹니다."
channel:
  - push
  - in-app messages
  - content cards

---

# 키-값 쌍

> This page covers how to use key-value pairs to send extra data payloads to user devices. 이 기능은 푸시, 인앱, 이메일 및 콘텐츠 카드 메시징 채널에서 사용할 수 있습니다.

키-값 쌍을 사용하여 메시지에 구조화된 메타데이터를 추가할 수 있습니다. 이러한 추가 데이터 페이로드는 메시지가 렌더링되거나 처리되는 방식에 영향을 줄 수 있는 추가 컨텍스트 정보로 메시지를 강화할 수 있습니다.

키-값 쌍은 메타데이터이므로 이 데이터는 수신자에게 반드시 표시되지는 않지만 연결된 시스템이나 프로세스에서 메시지 처리를 사용자 지정하는 데 사용할 수 있습니다. 

각 쌍은 다음으로 구성됩니다:

- **키:** 식별자(예: `utm_source`)
- **값:** 관련 데이터(예: `newsletter`)

## 사용 사례

다음은 키-값 쌍으로 메타데이터를 추가하는 사용 사례의 몇 가지 예입니다:

1. **추적 매개변수:** 분석 목적으로 UTM 매개변수 첨부하기
   - Key: `utm_campaign`
   - 가치: `spring_sale`
2. **사용자 지정 태그:** 내부 라우팅 또는 분류를 위한 태그 추가하기
   - Key: `priority`
   - 가치: `high`
3. **행동 유발기:** 인앱 동작을 트리거하거나 사용자 지정하는 데 사용되는 메타데이터
   - Key: `deep_link`
   - 가치: `app://promo-page`

## 푸시 알림

키-값 쌍을 Android, iOS 및 웹 푸시 알림에 추가할 수 있습니다. 키-값 쌍을 사용하여 내부 메트릭 및 앱 콘텐츠를 업데이트하거나 알림 우선순위 지정, 현지화 및 소리와 같은 푸시 알림 속성을 사용자 지정할 수 있습니다.

In the message composer, select the **Settings** tab, select **Add New Pair**, and specify your key-value pairs.

### iOS

Apple 푸시 알림 서비스(APNs)는 알림 환경 설정을 설정하고 키-값 페어를 사용하여 커스텀 데이터를 보내는 것을 지원합니다. APNs는 알림 속성을 제어하는 미리 결정된 키와 값을 포함하는 Apple 예약 ```aps``` 라이브러리를 사용합니다.

##### APS 라이브러리

| 키  | 값 유형  | 값 설명 |
|-------------------|-----------------------------|----------------------------------|
| 경고             | 문자열 또는 사전 객체 | 문자열 입력의 경우, 문자열을 메시지로 하여 닫기 및 보기 버튼이 있는 경고를 표시합니다. 비문자열 입력의 경우, 입력의 자식 속성에 따라 경고 또는 배너를 표시합니다. |
| 배지             | 숫자                      | 앱 아이콘에 배지로 표시되는 숫자를 관리합니다                                                                                                                              |
| 소리             | 문자열                      | 경고로 재생할 사운드 파일의 이름; 앱의 번들이나 ```Library/Sounds``` 폴더에 있어야 합니다                                                                                    |
| 콘텐츠 사용 가능 | 숫자                      | 1의 입력 값은 앱에 시작 또는 세션 재개 시 새로운 정보의 가용성을 신호합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### 알림 속성 라이브러리

| 키            | 값 유형               | 값 설명                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 제목         | 문자열                   | 알림의 일부로 Apple Watch에 잠시 표시되는 짧은 문자열                                                                    |
| 본문         | 문자열                   | 푸시 알림의 내용                                                                                                                  |
| title-loc-key  | 문자열 또는 null           | 현재 현지화의 제목 문자열을 ```Localizable.strings``` 파일에서 설정하는 키                                          |
| title-loc-args | 문자열 배열 또는 null | title-loc-key에서 제목 현지화 형식 지정자 대신 나타날 수 있는 문자열 값                                           |
| action-loc-key | 문자열 배열 또는 null  | 지정된 문자열이 있으면 닫기 및 보기 버튼에 대한 현지화를 설정합니다                                                         |
| loc-key        | 문자열 또는 null           | 현재 현지화에서 ```Localizable.strings``` 파일의 알림 메시지를 설정하는 키                                  |
| loc-args       | 문자열 배열         | loc-key에 현지화 형식 지정자 대신 나타날 수 있는 문자열 값                                                       |
| launch-image   | 문자열                  | 사용자가 실행 버튼을 누르거나 실행 슬라이드를 이동할 때 시작 이미지로 사용하려는 앱 번들에 있는 이미지 파일의 이름 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze 메시지 작성기는 **alert** 및 **its properties**, **content-available**, **sound**, **category** 키의 생성을 자동으로 처리합니다. 

이 값들은 푸시 메시지를 만들 때 **설정** 탭에 입력할 수 있습니다. **알림 옵션**을 선택하고 새 키-값 항목에 자동으로 채워질 키에 대한 알림 사전 키를 선택합니다.

![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Braze가 APNs에 푸시 알림을 보낼 때, 페이로드는 JSON 형식으로 작성됩니다.

**간단한 페이로드**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**복잡한 페이로드**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### 커스텀 키-값 쌍

```aps``` 라이브러리 페이로드 값 외에도 사용자 기기에 커스텀 키-값 페어를 보낼 수 있습니다. The values in these pairs are restricted to primitive types: dictionary (object), array, string, number, and boolean.

![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Use cases for custom key-value pairs include but are not limited to internal metrics keeping and setting the context for the user interface. Braze allows you to send additional key-value pairs along with a push notification to be used through your application within the [extras key]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). If you prefer to use another key, confirm that your app can handle this custom key.

{% alert warning %}
응용 프로그램에서 ab라는 최상위 키 또는 사전을 다루는 것을 피해야 합니다.
{% endalert %}

Apple은 클라이언트에게 고객 정보나 민감한 데이터를 커스텀 페이로드 데이터로 포함하지 않도록 권장합니다. 게다가 Apple은 경고 메시지와 관련된 모든 작업이 기기의 데이터를 삭제하지 않도록 권장합니다.

{% alert warning %}
If you're using the HTTP/2 provider API, any individual payload you send to APNs cannot exceed a size of 4096 bytes. 레거시 이진 인터페이스는 곧 사용 중단될 예정이며, 2048바이트의 페이로드 크기만 지원합니다.
{% endalert %}

###### API로 트리거된 캠페인

Braze를 사용하면 `extras`로 알려진 커스텀 정의 문자열 키-값 페어를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 추가 기능에 액세스하려면 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정하세요. 이로 인해 `"extras": { "test": { "foo": 1, "bar": 1 }`의 개발자 콘솔 출력이 발생합니다

### Android

Braze를 사용하면 키-값 페어를 사용하여 푸시 알림에 추가 데이터 페이로드를 보낼 수 있습니다.

##### 데이터 페이로드

iOS 푸시와 유사하게, 사용자 기기에 커스텀 키-값 페어를 보낼 수 있습니다.

커스텀 키-값 페어의 몇 가지 사용 사례로는 내부 측정기준 유지 및 사용자 인터페이스에 대한 컨텍스트 설정이 포함되지만, 원하는 목적에 따라 사용할 수 있습니다.

{% alert important %}
앱 백엔드는 데이터 페이로드가 제대로 작동하도록 커스텀 키-값 페어를 처리할 수 있어야 합니다.
{% endalert %}

###### API로 트리거된 캠페인

Braze를 사용하면 `extras`로 알려진 커스텀 정의 문자열 키-값 페어를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 추가 기능에 액세스하려면 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정하세요. 이로 인해 `"extras": { "test": { "foo": 1, "bar": 1 }`의 개발자 콘솔 출력이 발생합니다.

##### FCM 메시징 옵션

Android 푸시 알림은 FCM 메시지 옵션으로 더욱 맞춤 설정할 수 있습니다. These include [notification priority]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), [sound]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), delay, lifespan, and collapsibility. 이 값들은 푸시 메시지를 만들 때 **설정** 탭에서 지정할 수 있습니다. Refer to [Advanced push notification settings]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) for further instructions on how to set these options in the Braze message composer.

![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### 조용한 푸시 알림

무음 푸시 알림은 경고 메시지나 소리 없이 푸시 알림으로, 백그라운드에서 앱의 인터페이스나 콘텐츠를 업데이트하는 데 사용됩니다. 이 알림은 키-값 쌍을 사용하여 이러한 백그라운드 앱 동작을 트리거합니다. Silent push notifications also power our [uninstall tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

마케터는 푸시 알림이 앱 사용자에게 전송되기 전에 예상되는 동작을 트리거하는지 테스트해야 합니다. After you compose your [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) or [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) silent push notification, ensure that you only target a test user by filtering on [external user ID]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) or [email address]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

캠페인 시작 시, 테스트 기기에서 푸시 알림을 받지 않았는지 확인해야 합니다.

{% alert note %}
iOS 운영 체제는 일부 기능(제거 추적, 지오펜스 및 푸시 스토리)에 대해 [알림을 차단]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations)할 수 있습니다. 이 기능들에 어려움을 겪고 있다면, iOS의 무음 알림 게이트가 원인일 수 있습니다.
{% endalert %}

## 인앱 메시지

To add a key-value pair to an in-app message, select the **Settings** tab in the message composer, select **Add New Pair**, and specify your key-value pairs.

![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### API로 트리거된 캠페인

Braze를 사용하면 `extras`로 알려진 커스텀 정의 문자열 키-값 페어를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 추가 기능에 액세스하려면 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정하세요. 이로 인해 `"extras": { "test": { "foo": 1, "bar": 1 }`의 개발자 콘솔 출력이 발생합니다.

## 이메일

SparkPost와 SendGrid는 이메일에서 키-값 페어를 지원합니다. If you use SendGrid, key-value pairs will be sent as [unique arguments](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid는 최대 10,000바이트의 데이터에 대해 무제한의 키-값 페어를 첨부할 수 있습니다. These key-value pairs can be seen in posts from the SendGrid [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/).

{% alert note %}
반송된 이메일은 SparkPost 또는 SendGrid에 키-값 페어를 전달하지 않습니다.
{% endalert %}

![Sending Info tab of the email message composer in Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## 콘텐츠 카드

To add a key-value pair to a Content Card, go to the **Settings** tab in the Braze message composer and select **Add New Pair**.

![Add key-value pair to Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}


