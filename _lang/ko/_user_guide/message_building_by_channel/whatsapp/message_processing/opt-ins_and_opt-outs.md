---
nav_title: 옵트인 및 옵트아웃
article_title: WhatsApp 옵트인 및 옵트아웃
description: "이 참조 문서에서는 다양한 WhatsApp 옵트인 및 옵트아웃 방법을 다룹니다."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# 옵트인 및 옵트아웃

> WhatsApp은 귀하의 [전화번호 품질 등급](https://www.facebook.com/business/help/896873687365001)을 모니터링하므로 WhatsApp 옵트인 및 옵트아웃을 처리하는 것이 중요하며, 낮은 등급은 메시지 한도가 줄어들 수 있습니다. <br><br>높은 품질 등급을 구축하는 한 가지 방법은 사용자가 귀하의 비즈니스를 차단하거나 신고하지 않도록 하는 것입니다. 이는 [고품질 메시징](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)(사용자에게 가치를 제공하는 것과 같은), 메시지 빈도를 조절하고 고객이 향후 커뮤니케이션 수신을 옵트아웃할 수 있도록 허용함으로써 수행할 수 있습니다. <br><br>이 페이지에서는 옵트인 및 옵트아웃 설정 방법과 "regex" 및 "is" 수정자의 차이를 다룹니다.

옵트인은 외부 소스 또는 SMS, 인앱 및 브라우저 메시지와 같은 Braze 방법에서 올 수 있습니다. 옵트아웃은 Braze 및 WhatsApp 마케팅 버튼에 설정된 키워드를 사용하여 처리할 수 있습니다. 옵트인 및 옵트아웃 설정에 대한 안내를 위해 다음 방법을 참조하십시오.

#### 옵트인 방법
- [Braze 외부 옵트인 방법](#external-to-braze-opt-in-methods)
  - [외부에서 구축된 옵트인 목록](#externally-built-opt-in-list)
  - [고객 지원 WhatsApp 채널의 아웃바운드 메시지](#outbound-message-in-customer-support-whatsapp-channel)
  - [인바운드 WhatsApp 메시지](#inbound-whatsapp-message)
- [Braze 기반 옵트인 방법](#braze-powered-opt-in-methods)

#### 옵트아웃 방법
- [일반 옵트아웃 키워드](#general-opt-out-keywords)
- [마케팅 옵트아웃 선택](#marketing-opt-out-selection)

## Braze WhatsApp 채널에 대한 옵트인 설정하기

WhatsApp 옵트인에 대해서는 [WhatsApp의 요구 사항](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 준수해야 합니다. Braze에 다음 정보를 제공해야 합니다:
- 모든 사용자에 대한 `external_id`, [전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/), 및 업데이트된 구독 상태. 이는 [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)를 사용하거나 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 통해 전화번호와 구독 상태를 업데이트하여 수행할 수 있습니다.

{% alert note %}
Braze는 `/users/track` 엔드포인트에 대한 개선 사항을 발표했으며, 이를 통해 구독 상태를 업데이트할 수 있으며, [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)에서 자세히 알아볼 수 있습니다. 그러나 [`/v2/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)를 사용하여 이미 옵트인 프로토콜을 생성한 경우, 그곳에서 계속 진행할 수 있습니다.
{% endalert %}

### Braze 외부 옵트인 방법

귀하의 앱 또는 웹사이트(계정 등록, 체크아웃 페이지, 계정 설정, 신용 카드 단말기)에서 Braze로.

이메일 또는 문자에 대한 마케팅 동의가 이미 있는 곳에 WhatsApp을 위한 추가 섹션을 포함하세요. 사용자가 옵트인한 후에는 `external_id`, [전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/), 및 업데이트된 구독 상태가 필요합니다. 이를 위해 Braze 설치 방식에 따라 [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)를 활용하거나 [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)를 사용하세요.

#### 외부에서 구축된 옵트인 목록

이전에 WhatsApp을 사용한 경우, WhatsApp 요구 사항에 따라 옵트인이 있는 사용자 목록을 이미 구축했을 수 있습니다. 이 경우, CSV를 업로드하거나 [다음 정보]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)을 Braze에 API를 통해 사용하세요.

#### 고객 지원 WhatsApp 채널의 아웃바운드 메시지

고객 지원 채널에서 해결된 문제에 대해 후속 조치를 취하고, 마케팅 메시지에 옵트인할 것인지 자동 메시지로 문의하세요. 여기 기능은 선택한 고객 지원 도구의 기능 가용성 및 사용자 정보를 저장하는 위치에 따라 다릅니다.

1. WhatsApp 비즈니스 전화번호에서 [메시지 링크](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)를 제공하세요.
2. 고객이 "예"라고 답하여 옵트인하는 [빠른 응답 작업]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies)을 제공하세요.
3. 사용자 정의 키워드 트리거를 설정하세요.
4. 이 두 가지 아이디어 중 하나에 대해 다음으로 경로를 마무리해야 할 것입니다:
	- 사용자를 업데이트하거나 생성하기 위해 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)을 호출하세요.
	- [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)을 활용하거나 [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)를 사용하세요.

#### 수신 WhatsApp 메시지 

고객이 WhatsApp 번호로 수신 메시지를 보내도록 하세요.

사용자가 새로운 채널에서 확인 메시지를 받기를 원하는지에 따라 캔버스 또는 캠페인으로 설정할 수 있습니다.

1. 수신 메시지의 작업 기반 전달 트리거로 캠페인을 만드세요.
2. 웹훅 캠페인을 만드세요. 예시 웹훅은 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status)을 참조하세요.

{% alert tip %}
WhatsApp 채널에 가입하기 위해 [WhatsApp 관리자](https://business.facebook.com/wa/manage/phone-numbers/)의 **전화번호** > **메시지 링크**에서 URL 또는 QR 코드를 생성할 수 있습니다.<br>\![WhatsApp QR 코드 작성기.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze 기반 옵트인 방법 

#### SMS 메시지

캔버스에서 고객에게 WhatsApp 메시지를 수신하기 위해 옵트인할 것인지 묻는 캠페인을 설정하세요. 다음 방법 중 하나를 사용하세요:
- 고객 세그먼트: 미국 외의 마케팅 그룹에 가입한 고객
- 사용자 정의 키워드 트리거 설정

사용자 프로필의 구독 상태를 업데이트하는 방법에 대해 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)을(를) 확인하세요.

#### 앱 내 또는 브라우저 내 메시지

고객에게 WhatsApp 사용을 선택하도록 유도하는 앱 내 메시지 또는 브라우저 팝업을 생성하세요.

Braze SDK와 인터페이스하기 위해 [HTML 앱 내 메시지](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)와 [JavaScript "브리지"]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge)를 사용하세요. WhatsApp 구독 그룹 ID를 사용해야 합니다. 

#### 전화번호 수집 양식

사용자 전화번호를 수집하고 WhatsApp 구독 그룹을 늘리기 위해 앱 내 메시지의 드래그 앤 드롭 편집기에서 [전화번호 수집 양식]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) 템플릿을 사용하세요.

## Braze WhatsApp 채널에 대한 옵트아웃 설정

### 일반 옵트아웃 키워드

특정 단어로 메시지를 보내는 사용자가 향후 메시지 수신을 옵트아웃할 수 있도록 캠페인이나 캔버스를 설정할 수 있습니다. 캔버스는 성공적인 옵트아웃을 확인하는 후속 메시지를 포함할 수 있어 특히 유용합니다. 

#### 1단계: "수신 WhatsApp 메시지" 트리거로 캔버스를 생성하세요.
 
\![WhatsApp 수신 메시지를 보내는 사용자를 입력하는 액션 기반 캔버스 진입 단계.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

키워드 트리거를 선택할 때 "중지" 또는 "메시지 없음"과 같은 단어를 포함하세요. 이 방법을 선택하는 경우 고객이 옵트아웃 단어를 알고 있는지 확인하세요. 예를 들어, 초기 옵트인 후 "이 메시지에서 옵트아웃하려면 언제든지 "중지"라고 메시지를 보내세요."와 같은 후속 응답을 포함하세요. 

\![메시지 본문이 "STOP" 또는 "NO MESSAGE"인 WhatsApp 수신 메시지를 보내는 단계.]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### 2단계: 사용자 프로필을 업데이트하세요.

사용자가 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)에 설명된 방법 중 하나를 사용하여 프로필을 업데이트합니다.

### 마케팅 옵트아웃 선택

WhatsApp 메시지 템플릿 생성기 내에서 "마케팅 옵트아웃" 옵션을 포함할 수 있습니다. 이것을 포함할 때마다 템플릿이 구독 그룹 변경을 위한 후속 단계가 있는 캔버스에서 사용되도록 하십시오. 

1. "마케팅 옵트아웃" 빠른 응답으로 메시지 템플릿을 만듭니다.<br>\!["마케팅 옵트아웃"의 바닥글 옵션이 있는 메시지 템플릿]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>\![마케팅 옵트아웃 버튼을 구성하는 섹션.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. 이 메시지 템플릿을 사용하는 캔버스를 만듭니다.<br><br>
3. 이전 예제의 단계를 따르되 트리거 텍스트는 "STOP PROMOTIONS"로 설정합니다.<br><br>
4. 사용자의 구독 상태를 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)에 설명된 방법 중 하나를 사용하여 업데이트합니다.

## 옵트인 및 옵트아웃 워크플로우 설정

이 두 가지 방법으로 WhatsApp에 대해 "START" 및 "STOP" 키워드 응답 워크플로우를 구성할 수 있습니다:

- [사용자 업데이트 단계](#user-update-step)
- [두 번째 WhatsApp 캠페인을 트리거하는 웹훅 캠페인](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### 사용자 업데이트 단계

[사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)는 사용자가 구독 그룹의 전화번호로 키워드를 보낼 때 사용자의 전화번호를 WhatsApp 구독 그룹에 추가할 수 있습니다.

사용자 업데이트 단계는 사용자의 전화번호가 구독 그룹에 추가되기 전에 사용자가 캔버스의 다음 단계로 진행하지 않도록 하여 경쟁 조건을 피합니다. 또한 다른 방법보다 설정 단계가 적기 때문에 Braze는 일반적으로 이 방법을 권장합니다.

1. 액션 기반 단계 **WhatsApp 수신 메시지 전송**가 있는 캔버스를 만듭니다. **메시지 본문이 있는 위치**를 선택하고 **Is**에 대해 "START"를 입력합니다.

{% alert important %}
"STOP" 메시지의 경우, 옵트아웃을 확인하는 메시지 단계와 사용자 업데이트 단계를 반전시킵니다. 그렇지 않으면 사용자가 먼저 구독 그룹에서 옵트아웃되고, 확인 메시지를 받을 수 없게 됩니다.
{% endalert %}

\![메시지 본문이 "START"인 WhatsApp 메시지 단계.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. 캔버스에서 **사용자 업데이트 설정** 단계를 만들고 **작업**에 대해 **고급 JSON 편집기**를 선택합니다. <br><br>\!["고급 JSON 편집기" 작업을 가진 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. 다음 JSON 페이로드로 **사용자 업데이트 객체**를 채우고 `XXXXXXXXXXX`를 구독 그룹 ID로 교체합니다:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4\. 후속 WhatsApp 메시지 단계를 추가합니다. <br><br>\![캔버스의 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### 고려사항

업데이트는 Braze가 [사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) 요청을 배치하기 때문에 가변 속도로 완료될 수 있습니다.

### 두 번째 WhatsApp 캠페인을 트리거하는 웹훅 캠페인

웹훅 캠페인은 사용자가 구독 그룹의 전화번호로 키워드를 보낼 때 사용자의 전화번호를 WhatsApp 구독 그룹에 추가한 후 두 번째 캠페인에 진입하도록 트리거할 수 있습니다.

{% alert important %}
STOP 메시지에 이 방법을 사용할 필요는 없습니다. 확인 메시지는 사용자가 구독 그룹에서 제거되기 전에 전송되므로 다른 두 단계 중 하나를 사용할 수 있습니다.
{% endalert %}

1. 작업 기반 단계 **WhatsApp 수신 메시지 전송**으로 캠페인 또는 캔버스를 만듭니다. **메시지 본문이 있는 위치**를 선택하고 **Is**에 대해 "START"를 입력합니다.

\![메시지 본문이 "START"인 WhatsApp 메시지 단계.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. 캠페인 또는 캔버스에서 웹훅 메시지 단계를 만들고 **요청 본문**을 **원시 텍스트**로 변경합니다.

\![웹훅을 위한 메시지 단계.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. 고객의 [엔드포인트 URL]({{site.baseurl}}/api/basics/)을 **웹훅 URL**에 입력하고 엔드포인트 링크 `campaigns/trigger/send`를 추가합니다. 예를 들어, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

\!["웹훅 작성" 섹션 아래의 웹훅 URL 필드.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. 원시 텍스트에 다음 JSON 페이로드를 입력하고 `XXXXXXXXXXX`를 구독 그룹 ID로 교체합니다. 두 번째 캠페인을 만든 후 `campaign_id`을 교체해야 합니다.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5\. WhatsApp 캠페인(두 번째 캠페인)을 만들고 트리거를 API로 설정합니다. 이 `campaign_id`를 첫 번째 캠페인의 JSON 페이로드에 복사해야 합니다.

#### 고려사항

- 캔버스 API 트리거 JSON 페이로드 내의 속성 업데이트는 아직 지원되지 않으므로 WhatsApp 응답 메시지(2단계와 같이)에 대한 WhatsApp 캠페인만 트리거할 수 있습니다.
- WhatsApp 템플릿은 응답 메시지로 보내기 위해 승인되어야 합니다. 빠른 응답은 수신 메시지 트리거가 동일한 캠페인 또는 캔버스 내에 있어야 하기 때문에 발생합니다. [사용자 업데이트 단계](#user-update-step)을 사용하면 메타 승인 없이 빠른 응답 메시지를 보낼 수 있습니다.

## "regex"와 "is" 수정자의 차이를 이해하기

이 표에서 `STOP`은 수정자가 작동하는 방식을 보여주기 위한 예제 트리거 단어로 사용됩니다.

| 수정자 | 트리거 단어 | 작업 |
| --- | --- | --- |
| `Is` | `STOP` | 대소문자에 관계없이 "stop"의 전체 단어 사용을 포착합니다. 예를 들어, 이것은 "정지"를 잡지만 "제발 정지"는 잡지 않습니다. |
| `Matches regex` | `STOP` | 정확한 대문자에서 "정지"의 모든 사용을 잡습니다. 예를 들어, 이것은 "정지"와 "제발 정지"를 잡지만 "stop"은 잡지 않습니다. |
| `Matches regex` | `(?i)STOP(?-i)` | 모든 대문자에서 "정지"의 모든 사용을 잡습니다. 예를 들어, 이것은 "정지", "제발 정지", 그리고 "메시지를 보내는 것을 절대 멈추지 마세요"를 잡습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

