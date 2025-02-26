---
nav_title: "SMS 지리적 허용"
article_title: SMS 지리적 허용
description: "이 문서는 SMS 지리적 권한에 대한 국가 허용 목록을 다루며, SMS를 전달할 수 있는 국가를 선택할 수 있습니다."
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# SMS 지리적 허용

> SMS 지리적 권한은 보안을 강화하고 SMS 메시지를 보낼 수 있는 국가에 대한 통제를 시행하여 사기성 SMS 트래픽으로부터 보호합니다. SMS 메시지가 승인된 지역으로만 전송되도록 국가 허용 목록을 지정할 수 있습니다. 관리자만 국가 허용 목록을 변경할 수 있습니다. 관리자가 아닌 사용자는 구독 그룹이 보낼 수 있는 국가를 나타내는 허용 목록의 읽기 전용 버전에 액세스할 수 있습니다.

![미국과 영국이 '국가 허용 목록'에 선택된 비관리자 사용자를 위한 읽기 전용 SMS 지리적 권한 섹션입니다.][6]{: style="max-width:80%;"}

## SMS 국가 허용 목록 구성

관리자인 경우 허용 목록에 있는 국가를 구성할 수 있습니다. 국가 허용 목록은 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) 수준에서 구성됩니다. **오디언스** > **구독**으로 이동하여 SMS 구독 그룹을 선택하면 액세스할 수 있습니다. 허용 목록은 **SMS 지리적 권한** 아래에 있습니다.

![관리자가 "국가 허용 목록"에서 호주, 캐나다 및 미국을 선택한 경우 편집 가능한 SMS 지리적 권한 섹션입니다.][1]{: style="max-width:80%;"}

### 국가 선택

드롭다운을 사용하여 허용 목록에 국가를 추가하십시오. 가장 일반적인 SMS 국가가 상단에 표시되고 다른 국가가 아래에 표시됩니다. 텍스트 필드에 입력하여 국가를 검색할 수도 있습니다.

![가장 일반적인 국가가 상단에 표시되는 "국가 허용 목록" 드롭다운입니다.][2]{: style="max-width:80%;"}

이전에 선택한 국가를 제거하려면 해당 상자 옆의 상자를 지우세요.

### 변경 사항 저장 중

변경 사항은 **저장**을 선택한 후 적용됩니다. 허용 목록에서 국가를 제거하면 해당 국가의 번호로 SMS 및 MMS 메시지를 보내는 것이 차단됩니다.

![허용 목록에서 삭제될 국가를 확인하는 경고 모달입니다.][3]{: style="max-width:70%;"}

## 고위험 국가

일부 국가에서는 SMS 트래픽 펌핑의 위험이 더 높습니다. 이들 국가는 국가 드롭다운에서 **고위험** 태그로 표시됩니다.

![아제르바이잔이 "고위험" 태그를 가지고 있는 국가입니다.][4]{: style="max-width:80%;"}

이들 국가에서 발송을 허용하려면, 해당 국가가 허용 목록에 추가되기 전에 먼저 그러한 위험을 인지해야 합니다.

{% alert note %}
허용 목록의 국가를 비즈니스 요구 사항을 지원하는 데 필요한 국가로만 제한하세요. 이것은 사기성 트래픽의 가능성을 최소화할 것입니다. SMS 트래픽 펌핑을 방지하기 위한 추가 지침은 [SMS 트래픽 펌핑 사기 FAQ]({{site.baseurl}}/sms_traffic_pumping_fraud/)를 참조하세요.
{% endalert %}

## 차단된 전송의 가시성

허용 목록에 없는 국가로의 전송 시도는 중단됩니다. 중단된 메시지는 [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) 및 [SMS 중단 메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)에 기록됩니다. 

차단된 전송으로 인해 중단된 메시지는 `Abort_Type = "blocked_recipient_country"`로 표시되며 중단 로그에는 차단된 국가가 자세히 나옵니다.

![차단된 수신자 국가의 abort_type과 차단된 전화번호의 국가 이니셜을 보여주는 중단 로그입니다.][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}