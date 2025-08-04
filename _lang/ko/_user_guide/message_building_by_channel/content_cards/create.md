---
nav_title: 콘텐츠 카드 만들기
article_title: 콘텐츠 카드 만들기
page_order: 0
description: "이 참고 문서에서는 Braze 캠페인과 캔버스를 사용하여 콘텐츠 카드를 만들고, 작성하고, 구성하고, 전송하는 방법에 대해 설명합니다."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# 콘텐츠 카드 만들기

> 이 문서에서는 캠페인과 캔버스를 만들 때 Braze에서 콘텐츠 카드를 만드는 방법에 대해 설명합니다. 여기에서는 메시지 유형 선택하기, 카드 작성하기, 메시지 전송 예약하기 등을 안내해 드립니다.

## 1단계: 메시지를 작성할 위치 선택

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일 메시지로 사용자에게 신제품에 대해 알리는 등의 간단한 단일 메시징 캠페인에 적합하며, 캔버스는 시간 경과에 따른 사용자 행동에 따라 맞춤형 제품 제안을 보내는 등의 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab 캠페인 %}

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **콘텐츠 카드를** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가하세요.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어 [보고서 작성기를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 때 관련 태그를 기준으로 필터링할 수 있습니다.
5. 캠페인에 원하는 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 변형에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 이형 상품 **추가** 드롭다운에서 이형 **상품에서 복사를** 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab 캔버스 %}

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 메시지 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. **콘텐츠 카드**를 메시징 채널로 선택합니다.
4. Braze가 콘텐츠 카드에 대한 오디언스 자격 및 개인화를 계산할 시기를 선택합니다. 이는 단계 입력 또는 첫 노출(권장) 시점에 할 수 있습니다. 콘텐츠 카드가 포함된 단계는 예약 또는 액션 기반일 수 있습니다.
5. 사용자가 구매를 완료하거나 사용자 지정 이벤트를 수행할 때 콘텐츠 카드를 제거할지 여부를 선택합니다.
6. 콘텐츠 카드의 만료일(피드 내 시간)을 설정합니다. 이는 일정 기간이 지난 후 또는 특정 시점이 될 수 있습니다.
7. **배달 설정에서** 필요에 따라 이 단계의 대상 또는 수신자를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 오디언스를 더욱 세분화할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 발송되는 시점에 확인됩니다.
8. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: 메시지 유형 지정

세 가지 필수 콘텐츠 카드 유형 중 하나를 선택합니다: **클래식**, **캡션 이미지** 및 **이미지 전용**. 

각 유형의 예상 동작 및 모양에 대해 자세히 알아보려면 [크리에이티브 세부 정보를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) 참조하거나 다음 표의 링크를 확인하세요. 이러한 콘텐츠 카드 유형은 모바일 앱과 웹 애플리케이션 모두에서 사용할 수 있습니다.

| 메시지 유형 | 예시 | 설명 |
|---|---|---|
|[클래식]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![운동 클래스 예약을 권장하는 작은 아이콘과 텍스트가 있는 클래식 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |클래식 카드는 굵은 제목, 메시지 텍스트, 제목과 텍스트 왼쪽에 있는 선택 사항 이미지가 있는 단순한 레이아웃으로 되어 있습니다. 클래식 카드에는 정사각형 이미지나 아이콘을 사용하는 것이 가장 좋습니다. |
|[자막이 있는 이미지]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![역도 선수의 이미지와 운동 수업 예약을 독려하는 텍스트가 담긴 캡션 콘텐츠 카드]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | 캡션 이미지 카드는 카피와 시선을 사로잡는 이미지로 콘텐츠를 소개합니다. |
|[이미지만]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![텍스트만 있는 이미지 전용 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | 이미지 전용 카드는 이미지, GIF 및 기타 창의적인 비텍스트 콘텐츠를 위한 공간으로 주의를 끌 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 3단계: 콘텐츠 카드 작성

메시지 편집기의 **작성** 탭에서 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![메시지 편집기의 작성 탭에서 콘텐츠 카드 세부 정보 샘플을 작성합니다.][24]

여기에 표시되는 내용은 이전 단계에서 선택한 **카드 유형에** 따라 다르지만 다음 옵션 중 하나를 포함할 수 있습니다:

#### 언어

**언어 추가를** 선택하여 제공된 목록에서 원하는 언어를 추가합니다. 이렇게 하면 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)가 메시지에 삽입됩니다. 콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 원하는 위치에 텍스트를 채울 수 있도록 하는 것이 좋습니다. 사용 가능한 전체 언어 목록은 [지원되는 언어를][18] 참조하세요.

![언어에 영어, 스페인어, 프랑스어가 선택되어 있고 국제화할 필드에 제목, 설명, 링크 텍스트가 선택되어 있는 창입니다.][2]{: style="max-width:70%;"}

##### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### 제목 및 메시지

원하는 것은 무엇이든 작성하세요. 제한은 없지만, 메시지를 더 빨리 전달하고 고객의 클릭을 유도할수록 좋습니다! 명확하고 간결한 제목과 메시지 내용을 권장합니다. 이러한 필드는 이미지 전용 카드에는 제공되지 않습니다.

#### 이미지

**이미지 추가를** 선택하거나 이미지 URL을 입력하여 콘텐츠 카드에 이미지를 추가합니다. **이미지 추가를** 선택하면 이전에 업로드한 이미지를 선택하거나 새 이미지를 추가할 수 있는 **미디어 라이브러리가** 열립니다. 메시지 유형과 플랫폼마다 권장 비율과 요구 사항이 다를 수 있으므로 의뢰하거나 이미지를 처음부터 만들기 전에 해당 사항을 확인해야 합니다! 콘텐츠 카드 메시지 필드의 총 크기는 2KB로 제한된다는 점에 유의하세요.

#### 맨 위에 고정

고정 카드는 사용자의 피드 상단에 표시되며 사용자가 지울 수 없습니다. 사용자 피드에 두 개 이상의 카드가 고정된 경우, 고정 카드가 시간순으로 표시됩니다. 카드를 전송한 후에는 고정된 옵션을 소급하여 업데이트할 수 없습니다. 캠페인이 전송된 후 이 옵션을 변경하면 향후 전송에만 영향을 미칩니다.

!["이 카드를 피드 상단에 고정" 옵션을 선택한 상태에서 모바일 및 웹용 Braze의 콘텐츠 카드 미리 보기를 나란히 배치합니다.][1]{:style="border:none"}

#### 클릭 시 동작

고객이 카드에 표시된 링크를 클릭하면 앱으로 더 깊이 들어가거나 다른 사이트로 연결될 수 있습니다. 콘텐츠 카드의 클릭 시 동작을 선택한 경우 **링크 텍스트를** 그에 맞게 업데이트하는 것을 잊지 마세요.

콘텐츠 카드 링크에 대해 수행할 수 있는 작업은 다음과 같습니다:

| 작업 | 설명 |
|---|---|
| 웹 URL로 리디렉션 | 네이티브가 아닌 웹 페이지를 엽니다. |
| [앱으로 딥링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | 앱의 기존 화면으로 딥링크를 연결합니다. |
| 사용자 지정 이벤트 로그 | Choose a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) to trigger. 다른 콘텐츠 카드를 표시하거나 추가 메시지를 트리거하는 데 사용할 수 있습니다. |
| 사용자 지정 속성 로그 | Choose a [custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) to set for the current user. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**참고**: __로그 커스텀 이벤트__ 및 __로그 커스텀 속성__ 옵션을 사용하려면 다음 SDK 버전 호환성이 필요합니다.

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

{% alert warning %}
콘텐츠 카드 메시지 필드의 총 크기는 다음 필드의 바이트 크기 길이를 더하여 계산한 2KB로 제한됩니다. 제목, 메시지, 이미지 URL, 링크 텍스트, 링크 URL 및 키-값 쌍(이름 + 값). 이 크기를 초과하는 메시지는 전송되지 않습니다. 여기에는 이미지의 크기가 포함되지 않고 이미지 URL의 길이가 포함된다는 점에 유의하세요.
{% endalert %}

{% alert warning %}
각 사용자는 언제든지 피드에 만료되지 않은 콘텐츠 카드를 최대 250개까지 보유할 수 있습니다. 이 한도를 초과하면 읽지 않은 카드라도 가장 오래된 카드의 반환이 중지됩니다. 해지된 카드도 이 250개 카드 한도에 포함되므로 해지된 카드가 많으면 새 카드를 만들 수 있는 공간이 줄어들 수 있습니다.
{% endalert %}

## 4단계: 추가 설정 구성(선택 사항)

[키-값 쌍을][19] 사용하여 카드의 카테고리를 만들고, [여러 개의 콘텐츠 카드 피드를]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) 만들고, 카드 정렬 방식을 사용자 지정할 수 있습니다.

메시지에 키-값 쌍을 추가하려면 **설정** 탭으로 이동하여 **새 쌍 추가를** 선택합니다.

## 5단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab 캠페인 %}

나머지 캠페인을 구축하세요. 다음 섹션에서 도구를 가장 효과적으로 사용하여 콘텐츠 카드를 만드는 방법에 대한 자세한 내용을 계속 살펴보세요.

#### 배송 일정 또는 트리거 선택

콘텐츠 카드는 예약된 시간, 동작 또는 API 트리거에 따라 전달할 수 있습니다. 자세한 내용은 [캠페인 일정 잡기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)을 참조하세요.

캠페인의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)을 설정하고 콘텐츠 카드의 만료일을 결정할 수도 있습니다. 특정 만료일 또는 카드 만료일까지의 일수를 최대 30일까지 설정할 수 있습니다. 모든 이형 상품의 만료 날짜는 동일합니다.

{% alert note %}
콘텐츠 카드에는 횟수 제한이 적용되지 않습니다.
{% endalert %}

##### 예약 배송

전달이 예약된 콘텐츠 카드 캠페인의 경우, 카드 생성 시점을 지정하여 Braze가 새 콘텐츠 카드 캠페인에 대한 오디언스 자격 및 개인화 평가 시점을 선택할 수 있습니다. 자세한 내용은 [카드 만들기]({{site.baseurl}}/card_creation)를 참조하세요.

#### 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 [사용자를 타겟팅하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 오디언스의 범위를 좁힙니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

#### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

{% endtab %}

{% tab 캔버스 %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 캔버스의 나머지 부분을 구성하고, [다변량 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 및 [지능형 선택을]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 구현하는 방법 등에 대한 자세한 내용은 캔버스 문서의 캔버스 [구성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 6단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 제작을 완료한 후에는 세부 사항을 검토하고 [테스트한]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/) 다음 준비가 되면 전송하세요.

{% alert warning %}
콘텐츠 카드가 실행된 후에는 편집할 수 없습니다. 새 사용자에게만 전송을 중지하고 사용자의 피드에서 삭제할 수 있습니다. 이 시나리오에 접근하는 방법을 이해하려면 [보낸 카드 업데이트하기]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards)를 참조하세요.
{% endalert %}

다음으로 [콘텐츠 카드 보고]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/)를 확인하여 콘텐츠 카드 캠페인 결과에 액세스하는 방법을 알아보세요.

## 알아두어야 할 사항

### 전송 동작

콘텐츠 카드가 전송된 후에는 사용자에게 전달될 준비가 된 '받은 편지함'에서 대기합니다(이메일의 경우와 유사). 콘텐츠가 콘텐츠 카드로 가져온 후에는(표시 시점에) 콘텐츠의 수명 기간 동안 콘텐츠를 변경할 수 없습니다. 이는 커넥티드 콘텐츠를 통해 API를 호출하는 경우 엔드포인트의 데이터가 변경되는 경우에도 적용됩니다. 이 데이터는 업데이트되지 않습니다. 새 사용자에게만 전송을 중지하고 사용자의 피드에서 삭제할 수 있습니다. 캠페인을 수정하면 향후 전송되는 카드에만 업데이트가 적용됩니다.

오래된 카드를 제거해야 하는 경우 먼저 캠페인을 중지해야 합니다. 캠페인을 중지하려면 콘텐츠 카드 캠페인을 열고 **캠페인 중지**를 선택합니다. 캠페인을 중지하면 이미 카드를 받은 사용자를 어떻게 처리할지 결정하라는 메시지가 표시됩니다. 

사용자의 피드에서 콘텐츠 카드를 제거하려면 **피드에서 카드 제거를** 선택합니다. 그러면 다음 동기화 시 SDK에 의해 카드가 숨겨집니다.

![콘텐츠 카드 비활성화를 확인하는 대화 상자][25]{: style="max-width:75%" }

{% alert tip %}
콘텐츠 카드가 최대 30일보다 더 오래 지속되는 것처럼 보이기를 원하시나요? 이를 수행하는 한 가지 방법은 다음을 수행하는 것입니다:<br><br>

1. 콘텐츠 카드의 기간을 30일로 설정합니다.
2. 캠페인 재적격성을 30일로 설정합니다.
3. "세션 시작" 시 캠페인이 트리거되도록 설정합니다.
{% endalert %}

### 카드 제거 이벤트 {#action-based-card-removal}

일부 콘텐츠 카드는 사용자가 특정 작업을 수행할 때까지만 관련성이 있습니다. 예를 들어, 사용자가 온보딩 작업을 완료한 후에는 계정을 활성화하도록 유도하는 카드가 표시되지 않아야 합니다.

캠페인 또는 캔버스 메시지 내에서 선택적으로 **제거 이벤트를** 추가하여 이전에 전송된 카드가 해당 사용자의 피드에서 제거되도록 하는 사용자 지정 이벤트 또는 구매를 SDK 또는 REST API에 의해 트리거되도록 지정할 수 있습니다.

{% alert tip %}
사용자 피드에서 카드를 제거해야 하는 여러 사용자 지정 이벤트 및 구매를 지정할 수 있습니다. 사용자가 이러한 작업을 수행하면 캠페인의 카드가 전송한 기존 카드가 **모두** 제거됩니다. 향후 적격 카드는 메시지 일정에 따라 계속 발송됩니다.
{% endalert %}

![콘텐츠 카드 제거 이벤트 옵션이 있는 콘텐츠 카드 제거 조건 패널]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### 출시된 카드 업데이트

콘텐츠 카드는 전송된 후에는 편집할 수 없습니다. 이미 전송된 카드를 변경해야 하는 경우 다음 옵션에 표시된 대로 [캠페인 재적격성을]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) 사용하는 것이 좋습니다.

{% alert note %}
When a Content Card becomes re-eligible, it may be sent again when the original card is still in a user's app. To avoid duplicate cards in a user's app, you can turn off re-eligibility or extend the re-eligibility window so that users won't be sent a new card until the original has expired.
{% endalert %}

Also note that Content Cards using [at first impression]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) use impression time to calculate re-eligibility. However, Content Cards created at campaign launch or Canvas step entry use whichever send time or impression time is latest.

#### 옵션 1: 캠페인 복제하기

한 가지 방법은 캠페인을 아카이브하고 피드에서 활성 카드를 제거하는 것입니다. 그런 다음 캠페인을 복제하고 업데이트와 함께 캠페인을 시작하여 모든 적격 사용자가 업데이트된 카드를 받을 수 있도록 할 수 있습니다.

* 사용자가 콘텐츠 카드를 다시 받을 수 없는 경우 `Received Message from Campaign` 필터를 `Has Not` 조건으로 설정하여 이전 버전의 콘텐츠 카드를 받지 않은 사용자를 필터링할 수 있습니다.
* 이전 카드를 받은 사용자가 X일 이내에 다시 자격을 얻어야 하는 경우 `Last Received Message from specific campaign` 필터를 X일 이상으로 **설정하거나** `Received Message from Campaign` 조건으로 `Has Not` 필터를 설정할 수 있습니다.

##### 사용 사례

세션 시작 시 캠페인이 트리거되도록 설정하고 재자격이 30일로 설정되어 있다고 가정해 보겠습니다. 사용자가 이틀 전에 캠페인을 받았는데 사본을 변경하려고 합니다. 먼저 캠페인을 아카이브하고 피드에서 카드를 제거합니다. 둘째, 캠페인을 복제하고 새 카피로 다시 실행합니다. 사용자에게 다른 세션이 있는 경우 즉시 새 카드를 받게 됩니다.

##### 효과

* **보고:** 카드의 각 버전에는 별도의 분석 기능이 있습니다.
* **기존 수신자:** 신규 및 기존 수신자가 자격을 갖춘 경우 다음 피드 새로 고침 시 업데이트된 카드를 볼 수 있습니다.

{% alert tip %}
카드의 최신 콘텐츠를 표시하는 메시지(예: 홈페이지 배너), 변경 사항을 즉시 표시해야 하는 경우 또는 재자격이 꺼져 있는 경우에 이 옵션을 사용하는 것이 좋습니다.
{% endalert %}

#### 옵션 2: 중지 및 재시작

카드에 재적격성이 설정되어 있는 경우 이를 선택할 수 있습니다.

1. 캠페인을 중지합니다.
2. 사용자의 피드에서 활성 콘텐츠 카드를 제거합니다.
3. 필요에 따라 캠페인을 수정합니다.
4. 캠페인을 다시 시작합니다.

이 접근 방식을 사용하면 새로 자격을 갖춘 사용자는 새 카드를 받게 되고, 이전 수령자는 자격을 다시 갖추게 되면 새 카드를 받게 됩니다.

##### 사용 사례

세션 시작에 의해 트리거되고 재자격이 30일로 설정된 캠페인이 있다고 가정해 보겠습니다. 사용자가 이틀 전에 캠페인을 받았는데 사본을 변경하려고 합니다. 먼저 캠페인을 중지하고 피드에서 카드를 제거합니다. 둘째, 새 카피로 캠페인을 다시 게시합니다. 다른 세션이 있는 사용자의 경우 28일 후에 새 카드를 받게 됩니다.

##### 효과

* **보고:** 하나의 캠페인에는 출시된 카드 버전에 대한 모든 보고 분석이 포함됩니다. Braze는 출시된 버전을 구분하지 않습니다.
* **기존 수신자:** 이미 카드를 받은 사용자는 다시 자격을 갖추기 전까지는 업데이트된 카드를 받을 수 없습니다. 재적격성이 해제되면 새 카드를 받을 수 없습니다.

{% alert tip %}
알림 센터 또는 메시지 받은 편지함의 고유 메시지(예: 프로모션)에 이 옵션을 사용하는 것이 좋으며, 분석의 통합이 중요하거나 메시지의 적시성이 문제가 되지 않는 경우(예: 기존 수신자가 업데이트된 카드를 보기 전에 자격 기간을 기다릴 수 있는 경우) 이 옵션을 사용하는 것이 좋습니다.
{% endalert %}

#### 사용자 피드에 카드 보관

원하는 경우 사용자의 피드에서 활성 콘텐츠 카드 캠페인을 제거하지 않고 계속 유지할 수 있습니다. 라이브 캠페인이 편집되면 편집되지 않은 이전 버전의 캠페인 카드가 계속 라이브 상태로 유지되며, 편집 후 기준을 충족하는 사용자만 새 버전을 볼 수 있습니다. 그러나 이미 캠페인에 노출된 사용자에게는 두 가지 버전의 카드가 표시될 수 있습니다.

[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img/content_card_compose.png %}
[25]: {% image_buster /assets/img/cc_remove.png %}
[1]: {% image_buster /assets/img/cc_pin_to_top.png %}
[2]: {% image_buster /assets/img/add_languages.png %}
