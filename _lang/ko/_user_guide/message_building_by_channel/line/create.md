---
nav_title: LINE 메시지 만들기
article_title: LINE 메시지 만들기
page_order: 1
description: "이 문서에서는 LINE 메시지 캠페인 또는 캔버스를 만드는 방법에 대해 설명합니다."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# LINE 메시지 만들기

> LINE 캠페인은 고객에게 직접 다가가 프로그래밍 방식으로 채팅할 수 있습니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인적인 경험을 만들고 브랜드에 대한 사용자 경험을 방해하지 않는 환경을 조성하고 향상시킬 수 있습니다.

## 필수 조건

LINE 메시지를 작성하기 전에 다음을 수행합니다:

1. LINE 개요를 읽어보세요.
2. 정책, 제한 및 콘텐츠 규칙을 확인합니다.
3. [LINE 연결을 설정합니다]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

Braze에서 LINE 메시지를 보내면 계정의 메시지 크레딧이 차감됩니다.

## 1단계: 메시지를 작성할 위치 선택

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab 캠페인 %}

**단계:**

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **LINE**을 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널 캠페인을** 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다.
5. 캠페인에 필요한 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

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

## 2단계: LINE 메시지 작성하기

필요에 따라 개인화(예: 리퀴드 또는 커넥티드 콘텐츠)를 사용하여 메시지를 작성합니다. LINE에서는 각 메시지에 텍스트, 이미지, 리치, 카드 기반 등 사용 가능한 메시지 레이아웃 중 하나를 선택해 최대 5개의 말풍선을 넣을 수 있습니다.

![LINE composer with a message displayed in the preview.]({% image_buster /assets/img/line/line_composer.png %})

### Tips

#### Using Liquid

Liquid를 사용하려는 경우 개인화에 대한 기본값을 포함해야 합니다. 이렇게 하면 고객 프로필이 불완전한 수신자가 빈 입력 안내를 받는 것을 방지할 수 있습니다. 예를 들어 사용자가 "안녕하세요, !"라는 메시지를 받는 대신 "안녕하세요, 신규 구독자 여러분!"이라는 메시지를 받을 수 있습니다.

#### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## 3단계: 메시지 미리보기 및 테스트

**테스트** 탭으로 전환하여 콘텐츠 테스트 그룹 또는 개별 사용자에게 테스트 LINE 메시지를 보내거나 Braze에서 직접 사용자로 메시지를 미리 볼 수 있습니다.

![The "Tests" tab displaying a preview of a test message.]({% image_buster /assets/img/line/test_preview.png %})

## 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab 캠페인 %}

나머지 캠페인을 구축하세요. 다음 섹션에서 LINE의 도구를 사용하여 메시지를 작성하는 방법에 대해 자세히 알아보세요.

### 배송 일정 또는 트리거 선택

LINE 메시지는 예약된 시간, 동작 또는 API 트리거에 따라 전송할 수 있습니다. 예약 및 트리거 옵션에 대한 자세한 내용은 [캠페인 예약하기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)를 참조하세요.

사용자가 캠페인을 [다시]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) 수신할 수 있도록 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 규칙을 설정하는 등 전달 제어를 지정할 수 있습니다. 액션 기반 전달의 경우 캠페인의 기간과 [조용한 시간을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) 설정할 수도 있습니다.

### 타겟팅할 사용자 선택

[Target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow down your audience. 이미 구독 그룹을 선택했어야 하는데, 이 그룹은 사용자와 소통하고자 하는 수준이나 카테고리에 따라 사용자 범위를 좁혀줍니다. 

세그먼트에서 더 많은 오디언스를 선택하고 [필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)를 사용하여 해당 세그먼트를 더 좁힐 수 있습니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

전환 이벤트는 캠페인의 성공 여부를 측정하는 데 도움이 됩니다. 예를 들어, 다음과 같습니다.

- 지역 타겟팅을 사용하여 사용자의 구매를 최종 목표로 하는 LINE 메시지를 트리거하는 경우, 전환 이벤트를 `Purchase` 로 설정합니다.
- 사용자를 앱으로 유도하려는 경우 전환 이벤트를 `Starts Session` 으로 설정합니다.

특정 사용 사례에 따라 사용자 지정 전환 이벤트를 설정할 수도 있습니다. 창의력을 발휘하여 캠페인의 성공을 어떻게 측정할지 생각해 보세요.

{% endtab %}
{% tab 캔버스 %}

아직 완료하지 않았다면 캔버스의 나머지 섹션을 완성하세요. 캔버스의 나머지 구성, 다변량 테스트 및 지능형 선택 등을 사용하는 방법에 대한 자세한 내용은 [캔버스 만들기]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)를 참조하세요.

{% endtab %}
{% endtabs %}

## 5단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 제작을 완료한 후에는 세부 정보를 검토하고 테스트한 다음 전송하세요!

다음으로 [LINE 리포팅을]({{site.baseurl}}/line/reporting/) 통해 LINE 캠페인의 결과에 액세스하는 방법을 알아보세요.


