---
nav_title: Clarisights
article_title: Clarisights
description: "이 참조 문서에서는 셀프 서비스 성과 마케팅 보고 플랫폼인 Clarisights와 Braze 간의 파트너십을 간략하게 설명합니다. 이를 통해 Braze 캠페인과 캔버스에서 데이터를 가져와 성능 및 CRM/유지 마케팅의 통합된 보고 인터페이스를 구축할 수 있습니다."
alias: /partners/Clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights][2]는 데이터 중심 조직을 위한 셀프 서비스 성과 마케팅 보고 플랫폼입니다. 마케팅, 분석 및 기여도 소스의 모든 데이터를 자동으로 통합, 처리 및 시각화합니다.

_이 통합은 Clarisights에서 유지 관리합니다._

## 통합 정보

Braze와 Clarisights의 통합을 통해 Braze 캠페인과 캔버스에서 데이터를 가져와 성능 및 CRM/유지 마케팅의 통합된 보고 인터페이스를 구축할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Clarisights 계정 | 이 파트너십을 활용하려면 Clarisights 워크스페이스가 필요합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키입니다:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
| Braze 워크스페이스 이름 | Braze API 키와 연결된 워크스페이스의 이름입니다. 이 이름은 Clarisights에서 작업 공간 통합을 식별하는 데 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Braze와 Clarisights의 통합을 통해 사용자는 다양한 시각화 및 표를 생성하여 자신이 만든 캠페인에서 인사이트를 얻을 수 있습니다. 인기 있는 사용 사례는 다음과 같습니다:

{% tabs %}
{% tab 가시성 향상 %}
전체 캠페인 및 캔버스 성능에 대한 가시성이 향상됩니다.

![Clarisights 플랫폼에서 더 나은 실행 가능성을 보여주는 그래픽입니다. 이 그래픽에는 캠페인 및 캔버스 열람, 클릭, 전송, 전환 등에 대한 통계가 포함되어 있습니다.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab 세분화된 보고 %}
캠페인 및 캔버스에 대한 세분화된 보고.

!['전체 전송 채널별 전송 수' 및 '전환율'과 같은 세부적인 보고를 보여주는 그래픽입니다.]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab 통합 대시보드 %}
CMO와 CXO를 위한 통합 대시보드.

![통합 대시보드의 예를 보여주는 그래픽입니다.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## 통합

Braze 데이터를 Clarisights에 동기화하려면 Braze 커넥터를 빌드하고 Braze 워크스페이스를 연결해야 합니다.

1. Clarisights에서 **통합** 페이지로 이동하여 **Braze** 커넥터를 찾은 다음, **\+ 연결**을 선택합니다.<br>![Clarisights 통합 마켓플레이스에서 사용 가능한 커넥터 목록입니다.][6]<br><br>
2. 그런 다음, 통합 흐름을 사용하여 Clarisights 계정을 Braze에 연결합니다. Braze REST API 키, Braze 워크스페이스 이름, Braze REST 엔드포인트를 제공하면 됩니다.<br>![Clarisights 플랫폼의 Braze 작업 공간 커넥터. 이 페이지에는 Braze 워크스페이스 이름, Braze REST API 키 및 Braze REST 엔드포인트에 대한 필드가 있습니다.][7]<br><br>통합에 성공하면 사용자는 동일한 페이지에서 연결된 워크스페이스를 볼 수 있습니다.<br>!["Braze 계정"에서 연결된 워크스페이스 목록을 찾을 수 있습니다.][9]<br><br>

## 이 통합 사용

Clarisights 보고서에 Braze를 데이터 소스로 포함하려면 **새 보고서 생성**으로 이동합니다. 보고서의 이름을 지정하고 표시되는 프롬프트에서 **Braze**를 데이터 소스로 선택합니다. 보고서에 포함할 메트릭과 차원을 선택할 수도 있습니다. 완료되면 **보고서 생성**을 선택합니다. 

Braze의 데이터는 다음에 예약된 데이터 가져오기 시점부터 유입이 시작됩니다. Clarisights 고객 성공 매니저에게 연락하여 더 긴 기간의 백필을 요청할 수 있습니다. 

![이름 및 데이터 소스 필드가 표시된 Clarisight 보고 설정. 이 예제에서는 데이터 소스로 'Braze'를 선택했습니다.][8]

사용 가능한 [메트릭 및 차원][10] 또는 [보고서 작성에][11] 대한 자세한 내용은 Clarisights를 방문하세요.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights
