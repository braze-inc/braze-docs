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

**자동 재생**: 하드웨어 가속이 활성화되어 있어도, Android WebView는 미디어 재생을 시작하기 위해 사용자 제스처가 필요할 수 있습니다. 자동 재생이 필요하면, HTML 인앱 메시지를 렌더링하는 데 사용되는 WebView를 구성하여 사용자 제스처 요구 사항을 비활성화해야 합니다 [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). 이는 HTML 인앱 메시지가 표시되는 방식을 SDK 수준에서 사용자 정의해야 합니다. 설정 안내는 [Braze SDK에 대한 인앱 메시지 사용자 정의]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)를 참조하십시오.

## iOS 고려 사항

iOS 기기를 지원하려면:

- 전체 화면 재생이 지원되지 않기 때문에 `playsinline` 속성을 포함해야 합니다.
- **iOS에서 자동 재생이 보장되지 않습니다**. iOS 재생 동작은 `WKWebView` 및 OS 수준의 미디어 정책에 따라 달라지며, `autoplay` 및 `muted`가 설정되어 있어도 사용자 제스처가 필요할 수 있습니다. 대상 iOS 버전 및 장치에서 HTML 인앱 메시지를 테스트하십시오.

자동 재생이 필요하고 테스트에서 기본적으로 작동하지 않는 경우, HTML 인앱 메시지에서 사용되는 `WKWebViewConfiguration`을 사용자 정의하여 미디어 재생 사용자 작업 요구 사항을 조정할 수 있습니다. 예를 들어 `mediaTypesRequiringUserActionForPlayback` 속성을 설정하여 조정할 수 있습니다. 이는 SDK 수준에서 사용자 정의가 필요합니다. Swift 리소스는 [Braze SDK에 대한 인앱 메시지 사용자 정의]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) 및 [Swift용 WebView에 Braze JavaScript 인터페이스 추가]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift)를 참조하십시오.

## 웹 고려사항

대부분의 최신 브라우저는 특정 조건에서만 자동 재생을 허용합니다(일반적으로 비디오가 음소거된 경우). 웹 인앱 메시지에서 `autoplay`을 사용하는 경우, `muted`을 포함하고 지원되는 브라우저 및 장치에서 테스트하십시오. 브라우저 정책이 다르며 일부 경우에는 여전히 사용자 제스처가 필요할 수 있습니다.