---
nav_title: 콘텐츠 카드 만들기
article_title: 콘텐츠 카드 만들기
page_order: 0
description: "This reference article covers how to create, compose, configure, and send Content Cards using Braze campaigns and Canvases."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# 콘텐츠 카드 만들기

> 이 문서에서는 캠페인과 캔버스를 구축할 때 Braze에서 콘텐츠 카드를 만드는 방법을 다룹니다. 여기에서는 메시징 유형 선택, 카드 작성 및 메시지 전달 예약 과정을 안내합니다.

## 1단계: 메시지를 작성할 위치 선택

단일, 간단한 메시징(예: 하나의 메시지로 제품에 대해 사용자에게 알리기)에 캠페인을 사용하세요. 다단계 사용자 여정(예: 시간에 따라 사용자 행동에 기반한 맞춤형 제품 제안 전송)에 캔버스를 사용하세요.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **콘텐츠 카드를** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가하세요.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)를 사용할 때 관련 태그로 필터링할 수 있습니다.
5. 캠페인에 원하는 만큼의 변형을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 변형에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 **변형에서 복사**를 **변형 추가** 드롭다운에서 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에 메시지 단계를 추가하세요. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. **콘텐츠 카드**를 메시징 채널로 선택합니다.
4. Braze가 콘텐츠 카드에 대한 오디언스 자격 및 개인화를 계산할 시기를 선택합니다. 이는 단계 입력 또는 첫 노출(권장) 시점에 할 수 있습니다. 콘텐츠 카드가 포함된 단계는 예약 또는 액션 기반일 수 있습니다.
5. 사용자가 구매를 완료하거나 사용자 지정 이벤트를 수행할 때 콘텐츠 카드를 제거할지 여부를 선택합니다.
6. 콘텐츠 카드의 만료일(피드 내 시간)을 설정합니다. 이는 일정 기간이 지난 후 또는 특정 시점이 될 수 있습니다.
7. 필요에 따라 이 단계의 청중 또는 수신자를 **전달 설정**에서 필터링하세요. 세그먼트를 지정하고 추가 필터를 추가하여 청중을 더욱 세분화할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 발송되는 시점에 확인됩니다.
8. 메시지와 함께 쌍을 이루고 싶은 다른 메시징 채널을 선택하세요.

{% endtab %}
{% endtabs %}

## 2단계: 메시지 유형 지정

세 가지 필수 콘텐츠 카드 유형 중 하나를 선택하세요: **클래식**, **자막 이미지**, 및 **이미지 전용**. 

각 유형의 예상 동작 및 모양에 대한 자세한 내용은 [크리에이티브 세부정보]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/)를 참조하거나 다음 표의 링크를 확인하세요. 이러한 콘텐츠 카드 유형은 모바일 앱과 웹 애플리케이션 모두에서 사용할 수 있습니다.

| 메시지 유형 | 예시 | 설명 |
|---|---|---|
|[클래식]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![작은 아이콘과 텍스트가 포함된 클래식 콘텐츠 카드로, 운동 수업 예약을 장려합니다.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |클래식 카드는 제목, 메시지 텍스트 및 제목과 텍스트 왼쪽에 위치한 선택적 이미지가 있는 간단한 레이아웃을 가지고 있습니다. 클래식 카드에는 정사각형 이미지나 아이콘을 사용하는 것이 가장 좋습니다. |
|[자막이 있는 이미지]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![웨이트리프터의 이미지와 운동 수업 예약을 장려하는 텍스트가 포함된 자막 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | 자막 이미지 카드는 복사 및 주목을 끄는 이미지로 콘텐츠를 보여줍니다. |
|[이미지만]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![텍스트만 포함된 이미지 전용 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | 이미지 전용 카드는 이미지, GIF 및 기타 창의적인 비텍스트 콘텐츠를 위한 공간으로 주목을 끌고 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 3단계: 콘텐츠 카드 작성

메시지 편집기의 **작성** 탭에서 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![메시지 편집기의 작성 탭에서 샘플 콘텐츠 카드 세부정보를 확인하세요.]({% image_buster /assets/img/content_card_compose.png %})

여기에 표시되는 내용은 이전 단계에서 선택한 **카드 유형에** 따라 다르지만 다음 옵션 중 하나를 포함할 수 있습니다:

#### Language

원하는 언어를 제공된 목록에서 추가하려면 **언어 추가**를 선택하세요. 이렇게 하면 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)가 메시지에 삽입됩니다. 콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 원하는 위치에 텍스트를 채울 수 있도록 하는 것이 좋습니다. For our full list of available languages you can use, refer to [Languages supported]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![영어, 스페인어 및 프랑스어가 언어로 선택된 창과 제목, 설명 및 링크 텍스트가 국제화할 필드로 선택된 창입니다.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### 제목 및 메시지

원하는 것은 무엇이든 작성하세요. 제한은 없지만, 메시지를 빠르게 전달하고 고객이 클릭하도록 유도할수록 더 좋습니다! 명확하고 간결한 제목과 메시지 내용을 권장합니다. 이 필드는 이미지 전용 카드에는 제공되지 않음을 유의하세요.

#### 이미지

**이미지 추가**를 선택하거나 이미지 URL을 제공하여 콘텐츠 카드에 이미지를 추가하세요. **이미지 추가**를 선택하면 **미디어 라이브러리**가 열리며, 여기에서 이전에 업로드한 이미지를 선택하거나 새 이미지를 추가할 수 있습니다. 각 메시지 유형과 플랫폼은 고유한 비율과 요구 사항이 있을 수 있으므로, 이미지를 의뢰하거나 처음부터 만들기 전에 그것들이 무엇인지 확인하세요! 콘텐츠 카드 메시지 필드는 총 크기가 2KB로 제한된다는 점을 기억하세요.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### 맨 위에 고정

Braze는 사용자의 피드 상단에 고정 카드를 표시하며 사용자는 이를 해제할 수 없습니다. 사용자의 피드에 여러 개의 고정 카드가 있는 경우, Braze는 이를 시간순으로 정렬합니다. 카드를 보낸 후에는 고정 옵션을 소급하여 업데이트할 수 없습니다. 캠페인을 보낸 후 이 옵션을 변경하면 향후 전송에만 영향을 미칩니다.

!["이 카드를 피드 상단에 고정" 옵션을 선택한 상태에서 모바일 및 웹용 Braze의 콘텐츠 카드 미리 보기를 나란히 배치합니다.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### 클릭 시 동작

고객이 카드에 표시된 링크를 클릭하면 앱으로 더 깊이 들어가거나 다른 사이트로 연결될 수 있습니다. 콘텐츠 카드에 클릭 시 동작을 선택하는 경우, **링크 텍스트**를 적절히 업데이트하는 것을 잊지 마세요.

The following actions are available for Content Card links:

| Action | 설명 |
|---|---|
| 웹 URL로 리디렉션 | 네이티브가 아닌 웹 페이지를 엽니다. |
| [앱으로 딥링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | 앱의 기존 화면으로 딥링크를 연결합니다. |
| 사용자 지정 이벤트 로그 | Choose a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) to trigger. 다른 콘텐츠 카드를 표시하거나 추가 메시지를 트리거하는 데 사용할 수 있습니다. |
| 사용자 지정 속성 로그 | Choose a [custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) to set for the current user. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The **Log Custom Event** and **Log Custom Attribute** options require the following SDK version compatibility:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## 4단계: 추가 설정 구성(선택 사항)

You can use [key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) to create categories for your Cards, create [multiple Content Card feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds), and customize how cards are sorted.

메시지에 키-값 쌍을 추가하려면 **설정** 탭으로 이동하여 **새 쌍 추가**를 선택하세요.

## 5단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab Campaign %}

나머지 캠페인을 구축하세요. 콘텐츠 카드를 구축하기 위해 도구를 최적으로 사용하는 방법에 대한 추가 세부정보는 다음 섹션으로 계속하세요.

#### Choose a delivery schedule or trigger

콘텐츠 카드는 예약된 시간, 행동 또는 API 트리거에 따라 전달될 수 있습니다. 자세한 내용은 [캠페인 일정 잡기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)을 참조하세요.

캠페인의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)을 설정하고 콘텐츠 카드의 만료일을 결정할 수도 있습니다. 특정 만료일 또는 카드 만료일까지의 일수를 최대 30일까지 설정할 수 있습니다. 모든 이형 상품의 만료 날짜는 동일합니다.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

##### 예약 배송

전달이 예약된 콘텐츠 카드 캠페인의 경우, 카드 생성 시점을 지정하여 Braze가 새 콘텐츠 카드 캠페인에 대한 오디언스 자격 및 개인화 평가 시점을 선택할 수 있습니다. 자세한 내용은 [카드 만들기]({{site.baseurl}}/card_creation)를 참조하세요.

#### 타겟팅할 사용자 선택

다음으로, [대상 사용자]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/)를 선택하여 세그먼트나 필터를 선택하여 오디언스를 좁히세요. 해당 세그먼트 인구가 대략적으로 어떻게 보이는지 미리보기를 자동으로 받습니다. 메시지 전송 전에 정확한 세그먼트 멤버십이 항상 계산된다는 점을 기억하세요.

{% multi_lang_include target_audiences.md %}

#### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 캔버스를 구축하는 방법에 대한 자세한 내용은 [다변량 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 및 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 등을 구현하고, [캔버스를 구축하세요]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계의 설명서를 참조하세요.

{% endtab %}
{% endtabs %}

## 6단계: 검토 및 배포

캠페인 또는 캔버스의 마지막을 구축한 후, 세부 정보를 검토하고, [테스트하세요]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), 준비가 되면 전송하세요.

{% alert warning %}
콘텐츠 카드가 실행된 후에는 편집할 수 없습니다. 새 사용자에게만 전송을 중지하고 사용자의 피드에서 삭제할 수 있습니다. 이 시나리오에 접근하는 방법을 이해하려면 [보낸 카드 업데이트하기]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards)를 참조하세요.
{% endalert %}

다음으로 [콘텐츠 카드 보고]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/)를 확인하여 콘텐츠 카드 캠페인 결과에 액세스하는 방법을 알아보세요.

## 알아두어야 할 사항

### 페이로드 및 피드 제한

성능을 지원하기 위해 콘텐츠 카드는 두 가지 주요 제약 조건이 있습니다: 각 카드의 페이로드 크기 제한과 피드에 나타날 수 있는 카드의 최대 수입니다.

#### 콘텐츠 카드의 크기 제한

단일 콘텐츠 카드의 전체 데이터 페이로드는 2 KB를 초과할 수 없습니다 **이후** 모든 Liquid 개인화가 렌더링됩니다. This includes:

* 제목
* 메시지
* 이미지 URL (URL 문자열 자체의 길이, 이미지 파일 크기가 아님)
* 링크 텍스트
* 모든 지정된 플랫폼에 대한 링크 URL (iOS, Android 및 웹에 대한 별도의 URL 모두 총계에 포함됨)
* 키-값 쌍 (키 이름과 값 모두)

Liquid를 사용하여 긴 문자열의 텍스트를 가져오는 것은 (커스텀 속성에서와 같이) 제한을 초과할 수 있습니다. 

캠페인 작성기는 정적 콘텐츠가 제한을 초과하면 경고를 표시합니다. (Liquid를 사용하여 동적 콘텐츠의 크기를 예측하지 않습니다.) **메시지 크기가 2 KB를 초과하면 전송 시 중단됩니다.** 이러한 중단은 메시지 활동 로그에서 이유 `Content card maximum size exceeded`와 함께 확인할 수 있습니다.

{% alert important %}
테스트 전송 중, 2 KB를 초과하는 콘텐츠 카드는 여전히 전달되고 제대로 표시될 수 있습니다.
{% endalert %}

콘텐츠 카드 페이로드 크기를 관리하기 위한 몇 가지 모범 사례는 다음과 같습니다:

* 긴 링크에 URL 단축기를 사용하세요. URL, 특히 광범위한 추적 매개변수가 있는 URL은 크기 제한 문제에 직면할 수 있습니다. URL 단축 서비스를 사용하면 문자 수를 극적으로 줄이고 페이로드의 공간을 확보할 수 있습니다.
* Liquid로 동적 콘텐츠를 잘라냅니다. 사용자 속성 또는 API 호출에서 동적 텍스트로 카드를 개인화할 때 콘텐츠의 길이는 예측할 수 없습니다. 동적 텍스트의 길이를 제한하기 위해 `truncate`과 같은 Liquid 필터를 적극적으로 사용하세요.
* 다중 플랫폼 URL을 효율적으로 사용하세요. 2 KB 제한에는 정의한 모든 플랫폼의 URL이 포함됩니다. 각 플랫폼에 대해 길고 고유한 URL을 사용하면 페이로드의 크기가 증가할 수 있습니다. 가능하다면 모든 플랫폼에서 작동하는 단일 링크를 사용하거나 필요에 따라 URL 단축기를 사용하세요.
* 더 풍부한 콘텐츠를 위해 배너를 고려하세요. 일관되게 많은 양의 콘텐츠가 필요한 사용 사례의 경우, 콘텐츠 카드가 적합한 채널이 아닐 수 있습니다. 배너는 동일한 2 KB 페이로드 제한이 없으며 앱이나 웹사이트 경험에 풍부한 콘텐츠를 직접 삽입하는 데 더 적합합니다.

#### Number of cards in feed

각 사용자는 언제든지 피드에 만료되지 않은 콘텐츠 카드를 최대 250개까지 보유할 수 있습니다. 이 한도를 초과하면 읽지 않은 카드라도 가장 오래된 카드의 반환이 중지됩니다. 해지된 카드도 이 제한에 포함되므로 해지된 카드가 많으면 이전 카드에 사용할 수 있는 공간이 줄어듭니다.

카드 제한 문제를 방지하기 위해 다음의 모범 사례를 권장합니다:

- **짧은 만료 날짜 사용:** 시간에 민감한 캠페인(예: 주말 세일)의 경우 특정 만료 날짜를 설정하세요. 이렇게 하면 카드가 피드에서 자동으로 제거되고 더 이상 관련이 없을 때 제한에 포함되지 않습니다.
- **행동 기반 제거 활용:** 거래 또는 목표 기반 카드에 대한 제거 이벤트를 설정하세요. 예를 들어, 사용자가 프로필을 완료하도록 유도하는 카드는 `profile_completed` 이벤트가 기록되는 즉시 제거되어야 합니다.
- **장기 캠페인 감사:** 반복적이거나 진행 중인 캠페인을 검토하여 시간이 지남에 따라 사용자 피드를 너무 많은 카드로 채우지 않도록 poor experience를 만들지 않도록 하세요.

### 콘텐츠 카드에 대한 재자격 이해하기

재자격은 사용자가 동일한 캠페인으로부터 메시지를 여러 번 받을 수 있는지 여부와 시점을 결정합니다. 콘텐츠 카드의 경우, 이것이 어떻게 작동하는지를 이해하는 것은 반복 캠페인을 관리하고 사용자가 중복되거나 오래된 메시지를 받지 않도록 하는 데 중요합니다.

{% alert tip %}
귀하의 콘텐츠가 30일 이상 지속되기를 원하십니까? [배너]({{site.baseurl}}/user_guide/message_building_by_channel/banners)를 시도해 보세요.
{% endalert %}

#### 재자격이 계산되는 방법

재자격을 활성화하면 사용자가 캠페인에 "재진입"할 수 있는 시점의 카운트다운이 메시지가 전송된 후 시작됩니다. 이 카운트다운이 시작되는 특정 순간은 카드 생성 설정에 따라 다릅니다:

* [첫 번째 노출에서]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) 사용하는 콘텐츠 카드는 재자격을 계산하기 위해 노출 시간을 사용합니다.
* 캠페인 시작 또는 캔버스 단계 진입 시 생성된 콘텐츠 카드는 가장 최신의 전송 시간 또는 노출 시간을 사용합니다.

#### 30일 만료 및 재자격

혼란의 일반적인 원인은 캠페인 재자격과 모든 콘텐츠 카드의 자동 30일 만료 간의 상호작용입니다. 

모든 콘텐츠 카드는 전송되거나 제거된 후 30일이 지나면 Braze의 시스템에서 자동으로 삭제됩니다. 재자격이 **비활성화**된 상태에서 장기 실행되는 반복 캠페인이 있는 경우, 사용자는 여전히 30일 후에 동일한 카드를 다시 받을 수 있습니다. 원래 카드가 삭제되면 시스템은 해당 사용자가 캠페인을 받은 기록을 더 이상 보지 않으므로 다음 세션에서 다시 자격이 부여됩니다. 

사용자가 특정 캠페인으로부터 메시지를 한 번만 받도록 하려면, 이 캠페인으로부터 메시지를 받지 않은 사용자에 대해 캠페인 또는 캔버스 단계에 오디언스 필터를 추가하세요. 이 필터는 장기 실행 캠페인에서 중복 전송을 방지하는 가장 신뢰할 수 있는 방법입니다.

### 실시간 콘텐츠 카드 관리

콘텐츠 카드가 전송된 후, 사용자를 위해 배달될 준비가 된 "받은편지함"에서 대기합니다(이메일에서 발생하는 것과 유사합니다). After content is pulled into the Content Card (at the time of display), it cannot be changed during its lifespan. 이것은 연결된 콘텐츠를 통해 API를 호출하고 엔드포인트의 데이터가 변경되더라도 적용됩니다. 이 데이터는 업데이트되지 않습니다. 새 사용자에게만 전송을 중지하고 사용자의 피드에서 삭제할 수 있습니다. 캠페인을 수정하면 향후 전송되는 카드에만 업데이트가 적용됩니다.

#### 출시된 카드 업데이트

이미 카드를 받은 사용자에게 카드를 변경하려면 다음 방법 중 하나를 사용해야 합니다:

##### Option 1: 캠페인을 복제합니다(즉각적인 변경을 권장).

{% alert tip %}
카드에서 최신 콘텐츠를 보여주고 즉시 변경 사항을 표시해야 하거나 재자격이 꺼져 있을 때 이 옵션을 권장합니다.
{% endalert %}

첫 번째 접근 방식은 캠페인을 아카이브하고 새로 복제된 캠페인을 시작하는 것입니다:

1. 원래 캠페인을 중지하고, 프롬프트가 표시되면 `Remove card after the next sync`을 선택합니다.
2. 캠페인을 복제하고, 편집한 후 새 버전을 시작합니다.

캠페인을 복제할 때 새 버전의 오디언스를 정의해야 합니다. 세분화 필터를 사용하여 업데이트된 카드를 받는 대상을 제어합니다:
* 사용자가 콘텐츠 카드의 이전 버전을 받지 않은 경우, 필터 `Received Message from Campaign`을 `Has Not` 조건으로 설정하여 필터링할 수 있습니다.
* 이전 카드를 받은 사용자가 X일 이내에 다시 자격을 얻어야 하는 경우 `Last Received Message from specific campaign` 필터를 X일 이상으로 **설정하거나** `Received Message from Campaign` 조건으로 `Has Not` 필터를 설정할 수 있습니다.

###### 효과

* **기존 수신자:** 신규 및 기존 수신자가 자격을 갖춘 경우 다음 피드 새로 고침 시 업데이트된 카드를 볼 수 있습니다.
* **보고:** 카드의 각 버전에는 별도의 분석 기능이 있습니다.

Let's say you've set a campaign to be triggered by a session start, and it has re-eligibility set to 30 days. 사용자가 이틀 전에 캠페인을 받았는데 사본을 변경하려고 합니다. First, you'd archive the campaign and remove the cards from the feed. 둘째, 캠페인을 복제하고 새 복사본으로 다시 시작합니다. 사용자가 다른 세션을 가지고 있다면, 즉시 새 카드를 받게 됩니다.

##### Option 2: 같은 캠페인을 중지하고 다시 시작합니다.

{% alert tip %}
We recommend using this option for unique messages in a notification center or message inbox (such as promotions), when it’s important for analytics to be unified, or when the timeliness of the message isn't a concern (such as existing recipients can wait for the eligibility window before seeing the updated cards).
{% endalert %}

이 접근 방식은 모든 분석을 단일 캠페인에 통합합니다. 새로 자격이 생긴 사용자는 새 카드를 받지만, 기존 수신자에 대한 업데이트는 재자격이 생길 때까지 지연됩니다:

1. 캠페인을 중지하고, 프롬프트가 표시되면 **다음 동기화 후 카드 제거**을 선택합니다.
2. 필요에 따라 캠페인을 수정합니다.
3. 캠페인을 다시 시작합니다.

###### 효과

* **기존 수신자:** 이미 카드를 받은 사용자는 다시 자격을 갖추기 전까지는 업데이트된 카드를 받을 수 없습니다. 재적격성이 해제되면 새 카드를 받을 수 없습니다.
* **보고:** 하나의 캠페인에는 출시된 카드 버전에 대한 모든 보고 분석이 포함됩니다. Braze는 출시된 버전 간의 차별을 두지 않습니다.

세션 시작으로 트리거되는 캠페인이 있고 재자격이 30일로 설정되어 있다고 가정해 보겠습니다. 사용자가 이틀 전에 캠페인을 받았는데 사본을 변경하려고 합니다. 먼저 캠페인을 중지하고 피드에서 카드를 제거합니다. 둘째, 새 복사본으로 캠페인을 다시 게시합니다. 사용자에게 다른 세션이 있는 경우, 28일 후에 새 카드를 받게 됩니다.

#### 카드 제거 및 만료

##### 수동 카드 제거

캠페인을 중지하여 모든 사용자의 피드에서 카드를 수동으로 제거할 수 있습니다.

1. 콘텐츠 카드 캠페인을 열고 캠페인 중지를 선택합니다.
2. 프롬프트가 표시되면 **다음 동기화 후 카드 제거**를 선택합니다. 카드는 다음 피드 새로 고침 시 제거됩니다.

##### 자동 카드 제거 {#action-based-card-removal}

사용자가 구매 완료 또는 기능 활성화와 같은 특정 작업을 수행할 때 카드를 자동으로 제거할 수 있습니다.

캠페인 또는 캔버스 단계에서 제거 이벤트를 지정합니다. 사용자가 해당 이벤트를 수행하면, 카드는 Braze가 이벤트를 처리한 후 다음 새로 고침에서 피드에서 제거됩니다. 

{% alert note %}
이 제거는 즉각적이지 않습니다. 처리 지연이 있으므로 카드가 사라지려면 몇 분과 여러 번의 피드 새로 고침이 필요할 수 있습니다.
{% endalert %}

{% alert tip %}
사용자 피드에서 카드를 제거해야 하는 여러 사용자 지정 이벤트 및 구매를 지정할 수 있습니다. 사용자가 이러한 작업을 수행하면 캠페인의 카드가 전송한 기존 카드가 **모두** 제거됩니다. 향후 적격 카드는 메시지 일정에 따라 계속 발송됩니다.
{% endalert %}

![콘텐츠 카드 제거 조건 패널과 콘텐츠 카드 제거 이벤트 옵션.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### 카드 만료

콘텐츠 카드는 발송된 후 최대 30일 동안 사용 가능하며, 30일 후에는 Braze가 사용자 피드에서 제거하고 Braze 시스템에서 삭제합니다.

#### 카드를 30일 이상 지속시키기

{% alert tip %}
30일 콘텐츠 카드 제한보다 메시지가 더 오래 지속되어야 하는 사용 사례의 경우, 배너 사용을 고려하십시오. 배너는 지속성을 위해 설계되었으며, 필수 만료 날짜가 없어 필요할 때까지 계속 표시될 수 있습니다.
{% endalert %}

카드가 항상 사용 가능한 것처럼 보이게 하려면 (i.e. 30일 최대보다 오래 지속됨), 30일마다 카드를 효과적으로 교체하는 반복 캠페인을 생성할 수 있습니다:

1. 콘텐츠 카드의 기간을 30일로 설정합니다.
2. 캠페인 재적격성을 30일로 설정합니다.
3. "세션 시작" 시 캠페인이 트리거되도록 설정합니다.
