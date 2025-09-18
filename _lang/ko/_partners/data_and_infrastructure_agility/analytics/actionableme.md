---
nav_title: actionable.me
article_title: actionable.me
description: "이 참조 문서에서는 독점 소프트웨어 및 프로세스를 제공하는 actionable.me와 Braze 간의 파트너십을 간략하게 설명합니다. 이를 통해 Braze 투자를 즉각적으로 최대한 활용할 수 있습니다."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> 데이터 및 CRM 에이전시인 Massive Rocket의 팀이 구축한 [actionable.me][2]는 표준화되고 자동화된 CRM 프로그램 실행 방식으로, Braze 고객이 신속하고 일관되며 예측 가능한 방식으로 가치를 창출할 수 있도록 설계된 툴과 프로세스를 제공합니다. 

_This integration is maintained by actionable.me._

## 통합 정보

Braze와 actionable.me 통합을 통해 Braze 활용의 진행 상황을 모니터링할 수 있는 서비스를 배포할 수 있습니다. 여러 툴 및 프로세스의 조합을 통해, CRM 성능을 신속하게 벤치마킹하고 새로운 영업 기회를 식별하며 더 나은 성과를 내기 위한 권장 사항을 제공합니다.

## 전제 조건

| 요구 사항 | 설명 |
| --- | --- |
| actionable.me 계정 | 이 파트너십을 이용하려면 actionable.me 계정이 필요합니다. |
| Braze REST API 키 | 다음 섹션에 나열된 권한이 있는 Braze REST API 키.<br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Braze와 actionable.me를 통합하려면 actionable.me 플랫폼을 구성해야 하며, Braze에서 Braze API 키를 생성하고 actionable.me 대시보드에서 구성해야 합니다.

### 1단계: Braze API 키 생성

Braze에서 **설정** > **API 키로** 이동합니다. **새 API 키 생성을** 선택하고 다음 권한이 추가되었는지 확인합니다:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### 2단계: actionable.me 팀에 정보 제공

통합을 완료하려면 actionable.me 운영 팀에 REST API 키와 [REST 엔드포인트 URL][1]을 제공해야 합니다. 그러면 actionable.me에서 연결을 설정하고 설정이 완료된 후 연락하여 인사이트 공유를 시작할 수 있도록 안내합니다.

![actionable.me 운영팀에서 구성할 actionable.me "플랫폼 추가" 페이지입니다.][5]

## 문제 해결

추가 지원이 필요한 경우 actionable.me 또는 Massive Rocket 팀에 문의하세요: [info@massiverocket.com][3]


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}
