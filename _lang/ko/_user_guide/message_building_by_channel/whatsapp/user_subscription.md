---
nav_title: "구독 그룹"
article_title: WhatsApp 구독 그룹
page_order: 1
description: "이 도움말에서는 WhatsApp 구독 그룹, 제공되는 가입 상태, 구독 그룹 설정 방법에 대해 간략하게 설명합니다."
page_type: reference
channel:
  - WhatsApp
 
---

# 구독 그룹

> WhatsApp 구독 그룹은 **기술 파트너 포털**을 통해 WhatsApp을 앱과 통합하면 생성됩니다.

## WhatsApp 구독 상태

WhatsApp 사용자에게는 `subscribed` 와 `unsubscribed` 두 가지 구독 상태가 있습니다.

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 사용자가 특정 회사로부터 WhatsApp 메시지를 받고 싶다는 의사를 명시적으로 확인했습니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 WhatsApp의 가이드라인에 따라 옵트인 전략을 배포하여 구독할 수 있습니다. |
| 탈퇴됨 | 사용자가 명시적으로 옵트인 동의를 하지 않았거나 옵트인 상태가 명시적으로 삭제된 경우. <br><br> WhatsApp 구독 그룹에서 탈퇴한 사용자는 더 이상 해당 그룹에 속한 전화번호로 보낸 WhatsApp 메시지를 받지 않게 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 사용자의 WhatsApp 구독 그룹 설정

- **Rest API:** 고객 프로필은 [`/subscription/status/set` 엔드포인트][4]에서 Braze REST API를 사용하여 프로그래밍 방식으로 설정할 수 있습니다.
- **웹 SDK:** Users can be added to an email, SMS, or WhatsApp subscription group using the `addToSubscriptionGroup` method for [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), or [Web][11].
- **사용자 가져오기**: **사용자 가져오기를** 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 구독 그룹 상태를 업데이트할 때는 CSV에 `subscription_group_id` 및 `subscription_state` 두 개의 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) 참조하세요.

### 사용자의 WhatsApp 구독 그룹 확인

- **사용자 프로필:** 개별 고객 프로필은 **오디언스** > **사용자 검색**에서 Braze 대시보드를 통해 액세스할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 아이디로 사용자 프로필을 조회할 수 있습니다. 사용자 프로필에 들어가면 **참여** 탭에서 사용자의 WhatsApp 가입 그룹과 상태를 볼 수 있습니다.

- **Rest API:** 개별 고객 프로필 구독 그룹은 [사용자의 구독 그룹 목록 엔드포인트][9] 또는 [사용자의 구독 그룹 상태 목록 엔드포인트][8]에서 Braze REST API를 사용하여 확인할 수 있습니다. 

## WhatsApp 옵트인 및 옵트아웃 프로세스

현재 사용자는 웹사이트, WhatsApp 스레드, 전화 또는 직접 방문을 통해 [SMS를](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) 포함한 다양한 방법으로 WhatsApp 메시징을 구독하고 [옵트인 및 옵트아웃할]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) 수 있습니다. 옵트인(동의)이 필요합니다.

현재 WhatsApp 채널에서는 옵트인 키워드가 지원되지 않으므로 사용자 목록을 유지 관리하는 것은 사용자의 몫입니다. WhatsApp은 옵트인 및 요금 한도에 대한 소급 적용 방식을 채택하고 있어, 사용자가 신고 또는 차단을 시작하면 요금 한도가 낮아집니다. 

## 사용자의 WhatsApp 캔버스에 대한 구독 상태 업데이트하기 {#update-subscription-status}

사용하는 옵트인 및 옵트아웃 방법에 관계없이 다음 업데이트 방법 중 하나를 사용하여 사용자 프로필의 구독 상태를 업데이트할 수 있습니다:

- 다음 예시와 같이 REST API를 통해 구독 상태를 업데이트하는 [Braze-to-Braze 웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know)을 만듭니다.

![][1]{: style="max-width:90%;"}

경합 조건을 피하려면 웹훅 이후의 모든 후속 메시지는 첫 번째 캔버스의 결과에 의해 트리거되는 두 번째 캔버스에 포함되어야 합니다(예: 사용자가 캔버스 변형을 입력했고 WhatsApp 구독 그룹에 있는 경우).

- 고급 JSON 편집기를 사용하여 다음 템플릿으로 사용자 프로필을 업데이트합니다: 

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

![][2]{: style="max-width:90%;"}

{% alert note %}
사용자의 구독 상태를 업데이트하는 데 최대 60초가 걸릴 수 있습니다.
{% endalert %}

[1]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}
[4]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]:https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
