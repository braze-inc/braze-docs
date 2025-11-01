---
nav_title: SMS 메시지 만들기
article_title: SMS 메시지 만들기
page_order: 5
description: "이 참조 문서에서는 SMS 메시지를 구축하고 작성하는 단계에 대해 설명합니다."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# SMS 메시지 만들기

> SMS 캠페인은 고객에게 직접 다가가 프로그래밍 방식으로 대화하는 데 유용합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인화된 경험을 만들고 브랜드에 대한 사용자 경험을 촉진하고 향상시키는 환경을 조성할 수 있습니다. 

## 1단계: 메시지 구축 위치 선택하기

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab Campaign %}

**단계:**

1. **메시징** > **캠페인으로** 이동하여 **캠페인 만들기를** 선택합니다.
2. **SMS를** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다.
3. 캠페인 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가합니다.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 구축할 수 있습니다. 예를 들어 [보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 때 특정 태그를 기준으로 필터링할 수 있습니다.
5. 캠페인에 필요한 만큼 배리언트를 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 참조하세요.
6. [구독 그룹을]({{site.baseurl}}/sms_rcs_subscription_groups/) 선택하여 적절한 사용자에게 메시지를 보낼 수 있도록 하세요. 구독 그룹을 선택할 때 Braze는 자동으로 세그먼트화 필터를 추가하여 가입한 사용자만 캠페인을 수신할 수 있도록 합니다. 해당 구독 그룹에 속한 긴 코드와 짧은 코드만 타겟팅 사용자에게 SMS를 보내는 데 사용됩니다.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사를** 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**단계:**

1. 캔버스 작성기를 사용하여 캔버스를 [만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 일정을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 오디언스 옵션은 메시징이 전송되는 시점에 지연이 발생한 후에 확인됩니다.
5. [진행 방식을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: SMS 메시지 작성하기

필요에 따라 언어와 개인화(Liquid, 연결된 콘텐츠, 이모티콘)를 사용하여 메시지를 작성하세요. 초과 요금이 부과될 가능성을 줄이려면 메시지 카피 한도를 준수하세요.

{% alert important %}
계속 진행하기 전에 [SMS 메시지 세그먼트 및 복사 한도에]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) 대한 가이드라인을 읽어보세요. SMS 메시지 세그먼트는 휴대폰 사업자가 문자 메시지를 측정하는 데 사용하는 문자 배치입니다. 메시지는 메시지 세그먼트별로 요금이 부과되므로 메시지가 어떻게 분할되는지 그 뉘앙스를 이해하는 것이 좋습니다.
{% endalert %}

!"라는 메시지와 함께 Braze의 메시지 작성기 "안녕하세요 first_name, 여러분의 성원에 감사드립니다! 매장에 들러 이 SMS를 제시하고 특별 할인 혜택을 받아보는 것은 어떨까요? 답장 중지를 누르면 메시징 수신을 중단할 수 있습니다."]({% image_buster /assets/img/sms_campaign_compose.png %})

### 연락처 카드 추가하기

SMS 메시징에 연락처 카드를 추가하여 고객이 비즈니스 및 연락처 정보를 연락처에 쉽게 추가할 수 있도록 할 수 있습니다. 이러한 카드에 회사 이름, 전화번호, 주소, 이메일, 작은 사진 등의 공통 속성을 지정할 수 있습니다. 자세한 내용은 [연락처 카드에서]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) 확인하세요.

### 팁

#### Liquid 사용

{% raw %}
Liquid를 사용하려는 경우 선택한 개인화에 대한 기본값을 포함해야 수신자의 고객 프로필이 불완전한 경우 이름이나 일관된 문장 대신 빈 입력 안내문 `Hi, !` 이 표시되지 않습니다.
{% endraw %}

#### AI 카피 생성

멋진 카피를 만드는 데 도움이 필요하신가요? [AI 카피라이팅 도]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)우미를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람과 유사한 마케팅 문구를 생성합니다.

\![SMS 작성기의 메시지 필드에 있는 AI 카피라이터 실행 버튼을 클릭합니다.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### 오른쪽에서 왼쪽으로 메시지 만들기

오른쪽에서 왼쪽으로 표시되는 메시징의 최종 모양은 서비스 제공업체가 어떻게 렌더링하느냐에 따라 크게 달라집니다. 최대한 정확하게 오른쪽에서 왼쪽으로 표시되는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 메시지 만들기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) 참조하세요.

## 3단계: 메시지 미리보기 및 테스트하기

Braze는 항상 메시지를 보내기 전에 미리 보고 테스트할 것을 권장합니다. **테스트** 탭으로 전환하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트 SMS를 보내거나 Braze에서 직접 사용자로 메시지를 미리 볼 수 있습니다.

작성기의 테스트 탭에서 SMS 사본 미리보기. 프로필 섹션에서 이름 필드가 "James"로 설정되어 있습니다. 이제 미리보기 섹션에 "안녕하세요 제임스, 여러분의 성원에 감사드립니다!"라는 메시지가 표시됩니다.]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
SMS를 몇 개의 세그먼트로 분할할 수 있는지 테스트하려면 [SMS 세그먼트 계산기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator) 사용하여 카피 길이를 테스트하세요.
{% endalert %}

## 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab Campaign %}

그런 다음 나머지 캠페인을 구축합니다. 다음 섹션에서 도구를 사용하여 SMS 메시지를 구축하는 방법에 대한 자세한 내용을 참조하세요.

#### 전달 일정 또는 트리거 선택

SMS 메시지는 예약된 시간, 동작 또는 API 트리거에 따라 전달될 수 있습니다. 자세한 내용은 [캠페인 예약하기를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 참조하세요.

실행 기반 전달의 경우 캠페인 기간과 조용한 시간을 설정할 수도 있습니다.

이 단계에서는 사용자가 캠페인을 [다시]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) 수신할 수 있도록 허용하거나 [최대 게재빈도]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 설정 규칙을 인에이블하는 등 전달 제어를 지정할 수도 있습니다.

#### 타겟팅할 사용자 선택하기

다음으로 세그먼트 또는 필터를 선택하여 오디언스 범위를 좁혀 [사용자를 타겟팅해야]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) 합니다. 사용자와 소통하고자 하는 수준이나 카테고리에 따라 사용자를 좁혀주는 구독 그룹을 이미 선택하셨을 것입니다. 

{% multi_lang_include target_audiences.md %}

이 단계에서는 세그먼트에서 더 큰 오디언스를 선택하고, 원하는 경우 필터를 사용하여 해당 세그먼트를 더 좁힐 수 있습니다. 현재 대략적인 세그먼트 인구가 어떻게 보이는지 자동으로 미리 볼 수 있습니다. 정확한 세그먼트 멤버십은 항상 메시지 전송 직전에 계산된다는 점에 유의하세요.

{% alert tip %}
SMS 리타겟팅에 관심이 있으신가요? 자세한 내용은 SMS [리타겟팅 문서를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) 참조하세요.
{% endalert %}

#### 전환 이벤트 선택하기

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 액션, [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환이 카운트되는 기간을 최대 30일로 설정할 수 있습니다.

전환 이벤트는 캠페인의 성공 여부를 측정하는 데 도움이 됩니다. 예를 들어

- 지역 타겟팅을 사용하여 사용자의 구매를 최종 목표로 하는 SMS 메시지를 트리거하는 경우 전환 이벤트를 `Purchase` 로 설정합니다.
- 사용자를 앱으로 유도하려는 경우 전환 이벤트를 `Starts Session` 으로 설정하세요.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다. 창의력을 발휘하여 이 캠페인의 성공을 진정으로 측정할 수 있는 방법을 생각해 보세요.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 나머지 캔버스를 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 캔버스 설명서의 캔버스 [구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 5단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 구축을 완료한 후에는 세부 사항을 검토하고 테스트한 다음 전송하세요!

다음으로 SMS 캠페인 결과에 액세스하는 방법을 알아보려면 [SMS 리포팅을]({{site.baseurl}}/sms_mms_rcs_reporting/) 확인하세요.
