---
nav_title: 받은 편지함 몬스터
article_title: 받은 편지함 몬스터
alias: /partners/inbox_monster/
description: "이 참고 문서에서는 Braze와 온라인 이메일 마케팅 도구인 Inbox Monster의 파트너십에 대해 설명하며, 이를 통해 Braze 고객은 강력한 전달률 인사이트와 창의적인 분석을 통해 받은 편지함 성능을 향상시킬 수 있습니다."
page_type: partner
search_tag: Partner

---

# 받은 편지함 몬스터

> [인박스 몬스터는](https://inboxmonster.com/) 기업 브랜드가 모든 이메일을 수신할 수 있도록 도와주는 받은 편지함 신호 플랫폼입니다. It's an integrated suite of solutions for deliverability, creative rendering, and SMS monitoring, that empowers modern customer relationship management (CRM) teams and ends the sending scaries.

Braze와 Inbox Monster의 통합을 통해 수동 시드 리스트 테스트를 없애고, 강력하고 실행 가능한 받은 편지함 배치 신호를 자동으로 생성하며, 이메일 크리에이티브 자산 검토 및 승인 프로세스를 간소화하고, 귀중한 전달률 인사이트를 얻을 수 있습니다. 크리에이티브 진단 및 디바이스 미리보기를 위해 이메일 템플릿을 원활하게 가져올 수도 있습니다.

## 필수 조건

| 요구 사항                    | 설명                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 인박스 몬스터 플랫폼 계정 | 이 파트너십을 이용하려면 Inbox Monster 플랫폼 계정이 필요합니다.                                                                                                                                                                                                                                                                                                                                                                 |
| Braze REST API 키             | 다음 권한이 있는 Braze REST API 키입니다:  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> 그리고 다음과 같은 화이트리스트 IP를 사용합니다: <br> - `3.136.16.19` <br>  - `3.140.233.31`<br> - `18.220.127.138` <br><br> 이는 Braze 대시보드의 **설정** > **API 및 식별자** 탭의 **API 키에서** 생성할 수 있습니다. |
| Braze 앱 식별자           | Braze 앱 식별자입니다. <br><br>이는 Braze 대시보드의 **설정** > **API 및 식별자** 탭의 **앱 식별자** 탭에서 확인할 수 있습니다.                                                                                                                                                                                                                                                                                                |
| 브레이즈 엔드포인트                 | [Braze 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 URL에 맞춰 조정됩니다.<br><br> 예를 들어 대시보드 URL이 `https://dashboard-03.braze.com`인 경우 엔드포인트는 `dashboard-03`입니다.                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 통합

인박스 몬스터를 연동하려면 인박스 [몬스터와 연동하기의](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3) 단계를 따르세요.

## 사용량

받은 편지함 몬스터를 통해 받은 편지함 배치 테스트를 예약하는 방법을 알아보려면 [예약된 받은 편지함 배치 테스트를](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e) 참조하세요.
