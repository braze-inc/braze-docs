---
nav_title: 출시 전후 체크리스트
article_title: 출시 전후 체크리스트
page_order: 2
description: "이 문서는 캔버스를 시작하기 전과 후에 확인해야 할 사항에 대한 지침을 제공합니다."
tool: Canvas

---

# 출시 전 및 출시 후 체크리스트

> 이 문서는 캔버스를 시작하기 전과 후에 확인해야 할 사항에 대한 지침을 제공합니다.

## 출시 전 고려 사항

캔버스를 시작하기 전에 메시징 및 전송 시간이 오디언스의 선호도와 일치하는지 확인할 수 있는 여러 세부 사항이 있습니다. 고려해야 할 사항으로는 시간대의 차이, 입장 설정 등 여러 가지가 있습니다. 이 체크리스트를 가이드로 사용하여 사용 사례에 따라 이러한 영역을 미세 조정하여 캔버스의 성공에 기여하세요. 

{% alert important %}
2023년 2월 28일부터 오리지널 캔버스 경험 환경에서는 더 이상 캔버스를 생성하거나 복제할 수 없습니다. Braze는 원래 캔버스 경험을 사용하는 고객이 캔버스 플로우로 이동할 것을 권장합니다. 향상된 편집 경험을 통해 캔버스를 더 잘 구축하고 관리할 수 있습니다. [캔버스를 캔버스 플로우에 복제하는 방법]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)에 대해 자세히 알아보세요.
{% endalert %}

### 시간대 설정 검토

사용자의 현지 시간대에 따라 예약된 항목 일정을 사용하여 사용자를 입력하는 경우, 사용자가 캔버스에 들어가기를 원하는 시간보다 적어도 24시간 전에 캔버스를 시작해야 합니다. 예를 들어, 여기에 출시와 예정된 입장 시간 사이에 충분한 시간을 남기지 않은 캔버스가 있습니다. 이 시나리오에서는 일부 사용자가 특정 시간대에서 예정된 진입 시간이 이미 지났기 때문에 캔버스에 들어오지 않을 수 있습니다. 

{% alert tip %}
버퍼를 충분히 예약하지 않은 경우 경고가 표시됩니다. 빠른 해결책은 사용자가 전체 24시간 동안 대상 세그먼트에 남아 있을 수 있도록 전송 시간을 조정하는 것입니다.
{% endalert %}

![][1]

### 정규 표현식을 사용하여 오디언스 필터를 고려하십시오

사용자가 캔버스에 들어가야 하는 예비 세부 정보를 설정한 후에는 캔버스를 구축하는 **타겟 오디언스** 단계에서 세그먼트 또는 필터를 확인하는 것이 좋습니다. 이 단계에서 **대상 집단** 요약을 검토하여 대상 오디언스가 어떻게 설정되었는지 확인할 수 있습니다. 

여기에서 오디언스 경로 단계의 세그먼트 또는 필터에 정규표현식을 사용하고 메시지 및 결정 분할 단계에서도 전달 유효성 검사 설정을 사용하는 것을 고려하세요. [정규표현식]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (또는 정규식)은 문자열로, 대문자와 같은 것들 대신 패턴을 인식하고 문자를 고려한다는 것을 의미합니다. 이는 "같음 / 같지 않음"을 사용하는 경우 단순한 구문 오류로 인해 오디언스 크기를 제한할 수 있음을 의미합니다.

타겟 오디언스가 예상보다 작다는 것을 알게 되면, "일치하는 정규식" 또는 "일치하지 않는 정규식"을 "같음" 또는 "같지 않음" 대신 사용해 보세요. 이것은 누락된 사용자를 설명하고 더 큰 오디언스를 대상으로 할 수 있습니다. 

### 항목 설정 및 경합 조건 식별

경합 조건은 **입장 일정** 및 **대상 오디언스** 설정에서 동일한 입장 기준을 사용한 경우 발생할 수 있습니다. 

실행 기반 항목을 사용하는 경우 대상 오디언스에서와 동일한 트리거 동작을 사용하지 않았는지 확인하세요. 경합 조건이 발생할 수 있으며, 사용자가 트리거 이벤트를 수행할 때 오디언스에 속하지 않으면 캔버스에 들어가지 못하게 됩니다.

{% alert tip %}
Check out the [best practices]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) for avoiding this race condition when setting up an action-based Canvas with the same trigger as the audience filter.
{% endalert %}

### 캔버스 항목 속성과 이벤트 속성을 확인하십시오

이름은 비슷하지만, [캔버스 항목 속성과 이벤트 속성정보]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)는 캔버스 워크플로 내에서 다르게 작동합니다. 캔버스 항목 속성은 항목 설정에 연결되어 있으며, 캔버스 전반의 모든 메시지 구성 요소에서 참조할 수 있습니다. 캔버스 항목 속성은 사용자가 캔버스에 진입하도록 트리거하는 이벤트 또는 API 호출의 속성으로, 동작 기반 또는 API 트리거 진입 설정을 사용합니다.

이벤트 속성정보는 반면에 작업 경로 단계에 이어지는 첫 번째 메시지 단계에서만 참조할 수 있습니다. 이벤트 속성정보는 행동 경로 단계의 평가 창 동안 사용자가 수행한 커스텀 이벤트 또는 구매 이벤트의 속성이며, 정의된 행동 경로 중 하나로 진행을 유발합니다.

메시지 미리보기를 확인하여 캔버스 항목 속성 또는 이벤트 속성정보를 참조하는 메시지 단계가 있는지 확인하세요.

### 사용자 진행을 위한 메시지 단계 검토

기본값으로, 사용자는 메시지를 받았는지 여부에 관계없이 모든 메시지 단계를 진행합니다. 특정 메시지를 받는 사용자를 진급시키려면 메시지 구성 요소 바로 뒤에 결정 분할 단계를 추가하면 됩니다. 추가 필터로 "캔버스 단계에서 받은 메시지" 필터를 추가한 다음, 캔버스 및 메시지 단계를 선택합니다.

메시지 단계의 앱 내 메시징의 경우 결정 분할 구성 요소 대신 작업 경로 구성 요소를 사용할 수 있습니다. 이것은 사용자가 인앱 메시지를 보았는지 여부에 따라 사용자를 진급시킬 수 있게 해줍니다. 필터 "단계와 상호 작용"을 추가하고 **앱 메시지에서 보기**를 선택하여 작업 그룹을 정의합니다. 그런 다음, 단계의 평가 윈도우를 인앱 메시지의 만료 윈도우로 설정합니다.

다중 채널 메시징에서 메시지 구성 요소의 경우 다음을 권장합니다.
* 메시지 및 결정 분할 단계 사이에 지연 단계를 포함하고 지연 시간을 최소 5초로 설정하세요.
* 구성 요소에 Intelligent Timing이 포함된 경우 지연 시간을 24시간으로 설정하세요
* 구성 요소에 속도 제한이 포함된 경우 메시지를 여러 단일 채널 메시지 단계로 나누고 함께 연결하십시오. 그런 다음, 사용자가 메시지 중 하나를 받았는지 확인하기 위해 마지막 메시지 단계 바로 뒤에 결정 분할 단계를 연결합니다. 이 방법을 다중 채널 메시지 단계의 대안으로 Intelligent Timing과 함께 사용할 수도 있습니다.

## 출시 후 고려 사항

캔버스를 출시했습니다! 이제 어떻게 할까요? 이 체크리스트를 사용하여 출시 후 시나리오에 따라 발생할 수 있는 불일치를 검토하고 조정하는 방법을 확인하세요.

### 항목은 많은데 전송은 적은 경우

예를 들어, 메시지 발송 수와 총 항목 수 사이에 차이가 있음을 발견했다고 가정해 봅시다. 이 주요 영역을 확인하여 캔버스를 조정할 수 있는 영역을 식별하고 발견할 수 있습니다.

#### 항목 오디언스

예약 발송 캠페인을 사용하는 경우, 대상 집단을 검토하여 오디언스를 다시 확인하세요. 채널 전반의 숫자는 어떻게 보이며, 캔버스에서 사용한 채널과는 어떻게 관련이 있습니까? 가장 낮은 숫자가 캔버스에서 사용한 채널과 일치하면 문제를 찾은 것일 수 있습니다.

#### 캔버스의 첫 번째 구성 요소

캔버스 시작 구성 요소에서 사용된 모든 오디언스 필터, 작업 트리거 또는 세그먼트를 검토하세요. 캔버스가 제대로 시작되지 않게 하는 철자 오류나 너무 엄격한 조건이 있습니까? "Equals"을(를) 사용해야 할 때 "정규식 일치"을(를) 사용하고 있습니까?

#### 캔버스 대조군 

배리언트와 대조군 간의 사용자 분포를 검토하세요. 대조군이 의도한 것보다 더 큰가요? 그렇다면 이 설정을 편집할 수 있습니다. **지능형 선택**을 켜고 대조군이 이기고 있다면 캔버스를 중지하고 새로운 접근 방식을 시도해 보세요.

### 빈 총계 오디언스

캔버스에 대한 응모 데이터가 표시되지 않는 경우, 사용자가 캔버스에 응모하지 않는 이유는 경쟁 조건 및 제한적인 오디언스 세분화 필터 때문일 수 있습니다.

액션 기반 항목을 항목 일정에 사용 중인 경우 여기에서 **타겟 오디언스**와 동일한 트리거 동작을 사용하지 않았는지 확인하세요. 경합 조건이 발생할 수 있으며, 사용자가 트리거 이벤트를 수행할 때 오디언스에 속하지 않으면 캔버스에 들어가지 못하게 됩니다.

또한 **대상 집단** 테이블을 **오디언스** 설정에서 검토하여 선택한 세그먼트에 사용자가 있는지 확인하십시오. 이 숫자가 낮으면 입력 설정을 조정하거나 선택한 세그먼트 또는 필터에 오류가 있는지 검토하세요.

### 단계 간 예상치 못한 감소

조정할 영역을 식별하는 또 다른 명백한 방법은 한 캔버스 단계에서 다음 단계로 큰 감소가 있을 때 발생할 수 있습니다. 이 경우 오디언스 필터와 예외 이벤트에 철자 오류나 대문자 오류가 없는지 확인하십시오. 그리고 항상 오디언스 필터가 너무 엄격하여 대부분의 사용자가 캔버스에 들어오지 못하게 하지 않도록 확인하세요. 

다음으로, 메시지가 사용자에게 전송되는 시기와 여부에 영향을 미칠 수 있는 이러한 설정을 식별하는 것이 중요합니다.
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- 방해금지 시간
- 전달 검증

일반적으로 캔버스에 대해 Intelligent Timing 또는 방해금지 시간 중 하나를 선택하고 둘 다 선택하지 마세요. 동일한 제안은 Intelligent Timing 또는 [사용량 제한조치]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) 중 하나만 사용하고 둘 다 사용하지 않는 것입니다. For more information on how to best use the Intelligence Suite, read our [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/).

### 경로 간의 의심스러운 전송량

두 개 이상의 경로(오디언스 경로 또는 작업 경로) 간의 전송량이 예상과 다를 때, 이는 세그먼트, 필터 또는 트리거 동작을 확인할 수 있는 기회가 될 수 있습니다. 또한, 겹치는 필터를 식별하고 제거해야 합니다.

[1]: {% image_buster /assets/img_archive/canvas_checklist1.png %}
