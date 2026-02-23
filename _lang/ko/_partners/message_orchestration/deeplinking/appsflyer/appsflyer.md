---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "This reference article outlines the partnership between Braze and AppsFlyer, a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [앱스플라이어는](https://www.appsflyer.com/) 마케팅 분석, 모바일 어트리뷰션, 딥링킹을 통해 앱을 분석하고 최적화할 수 있도록 도와주는 모바일 마케팅 분석 및 어트리뷰션 플랫폼입니다.

The Braze and AppsFlyer integration allows you to better understand how to optimize and build more holistic campaigns by leveraging mobile install attribution data from AppsFlyer. 

You can also pass your AppsFlyer audiences (cohorts) directly to Braze with the [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/) integration, allowing you to create powerful customer engagement campaigns targeted toward just the right users at just the right time. 

## Prerequisites

| Requirement | Description |
|---|---|
| AppsFlyer account | An AppsFlyer account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| AppsFlyer SDK | In addition to the required Braze SDK, you must install the [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started).
| Email domain setup complete | You must have completed the [IP and domain setup step]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) of setting up your email during Braze onboarding. |
| SSL certificate | Your [SSL certificate]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) must be configured. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Map device ID

{% tabs local %}
{% tab Android %}
Android 앱이 있는 경우, 앱스플라이어에 고유한 Braze 기기 ID를 전달해야 합니다. 

다음 코드 줄이 올바른 위치에 삽입되었는지, 즉 Braze SDK가 실행된 후와 앱스플라이어 SDK의 초기화 코드 앞에 삽입되었는지 확인합니다. See the AppsFlyer [Android SDK integration guide](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) for more information.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
2023년 2월 이전에는 앱스플라이어 어트리뷰션 데이터 통합을 위해 IDFV(Identifier for Vendor)를 기본 식별자로 사용하여 iOS 어트리뷰션 데이터를 매칭했습니다. Objective-C를 사용하는 Braze 고객은 서비스 중단이 발생하지 않으므로 설치 시 Braze `device_id` 를 가져와서 앱스플라이어로 전송할 필요가 없습니다.
{% endalert%}

Swift SDK v5.7.0+를 사용하는 경우 IDFV를 상호 식별자로 계속 사용하려면 `useUUIDAsDeviceId` 필드가 `false` 으로 설정되어 있는지 확인하여 통합이 중단되지 않도록 해야 합니다. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to AppsFlyer upon app install in order for Braze to appropriately match iOS attributions.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
To map the device ID in Unity, use the following:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **AppsFlyer**. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in AppsFlyer's dashboard.<br><br>![AppsFlyer 기술 페이지에서 사용 가능한 '설치 경로에 대한 데이터 가져오기'. 이 상자에는 데이터 가져오기 키와 REST 엔드포인트가 포함되어 있습니다.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### 3단계: Configure Braze in AppsFlyer's dashboard

1. In AppsFlyer, navigate to the **Integrated Partners** page on the left bar. Next, search for **Braze** and select the Braze logo to open a configuration window.
2. Within the **Integration** tab, switch on **Activate Partner**.
3. Provide the data import key and REST endpoint that you found in the Braze dashboard. 
4. Toggle **Advanced Privacy** off and save your configuration.

Additional information on these instructions is available in [AppsFlyer's documentation](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Step 4: Confirm the integration

Braze가 앱스플라이어로부터 기여도 데이터를 수신하면, 앱스플라이어 기술 파트너 페이지의 연결 상태 표시기가 "연결되지 않음"에서 "연결됨"으로 변경되고 마지막 요청 성공의 타임스탬프가 포함됩니다.

이 상태는 Braze가 속성 설치에 대한 데이터를 수신한 후에만 변경됩니다. Braze는 오가닉 인스톨을 무시하며(Appsflyer 포스트백에서 제외), 연결 성공 여부를 판단할 때 이를 계산하지 않습니다.

### 5단계: Viewing user attribution data

#### Available data fields

데이터 통합에 성공하면 Braze는 모든 비오가닉 설치 데이터를 세그먼트 필터에 매핑합니다.

| AppsFlyer data field | Braze segment filter |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

설치 어트리뷰션 필터를 사용하여 Braze 대시보드에서 속성 데이터를 기준으로 사용자 기반을 세분화할 수 있습니다.

![Four available filters. 첫 번째는 "설치 어트리뷰션 소스는 network_val_0". 두 번째는 "설치 어트리뷰션 소스는 campaign_val_0". 세 번째는 "설치 어트리뷰션 소스는 adgroup_val_0". 네 번째는 "설치 어트리뷰션 소스는 creative_val_0". 나열된 필터 옆에서 이러한 어트리뷰션 소스가 고객 프로필에 어떻게 추가되는지 확인할 수 있습니다. 사용자 정보 페이지의 '설치 경로' 상자에 설치 소스는 network_val_0, 캠페인은 campaign_val_0, 등으로 표시됩니다.]({% image_buster /assets/img/braze_attribution.png %})

Additionally, attribution data for a particular user is available on each user's profile in the Braze dashboard.

{% alert note %}
Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. 이러한 미디어 소스는 파트너가 서드파티와 기여도 데이터를 공유하는 것을 허용하지 않으므로, 파트너는 해당 데이터를 Braze로 전송할 수 없습니다.
{% endalert %}

## 딥링킹을 위한 앱스플라이어와 Braze의 통합

Deep links—links that direct users toward a specific page or place within an app or website—are used to create a tailored user experience. 

널리 사용되고 있지만, 사용자 데이터 수집에 사용되는 또 다른 중요한 기능인 클릭 추적#8212과 함께 이메일 딥링크를 사용할 때 문제가 발생할 수 있습니다. 이러한 문제는 이메일 서비스 공급자(ESP)가 클릭 기록 도메인에 딥링크를 래핑하여 원래 링크를 끊어버리기 때문에 발생합니다. As such, supporting deep links requires additional setup.

앱스플라이어는 이러한 문제를 방지하는 [서비스를](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) 제공하여 이메일 서비스 공급업체 서버와 도메인 이름 사이에서 앱스플라이어가 중개자 역할을 할 수 있도록 합니다.  프록시 역할은 딥링킹을 용이하게 하는 연결 파일(AASA/자산 링크)의 제공을 인에이블먼트합니다. 

## 1단계 - 클릭 추적 도메인 만들기 

[Braze의 이메일 설정 안내의]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) 초기 요소에 따라 이메일 전송 도메인과 클릭 추적 도메인을 만듭니다. 지원을 받으려면 Braze 대시보드를 통해 티켓을 제기하여 Braze 이메일 팀과 함께 새 CTD에 대한 설정을 시작할 수 있습니다.

![오른쪽 상단의 "지원" 버튼 아래에 있는 "도움말 받기" 버튼이 표시된 Braze UI]({% image_buster /assets/img/attribution/appsflyer/1.png %})

이미 기존 CTD를 사용 중이더라도 새 CTD를 생성해야 합니다. 이렇게 하면 현재 진행 중인 라이브 이메일 캠페인의 트래픽에 영향을 미치지 않습니다. 

{% alert important%}
앱스플라이어가 SSL 인증서를 생성합니다. 이 단계에서는 이메일 링크가 보안되지 않았을 가능성이 높으며, 이는 URL 접두사가 HTTPS가 아닌 HTTP라는 의미입니다. 이 문제는 이후 단계에서 해결됩니다.	
{%endalert%}

## 2단계 - 앱스플라이어에서 원링크 템플릿 만들기
[원링크 템플릿을](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) 생성하고 '앱 설치 시'에서 유니버설 링크/앱 링크를 구성합니다. 이 템플릿은 나중에 이메일 캠페인용 원링크 링크를 만드는 데 사용됩니다.

{% alert note%} 유니버설 링크/앱 링크를 인에이블먼트하는 기존 원링크 템플릿이 이미 구성되어 있는 경우 이를 사용할 수 있습니다.
{%endalert%}

## 3단계 - 앱스플라이어에서 Braze 통합 설정하기
이제 앱스플라이어에서 Braze 통합을 설정할 차례입니다. 이 단계와 다음 단계('앱 구성')를 동시에 설정할 수 있습니다.
앱스플라이어에서 Braze 통합을 설정하려면:

### 1\. 앱스플라이어의 사이드 메뉴에서 참여 > 이메일 서비스 공급자 통합을 선택합니다.
![왼쪽 메뉴에 있는 "이메일 서비스 공급자 통합" 버튼이 표시된 앱스플라이어 UI]({% image_buster /assets/img/attribution/appsflyer/2.png %})

 
### 2\. Braze를 선택합니다.
![Braze를 포함한 이메일 서비스 공급자 통합 목록이 표시된 앱스플라이어 UI.]({% image_buster /assets/img/attribution/appsflyer/3.png %})

 
### 3\. 이메일 캠페인에 사용할 원링크 템플릿을 선택한 후 다음을 클릭합니다.
![사용자가 템플릿을 선택할 수 있는 드롭다운이 표시된 앱스플라이어 UI.]({% image_buster /assets/img/attribution/appsflyer/4.png %})

 
### 4\. 클릭 추적 도메인과 1단계에서 생성한 새 CTD와 함께 제공된 "Braze 엔드포인트" 값을 입력한 다음 연결 유효성 검사를 클릭합니다.

이렇게 하면 클릭 추적 도메인이 입력한 엔드포인트를 가리키는지 확인합니다.

![고객이 클릭 추적 도메인과 관련 세부 정보를 추가해야 하는 위치를 강조 표시한 앱스플라이어 UI.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

앱스플라이어는 "Braze 엔드포인트"를 통해 이 가이드의 1단계에서 제공한 세부 정보, 특히 새로운 CTD를 요청하고 있습니다. 

그런 다음 **연결 유효성** 검사를 클릭하여 클릭 추적 도메인이 입력한 엔드포인트를 가리키는지 확인합니다.
완료했으면 **다음을** 클릭합니다.

### 5\. 링크 트래픽을 앱스플라이어로 라우팅합니다:

#### a. 앱스플라이어에서 미리 제작된 커스텀 지침을 복사하여 IT 또는 도메인 관리자에게 전송하세요. 

관리자는 앱스플라이어가 제공한 새 도메인으로 DNS CNAME 레코드를 업데이트하여 이메일 서비스 공급자 서버에서 앱스플라이어 서버로 이메일 캠페인 트래픽을 리라우팅해야 합니다.

그 결과, 링크를 클릭할 때마다 클릭이 앱스플라이어로 리디렉션되고, 앱스플라이어는 다시 이메일 서비스 공급업체 엔드포인트로 리디렉션합니다.

![도메인에서 앱스플라이어, 이메일 서비스 공급업체 엔드포인트까지 클릭 데이터가 전달되는 과정을 보여주는 다이어그램]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. 지침을 복사하여 전송한 후 완료를 클릭합니다.
Braze 통합이 완료되었습니다.

{%alert important%}
Braze 통합 상태는 보류 중이며 CNAME 레코드가 매핑된 후에만 작동을 시작합니다. 매핑 후 새 통합이 작동을 시작하고 활성화되려면 최대 24시간이 걸릴 수 있습니다.
{%endalert%}

## 4단계: 앱 구성(개발자 작업)
앱스플라이어는 유니버설 연동을 지원하기 위해 웹 또는 앱 팀이 따라야 하는 올바른 앱 구성에 대한 [지침을 제공합니다](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task). 

## 5단계: Braze로 SSL 클릭 추적 인에이블먼트 확인

이 단계에서는 앱스플라이어에서 CTD 세부 정보를 공유하고 유효성을 검사한 후 테스트 전송을 수행하여 원링크 전송 도메인에 SSL 인증서가 있는지 확인하는 것이 좋습니다. 이는 [이메일 설정](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) 가이드와 일치합니다.

원링크를 사용하여 딥링크를 전송하여 품질 보증 및 문제 해결을 수행할 수 있습니다. See the [AppsFlyer documentation](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) for details on using OneLink.

CTD 링크가 HTTP로 식별되는 경우 Braze의 이메일 운영팀에 문의하여 SSL 클릭 추적을 인에이블먼트하세요. 이렇게 하면 모든 HTTP 링크가 자동으로 HTTPS로 변환됩니다.
고객 성공 매니저에게 연락할 때 다음 샘플 메시지 텍스트를 사용하거나 1단계에서와 같이 Braze 대시보드에 다시 티켓을 올리면 됩니다: 

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 
```

### AppsFlyer click tracking URLs in Braze (optional)

You can use AppsFlyer's [OneLink attribution links](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) in Braze campaigns across push, email, and more. 이를 통해 Braze 캠페인의 설치 또는 재참여 기여도 데이터를 앱스플라이어로 다시 전송할 수 있습니다. 결과적으로 마케팅 활동을 보다 효과적으로 측정하고 데이터 중심 의사 결정을 내릴 수 있습니다.

You can simply create your OneLink tracking URL in AppsFlyer and directly insert it into your Braze campaigns. 그런 다음 앱스플라이어는 [확률적 어트리뷰션 방법론을](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) 사용하여 링크를 클릭한 사용자의 기여도를 측정합니다. We recommend appending your AppsFlyer tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. 이는 링크를 클릭한 사용자에게 결정적인 속성을 부여합니다.

{% tabs local %}
{% tab Android %}
Android의 경우, Braze를 통해 고객은 [Google 광고 ID 수집(GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)을 옵트인할 수 있습니다. 앱스플라이어 SDK 통합은 GAID도 수집합니다. 다음 Liquid 로직을 사용하여 앱스플라이어 클릭 추적 링크에 GAID를 포함시킬 수 있습니다:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and AppsFlyer automatically collect the IDFV natively through our SDK integrations. IDFC를 기기 식별자로 사용할 수 있습니다. 다음 Liquid 로직을 사용하여 앱스플라이어 클릭 추적 링크에 IDFV를 포함시킬 수 있습니다:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}
