---
nav_title: LinkedIn
article_title: 캔버스 오디언스와 LinkedIn 동기화
alias: /linkedin_audience_sync/
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Braze 오디언스 동기화를 LinkedIn에 사용하는 방법에 대해 설명합니다."
Tool:
  - Canvas
page_order: 4

---

# LinkedIn에 오디언스 동기화

브랜드는 LinkedIn 오디언스 동기화 기능을 사용하여 Braze 통합의 사용자 데이터를 LinkedIn 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 사용하는 모든 기준이 이제 LinkedIn 고객 목록에 있는 해당 사용자에게 광고를 트리거할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다**:

- 여러 채널을 통해 고가치 사용자를 타겟팅하여 구매 또는 참여 유도하기
- 다른 마케팅 채널에 반응이 저조한 사용자 리타겟팅하기
- 이미 브랜드에 충성도가 높은 소비자인 사용자가 광고를 받지 못하도록 억제 타겟을 생성하기

이 기능을 통해 브랜드는 어떤 특정 퍼스트파티 데이터가 LinkedIn과 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

{% alert important %}
오디언스 동기화는 현재 베타 버전으로 제공되고 있습니다. 베타에 참여하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 필수 조건

Canvas에서 LinkedIn 오디언스 동기화 단계를 설정하기 전에 다음 항목이 생성, 완료 또는 수락되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| LinkedIn 광고 계정 | [LinkedIn](https://www.linkedin.com/campaignmanager) | 브랜드와 연결된 활성 LinkedIn 광고 계정입니다.<br><br>해당 계정에 액세스하고 사용하기 위해 관련 LinkedIn 이용약관을 수락했는지, LinkedIn 관리자가 오디언스를 관리할 수 있는 적절한 권한을 부여했는지 확인하세요. |
| LinkedIn 이용 약관 및 정책 | LinkedIn | LinkedIn 오디언스 동기화 사용과 관련된 LinkedIn의 필수 약관, 정책, 가이드라인 및 설명서를 준수하는 데 동의하며, 여기에 참조로 포함된 모든 약관, 정책, 가이드라인 및 설명서에는 LinkedIn의 약관, 정책, 가이드라인 및 문서가 포함될 수 있습니다: 서비스 약관, 광고 계약, 데이터 처리 계약 및 전문 커뮤니티 가이드라인. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: LinkedIn에 연결

Braze 대시보드에서 **기술 파트너**로 이동하여 **LinkedIn**을 선택합니다. **LinkedIn 대상 동기화** 섹션에서 **LinkedIn 연결을** 선택합니다.

![Braze의 LinkedIn 기술 페이지에는 개요 섹션과 연결된 LinkedIn 버튼이 있는 LinkedIn 오디언스 동기화 섹션이 있습니다.][3]{: style="max-width:75%;"}

그러면 오디언스 동기화 연동과 관련된 권한에 대해 Braze에 권한을 부여하기 위해 LinkedIn OAuth 페이지로 리디렉션됩니다. **확인**을 선택하면 다시 Braze로 리디렉션되어 동기화할 LinkedIn 광고 계정을 선택할 수 있습니다. 

!["연결할 광고 계정으로 'Braze 셀프 서비스'가 선택되어 있습니다.][7]{: style="max-width:75%;"}

연결에 성공하면 파트너 페이지로 돌아가서 어떤 계정이 연결되어 있는지 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![LinkedIn 계정에 성공적으로 연결되었습니다.][6]{: style="max-width:75%;"}

LinkedIn 연결은 Braze 워크스페이스 수준에서 적용됩니다. LinkedIn 관리자가 회원님을 LinkedIn 광고 계정에서 삭제하는 경우, Braze는 유효하지 않은 토큰을 감지합니다. 결과적으로 LinkedIn을 사용하는 활성 캔버스에 오류가 표시되고 Braze에서 사용자를 동기화할 수 없게 됩니다.

### 2단계: 캔버스 항목 기준 구성

광고 추적을 위한 오디언스를 구축할 때 선호도에 따라 특정 사용자를 포함하거나 제외할 수 있으며, [CCPA에](https://oag.ca.gov/privacy/ccpa) 따른 '판매 또는 공유 금지' 권한과 같은 개인정보 보호법을 준수할 수 있습니다. 마케터는 캔버스 진입 기준 내에서 사용자의 자격에 맞는 관련 필터를 구현해야 합니다. 아래에는 몇 가지 옵션이 나와 있습니다. 

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)를 수집한 경우, **광고 추적 사용** 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 사용자가 옵트인한 오디언스 동기화 대상으로만 사용자를 보낼 수 있습니다. 

!['광고 추적 사용' 필터가 적용된 응모 대상은 참입니다.][5]{: style="max-width:75%;"}

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우 캔버스 진입 기준에 필터로 포함해야 합니다.

![항목 대상 그룹이 "opted_in_marketing"인 캔버스는 "true"와 같습니다.][4]{: style="max-width:75%;"}

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance/)을 참조하세요.

### 3단계: LinkedIn에 오디언스 동기화 단계 추가

캔버스에 컴포넌트를 추가하고 오디언스 동기화를 선택합니다. **사용자 지정 대상** 버튼을 클릭하여 컴포넌트 에디터를 엽니다.

![사용 가능한 구성 요소 목록이 있는 캔버스 편집기입니다.][2]{: style="max-width:35%;"} ![선택한 오디언스 동기화 구성 요소입니다.][1]{: style="max-width:29%;"}

### 4단계: 동기화 설정

원하는 오디언스 동기화 파트너로 **LinkedIn**을 선택합니다.

!['오디언스 동기화 설정' 세부 정보에서 여러 파트너를 선택할 수 있습니다.][9]{: style="max-width:70%;"}

그런 다음 원하는 LinkedIn 광고 계정을 선택합니다. **새 대상 또는 기존 대상 선택** 드롭다운에서 새 대상 또는 기존 대상의 이름을 입력합니다.

![광고 계정으로 Braze를 선택한 상태에서 오디언스를 LinkedIn에 동기화합니다.][11]

{% tabs %}
{% tab 새로운 오디언스 만들기 %}

**새로운 오디언스 만들기**<br>
새 오디언스의 이름을 입력하고 **오디언스에 사용자 추가**를 선택한 다음 LinkedIn과 동기화할 필드를 선택합니다. 이 통합을 위해 현재 지원되는 기능은 다음과 같습니다: 
- 이메일
- 이름 및 성
- Android GAID

그런 다음, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장합니다.

![선택한 Braze 광고 계정, '리드' 오디언스, 오디언스에 사용자를 추가하는 액션, 일치시킬 필드로 이메일, Android GAID, 이름과 성이 있는 "리드" 오디언스 예시]({% image_buster /assets/img/linkedin/linkedin10.png %})

대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 또한 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다.

!['리드' 오디언스가 생성되었음을 확인합니다.]({% image_buster /assets/img/linkedin/linkedin9.png %})

새로운 오디언스와 함께 캔버스를 시작하면, Braze는 오디언스 동기화 구성요소에 들어가면 거의 실시간으로 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

**기존 오디언스와 동기화**<br>
또한 Braze는 기존 LinkedIn 오디언스에 사용자를 추가하여 해당 오디언스가 최신 상태인지 확인할 수 있는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력하고 **오디언스에 추가합니다**. 그러면 Braze는 오디언스 동기화 구성요소에 사용자가 들어오는 대로 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기입니다. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### 5단계: 캔버스 실행

오디언스 동기화를 LinkedIn에 구성한 후에는 캔버스를 실행하기만 하면 됩니다! 새 오디언스가 생성되고 오디언스 동기화 단계를 통해 유입되는 사용자는 LinkedIn에서 이 오디언스로 전달됩니다. 캔버스에 후속 구성 요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

광고 계정으로 이동하여 탐색의 **자산** 섹션에서 **오디언스를** 선택하면 LinkedIn의오디언스를 확인할 수 있습니다. **오디언스** 페이지에서 300명 이상의 회원에게 도달한 후 각 오디언스의 규모를 확인할 수 있습니다.

![주어진 대상에 대한 다음 메트릭을 나열하는 LinkedIn 페이지입니다.][8]

## 사용자 동기화 및 속도 제한 고려 사항

사용자가 오디언스 동기화 단계에 도달하면 Braze는 LinkedIn의 API 속도 제한을 준수하면서 거의 실시간으로 해당 사용자를 동기화합니다. 실제로 Braze는 이러한 사용자를 LinkedIn으로 보내기 전에 5초마다 최대한 많은 사용자를 일괄 처리하려고 시도합니다.

LinkedIn의 API 속도 제한은 초당 쿼리 10건, 요청당 사용자 수 100,000명을 초과할 수 없습니다. Braze 고객이 이 속도 제한에 도달하면 Braze 더 캔버스는 최대 약 13시간 동안 동기화를 재시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

## 분석 이해

다음 표에는 오디언스 동기화 구성 요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| METRIC | 설명 |
| ------ | ----------- | 
| 진입함 | LinkedIn에 동기화하기 위해 이 구성 요소를 입력한 사용자 수입니다. |
| 다음 단계로 진행됨 | 다음 구성요소로 진행한 사용자가 있는 경우 몇 명인가요? 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 사용자가 동기화됨 | LinkedIn에 성공적으로 동기화된 사용자 수입니다. |
| 사용자가 동기화되지 않음 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 사용자가 보류 중임 | 현재 Braze가 LinkedIn에 동기화하기 위해 처리 중인 사용자 수입니다. |
| 사용자에서 오류 발생 | 약 13시간 동안의 재시도 후 API 오류로 인해 LinkedIn에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 잘못된 LinkedIn 토큰 또는 LinkedIn에서 오디언스가 삭제된 경우 등이 있습니다. |
| 캔버스에서 나감 | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 오디언스 동기화 구성요소일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
각각 일괄 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류가 발생한 사용자 측정기준에 대한 보고가 지연될 수 있습니다.
{% endalert %}

{% alert important %}
LinkedIn은 플랫폼 내에서 일치율에 대한 추가 지표를 제공합니다. 특정 오디언스 동기화의 일치 여부를 검토하려면 오디언스 동기화 단계 지표를 선택하여 **캔버스 단계 세부 정보** 페이지로 이동합니다.
<br><br>
파트너를 **LinkedIn**, 광고 계정, 오디언스로 선택하면 LinkedIn에서 오디언스 규모와 일치율을 확인할 수 있습니다.

![입력된 사용자가 10,000명인 오디언스 동기화 단계 지표의 예.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Frequently asked questions

### How long will it take for the audience sizes to populate in LinkedIn?

LinkedIn 계정 내에서 오디언스를 확인하려면 최대 48시간이 지연될 수 있습니다.

### What is the minimum audience size for LinkedIn to populate within your ad account?

LinkedIn 계정 내 오디언스 규모를 채우려면 오디언스에 최소 300명의 회원이 포함되어야 합니다.

### What should I do next if I receive an invalid token error?

LinkedIn 파트너 페이지에서 LinkedIn 계정 연결을 끊었다가 다시 연결할 수 있습니다. 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 LinkedIn 관리자에게 확인합니다.

### Why is my Canvas not allowed to launch?

Confirm your LinkedIn ad account has successfully connected to Braze on the LinkedIn partner page. Next, make sure you've selected an ad account, entered a name for the new audience, and selected fields to match.

### 사용자를 LinkedIn에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요?

LinkedIn does provide information around match rates in their dashboard. LinkedIn의 **대상** 섹션에서 검토할 수 있습니다. You can review the match rate for your LinkedIn Audience in the Canvas step details of your Audience Sync step.

### How many audiences can LinkedIn support?

현재 LinkedIn 광고 계정의 오디언스 수에는 제한이 없습니다.

### Why is a segment stuck in BUILDING status and not updated?

초안 또는 활성 캠페인에서 30일 동안 지속적으로 사용되지 않으면 세그먼트가 사용되지 않은 것으로 간주되어 보관됨으로 설정됩니다. 이 때문에 업데이트가 보관된 세그먼트로 스트리밍될 때 세그먼트가 ARCHIVED에 "고정"된 것처럼 보일 수 있으며, 따라서 해당 세그먼트가 다시 보관되기 직전에 새로운 업데이트가 사용되지 않는 세그먼트로 스트리밍되어 BUILDING 상태가 됩니다.


[1]: {% image_buster /assets/img/linkedin/linkedin1.png %}
[2]: {% image_buster /assets/img/linkedin/linkedin2.png %}
[3]: {% image_buster /assets/img/linkedin/linkedin3.png %}
[4]: {% image_buster /assets/img/linkedin/linkedin4.png %}
[5]: {% image_buster /assets/img/linkedin/linkedin5.png %}
[6]: {% image_buster /assets/img/linkedin/linkedin6.png %}
[7]: {% image_buster /assets/img/linkedin/linkedin7.png %}
[8]: {% image_buster /assets/img/linkedin/linkedin8.png %}
[9]: {% image_buster /assets/img/linkedin/linkedin.png %}
[11]: {% image_buster /assets/img/linkedin/linkedin20.png %}