---
nav_title: Google
article_title: 캔버스 오디언스와 Google 동기화
alias: /google_audience_sync/
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Google에 Braze 오디언스 동기화를 사용하는 방법을 다룹니다."
Tool:
  - Canvas
page_order: 3

---

# Google에 오디언스 동기화

{% alert important %}
Google is updating its [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA, UK, and Switzerland end users, as well as obtain necessary consent from them. 자세한 내용은 다음 문서를 참조하세요.
{% endalert %}

Braze의 Google에 오디언스 동기화 통합을 통해 브랜드는 크로스채널 고객 여정의 도달 범위를 Google 검색, Google 쇼핑, Gmail, YouTube, Google 디스플레이로 확장할 수 있습니다. 퍼스트파티 고객 데이터를 사용하면 동적 행동 트리거, 세분화 등을 기반으로 광고를 안전하게 전달할 수 있습니다. 일반적으로 메시지를 트리거하는 데 사용하는 모든 기준(예: 푸시, 이메일 또는 SMS)을 Braze 캔버스의 일부로 사용하여 Google의 [고객 일치를](https://support.google.com/google-ads/answer/6379332?hl=en) 통해 해당 사용자에게 광고를 트리거할 수 있습니다.

{% alert important %}
2023년 5월 1일부터 Google Ads는 더 이상 타겟팅 및 보고를 위해 '유사 오디언스'라고도 하는 유사 오디언스를 생성하지 않습니다. 자세한 내용은 [Google 광고 설명서를](https://support.google.com/google-ads/answer/12463119?) 참조하세요.
{% endalert %}

**사용자 지정 대상을 동기화하는 일반적인 사용 사례는 다음과 같습니다:**
- 구매 또는 인게이지먼트를 유도하도록 여러 채널을 통해 고가치 사용자 타겟팅.
- 다른 마케팅 채널에 반응이 저조한 사용자를 리타겟팅합니다.
- 브랜드의 충성 소비자인 사용자는 광고를 받지 않도록 억제 오디언스 생성.

{% alert note %}
이 기능을 통해 브랜드는 어떤 특정 퍼스트파티 데이터가 Google과 공유되는지 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합을 최대한 고려합니다. Braze 데이터 개인정보 보호정책에 대해 자세히 알아보려면 [여기를](https://www.braze.com/privacy) 클릭하세요.
{% endalert %}

## 필수 조건

Make sure the following items are created and completed before setting up your Google Audience step in Canvas.

| 요구 사항 | Origin | 설명 |
| ----------- | ------ | ----------- |
| Google 광고 계정 | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | 브랜드에 대한 활성 Google 광고 계정입니다.<br><br>여러 관리 계정에서 오디언스를 공유하려는 경우, 오디언스를 [매니저 계정](https://support.google.com/google-ads/answer/6139186)에 업로드할 수 있습니다. |
| 구글 광고 약관 및 구글 광고 정책 | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | 귀하는 Braze 오디언스 동기화를 사용할 때 [EU 사용자 동의 정책을](https://www.google.com/about/company/user-consent-policy/) 포함한 Google의 [광고 약관](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) 및 [Google의 광고 정책](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC)을 수락하고 준수해야 합니다(해당되는 경우).<br><br>EEA, 영국 및 스위스 최종 사용자를 위한 Google 광고 서비스를 사용하기 위해 적절한 동의를 수집하고 있는지 확인하려면 법무팀에 Google의 새로운 EU 사용자 동의 정책에 대해 문의하세요. |
| Google 고객 일치 | [Google](https://support.google.com/google-ads/answer/6299717) |  모든 광고주가 고객 매치를 사용할 수 있는 것은 아닙니다.<br><br>**고객 일치를 사용하려면 계정에 다음 사항이 있어야 합니다.**<br>\- 정책 준수 이력<br>\- 양호한 결제 내역<br>\- Google Ads에서 90일 이상 기록<br>\- 평생 총 지출액 미화 50,000달러 이상. USD 이외의 통화로 계정을 관리하는 광고주의 경우, 지출 금액은 해당 통화의 월 평균 전환율을 사용하여 USD로 전환됩니다.<br><br>계정이 이러한 기준을 충족하지 않는 경우, 해당 계정은 현재 고객 일치를 사용할 수 없습니다.<br><br>계정의 고객 일치 사용 여부에 대한 자세한 안내는 Google Ads 담당자에게 문의하세요. |
| Google 동의 신호 | [Google](https://support.google.com/google-ads/answer/14310715) |  Google의 고객 일치 서비스를 사용하여 EEA 최종 사용자에게 광고를 게재하려면 Google의 EU 사용자 동의 정책의 일부로 다음 사용자 지정 속성(부울)을 Braze에 전달해야 합니다. 자세한 내용은 [EEA, 영국 및 스위스 최종 사용자에 대한 동의 수집에서](#collecting-consent-for-eea-uk-and-switzerland-end-users) 확인할 수 있습니다: <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze SDK를 사용하여 동의 신호를 수집하는 경우, 다음 최소 버전을 충족해야 합니다.

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### EEA, 영국 및 스위스 최종 사용자에 대한 동의 수집

Google의 EU 사용자 동의 정책에 따라 광고주는 EEA, 영국 및 스위스 최종 사용자에게 다음 사항을 공개하고 이에 대한 동의를 얻어야 합니다:

* 법적으로 필요한 경우 쿠키 또는 기타 로컬 저장소 사용.
* 개인 맞춤형 광고를 위해 개인 데이터를 수집, 공유 및 사용합니다.

이는 미국 최종 사용자 또는 EEA, 영국 또는 스위스 외부에 위치한 기타 최종 사용자에게는 영향을 미치지 않습니다. EEA, 영국 및 스위스 최종 사용자를 위한 Google 광고 서비스를 사용하기 위해 적절한 동의를 수집하고 있는지 확인하려면 법무팀에 Google의 새로운 EU 사용자 동의 정책에 대해 문의하세요.

2024년 3월 6일부터 시행되는 디지털 시장법(DMA) 요건에 따라 광고주는 Google과 데이터를 공유할 때 EEA, 영국 및 스위스 최종 사용자에 대한 동의를 받아야 합니다. 이 변경 사항의 일환으로, Braze에서 다음 부울 커스텀 속성으로 두 동의 신호를 모두 수집할 수 있습니다.

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze는 이러한 커스텀 속성의 데이터를 [Google의 적절한 동의 필드](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A)에 동기화합니다.

#### 취소된 동의 관리

EEA 최종사용자가 오디언스 목록에 추가되었다가 이후 두 가지 동의 중 하나(`$google_ad_user_data` 또는 `$google_ad_personalization`)를 철회한 경우 오디언스 목록을 최신 상태로 유지하려면 오디언스 동기화 단계를 사용하여 기존 오디언스 목록에서 사용자를 제거하도록 캔버스를 설정해야 합니다.

{% alert note %}
EEA가 이전에 두 가지 신호에 모두 동의한 경우, 해당 목록이 만료되거나 Google 오디언스 동기화를 통해 동의 상태가 명시적으로 업데이트될 때까지 또는 두 가지 모두에 해당할 때 해당 데이터는 Google의 고객 일치에 계속 사용됩니다.
{% endalert %}

#### 팁

* 값을 문자열 유형이 아닌 부울 유형으로 전송합니다.
* 속성 이름 앞에 달러 기호($)를 붙입니다. Braze는 속성 이름 시작 부분에 달러 기호를 사용하여 이 키가 특별하고 예약된 키임을 나타냅니다.
* Enter the attribute name in lowercase.
* 사용자를 명시적으로 지정되지 않은 사용자로 설정할 수는 없지만 `null` 또는 `nil` 값이나 `true` 또는 `false`가 아닌 값을 보내면 Braze는 이 사용자를 Google에 `UNSPECIFIED`로 전달합니다.
* 동의 속성을 지정하지 않고 추가하거나 업데이트한 신규 사용자는 해당 동의 속성이 지정되지 않음으로 표시된 상태로 Google에 동기화됩니다.

필수 동의 필드와 부여된 상태 없이 EEA 사용자와 동기화를 시도하면 Google은 이를 거부하고 해당 사용자에게 광고를 게재하지 않습니다. 또한 명시적인 동의 없이 EEA 사용자에게 광고를 게재하는 경우, 귀하는 법적 책임을 지게 되며 재정적 위험에 처할 수 있습니다. 이를 방지하려면 `true` Google 동의 속성이 있는 EEA, 영국 및 스위스 사용자만 포함하는 세그먼트 필터를 사용하여 캠페인을 전송하는 것이 좋습니다. 고객 매치 업로드 파트너에 대한 EU 사용자 동의 정책에 대한 자세한 내용은 Google의 [자주 묻는 질문을](https://support.google.com/google-ads/answer/14310715) 참조하세요.

### 캔버스 설정

Braze에 동기화하면 사용자 프로필과 세분화를 위해 다음과 같은 동의 속성을 사용할 수 있습니다:

- `$google_ad_user_data`
- `$google_ad_personalization`

Google 오디언스 동기화를 사용하여 사용자를 오디언스에 추가하기 위해 EEA, 영국 및 스위스 최종 사용자를 타겟팅하는 모든 캔버스에서 두 동의 속성이 모두 `true` 이 아닌 값일 때마다 이러한 사용자를 제외해야 합니다. 동의 값이 `true` 로 설정된 경우 이러한 사용자를 세분화하여 이를 달성할 수 있습니다. 또한 Google이 이러한 사용자를 잠재고객에서 제외한다는 것을 알고 있기 때문에 사용자에 대한 보다 정확한 분석이 동기화됩니다. Google 오디언스 동기화를 사용하여 사용자를 오디언스에서 제거하는 경우 동의 속성이 필요하지 않다는 점에 유의하세요.

## 통합

### 1단계: Google 계정 연결

시작하려면 **파트너 통합** > **기술 파트너** > **Google Ads**로 이동하여 **Google Ads 연결**을 선택합니다. You'll be prompted with a modal to select the email associated with your Google Ads account and then grant Braze access to your Google Ads account.

Once you have successfully connected your Google Ads account, you'll be taken back to your Google Ads partner page. You'll then be prompted to select which ad accounts you want to be accessed in the Braze workspace.

![A GIF that shows the workflow of a successful Google Ads account connection to Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Export iOS IDFA or Google Advertising IDs

If you plan to export iOS IDFA or Google Advertising IDs in your audience sync, Google requires your iOS app ID and Android app ID within the requests. Google 오디언스 동기화에서 **모바일 광고 ID 추가를** 선택하고 iOS 앱 ID와 Android 앱 ID(앱 패키지 이름)를 입력한 후 각각 저장합니다.

<br><br>
![연결된 광고 계정을 표시하는 업데이트된 Google 광고 기술 페이지에서 계정을 다시 동기화하고 모바일 광고 ID를 추가할 수 있습니다.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

If you have multiple apps in a single workspace, you can input any of your app IDs in the setup because mobile ad IDs for your users will be the same across multiple apps. This is because both the Android GAID and iOS IDFA are universal ad identifiers on the device and are not app-specific. To sync mobile ad IDs for users from a specific app, you can use segment filters ("Last Used Specific App" or Most Recent App Version") to target these users.

### 2단계: 캔버스 흐름에 Google 오디언스 단계 추가

Add a component in your Canvas, then select **Audience Sync**.

![The menu to select a Canvas component in the editor.][18]{: style="max-width:35%;"} ![The Audience Sync step added to the user journey.][20]{: style="max-width:28%;"}

### 3단계: 동기화 설정

1. Select **Custom Audience** to open the component editor.
2. Select **Google** as the Audience Sync partner.

![The Audience Sync step settings with the option to select a partner to start the sync.][19]{: style="max-width:80%;"}

{: start="3"}
3\. 원하는 Google 광고 계정을 선택합니다.
4\. In the **Choose a New or Existing Audience** dropdown, enter the name of a new or existing audience. 

{% tabs %}
{% tab 새로운 오디언스 만들기 %}

1. Enter a name for the new custom audience.
2. Select **Add Users to Audience**.
3. Select the first-party user field data to send to your audience. 둘 중 하나를 선택할 수 있습니다:

- **고객 연락처 정보**: Contains your users' email or phone numbers, or both if they exist in Braze. Google requires this to be a single field to sync instead of separate identifiers. You can still use this single field if you only have one of the identifiers.
- **모바일 광고주 ID**: Select either iOS IDFA or Android GAID. Due to Google’s Customer Match requirements, you can't have both mobile advertiser IDs in the same customer lists.

{: start="4"}
4\. Next, save your audience by selecting the **Create Audience** button at the bottom of the step editor.

![커스텀 오디언스 캔버스 구성요소의 확장된 보기. 여기에서 원하는 광고 계정이 선택되고 새 오디언스가 생성된 다음, '고객 연락처 정보' 확인란이 선택됩니다.]({% image_buster /assets/img/audience_sync/g_sync.png %})

대상 그룹이 성공적으로 생성되거나 이 과정에서 오류가 발생하면 단계 편집기 상단에 사용자에게 알림이 표시됩니다. 이 오디언스는 초안 모드에서 생성되었으므로 나중에 캔버스 여정에서 이 오디언스를 참조하여 사용자를 제거할 수 있습니다. 

![캔버스 구성요소에서 새 오디언스을 생성한 후에 표시되는 알림.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

When you launch a Canvas with a new audience, Braze will create a new custom audience upon launching the Canvas and subsequently sync users in near real-time as they enter the Google Audience step. 

{% alert important %}
Google의 고객 일치 요구 사항을 고려할 때 고객 연락처 정보와 모바일 광고주 ID를 동일한 고객 목록에 보유할 수 없습니다. 그러면 Google 고객 일치는 이 정보를 사용하여 Google 검색, Google 디스플레이, YouTube 및 Gmail 내에서 타겟팅할 수 있는 사용자를 결정합니다. Google 고객 일치 요구 사항에 대한 자세한 내용은 해당 [설명서](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507)를 참조하세요.
{% endalert %}
{% endtab %}
{% tab 기존 오디언스와 동기화 %}

또한 Braze는 기존 Google 고객 목록에서 사용자를 추가하거나 제거하여 이러한 오디언스가 최신 상태인지 확인하는 기능도 제공합니다. To sync with an existing audience:

1. Select an existing custom audience to sync.
2. Choose whether you want to **Add to the audience** or **Remove from the audience**.
3. Braze will add or remove users in near real-time as they enter the Google Audience step. 
4. After configuring your Google Audience step, select **Done**. Google 오디언스 단계에는 새 오디언스에 대한 세부 정보가 포함됩니다.

![커스텀 오디언스 캔버스 구성요소의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택되고 '오디언스에 사용자 추가' 라디오 버튼이 표시됩니다.]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### 4단계: 캔버스 실행

캔버스 내에서 나머지 사용자 여정을 완료한 다음, 시작하세요! 새 오디언스를 생성하기로 선택한 경우, Braze는 Google 내에서 오디언스를 생성한 다음, 캔버스에서 이 단계에 도달하면 사용자를 추가합니다. 기존 오디언스에서 사용자를 추가하거나 제거하도록 선택한 경우, Braze는 사용자 여정에서 이 단계에 도달하면 사용자를 추가하거나 제거합니다.

그런 다음, 사용자는 캔버스의 다음 구성요소가 있는 경우 해당 구성요소로 진행하거나 사용자 여정의 마지막 단계인 경우 캔버스를 종료합니다. 

## 사용자 동기화 및 속도 제한 고려 사항

사용자가 오디언스 동기화 구성 요소에 도달하면 Braze는 Google Ads API 속도 제한을 준수하면서 거의 실시간으로 해당 사용자를 동기화합니다. 즉, 실제로 Braze는 이러한 사용자를 Google로 보내기 전에 5초마다 최대한 많은 사용자를 배치 처리하려고 시도합니다. 

고객이 Google Ads API 사용량 제한에 도달하면 Google은 재시도 추천에 대한 피드백을 Braze에 다시 제공합니다. Braze 고객이 이 사용량 제한에 도달하면 Braze 캔버스는 최대 13시간 동안 동기화를 다시 시도합니다. 동기화가 불가능한 경우 이러한 사용자는 사용자 오류 측정기준 아래에 나열됩니다.

## 분석 이해 

다음 표에는 오디언스 동기화 단계의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| *진입함* | 이 단계에 들어간 사용자 중 Google에 동기화할 사용자 수. |
| *다음 단계로 진행됨* | 다음 구성 요소로 진급한 사용자 수(있는 경우). 모든 사용자가 자동 진행됩니다. 캔버스 브랜치의 마지막 단계인 경우 이 측정기준은 0이 됩니다. |
| *사용자가 동기화됨* | Google에 성공적으로 동기화된 사용자 수입니다. |
| *사용자가 동기화되지 않음* | 일치할 필드가 없거나 동의 속성이 누락되어 동기화되지 않은 사용자 수가 `false` 로 설정되었습니다. |
| *사용자에서 오류 발생* | 약 13시간 동안의 재시도 후 오류로 인해 Google에 동기화되지 않은 사용자 수. Google Ads API 서비스 중단과 같은 특정 오류의 경우, 캔버스는 최대 13시간 동안 동기화를 재시도합니다. 이 시점에서도 동기화가 되지 않으면 *사용자 동기화되지 않음* 메시지가 표시됩니다. |
| *사용자가 보류 중임* | 현재 Braze가 Google에 동기화하기 위해 처리 중인 사용자 수입니다. |
| *캔버스에서 나감* | 캔버스를 종료한 사용자 수입니다. 이는 캔버스의 마지막 단계가 Google 단계일 때 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### Why can I not select multiple fields to match in my Google Audience Step configuration?

Google 고객 일치에는 이러한 오디언스의 형식과 포함되는 고객 정보에 대한 엄격한 요구 사항이 있습니다. 특히 모바일 광고주 ID는 고객 연락처 정보(예: 이메일 및 전화번호)와 별도로 업로드해야 합니다. 자세한 내용은 [Google의 고객 일치 설명서](https://support.google.com/google-ads/answer/7659867?hl=en#undefined)를 참조하세요.

### How long will it take for my audiences to sync in Google?

오디언스가 Google에 동기화되는 데는 6~12시간이 소요될 수 있습니다. 

### I've synced an audience, so why is the audience size in Google zero?

For privacy purposes, the user list size will show zero until the list has at least 1,000 members. 그 이후에는 크기가 유효 두 자리로 반올림됩니다.

### I've synced an audience into Google, but my ads are not serving.

Check that your audiences contain at least 5,000 users so that ads can start serving.

### How do I resolve the "Mobile App IDs Deleted" error?

If you're syncing audiences to Google, this error will trigger if you have selected to sync mobile identifiers as part of your syncs but deleted your mobile app IDs from the Google partner page. To resolve this issue, make sure you've added the appropriate mobile app IDs for iOS and Android to the Google partner page.


[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/g_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/g_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/g_sync3.png %}
