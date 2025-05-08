---
nav_title: 통합
article_title: 웹용 인앱 메시지 통합
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "이 문서에는 웹 애플리케이션의 인앱 메시지 유형 및 메시지 동작에 대한 리소스가 포함되어 있습니다."
search_rank: 2
---

# 인앱 메시지 통합

> 이 문서에서는 웹 애플리케이션의 인앱 메시지를 설정하는 방법에 대해 설명합니다.

[인앱 메시지는]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) 푸시 알림을 통해 사용자의 일과를 방해하지 않고 콘텐츠를 전달할 수 있도록 도와줍니다. 사용자 지정 및 맞춤 조정된 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다. 다양한 레이아웃과 사용자 지정 툴을 선택하여 인앱 메시지를 통해 그 어느 때보다 높은 사용자 참여를 유도할 수 있습니다.

인앱 메시지의 예제를 보려면 [사례 연구](https://www.braze.com/customers)를 참조하세요.

## 인앱 메시지 유형

Braze는 현재 다음과 같은 기본 인앱 메시지 유형을 제공합니다: 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

각 인앱 메시지 유형은 콘텐츠, 이미지, 아이콘, 클릭 동작, 분석, 표시 및 전달 전반에 걸쳐 사용자 지정 가능합니다.

모든 인앱 메시지는 모든 인앱 메시지의 기본 동작과 특성을 정의하는 [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)에서 프로토타입을 상속하며, 이는 모든 인앱 메시지의 기본 동작과 특성을 정의합니다. 대표적인 서브클래스는 [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)와 [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

## 메시지 유형별 예상 동작

다음은 사용자가 기본 인앱 메시지 유형 중 하나를 여는 상황입니다.

{% tabs %}
{% tab 슬라이드업 %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) 인앱 메시지는 전통적으로 모바일 플랫폼에서 화면 위나 아래에서 '슬라이드 업' 또는 '슬라이드 다운'되기 때문에 그렇게 명명되었습니다. Braze 웹 SDK에서 이러한 메시지가 웹의 주요 패러다임에 맞춰 Growl 또는 Toast 스타일의 알림으로 표시됩니다. 화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

![휴대폰 화면 하단에서 '인간은 복잡하다'는 인앱 메시지가 슬라이딩되는 모습. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 하단에 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 모달 %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 클릭 동작과 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 가운데 다음과 같은 Modal 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 전체 화면 %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. 좁은 브라우저 창(예: 모바일 웹)에서는 `full` 인앱 메시지는 전체 브라우저 창을 차지합니다. 더 큰 브라우저 창에서는 `full` 인앱 메시지가 `modal` 인앱 메시지와 비슷하게 표시됩니다. `full` 인앱 메시지의 상단에는 이미지가 있고, 하단에는 최대 8줄의 텍스트와 최대 2개의 클릭 동작 및 분석 지원 버튼이 표시됩니다.

![휴대폰 화면 전체에 다음과 같은 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 크게 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 사용자 지정 HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) 인앱 메시지는 완전히 맞춤화된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML은 iFrame에 표시되며, 이미지, 글꼴, 비디오와 같은 다양한 형식의 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. 이 기능은 HTML 내에서 Braze 웹 SDK의 메서드를 호출하기 위해 JavaScript `brazeBridge` 인터페이스를 지원합니다. 자세한 내용은 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)를 참조하세요.

{% alert important %}

웹 SDK를 통해 HTML 인앱 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공**해야** 합니다(예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`). 이는 보안상의 이유 때문입니다. HTML 인앱 메시지는 JavaScript를 실행할 수 있으므로 사이트 관리자가 이를 활성화해야 합니다.

{% endalert %}

다음 예는 페이지가 지정된 HTML 인앱 메시지를 보여줍니다:

![콘텐츠 캐러셀과 대화형 버튼이 포함된 HTML 인앱 메시지입니다.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## 통합

기본적으로 인앱 메시지는 권장되는 [통합 지침]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/). 이 가이드의 단계에 따라 추가 사용자 지정이 가능합니다.

