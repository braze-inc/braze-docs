---
nav_title: "풍부한 알림 만들기"
article_title: "iOS용 리치 푸시 알림 만들기"
page_order: 3
page_type: tutorial
description: "이 튜토리얼에서는 Braze 캠페인용 iOS 리치 알림을 만드는 방법에 대한 요구 사항과 단계를 설명합니다."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# iOS용 리치 푸시 알림 만들기

> 리치 알림을 사용하면 복사본 외에 추가 콘텐츠를 추가하여 푸시 알림을 더욱 맞춤 설정할 수 있습니다. Android 알림에는 한동안 푸시 알림에 이미지가 포함되어 "확장된 알림 이미지"라는 메시지로 전달되었습니다. iOS 10부터는 고객이 GIF, 이미지, 동영상 또는 오디오가 포함된 iOS 푸시 알림을 받을 수 있습니다.

## 필수 조건

iOS용 리치 푸시 알림을 만들기 전에 다음 세부정보를 확인하세요:

- To ensure your app can send rich notifications, follow the [iOS push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications) instructions, as your developer will need to add a service extension to your app.
- 현재 대시보드 내에서 직접 업로드할 수 있도록 지원하는 파일 형식은 JPEG, PNG 또는 GIF입니다. 이러한 파일은 이러한 추가 파일 유형과 함께 템플릿 가능한 URL 필드에 입력할 수도 있습니다: AIF, M4A, MP3, MP4 또는 WAV.
- Reference [Apple's documentation](https://developer.apple.com/reference/usernotifications/unnotificationattachment) for media limitations and specs.
- 빠른 푸시 캠페인을 만들 때는 iOS 리치 알림을 사용할 수 없습니다.
- iOS는 화면에 맞게 이미지 크기를 조정하고 활성 또는 잠긴 보기의 리치 이미지 크기를 조정합니다.

{% alert note %}
2020년 1월부터 iOS 리치 푸시 알림은 10MB 미만의 1038x1038 이미지를 처리할 수 있지만, 가능한 한 작은 파일 크기를 사용하는 것이 좋습니다. 실제로 대용량 파일을 전송하면 불필요한 네트워크 스트레스가 발생하고 다운로드 시간 초과가 더 자주 발생할 수 있습니다.
{% endalert %}

### 문자 수

푸시에 포함할 정확한 문자 수에 대한 명확한 규칙을 제공할 수는 없지만, iOS 메시지를 디자인할 때 고려해야 할 [몇 가지 가이드라인을 제공합니다]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/). 이미지의 유무, 사용자 기기의 알림 상태 및 표시 설정, 기기 크기에 따라 약간의 차이가 있을 수 있습니다. 확실하지 않은 경우 짧고 간결하게 작성하세요.

모범 사례로서, Braze는 모바일 푸시 알림에서 선택적 제목과 메시지 본문의 각 텍스트 줄을 약 30-40자로 유지할 것을 권장합니다.

#### 알림 상태

사용자는 다양한 상황에서 푸시 알림을 볼 수 있으며, 다음과 같이 다양한 길이의 텍스트가 표시될 수 있습니다.

<table>
<thead>
  <tr>
    <th>잠금 화면 또는 알림 센터</th>
    <th>확장됨</th>
    <th>기기 활성화</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">가장 일반적인 시나리오입니다.<br><br><b>제목:</b> 텍스트 1줄<br><b>본문:</b> 텍스트 4줄<br><b>이미지:</b> 정사각형 썸네일</td>
    <td width="33%">사용자가 메시지를 길게 누른 경우.<br><br><b>제목:</b> 텍스트 1줄<br><b>본문:</b> 텍스트 7줄<br><b>이미지:</b> 2:1 화면비(권장, 다음 참고 사항 참조)</td>
    <td width="33%">사용자가 휴대전화가 잠금 해제되어 활성화된 상태에서 푸시를 받는 경우.<br><br><b>제목:</b> 텍스트 1줄<br><b>본문:</b> 텍스트 2줄</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![잠금 화면에 표시되는 푸시 알림, 확장 시 및 기기가 활성화되었을 때의 푸시 알림 예시]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
확장된 푸시 알림에는 2:1 화면 비율을 권장하지만, 거의 모든 화면 비율이 지원됩니다. 이미지는 항상 알림의 전체 너비에 걸쳐 표시되며, 그에 따라 높이가 조정됩니다.
{% endalert %}

#### 텍스트 잘림의 변수

콘텐츠를 만들 때 표시되는 텍스트 양에 영향을 줄 수 있는 다음 시나리오를 고려하세요.

{% tabs %}
{% tab 타이밍 %}

사용자가 푸시 알림에 참여하는 시점에 따라 타임스탬프가 제목 텍스트를 단축할 수 있습니다.

![타임스탬프가 "지금"이고 제목 글자 수가 35인 푸시 알림 예시]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>제목 글자 수: **35**

![타임스탬프가 '3시간 전'이고 제목 글자 수가 33자인 푸시 알림 예시]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>제목 글자 수: **33**

![타임스탬프가 "어제 오전 8시 37분"이고 제목 글자 수가 22인 푸시 알림의 예.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>제목 글자 수: **22**

{% endtab %}
{% tab 이미지 %}

이미지가 있는 경우 본문 텍스트는 한 줄당 약 10자씩 줄어듭니다.

![이미지가 없고 본문 글자 수가 179자인 푸시 알림의 예.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>본문 글자 수: **179**

![이미지와 본문 글자 수 154자가 포함된 푸시 알림 예시]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>본문 글자 수: **154**

{% endtab %}
{% tab 중단 수준 %}

iOS 15의 경우, 시간 민감 및 중요 표시가 제목을 타임스탬프 없이 새 줄로 밀어내어 약간 더 많은 공간을 제공합니다.

![시간 민감 또는 중요 표시가 없고 제목 글자 수가 35자인 푸시 알림 예시]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>제목 글자 수: **35**

![시간 민감 표시가 있고 제목 문자 수가 39인 푸시 알림 예시]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>제목 글자 수: **39**

{% endtab %}
{% tab 자세히 보기 %}

다음 세부정보도 텍스트 잘림에 영향을 줄 수 있습니다:

- **휴대폰 디스플레이 설정:** 사용자는 일반적으로 접근성을 위해 휴대폰의 글로벌 UI 글꼴 크기를 늘리거나 줄일 수 있습니다.
- **기기 너비:** 메시지가 작은 휴대폰이나 넓은 iPad에 표시될 수 있습니다.
- **콘텐츠 유형:** 이모티콘과 "m", "w"와 같은 넓은 문자는 "i"나 "t"보다 더 많은 공간을 차지하며, "인게이지먼트"와 같은 긴 단어는 짧은 단어보다 줄 바꿈이 더 심할 수 있습니다.

{% endtab %}
{% endtabs %}

## iOS 리치 알림 설정하기

### 1단계: 푸시 캠페인 만들기

Follow the [campaign steps]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) to compose a push notification for iOS. 리치 콘텐츠가 포함되지 않은 푸시 알림을 설정할 때 사용하는 것과 동일한 작성기를 사용하게 됩니다.

### 2단계: 미디어 추가

메시지 작성창의 **리치 알림 미디어** 필드에 이미지, GIF, 오디오 또는 동영상 파일을 추가합니다. 콘텐츠 파일을 추가하는 방법에 대한 [요구 사항](#requirements)을 참조하세요.

![An example of summary text for a push notification.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

iOS 10에서 실행되는 기기를 보유한 사용자에게만 메시지를 보내도록 이 메시지를 제한할 수도 있습니다. iOS 10으로 업그레이드하지 않은 사용자의 경우 **리치 알림을 지원하는 기기로만 보내기**를 선택하지 않은 상태로 두면 리치 콘텐츠가 없는 텍스트 전용 알림으로 표시됩니다.

![The Expanded notification image section where you can add an image or enter an image URL.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### 3단계: 캠페인 계속 만들기

Once your rich notification content is uploaded to the dashboard, you can continue [scheduling your campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign).

사용자가 푸시 알림을 받으면 푸시 메시지를 세게 눌러 이미지를 확대할 수 있습니다.

![A user receives a push notification and hard presses the message to show an expanded image that says "Hello!".]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }

