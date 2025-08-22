---
nav_title: 캔버스 플로우로 시작
article_title: 캔버스 플로우로 시작
page_order: 3
description: "이 참조 문서는 캔버스 플로우로 제작된 캔버스를 출시 전에 준비하고 테스트하는 방법을 다룹니다."
page_type: reference
tool: Canvas
---

# 캔버스 플로우로 시작

> 이 참조 문서는 캔버스 플로우를 사용하여 제작된 캔버스를 출시 전에 준비하고 테스트하는 방법을 다룹니다. 이것은 캔버스 진입 조건, 오디언스 요약 및 사용자 세그먼트와 같은 중요한 캔버스 체크포인트를 식별하는 것을 포함합니다.

캔버스를 시작할 준비를 할 때, Braze는 메시지 전송에 영향을 미칠 수 있는 설정을 위해 캔버스 빌더의 각 단계에서 캔버스를 확인할 것을 권장합니다. 포함:
* [경합 조건](#race-conditions)
* [전달 시간](#delivery-times)
* [사용자 세그먼트](#segment-users)

## 경합 조건 

캔버스를 시작하기 전에 발생할 수 있는 [경합 조건]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/)을 고려하세요. 

캔버스에 들어가려면 사용자는 캔버스가 예약되었는지, 동작 기반인지, API로 트리거되었는지에 관계없이 입장 일정이 발생하기 전에 입장 오디언스에 있어야 합니다. 

![An Action-Based Canvas that enters users when they make any purchase during a user's local time from April 30, 2025 at 12 pm to May 7, 2025 at 12 pm.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

캔버스가 출시된 후에 오디언스에 해당하는 사용자는 캔버스에 들어가지 않습니다.

{% alert tip %}
[입력 일정 유형]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule)을 확인하여 캔버스에 대한 예약된, 작업 기반 또는 API 트리거 전달을 사용할 시기에 대한 지침 및 세부 정보를 확인하세요!
{% endalert %}

### 입력 오디언스 필터 검토

일반적으로, 동일한 트리거를 오디언스 필터로 사용하는 동작 기반 또는 API 트리거 캔버스 구성을 피하세요. 예를 들어, 캔버스가 시작된 후 특정 작업을 수행하는 사용자는 진입 오디언스에 포함되므로 이벤트를 오디언스 필터로 추가할 필요가 없습니다. 

자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)에서 사용할 수 있는 세분화 필터를 참조하여 오디언스를 타겟팅하십시오.

### 여러 API 요청 일괄 처리

요청을 여러 번 호출하는 대신 동일한 API 호출에서 요청하여 고객 프로필이 먼저 생성되거나 업데이트되었는지 확인하십시오. [여러 엔드포인트 사용]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints)을 참조하세요.

### 지연 추가

경합 조건을 피하는 또 다른 방법은 캔버스의 첫 번째 단계로 지연 단계를 사용하는 것입니다(이상적으로는 5분 설정). 

이것은 속성, 이메일 주소 및 푸시 토큰이 새 고객 프로필로 처리된 후 다음 캔버스 단계의 대상으로 지정되기 전에 시간을 허용합니다. 이 지연 단계가 없으면 이메일이 아직 업데이트되지 않은 사용자에게 이메일이 전송될 수 있습니다.

## 전달 시간

캔버스 전송 시간을 실시간으로 설정하면 참여도와 전환율을 높일 수 있습니다. 캔버스에 설정한 전달 시간을 주목하세요. 참여도와 전환율을 높이려면 캔버스를 예약된 반복 방식이 아닌 실시간으로 트리거하는 것이 가장 좋습니다.

캔버스에 대한 예약된 전달을 선택한 경우, Braze는 캔버스가 시작되기 최소 24시간 전에 예약하여 캔버스에 대한 조정을 할 수 있도록 권장합니다.

## 사용자 세그먼트

구성 요소로 캔버스 플로우 사용자 여정을 과도하게 포화시키기 전에 사용자 여정을 어떻게 단순하게 유지할 수 있을지 고려해 보세요. 캔버스 편집기에서 단순화된 보기를 사용하여 사용자 여정이 어떻게 분기되는지 더 잘 파악할 수 있습니다. 

간단하고 효과적인 방식으로 사용자를 세그먼트할 수 있는 네 가지 주요 구성 요소가 있습니다:

* [오디언스 경로](#audience-paths)
* [결정 분할](#decision-split)
* [행동 경로](#action-paths)
* [실험 경로](#experiment-paths)

### 오디언스 경로

캔버스 내에서 고객 프로필의 커스텀 속성, 커스텀 이벤트 및 이전 메시지 인게이지먼트 데이터에 따라 사용자를 세그먼트하기 위해 [오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) 단계를 사용하세요.

### 결정 분할

[결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) 단계에서는 사용자가 양극성 질문에 대한 답변을 기반으로 다른 사용자 여정 경로로 이동할 수 있습니다.

### 행동 경로

[행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)는 커스텀 이벤트, 구매 이벤트 및 커스텀 속성 변경과 같은 실시간 행동을 기반으로 사용자를 세분화하는 데 중점을 둡니다. 

### 실험 경로

Similar to Action Paths, you can leverage [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) steps in your Canvas to test multiple Canvas paths against each other, along with a control group. 이것은 경로 성능을 추적하여 캔버스 여정을 구축할 때 정보에 입각한 결정을 내릴 수 있도록 합니다. 

## 출시 전에 테스트

세부 사항을 검토한 후, 테스트 사용자와 함께 캔버스를 테스트할 수 있는 다양한 방법을 확인하려면 [테스트 캔버스 보내기]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/)를 확인하세요.

## 문제 해결

{% details 왜 내 사용자들이 내 캔버스 메시지를 받지 못하나요? %}
**사용자 가용성 확인**
- 세분화 기준을 충족하는지 확인하세요.
- 푸시 구독 상태가 '구독' 또는 '옵트인' **이고** **푸시 사용** 상태가 'true'로 설정되어 있는지 확인합니다. 이것들을 캔버스 항목 규칙으로 추가한 경우 사용자가 캔버스에 들어가 메시지 단계를 받는 사이에 구독 취소되었을 수 있습니다.
- 캔버스 전송 설정과 일치하는지 확인합니다. (사용자가 '구독 중'이지만 설정이 '옵트인'인 경우 사용자가 채널에 대해 활성화되지 않습니다.)
- 캔버스에 대해 글로벌 빈도 제한이 활성화된 경우, 규칙에서 각 사용자가 특정 채널에서 메시지를 받을 수 있는 횟수를 제한하고 있는지 확인하세요. 
- 조용한 시간을 사용하도록 설정하면 메시지 전송 시간이 영향을 받아 다음 사용 가능한 시간(조용한 시간이 종료되는 시간)에 메시지가 전송되거나 완전히 취소될 수 있습니다.

**캔버스 단계에서 추가 필터에 대한 사용자 가용성 확인**
- 필수 사용자 지정 이벤트 또는 구매를 수행했는지 확인합니다.
- 여러 작업을 동시에 트리거할 경우 사용자가 받는 메시지에 영향을 주는 [경쟁 조건이]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) 있는지 확인합니다.
- 단계에 사용자가 메시지를 받지 못하도록 차단할 수 있는 특정 필터가 없는지 확인하세요.
- 동일한 캔버스 내에서 서로 다른 단계 간의 충돌을 검색합니다. 예를 들어, 메시지를 받지 못한 사용자는 다른 브랜치에서 다른 단계를 완료해야 하는 필터에 의해 중지될 수 있습니다.
- 사용자가 추가 유효성 검사 규칙을 충족하는지 확인합니다.
- 전송할 때 캔버스 단계가 이전 단계에 연결되었는지 확인합니다.
{% enddetails %}

