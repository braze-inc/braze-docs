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

> Braze는 키-값 페어를 통해 사용자 기기에 추가 데이터 페이로드를 보낼 수 있게 합니다. 이 기능은 푸시, 인앱, 이메일 및 콘텐츠 카드 메시징 채널에서 사용할 수 있습니다. 

메시지에 구조화된 메타데이터를 추가하려면 키-값 쌍을 사용하세요. 이러한 추가 데이터 페이로드는 메시지를 추가적인 상황별 정보로 풍부하게 하여 메시지가 렌더링되거나 처리되는 방식에 영향을 줄 수 있습니다.

키-값 쌍은 메타데이터이기 때문에 이 데이터는 반드시 수신자에게 보이지 않지만, 연결된 시스템이나 프로세스에서 메시지 처리를 사용자 정의하는 데 사용할 수 있습니다. 

각 쌍은 다음으로 구성됩니다:

- 키 식별자 (예: `utm_source`)
- 값 연관된 데이터 (예: `newsletter`)

## 사용 사례

메타데이터를 키-값 쌍으로 추가하는 몇 가지 예제 사용 사례는 다음과 같습니다:

1. **추적 매개변수:** 분석 목적으로 UTM 매개변수 첨부
   - 키: `utm_campaign`
   - 값: `spring_sale`
2. **커스텀 태그:** 내부 라우팅 또는 분류를 위한 태그 추가
   - 키: `priority`
   - 값: `high`
3. 행동 유발기:** 앱 내 동작을 트리거하거나 사용자 정의하는 데 사용되는 메타데이터
   - 키: `deep_link`
   - 값: `app://promo-page`

## 푸시 알림

키-값 쌍은 Android, iOS 및 웹 푸시 알림에 추가할 수 있습니다. 내부 측정기준 및 앱 콘텐츠를 업데이트하거나 푸시 알림 속성(예: 알림 우선 순위, 현지화 및 소리)을 사용자 지정하기 위해 키-값 쌍을 사용할 수 있습니다.

메시지 작성기에서 **설정** 탭을 선택하고, **새 쌍 추가**를 클릭한 다음, 키-값 쌍을 지정합니다.

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

![][16]
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

```aps``` 라이브러리 페이로드 값 외에도 사용자 기기에 커스텀 키-값 페어를 보낼 수 있습니다. 이 쌍의 값은 원시 타입으로 제한됩니다: 사전 (객체), 배열, 문자열, 숫자 및 불리언.

![][17]

커스텀 키-값 페어의 사용 사례에는 내부 측정기준 유지 및 사용자 인터페이스의 컨텍스트 설정 등이 포함되지만 이에 국한되지는 않습니다. Braze는 [extras key][1] 내에서 애플리케이션을 통해 원하는 방식으로 사용할 수 있도록 푸시 알림과 함께 추가 키-값 페어를 보낼 수 있게 해줍니다. 다른 키를 사용하려면 앱이 이 커스텀 키를 처리할 수 있는지 확인하세요.

{% alert warning %}
응용 프로그램에서 ab라는 최상위 키 또는 사전을 다루는 것을 피해야 합니다.
{% endalert %}

Apple은 클라이언트에게 고객 정보나 민감한 데이터를 커스텀 페이로드 데이터로 포함하지 않도록 권장합니다. 게다가 Apple은 경고 메시지와 관련된 모든 작업이 기기의 데이터를 삭제하지 않도록 권장합니다.

{% alert warning %}
HTTP/2 제공자 API를 사용하는 경우 APNs에 보내는 개별 페이로드는 4096바이트를 초과할 수 없습니다. 레거시 이진 인터페이스는 곧 사용 중단될 예정이며, 2048바이트의 페이로드 크기만 지원합니다.
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

Android 푸시 알림은 FCM 메시지 옵션으로 더욱 맞춤 설정할 수 있습니다. 여기에는 [알림 우선순위][8], [소리][10], 지연, 수명 및 접을 수 있는 기능이 포함됩니다. 이 값들은 푸시 메시지를 만들 때 **설정** 탭에서 지정할 수 있습니다. Braze 메시지 작성기에서 이러한 옵션을 설정하는 방법에 대한 자세한 지침은 [고급 푸시 알림 설정][7]을 참조하세요.

![][18]

### 조용한 푸시 알림

무음 푸시 알림은 경고 메시지나 소리 없이 푸시 알림으로, 백그라운드에서 앱의 인터페이스나 콘텐츠를 업데이트하는 데 사용됩니다. 이 알림은 키-값 쌍을 사용하여 이러한 백그라운드 앱 동작을 트리거합니다. 푸시 알림은 또한 우리의 [제거 추적][4]을 지원합니다.

마케터는 푸시 알림이 앱 사용자에게 전송되기 전에 예상되는 동작을 트리거하는지 테스트해야 합니다. [iOS][2] 또는 [Android][13] 무음 푸시 알림을 작성한 후 [외부 사용자 ID][14] 또는 [이메일 주소][15]로 필터링하여 테스트 사용자만 타겟팅하도록 하십시오.

캠페인 시작 시, 테스트 기기에서 푸시 알림을 받지 않았는지 확인해야 합니다.

{% alert note %}
iOS 운영 체제는 일부 기능(제거 추적, 지오펜스 및 푸시 스토리)에 대해 [알림을 차단]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations)할 수 있습니다. 이 기능들에 어려움을 겪고 있다면, iOS의 무음 알림 게이트가 원인일 수 있습니다.
{% endalert %}

## 인앱 메시지

인앱 메시지에 키-값 페어를 추가하려면 메시지 작성기의 **설정** 탭을 선택하고, **새 페어 추가**를 클릭한 다음 키-값 페어를 지정합니다.

![][21]

#### API로 트리거된 캠페인

Braze를 사용하면 `extras`로 알려진 커스텀 정의 문자열 키-값 페어를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 추가 기능에 액세스하려면 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정하세요. 이로 인해 `"extras": { "test": { "foo": 1, "bar": 1 }`의 개발자 콘솔 출력이 발생합니다.

## 이메일

SparkPost와 SendGrid는 이메일에서 키-값 페어를 지원합니다. SendGrid를 사용하면 키-값 쌍이 [고유 인수][11]로 전송됩니다. SendGrid는 최대 10,000바이트의 데이터에 대해 무제한의 키-값 페어를 첨부할 수 있습니다. 이러한 키-값 쌍은 SendGrid [이벤트 웹훅][12]의 게시물에서 볼 수 있습니다.

{% alert note %}
반송된 이메일은 SparkPost 또는 SendGrid에 키-값 페어를 전달하지 않습니다.
{% endalert %}

![Braze의 이메일 메시지 작성기의 보내기 정보 탭.][22]

## 콘텐츠 카드

콘텐츠 카드에 키-값 페어를 추가하려면 Braze 메시지 작성기의 **설정** 탭으로 이동하여 **새 페어 추가**를 클릭하세요.

![콘텐츠 카드에 키-값 페어 추가][24]{: style="max-width:70%;"}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#delivery-options
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds
[11]: https://docs.sendgrid.com/for-developers/sending-email/unique-arguments
[12]: https://sendgrid.com/docs/for-developers/tracking-events/event/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[14]: {{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id
[15]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %}
[17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %}
[18]: {% image_buster /assets/img_archive/keyvalue_androidkeys.png %}
[19]: {% image_buster /assets/img_archive/keyvalue_android.png %}
[20]: {% image_buster /assets/img_archive/keyvalue_web.png %}
[21]: {% image_buster /assets/img_archive/keyvalue_iam.png %}
[22]: {% image_buster /assets/img_archive/keyvalue_email.png %}
[23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %}
[24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}
