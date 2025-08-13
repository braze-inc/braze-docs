---
nav_title: Nexla
article_title: Nexla
description: "이 참조 문서에서는 Braze 커런츠 사용자가 데이터 레이크 데이터를 커스텀 형식으로 추출 및 변환하고 다른 위치로 로드할 수 있는 통합 데이터 운영 플랫폼인 Nexla와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com)는 통합 데이터 운영 분야의 리더이자 2021년 Gartner의 쿨 벤더로 선정된 기업입니다. Nexla 플랫폼을 사용하면 누구나 손쉽게 확장 가능한 데이터 흐름을 생성하여 비즈니스 및 데이터 팀에 마찰이 없고 통제된 데이터 운영, 더 나은 협업, 민첩성을 제공할 수 있습니다. 데이터로 작업하는 팀은 노코드/로우코드 통합 환경을 통해 모든 사용 사례에 맞게 데이터를 통합, 변환, 프로비저닝 및 모니터링할 수 있습니다. 

Braze와 Nexla의 통합을 통해 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)를 사용하는 고객은 Nexla를 활용하여 해당 데이터를 추출 및 변환하고 커스텀 형식으로 다른 위치로 로드할 수 있으므로 전체 에코시스템에서 데이터에 쉽게 액세스할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Nexla 계정 | 이 파트너십을 활용하려면 [Nexla 계정][2]이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | 귀하의 REST 엔드포인트 URL. 사용자의 엔드포인트는 [인스턴스를 위한 Braze URL][1]에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Nexla의 제품형 데이터인 [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)를 사용하면 메타데이터에 대한 걱정 없이 모든 형식의 데이터를 쉽게 작업할 수 있습니다. Nexla를 사용하여 Braze와의 데이터 흐름을 설정할 때 노코드 툴로 몇 분 안에 쉽게 작업할 수 있습니다. 데이터 흐름이 대상으로 설정되면 Nexla는 사용자의 흐름을 모니터링하고 데이터의 양에 따라 규모를 조정합니다.

## 통합

### 1단계: Nexla 계정 생성

아직 Nexla 계정이 없는 경우, Nexla [웹사이트](https://www.nexla.com)에서 무료 데모 및 평가판을 요청합니다 다음으로, [www.dataops.nexla.io](https://www.dataops.nexla.io)에 로그온하고 새 자격 증명으로 로그인합니다.

### 2단계: 소스 추가

#### Braze가 데이터 소스인 경우
1. Nexla 플랫폼의 왼쪽 툴바에서 **흐름> 새 흐름 생성**으로 이동합니다.
2. **새 소스 생성**을 클릭하고 Braze 커넥터를 선택한 후, **다음**을 클릭합니다. 
3. **새 자격 증명 추가**를 선택하고, 자격 증명 이름을 지정하며, Braze API 키와 REST 엔드포인트를 추가한 다음, **저장**합니다.
4. 마지막으로 데이터를 선택하고 **저장을** 클릭합니다. 

이제 Nexla가 찾은 데이터에 대한 소스를 검색하고 대상으로 전송하거나 변환을 위해 [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)를 생성합니다.

#### Braze가 대상인 경우

[Nexla에 소스를 연결](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source)하는 방법은 Nexla 설명서를 참조하세요.

### 3단계: 변환(선택 사항)

데이터에 사용자 정의 [변환을](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) 수행하거나 Nexla의 사전 구축 커넥터를 사용하려면 데이터 세트에서 **변환** 버튼을 클릭하여 변환 빌더로 들어갑니다. Transform Builder 사용에 대한 지침은 [Nexla 설명서](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)에서 확인할 수 있습니다.

### 4단계: 목적지로 보내기

대상으로 데이터를 보내려면 데이터 세트에서 **대상으로 전송** 화살표를 클릭하고 Nexla의 대상 커넥터 중 하나를 선택하거나 다른 소스가 있는 경우 Braze를 선택합니다. 자격 증명을 입력하고 대상 옵션을 구성한 다음, **저장**을 클릭합니다. 데이터는 지정한 형식으로 선택한 대상에 즉시 전송되기 시작합니다.

## 이 통합 사용

흐름이 설정되면 더 이상 아무것도 필요하지 않습니다. Nexla는 소스 데이터의 변경 사항을 처리하고, 새로운 데이터로 확장하며, 분류에 대한 스키마 변경이나 오류를 알려줍니다. 변환, 소스 또는 대상을 변경하려는 경우 이러한 옵션을 클릭하고 변경하면 Nexla가 즉시 흐름을 업데이트합니다.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]:https://www.nexla.com/get-demo