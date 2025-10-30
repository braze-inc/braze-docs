---
nav_title: 비디오
article_title: 인앱 메시징 내 비디오
page_order: 4
page_type: reference
description: "이 문서에서는 HTML 인앱 메시지에 동영상을 삽입하는 방법에 대해 설명합니다."
channel:
  - in-app messages
---

# 비디오 {#video}

> HTML 인앱 메시지에서 동영상을 재생하려면 HTML에 다음 `<video>` 요소를 포함시키고 동영상 이름을 파일 이름(또는 원격 자산의 URL)으로 바꿉니다. 다른 가능한 `<video>` 옵션은 [MDN 웹 문서에서](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) 찾을 수 있습니다.

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

현지 동영상 자산을 사용하려면 캠페인에 자산을 업로드할 때 이 파일을 포함해야 합니다.

{% alert note %}
동영상 콘텐츠는 기기의 네트워크 속도가 적절한 경우에만 사용할 수 있으며, 기기에 로컬로 동영상을 소싱하지 않는 한 사용할 수 없습니다.
{% endalert %}

## Android 고려 사항

Android에서 HTML 인앱 메시지에 동영상 및 기타 HTML5 콘텐츠를 삽입하려면 인앱 메시지가 표시되는 활동에서 하드웨어 가속을 인에이블먼트해야 합니다. 자세한 내용은 [Android 개발자 가이드를]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content) 참조하세요.

## iOS 고려 사항

iOS 기기를 지원하려면:

- 현재 전체화면 재생은 지원되지 않으므로 `playsinline` 속성을 포함해야 합니다.
- iOS는 기본값으로 자동 재생을 지원하지 않습니다. 이 기본값을 업데이트하려면 이 옵션을 수정하면 됩니다. [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)


