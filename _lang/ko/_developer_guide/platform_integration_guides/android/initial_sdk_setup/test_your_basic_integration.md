---
nav_title: 기본 통합을 테스트하십시오
article_title: Android 및 FireOS용 기본 통합 테스트
page_order: 1
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 대한 기본 통합을 테스트하는 방법을 다룹니다."

---

# 기본 통합을 테스트하십시오

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 대한 기본 통합을 테스트하는 방법을 다룹니다.

## 세션 추적이 작동하는지 확인

이때 Braze 통합에서 세션 추적이 작동해야 합니다. 테스트하려면 **개요**로 이동하여 선택한 앱 이름 드롭다운에서 애플리케이션을 선택하고(기본값: '모든 앱') **데이터 표시 기준**을 '오늘'로 설정합니다. 그런 다음 앱을 열고 페이지를 새로고침하세요. 주요 측정기준이 모두 1씩 증가했을 것입니다.

![]({% image_buster /assets/img_archive/android_sessions.png %})

애플리케이션을 탐색하면서 하나의 세션만 기록되는지 확인하여 통합을 계속 테스트해야 합니다. 그런 다음, 최소 10초 동안 백그라운드에서 앱을 실행한 후 다시 포그라운드로 전환합니다. 기본적으로 10초 후에 앱을 닫거나 백그라운드였다가 포그라운드로 다시 전환되면 새 세션이 생성됩니다. 이 작업을 완료한 후 다른 세션이 기록되었는지 확인하십시오.

## 디버깅 세션 추적
세션 추적이 예기치 않게 작동하는 경우 [자세한 로깅을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#enabling-logs) 켜고 세션 트리거 단계를 재현하는 동안 앱을 관찰하세요. logcat에서 Braze 명령을 관찰하여 활동에서 `openSession` 및 `closeSession` 호출을 기록하지 않은 위치를 감지합니다.

