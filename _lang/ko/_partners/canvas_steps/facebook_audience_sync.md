---
nav_title: Facebook
article_title: 캔버스 오디언스와 페이스북 동기화
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Facebook에 Braze 오디언스 동기화를 사용하는 방법을 다룹니다."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Facebook에 오디언스 동기화

브랜드는 Braze 오디언스 동기화 기능을 Facebook에 사용하여 자체 Braze 통합의 사용자 데이터를 Facebook 맞춤 오디언스에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS 또는 웹훅)를 트리거하는 데 사용하는 모든 기준을 이제 맞춤 타겟을 사용하여 Facebook에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

**사용자 지정 대상을 동기화하는 일반적인 사용 사례는 다음과 같습니다**:

- 구매 또는 인게이지먼트를 유도하도록 여러 채널을 통해 고가치 사용자 타겟팅.
- 다른 마케팅 채널에 반응이 저조한 사용자를 리타겟팅합니다.
- 브랜드의 충성 소비자인 사용자는 광고를 받지 않도록 억제 오디언스 생성.
- 새로운 사용자를 더 효율적으로 확보하기 위해 유사 오디언스 생성.

이 기능을 통해 브랜드는 어떤 특정 퍼스트 파티 데이터가 Facebook과 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

## 필수 조건

캔버스에서 Facebook 오디언스 단계를 설정하기 전에 다음 항목을 생성하고 완료했는지 확인해야 합니다. 

| 요구 사항 | Origin | 설명 |
| ----------- | ------ | ----------- |
| Facebook 비즈니스 관리자 | [Facebook][1] | 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리할 수 있는 중앙 집중식 도구입니다. |
| Facebook 광고 계정 | [Facebook][2] | 브랜드의 비즈니스 매니저와 연결된 활성 Facebook 광고 계정입니다.<br><br>Facebook 비즈니스 관리자 관리자가 Braze에서 사용하려는 Facebook 광고 계정에 대해 '캠페인 관리' 또는 '광고 계정 관리' 권한을 부여했는지 확인하세요. 또한 광고 계정 이용약관을 수락했는지 확인하세요. |
| Facebook 커스텀 오디언스 약관 | [Facebook][3] | Braze와 함께 사용하려는 Facebook 광고 계정에 대해 Facebook의 맞춤 타겟 약관에 동의합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: Facebook에 연결

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Facebook**을 선택합니다. Facebook 대상 내보내기에서 **Facebook 연결을** 선택합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **통합**에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

![개요 섹션과 연결된 페이스북 버튼이 있는 페이스북 오디언스 내보내기 섹션이 포함된 Braze의 페이스북 기술 페이지입니다.][4]{: style="max-width:70%;"}

Facebook 광고 계정에 맞춤 오디언스를 생성할 수 있도록 Braze에 권한을 부여하는 Facebook oAuth 대화창이 나타납니다.

!['X로 연결'이라는 프롬프트가 표시된 첫 번째 Facebook 대화 상자. 여기서, X는 Facebook 사용자 아이디입니다.][6]{: style="max-width:30%;"}  ![광고 계정에 대한 광고 관리 권한을 묻는 두 번째 Facebook 대화 상자입니다.][5]{: style="max-width:40%;"}

Braze를 Facebook 계정에 연결하면, Braze 워크스페이스 내에서 동기화할 광고 계정을 선택할 수 있습니다. 

![Facebook에 연결할 수 있는 사용 가능한 광고 계정 목록입니다.][7]{: style="max-width:70%;"}

연결에 성공하면 파트너 페이지로 돌아가서 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![Facebook 기술 파트너 페이지의 업데이트된 버전으로 광고 계정이 성공적으로 연결되었음을 보여줍니다.][8]{: style="max-width:70%;"}

Facebook 연결은 Braze 워크스페이스 수준에서 적용됩니다. 페이스북 관리자가 사용자를 페이스북 비즈니스 관리자에서 삭제하거나 연결된 페이스북 계정에 대한 액세스 권한을 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 결과적으로 Facebook 오디언스 구성요소를 사용하는 활성 캔버스에 오류가 표시되고 Braze는 사용자를 동기화할 수 없습니다. 

{% alert important %}
이전에 [광고 관리](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) 및 [광고 관리 표준 액세스](https://developers.facebook.com/docs/marketing-api/access#standard)에 대한 Facebook 앱 검토 절차를 거친 고객의 경우, 시스템 사용자 토큰은 Facebook 오디언스 구성요소에서 계속 유효합니다. Facebook 파트너 페이지를 통해서는 Facebook 시스템 사용자 토큰을 수정하거나 취소할 수 없습니다. 대신 Facebook 계정을 연결하여 Braze 워크스페이스 내에서 Facebook 시스템 사용자 토큰을 대체할 수 있습니다. 

<br><br>Facebook oAuth 구성은 [세그먼트를 통한 Facebook 내보내기]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)에도 적용됩니다.
{% endalert %}

### 2단계: 커스텀 오디언스 서비스 약관 수락

캔버스를 구축하기 전에 먼저 Facebook 커스텀 오디언스 서비스 약관을 수락해야 합니다. 서비스 약관은 다음 링크에서 확인할 수 있습니다:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### 3단계: 캔버스 흐름에 Facebook 오디언스 구성요소 추가

캔버스에 컴포넌트를 추가하고 **Facebook 오디언스를** 선택합니다.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### 4단계: 동기화 설정

**사용자 지정 대상** 버튼을 클릭하여 컴포넌트 에디터를 엽니다.

원하는 오디언스 동기화 파트너로 **Facebook**을 선택합니다.

![][19]{: style="max-width:80%;"}

원하는 Facebook 광고 계정을 선택합니다. **새 대상 또는 기존 대상 선택** 드롭다운에서 새 대상 또는 기존 대상의 이름을 입력합니다. 

{% tabs %}
{% tab 새로운 오디언스 만들기 %}
**새로운 오디언스 만들기**<br>
새 사용자 지정 대상의 이름을 입력하고 **대상에 사용자 추가를** 선택한 다음 Facebook과 동기화할 필드를 선택합니다. 그런 다음, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장합니다.

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

그런 다음, 단계 편집기 하단의 오디언스 생성 버튼을 클릭하여 오디언스를 저장합니다. 대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 또한 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다.

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

새 오디언스가 있는 캔버스를 시작하면, Braze는 캔버스를 시작할 때 새로운 커스텀 오디언스를 생성하고 이후 오디언스 동기화 단계에 들어가면 거의 실시간으로 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}
**기존 오디언스와 동기화**<br>
또한 Braze는 기존 Facebook 커스텀 오디언스에서 사용자를 추가하거나 제거하여 이러한 오디언스가 최신 상태인지 확인하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력하고 **오디언스에 추가** 또는 **오디언스에서 제거** 여부를 선택합니다. 그러면 Braze는 Facebook 오디언스 단계에 사용자가 들어오는 대로 거의 실시간으로 사용자를 추가하거나 제거합니다. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

Facebook의 경우 오디언스 크기가 너무 작을 때는(일반적으로 1,000명 미만) 커스텀 오디언스에서 사용자를 제거할 수 없도록 하고 있습니다. 이에 따라, Braze는 해당 오디언스가 적절한 오디언스 크기에 도달할 때까지 오디언스에서 제거에 대해 사용자 동기화를 진행할 수 없습니다.

{% endtab %}
{% endtabs %}

### 5단계: 캔버스 실행

Facebook 오디언스 구성요소를 구성한 후에는 캔버스를 시작하기만 하면 됩니다! 새로운 맞춤 타겟이 생성되고, Facebook 오디언스 구성 요소를 통해 유입되는 사용자는 Facebook에서 이 맞춤 타겟으로 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

Facebook 오디언스 관리자의 맞춤 오디언스의 **기록** 탭에는 Braze에서 오디언스로 전송한 사용자 수가 반영됩니다. 사용자가 해당 단계에 다시 들어가면 Facebook으로 다시 전송됩니다.

![활동, 활동 세부 정보, 변경된 항목, 날짜 및 시간에 대한 열이 있는 오디언스 기록 표가 포함된 특정 Facebook 오디언스에 대한 오디언스 세부 정보 및 기록 탭.][9]{: style="max-width:80%;"}

## 메타 작업 계정으로 마이그레이션하기

2023년 7월부터 Meta는 이 새로운 계정 유형을 채택하는 데 관심이 있는 소규모 비즈니스에 메타 업무용 계정을 출시할 예정이라는 점을 알아두세요. Braze와 통합된 비즈니스 계정이 있는 경우, 이 구현을 유지하고 활성 캔버스를 방해하지 않으려면 비즈니스 계정으로 [Facebook 파트너 페이지]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)에 연결을 끊었다가 다시 연결해야 합니다.

## 사용자 동기화 및 속도 제한 고려 사항
 
사용자가 오디언스 동기화 단계에 도달하면, Braze는 Facebook의 마케팅 API 사용량 제한도 준수하면서 거의 실시간으로 이러한 사용자를 동기화합니다. 즉, 실제로 Braze는 이러한 사용자를 Facebook으로 보내기 전에 5초마다 최대한 많은 사용자를 배치 처리하려고 시도합니다. 

Facebook의 마케팅 API 사용량 제한에 따르면 1시간 동안 각 광고 계정에 대해 최대 19만 건의 API 요청이 지원됩니다. Braze 고객이 이 사용량 제한에 도달하면 Braze 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

## 분석 이해

다음 표에는 오디언스 동기화 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| 진입함 | Facebook에 동기화하기 위해 이 구성 요소를 입력한 사용자 수입니다. |
| 다음 단계로 진행됨 | 다음 구성 요소로 진급한 사용자 수(있는 경우). 캔버스 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 사용자가 동기화됨 | Facebook에 성공적으로 동기화된 사용자 수입니다. |
| 사용자가 동기화되지 않음 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 사용자가 보류 중임 | 현재 Braze가 Facebook에 동기화하기 위해 처리 중인 사용자 수입니다. |
| 사용자에서 오류 발생 | 약 13시간 동안의 재시도 후 API 오류로 인해 Facebook에 동기화되지 않은 사용자 수. 오류의 잠재적 원인으로는 잘못된 Facebook 토큰 또는 Facebook에서 커스텀 오디언스가 삭제된 경우 등이 있습니다. |
| 캔버스에서 나감 | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 Facebook 단계일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
각각 일괄 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류가 발생한 사용자 측정기준에 대한 보고가 지연될 수 있습니다.
{% endalert %}   

## 문제 해결

{% details 유효하지 않은 토큰 오류가 발생하면 어떻게 해야 하나요? %}
페이스북 파트너 페이지에서 페이스북 계정 연결을 끊었다가 다시 연결하면 됩니다. 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 Facebook 비즈니스 매니저에게 확인합니다.
{% enddetails %}

{% details 왜 내 캔버스가 시작되지 않나요? %}
- 시스템 사용자 토큰이 인증되었으며 Facebook 비즈니스 관리자에서 원하는 광고 계정에 액세스할 수 있는지 확인하세요.
- 광고 계정을 선택하고, 새 맞춤 타겟의 이름을 입력하고, 일치시킬 필드를 선택했는지 확인하세요.
- Facebook의 커스텀 오디언스 제한인 500명에 도달했을 수 있습니다. 캔버스를 사용하여 새 커스텀 오디언스를 생성하기 전에 Facebook 오디언스 매니저로 이동하여 불필요한 항목을 삭제합니다.
{% enddetails %}

{% details 사용자를 Facebook에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요? %}
Facebook은 개인정보 보호를 위해 이 정보를 제공하지 않습니다.
{% enddetails %}

{% details Braze는 가치 기반 맞춤 오디언스를 지원하나요? %}
현재 가치 기반 사용자 지정 오디언스는 Braze에서 지원되지 않습니다. 이러한 유형의 사용자 지정 대상을 동기화하는 데 관심이 있는 경우 [제품 피드백을]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) 제출하세요.
{% enddetails %}

{% details 가치 기반 유사 커스텀 오디언스를 동기화할 때 발생하는 문제를 해결하려면 어떻게 해야 하나요? %}

현재 가치 기반 유사 커스텀 오디언스는 Braze에서 지원되지 않습니다. 이 오디언스과 동기화를 시도하면 오디언스 동기화 단계에서 오류가 발생할 수 있습니다. 이 문제를 해결하려면 다음 단계를 따르세요:

1. Facebook 광고 관리자 대시보드로 이동하여 **오디언스를** 선택합니다.
2. **오디언스 생성** > **커스텀 오디언스**를 선택합니다.
3. **고객 목록**을 선택합니다.
4. **값** 열 없이 CSV 또는 목록을 업로드합니다. **아니요, 고객 가치를 포함하지 않은 고객 목록으로 계속 진행**을 선택합니다.
5. 커스텀 오디언스 생성을 완료합니다.
6. Braze에서 생성한 커스텀 오디언스로 Facebook 오디언스 동기화 단계를 업데이트합니다.
{% enddetails %}

{% details Facebook 맞춤 타겟 서비스 이용약관과 관련된 이메일을 받았습니다. 이 문제를 해결하려면 어떻게 해야 하나요? %}
오디언스 동기화를 Facebook에 사용하려면 본 서비스 약관에 동의해야 합니다. 

- 광고 계정이 개인 Facebook 계정과 직접 연결되어 있는 경우 개인 계정 내에서 TOS에 동의할 수 있습니다: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=ACCOUNT_ID`.
- 광고 계정이 회사의 비즈니스 관리자 계정에 연결되어 있는 경우 비즈니스 관리자 계정( `https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID`)에서 TOS에 동의해야 합니다.

Facebook 맞춤 오디언스 서비스 약관을 수락한 후 다음을 수행합니다:
1. Facebook 계정 연결을 끊고 다시 연결하여 Braze에 대한 Facebook 액세스 토큰을 새로 고치세요.
2. 캔버스를 편집하고 업데이트하여 Facebook 오디언스 동기화 단계를 다시 활성화합니다.
그러면 Facebook 오디언스 단계에 도달하자마자 Braze가 사용자를 동기화할 수 있습니다.
{% enddetails %}


[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
