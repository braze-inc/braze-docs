---
nav_title: "지리적 권한"
article_title: 지리적 권한
description: "이 문서에서는 SMS, MMS 및 RCS를 전달할 수 있는 국가 허용 목록에 대해 설명합니다."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# 지리적 권한

> 지리적 권한은 메시지를 보낼 수 있는 국가에 대한 제어를 시행하여 사기성 SMS, MMS 및 RCS 트래픽으로부터 보호하고 보안을 강화합니다. SMS, MMS 및 RCS 메시지가 승인된 지역에만 전송되도록 국가 허용 목록을 지정할 수 있습니다. 관리자만 국가 허용 목록을 변경할 수 있습니다. 관리자가 아닌 사용자는 구독 그룹이 보낼 수 있는 국가를 나타내는 허용 목록의 읽기 전용 버전에 액세스할 수 있습니다.

관리자인 경우 허용 목록에 있는 국가를 구성할 수 있습니다. 국가 허용 목록은 [구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups/) 수준에서 구성됩니다. **오디언스** > **구독**으로 이동하여 SMS, MMS 또는 RCS 구독 그룹을 선택하여 액세스할 수 있습니다. 허용 목록은 **지리적 권한** 아래에 있습니다.

![여러 국가가 "국가 허용 목록"에 선택된 관리자를 위한 편집 가능한 SMS 지리적 권한 섹션입니다.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### 국가 선택

드롭다운을 사용하여 허용 목록에 국가를 추가하십시오. 가장 일반적인 SMS 및 RCS 국가가 상단에 표시되며, 다른 국가들은 아래에 표시됩니다. 텍스트 필드에 입력하여 국가를 검색할 수도 있습니다.

![가장 일반적인 국가가 상단에 표시되는 '국가 허용 목록' 드롭다운.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

이전에 선택한 국가를 제거하려면 해당 상자 옆의 상자를 지우세요.

### 변경 사항 저장 중

변경 사항은 **저장**을 선택한 후 적용됩니다. 허용 목록에서 국가를 제거하면 해당 국가의 번호로 SMS, MMS 및 RCS 메시지가 전송되지 않습니다.

![허용 목록에서 삭제될 국가를 확인하는 경고 모달입니다.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 고위험 국가

특정 국가는 SMS 및 RCS 트래픽 펌핑의 위험이 더 높습니다. 이들 국가는 국가 드롭다운에서 **고위험** 태그로 표시됩니다.

![아제르바이잔에 "높은 위험" 태그가 있는 국가 드롭다운입니다.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

이들 국가에서 발송을 허용하려면, 해당 국가가 허용 목록에 추가되기 전에 먼저 그러한 위험을 인지해야 합니다.

{% alert note %}
허용 목록의 국가를 비즈니스 요구 사항을 지원하는 데 필요한 국가로만 제한하세요. 이것은 사기성 트래픽의 가능성을 최소화할 것입니다. SMS 트래픽 펌핑을 방지하기 위한 추가 지침은 [SMS 트래픽 펌핑 사기 FAQ]({{site.baseurl}}/sms_traffic_pumping_fraud/)를 참조하세요.
{% endalert %}

## 차단된 전송의 가시성

허용 목록에 없는 국가로의 전송 시도는 중단됩니다. Aborted messages will be logged to the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) and within the [SMS abort message engagement event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

차단된 전송으로 인해 중단된 메시지는 **중단된 메시지 오류**로 표시되며 "수신자의 전화번호가 차단된 국가에 있습니다"라는 메시지가 표시됩니다.

![전화번호가 차단된 국가에 있어 차단된 여러 SMS 전송을 보여주는 중단 로그입니다.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

