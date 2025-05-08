---
nav_title: 고급 설정
article_title: FireOS의 고급 설정
platform: FireOS
page_order: 4
page_type: reference
description: "이 문서에서는 Braze 대시보드를 통해 전송되는 FireOS 푸시 알림에 사용할 수 있는 고급 설정을 다룹니다."
channel: push

---

# 고급 설정

> Braze 대시보드를 통해 발송되는 Android 및 FireOS 푸시 알림에 사용할 수 있는 많은 고급 설정이 있습니다. 이 문서에서는 이러한 기능과 이를 성공적으로 사용하는 방법에 대해 설명합니다.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

## TTL {#ttl}

TTL( **Time to Live** ) 필드에서는 푸시 메시징 서비스에 메시지를 저장할 사용자 지정 기간을 설정할 수 있습니다. TTL의 기본값은 FCM의 경우 4주, ADM의 경우 31일입니다.

## 요약 텍스트 {#summary-text}

요약 텍스트를 사용하면 확장된 알림 보기에서 추가 텍스트를 설정할 수 있습니다. 이미지가 포함된 알림의 캡션 역할도 합니다.

![제목이 'Greetings from Appboy!'이고 메시지가 'This is the message body! 이모티콘을 추가할 수도 있습니다." 및 요약 텍스트 "요약 텍스트입니다."]({% image_buster /assets/img_archive/summary_text.png %})

요약 텍스트는 확장 보기에서 메시지 본문 아래에 표시됩니다.

이미지가 포함된 푸시 알림의 경우 메시지 텍스트는 축소된 보기에 표시되며, 알림을 펼치면 요약 텍스트가 이미지 자막으로 표시됩니다. 

!["앱보이!" 제목, "메시지 본문은..." 메시지 및 "요약 텍스트는..."이라는 요약 텍스트가 포함된 Android 메시지]({% image_buster /assets/img_archive/messagesummary.gif %})

## 사용자 지정 URI {#custom-uri}

**사용자 지정 URI** 기능을 사용하면 알림을 클릭할 때 이동할 웹 URL 또는 Android 리소스를 지정할 수 있습니다. 사용자 지정 URI가 지정되지 않은 경우 알림을 클릭하면 사용자가 앱으로 이동합니다. 커스텀 URI를 사용하여 앱 내부에 딥링킹하고 사용자를 앱 외부에 존재하는 리소스로 연결할 수 있습니다. 이는 그림과 같이 [메시징 API]({{site.baseurl}}/api/endpoints/messaging) 또는 푸시 작성기의 **고급 설정** 아래의 대시보드를 통해 지정할 수 있습니다:

![브레이즈 푸시 작성기의 딥링킹 고급 설정]({% image_buster /assets/img_archive/deep_link.png %})

## 알림 표시 우선순위

{% alert important %}
알림 표시 우선순위 설정은 Android O 이상을 실행하는 기기에서는 더 이상 사용되지 않습니다. 최신 기기의 경우 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)을 통해 우선순위를 설정합니다.
{% endalert %}

푸시 알림의 우선순위 수준은 다른 알림과 비교하여 알림 트레이에 알림이 표시되는 방식에 영향을 줍니다. 또한 우선순위가 일반 이하인 메시지는 배터리 수명을 보존하기 위해 지연 시간이 약간 더 길어지거나 일괄 발송되는 반면, 우선순위가 높은 메시지는 항상 즉시 발송되므로 전송 속도와 방식에도 영향을 줄 수 있습니다.

Android O에서는 알림 우선 순위가 알림 채널의 속성이 되었습니다. 개발자와 협력하여 채널을 구성하는 동안 채널의 우선순위를 정의한 다음 대시보드를 사용하여 알림 소리를 보낼 때 적절한 채널을 선택해야 합니다. O 이전의 Android 버전을 실행하는 기기의 경우, Braze 대시보드 및 메시징 API를 통해 Android 및 FireOS 알림의 우선순위를 지정할 수 있습니다. 

전체 사용자에게 특정 우선순위로 메시지를 보내려면 [알림 채널 구성을](https://developer.android.com/training/notify-user/channels#importance) 통해 간접적으로 우선순위를 *지정하고* (O+ 디바이스 대상) 대시보드에서 개별 우선순위를 보내는 방법(<O 디바이스 대상)을 권장합니다.

Android 또는 Fire OS 푸시 알림에서 설정할 수 있는 우선 순위 수준은 다음과 같습니다:

| 우선순위 | 설명/용도 | `priority` 값(API 메시지의 경우) |
|----------|--------------------------|-------------------------------------|
| 최대      | 긴급하거나 시간이 촉박한 메시지 | `2` |
| 높음     | 친구의 새 메시지와 같은 중요한 커뮤니케이션 | `1` |
| 기본값  | 대부분의 알림 - 메시지가 다른 우선순위 유형에 명시적으로 속하지 않는 경우에 사용합니다. | `0` |
| 낮음      | 사용자가 알기를 원하지만 즉각적인 조치가 필요하지 않은 정보 | `-1` |
| 최소      | 컨텍스트 또는 배경 정보. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

자세한 내용은 Google의 [Android 알림](http://developer.android.com/design/patterns/notifications.html) 문서를 참조하세요.

## 소리 {#sounds}

Android O에서는 알림 소리가 알림 채널의 속성이 되었습니다. 개발자와 협력하여 채널을 구성하는 동안 채널의 사운드를 정의한 다음 대시보드를 사용하여 알림을 보낼 때 적절한 채널을 선택해야 합니다.

Android O 이전 버전을 실행하는 디바이스의 경우, Braze를 사용하면 대시보드 작성기를 통해 개별 푸시 메시지의 사운드를 설정할 수 있습니다. 기기에서 로컬 사운드 리소스를 지정하면 됩니다(예: `android.resource://com.mycompany.myapp/raw/mysound`). 이 필드에서 '기본값'을 지정하면 기기에서 기본 알림 사운드가 재생됩니다. 이는 [메시징 API]({{site.baseurl}}/api/endpoints/messaging) 또는 푸시 작성기의 **설정** 아래 대시보드를 통해 지정할 수 있습니다.

![Braze 푸시 작곡가의 사운드 고급 설정]({% image_buster /assets/img_archive/sound_android.png %})

대시보드 프롬프트에 전체 사운드 리소스 URI(예: `android.resource://com.mycompany.myapp/raw/mysound`)를 입력합니다.

전체 사용자에게 특정 사운드로 메시지를 보내려면 [알림 채널 구성을](https://developer.android.com/training/notify-user/channels) 통해 간접적으로 사운드를 *지정하고* (O+ 디바이스 대상) 대시보드에서 개별 사운드를 전송하는 방법(<O 디바이스 대상)을 사용하는 것이 좋습니다.

