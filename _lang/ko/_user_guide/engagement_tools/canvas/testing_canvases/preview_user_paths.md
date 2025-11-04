---
nav_title: 사용자 경로 미리보기
article_title: 사용자 경로 미리보기
page_order: 0.3
alias: /preview_user_paths/
description: "이 페이지에서는 캔버스에서 사용자 경로를 미리 보는 방법에 대해 설명합니다."
Tool:
  - Canvas
---

# 캔버스에서 사용자 경로 미리보기

> 사용자를 위해 만든 캔버스 여정을 경험하세요. 여기에는 수신할 타이밍과 메시지를 미리 보는 것도 포함됩니다. 이러한 테스트 실행은 캔버스를 보내기 전에 메시지가 올바른 오디언스에게 전송되는지 확인하는 품질 보증 역할을 합니다.

## Creating a test run

사용자 여정을 미리 보려면 다음 단계를 따르세요:

1. 캔버스 빌더로 이동합니다. 저장하지 않은 변경 사항을 저장하고 오류를 해결합니다.
2. 바닥글에서 **테스트 캔버스**를 선택합니다.
3. 테스트 사용자를 선택합니다.
4. (Optional) Select a recipient for the test.
5. **테스트 실행**을 선택합니다.

캔버스 편집 권한이 없는 경우에도 미리 보기를 실행할 수 있지만, 이 미리 보기는 저장되지 않은 변경 사항이 있는 경우 실행됩니다.

### 지원되는 단계

다음 단계가 지원됩니다:
- 메시지 
- 오디언스 경로
- 결정 분할
- 지연
- 작업 경로
- 실험 경로
- 사용자 업데이트(UI 편집기에서만 가능, JSON 편집기를 사용하는 단계는 건너뛰기)

테스트가 위에 나열되지 않은 단계 유형과 겹치는 경우 지원되지 않는 단계는 건너뛰고 테스트 사용자는 지원되는 다음 단계로 계속 진행합니다.

### 캔버스 단계 세부 정보

참가 기준에 대한 자세한 내용을 보려면 **자세히 보기를 선택하세요**. 세분화가 있는 단계에는 충족 또는 미충족 기준이 표시됩니다. 메시지에는 배달 유효성 검사 및 채널 적격성에도 이 정보가 표시됩니다. 메시지 단계에는 전송된 채널과 전송되지 않은 채널이 표시됩니다.

### Liquid

실제 테스트 메시지를 보내지 않더라도 테스트 실행 중에 Liquid 로직이 처리됩니다. 즉, [중단 메시지 로직]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages)과 기타 Liquid 로직이 반영되어 캔버스 사용자 여정에 영향을 미칠 수 있습니다.

미리보기가 사용자 여정의 마지막 단계를 중단하는 대신 전송하는 경우, 미리보기는 캔버스 입력 시간을 기준으로 사용자가 실제 단계에 있는 시간이 아닌 현재 시간을 Liquid 평가를 위해 테스트 중인 시간으로 사용할 수 있습니다.

## 타이밍을 위한 미리보기

예약된 캔버스의 경우, 테스트 사용자는 다음 예약된 입장 시간에 입장하게 됩니다. 시작 날짜가 있는 작업 기반 캔버스의 경우 테스트 사용자가 시작 날짜와 시간을 입력합니다. 

기본 시작 시간은 여전히 적용되지만, 모든 경우에 입장 시간을 구성할 수 있으므로 과거 또는 미래의 날짜를 시뮬레이션할 수 있습니다. 그러나 캔버스 시작일 이전이나 종료일 이후에는 테스트할 수 없습니다.

메시지 및 지연 단계는 사용자가 지연을 재구성할 필요 없이 메시지를 진행하거나 수신할 수 있는 시간을 표시합니다. 단계에 Intelligent Timing 사용 여부가 표시되지만 이 사용자 경로 미리보기는 테스트 사용자에 대한 예상치를 계산하지 않는다는 점에 유의하세요.

## 사용자가 들어오고 나갈 때

Test users will enter the preview even if they aren't eligible in real life. If they aren't eligible, you can see why they haven't met the criteria. When a test user enters the preview, we assume the test user has met the target audience criteria and performed the action trigger criteria. For example, for a Canvas that uses custom events in the entry criteria, the test user is assumed to have performed the custom event as expected in the entry criteria. However, if the same custom event is used elsewhere in the Canvas (like in the exit criteria), consider how this might impact your user path.

이벤트, API 트리거, 사용자 지정 속성 및 캔버스 항목 속성은 캔버스 항목에 따라 적용됩니다. 테스트 실행은 이러한 요소를 적용하지 않고 사용자 여정을 시뮬레이션하여 실제 사용자 프로필이나 캔버스의 흐름을 변경합니다. 예를 들어, 테스트 중에 사용자 지정 속성을 캔버스 트리거로 사용하면 사용자 지정 속성 변경을 트리거한 **것처럼** 트리거 기준이 사용자의 미리 보기에 적용됩니다.

### Consideration

If you test an Action Path with actions that correspond to exit criteria (including event properties), the exit criteria will be triggered and the test run will end. If you test a Message step that corresponds to exit criteria, the exit criteria will be triggered and the test run will end. 

현재로서는 행동 경로 내에서 특정 이벤트나 속성을 선택하여 종료 기준을 트리거할 수 없습니다(경로 전체만 트리거할 수 있습니다). 사용자가 잠재적으로 여러 종료 기준을 충족할 수 있는 경우, 가장 먼저 처리되어 충족하는 기준이 결과로 표시됩니다.

## 실험 경로 및 캔버스 변형

- 최상위 이형 상품이 있는 캔버스의 경우 테스트를 시작할 때 이형 상품을 선택합니다.
- 실험 경로의 경우 테스트 사용자가 단계를 접했을 때 사용자가 진행하는 배리언트를 선택합니다.
- 개인화된 경로 또는 위닝 배리언트를 사용하는 실험 경로의 경우, 테스트 사용자가 메시지 단계에서 대기하는 지연 시간이 있지만, Braze는 사용자가 선택한 배리언트를 즉시 진행했다고 가정하므로 이 지연 시간은 고려되지 않습니다.

## 테스트 전송

테스트 실행이 채워질 때 내부 테스트 그룹 또는 개별 사용자에게 테스트 메시지를 보내도록 선택할 수 있습니다. 즉, 테스트 경로를 따라 사용자가 마주치는 메시지만 전송됩니다. 수신자는 기본적으로 해당 속성이 포함된 메시지를 받게 되지만 테스트 사용자의 속성으로 이를 재정의할 수 있습니다.

경로에 관계없이 경로를 미리 보지 않고 캔버스에 있는 모든 테스트 메시지를 한 번에 보내려면 **테스트 보내기** 탭에서 **모든 테스트 메시지 보내기를** 선택하면 됩니다.

## 응답형

캔버스 단계는 사용자 경로를 미리 볼 때 타이밍에 반응합니다. 사용자 업데이트 단계를 통해 수행한 업데이트는 흐름의 후속 단계에 반영되지만 실제 사용자 프로필에는 적용되지 않습니다. 사용자가 배리언트를 입력한 효과는 미리보기의 향후 단계에 반영됩니다.

마찬가지로 필터는 테스트 사용자가 캔버스의 다른 단계와 상호 작용한 결과로 발생한 작업을 인식합니다. 예를 들어, 이 미리보기 모드는 사용자가 캔버스에서 이전에 "전송"된 메시지 단계를 만났음을 인식하고 테스트 사용자가 행동 경로를 진행하기 위해 "행동"을 취한 것으로 인식합니다.

응답형 행동에 대한 자세한 내용은 [종료 기준]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)을 참조하세요.

## 연결된 콘텐츠

연결된 콘텐츠가 캔버스에 포함되어 있으면 실행됩니다. 즉, 커넥티드 콘텐츠 호출이 있는 캔버스 또는 커넥티드 콘텐츠가 포함된 콘텐츠 블록을 테스트하는 경우 캔버스가 커넥티드 콘텐츠 호출을 전송하여 다른 캠페인이나 캔버스에서 참조된 데이터를 수정할 수 있습니다.

사용자 경로를 미리 볼 때 다른 캔버스 또는 캠페인에서 참조된 사용자 프로필이나 데이터를 변경하는 연결된 콘텐츠를 제거하는 것을 고려하세요.

## 웹훅

웹훅은 테스트 메시지가 전송될 때 실행되지만 테스트 실행 중에는 실행되지 않습니다. 커넥티드 콘텐츠와 마찬가지로, 다른 캔버스나 캠페인에서 참조된 사용자 프로필이나 데이터를 변경하는 웹훅을 제거하는 것이 좋습니다.

## 사용 사례

이 시나리오에서 캔버스는 앱에서 세션이 없는 사용자를 타겟팅하도록 설정되어 있습니다. 이 여정에는 환영 이메일이 포함된 메시지 단계, 하루 동안 설정된 지연 단계, 세션이 하나 이상 있는 사용자와 그 외의 모든 사용자로 분할되는 오디언스 경로 단계가 포함됩니다. 사용자가 어느 오디언스 경로에 속해 있는지에 따라 후속 메시지 단계가 전송됩니다.

![An example of a Canvas with a Message step, Delay step, Audience Paths step, and two Message steps.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

테스트 사용자는 캔버스 진입 기준을 충족하므로 캔버스에 들어가서 사용자 여정을 진행할 수 있습니다. 그러나 테스트 사용자가 지난 달력 날짜에 앱을 열지 않았기 때문에 "다른 모든 사용자" 경로로 계속 이동하여 다음과 같은 푸시 알림을 받게 됩니다. "마지막 기회! 첫 번째 과제를 완료하면 특별 보너스를 받을 수 있습니다."

![The "Test Results" section that shows the test user has met the entry criteria and provides a summary of their journey, including which steps they were sent.]({% image_buster /assets/img/preview_user_path_results_example.png %})

