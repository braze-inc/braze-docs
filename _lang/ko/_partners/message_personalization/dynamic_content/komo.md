---
nav_title: Komo
article_title: Komo
description: "이 참고 문서에서는 게임화, 인터랙티브 콘텐츠, 대회, 상금, 로열티를 전문으로 하는 고객 참여 플랫폼인 Braze와 Komo의 파트너십에 대해 설명합니다. 이 통합을 통해 Komo에서 캡처한 퍼스트파티 및 제로파티 데이터를 Braze에 게시할 수 있습니다."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo][7]는 게임화, 대화형 콘텐츠, 대회, 상금, 로열티에 특화된 고객 인게이지먼트 플랫폼입니다.

_This integration is maintained by Komo._

## 통합 정보

Braze와 Komo의 통합으로 Komo 인게이지먼트 허브를 통해 퍼스트파티 및 제로파티 데이터를 수집할 수 있습니다. 이러한 허브는 대화형 콘텐츠와 게임화 기능을 제공하는 동적 마이크로사이트입니다. 이러한 허브에서 수집된 사용자 데이터는 Braze API로 전송됩니다.

- Komo에서 Braze로 수집한 퍼스트파티 및 제로파티 사용자 데이터를 실시간으로 수집합니다
- 설문조사, 투표, 퀴즈 질문에 답할 때 시장 조사 및 사용자 선호도 데이터를 수집합니다
- 사용자가 계속해서 참여하고 자신에 대한 더 많은 데이터를 공유함에 따라 시간이 지남에 따라 Braze에서 점진적으로 고객 프로필을 빌드합니다.
- Braze를 통해 전송되는 트랜잭션 이메일의 모양과 느낌을 표준화하세요

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Komo 계정 | 이 파트너십을 이용하려면 활성 Komo 계정이 필요합니다. 지금 평가판을 시작하려면 [Komo][7]를 방문하세요. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다.<br><br>예를 들어 다음과 같이 표시되어야 합니다: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용 사례

{% tabs local %}
{% tab 데이터 캡처 - 양식 제출 %}

사용자가 Komo에서 사용자 지정 가능한 데이터 캡처 양식을 제출하면, Braze 통합에 매핑된 Komo 필드가 `/users/track/` API 호출을 통해 Braze로 전달됩니다.

데이터 캡처 양식은 카드의 시작 또는 끝에 존재합니다.

{% endtab %}
{% tab 시장 조사 - 곧 출시 예정 %}

곧 Komo는 사용자가 퀴즈 질문, 설문조사, 성격 테스트, 스와이퍼 등에 응답할 때 캡처된 시장 조사 데이터를 전달하는 기능을 추가할 예정입니다. 이 데이터를 통해 양식 제출에서 캡처된 데이터 외에도 고객 프로필을 개선할 수 있습니다.

{% endtab %}
{% endtabs %}

## 통합

### 1단계: Komo 인게이지먼트 허브 및 카드 게시

데이터 캡처 양식이 포함된 카드가 하나 이상 포함된 Komo 인게이지먼트 허브를 게시해야 합니다. 게시되면 사용자 환경을 엔드 투 엔드 테스트하고 통합이 올바르게 작동하는지 확인할 수 있습니다.

![][2]

### 2단계: Braze 통합 추가

코모에서 **허브 설정** 탭으로 이동하여 **연동** 섹션을 선택합니다. 그런 다음 목록에서 Braze 연동 서비스를 찾아 **연결** 버튼을 선택하여 연동을 활성화합니다.

![][3]

![][4]

#### 사용자 매핑 구성

가장 먼저 Komo에서 캡처된 사용자를 Braze 내 사용자에 매핑하는 방법부터 구성해야 합니다. Komo 내 필드에서 `braze_id` 또는 `external_id`를 캡처하는 경우 적절한 키를 선택할 수 있습니다. 그렇지 않은 경우 가장 일반적인 옵션인 이메일 또는 전화의 사용자 별칭을 선택합니다.

![][5]{: style="max-width:65%;"}

다음으로, Braze 속성으로 전송할 Komo 필드의 맵을 정의해야 합니다. Komo는 대량의 데이터를 캡처하므로 Braze 통합에 매핑된 필드만 Braze로 전송됩니다.

![][6]{: style="max-width:65%;"}

마지막으로, API 키와 REST 엔드포인트 URL을 추가하고 **저장**을 클릭하여 통합을 활성화합니다.

## 통합 사용

통합이 완료되면 Braze로 전송된 Komo 데이터를 사용하여 타겟팅을 위한 세그먼트를 생성할 수 있습니다.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
[7]:https://komo.tech/