{% tab swift %}
각 인앱 메시지 유형은 콘텐츠, 이미지, 아이콘, 클릭 동작, 분석, 표시 및 전달 전반에 걸쳐 고도로 사용자 지정 가능합니다. 모든 인앱 메시지의 기본 동작과 특성을 정의하는 `Braze.InAppMessage` 의 열거된 유형입니다. 인앱 메시지 속성 및 사용법에 대한 전체 목록은 [`InAppMessage` 클래스를](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) 참조하세요.

다음은 Braze에서 사용할 수 있는 인앱 메시지 유형과 최종 사용자에게 표시되는 방식입니다.

{% subtabs %}
{% subtab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) 인앱 메시지는 화면 상단 또는 하단에서 "슬라이드 업" 또는 "슬라이드 다운"되기 때문에 이 이름이 붙여졌습니다. 화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

![휴대폰 화면 하단과 상단에 슬라이드업 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 중앙에 표시되는 모달 인앱 메시지.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 이러한 메시지는 헤더나 메시지 텍스트가 없다는 점을 제외하면 `Modal` 유형과 유사합니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 중앙에 표시되는 모달 이미지 인앱 메시지.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `Full` 인앱 메시지의 상단에는 이미지가, 하단에는 텍스트와 최대 2개의 분석 지원 버튼이 표시됩니다.

![휴대폰 화면 전체에 표시되는 전체 화면 인앱 메시지.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) 인앱 메시지는 헤더나 메시지 텍스트가 없다는 점을 제외하면 `Full` 인앱 메시지와 유사합니다. 이 메시지 유형은 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `Full Image` 인앱 메시지에는 전체 화면에 걸친 이미지와 함께 최대 2개의 분석 지원 버튼을 표시하는 옵션이 포함되어 있습니다.

![휴대폰 화면 전체에 표시되는 전체 화면 이미지 인앱 메시지.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) 인앱 메시지는 완전히 맞춤화된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML 전체 인앱 메시지 콘텐츠는 `WKWebView`에 표시되며, 선택적으로 이미지 및 글꼴과 같이 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. <br><br>iOS 인앱 메시지는 HTML 내에서 Braze 웹 SDK의 메서드를 호출하기 위해 JavaScript `brazeBridge` 인터페이스를 지원합니다. 자세한 내용은 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)를 참조하세요.

다음 예는 페이지가 지정된 HTML 전체 인앱 메시지를 보여줍니다:

![콘텐츠 캐러셀과 대화형 버튼이 포함된 HTML 인앱 메시지입니다.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

현재 iOS 및 Android 플랫폼에서는 iFrame에 커스텀 HTML 인앱 메시지를 표시하는 기능을 지원하지 않습니다.

{% endsubtab %}
{% subtab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) 인앱 메시지에는 UI 구성요소가 포함되어 있지 않으며 주로 분석 목적으로 사용됩니다. 이 유형은 대조군에 전송된 인앱 메시지의 수신을 확인하는 데 사용됩니다.

지능형 선택 및 대조군에 대한 자세한 내용은 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)을 참조하세요.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
