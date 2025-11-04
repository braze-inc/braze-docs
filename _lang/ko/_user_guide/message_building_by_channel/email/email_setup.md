---
nav_title: 이메일 설정
article_title: 온보딩 이메일 설정
layout: dev_guide
page_order: 1
guide_top_header: "이메일 설정"
guide_top_text: "Braze는 이메일 캠페인 전송을 시작하는 데 도움을 줄 수 있습니다. 가이드를 따르거나 <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>이메일 온보딩</a> Braze 학습 과정을 확인하세요."
page_type: landing
description: "이 랜딩 페이지에는 IP 및 도메인 설정, IP 워밍업, 이메일 유효성 검사 등 이메일 캠페인 시작에 대한 리소스가 포함되어 있습니다."
channel: email

guide_featured_title: "섹션 기사"
guide_featured_list:
- name: "IP 및 도메인 설정"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "IP 워밍"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "이메일 유효성 검사"
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
- name: "배달 가능성 함정과 스팸 함정"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## 요구 사항

이메일 전송을 시작하기 전에 필요한 몇 가지 사항이 있습니다. 이러한 요구 사항에 대해 자세히 알아보려면 다음 표를 참조하세요.

| 요구 사항 | 설명 | 소스 |
|---|---|---|
| 전용 IP(인터넷 프로토콜)| 전용 IP는 단일 호스팅 계정에만 제공되는 고유한 인터넷 주소입니다. | Braze는 고객에게 전용 IP를 제공하여 이메일 발신자 평판을 관리할 수 있도록 합니다. Braze 온보딩에서 이를 설정할 수 있습니다.|
| 화이트 레이블 도메인 | 도메인과 하위 도메인으로 구성됩니다. 화이트라벨링을 사용하면 DKIM 및 SPF에 대한 이메일 인증 검사를 통과할 수 있습니다. | Braze 온보딩 팀에서 이러한 도메인을 생성해 주지만, 도메인의 이름은 직접 선택해야 합니다. |
| 하위 도메인 | 이는 이메일 주소 내의 도메인(예: "@news.company.com")을 세분화한 것입니다. 하위 도메인이 있으면 회사의 공식 이메일 평판을 손상시킬 수 있는 오류를 방지할 수 있습니다. | 온보딩 팀에서 생성해 주지만 하위 도메인의 이름은 직접 정해야 합니다. 현재 Braze 외부에서 사용 중인 하위 도메인은 사용할 수 없습니다. |
| IP 풀 | 이는 서로 다른 유형의 이메일(예: "프로모션" 및 "거래")의 평판을 분리하여 한 이메일의 평판이 다른 이메일에 영향을 미치는 것을 방지하고 더 높은 전달 가능성을 지원하는 데 사용되는 선택적 구성입니다. | 온보딩 팀에서 풀을 설정해 드립니다. Then, when composing your email, select your email's IP pool from the **IP Pool** dropdown on the **Target Audiences** page.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## IP 온난화

{% alert important %}
IP 워밍업은 이메일 설정 프로세스에서 **가장 중요한 단계입니다**. 첫 번째 단계는 아니지만(사실 마지막 단계입니다), IP 주소를 워밍업하지 않으면 보내는 모든 이메일이 스팸으로 전송되거나 다른 전송 장벽의 적용을 받게 된다는 점을 알려드리기 위해 이 단계를 안내해 드립니다.
{% endalert %}

[IP 워밍]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)은 첫 번째 배치에서 비교적 적은 수의 이메일을 발송한 다음 시간이 지남에 따라 일반적인 일일 발송량에 도달할 때까지 다음 배치에서 발송량을 조금씩 늘리는 것을 말합니다. 이 작업은 이메일 설정 과정의 맨 마지막에 수행됩니다.

소량의 이메일부터 시작하면 이메일 제공업체와 신뢰 관계를 구축하여 관련 사용자에게만 이메일을 보내고 있다는 것을 보여줄 수 있습니다. 인게이지먼트가 가장 높은 사용자에게 첫 번째 이메일을 보내면 제공업체에 대한 신뢰를 더 빨리 얻을 수 있습니다.

IP 워밍이 완료되면 [이메일 작성 및 전송을 시작할]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) 수 있습니다!

<br><br>