---
nav_title: Pinterest
article_title: Pinterest에 캔버스 오디언스 동기화
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Pinterest에 Braze 오디언스 동기화를 사용하는 방법을 다룹니다."
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# 오디언스 Pinterest에 동기화

Pinterest에 Braze 오디언스 동기화를 사용하여 브랜드는 자체 Braze 통합의 사용자 데이터를 Pinterest 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 사용하여 이제 Pinterest 오디언스의 해당 사용자에게 광고를 트리거할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다:**

- 구매 또는 인게이지먼트를 유도하도록 여러 채널을 통해 고가치 사용자 타겟팅
- 다른 마케팅 채널에 반응이 저조한 사용자 리타겟팅
- 이미 브랜드에 충성도가 높은 소비자인 사용자가 광고를 받지 못하도록 억제 타겟을 생성하기
- 새로운 사용자를 더 효율적으로 확보하기 위해 Actalike 오디언스 생성

이 기능을 통해 브랜드는 어떤 특정 퍼스트파티 데이터가 Pinterest와 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

{% alert important %}
**오디언스 Sync Pro 면책 조항**<br>
Pinterest에 Braze 오디언스 동기화는 Audience Sync Pro 통합 기능입니다. 이 통합에 대한 자세한 내용은 Braze 계정 매니저에게 문의하십시오.
{% endalert %}

## 전제 조건 
캔버스에서 Pinterest 오디언스 단계를 설정하기 전에 다음 항목이 생성, 완료 및/또는 수락되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| Pinterest 비즈니스 허브 | [Pinterest](https://www.pinterest.com/business/hub/) | 브랜드의 Pinterest 자산(광고 계정, 페이지, 앱 등)을 관리하는 중앙 집중식 도구입니다. |
| Pinterest 광고 계정 | [Pinterest](https://ads.pinterest.com/) | 브랜드의 Pinterest 비즈니스 허브에 연결된 활성 Pinterest 광고 계정.<br><br>Pinterest 비즈니스 허브 관리자가 Braze와 함께 사용할 계획인 Pinterest 광고 계정에 대한 관리자 권한을 부여했는지 확인하십시오. |
| Pinterest 약관 및 정책 | Pinterest | Pinterest Audience Sync 사용에 관한 Pinterest의 필수 약관, 정책, 지침 및 설명서를 준수하는 데 동의하며, 여기에는 참조로 통합된 약관, 정책, 지침 및 설명서가 포함될 수 있습니다. 예를 들어, 서비스 약관, 비즈니스 서비스 약관, 개인정보 보호정책, 개발자 및 API 서비스 약관, 광고 데이터 약관, 광고 지침, 광고 서비스 계약, 커뮤니티 지침 및 브랜드 지침이 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합 

### 1단계: Pinterest에 연결

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Pinterest**를 선택합니다. Pinterest 오디언스 동기화에서 **연결 Pinterest**를 선택하세요.

![브레이즈의 핀터레스트 기술 페이지로, 개요 섹션과 핀터레스트 오디언스 동기화 섹션이 포함되어 있으며, 연결된 핀터레스트 버튼이 있습니다.][1]{: style="max-width:80%;"}

그런 다음, Pinterest OAuth 페이지로 리디렉션되어 Braze에 광고 계정 관리 및 오디언스 관리 권한을 부여합니다.

After selecting **Confirm**, you'll be redirected back into Braze to select which Pinterest ad accounts you wish to sync. 

![Pinterest에 연결할 수 있는 사용 가능한 광고 계정 목록.][2]{: style="max-width:80%;"}

When successfully connected, you'll return to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![성공적으로 연결된 광고 계정을 보여주는 Pinterest 기술 파트너 페이지의 업데이트된 버전입니다.][3]{: style="max-width:80%;"}

귀하의 Pinterest 연결은 Braze 작업 공간 수준에서 적용됩니다. Pinterest 관리자가 Pinterest 비즈니스 허브 또는 연결된 Pinterest 계정에 대한 액세스에서 사용자를 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 결과적으로 Pinterest 오디언스 구성요소를 사용하는 활성 캔버스에 오류가 표시되고 Braze는 사용자를 동기화할 수 없습니다.

### 2단계: 오디언스 동기화 단계를 Pinterest에 추가

캔버스에 구성 요소를 추가하고 **오디언스 동기화**를 선택하세요.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### 3단계: 동기화 설정

**커스텀 오디언스** 버튼을 클릭하여 구성요소 편집기를 엽니다.

**Pinterest**을(를) 원하는 오디언스 동기화 파트너로 선택하십시오.

![][19]{: style="max-width:80%;"}

그런 다음 원하는 Pinterest 광고 계정을 선택합니다. **새 오디언스 또는 기존 오디언스 선택 드롭다운**에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

{% tabs %}
{% tab 새로운 오디언스 만들기 %}

**새 오디언스 생성**<br>
새 오디언스의 이름을 입력하고, **오디언스에 사용자 추가**를 선택한 다음, Pinterest와 동기화할 필드를 선택하세요. 다음으로, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장하세요.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정을 선택하고 새 오디언스를 생성합니다.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 또한 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다.

![캔버스 컴포넌트에서 새 오디언스가 생성된 후 나타나는 경고입니다.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

새로운 오디언스와 함께 캔버스를 시작하면, Braze는 오디언스 동기화 단계에 들어가면 거의 실시간으로 사용자를 동기화합니다.
{% endtab %}
{% tab 기존 오디언스와 동기화 %}
**기존 오디언스와 동기화**<br>
또한 Braze는 기존 Pinterest 오디언스에 사용자를 추가하여 해당 오디언스가 최신 상태인지 확인할 수 있는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력하고 오디언스에 추가합니다. 그러면 Braze는 오디언스 동기화 단계에 사용자가 들어오는 대로 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### 4단계: 캔버스 실행

Pinterest에 오디언스 동기화를 구성한 후 캔버스를 시작합니다! 새 오디언스가 생성되고 오디언스 동기화 단계를 통해 유입되는 사용자는 Pinterest에서 이 오디언스로 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

광고 매니저 계정으로 들어가 광고 드롭다운에서 오디언스를 선택하여 Pinterest에서 오디언스를 볼 수 있습니다. 오디언스 페이지에서 ~100에 도달한 이후 각 오디언스의 크기를 확인할 수 있습니다.

![오디언스 이름, 오디언스 ID, 오디언스 유형, 오디언스 크기를 포함하는 지정된 Pinterest 오디언스의 오디언스 세부 정보.][11]

## 사용자 동기화 및 속도 제한 고려 사항

사용자가 오디언스 동기화 단계에 도달하면, Braze는 Pinterest의 마케팅 API 사용량 제한을 준수하면서 거의 실시간으로 이러한 사용자를 동기화합니다. 실제로 Braze는 이러한 사용자를 Pinterest로 보내기 전에 5초마다 최대한 많은 사용자를 배치 처리하려고 시도합니다.

Pinterest의 세그먼트 API 사용량 제한은 사용자당 초당 7개의 쿼리를 초과할 수 없으며 요청당 1,900명의 사용자를 초과할 수 없다고 명시되어 있습니다. Braze 고객이 이 사용량 제한에 도달하면 Braze 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

## 분석 이해

다음 표에는 오디언스 동기화 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| 진입함 | 이 구성요소에 들어간 사용자 중 Pinterest에 동기화할 사용자 수. |
| 다음 단계로 진행됨 | 다음 구성요소로 진행한 사용자가 있는 경우 몇 명인가요? 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 사용자가 동기화됨 | 성공적으로 Pinterest에 동기화된 사용자 수. |
| 사용자가 동기화되지 않음 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 사용자가 보류 중임 | 현재 Braze에서 Pinterest로 동기화하기 위해 처리 중인 사용자 수. |
| 사용자에서 오류 발생 | 약 13시간 동안의 재시도 후 API 오류로 인해 Pinterest에 동기화되지 않은 사용자 수. 오류의 잠재적 원인으로는 잘못된 Pinterest 토큰 또는 Pinterest에서 오디언스가 삭제된 경우 등이 있습니다. |
| 캔버스에서 나감 | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 오디언스 동기화 구성요소일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
각각 일괄 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류 측정기준에 대한 보고가 지연될 수 있습니다.
{% endalert %}   

## Frequently asked questions

### How long will it take for my audiences to populate in Pinterest?

The audience size will update within 24-48 hours on the **Audiences** page in Pinterest's Ads Manager.

### How do I know if users have matched after passing users to Pinterest?

Pinterest는 자체 데이터 프라이버시 정책에 대해 이 정보를 제공하지 않습니다.

### What should I do next if I receive an invalid token error?

Confirm with your Pinterest Business Hub admin that you have the appropriate permissions to the ad account you wish to sync. You can also disconnect and reconnect your Pinterest account on the Pinterest partner page. 

### Why is my Canvas not allowed to launch?

Pinterest 계정이 Pinterest 파트너 페이지에서 Braze에 성공적으로 연결되도록 하십시오. 광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 일치시킬 필드를 선택했는지 확인합니다.

### Why can't I select my ad account for my Audience Sync step?

Check that your token was generated with the correct account permissions. Note that if you have too many audiences in your Pinterest ad account, the dropdown to select your ad account may timeout. In this case, we recommend reducing the amount of audiences in your ad account.

[1]: {% image_buster /assets/img/pinterest/pinterest1.png %}
[2]: {% image_buster /assets/img/pinterest/pinterest2.png %}
[3]: {% image_buster /assets/img/pinterest/pinterest3.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[6]: {% image_buster /assets/img/pinterest/pinterest6.png %}
[7]: {% image_buster /assets/img/pinterest/pinterest7.png %}
[8]: {% image_buster /assets/img/pinterest/pinterest8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[9]: {% image_buster /assets/img/pinterest/pinterest9.png %}
[10]: {% image_buster /assets/img/pinterest/pinterest10.png %}
[11]: {% image_buster /assets/img/pinterest/pinterest11.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}