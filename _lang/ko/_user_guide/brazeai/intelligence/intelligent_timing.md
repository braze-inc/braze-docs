---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 2
description: "이 문서에서는 Intelligent Timing(이전의 지능형 전달)에 대한 개요와 캠페인 및 캔버스에서 이 기능을 활용하는 방법을 설명합니다."

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Intelligent Timing을 사용하여 Braze가 최적의 전송 시간이라고 하는 사용자가 참여(열람 또는 클릭)할 가능성이 가장 높다고 판단되는 시간에 각 사용자에게 메시지를 전달합니다. 이렇게 하면 사용자가 원하는 시간에 메시지를 보내고 있는지 쉽게 확인할 수 있어 인게이지먼트를 높일 수 있습니다.

## 사용 사례

- 시간에 민감하지 않은 반복 캠페인 보내기
- 여러 시간대의 사용자를 대상으로 캠페인 자동화하기
- 인게이지먼트가 가장 높은 사용자에게 메시지를 보낼 때(인게이지먼트 데이터가 가장 많은 사용자)

## 작동 방식

Braze는 사용자의 과거 앱과의 상호작용 및 각 메시징 채널과의 상호작용에 대한 통계 분석을 기반으로 최적의 전송 시간을 계산합니다. The following interaction data is used: 

- Session times
- Push Direct Opens
- Push Influenced Opens
- Email Clicks
- Email Opens (excluding [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens))

예를 들어, 샘은 아침에 정기적으로 이메일을 열람하지만 저녁에는 앱을 열고 알림과 상호 작용할 수 있습니다. 즉, 샘은 아침에 Intelligent Timing이 적용된 이메일 캠페인을 수신하고, 인게이지먼트 가능성이 높은 저녁에는 푸시 알림이 포함된 캠페인을 수신하게 됩니다.

Braze가 최적의 전송 시간을 계산할 수 있는 인게이지먼트 데이터가 충분하지 않은 경우, 대체 [시간](#fallback-time)을 지정할 수 있습니다.

## Intelligent Timing 사용

이 섹션에서는 캠페인 및 캔버스에 대한 Intelligent Timing을 구성하는 방법에 대해 설명합니다.

### 캠페인

캠페인에서 Intelligent Timing을 사용하는 방법:

1. 캠페인을 만들고 메시지를 작성합니다.
2. 전달 유형으로 **예약 전달**을 선택합니다.
3. **시간 기반 예약 옵션에서** **Intelligent Timing**을 선택합니다.
4. 전송 날짜를 선택합니다. 고려해야 할 사항은 [캠페인 뉘앙스](#campaign-nuances)를 참조하세요.
5. [특정 시간 내에만 메시지를 보낼지](#sending-within-specific-hours) 여부를 결정합니다.
6. [대체 시간](#fallback-time)을 지정합니다. 고객 프로필에 최적의 시간을 계산할 수 있는 데이터가 충분하지 않은 경우 메시지가 전송됩니다.

![Intelligent Timing으로 캠페인 예약하기][1]

#### 특정 시간 내에 메시지 보내기 {#sending-within-specific-hours}

원하는 경우 최적의 시간을 특정 기간 이내로 제한하도록 선택할 수 있습니다. 캠페인이 특정 이벤트, 세일 또는 프로모션과 관련된 경우 유용하지만 일반적으로 그 외의 경우에는 권장하지 않습니다. 특정 시간 내에 보내는 기능은 방해금지 시간과 유사하게 작동하며, Intelligent Timing에서는 비생산적이므로 권장하지 않습니다. 자세한 내용은 이 도움말의 [제한 사항](#limitations) 섹션을 참조하세요.

1. Intelligent Timing을 구성할 때 **특정 시간 내에만 메시지를 보내기**를 선택합니다.
2. 전달 기간의 시작 및 종료 시간을 입력합니다.

!["특정 시간 내에만 메시지 보내기" 확인란을 선택하면 시간 창이 사용자 현지 시간으로 오전 8시에서 오전 12시 사이로 설정됩니다.][4]

전달 기간이 지정되면 Braze는 해당 기간 내의 인게이지먼트 데이터만 확인하여 사용자에게 가장 적합한 시간을 결정합니다. 해당 기간 내에 인게이지먼트 데이터가 충분하지 않으면 지정된 [대체 시간](#fallback-time)에 메시지가 전송됩니다.

#### 전달 시간 미리보기

하루 중 시간대별로 얼마나 많은 사용자가 메시지를 받을지 예상하려면 미리 보기 차트(캠페인만 해당)를 사용하세요.

1. 타겟 오디언스 단계에서 세그먼트 또는 필터를 추가합니다.
2. 대상 **전달 시간 미리보기** 섹션(타겟 오디언스 및 전달 예약 단계 모두에 표시됨)에서 채널을 선택합니다.
3. **데이터 새로 고침**을 클릭합니다.

![][2]

Intelligent Timing 또는 캠페인 오디언스에 대한 설정을 변경할 때마다 데이터를 다시 새로고침하여 업데이트된 차트를 확인합니다.

차트에는 최적의 시간을 계산하기에 충분한 데이터가 있는 사용자는 파란색으로, 대체 시간을 사용할 사용자는 빨간색으로 표시되어 있습니다. 계산 필터를 사용하여 미리 보기 보기를 조정하여 두 사용자 그룹을 더 세밀하게 살펴볼 수 있습니다.

#### 캠페인 뉘앙스

다음은 Intelligent Timing으로 캠페인을 예약할 때 주의해야 할 몇 가지 뉘앙스입니다.

##### 캠페인 시작하기

예정된 전송 날짜 최소 48시간 전에 캠페인을 시작하세요. 이는 시간대가 다르기 때문입니다. Braze는 세계에서 이른 표준 시간대 중 하나인 사모아 시간(UTC+13)의 자정을 기준으로 최적의 시간을 계산합니다. 하루는 전 세계적으로 약 48시간에 걸쳐 있으므로 이 48시간 버퍼 내에 캠페인을 시작하면 사용자의 시간대에서 최적의 시간이 이미 지나서 메시지가 전송되지 않을 수 있습니다.

{% alert important %}
캠페인이 시작되고 사용자의 최적 도달 시간이 과거 1시간 미만인 경우 메시지가 즉시 발송됩니다. 최적의 시간이 1시간 이상 지나면 메시지가 전혀 전송되지 않습니다.
{% endalert %}

##### 세그먼트 선택

특정 기간 동안 액션을 수행한 오디언스를 타겟팅하는 경우 세그먼트 필터에 최소 3일의 기간을 허용하세요. 예를 들어 `First used these apps more than 1 day ago` 및 `First used these apps less than 3 days ago` 대신 1일 및 4일을 사용합니다.

![캠페인이 1~4일 전에 해당 앱을 처음 사용한 사용자를 타겟팅하는 타겟 오디언스에 대한 필터입니다.][3]

이는 시간대 때문이기도 합니다. 3일 미만의 기간을 선택하면 일부 사용자가 최적의 전송 시간에 도달하기 전에 세그먼트에서 제외될 수 있습니다.

[Braze가 세그먼트 및 필터에 대한 자격 기준을 확인하는 시기]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters)에 대해 자세히 알아보세요.

##### 최적화를 통한 A/B 테스트

If you are leveraging [A/B testing with an optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), such as automatically sending the Winning Variant after the A/B test is over, the duration of the campaign will increase. 기본적으로 Intelligent Timing 캠페인은 초기 테스트 다음 날에 나머지 사용자에게 당첨 배리언트를 보내지만, 이 전송 날짜를 변경할 수 있습니다.

Intelligent Timing과 A/B 테스트를 모두 사용하는 경우, 위닝 배리언트를 초기 테스트 1일이 아닌 2일 후에 전송하도록 예약하는 것이 좋습니다.

![타겟 대상 단계의 A/B 테스트 섹션에서 테스트가 종료되고 초기 테스트가 시작된 후 이틀 후에 위닝 배리언트를 보냅니다.][5]

### 캔버스

이 섹션에서는 캔버스에서 Intelligent Timing을 사용하는 방법을 설명합니다. 단계는 사용 중인 캔버스 워크플로에 따라 약간씩 다릅니다.

{% alert important %}
2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 섹션은 원래 편집기에서 Intelligent Timing이 어떻게 작동하는지 이해하기 위해 참조할 수 있습니다.<br><br>Braze는 기존 캔버스 환경을 사용하는 고객은 캔버스 플로우로 전환할 것을 권장합니다. 향상된 편집 경험을 통해 캔버스를 더 잘 구축하고 관리할 수 있습니다. [캔버스를 캔버스 플로우에 복제하는 방법]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)에 대해 자세히 알아보세요.
{% endalert %}

{% tabs %}
{% tab 캔버스 흐름 %}

캔버스 흐름에서 Intelligent Timing은 메시지 단계에서 설정됩니다. 캔버스에서 Intelligent Timing을 사용하는 방법:

1. 캔버스에 [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)를 추가합니다.
2. **전달 설정**으로 이동합니다.
3. **Intelligent Timing 사용**을 선택합니다.
4. [대체 시간](#fallback-time)을 지정합니다.

이 단계를 입력한 사용자는 해당 시간이 아직 지나지 않은 경우 입력한 날의 최적 시간에 메시지를 받게 됩니다. 사용자가 메시지 단계를 입력한 당일에 최적의 시간(현지 시간 기준)이 지난 경우에는 다음 날 최적 시간에 전송됩니다. 여러 채널을 대상으로 하는 메시지 단계는 채널별로 서로 다른 시간에 메시지를 보내거나 보내려고 시도할 수 있습니다. 메시지 단계의 첫 번째 메시지가 전송을 시도하면 모든 사용자가 자동으로 고급 단계로 이동합니다.

#### 지연 단계 및 Intelligent Timing

[지연 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 후 Intelligent Timing을 사용하는 경우 지연을 계산하는 방법에 따라 전달 날짜가 달라질 수 있습니다. 이는 지연이 **기간 후**로 설정된 경우에만 적용되며, "일"과 "달력 일수"가 계산되는 방식에 차이가 있기 때문입니다.

- **일:** 1일은 24시간이며, 사용자가 지연 단계에 진입한 시점부터 계산됩니다.
- **달력 일:** 1일은 사용자가 지연 단계를 입력한 시점부터 해당 시간대의 자정까지의 기간입니다. 즉, 달력으로 하루가 몇 분처럼 짧을 수 있다는 뜻입니다.

Intelligent Timing을 사용할 때는 지연 시간을 24시간이 아닌 달력 날짜를 사용하는 것이 좋습니다. 달력 날짜를 사용하면 지연이 발생한 마지막 날에 최적 시간에 메시지가 전송되기 때문입니다. 24시간을 기준으로 하면 사용자의 최적 시간은 해당 단계에 진입하기 전이므로 지연 시간이 하루 더 추가될 수 있습니다.

예를 들어 루카의 최적 시간이 오후 2시라고 가정해 보겠습니다. 3월 1일 오후 2시 1분 지연 단계에 들어갔으며 지연은 2일로 설정되어 있습니다.

- 1일차는 3월 2일 오후 2시 1분에 종료됩니다.
- 2일차는 3월 3일 오후 2시 1분에 종료됩니다.

그러나 Intelligent Timing은 이미 시간이 지난 오후 2시에 전달되도록 설정되어 있습니다. 따라서 루카는 다음 날까지 메시지를 받지 못합니다. 3월 4일 오후 2시.

![사용자의 최적 시간이 오후 2시인데 오후 2시 01분에 지연 단계를 입력하고 지연이 2일로 설정된 경우 일과 달력 날짜의 차이를 나타내는 그래픽입니다. 일은 사용자가 최적 시간 이후에 단계를 입력했기 때문에 3일 후에 메시지를 전달하지만, 달력 일은 2일 후인 지연 마지막 날에 메시지를 전달합니다.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}

{% endtab %}
{% tab 원본 캔버스 워크플로 %}

원본 캔버스 워크플로에서 Intelligent Timing은 전체 단계의 지연 섹션에서 설정됩니다. 캔버스에서 Intelligent Timing을 사용하는 방법:

1. 캔버스에 단계를 추가합니다.
2. 단계에 대한 **지연**을 엽니다.
3. **예약됨**을 선택합니다.
4. *after*, *in* 또는 *on the next*를 사용하여 지연을 설정합니다.
   - *이후(after)*를 선택하는 경우 지연을 일 또는 주 단위로 설정합니다. 지연은 달력 날짜를 사용하여 자동으로 계산되므로 지연이 발생한 마지막 날에 사용자가 원하는 최적의 시간에 메시지가 전송됩니다. Intelligent Timing은 1일 미만의 지연에는 사용할 수 없습니다.
5. **Intelligent Timing 사용**을 선택합니다.
6. [대체 시간](#fallback-time)을 지정합니다.

{% endtab %}
{% endtabs %}

#### 캔버스 시작하기

캠페인과 달리 전송 날짜 48시간 전에 캔버스를 실행하는 것에 대해 걱정할 필요가 없습니다. 이는 Intelligent Timing이 캔버스 수준이 아닌 단계 수준에서 설정되기 때문입니다. 대신 사용자가 캔버스에 들어가서 Intelligent Timing이 사용되는 단계를 받을 때까지 최소 48시간의 지연 시간을 두는 것이 좋습니다.

### 대체 시간 {#fallback-time}

Braze가 최적 전송 시간을 계산할 수 있는 충분한 인게이지먼트 데이터가 없는 오디언스의 사용자에게 메시지를 전송할 대체 시간을 선택해야 합니다. 두 가지 옵션이 있습니다:

- 전체 사용자가 가장 많이 앱을 사용하는 시간
- 구체적인 커스텀 대체 시간(사용자 현지 시간 기준)

#### 가장 인기 있는 앱 시간

가장 인기 있는 앱 시간은 워크스페이스의 평균 세션 시작 시간(현지 시간 기준)에 따라 결정됩니다. 이 시간은 [미리보기 차트](#preview-delivery-times)에 빨간색으로 표시됩니다(캠페인만 해당).

캠페인의 경우 [전송 기간](#sending-within-specific-hours)을 지정했는데 앱 사용량이 가장 많은 시간이 해당 기간을 벗어나는 경우 전송 기간의 가장자리에 가장 가까운 시간에 메시지가 전송됩니다. 예를 들어 전달 기간이 오후 1시부터 오후 8시까지이고 가장 인기 있는 앱 이용 시간이 오후 10시인 경우 오후 8시에 메시지가 전송됩니다.

**세션 데이터 부족**<br>
드물지만 앱의 세션 데이터가 충분하지 않아 앱이 가장 많이 사용되는 시간을 계산할 수 없는 경우(데이터가 없는 완전히 새로운 앱), 사용자의 현지 시간대 오후 5시에 메시지가 전송됩니다. 사용자의 현지 시간을 알 수 없는 경우 회사 표준 시간대인 오후 5시에 전송됩니다.

사용 가능한 데이터가 제한되어 있는 사용자 생애주기 초기에 Intelligent Timing을 사용할 때의 한계를 인식하는 것이 중요합니다. 기록된 세션이 거의 없는 사용자도 자신의 행동에 대한 인사이트를 제공할 수 있으므로 여전히 유용할 수 있습니다. 그러나 Braze는 사용자 생애주기 후반에 최적의 전송 시간을 보다 효과적으로 계산할 수 있습니다.

#### 커스텀 대체 시간

커스텀 대체 시간을 사용하여 메시지를 보낼 다른 시간을 선택할 수 있습니다. 가장 인기 있는 앱 시간과 마찬가지로 사용자의 현지 표준 시간대의 대체 시간에 메시지가 전송됩니다. 사용자의 현지 표준 시간대를 알 수 없는 경우 회사 표준 시간대로 전송됩니다.

커스텀 대체 시간이 지정된 캠페인의 경우, 전송 날짜로부터 24시간 이내에 캠페인을 실행하면 최적 시간이 이미 지난 사용자에게 커스텀 대체 시간에 캠페인이 전송됩니다. 해당 시간대에서 커스텀 대체 시간이 이미 지난 경우에는 메시지가 즉시 전송됩니다.

## 제한 사항

- 인앱 메시지, 콘텐츠 카드 및 웹훅은 최적의 시간이 지정되지 않고 즉시 전달됩니다.
- 실행 기반 또는 API 트리거 캠페인에는 Intelligent Timing을 사용할 수 없습니다.
- 다음 시나리오에서는 Intelligent Timing을 사용해서는 안 됩니다.
    - **방해금지 시간:** 방해금지 시간과 Intelligent Timing을 모두 사용하는 것은 비생산적인데, 방해금지 시간은 한밤중에 메시지를 보내지 않는 등의 사용자 행동에 대한 하향식 가정을 기반으로 하는 반면 Intelligent Timing은 사용자 활동을 기반으로 하기 때문입니다. 샘은 새벽 3시에 앱 알림을 자주 확인할 수도 있습니다. 저희는 판단하지 않습니다.
    - **사용량 제한조치:** 사용량 제한조치와 Intelligent Timing을 모두 사용하는 경우 메시지가 언제 전달될지 보장할 수 없습니다. Intelligent Timing을 사용하는 일일 반복 캠페인은 총 메시지 전송 한도를 정확하게 지원하지 않습니다.
    - **IP 워밍 캠페인:** 일부 Intelligent Timing 동작으로 인해 IP를 처음 워밍할 때 필요한 일일 볼륨을 달성하는 데 어려움을 겪을 수 있습니다. 이는 Intelligent Timing이 캠페인 또는 캔버스가 처음 생성될 때와 사용자에게 보내기 전에 세그먼트를 두 번 평가하여 사용자가 여전히 해당 세그먼트에 있어야 하는지 확인하기 때문입니다. 이로 인해 세그먼트가 이동하고 변경되어 일부 사용자가 두 번째 평가에서 세그먼트에서 탈락하는 경우가 종종 있습니다. 이러한 사용자는 교체되지 않으므로 달성할 수 있는 최대 사용자 수에 영향을 미칩니다.

## 문제 해결

### 최적의 시간을 가진 소수의 사용자를 보여주는 미리보기 차트

Braze는 정확한 예측을 위해 일정량의 인게이지먼트 데이터가 필요합니다. 세션 데이터가 충분하지 않거나 타겟 사용자의 클릭 또는 열람 횟수가 거의 또는 전혀 없는 경우(신규 사용자 등), Braze는 기본적으로 대체 시간으로 설정됩니다. 구성에 따라 가장 많이 사용되는 앱 시간 또는 커스텀 대체 시간이 될 수 있습니다.

### 예정된 날짜가 지나서 보내기

Your Intelligent Timing campaign might be sending past the scheduled date if you are leveraging [A/B testing with an optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). A/B 테스트 최적화를 사용하는 캠페인은 초기 테스트가 종료된 후 자동으로 위닝 배리언트를 전송하여 캠페인 기간을 늘릴 수 있습니다. 기본적으로 최적화가 적용된 캠페인은 초기 테스트 다음 날에 나머지 사용자에게 위닝 배리언트를 전송하지만, 이 전송 날짜를 변경할 수 있습니다.

Intelligent Timing을 사용하는 경우, A/B 테스트가 완료될 때까지 시간을 더 두고 위닝 배리언트를 초기 테스트 후 1일이 아닌 2일 동안 전송하도록 예약하는 것이 좋습니다.


[1]: {% image_buster /assets/img/intelligent_timing_1.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
[4]: {% image_buster /assets/img/intelligent_timing_hours.png %}
[5]: {% image_buster /assets/img/intelligent_timing_ab_test_duration.png %}
