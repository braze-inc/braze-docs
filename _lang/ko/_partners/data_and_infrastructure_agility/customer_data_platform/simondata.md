---
nav_title: Simon Data
article_title: Simon Data
description: "Braze와 Simon Data 통합을 사용하면 코드 없이 실시간으로 오케스트레이션을 위해 정교한 오디언스를 생성하고 Braze에 동기화합니다."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon Data

> [Simon Data][1]는 마케터에게 친숙하고 데이터 팀이 신뢰하는 고객 데이터 플랫폼(CDP)입니다. Simon은 데이터 웨어하우스를 마케팅 파워하우스로 변환하여 비즈니스 성과와 탁월한 고객 경험을 이끌어냅니다.

Braze와 Simon Data 통합을 사용하면 코드 없이 실시간으로 오케스트레이션을 위해 정교한 오디언스를 생성하고 Braze에 동기화합니다. 이 통합을 통해 Simon의 캠페인 우선순위 지정 및 아이덴티티 매칭 기능, 복잡한 통합 지원 등의 장점을 활용하여 Braze 캠페인을 다운스트림으로 향상시킬 수 있습니다.

## 전제 조건

시작하려면 Simon Data 계정에서 Braze 계정을 인증해야 합니다.

| 요구 사항         | 설명                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | Simon Data 내에서 Braze 통합 기능을 활용하려면 기존 Simon Data 계정이 있어야 합니다.                                                                    |
| Braze REST API 키  | `users.track`, `campaigns.trigger.schedule.create`, `campaigns.trigger.send` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 대시보드 URL | [REST 엔드포인트 URL][3]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

- Braze 캔버스 또는 이메일 트리거  
- 세그먼트 속성 전달 및 유지 관리
- 동기화 특성 및 연락처 속성

{% alert note %}  
Simon과 Braze 통합을 사용할 때, Simon은 동기화할 때마다 델타만 Braze로 전송하여 관련 없는 데이터에 대한 비용이 발생하지 않도록 합니다. 자세한 내용은 [동기화 특성 및 연락처 속성정보](#sync-traits-and-contact-properties)를 참조하세요.
{% endalert %}

## 통합

### Simon에서 Braze 계정 인증하기

Braze 연동 기능을 사용하려면 먼저 Simon에서 Braze 계정을 인증하세요:

1. 왼쪽 탐색에서 **통합**을 클릭한 다음, Braze로 스크롤합니다.
2. Braze [REST API 키와][2] [대시보드 URL을][3] 입력합니다.
3. **변경 내용 저장**을 클릭합니다.

연결에 성공하면 창에 **연결됨이** 표시됩니다.

![Simon Data의 통합 화면][8]{: style="max-width:70%"}

### Simon의 흐름 또는 여정에 Braze 작업 추가

Simon에서 Braze 계정을 인증한 후에는 [흐름][4] 및 [여정][5]에 Braze 작업을 추가할 수 있습니다.

세 가지 작업을 사용할 수 있습니다.

- **Simon 세그먼트 속성 동기화**: 세그먼트 세부 정보를 Braze의 신규 또는 기존 사용자 지정 속성과 동기화하세요.
- **Braze 캔버스 트리거**: Simon 세그먼트 데이터를 활용하는 Braze 캔버스를 트리거합니다.
- **Braze 캠페인 전송**: Simon에서 전체 Braze 캠페인을 시작합니다.

![Simon 데이터에서 사용 가능한 Braze 작업 목록을 보여주는 드롭다운.][9]{: style="max-width:60%"}

일부 작업은 특정 흐름 유형 또는 여정에서만 사용할 수 있습니다. [docs.simondata.com][6]에서 자세히 알아보세요.

### 특성 및 연락처 속성 동기화

데이터 소비를 최소화하려면 세그먼트의 모든 고객에 대해 모든 필드를 업데이트하는 대신, 기본적으로 동기화할 특정 특성을 선택할 수 있습니다.

{% alert note %}
특성 동기화를 시작하려면 [Simon 지원 센터에서](https://docs.simondata.com/docs/support-center) 요청을 제출하세요. 계정 관리자가 다음 단계를 진행할 수 있는 시기를 알려드릴 것입니다.
{% endalert %}

계정 매니저가 연락처 특성을 활성화한 후:

1. Simon의 왼쪽 탐색에서 **관리 센터**를 확장하고 **연락처 특성 동기화**를 선택합니다.
2. **Braze**를 선택합니다. 연락처 속성이 데이터 세트별로 중첩되어 여기에 표시됩니다.
3. Simon과 Braze 통합을 사용할 때 동기화할 필드를 선택합니다:
   1. **개수 또는 특성**은 해당 데이터 세트에서 선택할 수 있는 특성 수를 나타냅니다. 모두 선택하거나 행을 확장하여 개별 필드를 선택할 수 있습니다.
   2. 필드 이름이 Braze에 도착했을 때 다르게 표시되도록 하려면 **다운스트림 이름**을 편집합니다.
   3. Simon에서 Braze와 처음 통합하는 경우 **모든 연락처 백필**을 클릭합니다. 백필링은 흐름이나 여정에서 처음 작업을 사용할 때 모든 데이터 포인트를 Braze로 전송하여 모든 데이터가 완전히 동기화되었는지 확인합니다. 이후 동기화할 때 이 화면에서 선택한 특성만 Braze로 전송됩니다. 이렇게 하면 필요한 데이터에 대해서만 요금이 청구되도록 보장할 수 있습니다.

![Simon 데이터에서 동기화 특성 선택.][10]




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center

[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}  
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}
