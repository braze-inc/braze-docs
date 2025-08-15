---
nav_title: SMS 메시지 만들기
article_title: SMS 메시지 만들기
page_order: 5
description: "이 참조 문서에서는 SMS 메시지 구축 및 작성과 관련된 단계를 다룹니다."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# SMS 메시지 만들기

> SMS 캠페인은 고객에게 직접 다가가 프로그래밍 방식으로 대화하는 데 유용합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인적인 경험을 만들고 브랜드에 대한 사용자 경험을 방해하지 않는 환경을 조성하고 향상시킬 수 있습니다. 

## 1단계: 메시지를 작성할 위치 선택

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab 캠페인 %}

**단계:**

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **SMS를** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가하세요.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. 캠페인에 필요한 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.
6. [구독 그룹을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) 선택하여 적절한 사용자에게 메시지를 보낼 수 있도록 하세요. 구독 그룹을 선택할 때 Braze는 자동으로 세그먼트 필터를 추가하여 구독한 사용자만 캠페인을 수신할 수 있도록 합니다. 해당 구독 그룹에 속하는 긴 코드와 짧은 코드만 대상 사용자에게 SMS를 보내는 데 사용됩니다.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 상품 추가** 드롭다운에서 **배리언트 상품에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab 캔버스 %}

**단계:**

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 스케줄]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 메시지가 전송된 후 지연 시간이 지나면 오디언스 옵션이 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)을 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: SMS 메시지 작성

필요에 따라 언어 및 개인화(리퀴드, 커넥티드 콘텐츠, 이모티콘)를 사용하여 메시지를 작성하세요. 초과량 요금이 부과될 가능성을 줄이려면 메시지 사본 한도를 준수해야 합니다.

{% alert important %}
계속 진행하기 전에 [SMS 메시지 세그먼트 및 복사 제한에]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) 대한 가이드라인을 읽어보세요. SMS 메시지 세그먼트는 휴대폰 사업자가 문자 메시지를 측정하는 데 사용하는 문자 일괄 처리입니다. 메시지는 메시지 세그먼트별로 요금이 부과되므로 메시지가 분할되는 방식에 대한 뉘앙스를 이해하는 것이 좋습니다.
{% endalert %}

!["안녕하세요 first_name, 여러분의 성원에 감사드립니다!"라는 메시지가 담긴 Braze의 SMS 빌더! 매장에 들러 이 SMS를 제시하고 특별 할인 혜택을 받아보는 것은 어떨까요? 답장 중지를 통해 메시지 수신을 중지할 수 있습니다."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Adding a contact card

You can add a contact card to your SMS message to make it easy for your customers to add your business and contact information to their contacts. 이러한 카드에 회사 이름, 전화번호, 주소, 이메일, 작은 사진 등의 공통 속성을 지정할 수 있습니다. 자세한 내용은 [연락처 카드에서]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) 확인하세요.

### Tips

#### Using Liquid

{% raw %}
If you plan to use Liquid, be sure to include a default value for your chosen personalization so, in the event your user profile of the recipient is incomplete, they will not receive a blank placeholder `Hi, !`, instead of their name or a coherent sentence.
{% endraw %}

#### Generating AI copy

멋진 카피를 만드는 데 도움이 필요하신가요? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/). 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있도록 사람과 유사한 마케팅 문구를 생성합니다.

![SMS 작성기의 메시지 필드에 있는 AI 카피라이터 실행 버튼(]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## 3단계: 메시지 미리보기 및 테스트

Braze는 항상 메시지를 보내기 전에 미리 보고 테스트할 것을 권장합니다. **테스트** 탭으로 전환하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트 SMS를 보내거나 Braze에서 직접 사용자로 메시지를 미리 볼 수 있습니다.

![작성기의 테스트 탭에서 SMS 사본 미리보기. 프로필 섹션에서 이름 필드가 "James"로 설정되어 있습니다. 이제 미리보기 섹션에 "안녕하세요 제임스, 여러분의 성원에 감사드립니다!"]({% image_buster /assets/img/sms_campaign_test.png %})라는 메시지가 표시됩니다.

{% alert tip %}
SMS를 몇 개의 세그먼트로 분할할 수 있는지 테스트하려면 [SMS 세그먼트 계산기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator) 사용하여 카피 길이를 테스트하세요.
{% endalert %}

## 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab 캠페인 %}

그런 다음 나머지 캠페인을 구축합니다. 다음 섹션에서 도구를 가장 효과적으로 사용하여 SMS 메시지를 작성하는 방법에 대한 자세한 내용을 참조하세요.

#### 배송 일정 또는 트리거 선택

SMS 메시지는 예약된 시간, 작업 또는 API 트리거를 기반으로 전송할 수 있습니다. 자세한 내용은 [캠페인 예약하기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)를 참조하세요.

액션 기반 전달의 경우 캠페인의 기간과 [조용한 시간을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) 설정할 수도 있습니다.

이 단계에서는 사용자가 캠페인을 받을 수 있도록 [다시 자격]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)을 얻을 수 있도록 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 규칙을 활성화하는 등의 전달 제어를 지정할 수 있습니다.

#### 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 [사용자를 타겟팅하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 오디언스의 범위를 좁혀야 합니다. 이미 구독 그룹을 선택했어야 하는데, 이 그룹은 사용자와 소통하고자 하는 수준이나 카테고리에 따라 사용자 범위를 좁혀줍니다. 이 단계에서는 세그먼트에서 더 많은 오디언스를 선택하고 원하는 경우 필터를 사용하여 해당 세그먼트를 더 좁힐 수 있습니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지 보여주는 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

{% alert tip %}
SMS 리타겟팅에 관심이 있으신가요? 자세한 내용은 SMS [리타겟팅 문서를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) 참조하세요.
{% endalert %}

#### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

전환 이벤트는 캠페인의 성공 여부를 측정하는 데 도움이 됩니다. 예를 들어, 다음과 같습니다.

- 지역 타겟팅을 사용하여 사용자의 구매를 최종 목표로 하는 SMS 메시지를 트리거하는 경우, 전환 이벤트를 `Purchase` 로 설정합니다.
- 사용자를 앱으로 유도하려는 경우 전환 이벤트를 `Starts Session` 으로 설정합니다.

특정 사용 사례에 따라 사용자 지정 전환 이벤트를 설정할 수도 있습니다. 창의력을 발휘하여 이 캠페인의 성공을 어떻게 측정하고 싶은지 진지하게 생각해 보세요.

{% endtab %}

{% tab 캔버스 %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 자세한 내용은 캔버스의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대해 설명서의 [캔버스 구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 5단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 제작을 완료한 후에는 세부 정보를 검토하고 테스트한 다음 전송하세요!

다음으로 SMS 캠페인 결과에 액세스하는 방법을 알아보려면 [SMS 리포팅]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/)을 확인하세요.
