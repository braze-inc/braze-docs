---
nav_title: 지능형 선택
article_title: 지능형 선택
page_order: 1.0
description: "이 문서에서는 하루에 두 번 반복 캠페인 또는 캔버스의 성과를 분석하여 각 메시지 배리언트를 수신하는 사용자의 비율을 자동으로 조정하는 기능인 지능형 선택에 대해 설명합니다."
search_rank: 10
toc_headers: h2
---

# 지능형 선택 {#intelligent-selection}

> 지능형 선택은 하루에 두 번 반복되는 캠페인 또는 캔버스의 성과를 분석하여 각 메시지 배리언트를 수신하는 사용자의 비율을 자동으로 조정하는 기능입니다. 

## About Intelligent Selection

다른 배리언트보다 실적이 더 좋은 것으로 보이는 배리언트는 더 많은 사용자에게 전송되고, 실적이 저조한 배리언트는 더 적은 수의 사용자에게 타겟팅됩니다. Each adjustment is made using a [statistical algorithm](https://en.wikipedia.org/wiki/Multi-armed_bandit) that makes sure Braze is adjusting for real performance differences and not just random chance.

![A/B Testing section of a campaign with Intelligent Selection enabled.]({% image_buster /assets/img/intelligent_selection1.png %})

지능형 선택의 기능:
- 성과 데이터를 반복적으로 살펴보고 캠페인 트래픽을 점차적으로 위닝 배리언트로 전환.
- 통계적 신뢰도를 유지하면서 더 많은 사용자가 가장 성능이 좋은 배리언트를 받을 수 있는지 확인.
- Rule out underperforming variants and identify high-performing variants faster than a [traditional A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- 사용자가 최상의 메시지를 볼 수 있도록 더 자주, 더 자신 있게 테스트하세요. 

Intelligent Selection works best for campaigns that send more than once. It needs early performance data to start optimizing, so single-send campaigns won’t benefit. For those campaigns, we recommend using a traditional [A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) instead.

## Prerequisites

{% tabs %}
{% tab Campaign %}
Before adding Intelligent Selection to your campaign, make sure you’ve set things up correctly:

- Your campaign sends on a recurring schedule. Single-send campaigns aren’t supported.
- You’ve added at least two message variants.
- You’ve defined a conversion event to measure performance across variants.
- The re-eligibility window is set to 24 hours or longer. Shorter windows aren’t supported, as they would affect the integrity of the control variant. To learn more, refer to [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
To use Intelligent Selection in a Canvas, confirm the following:
- Your Canvas includes at least two message variants in a Message step.
- You’ve added at least one conversion event.
{% endtab %}
{% endtabs %}

## Adding Intelligent Selection

You can add Intelligent Selection to your campaigns and Canvases.

{% tabs %}
{% tab Campaign %}
Intelligent Selection can be added to any multi-send campaign in the **Target Audiences** step of the Braze campaign composer. 한 번만 전송하는 캠페인은 이 기능을 활용할 수 없습니다.

{% alert note %}
Intelligent Selection cannot be used in campaigns with a re-eligibility period of less than 24 hours because it would affect the integrity of the control variant. To learn more, refer to [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Add at least one conversion event and two variants to your Canvas. Then, select one of the variant percentages in the Build step. 

![A Canvas with two variants, each set to 50% variant distribution, allowing Intelligent Selection to be enabled.]({% image_buster /assets/img/intelligent_selection.png %})

이를 통해 배리언트 배포를 편집하고 지능형 선택을 켤 수 있습니다. 

![Intelligent Selection option turned on for a Canvas]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

아직 캔버스에 전환 이벤트를 추가하지 않았거나 캠페인이 단독 배리언트로 구성된 경우에는 지능형 선택을 사용할 수 없습니다.
{% endtab %}
{% endtabs %}

## Run time

캠페인 및 캔버스의 경우, 지능형 선택은 배리언트의 "실제" 전환율에 대한 충분한 증거를 수집할 때까지 실행됩니다. "충분함"은 "후회"라는 특별한 지표에 의해 결정됩니다. 어떤 배리언트가 가장 적합한지 알 수 있는 충분한 데이터가 확보되면 지능형 선택 기능이 저절로 꺼질 것이라는 확신과 비슷하다고 생각하면 됩니다. 

대부분의 경우 지능형 선택은 배리언트 중 하나를 우승 배리언트으로 선택합니다. 이 배리언트는 향후 전송 시 100%의 오디언스에게 제공됩니다.

{% alert note %}
지능형 선택은 확실한 위너를 하나도 선택하지 않고 최적화를 중단할 수 있습니다. 지능형 선택은 실험을 계속해도 전환율이 현재 전환율의 1% 이상 개선되지 않을 것이라는 95%의 확신이 들면 최적화를 중지합니다.
{% endalert %}

## Frequently Asked Questions (FAQ) {#faq}

### Why is re-eligibility in less than 24 hours not available when combined with Intelligent Selection?

We don't allow Intelligent Selection campaigns to have re-eligibility in too short of a window because it would affect the integrity of the control variant. By creating a gap of 24 hours, we help ensure that the algorithm will have a statistically valid dataset to work with.

Normally, campaigns with re-eligibility will cause users to re-enter the same variant they received before. With Intelligent Selection, Braze can't guarantee that a user will receive the same campaign variant because the variant distribution would have shifted due to the optimum allocation aspect for this feature. If the user were to be allowed to re-enter before Intelligent Selection re-examines the variant performance, the data might be skewed due to users who re-entered.

For example, if a campaign is using these variants:

- Variant A: 20%
- Variant B: 20%
- Control: 60%

Then the variant distribution could be the following for the second round:

- Variant A: 15%
- Variant B: 25%
- Control: 60%

### Why are my Intelligent Selection variants showing equal sends during the early stages of my campaign?

Intelligent Selection allocates variants for sending based on the current status of campaign conversion. It only determines the final variant allocations after a training period, where sends are sent evenly across variants. If you don't want the Intelligent Selection to send evenly during the early stages of your campaign, use fixed variants for a traditional A/B test.

### Will Intelligent Selection stop optimizing without picking a clear winner?

Intelligent Selection will stop optimizing when it has 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its current rate.

### Why can't I enable Intelligent Selection in my Canvas or campaign (grayed out)?

Intelligent Selection will be unavailable if:

- You haven't added conversion events to your campaign or Canvas
- You are creating a single-send campaign
- You have reeligibility enabled with a window less than 24 hours
- Your Canvas is composed of a single variant with no additional variants or control groups added
- Your Canvas is composed of a single control group, with no variants added
