---
nav_title: 문제 해결
article_title: Unity 문제 해결
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "이 레퍼런스 문서에서는 Unity 플랫폼에 대한 문제 해결 주제를 다룹니다."

---

# 문제 해결

> 이 문서에서는 몇 가지 Unity 문제 해결 시나리오를 제공합니다.

## "파일을 읽을 수 없습니다" 오류

다음과 유사한 오류는 안전하게 무시해도 됩니다. Apple 소프트웨어는 Unity가 인식하지 못하는 CgBI라는 독점 PNG 확장을 사용합니다. 이러한 오류는 iOS 빌드나 Braze 번들에서 관련 이미지의 올바른 표시에는 영향을 미치지 않습니다.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
