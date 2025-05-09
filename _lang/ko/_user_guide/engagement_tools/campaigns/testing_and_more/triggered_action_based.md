---
nav_title: API 트리거 및 액션 기반 캠페인
article_title: API 트리거 및 액션 기반 캠페인 테스트하기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 API 트리거 및 실행 기반 캠페인을 테스트하는 방법에 대해 설명합니다."

---

# API 트리거 및 액션 기반 캠페인

> 캠페인을 설정할 때는 항상 시작하기 전에 메시지를 테스트하는 것이 좋습니다. 이 참조 문서에서는 API 요청, 페이로드를 검사하고 전달 가능성 로그를 볼 수 있는 테스트 사용자 세그먼트를 만드는 방법에 대해 설명합니다.

## 1단계: 테스트 사용자 세그먼트 만들기

API 또는 사용자 지정 이벤트로 캠페인의 트리거를 테스트하는 유일한 방법은 캠페인을 실시간으로 푸시하는 것입니다. 새 캠페인을 출시할 때 전달 가능성 트리거를 테스트할 때 캠페인에 테스트 사용자 세그먼트를 추가하는 것을 적극 권장합니다. 이렇게 하면 캠페인이 실수로 전송되더라도 내부 사용자에게만 전달되도록 안전망을 구축할 수 있습니다.

1. **테스트 사용자 가져오기**<br>테스트 사용자는 CSV 또는 [Postman]({{site.baseurl}}/api/postman_collection/)을 통한 일회성 일괄 요청을 통해 Braze로 가져올 수 있습니다. 이러한 사용자를 가져올 때는 프로필에 테스트 그룹 세그먼트를 구축하는 데 사용할 수 있는 사용자 지정 속성(예: `internal_test_user: true`)을 설정하는 것이 좋습니다. <br><br>
2. **테스트 사용자를 Braze가 인식하는 테스트 사용자로 추가하기**<br>[Marking your test users as Braze-recognized test users]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) in the dashboard gives you access to verbose logging for each user, allowing you to inspect API requests, their payloads, and view deliverability logs. 이러한 로그를 통해 최종 사용자에게 캠페인을 전달하는 데 문제가 있었는지 확인할 수 있습니다. <br><br>
3. **세그먼트 만들기**<br>테스트 사용자 세그먼트를 만들려면 `internal_test_user` 사용자 지정 속성을 `true` 으로 설정하여 사용자 세그먼트를 만듭니다. 이 세그먼트는 캠페인이 시작되면 제거할 수 있습니다. 

## 2단계: 테스트 전송

다음으로, Braze 대시보드에서 테스트 전송을 하거나 Inbox Vision(이메일 전용)을 사용하여 캠페인이 아직 초안 모드에 있는 동안 레이아웃이 어떻게 보이는지 확인할 수 있습니다. 그런 다음 테스트 사용자 세그먼트에 캠페인을 전송하여 예상대로 작동하는지 확인할 수 있습니다. 캠페인이 API 트리거형인지 액션 기반인지에 관계없이, Postman을 사용하여 일회성 요청을 Braze API에 전송하여 캠페인을 트리거할 수 있습니다. 

## 3단계: Braze 로깅을 사용하여 인바운드 결과 검사하기

Braze 로깅을 사용하여 트리거, 전송 및 이벤트 문제를 해결하세요. 
- The [event user log]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) will show you the raw payload of the API-trigger request, the custom event triggering the campaign, and any associated trigger or event properties.
- The [message activity log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) will log any errors and help you understand why a particular message may not have been delivered.

## 4단계: 테스트 세그먼트를 제거하고 캠페인을 롤아웃합니다.

클릭된 모든 링크가 등록된 상태에서 메시지가 트리거되고 제대로 렌더링되면 세그먼트를 제거하고 캠페인을 업데이트할 수 있습니다. 소수의 테스트 사용자 노출이 포함되지 않도록 캠페인을 처음부터 시작하려면 캠페인을 복제하고 테스트 사용자 세그먼트 없이 캠페인을 다시 시작할 수 있습니다. 
