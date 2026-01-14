---
nav_title: "구독 그룹"
article_title: WhatsApp 구독 그룹
page_order: 1
description: "이 문서에서는 WhatsApp 구독 그룹, 제공되는 구독 상태 및 구독 그룹 설정 방법에 대해 설명합니다."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp
 
---

# 구독 그룹

> WhatsApp 구독 그룹은 **기술 파트너 포털**을 통해 WhatsApp을 앱에 통합할 때 생성됩니다.

## WhatsApp 구독 상태

WhatsApp 사용자에게는 두 가지 구독 상태가 있습니다: `subscribed` 및 `unsubscribed`.

| 상태 | 정의 |
| --- | --- |
| 구독됨 | 사용자가 특정 회사로부터 WhatsApp 메시지를 수신하기를 원한다고 명시적으로 확인했습니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 WhatsApp의 가이드라인에 따라 옵트인 전략을 배포하여 구독될 수 있습니다. |
| 구독 취소됨 | 사용자가 옵트인에 대한 명시적인 동의를 주지 않았거나 옵트인 상태가 명시적으로 제거되었습니다. <br><br> WhatsApp 구독 그룹에서 구독 취소된 사용자는 구독 그룹에 속한 발신 전화번호로부터 더 이상 WhatsApp 메시지를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 사용자의 WhatsApp 구독 그룹 설정

- **REST API:** 사용자 프로필은 Braze REST API를 사용하여 [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)로 프로그래밍 방식으로 설정할 수 있습니다.
- **웹 SDK:** 사용자는 `addToSubscriptionGroup` 방법을 사용하여 [안드로이드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) 또는 [웹](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)의 이메일, SMS 또는 WhatsApp 구독 그룹에 추가될 수 있습니다.
- **사용자 가져오기**: 사용자는 **사용자 가져오기**를 통해 이메일 또는 SMS 구독 그룹에 추가될 수 있습니다. 구독 그룹 상태를 업데이트할 때, CSV에 `subscription_group_id` 및 `subscription_state` 두 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)를 참조하십시오.

### 사용자의 WhatsApp 구독 그룹 확인 중

- **사용자 프로필:** 개별 사용자 프로필은 Braze 대시보드의 **청중** > **사용자 검색**를 통해 접근할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 ID로 사용자 프로필을 조회할 수 있습니다. 사용자 프로필 내에서 **참여** 탭 아래에서 사용자의 WhatsApp 구독 그룹 및 상태를 볼 수 있습니다.

- **REST API:** 개별 사용자 프로필 구독 그룹은 Braze의 REST API를 사용하여 [사용자의 구독 그룹 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) 또는 [사용자의 구독 그룹 상태 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)를 통해 볼 수 있습니다. 

## WhatsApp 옵트인 및 옵트아웃 프로세스

현재 사용자는 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)을 포함하여 다양한 방법으로 WhatsApp 메시징에 구독할 수 있습니다: [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), 웹사이트, WhatsApp 스레드, 전화 또는 대면으로. 옵트인은 필수입니다.

WhatsApp 채널에 대한 옵트인 키워드는 현재 지원되지 않으므로 사용자 목록을 유지하는 것은 귀하에게 달려 있습니다. WhatsApp은 옵트인 및 비율 제한에 대한 회고적 접근 방식을 가지고 있으며, 사용자가 귀하를 신고하거나 차단하기 시작하면 비율 제한이 낮아집니다. 

## 사용자의 구독 상태를 WhatsApp 캔버스 {#update-subscription-status}로 업데이트

사용하는 옵트인 및 옵트아웃 방법에 관계없이, 다음 업데이트 방법 중 하나로 사용자 프로필의 구독 상태를 업데이트할 수 있습니다:

- 구독 상태를 REST API를 통해 업데이트하는 [Braze-to-Braze 웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know)을 생성하십시오. 다음 예와 같이:

\![POST 방법을 사용하는 메시지로 웹훅 작성기.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

경쟁 조건을 피하기 위해, 웹훅 이후의 모든 후속 메시지는 첫 번째 캔버스의 결과에 의해 트리거되는 두 번째 캔버스에 포함되어야 합니다(예: 사용자가 캔버스 변형에 들어가고 WhatsApp 구독 그룹에 있는 경우).

- 고급 JSON 편집기를 사용하여 다음 템플릿으로 사용자 프로필을 업데이트하십시오: 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

\![고급 JSON 편집기 단계로 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
사용자의 구독 상태 업데이트는 최대 60초가 소요될 수 있습니다.
{% endalert %}

