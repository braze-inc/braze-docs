---
nav_title: 전달 가능성의 함정 및 스팸 트랩
article_title: 전달 가능성의 함정 및 스팸 트랩
page_order: 7
page_type: reference
description: "이 참조 기사는 잠재적인 이메일 전달 가능성의 함정, 스팸 트랩 및 이를 피하는 방법을 다룹니다."
channel: email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}전달 가능성의 함정 및 스팸 트랩

귀하의 이메일 전달 가능성은 다음의 스팸 트랩 중 하나에 의해 영향을 받을 수 있습니다:

| 트랩 유형 | 설명 |
|---|---|
| 프리스틴 트랩 | 한 번도 사용된 적이 없는 이메일 주소 및 도메인입니다. |
| 재활용 트랩 | 원래 실제 사용자의 이메일 주소였지만 현재는 비활성 상태인 주소입니다. |
| 오타 트랩 | 일반적인 오타가 포함된 이메일 주소입니다. |
| 스팸 불만 | 고객이 귀하의 이메일을 스팸으로 표시할 때입니다. |
| 높은 반송률 | 수신자의 주소가 유효하지 않아 이메일이 지속적으로 배달되지 않을 때입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 스팸 트랩을 피하는 방법

확인된 옵트인 프로세스를 설정하면 이러한 트랩을 피할 수 있습니다. 초기 옵트인 이메일을 보내고 고객에게 메시지를 받고 싶어하는지 확인하도록 요청함으로써, 수신자가 귀하의 메시지를 듣고 싶어하고 실제 유효한 주소로 보내고 있음을 보장합니다. 스팸 트랩을 피하는 추가 방법은 다음과 같습니다:

1. 더블 옵트인 이메일을 보내십시오. 이 이메일은 사용자가 링크를 클릭하여 구독 선택을 확인해야 합니다.
2. 모범 사례로서, [선셋 정책]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/)을 구현하십시오.
3. **절대 이메일 목록을 구매하지 마십시오.** 

{% alert tip %}
Braze 고객 성공 및 배달 팀은 전 세계적으로 배달 가능성을 극대화하기 위해 모범 사례를 따르고 있는지 확인하는 데 도움을 줄 수 있습니다.
{% endalert %}

## 바운스 또는 스팸 목록에서 이메일 주소 제거하기

다음 엔드포인트를 사용하여 바운스된 이메일과 Braze 스팸 목록의 이메일을 제거할 수 있습니다:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)