---
nav_title: 사용자 타겟팅
article_title: 타겟팅 사용자
page_order: 9
page_type: reference
description: "이 참조 문서에서는 캠페인 및 Canvas 편집기에서 오디언스를 타겟팅하는 방법에 대해 설명합니다."
tool:
    - Campaigns
    - Canvas
---

# 사용자 타겟팅

> 사용자를 타겟팅하는 방법을 결정하는 것은 캠페인이나 캔버스를 만들 때 가장 중요한 단계 중 하나입니다. 행동, 선호도 및 인구통계를 기반으로 오디언스를 세분화하는 방법을 이해하면 메시지를 맞춤 설정하고 개인화할 수 있습니다.

## 타겟 오디언스 만들기

### 1단계: 사용자 선택

**타겟팅 옵션에서** 다음 옵션을 사용하여 캠페인 또는 캔버스에서 타겟팅할 사용자를 선택할 수 있습니다. 정의한 기준과 일치하는 사용자만 메시지를 받게 됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

{% tabs local %}
{% tab 단일 세그먼트 %}
이전에 만든 세그먼트의 멤버를 타겟팅하려면 **세그먼트별 타겟팅 사용자** 아래의 드롭다운에서 하나의 세그먼트를 선택합니다.
{% endtab %}

{% tab 여러 세그먼트 %}
이전에 생성한 여러 세그먼트에 속하는 사용자를 타겟팅하려면 **세그먼트별 타겟팅 사용자** 아래의 드롭다운에서 여러 세그먼트를 추가합니다. 결과 타겟 오디언스는 첫 번째 세그먼트와 두 번째 세그먼트, 세 번째 세그먼트 등의 사용자가 될 것입니다.
{% endtab %}

{% tab 여러 필터 %}
세그먼트를 추가하지 않고 사용자를 타겟팅하려면 일련의 필터를 사용할 수 있습니다. 이는 메시지 작성 중 즉석 대상이며 일회성 대상에게 보낼 때 세그먼트 생성을 건너뛸 수 있습니다.

![하루 이내에 마지막으로 앱을 열었고, 캠페인이나 캔버스 단계를 받은 적이 없으며, 구매한 지 30일이 지나지 않은 사용자를 대상으로 하는 메시지를 위한 추가 필터입니다.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab 세그먼트 및 필터 %}
또한 추가 필터에 해당하는 이전에 생성한 하나 이상의 세그먼트의 사용자를 타겟팅할 수도 있습니다. 먼저 세그먼트를 선택한 후 **추가 필터** 섹션에서 오디언스를 더욱 세분화할 수 있습니다. 이는 '일일 활성 사용자' 세그먼트, '이메일을 열어본 적이 없음' 세그먼트에 속하며 30일 이상 전에 구매한 사용자를 대상으로 하는 다음 스크린샷에서 확인할 수 있습니다.

![두 개의 세그먼트가 포함된 메시지에 대한 타겟팅 옵션과 30일 전에 이루어진 마지막 구매에 대한 추가 필터가 있습니다.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab 특정 앱 %}

특정 앱에만 인앱 메시지 또는 푸시 알림을 보내는 등 특정 앱에 캠페인 메시지 또는 캔버스 단계를 전달할 수 있습니다.

하지만 한 사용자가 여러 앱을 사용할 수 있다는 점을 기억하세요. '앱 있음' 필터는 선택한 앱을 가지고 있는 모든 사용자를 식별하지만 메시지를 받는 앱은 제어하지 않습니다. 예를 들어 '앱 있음'이 Android로 설정된 세그먼트 필터를 적용하면 iOS 앱도 가지고 있는 모든 사용자가 iOS 앱에서도 메시지를 받게 됩니다.

!["Hello, World(Android)" 앱을 보유한 사용자를 위한 필터입니다.]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Android 앱에만 인앱 메시지를 보내고 싶다고 가정해 보겠습니다.

1. 세그먼트를 만들고 **특정 앱의 사용자를** **대상으로 하는 앱 및 웹사이트를** 설정한 다음 Android 앱을 선택합니다.

![특정 앱의 사용자를 타겟팅하는 세그먼트인 "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. 캠페인 또는 캔버스에서 **타겟 오디언스** 단계로 이동하여 **세그먼트별 타겟 사용자** 섹션에서 세그먼트가 추가되었는지 확인합니다. 

![예시 세그먼트가 선택된 '타겟 오디언스' 단계]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
세그먼트 멤버십 필터를 통해 **추가 필터** 섹션에서 세그먼트를 추가하는 경우에는 이 기능이 작동하지 않습니다. 해당 앱에만 메시지를 전달하려면 **세그먼트별 타겟 사용자에서** 세그먼트를 직접 참조해야 합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
이메일 캠페인의 경우 **시드 그룹** 섹션에서 시드 그룹을 타겟팅할 수 있습니다. 캠페인에서 API 트리거 항목을 통해 시드 그룹을 포함할 수는 있지만, API 캠페인에는 시드 그룹을 사용할 수 없습니다. 자세한 내용은 [시드 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups)을 참조하세요.
{% endalert %}

### 2단계: 잠재 고객 테스트

After adding segments and filters to your audience, you can test if your audience is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) to confirm if they match the audience criteria.

!["사용자 조회" 버튼이 있는 "사용자 조회" 섹션]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### 오디언스 요약

오디언스 **요약에는** 타겟 오디언스에 누가 포함되어 있는지에 대한 개요가 표시됩니다. 여기에서 최대 사용자 수 제한 또는 전송 속도 [제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) 설정하여 잠재고객을 더욱 제한할 수 있습니다.

![최대 사용자 한도 또는 전송 속도 제한을 설정하는 옵션이 있는 '잠재 고객 요약' 섹션]({% image_buster /assets/img_archive/audience_summary.png %})

#### A/B 테스트

**A/B 테스트** 섹션에서는 동일한 마케팅 캠페인의 여러 버전에 대한 사용자의 반응을 비교하는 테스트를 설정할 수 있습니다. 이 버전은 비슷한 마케팅 목표를 공유하지만 문구와 스타일이 다릅니다. 목표는 마케팅 목표를 가장 잘 달성할 수 있는 캠페인 버전을 식별하는 것입니다. 

자세한 내용과 모범 사례는 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

#### 오디언스 통계

Braze는 바닥글에 타겟 채널에 대한 자세한 오디언스 통계를 제공합니다. 사용자 기반이 클수록 **도달 가능한 사용자** 수는 대략적인 추정치일 가능성이 높습니다. [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/)을 사용하거나 메시지 자격을 설정하면 도달 가능한 사용자 수가 줄어들 수 있습니다. 

- 도달 가능한 사용자의 정확한 숫자를 확인하려면 [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) 선택하면 사용자 기반의 모든 사용자를 검색할 수 있습니다.
- 타겟팅 중인 사용자 기반의 비율 또는 이 세그먼트의 평생 가치(LTV)를 확인하려면 **추가 통계 보기를** 선택합니다.
- 타겟팅 중인 사용자 기반의 비율 또는 이 세그먼트의 평생 가치(LTV)를 확인하려면 **추가 통계 보기를** 선택합니다.

##### 타겟 오디언스 수가 도달 가능한 사용자 수와 다를 수 있는 이유

{% multi_lang_include segments.md section='다른 잠재 고객 규모' %}

![각 타겟 채널에서 도달 가능한 사용자의 예상 수가 표시된 '총 인구수' 섹션]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
정확한 통계를 계산하는 데 몇 분이 걸릴 수 있습니다. 이 함수는 필터 또는 필터 그룹 수준이 아닌 세그먼트 수준에서만 정확한 통계를 계산합니다.<br><br>
큰 세그먼트의 경우, 정확한 통계를 계산할 때에도 약간의 변동이 있는 것이 정상입니다. 이 기능의 정확도는 99.999% 이상일 것으로 예상됩니다.
{% endalert %}

