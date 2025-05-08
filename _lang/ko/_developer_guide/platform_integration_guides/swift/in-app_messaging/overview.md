---
nav_title: 통합
article_title: iOS용 인앱 메시지 개요
platform: Swift
page_order: 0
description: "이 문서에서는 iOS 인앱 메시징 유형, 예상 동작 및 Swift SDK의 여러 사용 사례를 다룹니다."
channel:
  - in-app messages

---

# 인앱 메시지 통합

> [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)는 푸시 알림을 통해 일과를 방해하지 않고 사용자에게 콘텐츠를 전달할 수 있도록 도와줍니다. 사용자 지정 및 맞춤 조정된 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다. 다양한 레이아웃과 사용자 지정 도구를 선택할 수 있는 인앱 메시지는 그 어느 때보다 사용자의 참여를 유도할 수 있습니다.

인앱 메시지의 예제를 보려면 [사례 연구](https://www.braze.com/customers)를 참조하세요.

## 인앱 메시지 유형

Braze는 현재 다음과 같은 기본 인앱 메시지 유형을 제공합니다: 

- 슬라이드업
- Modal
- 모달 이미지
- 전체
- 전체 이미지
- 사용자 지정 HTML
- 제어

각 인앱 메시지 유형은 콘텐츠, 이미지, 아이콘, 클릭 동작, 분석, 표시 및 전달 전반에 걸쳐 고도로 사용자 지정 가능합니다.

인앱 메시지 속성정보 및 사용법에 대한 전체 목록은 [`InAppMessage` 클래스 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage)를 참조하세요.

모든 인앱 메시지 유형은 모든 인앱 메시지의 기본 동작과 특성을 정의하는 `Braze.InAppMessage`의 열거형입니다. 각 인앱 메시지 유형과 해당 세부 정보는 아래 탭에 나와 있습니다.

### 메시지 유형별 예상 동작

다음은 사용자가 기본 인앱 메시지 유형 중 하나를 여는 상황입니다.

{% tabs %}
{% tab 슬라이드업 %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) 인앱 메시지는 화면 상단 또는 하단에서 '슬라이드 업' 또는 '슬라이드 다운'되기 때문에 그렇게 이름이 붙여졌습니다. 화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

![휴대폰 화면 하단과 상단에 슬라이드업 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab 모달 %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 중앙에 표시되는 모달 인앱 메시지.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Modal 이미지 %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 이러한 메시지는 헤더나 메시지 텍스트가 없다는 점을 제외하면 `Modal` 유형과 유사합니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 중앙에 표시되는 모달 이미지 인앱 메시지.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab 전체 화면 %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `Full` 인앱 메시지의 상단에는 이미지가, 하단에는 텍스트와 최대 2개의 분석 지원 버튼이 표시됩니다.

![휴대폰 화면 전체에 표시되는 전체 화면 인앱 메시지.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab 전체 화면 이미지 %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) 인앱 메시지는 헤더나 메시지 텍스트가 없다는 점을 제외하면 `Full` 인앱 메시지와 유사합니다. 이 메시지 유형은 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `Full Image` 인앱 메시지에는 전체 화면에 걸친 이미지와 함께 최대 2개의 분석 지원 버튼을 표시하는 옵션이 포함되어 있습니다.

![휴대폰 화면 전체에 표시되는 전체 화면 이미지 인앱 메시지.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab 사용자 지정 HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) 인앱 메시지는 완전히 맞춤화된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML 전체 인앱 메시지 콘텐츠는 `WKWebView`에 표시되며, 선택적으로 이미지 및 글꼴과 같이 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. <br><br>iOS 인앱 메시지는 HTML 내에서 Braze 웹 SDK의 메서드를 호출하기 위해 JavaScript `brazeBridge` 인터페이스를 지원합니다. 자세한 내용은 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)를 참조하세요.

다음 예는 페이지가 지정된 HTML 전체 인앱 메시지를 보여줍니다:

![콘텐츠 캐러셀과 대화형 버튼이 포함된 HTML 인앱 메시지입니다.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

현재 iOS 및 Android 플랫폼에서는 iFrame에 커스텀 HTML 인앱 메시지를 표시하는 기능을 지원하지 않습니다.

{% endtab %}
{% tab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) 인앱 메시지에는 UI 구성요소가 포함되어 있지 않으며 주로 분석 목적으로 사용됩니다. 이 유형은 대조군에 전송된 인앱 메시지의 수신을 확인하는 데 사용됩니다.

지능형 선택 및 대조군에 대한 자세한 내용은 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)을 참조하세요.

{% endtab %}
{% endtabs %}


{% alert important %}
표준 SDK 통합에는 GIF 지원을 포함하여 인앱 메시지를 활성화하는 단계가 포함되어 있습니다. GIF 지원에 대한 자세한 내용은 이 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)을 참조하세요.
{% endalert %}


