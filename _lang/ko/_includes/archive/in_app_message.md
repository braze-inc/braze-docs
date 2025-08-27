### 슬라이드업 인앱 메시지

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} 인앱 메시지는 화면 상단 또는 하단에서 "슬라이드 업" 또는 "슬라이드 다운"되기 때문에 그렇게 이름이 붙여졌습니다.  화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

![슬라이드업 예시]({% image_buster /assets/img_archive/In-App_Slideup.png %})

### 모달 인앱 메시지

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 최대 두 개의 클릭 동작과 분석 지원 버튼을 제공할 수 있습니다.

![모달 예시]({% image_buster /assets/img_archive/In-App_Modal.png %})

### 전체 인앱 메시지

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다.  `full` 인앱 메시지의 상단에는 이미지가, 하단에는 텍스트와 최대 2개의 클릭 작업 및 분석 활성화 버튼이 표시됩니다.

![전체 예제]({% image_buster /assets/img_archive/In-App_Full.png %})

### HTML 전체 인앱 메시지

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} 인앱 메시지는 완전히 커스텀된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML 전체 인앱 메시지 콘텐츠는 {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %}에 표시되며, 선택적으로 이미지 및 글꼴과 같이 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다.

 {% if include.platform == "iOS" %}
다음 예는 페이지가 지정된 HTML 전체 인앱 메시지를 보여줍니다:

![HTML5 예제]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

 {% elsif include.platform == "Android" %}다음 예는 SoundCloud에서 만든 설문조사 HTML 전체 인앱 메시지를 보여줍니다.

![HTML5 예제]({% image_buster /assets/img_archive/HTML5.gif %})
{% endif %}

전체 인앱 메시지 콘텐츠는 WKWebView에 표시되며 선택적으로 이미지 및 글꼴과 같은 다른 풍부한 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. **현재 iOS 및 Android 플랫폼에서는 iFrame에서 커스텀 HTML 인앱 메시지를 표시하는 기능을 지원하지 않습니다.**

## 인앱 메시지 전달

### 인앱 메시지(트리거됨)

다음 문서는 '캠페인 만들기' 드롭다운에서 아래 강조 표시된 것처럼 브랜드가 표시된 '트리거된 인앱 메시지'라고도 하는 Braze `In-App Messaging` 제품에 대해 설명합니다:

![인앱 메시징 작성기]({% image_buster /assets/img_archive/trigger-iam-composer.png %})

더 이상 사용되지 않는 [`Original In-App Messaging`]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages) 제품에 대한 설명서를 참조할 수도 있습니다.

#### 트리거 유형

인앱 메시지 제품을 사용하면 여러 가지 이벤트 유형(`Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`)에 따라 인앱 메시지 표시를 트리거할 수 있습니다.  게다가, `Specific Purchase` 및 `Custom Event` 트리거는 강력한 속성정보 필터를 포함할 수 있습니다.

{% alert note %}
트리거된 인앱 메시지는 Braze SDK를 통해 기록된 커스텀 이벤트에서만 작동합니다. 인앱 메시지는 API 또는 API 이벤트(예: 구매 이벤트)를 통해 트리거할 수 없습니다. Android로 작업하는 경우 [Android에서 사용자 지정 이벤트 로깅 방법]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events). iOS로 작업하는 경우 [iOS에서 사용자 지정 이벤트 로깅 방법]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

#### 전달 의미 체계

사용자가 받을 수 있는 모든 인앱 메시지는 세션 시작 시 사용자의 기기로 전달됩니다. SDK의 세션 시작 시맨틱에 대한 자세한 내용은 [세션 생애주기 설명서]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}]를 참조하세요. SDK가 제공되면 에셋을 미리 불러와 트리거 시점에 즉시 사용할 수 있도록 하여 디스플레이 지연 시간을 최소화합니다.

트리거 이벤트에 적격한 인앱 메시지가 두 개 이상 연결된 경우 우선순위가 가장 높은 인앱 메시지만 전달됩니다.

세션 시작, 푸시 클릭 등 전송 즉시 표시되는 인앱 메시지의 경우 에셋이 프리페치되지 않아 약간의 지연 시간이 발생할 수 있습니다.

#### 트리거 사이의 최소 시간 간격

기본적으로 양질의 사용자 경험을 위해 인앱 메시지 전송을 30초에 한 번으로 사용량 제한하고 있습니다.

{% if include.platform == "iOS" %}`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달된 `appboyOptions` 매개변수 내부의 `ABKMinimumTriggerTimeIntervalKey`를 통해 이 값을 재정의할 수 있습니다. `ABKMinimumTriggerTimeIntervalKey`을 인앱 메시지 간 최소 시간(초)에 대해 원하는 정수 값으로 설정합니다.

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
이 값을 재정의하려면 `braze.xml`에서 `com_appboy_trigger_action_minimum_time_interval_seconds`를 설정하세요.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle

