---
nav_title: TikTok
article_title: 캔버스 오디언스와 틱톡 동기화
alias: /tiktok_audience_sync/
description: "이 참고 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Braze 오디언스 동기화를 TikTok에 사용하는 방법을 다룹니다."
Tool:
  - Canvas
page_order: 7

---

# TikTok에 오디언스 동기화

브랜드는 Braze 오디언스 동기화 기능을 사용하여 자체 Braze 통합의 사용자 데이터를 TikTok 오디언스에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 일반적으로 Braze 캔버스에서 메시지를 트리거하는 데 사용하는 모든 기준(푸시, 이메일, SMS, 웹훅 등). 

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다**:

- 여러 채널을 통해 고가치 사용자를 타겟팅하여 구매 또는 참여 유도하기
- 다른 마케팅 채널에 반응이 저조한 사용자 리타겟팅
- 이미 브랜드에 충성도가 높은 소비자인 사용자가 광고를 받지 못하도록 억제 타겟을 생성하기
- 새로운 사용자를 더 효율적으로 확보하기 위해 Actalike 오디언스 생성

이 기능을 통해 브랜드는 어떤 특정 퍼스트 파티 데이터가 TikTok과 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

{% alert important %}
**Audience Sync Pro 면책 조항**<br>
TikTok에 Braze 오디언스 동기화는 Audience Sync Pro 통합 기능입니다. 이 통합에 대한 자세한 내용은 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 전제 조건

캔버스에서 TikTok 오디언스 단계를 설정하기 전에 다음 항목이 생성, 완료 및/또는 수락되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| ----------- | ------ | ----------- |
| TikTok for Business Center 계정 | [TikTok](https://business.tiktok.com/) | 브랜드의 틱톡 자산(예: 광고 계정, 페이지, 앱)을 관리할 수 있는 중앙 집중식 툴입니다. |
| TikTok 광고 계정 | [TikTok](https://ads.tiktok.com/) | 브랜드의 비즈니스 센터 계정에 연결된 활성 틱톡 광고 계정입니다.<br><br>TikTok 비즈니스 센터 관리자가 Braze에 사용할 TikTok 광고 계정에 대한 관리자 권한을 부여했는지 확인하세요. |
| TikTok 이용 약관 및 정책 | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | 상업적 서비스 약관, 광고 약관, 개인정보 보호정책, 맞춤형 오디언스 약관, 개발자 서비스 약관, 개발자 데이터 공유 계약, 광고 정책, 브랜드 가이드라인 및 커뮤니티 가이드라인을 포함하여 여기에 참조로 포함된 모든 약관, 정책, 가이드라인 및 문서를 포함하여 귀하의 Pinterest 오디언스 동기화 사용과 관련된 TikTok의 모든 필수 약관, 정책, 가이드라인 및 문서를 준수하는 데 동의합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합 

### 1단계: TikTok에 연결

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하고 **TikTok**을 선택합니다. 틱톡 오디언스 동기화에서 **틱톡 연결을** 선택합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **통합**에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

![Braze의 틱톡 기술 페이지에는 개요 섹션과 연결된 틱톡 버튼이 있는 틱톡 오디언스 동기화 섹션이 있습니다.][1]{: style="max-width:75%;"}

그러면 광고 계정 관리 및 오디언스 관리를 위해 Braze에 권한을 부여하는 TikTok OAuth 페이지로 리디렉션됩니다. **확인**을 선택하면 다시 Braze로 리디렉션되어 동기화할 TikTok 광고 계정을 선택할 수 있습니다. 

![][2]{: style="max-width:75%;"}

연결에 성공하면 파트너 페이지로 돌아갑니다. 여기에서 어떤 계정이 연결되어 있는지 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![][3]{: style="max-width:75%;"}

틱톡 연결은 Braze 앱 그룹 수준에서 적용됩니다. 틱톡 관리자가 사용자를 틱톡 비즈니스 센터에서 삭제하거나 연결된 틱톡 계정에 대한 액세스 권한을 삭제하면 Braze에서 잘못된 토큰을 감지합니다. 결과적으로 TikTok 오디언스 구성요소를 사용하는 활성 캔버스에 오류가 표시되고 Braze는 사용자를 동기화할 수 없습니다.

### 2단계: 캔버스 흐름에 TikTok 오디언스 구성요소 추가

캔버스에 컴포넌트를 추가하고 **대상 동기화를** 선택합니다. 

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### 3단계: 동기화 설정

**사용자 지정 대상** 버튼을 클릭하여 컴포넌트 에디터를 엽니다.

원하는 오디언스 동기화 파트너로 **TikTok**을 선택합니다.

![][19]{: style="max-width:80%;"}

그런 다음 원하는 틱톡 광고 계정을 선택합니다. **새 대상 또는 기존 대상 선택** 드롭다운에서 새 대상 또는 기존 대상의 이름을 입력합니다.

![][11]

{% tabs %}
{% tab 새로운 오디언스 만들기 %}

**새로운 오디언스 만들기**<br>
새 오디언스의 이름을 입력하고 **오디언스에 사용자 추가**를 선택한 다음, TikTok과 동기화할 필드를 선택합니다. 그런 다음, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장합니다.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 또한 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

새로운 오디언스와 함께 캔버스를 시작하면, Braze는 오디언스 단계에 들어가면 거의 실시간으로 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

**기존 오디언스와 동기화**<br>
Braze는 또한 기존 TikTok 오디언스에 사용자를 추가하여 이러한 오디언스가 최신 정보를 확인할 수 있도록 하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력하고 **오디언스에 추가합니다**. 그러면 Braze는 사용자가 TikTok 오디언스 단계에 진입하면 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### 4단계: 캔버스 실행
틱톡 오디언스 컴포넌트를 구성한 후에는 캔버스를 실행하기만 하면 됩니다! 새로운 오디언스가 생성되고, TikTok 오디언스 구성 요소를 통해 유입되는 사용자는 TikTok에서 이 오디언스로 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

**광고 관리자 계정**으로 들어가서 **자산** 드롭다운에서 **오디언스**를 선택하면 TikTok에서 오디언스를 확인할 수 있습니다. **오디언스** 페이지에서 최대 1,000명에 도달한 후 각 오디언스의 규모를 확인할 수 있습니다.

![지정된 오디언스에 대한 다음 측정지표가 나열된 TikTok 페이지입니다.][5]

## 사용자 동기화 및 속도 제한 고려 사항

사용자가 오디언스 동기화 단계에 도달하면 Braze는 틱톡의 마케팅 API 속도 제한을 준수하면서 거의 실시간으로 해당 사용자를 동기화합니다. 즉, Braze는 5초마다 최대한 많은 사용자를 일괄 처리하고 처리한 후 해당 사용자를 TikTok으로 전송합니다.

TikTok의 세그먼트 API 사용량 제한은 초당 쿼리 50건, 요청당 사용자 10만 명 이하로 명시되어 있습니다. Braze 고객이 이 사용량 제한에 도달하면 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

## 분석 이해

다음 표에는 오디언스 동기화 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| 진입함 | 이 컴포넌트를 입력한 사용자 중 TikTok에 동기화할 사용자 수입니다. |
| 다음 단계로 진행됨 | 다음 구성요소가 있는 경우 다음 구성요소로 진행하는 사용자 수. 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 사용자가 동기화됨 | 틱톡에 성공적으로 동기화된 사용자 수입니다. 이는 틱톡에서 매칭된 사용자와는 동일하지 않다는 점에 유의하세요. |
| 사용자가 동기화되지 않음 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 사용자가 보류 중임 | 현재 Braze가 틱톡에 동기화하기 위해 처리 중인 사용자 수입니다. |
| 사용자에서 오류 발생 | 약 13시간 동안의 재시도 후 API 오류로 인해 TikTok에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 유효하지 않은 TikTok 토큰이 있거나 오디언스가 TikTok에서 삭제된 경우 등이 있습니다. |
| 캔버스에서 나감 | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 오디언스 동기화 구성요소일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
각각 일괄 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류가 발생한 사용자 측정기준에 대한 보고가 지연될 수 있습니다.
{% endalert %}

## 문제 해결

{% details 유효하지 않은 토큰 오류가 발생하면 어떻게 해야 하나요? %}
TikTok 파트너 페이지에서 TikTok 계정 연결을 해제했다가 다시 연결할 수 있습니다. 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 TikTok 비즈니스 센터 관리자에게 확인하세요.
{% enddetails %}

{% details 왜 내 캔버스가 시작되지 않나요? %}
틱톡 파트너 페이지에서 틱톡 계정이 Braze에 성공적으로 연결되었는지 확인합니다.
광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 일치시킬 필드를 선택했는지 확인합니다.
{% enddetails %}

{% details 사용자를 틱톡에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요? %}
TikTok은 데이터 프라이버시 정책과 관련해 이 정보를 제공하지 않습니다.
{% enddetails %}

{% details 내 오디언스가 TikTok에 표시되는 데 얼마나 걸리나요? %}
오디언스 규모는 24-48시간 이내에 TikTok 광고 매니저의 오디언스 페이지에서 업데이트됩니다.
{% enddetails %}

{% details 내 TikTok 광고 계정에서 보유할 수 있는 최대 오디언스는 몇 명인가요? %}
400
{% enddetails %}

[1]: {% image_buster /assets/img/tiktok/tiktok1.png %}
[2]: {% image_buster /assets/img/tiktok/tiktok2.png %}
[3]: {% image_buster /assets/img/tiktok/tiktok3.png %}
[4]: {% image_buster /assets/img/tiktok/tiktok4.png %}
[5]: {% image_buster /assets/img/tiktok/tiktok5.png %}
[6]: {% image_buster /assets/img/tiktok/tiktok6.png %}
[7]: {% image_buster /assets/img/tiktok/tiktok7.png %}
[8]: {% image_buster /assets/img/tiktok/tiktok8.png %}
[11]: {% image_buster /assets/img/tiktok/tiktok11.png %}
[12]: {% image_buster /assets/img/tiktok/tiktok12.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[14]: {% image_buster /assets/img/tiktok/tiktok14.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok15.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
