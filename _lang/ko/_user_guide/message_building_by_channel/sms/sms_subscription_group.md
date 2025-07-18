---
nav_title: "SMS 구독 그룹"
article_title: SMS 구독 그룹
page_order: 4
description: "이 참조 문서에서는 SMS 구독 그룹, 수신 상태 및 구독 그룹 설정 프로세스에 대해 설명합니다."
page_type: reference
channel:
  - SMS
  
---

# SMS 구독 그룹

> 구독 그룹은 Braze를 통해 SMS 및 MMS를 전송하기 위한 기반입니다. 가입 그룹은 특정 유형의 메시징 목적으로 사용되는 [발신 전화번호][2](예: 짧은 코드, 긴 코드 또는 영숫자 발신자 ID)의 모음입니다. 예를 들어, 브랜드에서 거래 및 프로모션 SMS 메시지를 모두 전송할 계획이 있는 경우, Braze 대시보드 내에서 별도의 전송 전화번호 풀을 가진 두 개의 구독 그룹을 설정해야 합니다.

## SMS 구독 상태

SMS 사용자의 구독 상태는 `subscribed` 와 `unsubscribed` 두 가지입니다. 사용자의 구독 상태는 구독 그룹 간에 공유되지 않으므로 사용자는 트랜잭션 구독 그룹에는 `subscribed`, 프로모션 구독 그룹에는 `unsubscribed` 일 수 있습니다. 브랜드 입장에서는 이러한 상태 분리를 통해 사용자에게 관련성 있는 SMS 메시지를 계속 보낼 수 있습니다.

| 상태 | 정의 |
| --------- | ---------- |
| 가입됨 | 사용자가 특정 구독 그룹으로부터 SMS 수신을 원한다고 명시적으로 확인했습니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 옵트인 키워드 응답을 문자로 전송하여 구독할 수 있습니다. SMS를 수신하려면 사용자가 SMS 수신 그룹에 가입되어 있어야 합니다. |
| 탈퇴됨 | 사용자가 SMS 구독 그룹 및 구독 그룹 내 발신 전화번호의 메시지를 명시적으로 수신 거부한 경우. 사용자는 옵트아웃 키워드 응답을 문자로 전송하여 구독을 취소하거나 브랜드가 [Braze 구독 API][4]]를 통해 사용자의 구독을 취소할 수 있습니다. SMS 구독 그룹에서 수신 거부된 사용자는 더 이상 구독 그룹에 속한 발신 전화번호로 발송되는 모든 SMS를 수신하지 않습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 사용자의 SMS 수신 그룹 설정 방법 

- **Rest API:** 고객 프로필은 [`/subscription/status/set` 엔드포인트][4]에서 Braze REST API를 사용하여 프로그래밍 방식으로 설정할 수 있습니다.
- **SDK Integration** Users can be added to an email or SMS subscription group using the `addToSubscriptionGroup` method for [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), or [Web][11].
- **사용자 옵트인/옵트아웃 시 자동으로 처리됩니다:** 사용자가 기본 옵트인 또는 옵트아웃 [키워드][7]을 문자로 보내면 Braze는 자동으로 사용자의 구독 상태를 설정하고 업데이트합니다.
- **사용자 가져오기**: **사용자 가져오기를** 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 구독 그룹 상태를 업데이트할 때는 CSV에 `subscription_group_id` 와 `subscription_state` 두 개의 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) 참조하세요.

사용자 프로필에서 전화번호가 업데이트되면 새 전화번호는 사용자의 가입 그룹 상태를 상속받습니다. 전화번호가 Braze에 이미 존재하는 번호로 업데이트되면 기존 전화번호의 구독 상태가 상속됩니다.

예를 들어 사용자 A가 여러 가입 그룹에 가입되어 있는 전화번호를 가지고 있는데 그 전화번호가 사용자 B에게 추가되면 사용자 B는 동일한 가입 그룹에 가입됩니다. 사용자가 기존 구독을 상속받지 못하도록 하려면 사용자가 번호를 변경할 때마다 REST API를 통해 이전 번호의 구독 그룹을 재설정할 수 있습니다. 여러 사용자가 이 전화번호를 공유하면 모두 구독이 취소됩니다.

### 사용자의 SMS 수신 그룹을 확인하는 방법

- **사용자 프로필:** 개별 고객 프로필은 사이드바에서 사용자 검색을 선택하여 Braze 대시보드에서 액세스할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 아이디로 사용자 프로필을 조회할 수 있습니다. 고객 프로필의 인게이지먼트 탭에서 사용자의 SMS 구독 그룹을 볼 수 있습니다. 
- **Rest API:** 개별 고객 프로필 구독 그룹은 [사용자의 구독 그룹 목록 엔드포인트][9] 또는 [사용자의 구독 그룹 상태 목록 엔드포인트][8]에서 Braze REST API를 사용하여 확인할 수 있습니다. 

## 구독 그룹과 함께 보내기

Braze를 통해 SMS 캠페인을 시작하려면 다음 이미지와 같이 드롭다운에서 구독 그룹을 선택해야 합니다. 오디언스 필터가 선택되면 캠페인 또는 캔버스에 자동으로 추가되어 선택한 구독 그룹의 `subscribed` 사용자만 타겟 대상에 포함되도록 합니다. 국제 [통신 규정 준수 및 가이드라인][3]]을 준수하기 위해 Braze는 선택한 구독 그룹에 가입하지 않은 사용자에게는 절대로 SMS를 보내지 않습니다.  

![구독 그룹 드롭다운이 열려 있고 사용자가 "SMS용 메시징 서비스 A"를 강조 표시한 상태의 SMS 작성기입니다.][6]

## 설정 프로세스

SMS 온보딩 과정에서 Braze 온보딩 관리자가 대시보드 계정에 대한 구독 그룹을 설정합니다. 필요한 구독 그룹 수를 결정하고 적절한 발신 전화번호를 구독 그룹에 추가하기 위해 고객과 협력합니다. 가입 그룹을 설정하는 타임라인은 추가하는 전화번호 유형에 따라 다릅니다. 예를 들어, 짧은 코드 애플리케이션은 8~12주 정도 걸리는 반면, 긴 코드는 하루 안에 설정할 수 있습니다. Braze 대시보드 설정에 대해 궁금한 점이 있으면 Braze 담당자에게 문의하여 지원을 받으세요.  

## 구독 그룹 MMS 활성화

MMS 메시지를 보내려면 구독 그룹 내에서 하나 이상의 번호가 MMS를 보낼 수 있도록 설정되어 있어야 합니다. 이는 구독 그룹 옆에 있는 태그로 표시됩니다. 

!["SMS용 메시징 서비스 A"가 강조 표시된 구독 그룹 드롭다운이 표시됩니다. 항목 앞에는 "MMS" 태그가 붙습니다.][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
[11]:https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
