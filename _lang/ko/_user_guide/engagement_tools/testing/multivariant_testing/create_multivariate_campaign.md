---
nav_title: 테스트 만들기
article_title: 다변량 및 A/B 테스트 만들기
page_order: 1
page_type: reference
description: "이 문서에서는 Braze로 다변량 및 A/B 테스트를 만드는 방법을 설명합니다."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# 다변량 및 A/B 테스트 만들기 {#creating-tests}

> 단일 채널을 타겟팅하는 모든 캠페인에 대해 [다변량 또는 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 만들 수 있습니다.

![][2]{: style="max-width:25%;float:right;margin-left:15px;" }

## 1단계: 캠페인 만들기

**캠페인 생성**을 클릭하고 다변량 및 A/B 테스트가 가능한 섹션에서 캠페인의 채널을 선택합니다. 각 메시징 채널에 대한 자세한 설명서는 [캠페인 만들기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)를 참조하세요.

## 2단계: 배리언트 상품 구성

제목, 콘텐츠, 이미지 등을 차별화하여 최대 8가지의 메시지 배리언트를 만들 수 있습니다. 메시지 간 차이의 수에 따라 다변량 테스트인지 A/B 테스트인지가 결정됩니다. A/B 테스트는 하나의 변수를 변경했을 때의 효과를 검사하는 반면, 다변량 테스트는 두 개 이상의 변수를 검사합니다.

이형 상품 차별화를 시작하는 방법에 대한 몇 가지 아이디어는 [채널별 팁을](#tips-different-channels) 참조하세요.

![][3]

## 3단계: 캠페인 예약하기

다변량 캠페인의 예약은 다른 Braze 캠페인의 예약과 동일하게 작동합니다. 모든 표준 [전달 유형][4]을 사용할 수 있습니다.

다변량 테스트가 시작되면 캠페인을 변경할 수 없습니다. 제목이나 HTML 본문과 같은 매개변수를 변경하면 Braze는 실험이 손상된 것으로 간주하고 즉시 실험을 비활성화합니다.

{% alert important %}
[최적화]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (일부 채널에서 사용 가능)를 사용하려면 캠페인을 한 번만 게재하도록 예약하세요. 반복되거나 재적격성이 켜져 있는 캠페인에는 최적화를 사용할 수 없습니다.
{% endalert %}

## 4단계: 세그먼트를 선택하고 배리언트 상품에 사용자를 배포하세요.

타겟팅할 세그먼트를 선택한 다음 선택한 배리언트 상품과 선택적 [대조군](#including-a-control-group)에 멤버를 배포합니다. 테스트할 세그먼트 선택에 대한 모범 사례는 [세그먼트 선택하기](#choosing-a-segment)를 참조하세요.

한 번만 전송하도록 예약된 푸시, 이메일 및 웹훅 캠페인의 경우 [최적화를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) 사용할 수도 있습니다. 이렇게 하면 A/B 테스트에서 타겟 오디언스의 일부를 예약하고 첫 번째 테스트의 결과를 기반으로 두 번째 최적화된 전송을 위해 보류합니다.

### 대조군 {#including-a-control-group}

타겟 오디언스의 일정 비율을 무작위 대조군으로 예약할 수 있습니다. 대조군 사용자에게는 테스트가 제공되지 않지만, Braze는 캠페인 기간 동안 전환율을 모니터링합니다.

결과를 볼 때 이형 상품의 전환율을 대조 그룹에서 제공한 기준 전환율과 비교할 수 있습니다. 이를 통해 메시지를 전혀 보내지 않았을 때 발생할 전환율과 배리언트의 효과를 모두 비교할 수 있습니다.

![대조군, 배리언트 1, 배리언트 2 및 배리언트 3의 백분율 분석을 각 그룹에 대해 25%로 표시하는 A/B 테스트 패널입니다.][5]

{% alert important %}
열기 또는 클릭 수로 우승자를 결정할 때 대조군을 사용하는 것은 권장되지 않습니다. 대조군은 메시지를 수신하지 않으므로 해당 사용자는 열기나 클릭을 수행할 수 없습니다. 따라서 해당 그룹의 전환율은 정의상 0%이므로 배리언트 상품과 의미 있는 비교가 되지 않습니다.
{% endalert %}

#### A/B 테스트를 통한 대조군

A/B 테스트에서 사용량 제한을 사용하는 경우, 사용량 제한은 테스트 그룹과 동일한 방식으로 대조군에 적용되지 않으므로 시간 편향의 잠재적 원인이 될 수 있습니다. 이러한 편향을 피하려면 적절한 전환 기간을 사용하세요.

#### 지능형 선택 기능이 있는 제어 그룹

[지능형 선택을][1] 사용하는 캠페인의 대조군 크기는 이형 상품 수를 기준으로 합니다. 각 배리언트가 20% 이상의 사용자에게 전송되는 경우, 대조군은 20%이고 변종은 나머지 80%에 균등하게 분배됩니다. 그러나 각 배리언트가 20% 미만의 사용자에게 전송될 만큼 충분한 변종이 있는 경우 대조군은 더 작아져야 합니다. 지능형 선택이 테스트의 성과를 분석하기 시작하면 결과에 따라 대조군이 커지거나 줄어듭니다.

## 5단계: 전환 이벤트 지정(선택 사항)

캠페인에 전환 이벤트를 설정하면 해당 캠페인을 수신한 후 특정 작업을 수행한 수신자 수를 확인할 수 있습니다.

이는 이전 단계에서 **주요 전환**을 선택한 경우에만 테스트에 영향을 미칩니다. 자세한 내용은 [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) 참조하세요. 

## 6단계: 검토 및 실행

확인 페이지에서 다변량 캠페인의 세부 정보를 검토하고 테스트를 시작하세요! 다음으로 [테스트 결과를 이해하는]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/) 방법을 알아보세요.

## 알아두어야 할 사항

{% alert important %}
실험이 시작된 후 메시지를 수정하면 테스트 결과가 무효화됩니다.

- 실험이 전송 중일 때 메시지를 수정하면 실험이 쓸모없어지고 실험 결과가 모두 제거됩니다.
- 실험이 완료되고 전송 후 메시지를 수정하면 대시보드 분석 페이지에서 실험 결과를 계속 확인할 수 있습니다. 캠페인을 다시 실행하면 실험 결과가 제거됩니다.
{% endalert %}

### 다양한 채널을 위한 팁 {#tips-different-channels}

어떤 채널을 선택하느냐에 따라 메시지의 다양한 구성 요소를 테스트할 수 있습니다. 무엇을 테스트하고 무엇을 증명하고자 하는지에 대한 아이디어를 가지고 변형을 작성해 보세요.

어떤 레버를 당겨야 하며 원하는 효과는 무엇인가요? 다변량 및 A/B 테스트를 사용하여 조사할 수 있는 가능성은 수백만 가지가 있지만, 시작하기 위한 몇 가지 제안 사항이 있습니다.

| 채널 | 변경할 수 있는 메시지의 측면 | 찾아야 할 결과 |
| ---------------------| --------------- | ------------- |
| 푸시 | 복사 <br> 이미지 및 이모티콘 사용 <br> 딥링크  <br> 숫자 표시(예: "3배" 대 "200% 증가")  <br> 시간 표시(예: "자정에 종료" 대 "6시간 후 종료") | 열람 수  <br> 전환율 |
| 이메일 | 제목 <br> 표시 이름 <br> 인사말 <br> 본문 복사 <br> 이미지 및 이모티콘 사용 <br> 숫자 표시(예: "3배" 대 "200% 증가") <br> 시간 표시(예: "자정에 종료" 대 "6시간 후 종료") | 열람 수  <br> 전환율 |
| 인앱 메시지 | "푸시"에 대해 나열된 측면 <br> [메시지 형식][7] | 클릭 <br> 전환율 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
When running A/B tests, don't forget to generate [funnel reports]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) that let you understand how each variant impacted your conversion funnel, especially if "conversion" for your business involves taking multiple steps or actions.
{% endalert %}

또한 채널에 따라 이상적인 테스트 길이도 달라질 수 있습니다. 대부분의 사용자가 각 채널에 참여하는 데 걸리는 평균 시간을 염두에 두세요.

예를 들어 푸시를 테스트하는 경우 사용자가 푸시를 즉시 확인하지만 이메일을 확인하거나 열기까지 며칠이 걸릴 수 있으므로 이메일을 테스트할 때보다 더 빠르게 유의미한 결과를 얻을 수 있습니다. 인앱 메시지를 테스트하는 경우, 사용자가 캠페인을 보려면 앱을 열어야 하므로 가장 활발하게 앱을 여는 사용자뿐만 아니라 일반적인 사용자로부터 결과를 수집하려면 더 오래 기다려야 한다는 점에 유의하세요.

테스트를 얼마나 오래 실행해야 할지 잘 모르겠다면 [지능형 선택][6] 기능을 사용하면 위닝 배리언트를 효율적으로 찾을 수 있습니다.

### 세그먼트 선택 {#choosing-a-segment}

사용자 세그먼트에 따라 메시지에 다르게 반응할 수 있으므로 특정 메시지의 성공 여부는 메시지 자체와 대상 세그먼트 모두에 대해 알 수 있습니다. 따라서 타겟 세그먼트를 염두에 두고 테스트를 설계하세요.

예를 들어, 활성 사용자는 "이 딜은 내일 만료됩니다!"와 "이 딜은 24시간 후에 만료됩니다!"에 대한 응답률이 동일할 수 있지만, 일주일 동안 앱을 열지 않은 사용자는 후자의 문구가 더 긴박감을 주기 때문에 후자의 문구에 더 많은 반응을 보일 수 있습니다.

또한 테스트를 실행할 세그먼트를 선택할 때는 해당 세그먼트의 크기가 테스트에 충분히 큰지 고려해야 합니다. 일반적으로 배리언트가 많은 다변량 및 A/B 테스트는 통계적으로 유의미한 결과를 얻기 위해 더 큰 테스트 그룹이 필요합니다. 이형 상품이 많아지면 각 이형 상품을 보는 사용자 수가 줄어들기 때문입니다.

{% alert tip %}
일반적으로 테스트 결과에서 95%의 신뢰도를 얻으려면 배리언트 상품당 약 15,000명의 사용자(대조군 포함)가 필요합니다. 그러나 필요한 정확한 사용자 수는 특정 사례에 따라 이보다 더 많거나 적을 수 있습니다. 배리언트 샘플 크기에 대한 보다 정확한 지침은 [샘플 크기 계산기](https://www.calculator.net/sample-size-calculator.html)를 참조하세요.
{% endalert %}

### 편향 및 무작위 배정

대조군 및 테스트 그룹 할당에 대한 일반적인 질문은 테스트에 편향이 생길 수 있는지 궁금해하는 것입니다. 어떤 사람들은 이러한 과제가 정말 무작위인지 어떻게 알 수 있는지 궁금해하기도 합니다.

사용자는 (무작위로 생성된) 사용자 ID를 (무작위로 생성된) 캠페인 또는 캔버스 ID와 연결하고 해당 값의 계수를 100으로 하여 메시지 배리언트, 캔버스 배리언트 또는 각각의 대조군에 할당된 다음, 대시보드에서 선택한 배리언트 및 선택적 제어에 대한 할당 비율에 해당하는 슬라이스로 사용자를 정렬합니다. 따라서 특정 캠페인이나 캔버스를 만들기 전 사용자의 행동이 변형과 제어에 따라 체계적으로 달라질 수 있는 실질적인 방법은 없습니다. 또한 이 구현보다 더 무작위(또는 더 정확하게는 의사 무작위)로 구현하는 것은 실용적이지 않습니다.

#### 피해야 할 실수

오디언스를 올바르게 필터링하지 않으면 메시징 채널에 따라 차이가 있는 것처럼 보이게 되는 몇 가지 일반적인 실수를 피할 수 있습니다.

예를 들어, 컨트롤을 사용하여 광범위한 대상에게 푸시 메시지를 보내는 경우 테스트 그룹은 푸시 토큰이 있는 사용자에게만 메시지를 보냅니다. 그러나 대조군에는 푸시 토큰을 보유한 사용자와 그렇지 않은 사용자가 모두 포함됩니다. 이 경우 캠페인 또는 캔버스의 초기 오디언스가 푸시 토큰을 가지고 있는지 필터링해야 합니다(`Push Enabled`는 `true`). 다른 채널에서 메시지를 받을 수 있는 자격(옵트인, 푸시 토큰 보유, 구독 등)을 갖추려면 동일한 절차를 거쳐야 합니다.

{% alert note %}
대조군에 무작위 버킷 번호를 수동으로 사용하는 경우, 대조군에서 [주의해야 할 사항]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) 목록을 참조하세요.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
[6]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
