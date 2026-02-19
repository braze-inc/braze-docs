---
nav_title: 동영상
article_title: 인앱 메시지 내 동영상
page_order: 4
page_type: reference
description: "이 문서에서는 HTML 인앱 메시지에 동영상을 삽입하는 방법에 대해 설명합니다."
channel:
  - in-app messages
---

# 비디오 {#video}

> HTML 인앱 메시지에서 동영상을 재생하려면 HTML에 다음 `<video>` 요소를 포함하고 동영상 이름을 파일 이름(또는 원격 자산의 URL)으로 바꿉니다. You can find other possible `<video>` options on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

로컬 동영상 에셋을 사용하려면 캠페인에 에셋을 업로드할 때 이 파일을 포함해야 합니다.

{% alert note %}
동영상 콘텐츠는 디바이스의 네트워크 속도가 적절한 경우에만 사용할 수 있으며, 로컬에서 비디오를 소싱하지 않는 한 기기에서 사용할 수 없습니다.
{% endalert %}

## Android 고려 사항

Android에서 HTML 인앱 메시지에 동영상 및 기타 HTML5 콘텐츠를 포함하려면 인앱 메시지가 표시되는 활동에서 하드웨어 가속을 사용하도록 설정해야 합니다. For more information, refer to the [Android developer guide]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

**자동 재생**: 하드웨어 가속이 인에이블먼트된 경우에도 Android WebViews에서는 미디어 재생을 시작하기 위해 사용자 제스처가 필요할 수 있습니다. 자동 재생이 필요한 경우, HTML 인앱 메시지를 렌더링하는 데 사용되는 웹뷰를 설정하여 사용자 제스처 요구 사항을 비활성화하도록 구성합니다. [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). 이를 위해서는 HTML 인앱 메시지가 표시되는 방식에 대한 소프트웨어 개발 키트 수준의 커스텀이 필요합니다. 설정 지침은 [Braze SDK용 인앱 메시지 커스텀하기를]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android) 참조하세요.

## iOS 고려 사항

iOS 기기를 지원하려면:

- 전체화면 재생은 지원되지 않으므로 `playsinline` 속성을 포함해야 합니다.
- iOS에서는 **자동 재생이 보장되지 않습니다**. iOS 재생 동작은 `WKWebView` 및 OS 수준 미디어 정책에 따라 달라지며 `autoplay` 및 `muted` 설정된 경우에도 사용자 제스처가 필요할 수 있습니다. 타겟 iOS 버전 및 기기에서 HTML 인앱 메시지를 테스트하세요.

자동 재생이 필요한데 테스트 결과 기본값으로 작동하지 않는 경우, 예를 들어 `mediaTypesRequiringUserActionForPlayback` 속성을 설정하는 등 HTML 인앱 메시지에 사용되는 `WKWebViewConfiguration` 을 커스텀하여 미디어 재생 사용자 작업 요구 사항을 조정할 수 있습니다. 이를 위해서는 소프트웨어 개발 키트 수준의 커스텀이 필요합니다. Swift 리소스에 대한 자세한 내용은 [Braze SDK용 인앱 메시지 커스텀하기]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) 및 [Swift용 WebView에 Braze JavaScript 인터페이스 추가하기를]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift) 참조하세요.

## 웹 고려 사항

대부분의 최신 브라우저는 특정 조건(일반적으로 동영상이 음소거된 경우)에서만 자동 재생을 허용합니다. 웹 인앱 메시지에 `autoplay` 을 사용하는 경우 브라우저 정책에 따라 다르며 경우에 따라 사용자 제스처가 필요할 수 있으므로 `muted` 을 포함하여 지원되는 브라우저 및 기기에서 테스트하세요.