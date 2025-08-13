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

> Braze Audience Sync를 Facebook에 사용하면 Braze 통합에서 사용자 데이터를 Facebook 맞춤 오디언스에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다.

Braze Canvas에서 사용자 데이터를 기반으로 메시지(푸시, 이메일, SMS 또는 웹훅)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 Facebook의 맞춤 오디언스에 있는 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다. 예를 들어, Facebook에 Audience Sync를 구성하면 이메일, 전화번호, 이름, 성과 같은 다양한 1차 필드를 사용할 수 있습니다.

**맞춤 오디언스를 동기화하는 일반적인 사용 사례**:

- 구매 또는 참여를 유도하기 위해 여러 채널을 통해 높은 가치의 사용자 타겟팅.
- 다른 마케팅 채널에 반응이 저조한 사용자를 리타겟팅합니다.
- 브랜드의 충성 소비자인 사용자는 광고를 받지 않도록 억제 오디언스 생성.
- 새로운 사용자를 더 효율적으로 확보하기 위해 유사한 오디언스 생성.

이 기능을 통해 브랜드는 어떤 특정 퍼스트 파티 데이터가 Facebook과 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. 자세한 내용은 [개인정보 처리방침을](https://www.braze.com/privacy) 참조하세요.

## 사용자 동기화 및 속도 제한 고려 사항
 
사용자가 Audience Sync 단계에 도달하면 Braze는 Facebook의 마케팅 API 속도 제한을 준수하면서 거의 실시간으로 이러한 사용자를 동기화합니다. 즉, 실제로 Braze는 이러한 사용자를 Facebook으로 보내기 전에 5초마다 최대한 많은 사용자를 배치 처리하려고 시도합니다. 

Facebook의 마케팅 API 속도 제한은 한 시간 동안 각 광고 계정에 대해 ~190,000개의 API 요청을 초과할 수 없습니다. Braze 고객이 이 사용량 제한에 도달하면 Braze 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

## 필수 조건

Canvas에서 Facebook Audience 단계를 설정하기 전에 다음 항목이 생성되고 완료되었는지 확인해야 합니다. 

| 요구 사항 | Origin | 설명 |
| ----------- | ------ | ----------- |
| Facebook 비즈니스 관리자 | [Facebook][1] | 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리할 수 있는 중앙 집중식 도구입니다. |
| Facebook 광고 계정 | [Facebook][2] | 브랜드의 비즈니스 매니저와 연결된 활성 Facebook 광고 계정입니다.<br><br>Facebook 비즈니스 관리자 관리자가 Braze와 함께 사용할 계획인 Facebook 광고 계정에 대해 "캠페인 관리" 또는 "광고 계정 관리" 권한을 부여했는지 확인하십시오. 또한 광고 계정 이용약관을 수락했는지 확인하세요. |
| Facebook 커스텀 오디언스 약관 | [Facebook][3] | Braze와 함께 사용하려는 Facebook 광고 계정에 대해 Facebook의 맞춤 타겟 약관에 동의합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: Facebook에 연결

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Facebook**을 선택합니다. Facebook 대상 내보내기에서 **Facebook 연결을** 선택합니다.

![개요 섹션과 연결된 페이스북 버튼이 있는 페이스북 오디언스 내보내기 섹션이 포함된 Braze의 페이스북 기술 페이지입니다.][4]{: style="max-width:85%;"}

Facebook 광고 계정에 맞춤 오디언스를 생성할 수 있도록 Braze에 권한을 부여하는 Facebook oAuth 대화창이 나타납니다.

!['X로 연결'이라는 프롬프트가 표시된 첫 번째 Facebook 대화 상자. 여기서, X는 Facebook 사용자 아이디입니다.][6]{: style="max-width:30%;"}  ![광고 계정에 대한 광고 관리 권한을 묻는 두 번째 Facebook 대화 상자입니다.][5]{: style="max-width:40%;"}

Braze를 Facebook 계정에 연결하면, Braze 워크스페이스 내에서 동기화할 광고 계정을 선택할 수 있습니다. 

![Facebook에 연결할 수 있는 사용 가능한 광고 계정 목록입니다.][7]{: style="max-width:70%;"}

연결에 성공하면 파트너 페이지로 돌아가게 되며, 여기에서 연결된 계정을 보고 기존 계정을 연결 해제할 수 있습니다.

![Facebook 기술 파트너 페이지의 업데이트된 버전으로 광고 계정이 성공적으로 연결되었음을 보여줍니다.][8]{: style="max-width:85%;"}

Facebook 연결은 Braze 워크스페이스 수준에서 적용됩니다. 페이스북 관리자가 사용자를 페이스북 비즈니스 관리자에서 삭제하거나 연결된 페이스북 계정에 대한 액세스 권한을 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 결과적으로 Facebook 오디언스 구성요소를 사용하는 활성 캔버스에 오류가 표시되고 Braze는 사용자를 동기화할 수 없습니다. 

{% alert important %}
이전에 [광고 관리](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) 및 [광고 관리 표준 액세스](https://developers.facebook.com/docs/marketing-api/access#standard)에 대한 Facebook 앱 검토 절차를 거친 고객의 경우, 시스템 사용자 토큰은 Facebook 오디언스 구성요소에서 계속 유효합니다. Facebook 파트너 페이지를 통해서는 Facebook 시스템 사용자 토큰을 수정하거나 취소할 수 없습니다. 대신 Facebook 계정을 연결하여 Braze 워크스페이스 내에서 Facebook 시스템 사용자 토큰을 대체할 수 있습니다. 

<br><br>Facebook oAuth 구성은 [세그먼트를 사용한 Facebook 내보내기]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)에도 적용됩니다.
{% endalert %}

### 2단계: 커스텀 오디언스 서비스 약관 수락

Canvas를 구축하기 전에 다음 링크에서 Facebook 서비스 약관에 동의해야 합니다:

- **개인 계정에 대한 고객 목록 맞춤 오디언스 약관:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **비즈니스 계정에 대한 Facebook 비즈니스 도구 약관:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![고객 목록 맞춤 오디언스에 대해 수락해야 할 약관의 예입니다.][24]{: style="max-width:85%;"}
![Facebook 비즈니스 도구에 대해 수락해야 할 약관의 예입니다.][25]{: style="max-width:85%;"}

통합 시 Facebook 계정을 감사하는 데 대한 자세한 내용은 [FAQ 섹션](#terms)을 참조하십시오.

### 3단계: 캔버스 흐름에 Facebook 오디언스 구성요소 추가

캔버스에 컴포넌트를 추가하고 **Facebook 오디언스를** 선택합니다.

![Canvas에 추가할 구성 요소 목록입니다.][18]{: style="max-width:35%;"} ![Audience Sync 구성 요소입니다.][20]{: style="max-width:28%;"}

### 4단계: 동기화 설정

**커스텀 오디언스** 버튼을 선택하여 구성 요소 편집기를 엽니다. 그런 다음 **Facebook**을(를) 오디언스 동기화 파트너로 선택합니다.

!["오디언스 동기화 설정"에서 파트너 선택 옵션이 있습니다.][19]{: style="max-width:80%;"}

원하는 Facebook 광고 계정을 선택합니다. **새 대상 또는 기존 대상 선택** 드롭다운에서 새 대상 또는 기존 대상의 이름을 입력합니다. 

{% tabs %}
{% tab 새로운 오디언스 만들기 %}

1. 새 커스텀 오디언스의 이름을 입력합니다.
2. **오디언스에 사용자 추가**를 선택하고 Facebook과 동기화할 필드를 선택합니다. 
3. 다음으로 **오디언스 생성**을 선택하여 오디언스를 저장합니다.

!["버려진 장바구니" 오디언스에 대한 오디언스 동기화 설정으로 이메일, 전화번호, 이름 및 성 정보를 일치시킵니다.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

오디언스가 성공적으로 생성되었거나 이 과정에서 오류가 발생하면 단계 편집기 상단에서 알림을 받게 됩니다. 이 오디언스는 초안 모드에서 생성되었기 때문에 Canvas 여정에서 사용자 제거를 위해 참조할 수 있습니다.

!["버려진 장바구니" 오디언스가 생성되었다는 성공 메시지입니다.]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

새 오디언스와 함께 Canvas를 시작하면 Braze가 Canvas를 시작할 때 새 커스텀 오디언스를 생성하고 사용자가 오디언스 동기화 단계에 들어갈 때 거의 실시간으로 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

Braze는 기존 Facebook 커스텀 오디언스에서 사용자를 추가하거나 제거할 수 있는 기능을 제공하여 이러한 오디언스가 최신 상태인지 확인합니다. 기존 오디언스와 동기화하려면 다음을 수행하십시오:

1. 드롭다운에서 기존 오디언스 이름을 입력합니다.
2. **오디언스에 추가** 또는 **오디언스에서 제거**할지 선택합니다. 
3. Braze는 사용자가 Facebook 오디언스 단계에 들어갈 때 거의 실시간으로 사용자를 추가하거나 제거합니다. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook은 오디언스 크기가 너무 낮은 경우(일반적으로 1,000명 미만) 커스텀 오디언스에서 사용자를 제거하는 것을 금지합니다. 그 결과, Braze는 오디언스가 적절한 오디언스 크기에 도달할 때까지 오디언스 동기화 단계에서 사용자 제거를 동기화할 수 없습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5단계: 캔버스 실행

Facebook 오디언스 구성 요소를 구성한 후 Canvas를 시작할 시간입니다! 새 커스텀 오디언스가 생성되며, Facebook 오디언스 단계를 통과하는 사용자는 이 커스텀 오디언스에 전달됩니다. 사용자의 캔버스에 후속 단계가 포함되어 있으면, 사용자는 사용자 여정의 다음 단계로 진행하게 됩니다.

Facebook 오디언스 관리자의 맞춤 오디언스의 **기록** 탭에는 Braze에서 오디언스로 전송한 사용자 수가 반영됩니다. 사용자가 해당 단계에 다시 들어가면 Facebook으로 다시 전송됩니다.

![활동, 활동 세부 정보, 변경된 항목, 날짜 및 시간에 대한 열이 있는 오디언스 기록 표가 포함된 특정 Facebook 오디언스에 대한 오디언스 세부 정보 및 기록 탭.][9]{: style="max-width:80%;"}

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
내부 처리로 인해 동기화된 사용자와 오류가 발생한 사용자 메트릭에 대한 보고에 지연이 발생할 것입니다.
{% endalert %}

## Frequently asked questions

### 오디언스 동기화 파트너 대시보드에 오디언스가 채워지는 데 얼마나 걸리나요?

오디언스를 채우는 데 걸리는 시간은 특정 파트너에 따라 다릅니다. 모든 네트워크는 Braze의 요청을 처리하고 사용자를 매칭하려고 시도합니다. 커스텀 오디언스가 업데이트되는 데 최대 24시간이 걸릴 수 있습니다.

### 유효하지 않은 토큰 오류가 발생하면 다음에 무엇을 해야 합니까?

페이스북 파트너 페이지에서 페이스북 계정 연결을 끊었다가 다시 연결하면 됩니다. 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 Facebook 비즈니스 매니저 관리자에게 확인하세요.

### 내 캔버스가 시작할 수 없는 이유는 무엇입니까?

- 시스템 사용자 토큰이 인증되었으며 Facebook 비즈니스 관리자에서 원하는 광고 계정에 액세스할 수 있는지 확인하세요.
- 광고 계정을 선택하고, 새 맞춤 타겟의 이름을 입력하고, 일치시킬 필드를 선택했는지 확인하세요.
- Facebook의 커스텀 오디언스 제한인 500명에 도달했을 수 있습니다. 새로운 커스텀 오디언스를 캔버스를 사용하여 만들기 전에 불필요한 항목을 삭제하려면 Facebook 오디언스 매니저로 가세요.

### 사용자를 Facebook으로 전달한 후 사용자가 일치했는지 어떻게 알 수 있나요?

Facebook은 개인정보 보호를 위해 이 정보를 제공하지 않습니다.

### Braze는 가치 기반 커스텀 오디언스를 지원하나요?

현재 가치 기반 사용자 지정 오디언스는 Braze에서 지원되지 않습니다. 이러한 유형의 사용자 지정 대상을 동기화하는 데 관심이 있는 경우 [제품 피드백을]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) 제출하세요.

### Braze는 데이터를 Audience Sync 파트너에게 전송하기 전에 해시 처리하나요?

이메일 데이터가 정규화되면 Braze는 SHA256으로 해시합니다.

**IDFA/AAID/phone:** Braze는 SHA256으로 해시합니다. 우리가 동기화하는 오디언스 유형은 항상 다음 중 하나입니다:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256\.

빈도 측면에서 Braze는 사용자가 동기화 준비를 위해 사용자 여정의 Audience Sync 단계에 들어갈 때만 개인 식별 정보(PII)를 해시합니다.

### 가치 기반 유사 오디언스 동기화 문제를 어떻게 해결하나요?

현재 가치 기반 유사 커스텀 오디언스는 Braze에서 지원되지 않습니다. 이 오디언스과 동기화를 시도하면 오디언스 동기화 단계에서 오류가 발생할 수 있습니다. 이 문제를 해결하려면 다음 단계를 따르세요:

1. Facebook 광고 관리자 대시보드로 이동하여 **오디언스를** 선택합니다.
2. **오디언스 생성** > **커스텀 오디언스**를 선택합니다.
3. **고객 목록**을 선택합니다.
4. **값** 열 없이 CSV 또는 목록을 업로드합니다. **아니요, 고객 가치를 포함하지 않은 고객 목록으로 계속 진행**을 선택합니다.
5. 커스텀 오디언스 생성을 완료합니다.
6. Braze에서 생성한 커스텀 오디언스로 Facebook 오디언스 동기화 단계를 업데이트합니다.

### Facebook 커스텀 오디언스 서비스 약관과 관련된 이메일을 받았습니다. 이 문제를 해결하려면 무엇을 해야 하나요?

오디언스 동기화를 Facebook에 사용하려면 본 서비스 약관에 동의해야 합니다. 

- 광고 계정이 개인 Facebook 계정과 직접 연결되어 있는 경우, 개인 계정에서 서비스 약관을 수락할 수 있습니다: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- 광고 계정이 회사의 비즈니스 관리자 계정에 연결되어 있는 경우, Facebook 비즈니스 관리자 계정에서 서비스 약관을 수락해야 합니다: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Facebook 맞춤 오디언스 서비스 약관을 수락한 후 다음을 수행합니다:

1. Facebook 계정 연결을 끊고 다시 연결하여 Braze에 대한 Facebook 액세스 토큰을 새로 고치세요.
2. 캔버스를 편집하고 업데이트하여 Facebook 오디언스 동기화 단계를 다시 활성화합니다.

그런 다음, Braze는 사용자가 Facebook Audience Sync 단계에 도달하는 즉시 동기화할 수 있습니다.

## 문제 해결

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>오류</th>
      <th>설명</th>
      <th>해결 단계</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>유효하지 않은 토큰</b></td>
      <td>일반적인 원인은 통합을 연결한 사용자가 비밀번호를 변경하거나 자격 증명이 만료되는 경우 등입니다.</td>
      <td><b>파트너 통합</b> > <b>Facebook</b>로 이동하여 계정을 연결 해제한 후 다시 연결하세요. Facebook 계정을 감사하기 위한 추가 단계는 <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>이 문제 해결 섹션</a>을 참조하세요.</td>
    </tr>
    <tr>
      <td><b>잠재 고객 규모가 너무 낮음</b></td>
      <td>사용자를 오디언스에서 제거하는 Audience Sync 단계를 생성한 경우 이 오류가 발생할 수 있습니다. 오디언스 크기가 0에 가까워지면 네트워크에서 오디언스 크기가 너무 작아서 서비스를 제공할 수 없다는 플래그를 지정할 수 있습니다.</td>
      <td> 오디언스 크기를 완전히 소진하지 않도록 정기적으로 사용자를 추가 및 제거하는 Audience Sync 전략을 사용하세요.</td>
    </tr>
    <tr>
      <td><b>대상자가 존재하지 않음</b></td>
      <td>Audience Sync 단계는 존재하지 않거나 삭제된 오디언스를 사용합니다. 필요한 권한이 더 이상 없으면 이 오류가 발생할 수 있습니다.</td>
      <td>관리자에게 파트너 플랫폼에서 오디언스가 여전히 존재하는지 확인하도록 하세요. <br><br>존재하는 경우, 통합을 연결한 사용자가 오디언스에 대한 권한이 있는지 확인하세요. 권한이 없는 경우, 해당 오디언스에 대한 접근 권한을 부여해야 합니다. <br><br>오디언스가 의도적으로 제거된 경우, 활성 오디언스를 추가하고 단계에서 새 오디언스를 생성하세요.</td>
    </tr>
    <tr>
      <td><b>광고 계정 액세스 시도</b></td>
      <td>선택한 광고 계정이나 오디언스에 대한 권한이 없습니다.</td>
      <td>광고 계정의 관리자와 협력하여 적절한 접근 및 권한을 얻으세요.</td>
    </tr>
    <tr>
      <td><b>서비스 약관이 수락되지 않음</b></td>
      <td>Facebook과 같은 일부 Audience Sync 목적지에서는 Audience Sync 기능을 사용하기 위해 특정 서비스 약관을 수락해야 합니다. 적절한 약관을 수락하지 않으면 이 오류가 발생합니다. 결과적으로, Braze로부터 이 제목의 이메일을 받았을 수도 있습니다: “Facebook의 인증 자격 증명이 유효하지 않습니다.”</td>
      <td>Facebook의 필수 약관을 수락했는지 확인하십시오.</td>
    </tr>
    <tr>
      <td><b>모든 사용자가 오류가 발생했습니다.</b></td>
      <td>모든 사용자가 단계에서 오류가 발생하고 이 사용자가 선택된 필드에 값이 있는 것을 확인했음에도 불구하고, 이는 Facebook 계정에 문제가 있음을 나타낼 수 있습니다.</td>
      <td>계정에 문제가 있는지 확인하려면 <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>이 문제 해결 섹션</a>의 단계를 따르십시오.
      </td>
    </tr>
    <tr>
      <td><b>오디언스 생성 실패</b></td>
      <td>Facebook 기술 파트너 페이지에서 “연결됨”을 보고 있지만, 오디언스를 동기화할 때 Facebook 오디언스 동기화 단계에서 오류가 발생했습니다. “오디언스 "오디언스 이름" 생성 실패.” Facebook 계정의 인증에 실패했습니다. 계정을 다시 연결하려면 기술 파트너 페이지를 방문하십시오.</td>
      <td>계정에 문제가 있는지 확인하려면 <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>이 문제 해결 섹션</a>의 단계를 따르십시오.
      </td>
    </tr>
  </tbody>
</table>

### Facebook 계정을 감사하십시오.

통합에 추가 문제가 발생하면, Facebook 계정을 감사하기 위해 다음 섹션과 단계를 참조하십시오. 

#### 계정 권한 검토

1. 이 권한을 관리하는 방법에 대한 [Facebook의 설명서](https://www.facebook.com/business/help/186007118118684?id=829106167281625)를 검토하십시오. Facebook 비즈니스 관리자에 대해, 필요한 광고 계정에 접근할 수 있는 **관리자** 또는 **직원** 비즈니스 관리자 역할 중 적어도 하나가 필요합니다.
2. **직원**으로서, 오디언스를 생성하거나 사용자를 오디언스에 동기화하기 위해 각 광고 계정에 대한 전체 **광고 계정 관리** 권한을 관리자가 부여하는지 확인하십시오. 
3. 그 후, 계정을 분리하고 다시 연결해야 합니다.

#### 서비스 약관을 수락하십시오 {#terms}

Facebook의 보류 중인 서비스 약관(TOS)을 수락하십시오. Facebook은 주기적으로 사용자(당신)와 비즈니스 관리자에게 서비스 약관을 재승인하도록 요구할 것입니다.

1. 연결된 사용자는 각 광고 계정에 대한 모든 서비스 약관을 수락해야 합니다:
- 개인 Facebook 계정에 대한 맞춤 오디언스 약관:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- 가치 기반 맞춤 오디언스 약관:
  - 광고 계정이 회사의 비즈니스 관리자 계정에 연결되어 있는 경우, 여기에서 비즈니스 관리자 계정의 약관을 수락해야 합니다: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.
  - 광고 계정이 개인 계정(비즈니스와 연결되지 않음)에 연결되어 있는 경우, 여기에서 약관을 수락해야 합니다: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>`

![광고 계정을 관리할 수 있는 전체 제어 권한이 있는 계정입니다.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

계정 및 비즈니스 ID를 찾으려면 다음 단계를 따르세요:

1. [Facebook 광고 관리자 계정](https://adsmanager.facebook.com/)으로 이동하세요.
2. 드롭다운 메뉴에서 올바른 광고 계정을 확인하여 사용 중인지 확인하세요.
3. URL에서 `act=` 뒤에 있는 계정 ID와 `business_id=` 뒤에 있는 비즈니스 ID를 찾으세요.

![계정 ID와 비즈니스 ID가 강조 표시된 URL입니다.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. 맞춤 오디언스 약관에 대해 **수락**을 읽고 선택하세요. 약관이 서명되는 계정을 확인하기 위해 약관 상단의 드롭다운을 사용하는 것을 권장합니다.

![서비스 약관에 서명하는 계정을 보여주는 드롭다운입니다.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\. 서비스 약관에 대해 **수락**을 선택해야 합니다. 이후, 다음 메시지가 표시됩니다: "Braze를 대신하여 이러한 서비스 약관을 수락했습니다".
6\. Facebook 계정 연결을 끊고 다시 연결하여 Braze에 대한 Facebook 액세스 토큰을 새로 고치세요.
7\. 캔버스를 편집하고 업데이트하여 Facebook 오디언스 동기화 단계를 다시 활성화합니다. 그러면 Facebook 오디언스 단계에 도달하자마자 Braze가 사용자를 동기화할 수 있습니다.
8\. 문제가 지속되면, 광고 관리자를 통해 약관을 수동으로 수락할 수 있는 관리자 권한이 있는 별도의 사용자를 사용해 보세요.

#### 보류 중인 작업을 완료하세요 

Facebook 광고 서비스 사용을 차단할 수 있는 Facebook과의 보류 중인 작업이 있는지 확인하세요:

1. [페이스북 광고 관리자에 로그인](https://adsmanager.facebook.com/).
2. 문제가 있는 광고 계정을 선택하세요.
3. 탐색에서 **계정 개요**를 선택하세요. <br> ![계정 개요가 선택된 탐색입니다.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. 해결해야 할 경고가 있는지 확인하세요. <br> ![만료된 신용카드가 있는 계정입니다.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. 완료해야 할 설정 작업이 있는지 확인하세요. <br> ![부분적으로 완료된 계정 설정이 있는 계정입니다.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### 다른 사용자와 연결하세요.

또 다른 문제 해결 단계로, 다른 관리자 사용자가 다음을 수행하여 자신의 계정을 연결해 보기를 권장합니다:

1. 현재 통합을 끊으세요.
2. 관리 권한이 있는 다른 사용자가 자신의 페이스북 사용자 계정을 연결합니다.

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
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}