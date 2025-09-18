---
nav_title: Snapchat
article_title: Snapchat에 캔버스 오디언스 동기화
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Snapchat에 Braze 오디언스 동기화를 사용하는 방법을 다룹니다."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# 잠재 고객과 Snapchat 동기화

브랜드는 Braze 오디언스 동기화를 Snapchat에 사용하여 Braze 통합의 사용자 데이터를 Snapchat 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 사용하여 이제 Snapchat 고객 목록의 해당 사용자에게 광고를 트리거할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다:**

- 구매 또는 인게이지먼트를 유도하도록 여러 채널을 통해 고가치 사용자 타겟팅
- 다른 마케팅 채널에 반응이 저조한 사용자 리타겟팅
- 브랜드의 충성 고객인 사용자는 광고를 받지 않도록 억제 오디언스 생성
- 새로운 사용자를 더 효율적으로 확보하기 위해 유사 오디언스 생성

이 기능을 통해 사용자는 어떤 특정 퍼스트파티 데이터가 Snapchat과 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

{% alert important %}
**오디언스 Sync Pro 면책 조항**<br>
Snapchat에 Braze 오디언스 동기화는 Audience Sync Pro 통합 기능입니다. 이 통합에 대한 자세한 내용은 Braze 계정 매니저에게 문의하십시오.
{% endalert %}

## 전제 조건 

캔버스에서 Snapchat 오디언스 단계를 설정하기 전에 다음 항목이 생성, 완료 및/또는 수락되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| Snapchat 비즈니스 관리자 | Snapchat | 광고 계정, 페이지, 앱 등 브랜드의 Snapchat 자산을 관리할 수 있는 중앙집중식 툴입니다. |
| Snapchat 광고 계정 | Snapchat | 브랜드의 Snapchat 비즈니스 매니저 브랜드에 연결된 활성 Snapchat 광고 계정.<br><br>Snapchat 비즈니스 매니저 관리자가 Braze와 함께 사용하려는 Snapchat 광고 계정에 대한 관리자 권한을 부여했는지 확인하세요. |
| Snapchat 이용약관 및 정책 | [Snapchat](https://www.snap.com/en-US/policies) | 서비스 약관, 비즈니스 서비스 약관, 개발자 약관, 오디언스 매치, 광고 정책, 상업용 콘텐츠 정책, 커뮤니티 가이드라인 및 공급업체 책임 등 참조로 포함된 모든 약관, 정책, 가이드라인 및 문서를 포함하여 귀하의 Snapchat 오디언스 동기화 사용과 관련된 Snapchat의 모든 필수 약관, 정책, 가이드라인 및 설명서를 준수하는 데 동의합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합 

### 1단계: Snapchat에 연결

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Snapchat**을 선택합니다. 스냅챗 오디언스 동기화에서 **스냅챗 연결을** 선택합니다.

![개요 섹션과 Snapchat 오디언스 동기화 섹션이 포함된 Braze의 Snapchat 기술 페이지에 연결된 Snapchat 버튼이 있습니다.][1]{: style="max-width:80%;"}

그러면 오디언스 동기화 연동과 관련된 권한에 대해 Braze에 권한을 부여할 수 있는 Snapchat OAuth 페이지로 리디렉션됩니다.

확인을 선택하면 다시 Braze로 리디렉션되어 동기화할 Snapchat 광고 계정을 선택할 수 있습니다. 

![스냅챗에 연결할 수 있는 사용 가능한 광고 계정 목록입니다.][2]{: style="max-width:80%;"}

연결에 성공하면 파트너 페이지로 돌아가 연결된 계정을 확인하고 기존 계정을 연결 해제할 수 있습니다.

![광고 계정이 성공적으로 연결되었음을 보여주는 업데이트된 버전의 Snapchat 기술 파트너 페이지입니다.][3]{: style="max-width:80%;"}

Snapchat 연결은 Braze 워크스페이스 수준에서 적용됩니다. Snapchat 관리자가 Snapchat 비즈니스 매니저 또는 연결된 Snapchat 계정에 대한 액세스에서 사용자를 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 그 결과, Snapchat을 사용하는 활성 캔버스에 오류가 표시되고 Braze에서 사용자를 동기화할 수 없게 됩니다.

### 2단계: Snapchat에서 오디언스 동기화 단계 추가

캔버스에 구성 요소를 추가하고 **오디언스 동기화**를 선택하세요.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### 3단계: 동기화 설정

**사용자 지정 대상** 버튼을 클릭하여 컴포넌트 에디터를 엽니다.

원하는 오디언스 동기화 파트너로 **TikTok**을 선택합니다.

![][19]{: style="max-width:80%;"}

그런 다음, 원하는 Snapchat 광고 계정을 선택합니다. **새 대상 또는 기존 대상 선택** 드롭다운에서 새 대상 또는 기존 대상의 이름을 입력합니다.

{% tabs %}
{% tab 새로운 오디언스 만들기 %}

**새 오디언스 생성**<br>
새 오디언스의 이름을 입력하고 **오디언스에 사용자 추가**를 선택한 다음, Snapchat과 동기화할 필드를 선택합니다. 다음으로, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장하세요.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정을 선택하고 새 오디언스를 생성합니다.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 또한 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다.

![캔버스 컴포넌트에서 새 오디언스가 생성된 후 나타나는 경고입니다.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

새로운 오디언스와 함께 캔버스를 시작하면, Braze는 오디언스 동기화 구성요소에 들어가면 거의 실시간으로 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}
**기존 오디언스와 동기화**<br>
또한 Braze는 기존 Snapchat 오디언스에 사용자를 추가하여 해당 오디언스가 최신 상태인지 확인할 수 있는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력하고 **오디언스에 추가합니다**. 그러면 Braze는 오디언스 동기화 구성요소에 사용자가 들어오는 대로 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### 4단계: 캔버스 실행

Snapchat에 오디언스 동기화를 구성한 후 캔버스를 시작합니다! 새 오디언스가 생성되고 오디언스 동기화 단계를 통해 유입되는 사용자는 Snapchat에서 이 오디언스로 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

광고 관리자 계정으로 들어가 탐색의 자산 섹션에서 **오디언스**를 선택하면 Snapchat에서 오디언스를 확인할 수 있습니다. **잠재고객** 페이지에서 최대 1,000명에 도달한 후 각 잠재고객의 규모를 확인할 수 있습니다.

![Audience details for a given Snapchat audience that includes audience name, audience type, audience size, and audience retention in days.][9]

## 사용자 동기화 및 속도 제한 고려 사항

사용자가 오디언스 동기화 단계에 도달하면, Braze는 Snapchat의 API 사용량 제한을 준수하면서 거의 실시간으로 이러한 사용자를 동기화합니다. 실제로 Braze는 이러한 사용자를 Snapchat으로 보내기 전에 5초마다 최대한 많은 사용자를 배치 처리하려고 시도합니다.

Snapchat의 API 사용량 제한은 초당 10개의 쿼리를 초과할 수 없으며 요청당 100,000명의 사용자를 초과할 수 없다고 명시되어 있습니다. Braze 고객이 이 사용량 제한에 도달하면 Braze 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

### 분석 이해

다음 표에는 오디언스 동기화 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| 진입함 | 이 구성요소에 들어간 사용자 중 Snapchat에 동기화할 사용자 수. |
| 다음 단계로 진행됨 | 다음 구성요소로 진행한 사용자가 있는 경우 몇 명인가요? 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 사용자가 동기화됨 | 스냅챗에 성공적으로 동기화된 사용자 수입니다. |
| 사용자가 동기화되지 않음 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 사용자가 보류 중임 | 현재 Braze에서 Snapchat으로의 동기화를 처리 중인 사용자 수. |
| 사용자에서 오류 발생 | 약 13시간 동안의 재시도 후에도 API 오류로 인해 Snapchat에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 잘못된 Snapchat 토큰 또는 Snapchat에서 오디언스가 삭제된 경우 등이 있습니다. |
| 캔버스에서 나감 | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 오디언스 동기화 구성요소일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
각각 일괄 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류 측정기준에 대한 보고가 지연될 수 있습니다.
{% endalert %}   

## Frequently asked questions

### How many audiences can Snapchat support

현재 Snapchat 계정에서는 1,000명의 오디언스만 보유할 수 있습니다. 

If you exceed this limit, Braze will notify you that we can't create new audiences. You'll need to remove audiences you're no longer using in your Snapchat ad account.

### How do I know if users have matched after passing users to Snapchat?

Snapchat doesn't provide this information for their data privacy policies.

### What should I do next if I receive an invalid token error?

Snapchat 파트너 페이지에서 Snapchat 계정 연결을 끊었다가 다시 연결할 수 있습니다. Confirm with your Snapchat Business Manager admin that you have the appropriate permissions to the ad account you wish to sync with.

### Why is my Canvas not allowed to launch?

Make sure your Snapchat ad account successfully connects to Braze on the Snapchat partner page. Check that you've selected an ad account, entered a name for the new audience, and selected fields to match.


[1]: {% image_buster /assets/img/snapchat/snapchat1.png %}
[2]: {% image_buster /assets/img/snapchat/snapchat2.png %}
[3]: {% image_buster /assets/img/snapchat/snapchat3.png %}
[6]: {% image_buster /assets/img/snapchat/snapchat4.png %}
[7]: {% image_buster /assets/img/snapchat/snapchat5.png %}
[8]: {% image_buster /assets/img/snapchat/snapchat6.png %}
[9]: {% image_buster /assets/img/snapchat/snapchat7.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}