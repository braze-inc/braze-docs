---
nav_title: 개요
article_title: Roku용 인앱 메시지 개요
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "이 문서에서는 모범 사례 및 사용 사례를 포함하여 Roku 인앱 메시징에 대한 개요를 다룹니다."

---

# 인앱 메시지 개요

> [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)는 푸시 알림을 통해 일과를 방해하지 않고 사용자에게 콘텐츠를 전달할 수 있도록 도와줍니다. 사용자 지정 및 맞춤 조정된 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다. 다양한 레이아웃과 사용자 지정 도구를 선택할 수 있는 인앱 메시지는 그 어느 때보다 사용자의 참여를 유도할 수 있습니다.

인앱 메시지의 예제를 보려면 [사례 연구](https://www.braze.com/customers)를 참조하세요.

![사용자가 빌드할 수 있는 잠재적인 세 가지 Roku 인앱 메시지 이미지. 이러한 예로는 '전체 화면 가져오기', '홈페이지 배너', '코너 알림' 등이 있습니다.]({% image_buster /assets/img/roku/Docs-Imagery.png %})

## 인앱 메시지 유형

인앱 메시지 플랫폼으로 **Roku 기기**를 선택하여 Roku용 인앱 메시지를 생성합니다.

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})

## 기술 문서

인앱 메시지 표시와 노출 수 및 클릭 분석 로깅에 대한 지침은 [통합 가이드]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration) )를 참조하세요.

![사용자 지정 배너를 만드는 데 필요한 다양한 구성 요소를 보여주는 '홈페이지 배너' 예시입니다. 나열된 구성 요소에는 메시지 구성 구성 요소(본문, 버튼 텍스트, 이미지, 할당된 버튼 동작(딥링크) 및 키-값 쌍 표시), 백엔드 세부 정보(대상은 '시즌 1을 시청한 사용자'로 표시), 의도된 상호작용(버튼이 앱으로 딥링크, 메시지를 닫으면 메시지 해제, 10초 후 자동 해제), 트리거(세션 시작) 및 키-값 쌍(템플릿 = homepage_banner)(]({% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %})) 등이 있습니다.

## 테스트 및 QA

Roku 인앱 메시지에는 테스트 보내기 기능이 지원되지 않습니다. 메시지를 테스트하려면 사용자 ID로만 필터링된 캠페인을 실행합니다.

