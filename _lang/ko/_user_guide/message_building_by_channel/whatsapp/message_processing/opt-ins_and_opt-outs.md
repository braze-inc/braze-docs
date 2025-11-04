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

> WhatsApp 옵트인 및 옵트아웃 처리는 중요합니다. WhatsApp은 [전화번호 품질 등급](https://www.facebook.com/business/help/896873687365001)을 모니터링하며, 낮은 등급은 메시지 한도가 줄어들 수 있습니다. <br><br>고품질 평가를 구축하는 한 가지 방법은 사용자가 귀하의 비즈니스를 차단하거나 신고하지 못하도록 하는 것입니다. 이것은 [고품질 메시징](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)(사용자에게 가치를 제공하는 것과 같은), 메시지 빈도를 제어하고, 고객이 향후 통신 수신을 거부할 수 있도록 허용함으로써 수행할 수 있습니다. <br><br>이 페이지에서는 옵트인 및 옵트아웃 설정 방법과 "정규식" 및 "is" 수정자 간의 차이를 다룹니다.

옵트인은 외부 소스 또는 SMS나 인앱 및 브라우저 내 메시지와 같은 Braze 방법에서 올 수 있습니다. 수신 거부는 Braze 및 WhatsApp 마케팅 버튼에 설정된 키워드를 사용하여 처리할 수 있습니다. 다음 방법을 참조하여 옵트인 및 옵트아웃 설정에 대한 지침을 확인하십시오.

#### 옵트인 방법
- [Braze 외부 옵트인 방법](#external-to-braze-opt-in-methods)
  - [외부에서 작성된 옵트인 목록](#externally-built-opt-in-list)
  - [고객 지원 WhatsApp 채널의 아웃바운드 메시지](#outbound-message-in-customer-support-whatsapp-channel)
  - [인바운드 WhatsApp 메시지](#inbound-whatsapp-message)
- [Braze 기반 옵트인 방법](#braze-powered-opt-in-methods)

#### 옵트아웃 방법
- [일반 옵트아웃 키워드](#general-opt-out-keywords)
- [마케팅 opt-out selection](#marketing-opt-out-selection)

## Braze WhatsApp 채널에 옵트인을 설정하세요

WhatsApp 옵트인에 대해서는 [WhatsApp의 요구 사항](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 준수해야 합니다. 다음 정보를 Braze에 제공해야 합니다:
- [전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)인 `external_id` 및 모든 사용자의 업데이트된 가입 상태. This can be done by using the [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) or through the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update the phone number and subscription status.

{% alert note %}
Braze는 `/users/track` 엔드포인트에 대한 개선 사항을 발표하여 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)에서 배울 수 있는 구독 상태 업데이트를 허용합니다. 그러나 [`/v2/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)를 사용하여 이미 옵트인 프로토콜을 생성한 경우 계속해서 해당 엔드포인트를 사용할 수 있습니다.
{% endalert %}

### Braze 외부 옵트인 방법

귀하의 앱 또는 웹사이트(계정 등록, 결제 페이지, 계정 설정, 신용 카드 단말기)를 Braze에 연결하십시오.

이미 이메일 또는 문자 메시지에 대한 마케팅 동의가 있는 경우 WhatsApp에 대한 추가 섹션을 포함하세요. 사용자가 옵트인한 후에는 `external_id`, [전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/), 업데이트된 구독 상태가 필요합니다. To do this, depending on how your install of Braze is set up, either leverage the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) or use the [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### 외부에서 작성된 옵트인 목록

이전에 WhatsApp을 사용한 적이 있다면, WhatsApp 요구 사항에 따라 이미 옵트인된 사용자 목록을 작성했을 수 있습니다. 이 경우 CSV를 업로드하거나 [다음 정보]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)를 사용하여 API를 Braze에 사용하십시오.

#### 고객 지원 WhatsApp 채널의 아웃바운드 메시지

고객 지원 채널에서 해결된 문제에 대해 자동 메시지를 보내 마케팅 메시징에 옵트인할지 여부를 묻습니다. 여기서 기능은 고객 지원 도구의 선택과 사용자 정보를 보관하는 위치에 따라 달라집니다.

1. 귀하의 WhatsApp 비즈니스 전화번호에서 [메시지 링크](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)를 제공하십시오.
2. 고객이 옵트인을 나타내기 위해 "예"라고 응답하는 [빠른 응답 작업]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies)을 제공하세요
3. 커스텀 키워드 트리거를 설정합니다.
4. 그 아이디어 중 어느 것이든 다음과 같이 경로를 완료해야 할 것입니다.
	- [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 호출하여 사용자를 업데이트하거나 생성합니다
	- Leverage the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) or use the [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### 인바운드 WhatsApp 메시지 

고객이 WhatsApp 번호로 인바운드 메시지를 보내도록 하십시오.

이것은 사용자가 새 채널에서 확인 메시지를 받기를 원하는지 여부에 따라 캔버스 또는 캠페인으로 설정할 수 있습니다.

1. 실행 기반 전달 트리거가 포함된 인바운드 메시지 캠페인을 만드세요.
2. 웹훅 캠페인을 만드세요. 예제 웹훅에 대해서는 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status)을 참조하십시오.

{% alert tip %}
[WhatsApp 매니저](https://business.facebook.com/wa/manage/phone-numbers/) 내의 **전화번호** > **메시지 링크**에서 WhatsApp 채널에 가입할 수 있는 URL 또는 QR 코드를 구축할 수 있습니다.<br>WhatsApp QR 코드 컴포저.()
{% endalert %}

### Braze 기반 옵트인 방법 

#### SMS 메시지

캔버스에서 고객에게 WhatsApp 메시지 수신에 옵트인할 것인지 묻는 캠페인을 설정하려면 다음 방법 중 하나를 사용하세요.
- 고객 세그먼트: 미국 외부의 구독된 마케팅 그룹
- 커스텀 키워드 트리거 설정

사용자 프로필의 구독 상태를 업데이트하는 방법에 대해 알아보려면 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)을(를) 참조하세요.

#### 인앱 또는 인브라우저 메시지

인앱 메시지 또는 브라우저 내 팝업을 만들어 고객에게 WhatsApp 사용에 옵트인하도록 요청하세요.

[HTML 인앱 메시지](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)를 [JavaScript "bridge"]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge)와 함께 사용하여 Braze 소프트웨어 개발 키트와 인터페이스하십시오. WhatsApp 구독 그룹 ID를 사용하십시오. 

#### 전화번호 캡처 양식

드래그 앤 드롭 편집기에서 [전화번호 캡처 양식]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) 템플릿을 사용하여 앱 내 메시지로 사용자 전화번호를 수집하고 WhatsApp 구독 그룹을 성장시키세요.

## Braze WhatsApp 채널에 대한 옵트아웃 설정

### 일반 옵트아웃 키워드

사용자가 특정 단어를 메시지로 보내면 향후 메시징을 거부할 수 있도록 하는 캠페인 또는 캔버스를 설정할 수 있습니다. 캔버스는 성공적인 옵트아웃을 확인하는 후속 메시지를 포함할 수 있도록 해주기 때문에 특히 유용할 수 있습니다. 

#### 1단계: "인바운드 WhatsApp 메시지"의 트리거로 캔버스를 만드세요
 
![Action-based Canvas entry step that that enters users who send a WhatsApp inbound message.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

키워드 트리거를 선택할 때 "중지" 또는 "메시지 없음"과 같은 단어를 포함하세요. 이 방법을 선택하면 고객이 옵트아웃 단어를 알고 있는지 확인하세요. 예를 들어, 초기 옵트인을 받은 후에 "이 메시지를 옵트아웃하려면 언제든지 "중지"라고 메시지를 보내세요."와 같은 후속 응답을 포함하세요. 

![Message step to send a WhatsApp inbound message where the message body is "STOP" or "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### 2단계: 사용자의 프로필을 업데이트하십시오

[구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)에 설명된 방법 중 하나를 사용하여 사용자의 프로필을 업데이트하십시오.

### 마케팅 opt-out selection

WhatsApp 메시지 템플릿 생성기 내에서 "마케팅 옵트아웃" 옵션을 포함할 수 있습니다. 이것을 포함할 때마다 템플릿이 캔버스에서 사용되고 구독 그룹 변경을 위한 후속 단계가 있는지 확인하십시오. 

1. "마케팅 옵트아웃" 빠른 응답과 함께 메시지 템플릿을 만드세요.<br>![Message template with a footer option of "Marketing opt-out"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Section to configure a marketing oopt-out button.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. 이 메시지 템플릿을 사용하는 캔버스를 만드십시오.<br><br>
3. 앞의 예에서와 같이 단계를 따르되 트리거 텍스트 "STOP PROMOTIONS"를 사용하십시오.<br><br>
4. [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)에 설명된 방법 중 하나를 사용하여 사용자의 구독 상태를 업데이트하십시오.

## 옵트인 및 옵트아웃 워크플로우 설정

WhatsApp에 대해 "시작" 및 "중지" 키워드 응답 워크플로를 구성하려면 다음 두 가지 방법을 사용할 수 있습니다.

- [사용자 업데이트 단계](#user-update-step)
- [웹훅 캠페인으로 두 번째 WhatsApp 캠페인을 트리거합니다](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### 사용자 업데이트 단계

[사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)는 사용자가 키워드를 구독 그룹의 전화번호로 보낼 때 사용자의 전화번호를 WhatsApp 구독 그룹에 추가할 수 있습니다.

사용자 업데이트 단계는 사용자의 전화번호가 구독 그룹에 추가되기 전에 캔버스의 다음 단계로 진행되지 않기 때문에 경쟁 상태를 방지합니다. 또한 다른 방법보다 설정 단계가 적기 때문에 Braze는 일반적으로 이 방법을 권장합니다.

1. 캔버스를 만들고 작업 기반 단계 **WhatsApp 수신 메시지 보내기**를 수행합니다. **메시지 본문**을 선택하고 **Is**에 "START"를 입력합니다.

{% alert important %}
"중지" 메시지의 경우 메시지 단계를 반전하여 옵트아웃 확인 및 사용자 업데이트 단계를 수행합니다. 사용자가 그렇지 않으면 먼저 구독 그룹에서 선택 해제되고 확인 메시지를 받을 자격이 없게 됩니다.
{% endalert %}

![A WhatsApp message step where the message body is "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. 캔버스에서 **사용자 업데이트 설정** 단계를 만들고 **작업**에 대해 **고급 JSON 편집기**를 선택합니다. <br><br>![User Update step with an action of "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. 다음 JSON 페이로드로 **사용자 업데이트 개체**를 채우고 `XXXXXXXXXXX`를 구독 그룹 ID로 바꿉니다:

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
4\. WhatsApp 메시지 단계를 추가합니다. <br><br>![User Update step in a Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### 고려 사항

업데이트는 Braze가 [사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) 요청을 일괄 처리하기 때문에 다양한 속도로 완료될 수 있습니다.

### 웹훅 캠페인으로 두 번째 WhatsApp 캠페인을 트리거합니다

웹훅 캠페인은 사용자가 구독 그룹의 전화번호로 키워드를 보낼 때 사용자의 전화번호를 WhatsApp 구독 그룹에 추가한 후 두 번째 캠페인에 진입할 수 있습니다.

{% alert important %}
STOP 메시지에는 이 방법을 사용할 필요가 없습니다. 확인 메시지는 사용자가 구독 그룹에서 제거되기 전에 전송되므로 다른 두 단계 중 하나를 사용할 수 있습니다.
{% endalert %}

1. 캠페인 또는 캔버스를 생성하고 액션 기반 단계 **WhatsApp 인바운드 메시지 보내기**를 추가하세요. **메시지 본문**을 선택하고 **Is**에 "START"를 입력합니다.

![WhatsApp message step where the message body is "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. In the campaign or Canvas, create a Webhook Message step, and change the **Request Body** to **Raw Text**.

![Message step for a webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Enter the customer's [endpoint URL]({{site.baseurl}}/api/basics/) in the **Webhook URL**, followed by the endpoint link `campaigns/trigger/send`. For example, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Webhook URL field under the "Compose Webhook" section.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. In the raw text, enter the following JSON payload and replace `XXXXXXXXXXX` with your subscription group ID. You will need to replace the `campaign_id` after creating your second campaign.

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
5\. WhatsApp 캠페인(두 번째 캠페인)을 만들고 트리거를 API로 설정하세요. 이 `campaign_id`를 첫 번째 캠페인의 JSON 페이로드에 복사했는지 확인하세요.

#### 고려사항

- 캔버스 API 트리거 JSON 페이로드 내에서 속성 업데이트는 아직 지원되지 않으므로 WhatsApp 응답 메시지에 대한 WhatsApp 캠페인만 트리거할 수 있습니다(2단계에서와 같이).
- WhatsApp 템플릿은 응답 메시지로 보내기 위해 승인되어야 합니다. 이것은 빠른 응답이 동일한 캠페인 또는 캔버스 내에 인바운드 메시지 트리거가 있어야 하기 때문입니다. [사용자 업데이트 단계](#user-update-step)를 사용하면 Meta의 승인을 받지 않고도 빠른 응답 메시지를 보낼 수 있습니다.

## "정규식"과 "is" 수정자 간의 차이를 이해하기

이 표에서 `STOP`는 수정자가 작동하는 방식을 보여주기 위해 예시 트리거 단어로 사용됩니다.

| 수정자 | 트리거 단어 | 작업 |
| --- | --- | --- |
| `Is` | `STOP` | "stop"라는 단어의 대소문자에 관계없이 전체 단어 사용을 포착합니다. 예를 들어, 이것은 "멈춰"를 잡지만 "제발 멈춰"는 잡지 않습니다. |
| `Matches regex` | `STOP` | 그 경우 "STOP"의 사용을 모두 포착합니다. 예를 들어, 이것은 "stop"을 잡지만 "PLEASE STOP"은 잡지 않습니다. |
| `Matches regex` | `(?i)STOP(?-i)` | "STOP"의 모든 사용을 대소문자 구분 없이 포착합니다. 예를 들어, 이것은 "멈춰" , "제발 멈춰" , 그리고 "절대 나에게 메시지를 보내는 것을 멈추지 마"를 잡습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

