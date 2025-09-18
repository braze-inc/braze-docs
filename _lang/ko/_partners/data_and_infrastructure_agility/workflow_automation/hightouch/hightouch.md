---
nav_title: Hightouch
article_title: Hightouch
description: "이 참조 문서에서는 고객 데이터를 웨어하우스에서 비즈니스 툴로 동기화하는 플랫폼인 Hightouch와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch][1]는 IT 또는 엔지니어링 팀의 도움 없이도 웨어하우스 또는 데이터 레이크의 고객, 제품 또는 독점 데이터를 원하는 앱에 동기화할 수 있는 최신 데이터 통합 플랫폼입니다.

Braze와 Hightouch의 통합을 통해 데이터 웨어하우스의 최신 고객 데이터로 Braze에서 더 나은 캠페인을 구축할 수 있습니다. 고객 데이터를 Braze에 자동으로 동기화하면 더 이상 데이터 일관성에 대해 걱정할 필요가 없으며, 세계적 수준의 고객 경험을 구축하는 데 집중할 수 있습니다. 

또한 이 통합을 통해 [사용자 코호트를 Braze로 가져와서]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/hightouch/) 웨어하우스에만 존재할 수 있는 데이터를 기반으로 타겟팅 캠페인을 전송할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Hightouch 계정정 | 이 파트너십을 활용하려면 Hightouch 계정이 필요합니다.
| Braze REST API 키 | `users.track` 및 `users.export.ids` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | REST 엔드포인트 URL. 귀하의 엔드포인트는 귀하의 인스턴스에 대한 [Braze URL][2]에 따라 달라집니다.<br><br>하이터치에는 Braze 인스턴스가 위치한 클러스터의 이름이 필요합니다. 예를 들어, Braze 엔드포인트가 `https://rest.iad-01.braze.com`인 경우 `iad-01`만 있으면 됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

* 사용자 및 계정에 대한 데이터를 Braze에 동기화하여 초개인화된 캠페인을 구축하세요.
* 웨어하우스의 새로운 데이터로 Braze 세그먼트를 자동으로 업데이트합니다.
* 다른 고객 접점의 데이터를 Braze로 가져와 더 나은 경험을 제공하세요.
* 사용자 코호트를 Braze로 가져와서 타겟팅된 캠페인과 캔버스를 전송할 수 있습니다. 

## 통합

### 1단계: Hightouch Braze 대상 생성

1. Hightouch 플랫폼의 **대상** 섹션에서 **대상 추가**를 클릭합니다.
2. 사용 가능한 대상 목록에서 **Braze**를 선택합니다.
3. Braze REST 엔드포인트('https://rest.' 제외)와 Braze REST API 키를 제공합니다.<br><br>![][3]

### 2단계: 개체 및 이벤트 동기화

하이터치는 사용자 개체와 이벤트 모두에 대한 동기화를 지원합니다.

| 대상 | 설명 | 지원 모드 |
|---|---|---|
| 객체 | 대상의 사용자 또는 조직과 같은 오브젝트에 레코드를 동기화합니다.| 변경 또는 업데이트 |
| 이벤트 | 레코드를 이벤트로 대상에 동기화합니다. 종종 추적 호출의 형태로 수행됩니다. | 이벤트 추적 또는 구매 추적 |

{% alert note %}
동기화가 Braze 데이터 포인트 소비에 미치는 영향에 대한 자세한 내용은 [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption)를 참조하세요.
{% endalert %}

#### Braze 개체 동기화

Hightouch 오브젝트(사용자 필드)를 동등한 Braze 기본 필드 또는 커스텀 필드에 동기화할 수 있습니다. 또한 레코드 일치를 수행하여 두 플랫폼에서 데이터를 통합하는 데 도움을 줄 수 있습니다.

#### Braze 이벤트 동기화

하이터치를 사용하면 이벤트 및 구매 데이터를 추적하고 이를 Braze에 동기화할 수 있습니다. 추적 데이터 설정, 존재하지 않는 사용자 행동 정의 등 동기화 동작에 영향을 주는 여러 옵션을 Hightouch에서 설정할 수 있습니다.

{% alert important %}
오브젝트 및 이벤트 동기화에 대한 자세한 지침은 [Hightouch 설명서](https://hightouch.io/docs/destinations/braze/)에서 확인할 수 있습니다.
{% endalert %}



## 통합 데모

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]:https://hightouch.io/docs/destinations/braze/

