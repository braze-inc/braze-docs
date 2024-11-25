---
nav_title: HTML로 보는 YouTube
article_title: Android 및 FireOS용 HTML 인앱 메시지에서 YouTube
platform: 
  - Android
  - FireOS
page_order: 8
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션용 HTML 인앱 메시지에 YouTube 비디오를 추가하는 방법을 다룹니다."
channel:
  - in-app messages

---

# HTML로 보는 YouTube

> YouTube 및 기타 HTML5 콘텐츠는 HTML 인앱 메시지에서 재생할 수 있습니다. 이를 위해 인앱 메시지가 표시되는 활동에서 하드웨어 가속을 활성화해야 합니다. 자세한 내용은 [Android 개발자 가이드](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling)를 참조하세요. 하드웨어 가속은 Android API 버전 11 이상에서만 사용할 수 있습니다.

다음은 HTML 스니펫에 임베드된 YouTube 동영상의 예시입니다:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```

