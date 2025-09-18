---
nav_title: Narvar
article_title: Narvar
description: "Narvar와 Braze를 통합하는 방법을 알아보세요."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar는 주문 추적, 배송 업데이트, 반품 관리를 통해 고객 충성도를 향상시키는 구매 후 플랫폼입니다. Braze와 Narvar의 통합을 통해 브랜드는 Narvar의 알림 이벤트를 활용하여 Braze에서 직접 메시지를 트리거함으로써 고객에게 적시에 업데이트된 정보를 제공할 수 있습니다.

## 필수 조건

| 요구 사항           | 설명                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| 나바르 계정        | 이 파트너십을 이용하려면 Narvar 계정이 필요합니다.                           |
| Braze REST API 키    | `messages.send` 권한이 있는 Braze REST API 키. 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다.                                            |
| Braze REST 엔드포인트   | Braze 인스턴스의 URL에 따라 달라지는 [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 지원되는 기능

|유형|지원되는 기능|
|-------|----------|
| 알림 | \- 배송 예상<br>\- 이동 통신사 지연<br>\- 표준 제공 |
| 채널 | 푸시 알림 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
추가 알림 유형이나 채널에 관심이 있는 경우 Braze 및 Narvar CSM에게 문의하세요.
{% endalert %}

## 통합 세부 정보

For each notification event, Narvar initiates a request to the Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) endpoint to deliver a push message to each opted-in consumer.

Narvar는 각 메시지에 대한 푸시 알림 페이로드를 구성할 책임이 있습니다. 현재 Narvar에는 푸시 알림을 위한 디자인 인터페이스가 내장되어 있지 않으므로 팀과 협력하여 페이로드 요구 사항을 결정하고 정의합니다. 이러한 페이로드는 주문 데이터 및 소비자 세부 정보와 같은 가변 콘텐츠 자리 표시자를 지원하는 등 자체 시스템을 통해 전송되는 것과 동일한 수준으로 사용자 지정할 수 있습니다.

## Braze-나르바 통합 시작하기

1. **Narvar CSM에게 연락하여** 통합에 대한 관심을 표현하세요.
2. 스테이징 및 프로덕션을 위한 **Braze 환경을 지정합니다**.
3. Narvar에서 사용할 수 있도록 Braze에서 **API 키를 생성합니다**.
4. 필요에 따라 Braze에서 **캠페인 키를 생성합니다**.
5. 안전한 일회성 링크를 통해 Narvar에 **API 및 캠페인 키를 제공합니다**.
6. **푸시 알림 페이로드 세부 정보를 공유하여** 설정을 마무리합니다.
