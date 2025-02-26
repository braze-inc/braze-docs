---
nav_title: Criteo
article_title: Criteo에 캔버스 오디언스 동기화
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Criteo에 Braze 오디언스 동기화를 사용하는 방법을 다룹니다."
page_order: 1
alias: "/audience_sync_criteo/"

Tool:
  - Canvas
---

# Criteo에 오디언스 동기화

Criteo에 Braze 오디언스 동기화를 사용하여 브랜드는 자체 Braze 통합의 사용자 데이터를 Criteo 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 Criteo 고객 목록에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다:**

- 구매 또는 인게이지먼트를 유도하도록 여러 채널을 통해 고가치 사용자 타겟팅
- 다른 마케팅 채널에 반응이 저조한 사용자 리타겟팅
- 이미 브랜드에 충성도가 높은 소비자인 사용자가 광고를 받지 못하도록 억제 타겟을 생성하기
- 새로운 사용자를 더 효율적으로 확보하기 위해 유사 오디언스 생성

이 기능을 통해 브랜드는 어떤 특정 퍼스트파티 데이터가 Criteo와 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

{% alert important %}
**Audience Sync Pro 면책 조항**<br>
Criteo에 Braze 오디언스 동기화는 Audience Sync Pro 통합 기능입니다. 이 통합에 대한 자세한 내용은 Braze 계정 관리자에게 문의하세요. <br> 
{% endalert %}

## 필수 조건 

Criteo에 오디언스 동기화를 설정하기 전에 다음 항목이 생성 및/또는 완료되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| Criteo 광고 계정 | [Criteo](https://marketing.criteo.com/) | 브랜드에 연결된 활성 Criteo 광고 계정.<br><br>Criteo 관리자가 오디언스에 액세스할 수 있는 적절한 권한을 부여했는지 확인합니다. |
| [Criteo 광고 지침](https://www.criteo.com/advertising-guidelines/)<br>그리고<br>[Criteo 브랜드 안전 지침](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | 활성 Criteo 고객이라면, Criteo 캠페인을 시작하기 전에 Criteo의 광고 및 브랜드 안전 지침을 준수할 수 있는지 확인해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합 

### 1단계: Criteo에 연결

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하고 **Criteo**를 선택합니다. 크리테오 오디언스 내보내기에서 **크리테오 연결을** 선택합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **통합**에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

![Braze의 크리테오 기술 페이지에는 개요 섹션과 연결된 크리테오 버튼이 있는 크리테오 섹션이 포함되어 있습니다.][5]{: style="max-width:80%;"}

오디언스 동기화 통합과 관련된 권한에 대해 Braze에 권한을 부여하는 Criteo oAuth 페이지가 나타납니다.

확인을 선택하면 Braze로 리디렉션되어 동기화할 Criteo 광고 계정을 선택할 수 있습니다. 

![Criteo에 연결할 수 있는 사용 가능한 광고 계정 목록.][7]{: style="max-width:80%;"}

연결에 성공하면 파트너 페이지로 돌아가서 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![광고 계정이 성공적으로 연결되었음을 보여주는 Criteo 기술 파트너 페이지의 업데이트된 버전.][4]{: style="max-width:80%;"}

Criteo 연결은 Braze 워크스페이스 수준에서 적용됩니다. Criteo 관리자가 회원님을 Criteo 광고 계정에서 삭제하는 경우, Braze는 유효하지 않은 토큰을 감지합니다. 결과적으로 Criteo를 사용하는 활성 캔버스에 오류가 표시되고 Braze는 사용자를 동기화할 수 없습니다.

### 2단계: 캔버스 진입 기준 구성

광고 추적을 위한 오디언스를 구축할 때 선호도에 따라 그리고 [CCPA](https://oag.ca.gov/privacy/ccpa)의 '판매 또는 공유 금지' 권한과 같은 개인정보 보호법을 준수하기 위해 특정 사용자를 포함하거나 제외할 수 있습니다. 마케터는 캔버스 진입 기준 내에서 사용자의 자격에 맞는 관련 필터를 구현해야 합니다. 아래에는 몇 가지 옵션이 나와 있습니다.

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)를 수집한 경우, 광고 추적 활성화됨 필터를 사용할 수 있습니다. 값을 true로 선택하면 사용자가 옵트인한 오디언스 동기화 대상으로만 사용자를 보낼 수 있습니다.

![][11]

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우 캔버스 진입 기준에 필터로 포함해야 합니다.

![][12]

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance/)을 참조하세요.

### 3단계: Criteo에서 오디언스 동기화 단계 추가

캔버스에 컴포넌트를 추가하고 **대상 동기화를** 선택합니다.

![캔버스 흐름에서 Criteo 오디언스 구성요소를 추가하는 이전 단계의 워크플로.][9]{: style="max-width:35%;"} ![캔버스 흐름에서 Criteo 오디언스 구성요소를 추가하는 이전 단계의 워크플로.][10]{: style="max-width:28%;"}

### 4단계: 동기화 설정

**사용자 지정 대상** 버튼을 클릭하여 컴포넌트 에디터를 엽니다.

원하는 오디언스 동기화 파트너로 **Criteo**를 선택합니다. 

![][6]

그런 다음, 원하는 Criteo 광고 계정을 선택합니다. **새 대상 또는 기존 대상 선택** 드롭다운에서 새 대상 또는 기존 대상의 이름을 입력합니다.

{% tabs %}
{% tab 새로운 오디언스 만들기 %}
**새로운 오디언스 만들기**<br>
새 오디언스의 이름을 입력하고 **오디언스에 사용자 추가**를 선택한 다음, Criteo와 동기화할 필드를 선택합니다. 그런 다음, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정을 선택하고 새 오디언스를 생성합니다.]({% image_buster /assets/img/criteo/criteo3.png %})

대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 또한 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다.

![캔버스 구성요소에서 새 오디언스을 생성한 후에 표시되는 알림.]({% image_buster /assets/img/criteo/criteo1.png %})

새로운 오디언스와 함께 캔버스를 시작하면, Braze는 오디언스 동기화 구성요소에 들어가면 거의 실시간으로 사용자를 동기화합니다.
{% endtab %}
{% tab 기존 오디언스와 동기화 %}
**기존 오디언스와 동기화**<br>
또한 Braze는 기존 Criteo 오디언스에 사용자를 추가하여 해당 오디언스가 최신 상태인지 확인할 수 있는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력하고 **오디언스에 추가합니다**. 그러면 Braze는 오디언스 동기화 구성요소에 사용자가 들어오는 대로 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### 5단계: 캔버스 실행

오디언스 동기화를 Criteo에 구성한 후에는 캔버스를 실행하기만 하면 됩니다! 새 오디언스가 생성되고 오디언스 동기화 단계를 통해 유입되는 사용자는 Criteo에서 이 오디언스로 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

광고 매니저 계정으로 이동하고 탐색의 **오디언스 라이브러리**에서 세그먼트를 선택하면 Criteo에서 오디언스를 확인할 수 있습니다. **세그먼트** 페이지에서 최대 1,000명에 도달한 후 각 오디언스의 크기를 확인할 수 있습니다.

![세그먼트, ID, 소스, 유형, 크기, 현재 사용량, 마지막 업데이트가 표시된 오디언스 라이브러리.][0]

## 사용자 동기화 및 속도 제한 고려 사항

사용자가 오디언스 동기화 단계에 도달하면, Braze는 Criteo의 API 사용량 제한을 준수하면서 거의 실시간으로 이러한 사용자를 동기화합니다. 즉, 실제로 Braze는 이러한 사용자를 Snapchat으로 보내기 전에 5초마다 최대한 많은 사용자를 배치 처리하려고 시도합니다.

Criteo의 API 사용량 제한은 분당 250건 이하로 명시되어 있습니다. Braze 고객이 이 사용량 제한에 도달하면 Braze 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다. 

## 분석 이해

다음 표에는 오디언스 동기화 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| 진입함 | 이 구성요소에 들어간 사용자 중 Criteo에 동기화할 사용자 수. |
| 다음 단계로 진행됨 | 다음 구성 요소로 진급한 사용자 수(있는 경우). 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 사용자가 동기화됨 | Criteo에 성공적으로 동기화된 사용자 수. |
| 사용자가 동기화되지 않음 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 사용자가 보류 중임 | 현재 Braze에서 Criteo로의 동기화를 처리 중인 사용자 수. |
| 사용자에서 오류 발생 | 약 13시간 동안의 재시도 후 API 오류로 인해 Criteo에 동기화되지 않은 사용자 수. 오류의 잠재적 원인으로는 잘못된 Criteo 토큰 또는 Criteo에서 오디언스가 삭제된 경우 등이 있습니다. |
| 캔버스에서 나감 | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 오디언스 동기화 구성요소일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
각각 일괄 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류가 발생한 사용자 측정기준에 대한 보고가 지연될 수 있습니다.
{% endalert %}

## 문제 해결

{% details 유효하지 않은 토큰 오류가 발생하면 어떻게 해야 하나요? %}
Criteo 파트너 페이지에서 Criteo 계정 연결을 끊었다가 다시 연결하면 됩니다. 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 Criteo 관리자에게 확인합니다.
{% enddetails %}

{% details 왜 내 캔버스가 시작되지 않나요? %}
Criteo 파트너 페이지에서 Criteo 광고 계정이 Braze에 성공적으로 연결되었는지 확인합니다.

광고 계정을 선택하고, 새 오디언스의 이름을 입력하며, 일치시킬 필드를 선택했는지 확인합니다.
{% enddetails %}

{% details Criteo에 사용자를 전달한 후 사용자가 일치하는지 어떻게 알 수 있나요? %}
Criteo는 데이터 프라이버시 정책과 관련해 이 정보를 제공하지 않습니다.
{% enddetails %}

{% details Criteo는 몇 명의 오디언스를 지원할 수 있나요? %}
현재 Criteo 계정에서는 1,000명의 오디언스만 보유할 수 있습니다. 

이 제한을 위반하는 경우, Braze는 새로운 오디언스를 생성할 수 없음을 알립니다. 

Criteo 광고 계정으로 이동하여 더 이상 사용하지 않는 오디언스를 제거해야 합니다.
{% enddetails %} 

[0]: {% image_buster /assets/img/criteo/criteo.png %}
[1]: {% image_buster /assets/img/criteo/criteo1.png %}
[2]: {% image_buster /assets/img/criteo/criteo2.png %}
[3]: {% image_buster /assets/img/criteo/criteo3.png %}
[4]: {% image_buster /assets/img/criteo/criteo4.png %}
[5]: {% image_buster /assets/img/criteo/criteo5.png %}
[6]: {% image_buster /assets/img/criteo/criteo6.png %}
[7]: {% image_buster /assets/img/criteo/criteo7.png %}
[8]: {% image_buster /assets/img/criteo/criteo8.png %}
[9]: {% image_buster /assets/img/criteo/criteo9.png %}
[10]: {% image_buster /assets/img/criteo/criteo10.png %}
[11]: {% image_buster /assets/img/criteo/criteo11.png %}
[12]: {% image_buster /assets/img/criteo/criteo12.png %}
