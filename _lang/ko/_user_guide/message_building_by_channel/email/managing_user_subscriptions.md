---
nav_title: 이메일 구독
article_title: 이메일 구독
page_order: 6
description: "이 참조 문서에서는 다양한 사용자 구독 상태, 구독 그룹을 만들고 관리하는 방법, 구독에 따라 사용자를 분류하는 방법에 대해 설명합니다."
channel:
  - email

---

# 이메일 구독

> 사용자 구독 상태, 구독 그룹 생성 및 관리 방법, 그리고 구독을 기반으로 사용자를 세그먼트화하는 방법에 대해 알아보세요.

이 문서는 정보 제공 목적으로만 제공됩니다. 이 문서는 법률 자문을 제공하기 위한 것이 아니며, 어떤 형태로든 법률 자문을 제공하는 것으로 간주되어서는 안 됩니다. 마케팅 및 거래 이메일 전송에는 특정 법적 요건이 적용될 수 있습니다. 회사에 적용되는 모든 관련 법률, 규칙 및 규정을 준수하고 있는지 확인하려면 법률 고문 및/또는 규정 준수 팀의 조언을 구해야 합니다.

## 구독 상태 {#subscription-states}

Braze는 이메일 사용자에 대해 세 가지 글로벌 구독 상태를 가지고 있습니다. 이 상태는 사용자에게 메시지를 차단합니다. 예를 들어, `unsubscribed` 상태의 사용자는 `subscribed` 또는 `opted-in`을 대상으로 하는 메시지를 받지 않습니다.

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

Braze는 사용자가 [커스텀 푸터]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer)를 통해 수동으로 구독 취소할 경우 자동으로 구독을 취소합니다. 사용자가 이메일 주소를 업데이트하고 **이메일 업데이트 시 사용자 재구독**가 **전송 구성**에서 활성화되어 있으면, 정상 전송이 재개됩니다.

사용자가 귀하의 이메일 중 하나 이상을 스팸으로 표시하면, Braze는 해당 사용자에게 거래 이메일만 보냅니다. 거래 이메일은 **구독 취소된 사용자를 포함한 모든 사용자에게 전송** 옵션을 **대상 오디언스**에서 참조합니다.

{% alert tip %}
Refer to our [IP warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) best practices for guidance on how to re-engage your users effectively.
{% endalert %}

### 반송 및 유효하지 않은 이메일

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

이메일 주소가 하드 바운스되면, Braze는 사용자의 구독 상태를 "구독 취소됨"으로 자동 설정하지 않습니다. 주소가 하드 바운스(유효하지 않거나 존재하지 않음)되면, Braze는 이를 유효하지 않다고 표시하고 추가 전송을 시도하지 않습니다. 사용자가 이메일 주소를 변경하면, Braze는 전송을 재개합니다. Braze는 소프트 바운스를 72시간 동안 재시도합니다.

### 이메일 구독 상태 업데이트하기

사용자의 이메일 구독 상태를 업데이트하는 방법에는 네 가지가 있습니다:

#### SDK 통합

Braze SDK를 사용하여 사용자의 구독 상태를 업데이트하세요.

#### REST API

사용자의 [`email_subscribe` 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object)을 업데이트하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하세요.

#### 사용자 프로필

1. **사용자 검색**을 통해 사용자를 찾습니다. 
2. **참여** 아래에서 **구독 취소됨**, **구독됨**, 또는 **옵트인**을 선택하여 사용자의 구독 상태를 변경합니다. 

가능한 경우 고객 프로필에는 사용자의 구독이 마지막으로 변경된 시점의 타임스탬프도 표시됩니다.

#### 환경 설정 센터

사용자가 옵트인 또는 옵트아웃할 수 있도록 이메일 하단에 [선호 센터](#email-preference-center) Liquid를 포함하세요. Braze는 선호 센터에서 구독 상태 업데이트를 관리합니다.

### 이메일 구독 상태 확인

![User profile for John Doe with their email subscription state set to Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

사용자의 이메일 구독 상태를 확인하는 방법은 다음과 같습니다:

1. **REST API 내보내기:** Use the [Export users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) or [Export users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoints to export individual user profiles in JSON format.
2. **사용자 프로필:** Find the user's profile on the [Search Users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) page, then select the **Engagement** tab to view and manually update a user's subscription state.

사용자가 이메일 주소를 업데이트하면 업데이트된 이메일 주소가 Braze 워크스페이스의 다른 곳에 이미 존재하지 않는 한 구독 상태가 구독됨으로 설정됩니다.

## Subscription groups

구독 그룹은 [전역구독 상태](#subscription-states)에서 대상을 더욱 좁힐 수 있는 세그먼트 필터입니다. 작업 공간당 최대 350개의 구독 그룹을 추가할 수 있습니다. 이러한 그룹을 사용하면 최종 사용자에게 보다 세분화된 구독 옵션을 제공할 수 있습니다.

예를 들어 여러 카테고리의 이메일 캠페인(프로모션, 뉴스레터 또는 제품 업데이트)을 발송한다고 가정해 보겠습니다. 이 경우 [이메일 환경설정 센터](#email-preference-center)를 사용하여 구독 그룹을 사용하여 고객이 단일 페이지에서 일괄적으로 구독 또는 수신 거부할 이메일 카테고리를 선택하도록 할 수 있습니다. 또는 구독 그룹을 사용하여 일별, 주별 또는 월별 이메일에 대한 구독 그룹을 만들어 고객이 이메일 수신 빈도를 선택할 수 있도록 할 수도 있습니다.

Use the [Subscription Group endpoints]({{site.baseurl}}/api/endpoints/subscription_groups) to programmatically manage the subscription groups that you have stored on the Braze dashboard to the **Subscription Group** page.

### 구독 그룹 만들기

1. **오디언스** > **구독 그룹 관리**로 이동하세요.
2. Select **Create email subscription group**. 
3. Give your subscription group a name and description.
4. Select **Save**. 

모든 구독 그룹은 환경설정 센터에 자동으로 추가됩니다.

![Fields to create a subscription group.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### 구독 그룹으로 세분화하기

세그먼트를 만들 때 구독 그룹 이름을 필터로 설정합니다. 이렇게 하면 그룹에 옵트인한 사용자가 내 이메일을 받을 수 있습니다. 월간 뉴스레터, 쿠폰, 멤버십 등급 등에 유용하게 사용할 수 있습니다.

![ "주간 이메일" 구독 그룹의 사용자 필터로 "소멸된 사용자" 세그먼트의 사용자를 타겟팅하는 예시입니다.]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### 구독 그룹 아카이브

보관된 구독 그룹은 편집할 수 없으며 세그먼트 필터나 환경설정 센터에 더 이상 표시되지 않습니다. 이메일, 캠페인 또는 캔버스에서 세그먼트 필터로 사용 중인 그룹을 보관하려고 하면 해당 그룹의 모든 사용을 제거할 때까지 해당 그룹을 보관할 수 없다는 오류 메시지가 표시됩니다.

To archive your group from the **Subscription Groups** page, do the following:

1. Find your group in the list of subscription groups. 
2. Select **Archive** from the <i class="fa-solid fa-ellipsis-vertical"></i> dropdown menu.

Braze는 아카이브된 그룹의 사용자 상태 변경을 처리하지 않습니다. 예를 들어, Alex가 구독 중인 구독 그룹 1을 아카이브하면, Alex는 탈퇴 링크를 클릭하더라도 여전히 "구독 중"으로 남아 있습니다. 이것은 중요하지 않습니다. 왜냐하면 구독 그룹 1이 아카이브되어 있고 이를 사용하여 메시지를 보낼 수 없기 때문입니다.

#### 구독 그룹 크기 보기

You can reference the **Subscription Group Timeseries** graph in the **Subscription Groups** page to view the subscription group size based on the number of users over a period of time. 이러한 구독 그룹 크기는 세그먼트 크기 계산과 같은 Braze의 다른 영역과도 일치합니다.

![12월 2일부터 11일까지의 '구독 그룹 시계열' 그래프 예시입니다. The graph shows a ~10 million increase in the number of users from the 6th to the 7th.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### 캠페인 분석에서 구독 그룹 보기

특정 이메일 캠페인에서 구독 상태(구독 또는 탈퇴)를 변경한 사용자 수를 해당 캠페인의 분석 페이지에서 확인할 수 있습니다.

1. From the **Campaign Analytics** page for your campaign, scroll down to the **Email Message Performance** section.
2. Select the arrow under **Subscription Groups** to see the aggregate count of state changes, as submitted by your customers.

![The "Email Message Performance" page displaying the aggregate count of state changes submitted by customers.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### 사용자의 이메일 구독 그룹 확인하기

- **사용자 프로필:** 개별 사용자 프로필은 [사용자 검색]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles) 페이지의 Braze 대시보드를 통해 액세스할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 아이디로 사용자 프로필을 조회할 수 있습니다. 사용자의 이메일 구독 그룹을 **참여** 탭에서 볼 수 있습니다.
- **Braze REST API:** 개별 사용자 프로필의 구독 그룹을 보려면 [사용자의 구독 그룹 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) 또는 [사용자의 구독 그룹 상태 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)를 사용하세요. 

## 이메일 환경설정 센터

이메일 선호 센터를 통해 어떤 사용자가 구독 그룹 뉴스레터를 받을지 관리할 수 있습니다. 대시보드의 **구독 그룹**에서 찾을 수 있습니다. 생성하는 각 구독 그룹은 환경설정 센터 목록에 추가됩니다. 

To learn more about how to add or customize a preference center, refer to [Preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## 이메일 구독 변경하기 {#changing-email-subscriptions}

대부분의 경우, 사용자는 수신하는 이메일에 포함된 링크를 통해 이메일 구독을 관리합니다. 모든 이메일 하단에 탈퇴 링크가 포함된 법적으로 준수하는 바닥글을 삽입하세요. 사용자가 탈퇴 URL을 선택하면, Braze는 그들을 탈퇴시키고 변경을 확인하는 랜딩 페이지를 표시합니다. 다음 Liquid 태그를 포함하세요: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

사용자가 선호 센터에서 "위의 모든 유형의 이메일 탈퇴"를 선택하면, Braze는 그들의 전역 이메일 구독 상태를 `unsubscribed`로 설정하고 모든 그룹에서 탈퇴시킵니다.

### 커스텀 바닥글 만들기 {#custom-footer}

기본 바닥글을 사용하고 싶지 않다면, 작업 공간 전체에 맞춤 이메일 바닥글을 만들고 {% raw %}`{{${email_footer}}}`{% endraw %}를 사용하여 모든 이메일에 템플릿화하세요.

이렇게 하면 모든 이메일 템플릿이나 이메일 캠페인에 대해 새로운 바닥글을 만들 필요가 없습니다. 단계는 [맞춤 이메일 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/)을 참조하세요.

#### 중국 IP 주소에 대한 구독 상태 관리

중국 IP 주소를 예상하는 경우, `unsubscribed` 목록을 유지하기 위해 탈퇴 링크에만 의존하지 마세요. 지원 티켓이나 고객 담당자 이메일과 같은 대체 탈퇴 경로를 제공하세요. 

### 커스텀 수신 거부 페이지 만들기

사용자가 탈퇴 URL을 선택하면 Braze는 변경 사항을 확인하는 기본 랜딩 페이지를 표시합니다.

구독 후 표시되는 기본 랜딩 페이지 대신 커스텀 랜딩 페이지를 만들려면:

1. Go to **Email Preferences** > **Subscription Pages and Footers**.
2. Provide the HTML for your custom landing page. 

사용자가 실수로 탈퇴한 경우 다시 구독할 수 있도록 재구독 링크(예: {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %})를 포함하세요.

![미리보기 "안녕히 가세요!"가 있는 커스텀 탈퇴 페이지입니다.]({% image_buster /assets/img/custom_unsubscribe.png %})

### 사용자 지정 옵트인 페이지 만들기

사용자가 구독 전에 알림 기본 설정을 인식하고 제어할 수 있도록 커스텀 옵트인 페이지를 사용하세요. 이 추가 커뮤니케이션은 이메일 캠페인이 스팸 폴더에 들어가지 않도록 도와줄 수 있습니다.

1. Go to **Settings** > **Email Preferences**.
2. Select **Subscription Pages and Footers**.
3. Customize the styling in the **Custom opt-in page** section to see how that indicates to your users that they've been subscribed.

사용자는 {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} 태그를 통해 이 페이지에 도달합니다.

{% alert tip %}
더 나은 아웃리치를 위해 더블 옵트인 프로세스를 사용하세요. Braze는 사용자가 링크를 통해 알림 기본 설정을 확인하는 추가 확인 이메일을 보냅니다. 확인 후 사용자는 옵트인 상태가 됩니다.
{% endalert %}

![메시지 "여전히 저희 소식을 듣고 싶어 하신다니 기쁩니다"가 있는 커스텀 옵트인 이메일입니다.]({% image_buster /assets/img/custom_optin.png %})

## 구독 및 캠페인 타겟팅 {#subscriptions-and-campaign-targeting}

기본적으로 Braze는 구독하거나 옵트인한 사용자에게 푸시 또는 이메일 메시지로 캠페인을 타겟팅합니다. **타겟 오디언스**에서 **이 사용자에게 전송:** 옆의 드롭다운을 선택하여 변경하세요.

Braze는 세 가지 타겟팅 상태를 지원합니다:

- 구독 또는 옵트인한 사용자(기본값).
- 옵트인한 사용자만 사용할 수 있습니다.
- 구독을 취소한 사용자를 포함한 모든 사용자.

{% alert important %}
It's your responsibility to comply with any applicable [spam laws]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) when using these targeting settings.
{% endalert %}

## 사용자 구독별로 세분화하기 {#segmenting-by-user-subscriptions}

"이메일 구독 상태" 및 "푸시 구독 상태" 필터를 사용하여 구독 상태에 따라 사용자를 세그먼트화하세요.

옵트인도 옵트아웃도 하지 않은 사용자를 타겟팅하고 명시적인 옵트인을 유도하는 데 사용하세요. "이메일/푸시 구독 상태가 구독됨" 필터로 세그먼트를 만들고 구독했지만 옵트인하지 않은 사용자에게 캠페인을 전송하세요.

![Email Subscription Status used as a segment filter.]({% image_buster /assets/img_archive/not_optin.png %})

