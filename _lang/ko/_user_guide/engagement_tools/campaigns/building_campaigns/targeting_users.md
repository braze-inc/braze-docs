---
nav_title: 사용자 타겟팅
article_title: 사용자 타겟팅
page_order: 4
tool: Campaigns
page_type: reference
description: "이 참조 문서에서는 캠페인 생성의 타겟 오디언스 단계에 있는 타겟팅 옵션에 대해 설명합니다."
---

# 사용자 타겟팅

> [캠페인을 구성하고][1] [전달 일정을][2] 결정한 후에는 **타겟 대상** 단계에서 캠페인의 타겟 수신자를 설정할 수 있습니다. 

## 타겟팅 옵션

**타겟팅 옵션** 섹션에는 캠페인을 보낼 수 있는 대상에 대한 몇 가지 옵션이 있습니다.

{% alert note %}
정의한 기준과 일치하는 사용자만 캠페인을 받게 됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.
{% endalert %}

### 기존 세그먼트의 타겟 사용자 {#existing-segment}

이전에 만든 세그먼트의 멤버를 타겟팅하려면 **세그먼트별 타겟팅 사용자** 아래의 드롭다운에서 하나의 세그먼트를 선택합니다.

### 기존 여러 세그먼트의 사용자 타겟팅 {#multiple-existing-segment}

이전에 생성한 여러 세그먼트에 속하는 사용자를 타겟팅하려면 **세그먼트별 타겟팅 사용자** 아래의 드롭다운에서 여러 세그먼트를 추가합니다. 결과 타겟 오디언스는 첫 번째 세그먼트와 두 번째 세그먼트, 세 번째 세그먼트 등의 사용자가 될 것입니다.

### 기존 여러 세그먼트 및 필터의 사용자 타겟팅 {#existing_segment_filter}

또한 추가 필터에 해당하는 이전에 생성한 하나 이상의 세그먼트의 사용자를 타겟팅할 수도 있습니다. 먼저 세그먼트를 선택한 후 **추가 필터** 섹션에서 오디언스를 더욱 세분화할 수 있습니다. 이는 일일 활성 사용자 세그먼트, 이메일을 열지 않음 세그먼트에 속하며 30일 이내에 구매한 사용자를 대상으로 하는 다음 스크린샷에서 확인할 수 있습니다.

![][25]

### 세그먼트 없이 사용자 타겟팅 {#without-segment}

세그먼트를 추가하지 않고 사용자를 타겟팅하려면 일련의 필터를 사용할 수 있습니다. 즉, 기존 세그먼트에서 캠페인을 타겟팅할 필요가 없으며, **세그먼트별 타겟팅 사용자**에서 세그먼트를 선택하지 않고 추가 필터만 사용하여 캠페인 생성 중에 즉석에서 오디언스를 만들 수 있습니다. 이렇게 하면 일회성 오디언스에게 캠페인을 보낼 때 세그먼트 생성을 건너뛸 수 있습니다.

![][26]

## 시드 그룹 타겟팅

이메일 캠페인의 경우 **시드 그룹** 섹션에서 시드 그룹을 타겟팅할 수 있습니다. 캠페인에서 API 트리거 항목을 통해 시드 그룹을 포함할 수는 있지만, API 캠페인에는 시드 그룹을 사용할 수 없습니다. 자세한 내용은 [시드 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups)을 참조하세요.

## 오디언스를 테스트 중

After adding segments and filters to your audience, you can test if your audience is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) to confirm if they match the audience criteria.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## 오디언스 요약

세그먼트 또는 필터를 추가하여 오디언스를 세밀하게 조정하면 **오디언스 요약**에 타겟 오디언스에 누가 포함되는지에 대한 개요가 표시됩니다. 여기에서 최대 사용자 한도를 설정하거나 [사용량 제한조치][3]를 설정하여 캠페인 오디언스를 더욱 제한할 수 있습니다. 이메일 및 푸시 알림 캠페인의 경우 타겟팅할 구독 및 옵트인 상태를 선택할 수 있습니다.

![][27]

## A/B 테스트

**A/B 테스트** 섹션에서 동일한 마케팅 캠페인의 여러 버전에 대한 사용자의 반응을 비교하는 테스트를 설정할 수 있습니다. 이 버전은 비슷한 마케팅 목표를 공유하지만 문구와 스타일이 다릅니다. 목표는 마케팅 목표를 가장 잘 달성할 수 있는 캠페인 버전을 식별하는 것입니다. 

자세한 내용과 모범 사례는 [다변량 및 A/B 테스트][4]를 참조하세요.

## 오디언스 통계

Braze는 바닥글에 타겟 채널에 대한 자세한 오디언스 통계를 제공합니다. 

사용자 기반이 클수록 **도달 가능한 사용자** 수는 대략적인 추정치일 가능성이 높습니다. [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/)을 사용하거나 메시지 자격을 설정하면 도달 가능한 사용자 수가 줄어들 수 있습니다. [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) 선택하면 사용자 기반의 모든 사용자를 검색하므로 도달 가능한 사용자의 정확한 수치를 확인할 수 있습니다. 

참고:

- 정확한 통계를 계산하는 데 몇 분이 걸릴 수 있습니다. 이 함수는 필터 또는 필터 그룹 수준이 아닌 세그먼트 수준에서만 정확한 통계를 계산합니다.
- 큰 세그먼트의 경우, 정확한 통계를 계산할 때에도 약간의 변동이 있는 것이 정상입니다. 이 기능의 정확도는 99.999% 이상일 것으로 예상됩니다.

![][24]

타겟팅 중인 사용자 기반의 비율 또는 이 세그먼트의 평생 가치(LTV)를 확인하려면 **추가 통계 보기를** 선택합니다.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
