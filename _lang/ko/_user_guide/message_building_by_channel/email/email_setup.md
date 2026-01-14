---
nav_title: 이메일 설정
article_title: 온보딩 이메일 설정
layout: dev_guide
page_order: 1
guide_top_header: "이메일 설정"
guide_top_text: "브레이즈는 이메일 캠페인을 보내기 시작하는 데 도움을 줄 수 있습니다. 우리의 가이드를 따르거나 <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>이메일 온보딩</a> 브레이즈 학습 과정을 확인하세요."
page_type: landing
description: "이 랜딩 페이지에는 이메일 캠페인을 시작하는 데 필요한 리소스가 포함되어 있으며, IP 및 도메인 설정, IP 워밍, 이메일 검증 등을 포함합니다."
channel: email

guide_featured_title: "섹션 기사"
guide_featured_list:
- name: "IPs 및 도메인 설정"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "IP 워밍"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "이메일 검증"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "이메일 인증"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "이메일 목록 가져오기"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "SSL 개요"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "동의 및 주소 수집"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "전달 가능성 함정 및 스팸 트랩"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## 요구 사항

이메일을 보내기 시작하기 전에 필요한 몇 가지 사항이 있습니다. 다음 차트를 참조하여 이러한 요구 사항에 대해 자세히 알아보세요.

| 요구 사항 | 설명 | 소스 |
|---|---|---|
| 전용 IP (인터넷 프로토콜)| 전용 IP는 단일 호스팅 계정에 독점적으로 제공되는 고유한 인터넷 주소입니다. | Braze는 이메일 발신자 평판을 제어할 수 있도록 전용 IP를 제공합니다. Braze 온보딩이 이를 설정해 드립니다.|
| 화이트라벨 도메인 | 이들은 도메인과 서브도메인으로 구성됩니다. 화이트라벨링을 사용하면 DKIM 및 SPF에 대한 이메일 인증 검사를 통과할 수 있습니다. | Braze 온보딩 팀이 이 도메인을 생성해 드리지만, 이름은 선택해야 합니다. |
| 서브도메인 | 이는 이메일 주소 내의 도메인(예: "@news.company.com")의 하위 구분입니다. 서브도메인을 사용하면 회사의 공식 이메일 평판에 손상을 줄 수 있는 오류를 방지할 수 있습니다. | 온보딩 팀이 이를 생성해 드리지만, 서브도메인 이름은 결정해야 합니다. 현재 Braze 외부에서 사용 중인 서브도메인은 사용할 수 없습니다. |
| IP 풀 | 이들은 서로 다른 유형의 이메일(예: "프로모션" 및 "거래")의 평판을 분리하는 데 사용되는 선택적 구성으로, 하나의 평판이 다른 평판에 영향을 미치는 것을 방지하고 더 높은 배달 가능성을 지원합니다. | 온보딩 팀이 풀을 설정해 드립니다. 그런 다음 이메일을 작성할 때 **대상 청중** 단계에서 이메일의 IP 풀을 볼 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## IP 워밍

{% alert important %}
IP 워밍은 이메일 설정 과정에서 **가장 중요한 단계**입니다. 비록 그것이 첫 번째 단계는 아니지만(실제로는 마지막 단계입니다), 당신의 IP 주소를 워밍업해야 한다는 것을 알려주기 위해 여기서 언급하고 있습니다. 그렇지 않으면 당신이 보내는 이메일은 스팸으로 분류되거나 다른 전송 장벽에 직면할 것입니다.
{% endalert %}

[IP 워밍]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)은 첫 번째 배치에서 상대적으로 적은 수의 이메일을 보내고, 시간이 지남에 따라 다음 배치에서 볼륨을 조금씩 증가시켜 일반적인 일일 볼륨에 도달하는 것입니다. 이는 이메일 설정 과정의 마지막 단계에서 수행됩니다.

작은 볼륨의 이메일로 시작함으로써, 당신은 이메일 제공자와의 신뢰 수준을 구축하고, 관련 사용자에게만 이메일을 보내고 있음을 보여줍니다. 가장 참여도가 높은 사용자에게 첫 번째 배치의 이메일을 보내는 것은 제공자와의 신뢰를 더 빨리 얻는 데 도움이 될 수 있습니다.

IP 워밍이 끝나면 [이메일을 만들고 보내기 시작할 수 있습니다]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)!

<br><br>
