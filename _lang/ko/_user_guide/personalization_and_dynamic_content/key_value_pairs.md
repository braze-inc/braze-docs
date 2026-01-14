---
nav_title: 키-값 페어
article_title: 키-값 페어
page_order: 4
description: "이 참조 문서에서는 키-값 페어와 이를 사용하여 사용자 기기에 추가 데이터 페이로드를 전송하는 방법을 다룹니다."
channel:
  - push
  - in-app messages
  - content cards

---

# 키-값 페어

> 이 페이지에서는 키-값 페어를 사용하여 사용자 기기에 추가 데이터 페이로드를 전송하는 방법을 설명합니다. 이 기능은 푸시, 인앱, 이메일, 콘텐츠 카드 메시징 채널에서 사용할 수 있습니다.

키-값 페어를 사용하여 메시징에 구조화된 메타데이터를 추가하세요. 이러한 추가 데이터 페이로드는 메시징이 렌더링되거나 처리되는 방식에 영향을 줄 수 있는 추가적인 상황별 정보로 메시지를 강화할 수 있습니다.

키-값 페어는 메타데이터이므로 이 데이터는 수신자에게 반드시 표시되지는 않지만 연결된 시스템이나 프로세스에서 메시지 처리를 커스텀하는 데 사용할 수 있습니다. 

각 쌍은 다음으로 구성됩니다:

- **Key:** 식별자(예: `utm_source`)
- **가치:** 관련 데이터(예: `newsletter`)

## 사용 사례

다음은 키-값 페어로 메타데이터를 추가하는 몇 가지 사용 사례입니다:

1. **추적 매개변수:** 분석 목적으로 UTM 매개변수 첨부하기
   - Key: `utm_campaign`
   - 가치: `spring_sale`
2. **커스텀 태그:** 내부 라우팅 또는 분류를 위한 태그 추가하기
   - Key: `priority`
   - 가치: `high`
3. **행동 트리거:** 인앱 행동을 트리거하거나 커스텀하는 데 사용되는 메타데이터
   - Key: `deep_link`
   - 가치: `app://promo-page`

## 푸시 알림

키-값 페어를 Android, iOS 및 웹 푸시 알림에 추가할 수 있습니다. 키-값 페어를 사용하여 내부 측정기준 및 앱 콘텐츠를 업데이트하거나 알림 우선순위 지정, 현지화 및 소리와 같은 푸시 알림 속성을 커스텀할 수 있습니다.

메시지 작성기에서 **설정** 탭을 선택하고 **새 페어 추가를** 선택한 다음 키-값 페어를 지정합니다.

### iOS

Apple 푸시 알림 서비스(APN)는 알림 환경설정을 설정하고 키-값 페어를 사용하여 커스텀 데이터를 전송할 수 있도록 지원합니다. APN은 경고 속성을 관리하는 미리 정해진 키와 값이 포함된 Apple 예약 라이브러리( ```aps``` )를 사용합니다.

##### APS 라이브러리

| 키  | 값 유형  | 값 설명 |
|-------------------|-----------------------------|----------------------------------|
| 알림             | 문자열 또는 사전 객체 | 문자열 입력의 경우 닫기 및 보기 버튼과 함께 문자열을 메시지로 하는 경고를 표시하고, 문자열이 아닌 입력의 경우 입력의 하위 속성에 따라 경고 또는 배너를 표시합니다. |
| 배지             | 숫자                      | 앱 아이콘에 배지로 표시되는 번호를 관리합니다.                                                                                                                              |
| 소리             | 문자열                      | 알림으로 재생할 사운드 파일의 이름; 앱의 번들 또는 ```Library/Sounds``` 폴더에 있어야 합니다.                                                                                    |
| 콘텐츠 사용 가능 | 숫자                      | 입력값이 1이면 앱 실행 또는 세션 재개 시 새로운 정보를 사용할 수 있음을 앱에 알립니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### 경고 속성 라이브러리

| 키            | 값 유형               | 값 설명                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | 문자열                   | Apple Watch에서 알림의 일부로 짧게 표시하는 문자열입니다.                                                                    |
| body         | 문자열                   | 푸시 알림의 내용                                                                                                                  |
| title-loc-key  | 문자열 또는 널           | ```Localizable.strings``` 파일에서 현재 현지화의 제목 문자열을 설정하는 키입니다.                                          |
| title-loc-args | 문자열 배열 또는 null | title-loc-key에서 제목 현지화 형식 지정자 대신 표시할 수 있는 문자열 값입니다.                                           |
| action-loc-key | 문자열 배열 또는 null  | 있는 경우 지정된 문자열은 닫기 및 보기 버튼의 현지화를 설정합니다.                                                         |
| loc-key        | 문자열 또는 널           | ```Localizable.strings``` 파일에서 현재 현지화에 대한 알림 메시지를 설정하는 키입니다.                                  |
| loc-args       | 문자열 배열         | loc-key에서 현지화 형식 지정자 대신 표시할 수 있는 문자열 값입니다.                                                       |
| launch-image   | 문자열                  | 사용자가 실행 버튼을 탭하거나 액션 슬라이드를 이동할 때 실행 이미지로 사용할 앱 번들 내 이미지 파일의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze 메시지 작성기는 **알림** 및 **해당 속성**, **콘텐츠 사용 가능 여부**, **사운드**, **카테고리** 등의 키 생성을 자동으로 처리합니다. 

이 값은 푸시 메시지를 구축할 때 **설정** 탭에서 입력할 수 있습니다. **경고 옵션을** 선택하고 새 키-값 항목에 자동으로 입력할 경고 사전 키를 선택합니다.

\![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Braze가 APN에 푸시 알림을 보내면 페이로드는 JSON으로 형식이 지정됩니다.

**간편 페이로드**

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

##### 커스텀 키-값 페어

```aps``` 라이브러리 페이로드 값 외에도 커스텀 키-값 페어를 사용자의 기기에 전송할 수 있습니다. 이 쌍의 값은 사전(객체), 배열, 문자열, 숫자 및 부울과 같은 기본 유형으로 제한됩니다.

\![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

커스텀 키-값 페어 사용 사례에는 내부 측정기준 유지 및 사용자 인터페이스의 컨텍스트 설정이 포함되지만 이에 국한되지는 않습니다. Braze를 사용하면 추가 키-값 페어와 함께 푸시 알림을 전송하여 추가 [키]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs) 내에서 애플리케이션을 통해 사용할 수 있습니다. 다른 키를 사용하려면 앱에서 이 커스텀 키를 처리할 수 있는지 확인하세요.

{% alert warning %}
애플리케이션에서 ab라는 최상위 키 또는 사전을 처리하지 않아야 합니다.
{% endalert %}

Apple은 클라이언트에게 고객 정보나 민감한 데이터를 커스텀 페이로드 데이터로 포함하지 말 것을 권장합니다. 또한 Apple은 경고 메시지와 관련된 어떤 작업도 기기의 데이터를 삭제해서는 안 된다고 권장합니다.

{% alert warning %}
HTTP/2 공급자 API를 사용하는 경우, APN에 보내는 개별 페이로드는 4096바이트 크기를 초과할 수 없습니다. 곧 지원 중단될 레거시 바이너리 인터페이스는 2048바이트의 페이로드 크기만 지원합니다.
{% endalert %}

###### API 트리거 캠페인

Braze를 사용하면 커스텀 정의된 문자열 키-값 페어( `extras`)를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 엑스트라에 액세스하려면 대시보드에서 키를 "example_key", 로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} 로 설정하세요. 그러면 개발자 콘솔 출력은 다음과 같습니다. `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze를 사용하면 키-값 페어를 사용하여 푸시 알림에 추가 데이터 페이로드를 전송할 수 있습니다.

##### 데이터 페이로드

iOS 푸시와 마찬가지로 커스텀 키-값 페어를 사용자의 기기에 보낼 수 있습니다.

커스텀 키-값 페어의 일부 사용 사례에는 내부 측정기준 유지 및 사용자 인터페이스의 컨텍스트 설정이 포함되지만, 어떤 용도로든 사용할 수 있습니다.

{% alert important %}
앱의 백엔드는 데이터 페이로드가 제대로 작동하려면 커스텀 키-값 페어를 처리할 수 있어야 합니다.
{% endalert %}

###### API 트리거 캠페인

Braze를 사용하면 커스텀 정의된 문자열 키-값 페어( `extras`)를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 엑스트라에 액세스하려면 대시보드에서 키를 "example_key", 로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} 로 설정하세요. 그러면 개발자 콘솔 출력은 `"extras": { "test": { "foo": 1, "bar": 1 }` 입니다.

##### FCM 메시징 옵션

Android 푸시 알림은 FCM 메시지 옵션으로 더욱 커스텀할 수 있습니다. 여기에는 [알림 우선순위]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), [소리]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), 지연, 수명 및 접을 수 있는 기능이 포함됩니다. 이 값은 푸시 메시지를 만들 때 **설정** 탭에서 지정할 수 있습니다. Braze 메시지 작성기에서 이러한 옵션을 설정하는 방법에 대한 자세한 안내는 [고급 푸시 알림 설정을]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) 참조하세요.

\![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### 무음 푸시 알림

무음 푸시 알림은 경고 메시지나 소리가 없는 푸시 알림으로, 백그라운드에서 앱의 인터페이스나 콘텐츠를 업데이트하는 데 사용됩니다. 이러한 알림은 키-값 페어를 사용하여 이러한 백그라운드 앱 동작을 트리거합니다. 무음 푸시 알림은 [제거 추적]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/) 기능도 지원합니다.

마케터는 앱 사용자에게 푸시 알림을 보내기 전에 무음 푸시 알림이 예상되는 행동을 트리거하는지 테스트해야 합니다. [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) 또는 [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) 무음 푸시 알림을 작성한 후에는 [외부 사용자 ID]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) 또는 [이메일 주소를]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 필터링하여 테스트 사용자만 타겟팅해야 합니다.

캠페인이 시작되면 테스트 기기에 푸시 알림이 표시되지 않는지 확인해야 합니다.

{% alert note %}
iOS 운영 체제는 일부 기능(제거 추적, 지오펜스, 푸시 스토리)에 대한 [알림을 게이트 알림으로]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) 처리할 수 있습니다. 이러한 기능에 문제가 있는 경우 iOS의 무음 알림 게이트가 원인일 수 있습니다.
{% endalert %}

## 인앱 메시지

인앱 메시지에 키-값 쌍을 추가하려면 메시지 작성기에서 **설정** 탭을 선택하고 **새 쌍 추가를** 선택한 다음 키-값 쌍을 지정합니다.

\![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### API 트리거 캠페인

Braze를 사용하면 커스텀 정의된 문자열 키-값 페어( `extras`)를 보낼 수 있습니다. API 트리거 및 예약된 API 트리거 캠페인에서 엑스트라에 액세스하려면 대시보드에서 키를 "example_key", 로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} 로 설정하세요. 그러면 개발자 콘솔 출력은 `"extras": { "test": { "foo": 1, "bar": 1 }` 입니다.

## 이메일

SparkPost와 SendGrid는 모두 이메일에서 키-값 페어를 지원합니다. SendGrid를 사용하는 경우 키-값 페어는 [고유한 인수로](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments) 전송됩니다. SendGrid를 사용하면 최대 10,000바이트의 데이터까지 키-값 페어를 무제한으로 첨부할 수 있습니다. 이러한 키-값 페어는 SendGrid [이벤트 웹훅의](https://sendgrid.com/docs/for-developers/tracking-events/event/) 게시물에서 확인할 수 있습니다.

{% alert note %}
반송된 이메일은 스팍포스트 또는 SendGrid에 키-값 페어를 전달하지 않습니다.
{% endalert %}

Braze의 이메일 메시지 작성기의 정보 보내기 탭입니다.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## 콘텐츠 카드

콘텐츠 카드에 키-값 쌍을 추가하려면 Braze 메시지 작성기의 **설정** 탭으로 이동하여 **새 쌍 추가를** 선택합니다.

\![콘텐츠 카드에 키-값 페어 추가하기]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}


