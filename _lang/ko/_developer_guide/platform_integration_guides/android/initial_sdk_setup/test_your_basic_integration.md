---
nav_title: 기본 통합을 테스트하십시오
article_title: 기본 통합 테스트 Android 및 FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "이 참조 문서는 Android 또는 FireOS 애플리케이션에 대한 기본 통합을 테스트하는 방법을 다룹니다."

---

# 기본 통합을 테스트하십시오

> 이 참조 문서는 Android 또는 FireOS 애플리케이션에 대한 기본 통합을 테스트하는 방법을 다룹니다.

## 세션 추적이 작동하는지 확인

이 시점에서, Braze 통합에서 세션 추적이 작동해야 합니다. 이것을 테스트하려면 **개요**로 이동하여 선택한 앱 이름 드롭다운에서 애플리케이션을 선택하고 **데이터 표시**를 '오늘'로 설정합니다. 그런 다음 앱을 열고 페이지를 새로고침하세요. 주요 측정기준이 모두 1씩 증가했을 것입니다.

![][55]

응용 프로그램을 탐색하고 하나의 세션만 기록되었는지 확인하여 통합을 계속 테스트해야 합니다. 그런 다음 앱을 최소 10초 동안 백그라운드로 전환한 후 다시 포그라운드로 가져옵니다. 기본값으로, 앱이 백그라운드로 전환되거나 10초 이상 닫힌 후 포그라운드로 전환되면 새 세션이 생성됩니다. 이 작업을 완료한 후 다른 세션이 기록되었는지 확인하십시오.

## 디버깅 세션 추적
세션 추적이 예상치 못하게 작동하면, \[상세 로깅][56]을 켜고 세션 트리거링 단계를 재현하는 동안 앱을 관찰하세요. logcat에서 Braze 문을 관찰하여 활동에서 `openSession` 및 `closeSession` 호출을 기록하지 않은 위치를 감지하십시오.

[55]: {% image_buster /assets/img_archive/android_sessions.png %}
[56]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#enabling-logs