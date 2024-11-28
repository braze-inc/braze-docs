---
nav_title: 이메일 구독
article_title: 이메일 구독
page_order: 6
description: "이 참조 문서에서는 다양한 사용자 구독 상태, 구독 그룹을 만들고 관리하는 방법, 구독에 따라 사용자를 분류하는 방법에 대해 설명합니다."
channel:
  - email

---

# 이메일 구독

> 다양한 사용자 구독 상태, 구독 그룹을 만들고 관리하는 방법, 구독을 기준으로 사용자를 세분화하는 방법에 대해 알아보세요.

이 문서는 정보 제공 목적으로만 제공됩니다. 이 문서는 법률 자문을 제공하기 위한 것이 아니며, 어떤 형태로든 법률 자문을 제공하는 것으로 간주되어서는 안 됩니다. 마케팅 및 거래 이메일 전송에는 특정 법적 요건이 적용될 수 있습니다. 회사에 적용되는 모든 관련 법률, 규칙 및 규정을 준수하고 있는지 확인하려면 법률 고문 및/또는 규정 준수 팀의 조언을 구해야 합니다.

## 구독 상태 {#subscription-states}

Braze는 이메일 사용자를 위한 세 가지 글로벌 구독 상태(다음 표에 나열됨)를 제공하며, 이는 메시지와 사용자 사이의 최종 게이트키퍼 역할을 합니다. 예를 들어 `unsubscribed`로 간주되는 사용자는 `subscribed` 또는 `opted-in`의 글로벌 구독 상태를 대상으로 하는 메시지를 수신하지 않습니다.

| 상태 | 정의 |
| ----- | ---------- |
| 옵트인 | 사용자가 이메일 수신을 명시적으로 확인했습니다. 이메일 전송에 대한 사용자의 동의를 얻기 위해 명시적인 옵트인 프로세스를 권장합니다. |
| 가입됨 | 사용자가 이메일 수신을 거부하거나 명시적으로 수신에 옵트인하지 않았습니다. 사용자 프로필이 생성될 때 기본 구독 상태입니다. |
| 탈퇴됨 | 사용자가 명시적으로 이메일 수신을 거부했습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Braze는 데이터 포인트, 전 세계 및 구독 그룹에 대한 구독 상태 변경 사항을 집계하지 않습니다.
{% endalert %}

### 수신 거부된 이메일 주소

Braze는 [커스텀 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer)을 통해 수동으로 이메일 구독을 취소하는 모든 사용자의 구독을 자동으로 취소합니다. 사용자가 이메일 주소를 업데이트하고 **전송 구성** 설정에서 **이메일 업데이트 시 사용자 재구독이** 활성화되어 있으면 정상적인 이메일 전송이 재개됩니다.

사용자가 하나 이상의 이메일을 스팸으로 표시한 경우 Braze는 해당 사용자에게만 트랜잭션 이메일을 보냅니다. 이 경우 트랜잭션 이메일은 **대상 고객** 단계에서 **수신 거부한 사용자를 포함한 모든 사용자에게 보내기** 옵션을 선택한 것을 의미합니다.

{% alert tip %}
[IP 온난화]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) 모범 사례를 참조하여 사용자를 효과적으로 다시 참여시키는 방법에 대한 지침을 확인하세요.
{% endalert %}

### 반송 및 유효하지 않은 이메일

{% multi_lang_include metrics.md metric='하드 바운스' %} {% multi_lang_include metrics.md metric='소프트 바운스' %} 

해당 사용자의 이메일 주소가 변경되면 새 이메일이 유효할 수 있으므로 이메일 전송을 재개합니다. 소프트 바운스는 72시간 동안 자동으로 재시도됩니다.

### 이메일 구독 상태 업데이트하기

사용자의 이메일 구독 상태를 업데이트하는 방법에는 네 가지가 있습니다:

#### SDK 통합

Braze SDK를 사용하여 사용자의 구독 상태를 업데이트하세요.

#### REST API

`/users/track` 엔드포인트][사용자 트랙]을 사용하여 지정된 사용자에 대한 [`email_subscribe`][user_attributes_object] 속성을 업데이트합니다.

#### 사용자 프로필

1. **사용자 검색**을 통해 사용자를 찾습니다. 
2. **참여** 탭에서 **구독 취소**, **구독** 또는 **옵트인** 버튼을 클릭하여 해당 사용자의 구독 상태를 변경합니다. 

가능한 경우 고객 프로필에는 사용자의 구독이 마지막으로 변경된 시점의 타임스탬프도 표시됩니다.

#### 환경 설정 센터

이메일 하단에 [환경설정 센터](#email-preference-center) Liquid를 포함하여 사용자가 이메일을 수신하거나 수신 거부할 수 있도록 할 수 있습니다. Braze는 환경설정 센터에서 구독 상태 업데이트를 관리합니다.

### 이메일 구독 상태 확인

![이메일 구독 상태가 구독됨으로 설정된 신원미상의 고객 프로필입니다.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Braze에서 사용자의 이메일 구독 상태를 확인할 수 있는 방법은 두 가지가 있습니다:

1. **REST API 내보내기:** 세그먼트로 사용자 내보내기][세그먼트] 또는 [식별자로 사용자 내보내기][식별자] 엔드포인트를 사용하여 개별 고객 프로필을 JSON 형식으로 내보낼 수 있습니다.
2. **사용자 프로필:** 사용자 검색][5] 페이지]에서 사용자의 프로필을 찾은 다음 **참여** 탭을 선택하여 사용자의 구독 상태를 확인하고 수동으로 업데이트합니다.

사용자가 이메일 주소를 업데이트하면 업데이트된 이메일 주소가 Braze 워크스페이스의 다른 곳에 이미 존재하지 않는 한 구독 상태가 구독됨으로 설정됩니다. 세그먼트로 사용자 내보내기][세그먼트] 또는 [식별자로 사용자 내보내기][식별자] 엔드포인트를 사용하여 개별 고객 프로필을 JSON 형식으로 내보낼 수 있습니다.

## 구독 그룹

구독 그룹은 [전역구독 상태](#subscription-states)에서 대상을 더욱 좁힐 수 있는 세그먼트 필터입니다. 작업 공간당 최대 350개의 구독 그룹을 추가할 수 있습니다. 이러한 그룹을 사용하면 최종 사용자에게 보다 세분화된 구독 옵션을 제공할 수 있습니다.

예를 들어 여러 카테고리의 이메일 캠페인(프로모션, 뉴스레터 또는 제품 업데이트)을 발송한다고 가정해 보겠습니다. 이 경우 [이메일 환경설정 센터](#email-preference-center)를 사용하여 구독 그룹을 사용하여 고객이 단일 페이지에서 일괄적으로 구독 또는 수신 거부할 이메일 카테고리를 선택하도록 할 수 있습니다. 또는 구독 그룹을 사용하여 일별, 주별 또는 월별 이메일에 대한 구독 그룹을 만들어 고객이 이메일 수신 빈도를 선택할 수 있도록 할 수도 있습니다.

구독 그룹 엔드포인트][25]를 사용하여 Braze 대시보드에 저장한 구독 그룹을 프로그래밍 방식으로 관리하여 **구독 그룹** 페이지로 이동합니다.

### 구독 그룹 만들기

1. **오디언스** > **구독**으로 이동합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 이 페이지는 **사용자** > **구독 그룹**에 있습니다.
{% endalert %}

{: start="2"}
2\. **+이메일 구독 그룹 만들기**를 선택합니다.
3\. 구독 그룹에 이름과 설명을 입력하고 **저장**을 클릭합니다. 

모든 구독 그룹은 환경설정 센터에 자동으로 추가됩니다.

![필드를 사용하여 구독 그룹을 만듭니다.][26]{: height="50%" width="50%"}

### 구독 그룹으로 세분화하기

세그먼트를 만들 때 구독 그룹 이름을 필터로 설정합니다. 이렇게 하면 그룹에 옵트인한 사용자가 내 이메일을 받을 수 있습니다. 월간 뉴스레터, 쿠폰, 멤버십 등급 등에 유용하게 사용할 수 있습니다.

![구독 그룹 이름을 필터로 설정한 사용자의 GIF입니다.][27]{: style="max-width:80%"}

### 구독 그룹 아카이브

보관된 구독 그룹은 편집할 수 없으며 세그먼트 필터나 환경설정 센터에 더 이상 표시되지 않습니다. 이메일, 캠페인 또는 캔버스에서 세그먼트 필터로 사용 중인 그룹을 보관하려고 하면 해당 그룹의 모든 사용을 제거할 때까지 해당 그룹을 보관할 수 없다는 오류 메시지가 표시됩니다.

**구독 그룹** 페이지에서 그룹을 아카이브할 수 있습니다. 목록에서 해당 그룹을 찾은 다음 기어를 클릭하고 드롭다운 메뉴에서 **아카이브**를 선택합니다.

Braze는 보관된 그룹의 사용자에 대한 상태 변경을 처리하지 않습니다. 예를 들어 수지가 `subscribed`인 상태에서 "구독 그룹 A"를 보관하면, Susie가 수신 거부 링크를 클릭하더라도 이 그룹은 "`subscribed`"로 유지됩니다("구독 그룹 A"는 보관되어 있고 이를 사용하여 메시지를 보낼 수 없으므로 수지에게는 중요하지 않습니다).

#### 구독 그룹 크기 보기

**구독 그룹** 페이지에서 **구독 그룹 시계열** 그래프를 참조하여 일정 기간 동안의 사용자 수에 따른 구독 그룹 규모를 확인할 수 있습니다. 이러한 구독 그룹 크기는 세그먼트 크기 계산과 같은 Braze의 다른 영역과도 일치합니다.

![][10]

#### 캠페인 분석에서 구독 그룹 보기

해당 캠페인의 분석 페이지에서 특정 이메일 캠페인에서 구독 상태(구독 또는 구독 취소)를 변경한 사용자 수를 확인할 수 있습니다.

캠페인의 캠페인 **분석** 페이지에서 **이메일 메시지 실적** 섹션까지 아래로 스크롤하여 **구독 그룹** 아래의 화살표를 클릭하면 고객이 제출한 상태 변경의 총 개수를 확인할 수 있습니다.

![][30]

## 이메일 환경설정 센터

이메일 환경설정 센터는 어떤 사용자가 특정 뉴스레터 그룹을 수신할지 쉽게 관리할 수 있는 방법으로, 대시보드의 **구독 그룹**에서 찾을 수 있습니다. 생성하는 각 구독 그룹은 환경설정 센터 목록에 추가됩니다. 환경설정 센터를 추가하거나 커스텀하는 방법에 대해 자세히 알아보려면 [환경설정 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/)를 참조하세요.

## 이메일 구독 변경하기 {#changing-email-subscriptions}

대부분의 경우 사용자는 수신하는 이메일에 포함된 구독 링크를 통해 이메일 구독을 관리합니다. 보내는 모든 이메일 하단에 수신 거부 링크가 포함된 법적 규정을 준수하는 바닥글을 삽입해야 합니다. 사용자가 바닥글에 있는 구독 취소 URL을 클릭하면 구독이 취소되고 구독 변경을 확인하는 랜딩 페이지로 이동해야 합니다. 이 Liquid 태그를 포함하는 것을 권장합니다: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

사용자가 이메일 환경설정 센터에서 "위의 모든 유형의 이메일 수신 취소"를 선택하면 글로벌 이메일 수신 상태가 `unsubscribed`로 업데이트되고 모든 수신 그룹에서 수신이 취소됩니다.

### 커스텀 바닥글 만들기 {#custom-footer}

이메일에 기본 Braze 바닥글을 사용하고 싶지 않다면 {% raw %}`{{${email_footer}}}`{% endraw %} Liquid 속성을 사용하여 모든 이메일에 템플릿으로 사용할 수 있는 워크스페이스 전체에 사용자 지정 이메일 바닥글을 만들 수 있습니다.

이렇게 하면 사용하는 모든 이메일 템플릿이나 이메일 캠페인에 대해 바닥글을 새로 만들 필요가 없습니다. 단계는 [커스텀 이메일 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/)을 참조하세요.

#### 중국 IP 주소에 대한 구독 상태 관리

이메일 수신자가 중국 IP 주소를 사용할 것으로 예상되는 경우 이메일의 수신 거부 링크에만 의존하여 `unsubscribed` 목록을 유지해서는 안 됩니다. 대신 지원 포털을 통해 지원 티켓을 열거나 고객 담당자에게 이메일을 보내는 등 사용자가 쉽게 구독을 취소할 수 있는 다른 방법을 제공하세요. 

### 커스텀 수신 거부 페이지 만들기

사용자가 이메일에서 수신 거부 URL을 클릭하면 구독 변경을 확인하는 기본 랜딩 페이지로 이동합니다.

구독 시 사용자가 기본 페이지 대신 연결되는 사용자 지정 랜딩 페이지를 만들려면 **이메일 환경설정** > **구독 페이지 및 바닥글로** 이동하여 사용자 지정 랜딩 페이지의 HTML을 입력합니다. 사용자가 실수로 구독을 취소한 경우 재수신할 수 있도록 랜딩 페이지에 재수신 링크(예: {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %})를 포함시키는 것이 좋습니다.

![커스텀 수신 거부 페이지 패널에서 커스텀 수신 거부 이메일을 작성합니다.][11]

### 사용자 지정 옵트인 페이지 만들기

사용자를 이메일 캠페인에 즉시 가입시키는 대신 사용자 지정 옵트인 페이지를 만들면 사용자가 자신의 알림 기본 설정을 확인하고 제어할 수 있습니다. 이러한 추가 커뮤니케이션은 사용자가 수신 동의를 선택했기 때문에 이메일 캠페인이 스팸 폴더에서 제외되는 데 도움이 될 수 있습니다. 

**이메일 환경설정** > **구독 페이지 및 바닥글로** 이동하여 사용자 **지정 옵트인 페이지** 섹션에서 스타일을 사용자 지정하여 사용자에게 구독했음을 표시하는 방법을 확인합니다.

{% alert tip %}
Braze는 이메일 홍보를 위해 이중 옵트인 프로세스를 사용할 것을 권장합니다. 이 프로세스는 사용자가 이메일의 링크를 통해 알림 기본 설정을 다시 확인할 수 있는 추가 확인 이메일을 보냅니다. 이 시점에서 사용자는 옵트인한 것으로 간주됩니다.
{% endalert %}

## 구독 및 캠페인 타겟팅 {#subscriptions-and-campaign-targeting}

푸시 또는 이메일 메시지가 포함된 캠페인은 기본적으로 구독 또는 옵트인한 사용자를 대상으로 합니다. 캠페인을 수정할 때 **타겟 오디언스** 단계로 이동하여 **다음 사용자에게 보내기:** 옆의 드롭다운을 클릭하여 이 타겟팅 기본 설정을 변경할 수 있습니다.

Braze는 세 가지 타겟팅 상태를 지원합니다:

- 구독 또는 옵트인한 사용자(기본값).
- 옵트인한 사용자만 사용할 수 있습니다.
- 구독을 취소한 사용자를 포함한 모든 사용자.

{% alert important %}
이러한 타겟팅 설정을 사용할 때 해당 [스팸 관련 법률을]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) 준수하는 것은 회원님의 책임입니다.
{% endalert %}

![타겟 오디언스 단계의 타겟팅 옵션 섹션에서 구독 또는 옵트인한 사용자를 대상으로 하는 타겟팅 예시입니다.][17]

## 사용자 구독별로 세분화하기 {#segmenting-by-user-subscriptions}

`Email Subscription Status` 및 `Push Subscription Status` 필터를 사용하면 구독 상태별로 사용자를 세분화할 수 있습니다.

예를 들어, 옵트인하거나 옵트아웃하지 않은 사용자를 타겟팅하여 이메일이나 푸시 수신에 명시적으로 옵트인하도록 유도하려는 경우 유용할 수 있습니다. 이 경우 "이메일/푸시 구독 상태가 구독됨"에 대한 필터를 사용하여 세그먼트를 생성하면 이 세그먼트에 대한 캠페인이 구독 중이지만 옵트인하지 않은 사용자에게 전달됩니다.

![이메일 구독 상태는 세그먼트 필터로 사용됩니다.][18]

[10]: {% image_buster /assets/img_archive/subscription_group_graph.png %}
[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %}
[17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui.png %}
[18]: {% image_buster /assets/img_archive/not_optin.png %}
[19]: {% image_buster /assets/img_archive/email_settings.png %}
[25]: {{site.baseurl}}/api/endpoints/subscription_groups
[26]: {% image_buster /assets/img/sub_group_create.png %}
[27]: {% image_buster /assets/img/sub_group_use.gif %}
[28]: {{site.baseurl}}/api/endpoints/preference_center/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[3]: {% image_buster /assets/img/push_example.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
