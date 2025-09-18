---
title: Ketch
nav_title: Ketch
description: "이 참고 문서에서는 Braze와 Ketch 통합에 대해 설명합니다. Ketch는 간소화된 개인정보 보호 운영, 완전하고 동적인 데이터 제어, 인텔리전스를 제공합니다."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com)를 통해 비즈니스는 데이터에 대한 책임감 있는 관리자가 될 수 있습니다. Ketch는 간소화된 개인정보 보호 운영, 완전하고 동적인 데이터 제어, 인텔리전스를 제공합니다. 

_This integration is maintained by Ketch._

## 통합 정보

Braze와 Ketch의 통합을 통해 Ketch 환경설정 센터 내에서 고객 커뮤니케이션 환경설정을 제어하고 이러한 변경 사항을 자동으로 Braze에 전파할 수 있습니다. 

{% alert note %}
구독 그룹 생성에 대한 안내를 찾고 계신가요? <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS 구독 그룹</a> 및 <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>이메일 구독 그룹에</a> 대한 도움말을 확인하세요.
{% endalert %}

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Ketch 계정 | 이 통합을 활성화하려면 관리자 권한이 있는 [Ketch](https://www.ketch.com) 계정이 필요합니다. |
| Braze API 키 | `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe`, `email.blacklist` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드**(개발자 콘솔** > **REST API 키** > **새 API 키 생성**)에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Braze 연결 설정

1. [Ketch 인스턴스에서](https://app.ketch.com) **데이터 시스템으로** 이동하여 **Braze를** 선택합니다. 그런 다음, **새 연결**을 클릭합니다.
2. Braze 연결에 식별 가능한 이름을 지정합니다. 그러면 API 기반 프로세스에서 이 연결을 참조하는 데 사용됩니다. 해당 연결에 대한 코드도 생성된다는 점에 유의하세요. 이 코드는 모든 연결에서 고유해야 합니다.
3. 사용자의 ID 매핑을 확인합니다. 기본적으로 Ketch는 사용자의 이메일 주소 또는 Braze의 `external_id`를 기준으로 사용자 ID를 매핑합니다.
4. Braze API 키를 추가하고 API 엔드포인트를 제공합니다. 이 [API 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)는 조직에서 사용 중인 Braze 인스턴스를 기반으로합니다.

### 2단계: 가입 환경설정 구성

1. **정책 센터 > 가입**으로 이동합니다. **정책 센터** 아래 가입 탭이 표시되지 않으면 마케팅 환경설정 센터에 액세스할 수 있는지 확인하고 제품의 이 부분에 액세스할 수 있는 올바른 계정 권한이 있는지 확인합니다.
2. **새 가입 생성**을 클릭하여 새 주제를 생성합니다. 각 구독에는 이름과 코드가 있습니다.
3. 구독 주제를 전송할 채널을 추가합니다. 각 채널은 사용자의 마케팅 환경설정 센터에 표시됩니다. 또한 Ketch 환경설정 센터에서 특정 옵트인 또는 옵트아웃 신호를 조율하는 방법에 대한 세부 정보를 추가할 수도 있습니다.
4. 옵트인 및 옵트아웃 신호를 오케스트레이션하는 데 사용할 Braze 연결을 선택합니다.
5. Ketch 사용자 환경설정을 보낼 구독 그룹에 대한 Braze `subscription_group_id`를 입력합니다.

![Braze 정기구독 그룹 ID.][1]

{% alert note %}
사용자 옵트인 및 옵트아웃 신호를 수집하고 조율하려면 ID를 올바르게 구성해야 합니다. Ketch는 이 통합을 위해 이메일을 식별자로 구성하여 사용자 환경설정 신호를 조율하도록 권장합니다.
{% endalert %}


### 3단계: ID 구성

사용자는 Ketch가 해당 사용자의 마케팅 환경설정 신원을 확인할 수 있는 경우에만 마케팅 환경설정 센터를 볼 수 있습니다. Ketch가 사용자의 신원을 제대로 파악할 수 없는 경우, Ketch가 사용자 환경설정을 관리할 수 없으므로 마케팅 환경설정 페이지가 해당 사용자에게 표시되지 않습니다.

1. 마케팅 환경설정 ID를 구성하려면 Ketch의 **설정** 페이지로 이동하여 **ID 스페이스**를 클릭합니다. 새 아이덴티티 스페이스를 만들거나 기존 아이덴티티 스페이스를 편집하여 해당 아이덴티티 스페이스를 마케팅 기본 설정 아이덴티티로 할당해야 합니다. 속성정보에 배포된 Ketch 태그가 해당 ID 스페이스를 제대로 캡처하는지 확인합니다.
2. **경험 서버** > **속성정보**로 이동하여 원하는 속성정보를 편집합니다. 해당 속성의 데이터 계층 아래에서 사용자 지정 ID 공간을 활성화해야 합니다. 그런 다음 이 사이트에서 마케팅 기본 설정 ID를 캡처하는 방법을 구성합니다.
3. ID 스페이스를 구성한 후에는 Ketch 태그가 배포된 웹사이트에서 환경설정 센터를 열어 환경설정 센터가 표시되는지 테스트합니다.


[1]: {% image_buster /assets/img/ketch/ketch1.png %}
