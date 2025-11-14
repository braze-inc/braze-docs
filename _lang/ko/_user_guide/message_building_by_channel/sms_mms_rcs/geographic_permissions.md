---
nav_title: "지리적 권한"
article_title: 지리적 권한
description: "이 문서에서는 지리적 권한의 국가 허용 목록에 대해 설명하며, 이를 통해 SMS, MMS 및 RCS를 전송할 수 있는 국가를 선택할 수 있습니다."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# 지리적 권한

> 지리적 권한은 메시지를 보낼 수 있는 국가에 대한 제어를 적용하여 보안을 강화하고 사기성 SMS, MMS 및 RCS 트래픽으로부터 보호합니다. 국가 허용 목록을 지정하여 SMS, MMS 및 RCS 메시지가 승인된 지역으로만 전송되도록 할 수 있습니다. 관리자만 국가 허용 목록을 변경할 수 있습니다. 관리자가 아닌 사용자는 구독 그룹이 보낼 수 있는 국가를 나타내는 허용 목록의 읽기 전용 버전에 액세스할 수 있습니다.

관리자는 허용 목록에 있는 국가를 구성할 수 있습니다. 국가 허용 목록은 [구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups/) 수준에서 구성됩니다. **오디언스** > **구독으로** 이동하여 SMS, MMS 또는 RCS 구독 그룹을 선택하면 액세스할 수 있습니다. 허용 목록은 **지리적 권한** 아래에 있습니다.

'국가 허용 목록'에서 여러 국가를 선택한 관리자의 편집 가능한 SMS 지리적 권한 섹션입니다.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### 국가 선택

드롭다운을 사용하여 허용 목록에 국가를 추가합니다. 가장 일반적인 SMS 및 RCS 국가는 상단에 표시되며, 그 외 국가는 아래에 표시됩니다. 텍스트 필드에 입력하여 국가를 검색할 수도 있습니다.

가장 일반적인 국가가 상단에 표시되는 '국가 허용 목록' 드롭다운이 표시됩니다.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

이전에 선택한 국가 옆의 각 확인란을 선택 취소하여 해당 국가를 제거합니다.

### 변경 사항 저장하기

**저장을** 선택하면 변경 사항이 적용됩니다. 허용 목록에서 국가를 삭제하면 해당 국가의 번호로 모든 SMS, MMS 및 RCS 메시지를 보낼 수 없게 됩니다.

\![허용 목록에서 삭제될 국가를 확인하는 경고 모달입니다.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 고위험 국가

특정 국가에서는 SMS 및 RCS 트래픽 폭증의 위험이 더 높습니다. 이러한 국가는 국가 드롭다운에 **고위험** 태그가 표시되어 있습니다.

아제르바이잔에 '고위험' 태그가 있는 국가 드롭다운이 표시됩니다.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

이러한 국가에서의 전송을 허용하는 경우 해당 국가를 허용 목록에 추가하기 전에 먼저 해당 국가에 대한 위험을 인지해야 합니다.

{% alert note %}
허용 목록에 있는 국가는 비즈니스 요구 사항을 지원하는 데 필요한 국가로만 제한하세요. 이렇게 하면 사기성 트래픽이 발생할 가능성을 최소화할 수 있습니다. SMS 트래픽 펌핑을 방지하는 방법에 대한 자세한 안내는 [SMS 트래픽 펌핑 사기 FAQ를]({{site.baseurl}}/sms_traffic_pumping_fraud/) 참조하세요.
{% endalert %}

## 차단된 전송의 가시성

허용 목록에 없는 국가로 보내려는 시도는 중단됩니다. 중단된 메시지는 [메시지 활동 로그와]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) [SMS 중단 메시지 참여 이벤트에]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 기록됩니다. 

차단된 전송으로 인해 중단된 메시지는 **중단된 메시지 오류로** 표시되며 "수신자의 전화번호가 차단된 국가에 있습니다."라는 메시지가 표시됩니다.

전화번호가 차단된 국가에 있기 때문에 차단된 여러 개의 SMS 전송을 보여주는 중단 로그가 표시됩니다.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

