---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "이 참조 문서에서는 앱을 분석하고 최적화하는 데 도움을 주는 모바일 마케팅 분석 및 기여도 플랫폼인 AppsFlyer와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer는 모바일 마케팅 분석 및 기여도 분석 플랫폼입니다. 마케팅 분석과 모바일 기여도 분석 및 딥링킹을 통해 앱 분석과 최적화가 가능합니다.

Braze와 AppsFlyer의 통합을 통해 AppsFlyer의 모바일 설치 경로 데이터를 활용하여 보다 총체적인 캠페인을 최적화하고 빌드하는 방법을 더 잘 이해할 수 있습니다. 

또한 [AppsFlyer 오디언스]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/appsflyer_audiences/) 통합을 통해 AppsFlyer 오디언스(코호트)를 Braze에 직접 전달하여 적시에 올바른 사용자를 타겟팅하는 강력한 고객 참여 캠페인을 생성할 수 있습니다. 

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Appsflyer 계정 | 이 파트너십을 활용하려면 Appsflyer 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요구 사항의 세부 정보는 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| AppsFlyer SDK | 필수 Braze SDK 외에도 [Appsflyer SDK](https://dev.appsflyer.com/hc/docs/getting-started)를 설치해야 합니다.
| 이메일 도메인 설정 완료 | Braze 온보딩 중에 이메일 설정의 [IP 및 도메인 설정 단계]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)를 완료해야 합니다. |
| SSL 인증서 | [SSL 인증서를]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) 구성해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 기기 ID 매핑

{% tabs local %}
{% tab Android %}
Android 앱이 있는 경우, 고유한 Braze 기기 ID를 Appsflyer에 전달해야 합니다. 

다음 코드 줄이 올바른 위치에 삽입되었는지(Braze SDK가 실행된 후와 AppsFlyer SDK의 초기화 코드 앞) 확인합니다. 자세한 내용은 AppsFlyer [Android SDK 통합 가이드](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)를 참조하세요.

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
2023년 2월 이전에, Appsflyer 기여도 통합은 iOS 기여도 데이터를 일치시키기 위해 IDFV를 기본 식별자로 사용했습니다. Objective-C를 사용하는 Braze 고객은 서비스 중단이 발생하지 않으므로 설치 시 Braze `device_id`를 가져와 Appsflyer로 전송할 필요가 없습니다.
{% endalert%}

Swift SDK v5.7.0 이상을 사용하는 경우 IDFV를 상호 식별자로 계속 사용하려면 `useUUIDAsDeviceId` 필드를 `false`로 설정하여 통합이 중단되지 않도록 해야 합니다. 

`true`로 설정한 경우, 앱 설치 시 Braze `device_id`를 Appsflyer로 전달하여 Braze가 iOS 기여도와 적절히 일치하도록 Swift용 iOS 기기 ID 매핑을 구현해야 합니다.

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

{% tab 유니티 %}
Unity에서 기기 ID를 매핑하려면 다음을 사용하십시오:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### 2단계: Braze 데이터 가져오기 키 가져오기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Appsflyer**를 선택합니다. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Appsflyer의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.<br><br>![AppsFlyer 기술 페이지에서 사용 가능한 '설치 경로에 대한 데이터 가져오기'. 이 상자에는 데이터 가져오기 키와 REST 엔드포인트가 포함되어 있습니다.][4]{: style="max-width:70%;"}

### 3단계: AppsFlyer 대시보드에서 Braze 구성

1. AppsFlyer의 왼쪽 표시줄에서 **통합 파트너** 페이지로 이동합니다. Next, search for **Braze** and select the Braze logo to open a configuration window.
2. **연동** 탭에서 **파트너 활성화를 켭니다**.
3. Provide the data import key and REST endpoint that you found in the Braze dashboard. 
4. **고급 개인정보 보호를** 끄고 구성을 저장합니다.

이 지침에 대한 추가 정보는 [AppsFlyer 설명서][16]에서 확인할 수 있습니다.

### 4단계: 통합 확인

Braze가 Appsflyer로부터 기여도 데이터를 수신하면 Braze의 Appsflyer 기술 파트너 페이지에서 연결 상태 표시기가 '연결되지 않음'에서 '연결됨'으로 변경됩니다. 마지막으로 성공한 요청의 타임스탬프도 포함됩니다. 

기여도 설치에 대한 데이터가 수신될 때까지는 이 작업이 수행되지 않습니다. Appsflyer 포스트백에서 제외되어야 하는 유기적 설치는 API에서 무시되며, 연결이 성공적으로 설정되었는지 확인할 때 계산되지 않습니다.

### 5단계: 사용자 어트리뷰션 데이터 보기

#### 사용 가능한 데이터 필드

제안된 대로 통합을 구성하면, Braze는 비유기적 설치 데이터를 세그먼트 필터에 매핑합니다.

| AppsFlyer 데이터 필드 | 브레이즈 세그먼트 필터 |
| -------------------- | --------------------- |
| `media_source` | 기여도 소스 |
| `campaign` | 기여도 캠페인 |
| `af_adset` | 기여도 광고 그룹 |
| `af_ad` | 기여도 광고 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze 대시보드에서 설치 경로 필터를 사용하여 사용자 기반을 기여도 데이터로 세분화할 수 있습니다.

![사용 가능한 네 가지 필터. 첫 번째는 "설치 어트리뷰션 소스는 network_val_0입니다."입니다. 두 번째는 "설치 어트리뷰션 소스는 캠페인_val_0입니다."입니다. 세 번째는 "설치 어트리뷰션 소스는 adgroup_val_0입니다."입니다. 네 번째는 "설치 어트리뷰션 소스는 creative_val_0입니다."입니다. 나열된 필터 옆에서 이러한 기여도 소스가 고객 프로필에 어떻게 추가되는지 확인할 수 있습니다. 사용자 정보 페이지의 '설치 경로' 상자에서 설치 소스는 network_val_0으로, 캠페인은 campaign_val_0 등으로 표시됩니다.][2]

또한 특정 사용자에 대한 기여도 데이터는 Braze 대시보드의 각 고객 프로필에서 확인할 수 있습니다.

{% alert note %}
Facebook 및 X(구 트위터) 캠페인의 어트리뷰션 데이터는 파트너를 통해 제공되지 않습니다. 이러한 미디어 소스는 파트너가 서드파티와 기여도 데이터 공유를 허용하지 않으므로 파트너는 해당 데이터를 Braze로 전송할 수 없습니다.
{% endalert %}

## 딥링킹을 위한 이메일 서비스 공급자와 AppsFlyer 통합

AppsFlyer는 이메일 서비스 제공업체(ESP)로 SendGrid 및 SparkPost와 통합하여 딥링킹 및 클릭 추적을 지원합니다. 아래 지침에 따라 원하는 ESP와 통합하세요.

{% alert tip %}
딥링크(앱이나 웹사이트 내의 특정 페이지나 장소로 사용자를 안내하는 링크)는 맞춤형 사용자 환경을 만드는 데 사용됩니다. 널리 사용되지만, 사용자 데이터 수집에 사용되는 또 다른 중요한 기능인 클릭 추적과 함께 이메일로 전달되는 딥링크를 사용할 때 문제가 발생할 수 있습니다. 이러한 문제는 ESP가 클릭 기록 도메인에 딥링크를 래핑하여 원본 링크를 끊기 때문에 발생합니다. 따라서 딥링크를 지원하려면 추가 설정이 필요합니다. AppsFlyer를 SendGrid 또는 SparkPost와 통합하면 이러한 문제를 방지할 수 있습니다. [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)에서 이 주제에 대해 자세히 알아보세요.
{% endalert %}

### 1단계: AppsFlyer에서 OneLink 설정

1. AppsFlyer에서 이메일 캠페인에 대한 OneLink 템플릿을 선택합니다. 템플릿이 유니버설 링크(iOS) 또는 앱 링크(Android)를 지원하는지 확인합니다. 
2. OneLink로 딥링킹을 지원하도록 앱을 구성합니다. OneLink를 원하도록 앱을 구성하는 방법에 대한 자세한 내용은 [AppsFlyer 설명서](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup)를 참조하세요.

### 2단계: 유니버설 링크 및 앱 링크를 지원하도록 앱을 구성하세요.

유니버설 링크(iOS) 또는 앱 링크(Android)를 사용하면 디바이스의 운영 체제에서 클릭 시 지정된 앱을 열 수 있습니다.

유니버설 링크 및 앱 링크를 지원하려면 다음 단계를 수행하세요.

{% tabs 로컬 %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
이메일에서 유니버설 링크를 활성화하도록 Apple App Site Association(AASA) 파일 호스팅을 설정합니다.

1. 다음 방법 중 하나로 AASA 파일을 받습니다:
    * 유니버설 링크가 있는 OneLink를 설정했다면 이미 OneLink와 연결된 AASA 파일이 있을 수 있습니다. AASA 파일을 얻으려면 다음을 수행합니다:
        * OneLink 템플릿의 OneLink 하위 도메인을 복사합니다. 템플릿이 유니버설 링크를 지원하는지 확인하세요.
        * 다음 URL에 자리 표시자 대신 붙여넣기합니다: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * AASA 파일을 다운로드하려면 브라우저의 주소창에 원링크 URL을 붙여넣고 **Enter** 키를 누릅니다. 그러면 파일이 컴퓨터에 다운로드되며 텍스트 편집기를 사용하여 파일을 열고 내용을 볼 수 있습니다.
    * [Apple의 유니버설 링크에 대한 가이드에서](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) AASA 파일을 만드는 방법을 설명합니다.
2. 클릭 기록 도메인 서버에서 AASA 파일을 호스팅합니다. 파일은 `click.example.com/.well-known/apple-app-site-association` 경로에 호스팅되어야 합니다. 

SendGrid용 AASA 파일을 구성하고 AASA 파일을 호스팅하도록 CDN 서비스를 설정하는 방법은 [SendGrid 설명서](https://docs.sendgrid.com/ui/sending-email/universal-links)를 참조하세요.

{% alert important %}
AASA 파일이 호스팅된 후 OneLink 구성을 변경(수정 또는 대체)할 때마다 새 AASA 파일을 생성해야 합니다.
{% endalert %}
{% endsubtab %}
{% subtab Android %}
Digital Asset Links 파일 호스팅을 설정하여 이메일에서 앱 링크를 활성화합니다.

1. 다음 방법 중 하나로 Digital Asset Links 파일을 가져옵니다.
    * 앱 링크와 함께 OneLink를 설정했다면 이미 OneLink와 연결된 디지털 자산 링크 파일이 있을 수 있습니다. 파일을 가져오려면 다음을 수행합니다:
        * OneLink 템플릿의 OneLink 하위 도메인을 복사합니다. 템플릿이 앱 링크를 지원하는지 확인합니다.
        * 원링크 URL 끝에 `/.well-known/assetlinks.json`을 추가합니다.
        * 디지털 자산 링크 파일을 다운로드하려면 브라우저의 주소창에 원링크 URL을 붙여넣고 **Enter** 키를 누릅니다. 예: `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. 그러면 파일이 컴퓨터에 다운로드되며 텍스트 편집기를 사용하여 파일을 열고 내용을 볼 수 있습니다.
    * [Android의 앱 링크 가이드](https://developer.android.com/studio/write/app-link-indexing)에서는 Digital Asset Links 파일을 생성하는 방법을 설명합니다.
2. 클릭 기록 도메인 서버에 Digital Asset Links 파일을 호스팅합니다. 파일은 `click.example.com/.well-known/apple-app-site-association` 경로에 호스팅되어야 합니다.

SendGrid용 Digital Asset Links 파일을 구성하고 Digital Asset Links 파일을 호스팅하도록 CDN 서비스를 설정하는 방법은 [SendGrid 설명서](https://docs.sendgrid.com/ui/sending-email/universal-links)를 참조하세요.

{% alert important %}
Digital Asset Links 파일이 호스팅된 후 OneLink 구성을 변경(수정 또는 대체)할 때마다 새 파일을 생성해야 합니다.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### 2a단계: AASA 파일 호스팅 설정
이메일에서 유니버설 링크를 활성화하도록 Apple App Site Association(AASA) 파일 호스팅을 설정합니다.

1. 다음 방법 중 하나로 AASA 파일을 받습니다:
    * 유니버설 링크가 있는 OneLink를 설정했다면 이미 OneLink와 연결된 AASA 파일이 있을 수 있습니다. AASA 파일을 얻으려면 다음을 수행합니다:
        * OneLink 템플릿의 OneLink 하위 도메인을 복사합니다. 템플릿이 유니버설 링크를 지원하는지 확인하세요.
        * 다음 URL에 자리 표시자 대신 붙여넣기합니다: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * AASA 파일을 다운로드하려면 브라우저의 주소창에 원링크 URL을 붙여넣고 **Enter** 키를 누릅니다. 그러면 파일이 컴퓨터에 다운로드되며 텍스트 편집기를 사용하여 파일을 열고 내용을 볼 수 있습니다.
    * [Apple의 유니버설 링크에 대한 가이드에서](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) AASA 파일을 만드는 방법을 설명합니다.
2. 클릭 기록 도메인 서버에서 AASA 파일을 호스팅합니다. 파일은 `click.example.com/.well-known/apple-app-site-association` 경로에 호스팅되어야 합니다. 

SparkPost용 AASA 파일을 구성하고 커스텀 링크 하위 경로를 설정하는 방법은 [SparkPost 설명서](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)를 참조하세요.

{% alert important %}
AASA 파일이 호스팅된 후 OneLink 구성을 변경(수정 또는 대체)할 때마다 새 AASA 파일을 생성해야 합니다.
{% endalert %}

#### 2b단계: 클릭 추적 도메인을 AASA 파일 호스트로 리디렉션합니다.
[이메일을 구성하는]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) 동안 DNS 서버에 CNAME 레코드를 만들었습니다. Braze에서 클릭 추적 도메인을 확인한 후 다음 단계를 수행합니다. 

1. 하위 도메인을 SparkPost 도메인으로 리디렉션하는 CNAME 레코드를 삭제합니다.
2. 위에서 삭제한 레코드 대신 클릭 추적 도메인을 앱 AASA 파일을 호스팅하는 CDN으로 리디렉션하는 CNAME 레코드를 생성합니다.
{% endsubtab %}
{% subtab Android %}
#### 2a단계: 디지털 자산 링크 파일 호스팅 설정
Digital Asset Links 파일 호스팅을 설정하여 이메일에서 앱 링크를 활성화합니다.

1. 다음 방법 중 하나로 Digital Asset Links 파일을 가져옵니다.
    * 앱 링크와 함께 OneLink를 설정했다면 이미 OneLink와 연결된 디지털 자산 링크 파일이 있을 수 있습니다. 파일을 가져오려면 다음을 수행합니다:
        * OneLink 템플릿의 OneLink 하위 도메인을 복사합니다. 템플릿이 앱 링크를 지원하는지 확인합니다.
        * 원링크 URL 끝에 `/.well-known/assetlinks.json`을 추가합니다.
        * 디지털 자산 링크 파일을 다운로드하려면 브라우저의 주소창에 원링크 URL을 붙여넣고 **Enter** 키를 누릅니다. 예: `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. 그러면 파일이 컴퓨터에 다운로드되며 텍스트 편집기를 사용하여 파일을 열고 내용을 볼 수 있습니다.
    * [Android의 앱 링크 가이드](https://developer.android.com/studio/write/app-link-indexing)에서는 Digital Asset Links 파일을 생성하는 방법을 설명합니다.
2. 클릭 기록 도메인 서버에 Digital Asset Links 파일을 호스팅합니다. 파일은 `click.example.com/.well-known/apple-app-site-association` 경로에 호스팅되어야 합니다.

SparkPost용 디지털 자산 링크 파일을 구성하고 사용자 지정 링크 하위 경로를 설정하는 방법을 알아보려면 [SparkPost 설명서를](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) 참조하세요.

{% alert important %}
Digital Asset Links 파일이 호스팅된 후 OneLink 구성을 변경(수정 또는 대체)할 때마다 새 파일을 생성해야 합니다.
{% endalert %}

#### 2b단계: 클릭 추적 도메인을 디지털 자산 링크 파일 호스트로 리디렉션하세요.
[이메일을 구성하는]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) 동안 DNS 서버에 CNAME 레코드를 만들었습니다. Braze에서 클릭 추적 도메인을 확인한 후 다음 단계를 수행합니다. 

1. 하위 도메인을 SparkPost 도메인으로 리디렉션하는 CNAME 레코드를 삭제합니다.
2. 위에서 삭제한 레코드 대신 클릭 추적 도메인을 앱 디지털 자산 링크 파일을 호스팅하는 CDN으로 리디렉션하는 CNAME 레코드를 생성합니다.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 3단계: 딥링킹을 지원하도록 AppsFlyer SDK 구성

{% tabs 로컬 %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### 3a단계: AASA 파일을 지원하도록 SDK를 구성하세요.
클릭 기록 도메인에서 AASA 파일을 호스팅한 후, AASA 파일을 지원하도록 AppsFlyer SDK를 구성합니다.

1. Xcode에서 프로젝트를 선택합니다.
2. **기능**을 선택합니다.
3. **연결된 도메인**을 켭니다.
4. **+**를 클릭하고 클릭 도메인을 입력합니다. 예: `applinks:click.example.com`.
유니버설 링크를 클릭하면 앱이 열리고 SDK가 시작됩니다. 앱에서 클릭 도메인 뒤에 있는 OneLink를 추출하고 딥링크를 확인하도록 설정하려면 다음을 수행합니다.

#### 3b단계: 딥링크 데이터 처리
1. 클릭 기록 도메인을 SDK API에 제공하십시오. [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). 이 API는 SDK를 초기화하기 전에 호출해야 합니다. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API를 사용하여 딥링크 파라미터를 가져오고 딥링크 데이터를 처리합니다.

{% endsubtab %}
{% subtab Android %}
#### 3a단계: Digital Asset Links 파일을 지원하도록 SDK 구성

이전 단계에서 클릭 기록 도메인에 Digital Asset Links 파일을 호스팅한 후, 파일을 지원하도록 SDK를 구성합니다.

Android 매니페스트에서 딥링킹하려는 활동의 활동 태그에 클릭 도메인 호스트 및 접두사를 추가합니다.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### 3b단계: 딥링크 데이터 처리
앱 링크를 클릭하면 앱이 열리고 SDK가 시작됩니다.  앱에서 클릭 도메인 뒤에 있는 OneLink를 추출하고 딥링크를 확인하도록 설정하려면 SDK 메서드 [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls)에서 클릭 도메인을 나열합니다. 이 프로퍼티는 SDK를 초기화하기 전에 설정해야 합니다. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### 3a단계: AASA 파일을 지원하도록 SDK를 구성하세요.
클릭 기록 도메인에서 AASA 파일을 호스팅한 후, AASA 파일을 지원하도록 SDK를 구성합니다.

1. Xcode에서 프로젝트를 선택합니다.
2. **기능**을 선택합니다.
3. **연결된 도메인**을 켭니다.
4. **+**를 클릭하고 클릭 도메인을 입력합니다. 예: `applinks:click.example.com`.

#### 3b단계: 딥링크 데이터 처리
유니버설 링크를 클릭하면 앱이 열리고 SDK가 시작됩니다. SDK에서 클릭 도메인 뒤에 있는 OneLink를 추출할 수 있도록 하려면 다음을 수행합니다.
1. SDK 속성정보 [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls)에서 클릭 도메인을 나열합니다. SDK를 초기화하기 전에 이 프로퍼티를 설정해야 합니다.
2. 목록 <em>spgo.io</em> 가 나열된 도메인 중 하나인지 확인합니다. SparkPost는 이 도메인을 소유하고 있으며, 이는 리디렉션 흐름의 일부입니다. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API를 사용하여 딥링크 파라미터를 가져오고 딥링크 데이터를 처리합니다.
{% endsubtab %}
{% subtab Android %}
#### 3a단계: Digital Asset Links 파일을 지원하도록 SDK 구성

이전 단계에서 클릭 기록 도메인에 Digital Asset Links 파일을 호스팅한 후, 파일을 지원하도록 SDK를 구성합니다.

Android 매니페스트에서 딥링킹하려는 활동의 활동 태그에 클릭 도메인 호스트 및 접두사를 추가합니다.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### 3b단계: 앱 링크 데이터 처리
앱 링크를 클릭하면 앱이 열리고 SDK가 시작됩니다. 앱에서 클릭 도메인 뒤에 있는 OneLink를 추출하고 딥링크를 확인하도록 설정하려면 다음을 수행합니다.

1. SDK 메서드 [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls)에서 클릭 도메인을 나열합니다. 이 프로퍼티는 SDK를 초기화하기 전에 설정해야 합니다.
2. 목록 *spgo.io* 가 나열된 도메인 중 하나인지 확인합니다. SparkPost는 이 도메인을 소유하고 있으며, 이는 리디렉션 흐름의 일부입니다. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

통합 단계를 완료한 후에는 OneLink를 사용해 딥링크를 전송하여 품질 보증 및 문제 해결을 수행할 수 있습니다. OneLink 사용에 대한 자세한 내용은 [AppsFlyer 설명서](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)를 참조하세요.

### Braze의 AppsFlyer 클릭 추적 URL(선택 사항)

AppsFlyer의 [OneLink 기여도 링크](https://support.AppsFlyer.com/hc/en-us/articles/360001294118)를 푸시, 이메일 등에 걸쳐 Braze 캠페인에 사용할 수 있습니다. 이를 통해 Braze 캠페인의 설치 또는 재참여 기여도 데이터를 AppsFlyer로 다시 전송할 수 있습니다. 그 결과, 마케팅 활동을 보다 효과적으로 측정하고 데이터 중심의 의사 결정을 내릴 수 있습니다.

AppsFlyer에서 OneLink 추적 URL을 생성하여 Braze 캠페인에 바로 삽입할 수 있습니다. 그런 다음, Appsflyer는 [확률적 기여도 방법론](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)을 사용하여 링크를 클릭한 사용자의 기여도를 측정합니다. Braze 캠페인에서 기여도의 정확성을 개선하기 위해 Appsflyer 추적 링크에 기기 식별자를 추가하는 것이 좋습니다. 이렇게 하면 링크를 클릭한 사용자에게 결정론적으로 어트리뷰션이 부여됩니다.

{% tabs local %}
{% tab Android %}
Android의 경우 Braze를 사용하면 고객이 [Google 광고 ID 수집(GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)에 옵트인할 수 있습니다. GAID도 Appsflyer SDK 통합을 통해 기본적으로 수집됩니다. 다음 Liquid 로직을 활용하여 Appsflyer 클릭 추적 링크에 GAID를 포함할 수 있습니다.
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOS의 경우, Braze와 Appsflyer 모두 SDK 통합을 통해 기본적으로 IDFV를 자동으로 수집합니다. 디바이스 식별자로 사용할 수 있습니다. 다음 Liquid 로직을 활용하여 Appsflyer 클릭 추적 링크에 IDFV를 포함할 수 있습니다.

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



[1]: {% image_buster /assets/img/braze_integration.png %}
[2]: {% image_buster /assets/img/braze_attribution.png %}
[3]:https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]:https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}
