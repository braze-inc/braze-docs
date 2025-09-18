---
nav_title: 위치 추적
article_title: Windows Universal을 위한 위치 추적
platform: Windows Universal
page_order: 6
description: "이 참조 문서에서는 Windows Universal 앱에 위치 추적을 추가하는 방법을 다룹니다."
tool: Location
hidden: true
---

# 위치 추적
{% multi_lang_include archive/windows_deprecation.md %}

1. `Package.appxmanifest` 파일 내에서 `location`이 확인되었는지 확인하세요.
2. 자동 위치 추적을 끄려면 `AppboyConfiguration.xml`에서 `<DisableLocationCollection>false</DisableLocationCollection>`를 `true`로 설정하세요.
