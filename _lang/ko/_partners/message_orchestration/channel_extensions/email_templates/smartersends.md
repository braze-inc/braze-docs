---
nav_title: SmarterSends
article_title: SmarterSends
description: "이 참고 문서에서는 마케팅 담당자가 아닌 사용자도 브랜드에 맞는 이메일 캠페인을 생성, 예약 및 배포할 수 있도록 설계된 사용하기 쉬운 인터페이스인 Braze와 SmarterSends의 파트너십에 대해 설명합니다."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends는][2] 기업이 생성, 예약 및 배포할 수 있는 마케팅 캠페인을 통해 개인화를 촉진하여 사용된 콘텐츠와 데이터를 제어하고 브랜드 및 법적 규정을 준수할 수 있도록 지원합니다. 

_This integration is maintained by SmarterSends._

## 통합 정보

Braze와 SmarterSends의 파트너십을 통해 분산된 사용자가 소유한 초지역화 콘텐츠에 Braze의 강력한 기능을 결합하여 마케팅 캠페인을 향상시킬 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| SmarterSends 계정 | 이 파트너십을 이용하려면 [SmarterSends 계정이][2] 필요합니다. |
| Braze REST API 키 | 이러한 권한이 있는 Braze REST API 키입니다: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} 이는 Braze 대시보드의 **설정** > **API 키에서** 생성할 수 있습니다. 보안을 강화하려면 SmarterSends IP 주소(인스턴스에서 사용 가능)를 허용 목록에 추가하세요. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
| Braze API 캠페인 ID | [Braze API 캠페인 ID]({{site.baseurl}}/api/api_campaigns/)는 SmarterSends를 통해 전송되는 모든 캠페인의 고유 식별자입니다. 이는 Braze 대시보드의 **메시징** > **캠페인에서** 만들 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Braze와 SmarterSends를 통합하면 여러 채널과 위치에서 마케팅 캠페인을 생성하고 실행하여 분산 마케팅의 이점을 활용할 수 있습니다. 이러한 이점에는 다음이 포함됩니다:

1. **도달 범위 증가:** 여러 채널과 위치를 사용하여 더 많은 오디언스에 도달하고 다양한 위치의 고객을 타겟팅하여 브랜드 노출을 늘릴 수 있습니다.
2. **타겟팅된 메시징:** 채널과 위치에 따라 현지 오디언스의 공감을 불러일으킬 수 있도록 메시지를 맞춤화하여 고객과 더욱 효과적으로 소통하고 참여를 유도합니다. 
3. **브랜드 일관성 향상:** 모든 채널과 위치에서 브랜드 메시지와 이미지를 일관되게 유지하는 것은 강력하고 인지도가 높은 브랜드를 구축하는 데 중요합니다.
4. **더 나은 인사이트:** 다양한 채널과 위치에서 데이터를 수집하여 고객 행동과 선호도에 대한 귀중한 인사이트를 제공하며, 이를 통해 지역 및 글로벌 차원에서 마케팅 전략과 전술을 개선하는 데 사용할 수 있습니다.
5. **효율성 향상:** 다양한 채널과 위치의 강점을 활용하면 원하는 마케팅 목표를 달성하면서 리소스를 보다 효율적으로 사용할 수 있습니다. 

## 통합

### 1단계: REST API 키 만들기

1. Braze에서 **설정** > **API 키로** 이동하여 **새 API 키 만들기를** 클릭합니다.
2. API 키의 이름을 입력합니다.
3. 이 키에 대해 다음 권한을 선택하여 SmarterSends가 Braze 워크스페이스와 상호 작용할 수 있도록 허용합니다.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. SmarterSends IP 주소를 **화이트리스트 IP** 섹션에 추가합니다.
5. **API 키 저장**을 클릭합니다.
6. 적절한 권한이 있는 API 키를 복사하여 SmarterSends의 **Braze 이메일 서비스 제공업체** 설정에 붙여넣습니다.

### 2단계: 애플리케이션 ID 생성 또는 복사

1. Braze 작업 영역에서 **설정** > **앱 설정으로** 이동합니다. 
2. 새 앱을 설정하거나 워크스페이스 내 기존 애플리케이션의 애플리케이션 ID를 사용합니다. 애플리케이션 ID 라벨은 **API 키**로 지정됩니다. 
3. 이 ID를 복사하여 SmarterSends의 **앱 ID** 필드에 붙여넣습니다.

### 3단계: API 캠페인 만들기

API 캠페인을 사용하면 Braze 내 모든 SmarterSends 메일에 대한 측정기준을 추적할 수 있으며, SmarterSends에서 이러한 API 기반 캠페인을 트리거할 수 있습니다.

1. Braze에서 [API 캠페인을 생성합니다]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. **메시지 채널 선택** 아래에서 **이메일을** 클릭하여 메시징 채널을 추가하여 지표 추적을 시작합니다.
3. 그런 다음, Braze의 캠페인 ID를 복사하여 SmarterSends의 **캠페인 ID** 필드에 붙여넣습니다. 
4. Braze의 메시지 변형 ID를 복사하여 SmarterSends의 **메시지 변형 ID** 필드에 붙여넣습니다. SmarterSends에서 각 그룹에 대한 메시지 ID를 만들지 않기로 결정한 경우 사용되는 기본 메시지 ID가 됩니다.
5. SmarterSends에서 생성한 각 그룹에 대해 Braze에서 API 캠페인에 메시지 변형을 추가합니다. 그런 다음, SmarterSends에서 메시지 배리언트 ID를 그룹의 메시지 배리언트 ID로 복사합니다.

{% alert tip %}
SmarterSends에서 생성하는 각 그룹에 대해 메시지 변형 ID를 생성하여 Braze 작업 영역에서 각 그룹의 전송에 대한 지표를 개별적으로 볼 수 있습니다. 이는 Braze에서 보고서를 작성할 때 그룹 전체의 트렌드를 파악하는 데 도움이 될 수 있습니다.
{% endalert %}

## 사용자 지정

각 SmarterSends 인스턴스는 브랜드의 로고 색상과 사용자 지정 도메인 이름으로 완벽하게 사용자 지정할 수 있어 친숙한 환경을 조성할 수 있습니다. 또한, 추가적인 개인화를 위해 Braze 작업 영역 내의 세그먼트를 기반으로 캠페인에서 사용자를 타겟팅할 속성 및 사용자 지정 속성을 정의할 수 있습니다.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://smartersends.com