---
nav_title: 메시지 형식
article_title: 푸시 메시지 및 이미지 형식
page_order: 5
page_type: reference
description: "이 문서에서는 푸시 알림의 메시지 및 이미지 형식에 대해 설명합니다."
channel: push

---

# 푸시 메시지 및 이미지 형식

> 이 참고 문서에서는 푸시 알림의 메시지 및 이미지 형식에 대해 설명합니다.

최상의 결과를 얻으려면 푸시 메시지를 작성할 때 다음 이미지 크기 및 메시지 길이 가이드라인을 참조하세요. 이미지의 유무, 사용자 기기의 알림 상태(iOS) 및 디스플레이 설정, 기기 크기에 따라 약간의 차이가 있을 수 있습니다. 확실하지 않은 경우에는 짧고 간결하게 작성하세요.

## iOS 및 Android 푸시

{% tabs local %}
{% tab Images %}

**이미지 유형** | **권장 이미지 크기** | **최대 이미지 크기** | **파일 형식**
--- | --- | --- | ---
(iOS) 2:1 *권장* | 500 KB | 5MB | PNG, JPEG, GIF
(Android) 푸시 아이콘 | 500 KB | 5MB | PNG, JPEG
(Android) 확장 알림 | 500 KB | 5MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Text %}

| 메시지 유형 | 권장 메시지 길이(텍스트만 해당) | 권장 메시지 길이(리치)
--- | ---
(iOS) 잠금 화면 | 160자 | 130자
(iOS) 알림 센터 | 160자 | 130자
(iOS) 배너 알림 | 80자 | 65자
(Android) 잠금 화면 | 49자 | N/A
(Android) 알림 서랍 | 597자 | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS 푸시 알림에서 잘리지 않고 사용할 수 있는 글자 수가 궁금하신가요? [iOS 문자 수 가이드라인을]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count) 확인하세요.

{% endtab %}
{% tab Payload Size %}

**플랫폼** | **크기**
--- | ---
iOS 8 이전 | 0.256 KB
포스트 iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image Example %}
{% subtabs %}
{% subtab iOS %}

!"라는 텍스트가 포함된 iOS 푸시 알림이 표시됩니다: "안녕하세요! 이모티콘이 포함된 iOS 푸시입니다."라는 메시지가 표시됩니다. 텍스트 옆에 작은 이미지가 있습니다.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
이전 메시지와 동일한 텍스트와 함께 텍스트 앞에 확장된 이미지가 포함된 하드 푸시 푸시 알림이 표시됩니다.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

메시지 텍스트 아래에 큰 이미지가 포함된 Android 푸시 알림.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
큰 이미지 알림은 최소 600x300픽셀의 이미지를 사용할 때 가장 잘 표시됩니다.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Text Example %}
{% subtabs %}
{% subtab iOS %}

!"라는 텍스트가 포함된 iOS 푸시 알림이 표시됩니다: "안녕하세요! iOS 푸시입니다".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
홈 화면에 표시되는 Android 푸시 알림.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 웹 푸시

{% tabs local %}
{% tab Images %}

| **브라우저** | **권장 아이콘 크기**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (아이콘은 MacOS 13 이상에서 Safari 16을 사용하여 캠페인별로 구성할 수 있습니다.)
오페라 | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **브라우저** | **플랫폼** | **큰 이미지 크기**
| --- | --- | ---
Chrome | Android | 2:1 종횡비
Firefox | Android | N/A
Chrome | Windows | 2:1 종횡비
Edge | Windows | 2:1 종횡비
Firefox | Windows | N/A
Firefox | Windows | 2:1 종횡비
Safari | MacOS | N/A
Chrome | MacOS | N/A
Firefox | MacOS | N/A
오페라 | MacOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| **브라우저** | **플랫폼** | **최대 타이틀 길이**  | **최대 메시지 본문 길이**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
오페라 | Windows | 50 | 120
Chrome | MacOS | 35 | 50
Safari | MacOS | 38 | 84
Firefox | MacOS | 38 | 42
오페라 | MacOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


