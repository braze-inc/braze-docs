---
nav_title: 개요
article_title: iOS용 인앱 메시지 개요
platform: iOS
page_order: 0
description: "이 참조 문서에서는 iOS 인앱 메시징 유형, 예상 동작 및 여러 사용 사례를 다룹니다."
channel:
  - in-app messages
search_rank: 4
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 인앱 메시지

[인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)는 푸시 알림을 통해 일과를 방해하지 않고 사용자에게 콘텐츠를 전달할 수 있도록 도와줍니다. 사용자 지정 및 맞춤 조정된 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다. 다양한 레이아웃과 사용자 지정 도구를 선택할 수 있는 인앱 메시지는 그 어느 때보다 사용자의 참여를 유도할 수 있습니다.

인앱 메시지의 예제를 보려면 [사례 연구](https://www.braze.com/customers)를 참조하세요.

## 인앱 메시지 유형

Braze는 현재 다음과 같은 기본 인앱 메시지 유형을 제공합니다: 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

각 인앱 메시지 유형은 콘텐츠, 이미지, 아이콘, 클릭 동작, 분석, 표시 및 전달 전반에 걸쳐 고도로 사용자 지정 가능합니다.

모든 인앱 메시지는 모든 인앱 메시지의 기본 동작과 특성을 정의하는 `ABKInAppMessage`의 서브클래스입니다. 인앱 메시지 클래스 구조는 다음과 같습니다:

![ABKInAppMessage 클래스가 ABKInAppMessageSlideup, ABKInAppMessageImmersive, ABKInAppMessageHTML의 루트 클래스임을 보여주는 그래픽. ABKInAppMessage에는 메시지, 추가 항목, 기간, 클릭 동작, URI, 해제 동작, 아이콘 방향 및 텍스트 정렬과 같은 사용자 지정 가능한 속성정보가 포함되어 있습니다. ABKInAppMessageSlideup에는 갈매기형 및 슬라이드업 앵커와 같은 사용자 지정 가능한 속성정보가 포함되어 있습니다. ABKInAppMessageImmersive에는 헤더, 닫기 버튼, 프레임 및 인앱 메시지 버튼과 같은 사용자 지정 가능한 속성정보가 포함되어 있습니다. ABKInAppMessageHTML을 사용하면 HTML 인앱 메시지 버튼 클릭을 수동으로 기록할 수 있습니다.]({% image_buster /assets/img_archive/ABKInAppMessage-models.png %})

{% alert important %}
기본적으로 인앱 메시지는 GIF 지원을 포함하여 표준 SDK 통합을 완료한 후에 활성화됩니다.
<br><br>
iOS 인앱 메시지 또는 콘텐츠 카드에서 이미지를 표시하기 위해 Braze UI를 사용하려는 경우 `SDWebImage`의 통합이 필요합니다.
{% endalert %}

### 메시지 유형별 예상 동작

다음은 사용자가 기본 인앱 메시지 유형 중 하나를 여는 상황입니다.

{% tabs %}
{% tab 슬라이드업 %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) 인앱 메시지는 화면 상단 또는 하단에서 '슬라이드 업' 또는 '슬라이드 다운'되기 때문에 그렇게 이름이 붙여졌습니다. 화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

![휴대폰 화면 하단에서 '인간은 복잡하다'는 인앱 메시지가 슬라이딩되는 모습. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 하단에 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}


{% endtab %}
{% tab 모달 %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 클릭 동작과 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 가운데 다음과 같은 Modal 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 전체 화면 %}

[`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `full` 인앱 메시지의 상단에는 이미지가, 하단에는 텍스트와 최대 2개의 클릭 동작 및 분석 지원 버튼이 표시됩니다.

![휴대폰 화면 전체에 다음과 같은 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 크게 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 사용자 지정 HTML %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) 인앱 메시지는 완전히 맞춤화된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML 전체 인앱 메시지 콘텐츠는 `WKWebView`에 표시되며, 선택적으로 이미지 및 글꼴과 같이 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. <br><br>iOS 인앱 메시지는 HTML 내에서 Braze 웹 SDK의 메서드를 호출하기 위해 JavaScript `brazeBridge` 인터페이스를 지원합니다. 자세한 내용은 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)를 참조하세요.

다음 예는 페이지가 지정된 HTML 전체 인앱 메시지를 보여줍니다:

![콘텐츠 캐러셀과 대화형 버튼이 포함된 HTML 인앱 메시지입니다.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

전체 인앱 메시지 콘텐츠는 `WKWebView`에 표시되며, 선택적으로 이미지 및 글꼴과 같은 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. 현재 iOS 및 Android 플랫폼에서는 iFrame에 커스텀 HTML 인앱 메시지를 표시하는 기능을 지원하지 않습니다.

{% alert note %}
iOS SDK 버전 3.19.0부터 `alert`, `confirm`, `prompt`와 같은 JavaScript 메서드는 HTML 인앱 메시지에서 사용할 수 없습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

