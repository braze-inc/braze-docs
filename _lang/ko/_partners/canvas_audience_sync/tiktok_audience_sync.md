---
nav_title: TikTok
article_title: TikTok에 Canvas Audience Sync
alias: /tiktok_audience_sync/
description: "이 참조 문서에서는 Braze Audience Sync to TikTok을 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
Tool:
  - Canvas
page_order: 8

---

# TikTok에 Audience Sync

Braze Audience Sync to TikTok을 사용하면 브랜드는 자체 Braze 통합에서 사용자 데이터를 TikTok 오디언스에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 활용할 수 있습니다.

**Audience Sync의 일반적인 활용 사례는 다음과 같습니다**:

- 여러 채널을 통해 고가치 사용자를 타겟팅하여 구매 또는 참여를 유도
- 다른 마케팅 채널에 반응이 적은 사용자를 리타겟팅
- 이미 브랜드의 충성 소비자인 사용자가 광고를 받지 않도록 억제 오디언스 생성
- 신규 사용자를 더 효율적으로 확보하기 위한 유사 오디언스(Actalike Audiences) 생성

이 기능을 통해 브랜드는 TikTok과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

{% alert important %}
**Audience Sync Pro 면책 조항**<br>
Braze Audience Sync to TikTok은 Audience Sync Pro 통합입니다. 이 통합에 대한 자세한 정보는 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 필수 조건

캔버스에서 TikTok Audience 단계를 설정하기 전에 다음 항목이 생성, 완료 및/또는 수락되었는지 확인해야 합니다.

| 요구 사항 | 출처 | 설명 |
| ----------- | ------ | ----------- |
| TikTok for Business Center 계정 | [TikTok](https://business.tiktok.com/) | 브랜드의 TikTok 자산(광고 계정, 페이지, 앱 등)을 관리하는 중앙 집중식 도구입니다. |
| TikTok 광고 계정 | [TikTok](https://ads.tiktok.com/) | 브랜드의 Business Center 계정에 연결된 활성 TikTok 광고 계정입니다.<br><br>TikTok Business Center 매니저 관리자가 Braze와 함께 사용할 TikTok 광고 계정에 대한 관리자 권한을 부여했는지 확인하세요. |
| TikTok 약관 및 정책 | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Pinterest Audience Sync 사용과 관련된 TikTok의 필수 약관, 정책, 가이드라인 및 문서(참조로 포함된 약관, 정책, 가이드라인 및 문서 포함)를 준수하는 데 동의합니다. 여기에는 상업 서비스 약관, 광고 약관, 개인정보 보호정책, 커스텀 오디언스 약관, 개발자 서비스 약관, 개발자 데이터 공유 계약, 광고 정책, 브랜드 가이드라인 및 커뮤니티 가이드라인이 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: TikTok에 연결

{% alert important %}
TikTok을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)이 필요합니다.
{% endalert %}

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **TikTok**을 선택합니다. TikTok Audience Sync 아래에서 **Connect TikTok**을 선택합니다.

![Braze의 TikTok 기술 페이지에는 개요 섹션과 Connect TikTok 버튼이 있는 TikTok Audience Sync 섹션이 있습니다.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

그러면 TikTok OAuth 페이지로 리디렉션되어 Braze에 광고 계정 관리 및 오디언스 관리 권한을 부여합니다. **확인**을 선택하면 Braze로 다시 리디렉션되어 동기화할 TikTok 광고 계정을 선택할 수 있습니다.

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

성공적으로 연결되면 파트너 페이지로 돌아갑니다. 여기에서 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

TikTok 연결은 Braze 앱 그룹 수준에서 적용됩니다. TikTok 관리자가 TikTok Business Center에서 사용자를 제거하거나 연결된 TikTok 계정에 대한 액세스를 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 그 결과 TikTok Audience 구성요소를 사용하는 활성 캔버스에 오류가 표시되며, Braze는 사용자를 동기화할 수 없게 됩니다.

### 2단계: 캔버스에 TikTok Audience 구성요소 추가

캔버스에 구성요소를 추가하고 **Audience Sync**를 선택합니다.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3단계: 동기화 설정

**Custom Audience** 버튼을 클릭하여 구성요소 편집기를 엽니다.

원하는 Audience Sync 파트너로 **TikTok**을 선택합니다.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

그런 다음 원하는 TikTok 광고 계정을 선택합니다. **Choose a New or Existing Audience** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab 새 오디언스 생성 %}

**새 오디언스 생성**<br>
새 오디언스의 이름을 입력하고 **Add Users to Audience**를 선택한 다음 TikTok과 동기화할 필드를 선택합니다. 그런 다음 단계 편집기 하단의 **Create Audience** 버튼을 클릭하여 오디언스를 저장합니다.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

오디언스가 성공적으로 생성되었거나 오류가 발생한 경우 Braze가 단계 편집기 상단에 알림을 표시합니다. 오디언스가 초안 모드로 생성되었기 때문에 나중에 캔버스 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

새 오디언스로 캔버스를 시작하면 Braze는 사용자가 오디언스 단계에 진입할 때 거의 실시간으로 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

**기존 오디언스와 동기화**<br>
Braze는 기존 TikTok 오디언스에 사용자를 추가하여 해당 오디언스를 최신 상태로 유지하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에서 기존 오디언스 이름을 입력하고 **Add to the Audience**를 선택합니다. 그러면 Braze는 사용자가 TikTok Audience 단계에 진입할 때 거의 실시간으로 사용자를 추가합니다.

![Custom Audience 캔버스 단계의 확장된 보기입니다. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### 4단계: 캔버스 시작
TikTok Audience 구성요소를 구성한 후 캔버스를 시작하면 됩니다! 새 오디언스가 생성되고, TikTok Audience 구성요소를 통과하는 사용자는 TikTok의 이 오디언스에 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

**Ads Manager Account**에 접속하고 **자산** 드롭다운에서 **Audiences**를 선택하여 TikTok에서 오디언스를 확인할 수 있습니다. **Audience** 페이지에서 &#126;1,000명에 도달한 후 각 오디언스의 규모를 확인할 수 있습니다.

![지정된 오디언스에 대한 다음 측정기준이 나열된 TikTok 페이지입니다.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## 사용자 동기화 및 사용량 제한 고려 사항

사용자가 Audience Sync 단계에 도달하면 Braze는 TikTok의 마케팅 API 사용량 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 TikTok으로 전송하기 전에 5초마다 가능한 한 많은 사용자를 배치하고 처리합니다.

TikTok의 세그먼트 API 사용량 제한은 초당 최대 50개의 쿼리와 요청당 10,000명의 사용자를 허용합니다. 고객이 이 한도에 도달하면 Braze는 최대 &#126;13시간 동안 동기화를 재시도합니다. 동기화가 여전히 불가능한 경우 Braze는 이러한 사용자를 Users Errored 측정기준 아래에 나열합니다.

## 분석 이해하기

다음 표에는 Audience Sync 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| Entered | TikTok에 동기화하기 위해 이 구성요소에 진입한 사용자 수입니다. |
| Proceeded to Next Step | 다음 구성요소가 있는 경우 다음 구성요소로 진행한 사용자 수입니다. 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| Users Synced | TikTok에 성공적으로 동기화된 사용자 수입니다. 이는 TikTok에서 매칭된 사용자와 동일하지 않습니다. |
| Users Not Synced | 매칭할 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| Users Pending | 현재 Braze에서 TikTok으로 동기화하기 위해 처리 중인 사용자 수입니다. |
| Users Errored | 약 13시간의 재시도 후 API 오류로 인해 TikTok에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인에는 유효하지 않은 TikTok 토큰 또는 TikTok에서 오디언스가 삭제된 경우가 포함될 수 있습니다. |
| Exited Canvas | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 Audience Sync 구성요소인 경우에 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
대량 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류 발생 사용자 측정기준의 보고에 지연이 있을 수 있습니다.
{% endalert %}

## 자주 묻는 질문

### 유효하지 않은 토큰 오류를 받으면 어떻게 해야 하나요?

TikTok 파트너 페이지에서 TikTok 계정의 연결을 해제하고 다시 연결할 수 있습니다. TikTok Business Center 관리자에게 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 확인하세요.

### 캔버스를 시작할 수 없는 이유는 무엇인가요?

TikTok 파트너 페이지에서 TikTok 계정이 Braze에 성공적으로 연결되었는지 확인하세요. 그런 다음 광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 매칭할 필드를 선택했는지 확인하세요.

### TikTok에 사용자를 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요?

TikTok은 데이터 프라이버시 정책에 따라 이 정보를 제공하지 않습니다.

### TikTok에서 오디언스가 채워지는 데 얼마나 걸리나요?

오디언스 크기는 TikTok Ads Manager의 Audiences 페이지에서 24~48시간 이내에 업데이트됩니다.

### TikTok 광고 계정에서 보유할 수 있는 최대 오디언스 수는 얼마인가요?

TikTok 광고 계정당 최대 400개의 오디언스를 보유할 수 있습니다.

### TikTok의 오디언스 크기 또는 매칭률이 Braze의 Audience Sync에서 동기화된 사용자보다 높은 이유는 무엇인가요?

이는 TikTok에서 하나의 ID가 여러 TikTok 사용자와 연결될 수 있기 때문입니다. 이는 클라이언트가 모바일 광고 ID(iOS IDFA 및 Android GAID)를 사용할 때 가장 자주 발생하는데, 하나의 기기에 여러 TikTok 사용자가 로그인되어 있을 수 있기 때문입니다.

또한 TikTok은 Pangle 사용자도 매칭된 사용자로 계산하므로 일부 경우 매칭률이 높아질 수 있습니다. 그러나 광고 전달을 위해 오디언스를 사용할 때 실제 전달 가능한 오디언스 크기는 게재 위치 및 기타 영향 요인에 따라 매칭된 사용자 크기만큼 높지 않을 수 있습니다.

### "캔버스에 대한 오디언스가 존재하지 않습니다"라는 제목의 이메일을 받는 이유는 무엇인가요?

동기화하려는 오디언스가 스트리밍 오디언스가 아닌 경우(예: 유사 오디언스 또는 사용자 파일 오디언스인 경우) 이 문제가 발생할 수 있습니다. Braze Audience Sync 캔버스 단계를 통해 새 오디언스를 생성해 보세요.