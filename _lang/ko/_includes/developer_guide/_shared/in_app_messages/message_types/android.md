
{% tab android %}
Braze는 메시지, 이미지, [폰트 어썸](https://fontawesome.com/icons?d=gallery&p=2) 아이콘, 클릭 액션, 분석, 색 구성표 등으로 각각 사용자 지정할 수 있는 여러 가지 기본값 인앱 메시지 유형을 제공합니다.

기본 동작과 특성은 다음과 같은 서브클래스의 [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) 라는 서브클래스의 인터페이스에 의해 정의됩니다. [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html)`IInAppMessage` 에는 하위 인터페이스도 포함되어 있습니다, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)라는 하위 인터페이스도 포함되어 있어 앱에 닫기, 클릭 동작 및 분석 [버튼을](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) 추가할 수 있습니다.

{% alert important %}
버튼 텍스트를 추가하기 전에 클릭 액션이 추가되면 버튼이 포함된 인앱 메시지의 최종 페이로드에 `clickAction` 메시지가 포함된다는 점에 유의하세요.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) 인앱 메시지는 화면 상단 또는 하단에서 '슬라이드 업' 또는 '슬라이드 다운'되기 때문에 그렇게 이름이 붙여졌습니다. 화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

`slideup` 인앱 메시지 오브젝트는 [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html)를 확장합니다.

![휴대폰 화면 하단에서 '인간은 복잡하다'는 인앱 메시지가 슬라이딩되는 모습. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 오른쪽 하단에 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 두 개의 클릭 동작과 분석 지원 버튼을 제공할 수 있습니다.

이 메시지 유형은 추상 클래스인 [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)의 서브클래스로, `IInAppMessageImmersive` 을 구현하는 추상 클래스로서 로컬로 생성된 인앱 메시징에 커스텀 기능을 추가할 수 있는 옵션을 제공합니다.

![휴대폰 화면 가운데 다음과 같은 Modal 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `full` 인앱 메시지의 상단에는 이미지가, 하단에는 텍스트와 최대 2개의 클릭 동작 및 분석 지원 버튼이 표시됩니다.

이 메시지 유형은 확장된 [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)를 확장하여 로컬에서 생성된 인앱 메시지에 커스텀 기능을 추가할 수 있는 옵션을 제공합니다.

![휴대폰 화면 전체에 다음과 같은 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 크게 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) 인앱 메시지는 완전히 맞춤화된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML 인앱 메시지 콘텐츠는 `WebView`에 표시되며, 선택적으로 이미지 및 글꼴과 같은 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다.

이 메시지 유형은 서브 클래스인 [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)의 서브 클래스인 [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

Android 인앱 메시지는 HTML 내에서 Braze 소프트웨어 개발 키트의 메서드를 호출할 수 있는 JavaScript `brazeBridge` 인터페이스를 지원하며, 자세한 내용은 <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">JavaScript 브릿지</a> 페이지를 참조하세요.

![콘텐츠 캐러셀과 대화형 버튼이 포함된 HTML 인앱 메시지입니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
현재 iOS 및 Android 플랫폼에서는 iFrame에 커스텀 HTML 인앱 메시지를 표시하는 기능을 지원하지 않습니다.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
앱에 대한 커스텀 인앱 메시지 보기를 정의할 수도 있습니다. 전체 안내는 [커스텀 공장 설정하기를]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories) 참조하세요.
{% endalert %}
{% endtab %}