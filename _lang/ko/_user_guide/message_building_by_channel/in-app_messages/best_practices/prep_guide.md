---
nav_title: 준비 가이드
article_title: 앱 내 메시지 준비 가이드
page_order: 0.5

page_type: reference
description: "이 문서에서는 앱 내 메시지를 작성하기 전에 고려해야 할 몇 가지 질문과 모범 사례를 다룹니다."
channel: in-app messages

---

# 앱 내 메시지 준비 가이드

> 앱 내 메시지를 작성하기 전에 다음 주제 중 몇 가지를 고려해야 메시지를 빠르고 쉽게 작성할 수 있습니다.

## 일반 고려 사항

- 캠페인을 구축하고 있다면 이 메시지의 몇 가지 변형을 표시하고 싶으신가요? 변형 테스트 아이디어는 [다양한 채널에 대한 팁]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels)를 확인하세요.
- 캔버스를 구축하고 있다면 이 메시지가 해당 단계의 다른 메시징 채널과 함께 사용될 것인가요?
- 언제 [귀하의 메시지가 만료되기를 원하십니까?]({{site.baseurl}}/canvas_in-app_messages/)

## 타겟팅 고려 사항

- 앱 내 메시지는 귀하의 앱을 정기적으로 방문하는 사용자에게 가장 적합합니다. 이 대상을 포함하고 있습니까?
- 사용자가 메시지를 어디에서 보기를 원하십니까? 웹 앱에서요? 모바일 앱에서요?
- 어떤 이벤트가 이 메시지를 트리거해야 합니까?
- 사용자 중 일부가 이전 버전의 앱을 사용하고 있습니까? 그렇다면, 그들은 메시지의 일부 요소를 볼 수 없을 수도 있습니다.
- 이 메시지를 위해 어떤 유형의 장치 또는 장치들을 구축하고 있습니까? 메시지를 **미리보기** 상자 또는 **테스트** 탭을 사용하여 미리 볼 수 있습니다. 자세한 내용은 [테스트]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)를 참조하십시오.

## 콘텐츠 고려사항

- 이 메시지에서 어떤 언어를 사용할 것인가요?
- 헤더와 본문 복사는 무엇인가요? 사용자에게 눈에 띄고 관련성이 있나요?
- 앱 내 메시지는 정해진 시간 동안만 표시됩니다. 복사가 간결하고 기억에 남나요?
- 사용자 정의 복사를 추가하기 위해 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)을 사용할 것인가요?
- 전체 화면 앱 내 메시지의 경우, 이미지나 기타 미디어가 [안전 영역]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone) 내에 있나요?
- 설문 조사 앱 내 메시지의 경우, 속성이나 제출을 기록하시겠습니까? 확인 페이지를 설정하셨나요?

## 전환 고려사항

- 이 메시지의 목표는 무엇인가요? 그것을 메시지에서 어떻게 표현할 수 있나요?
- 버튼이 사용자에게 의미 있는 옵션을 제공하나요? 당신의 [주요 행동 유도]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)는 무엇인가요?
- 다른 앱 내 콘텐츠에 [딥 링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)를 하고 있나요? 이 앱 내 메시지를 사용하여 [권한 또는 푸시 프라이밍 요청]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)을 보내고 수락하고 있나요?
- 메시지 종료 옵션이 있나요? 그렇지 않으면, 이 코드를 복사하여 붙여넣어 빠른 버튼을 만들 수 있습니다:
    ```html
    <a href="appboy://close">X</a>
    ```


