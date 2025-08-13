---
nav_title: 준비 가이드
article_title: 인앱 메시지 준비 가이드
page_order: 0.5

page_type: reference
description: "이 문서에서는 인앱 메시지를 작성하기 전에 고려해야 할 몇 가지 질문과 모범 사례에 대해 설명합니다."
channel: in-app messages

---

# 인앱 메시지 준비 가이드

> 인앱 메시지를 작성하기 전에 다음 몇 가지 주제를 고려해야 빠르고 쉽게 메시지를 작성할 수 있습니다.

## 일반적인 고려 사항

- 캠페인을 구축하는 경우 이 메시지의 변형을 몇 개 표시하시겠습니까? 배리언트 테스트 아이디어는 [다양한 채널에 대한 팁]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels)을 확인하세요.
- 캔버스를 구축하는 경우 해당 단계에서 이 메시지가 다른 메시징 채널과 페어링되나요?
- [메시지가 언제 만료되기를]({{site.baseurl}}/canvas_in-app_messages/) 원하시나요?

## 타겟팅 고려 사항

- 인앱 메시지는 앱을 정기적으로 방문하는 사용자에게 가장 적합합니다. 이 오디언스도 포함되나요?
- 사용자가 메시지를 어디에 표시하기를 원하나요? 웹 앱? 모바일 앱?
- 어떤 이벤트가 이 메시지를 트리거해야 하나요?
- 이전 버전의 앱을 사용하는 사용자가 있나요? 그렇다면 메시지의 일부 요소를 보지 못할 수도 있습니다.
- 이 메시지를 작성하는 기기 유형은 무엇인가요? **미리보기** 상자 또는 **테스트** 탭을 사용하여 메시지를 미리 볼 수 있다는 점을 기억하세요. 자세한 내용은 [테스트]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)를 참조하세요.

## 콘텐츠 고려 사항

- 이 메시지에서 어떤 언어를 사용하시나요?
- 헤더와 본문 카피는 무엇인가요? 사용자의 눈길을 사로잡고 관련성이 있나요?
- 인앱 메시지는 설정된 시간 동안만 표시됩니다. 간결하고 기억에 남는 카피인가요?
- 커스텀 사본을 추가하기 위해 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)를 사용하시나요?
- 전체 화면 인앱 메시지의 경우 이미지 또는 기타 미디어가 [안전 영역]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone) 내에 있나요?
- 설문조사 인앱 메시지의 경우 속성 또는 제출을 기록하시겠습니까? 확인 페이지를 설정하셨나요?

## 전환 고려 사항

- 이 메시지의 목표는 무엇인가요? 이를 메시지에서 어떻게 표현할 수 있을까요?
- 버튼이 사용자에게 적합한 옵션을 제공하나요? [주요 클릭 유도 문안은]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons) 무엇인가요?
- [다른 인앱 콘텐츠로 딥링킹하고]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) 있나요? 이 인앱 메시지를 사용하여 [권한 또는 푸시 프라이밍 요청]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)을 보내고 수락하고 있나요?
- 메시지 종료 옵션이 있나요? 그렇지 않은 경우 언제든지 이 스니펫을 복사하여 붙여넣어 빠른 버튼을 만들 수 있습니다:
    ```html
    <a href="appboy://close">X</a>
    ```


