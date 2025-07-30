---
nav_title: "푸시 메시지 만들기"
article_title: 푸시 캠페인 만들기
page_order: 4
page_type: tutorial
description: "이 튜토리얼 페이지에서는 구성, 전송, 타겟팅 등 푸시 메시지 작성에 관련된 다양한 구성요소에 대해 설명합니다."
channel: push
tool:
  - Campaigns
  
---

# 푸시 메시지 만들기

> 푸시 알림은 시간에 민감한 클릭 유도 문안과 한동안 앱에 접속하지 않았던 사용자의 재참여를 유도하는 데 유용합니다. 성공적인 푸시 캠페인은 사용자를 콘텐츠로 직접 유도하고 앱의 가치를 입증합니다. 푸시 알림의 예시를 보려면 [사례 연구][8]]를 참조하세요.

## 1단계: 메시지를 작성할 위치 선택 {#create-new-campaign-push}

{% alert tip %}
캠페인과 캔버스 중 어떤 것을 사용할지 고민 중이신가요? 캠페인은 단순한 단일 메시지 캠페인에 적합하며, 캔버스는 다단계 사용자 여정에 더 적합합니다.
{% endalert %}

{% tabs %}
{% tab 캠페인 %}
1. **메시징** > **캠페인으로** 이동한 다음 **캠페인 만들기를** 선택합니다.
2. 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다. 그렇지 않으면 **푸시 알림을** 선택합니다. 그래도 잘 모르겠다면 아래의 **일반 푸시 캠페인과 멀티채널 푸시 캠페인 중 결정하기를** 참조하세요.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed. **팁:** 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. 캠페인에 필요한 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

{% details 일반 푸시 캠페인과 멀티채널 푸시 캠페인 중 결정하기 %}

모바일, 웹, Kindle, iOS, Android 등 여러 기기와 플랫폼을 타겟팅하려는 경우 이 단계에서 선택한 사항이 나중에 일부 기능 및 설정의 가용성에 영향을 미칠 수 있습니다.

멀티채널 또는 푸시 알림 캠페인을 만들기 전에 다음 의사 결정 차트를 참조하세요:

!["캠페인 유형 선택을 위한 순서도. 여러 기기와 플랫폼을 타겟팅할지 결정하는 것부터 시작합니다. 그렇지 않은 경우 '푸시 알림 선택'으로 연결됩니다. 그렇다면 '푸시 메시지 유형은 무엇입니까?"라는 질문과 함께 '표준 푸시'를 선택하면 '기기별 설정을 사용해야 합니까?"라는 결정 사항으로 이어집니다. 그렇지 않은 경우 '푸시 알림 선택 및 빠른 푸시 사용'으로 이어집니다. 그렇다면 '멀티채널 선택'으로 이동합니다. '푸시 메시지 유형은 무엇인가요? '로 돌아가서 '푸시 스토리 또는 인라인 이미지'라고 답하면 '멀티채널 선택'으로 이동합니다."]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

**푸시 알림**을 선택하고 여러 기기와 플랫폼을 타겟팅하도록 선택하면 자동으로 빠른 푸시 캠페인이 생성됩니다. 빠른 푸시에서는 특정 기기별 설정을 사용할 수 없습니다:

- 푸시 액션 버튼
- 알림 채널 및 그룹
- 푸시 유지 시간(TTL)
- 우선순위 표시
- 소리

계속하기 전에 [빠른 푸시 캠페인을]({{site.baseurl}}/quick_push) 참조하여 이 편집 환경의 달라진 점을 이해하세요.

{% enddetails %}

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 상품 추가** 드롭다운에서 **배리언트 상품에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab 캔버스 %}
1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 스케줄]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 메시지가 전송된 후 지연 시간이 지나면 오디언스 옵션이 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)을 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: 전달 플랫폼 지정

먼저 푸시를 수신할 기기와 플랫폼 조합을 선택합니다. 이 선택을 사용하면 푸시 알림을 특정 앱 집합으로 제한할 수 있습니다.

이전 선택 항목에 따라 몇 가지 다른 방법으로 이 작업을 수행할 수 있습니다:

| 이전 선택 | 옵션 |
| --- | --- | 
| 푸시 알림 캠페인 | 하나 이상의 플랫폼과 기기를 선택합니다. 여러 기기와 플랫폼을 타겟팅하도록 선택하면 자동으로 퀵 푸시 캠페인이 생성됩니다. 이를 통해 단일 편집기에서 선택한 모든 플랫폼에 대해 하나의 메시지를 작성하는 데 최적화된 편집 환경을 제공합니다. [빠른 푸시 캠페인]({{site.baseurl}}/quick_push)을 참조하여 이 편집 환경의 달라진 점을 알아보세요. |
| 멀티채널 캠페인 | **메시징 채널 추가를** 선택하여 푸시 플랫폼을 추가합니다. 플랫폼 선택은 각 배리언트에 따라 다르므로 플랫폼별로 메시지 인게이지먼트를 테스트해 볼 수 있습니다!
| 캔버스 | 메시지 단계에서 **\+ 추가를** 선택하여 푸시 플랫폼을 추가합니다. 멀티채널 캠페인과 마찬가지로 플랫폼 선택은 각 변형에 따라 다릅니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 3단계: 알림 유형 선택(iOS 및 Android)

빠른 푸시 캠페인을 생성하는 경우 알림 유형은 자동으로 표준 푸시로 설정되며 변경할 수 없습니다.

![표준 푸시를 선택한 알림 유형을 예로 들어 설명합니다.][3]{: style="float:right;max-width:40%;margin-left:15px;"}

그렇지 않으면 iOS 및 Android의 경우 알림 유형을 선택합니다:

- 표준 푸시
- [푸시 스토리]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- 인라인 이미지(Android 전용)

푸시 캠페인에 이미지를 포함하려면 다음 [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) 또는 [Android용]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/) 리치 알림 만들기에 대한 가이드를 참조하세요.

## 4단계: 푸시 메시지 작성

이제 푸시 메시지를 작성할 차례입니다! **작성** 탭에서는 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![푸시 알림을 작성하는 작성 탭.]({% image_buster /assets/img_archive/push_compose.png %})

**작성** 탭의 콘텐츠는 이전 단계에서 선택한 알림 유형에 따라 다르지만 다음 옵션 중 하나를 포함할 수 있습니다:

#### 알림 채널 또는 그룹(iOS 및 Android)

For more information on platform-specific notification options, see [iOS Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) or [Android Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### 언어

**언어 추가** 버튼을 사용하여 여러 언어로 사본을 추가합니다. 콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 원하는 위치에 텍스트를 채울 수 있도록 하는 것이 좋습니다. 사용 가능한 전체 언어 목록은 [지원 언어][18] 를 참조하세요.

If you're adding copy in a language that is written right-to-left, note that the final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### 제목 및 본문

{% tabs local %}
{% tab ios %}
메시지 상자에 입력을 시작하면 왼쪽의 미리보기 상자에 미리보기가 표시됩니다. 푸시 메시지는 일반 텍스트 형식으로 작성해야 합니다. 

**제목** 필드를 사용하여 제목을 추가합니다. 푸시를 개인화 및 타겟팅하기 위해 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 포함할 수 있습니다.
{% endtab %}

{% tab Android %}
메시지 상자에 입력을 시작하면 왼쪽의 미리보기 상자에 미리보기가 표시됩니다. 푸시 메시지는 일반 텍스트 형식으로 작성해야 합니다. 

푸시를 개인화 및 타겟팅하기 위해 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 포함할 수 있습니다.

{% alert important %}
제목 없이 Android 푸시 메시지를 보낼 **수는** 없지만, 대신 공백 하나를 입력할 수 있습니다. 메시지에 공백이 하나만 포함되어 있으면 무음 푸시 알림으로 전송된다는 점에 유의하세요. 자세한 내용은 [무음 푸시 알림을]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) 참조하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
멋진 카피를 만드는 데 도움이 필요하신가요? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/). 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있도록 사람과 유사한 마케팅 문구를 생성합니다.

![푸시 작성기의 본문 필드에 있는 AI 카피라이터 실행 버튼을 누릅니다.(]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### 이미지

지원되는 경우 앱 아이콘이 푸시 알림의 이미지로 자동으로 추가됩니다. 또한 리치 알림을 보낼 수 있는 옵션이 있어 복사본 외에 추가 콘텐츠를 추가하여 푸시 알림을 더욱 맞춤 설정할 수 있습니다.

푸시 알림에 이미지를 사용하는 방법에 대한 자세한 안내는 다음 도움말 문서를 참조하세요:

- [iOS용 리치 알림 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Android용 리치 알림 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### 클릭 시 동작

사용자가 **온클릭 동작을** 사용하여 푸시 알림 본문을 선택하면 어떤 일이 발생하는지 지정합니다. 예를 들어 고객에게 애플리케이션을 열라는 메시지를 표시하거나, 고객을 지정된 웹 URL로 리디렉션하거나, [딥링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)를 통해 애플리케이션의 특정 페이지를 열 수 있습니다.

여기에서 푸시 알림 내에서 다음과 같은 버튼 프롬프트를 설정할 수도 있습니다:

- 수락/거절
- 예/아니요
- 확인/취소
- 더 보기 

#### 기기 옵션

사용자가 여러 기기에 앱을 설치한 경우 기본적으로 유효한 푸시 토큰이 할당된 모든 기기에 푸시 메시지가 전송됩니다. 원하는 경우 **사용자가 가장 최근에 사용한 기기로만 푸시 전송**을 선택할 수 있습니다.

![기기 옵션 확인란을 선택하면 사용자가 가장 최근에 사용한 기기로만 푸시를 보낼 수 있습니다.][9]{: style="max-width:70%;" }

이 설정에는 약간의 뉘앙스가 있습니다. 이 옵션을 선택하면 캠페인이 iOS와 Android 등 여러 플랫폼을 타겟팅하는 경우를 제외하고는 Braze에서 다중 전송이 발생하지 않도록 제한합니다. 사용자가 iOS와 Android 기기 모두에 앱을 설치한 경우 두 플랫폼 모두에 대한 푸시를 받게 됩니다. 사용자가 가장 최근에 사용한 기기가 [푸시를 사용하도록]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled) 설정되어 있지 않으면 메시지가 전송되지 않습니다.

iOS의 경우 푸시 알림을 iPad 기기로만 보내거나 iPhone 및 iPod 기기로만 보내도록 설정하여 메시징을 더욱 제한할 수 있습니다.

## 5단계: 메시지 미리보기 및 테스트(선택 사항)

![푸시 메시지 테스트][7]{: style="float:right;max-width:30%;margin-left:15px;"}

테스트는 가장 중요한 단계 중 하나입니다. 완벽한 푸시 메시지 작성을 완료한 후에는 보내기 전에 테스트해 보세요. **테스트** 탭을 선택하고 **사용자로서 메시지 미리 보기**를 사용하여 모바일에서 메시지가 어떻게 표시되는지 파악할 수 있습니다. **테스트 보내기를** 사용하여 테스트 푸시를 보내고 메시지가 제대로 표시되는지 확인합니다.

## 6단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab 캠페인 %}

나머지 캠페인을 구축하세요. 푸시 알림을 구축하기 위해 도구를 가장 효과적으로 사용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

#### 배송 일정 또는 트리거 선택

푸시 메시지는 예약된 시간, 작업 또는 API 트리거에 따라 전달할 수 있습니다. 자세한 내용은 [캠페인 일정 잡기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)을 참조하세요.

액션 기반 전달의 경우 캠페인의 기간과 [조용한 시간을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) 설정할 수도 있습니다.

이 단계에서는 사용자가 캠페인을 받을 수 있도록 [다시 자격]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)을 얻을 수 있도록 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 규칙을 활성화하는 등의 전달 제어를 지정할 수 있습니다.

#### 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 [사용자를 타겟팅하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 오디언스의 범위를 좁혀야 합니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 캠페인이 타겟팅하는 채널에 대한 자세한 오디언스 통계는 바닥글에서 확인할 수 있습니다. 타겟팅 중인 사용자층의 비율과 이 세그먼트의 평생 가치를 확인하려면 **추가 통계 표시를** 선택합니다.

{% details 총 도달 가능한 사용자 수 지표가 모든 채널의 합계와 일치하지 않는 이유는 무엇인가요? %}

필터링된 대상 그룹에 대한 총 도달 가능한 사용자를 보면 개별 열의 합계가 총 도달 가능한 사용자보다 작다는 것을 알 수 있습니다. 이러한 격차는 일반적으로 캠페인의 세그먼트 또는 필터에 대한 자격이 있지만 푸시를 통해 도달할 수 없는 사용자가 많기 때문입니다(예: 유효하거나 활성화된 [푸시 토큰]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)이 없기 때문).

{% enddetails %}

![도달 가능한 사용자에 대한 자세한 오디언스 통계 표.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

또한 구독 중이고 푸시 수신에 동의한 사용자와 같이 특정 [구독 상태를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) 가진 사용자에게만 캠페인을 보내도록 선택할 수도 있습니다.

선택적으로 세그먼트 내에서 지정된 수의 사용자에게만 전달하도록 제한하거나 캠페인이 반복될 때 사용자가 동일한 메시지를 두 번 수신하도록 허용할 수도 있습니다.

##### 이메일 및 푸시를 통한 멀티채널 캠페인

이메일과 푸시 채널을 모두 대상으로 하는 멀티채널 캠페인의 경우 명시적으로 옵트인한 사용자만 메시지를 수신하도록 캠페인을 제한할 수 있습니다(구독 또는 수신 거부한 사용자 제외). 예를 들어 옵트인 상태가 서로 다른 세 명의 사용자가 있다고 가정해 보겠습니다:

- **사용자 A**는 이메일을 구독하고 푸시를 사용하도록 설정되어 있습니다. 이 사용자는 이메일을 수신하지 않지만 푸시를 받게 됩니다.
- **사용자 B**는 이메일 수신에 옵트인했지만 푸시를 사용하도록 설정되어 있지 않습니다. 이 사용자는 이메일을 받지만 푸시는 받지 않습니다.
- **사용자 C는** 이메일 수신에 동의하고 푸시를 사용하도록 설정되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받게 됩니다.

이렇게 하려면 **오디언스 요약**에서 "옵트인한 사용자에게만" 이 캠페인을 보내도록 선택합니다. 이 옵션을 선택하면 옵트인한 사용자만 이메일을 받게 되며, Braze는 기본적으로 푸시를 사용하도록 설정한 사용자에게만 푸시를 보냅니다.

{% alert important %}
이 구성에서는 **대상 사용자** 단계에 대상을 단일 채널로 제한하는 필터(예: `Push Enabled = True` 또는 `Email Subscription = Opted-In`)를 포함하지 마세요.
{% endalert %}

#### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

{% endtab %}

{% tab 캔버스 %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 자세한 내용은 캔버스의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대해 설명서의 [캔버스 구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 7단계: {#review-and-deploy-push} 검토 및 배포

캠페인 또는 캔버스의 마지막 제작을 완료한 후에는 세부 정보를 검토합니다. 캠페인의 경우 마지막 페이지에 방금 디자인한 캠페인에 대한 요약이 표시됩니다. 모든 관련 세부 정보를 확인하고 메시지를 테스트한 다음 메시지를 전송하고 데이터가 들어오는 것을 지켜보세요!

다음으로 푸시 캠페인의 결과에 액세스하는 방법을 알아보려면 [푸시 보고]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/)를 확인하세요. 푸시 알림의 경우 전송, 전달, 반송, 열람 및 직접 열어본 메시지 수에 대한 통계를 볼 수 있습니다.

[1]: {% image_buster /assets/img_archive/new_campaign_push.png %}
[2]: {% image_buster /assets/img_archive/push_1.png %}
[3]: {% image_buster /assets/img_archive/push_2.png %}
[4]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[7]: {% image_buster /assets/img_archive/push_3.png %}
[8]:https://www.braze.com/customers
[9]: {% image_buster /assets/img_archive/push_recent_device.png %}
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %} 
