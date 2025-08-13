---
nav_title: 유니버설 링크 및 앱 링크
article_title: 유니버설 링크 및 앱 링크
page_order: 6.4
page_type: reference
description: "이 도움말에서는 Apple 유니버설 링크 및 Android 앱 링크 설정 방법을 안내합니다."
channel: email
---

# 유니버설 링크 및 앱 링크

Apple 유니버설 링크와 Android 앱 링크는 웹 콘텐츠와 모바일 앱 간의 원활한 전환을 제공하기 위해 고안된 메커니즘입니다. 보편적 링크는 iOS에만 해당되지만, Android 앱 링크는 Android 애플리케이션에 동일한 목적을 제공합니다.

## 유니버설 링크 및 앱 링크의 작동 방식

유니버설 링크(iOS) 및 앱 링크(Android)는 웹 페이지와 앱 내의 콘텐츠를 모두 가리키는 표준 웹 링크(`http://mydomain.com`)입니다.

유니버셜 링크 또는 앱 링크가 열리면 운영 체제가 설치된 앱이 해당 도메인에 등록되어 있는지 확인합니다. 앱이 발견되면 웹 페이지를 로드하지 않고 즉시 실행됩니다. 앱이 발견되지 않으면 사용자의 기본 웹 브라우저에서 웹 URL이 로드되며, 이는 각각 App Store 또는 Google Play Store로 리디렉션되도록 구성될 수도 있습니다.

명백히, 유니버설 링크는 웹사이트가 특정 앱 화면과 웹 페이지를 연결할 수 있게 하여 사용자가 앱 화면에 해당하는 웹 페이지 링크를 클릭하면 앱이 직접 열리도록 합니다 (앱이 현재 설치되어 있는 경우).

이 표는 유니버설 링크와 전통적인 딥 링크 간의 주요 차이점을 설명합니다:

|                        | 유니버설 링크 및 앱 링크                                  | 딥링크                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| 플랫폼 호환성 | iOS (버전 9 이상) 및 Android (버전 6.0 이상)  | 다양한 모바일 운영 체제에서 사용    |
| 목적                | iOS 및 Android 기기에서 웹 및 앱 콘텐츠를 원활하게 연결 | 특정 앱 콘텐츠로 연결 |
| 기능               | 문맥에 따라 웹 페이지 또는 앱 콘텐츠로 이동합니다           | 특정 앱 화면을 엽니다   |
| 앱 설치       | 앱이 설치되어 있으면 앱을 열고, 그렇지 않으면 웹 콘텐츠를 엽니다 | 앱 설치가 필요합니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용 사례

유니버설 링크와 앱 링크는 이메일 캠페인에 가장 많이 사용됩니다. 이메일은 데스크탑과 모바일 장치 모두에서 열리고 클릭될 수 있기 때문입니다.

일부 채널은 이러한 링크와 잘 작동하지 않습니다. 예를 들어, 푸시 알림, 인앱 메시지 및 콘텐츠 카드에는 스킴 기반의 딥링크를 사용해야 합니다(`mydomain://`).

{% alert note %}
Android 앱 링크에는 다른 웹 URL과 별도로 도메인의 링크를 처리하는 로직이 포함된 커스텀 `IBrazeDeeplinkHandler`가 필요합니다. 대신 딥링크를 사용하는 것이 더 쉬울 수 있으며 이메일 이외의 채널에 대한 링크 관행을 일관되게 유지할 수 있습니다.
{% endalert %}

## 필수 조건

유니버설 링크 및 앱 링크를 사용하려면:

- 귀하의 웹사이트는 HTTPS를 통해 액세스할 수 있어야 합니다
- 귀하의 앱은 App Store(iOS) 또는 Google Play Store(Android)에서 사용할 수 있어야 합니다

## 유니버설 링크 및 앱 링크 설정

앱이 유니버설 링크 또는 앱 링크를 지원하려면 iOS와 Android 모두 링크 도메인에 호스팅되는 특수 권한 파일이 필요합니다. 이 파일에는 해당 도메인에서 링크를 열 수 있는 앱과 iOS에서 이러한 앱이 열 수 있는 경로에 대한 정의가 포함되어 있습니다:

- **iOS:** Apple 앱 Site Association (AASA) file
- **Android:** 디지털 자산 링크 파일

이 권한 파일 외에도 앱 내에서 설정된 앱이 열 수 있는 링크 도메인의 하드코딩된 정의가 있습니다.

- **iOS:** Xcode에서 "연관 도메인"으로 설정
- **Android:** 앱의 `AndroidManifest.xml` 파일에 정의됨

이 두 부분으로 구성된 도메인-앱 연관은 유니버설 링크 또는 앱 링크가 작동하기 위해 필요하며 특정 도메인에서 링크를 가로채거나 특정 앱을 여는 것을 방지합니다.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

이 단계는 Apple 개발자 설명서에서 가져온 것입니다. 자세한 내용은 [앱과 웹사이트가 귀하의 콘텐츠에 연결되도록 허용하기](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)를 참조하십시오.

### 1단계: 앱 권한을 구성합니다

{% alert note %}
[Xcode 13 및 이후 버전에서](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode는 권한 프로비저닝을 자동으로 처리할 수 있습니다. 문제가 발생하면 [1c 단계](#step-1c)로 건너뛰고 이 지침을 참조할 수 있습니다.
{% endalert %}

#### 1단계 a: 앱 을 등록합니다{#step-1a}

1. developer.apple.com으로 이동하고 로그인하세요.
2. **인증서, 식별자 및 프로필**을 클릭합니다.
3. **식별자**를 클릭합니다.
4. 앱 식별자가 아직 등록되지 않은 경우 +를 클릭하여 하나를 만듭니다.
   a. **이름**을 입력하세요. 원하는 아무 이름을 사용할 수 있습니다.
   b. **번들 ID**를 입력하세요. Xcode 프로젝트의 **일반** 탭에서 번들 ID를 찾아 올바른 구축 대상을 설정할 수 있습니다.

#### 1b단계: 앱 식별자에서 연결된 도메인을 켜십시오

1. 기존 또는 새로 생성한 앱 식별자에서 **앱 서비스** 섹션을 찾으십시오.
2. **연관된 도메인**을 선택하십시오.
3. **저장**을 클릭합니다.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### 1단계 c: Xcode 프로젝트에서 연결된 도메인을 켭니다 {#step-1c}

진행하기 전에 Xcode 프로젝트에서 방금 등록한 앱 식별자와 동일한 팀이 선택되어 있는지 확인하세요. 

1. Xcode에서 프로젝트 파일의 **Capabilities** 탭으로 이동합니다.
2. **연관된 도메인**을 켜십시오.

##### 문제 해결 팁

다음 오류가 발생하면 "'your-app-id' 식별자를 가진 앱 ID를 사용할 수 없습니다. 다른 문자열을 입력하십시오", 다음을 수행하십시오:

1. 선택한 팀이 올바른지 확인하십시오.
2. Xcode 프로젝트의 번들 ID([step 1a](#step-1a))가 앱 식별자를 등록하는 데 사용된 것과 일치하는지 확인합니다.

#### 1단계 d: 도메인 자격 추가

도메인 섹션에서 적절한 도메인 태그를 추가하십시오. `applinks:`로 시작해야 합니다. 이 경우, 우리는 `applinks:yourdomain.com`을 추가한 것을 볼 수 있습니다.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### 1단계 e: 구축 시 권한 파일이 포함되어 있는지 확인하세요

프로젝트 브라우저에서 새 사용 권한 파일이 **대상 멤버십**에 선택되어 있는지 확인하세요.

Xcode는 이를 자동으로 처리해야 합니다.

### 2단계: 웹사이트를 구성하여 AASA 파일을 호스팅하십시오

iOS에서 네이티브 앱과 웹사이트 도메인을 연결하려면 Apple 앱 사이트 연결(AASA) 파일을 웹사이트에 호스팅해야 합니다. 이 파일은 iOS에 도메인 소유권을 확인하는 안전한 방법으로 사용됩니다. iOS 9 이전에는 개발자가 검증 없이 앱을 열기 위해 임의의 URI 스킴을 등록할 수 있었습니다. 그러나 AASA를 통해 이 과정은 훨씬 더 안전하고 신뢰할 수 있게 되었습니다.

AASA 파일에는 도메인에서 보편적 링크로 포함되거나 제외되어야 하는 앱 목록과 URL 경로가 포함된 JSON 객체가 포함되어 있습니다. 다음은 샘플 AASA 파일입니다:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: 앱의 **팀 ID** (팀 ID를 얻으려면 `https://developer.apple.com/account/#/membership/`로 이동) 및 **번들 식별자**를 결합하여 빌드되었습니다. 위의 예에서 "JHGFJHHYX"는 팀 ID이고, "com.facebook.ios"는 번들 ID입니다.
- `paths`: 포함되거나 제외되는 경로를 지정하는 문자열 배열. 경로를 비활성화하려면 경로 앞에 `NOT`을 사용할 수 있습니다. 이 예제에서는 이 경로의 모든 링크가 앱을 여는 대신 웹으로 이동합니다. 디렉토리의 모든 경로를 활성화하려면 `*`를 와일드카드로 사용할 수 있으며, 단일 문자를 일치시키려면 `?`를 사용할 수 있습니다 (예: /archives/201?/는 2010년부터 2019년까지의 모든 숫자와 일치합니다).

{% alert note %}
이 문자열들은 대소문자를 구분하며 쿼리 문자열과 프래그먼트 식별자는 무시됩니다.
{% endalert %}

### 3단계: 도메인에 AASA 파일을 호스팅하십시오

AASA 파일을 준비하면 `https://<<yourdomain>>/apple-app-site-association` 또는 `https://<<yourdomain>>/.well-known/apple-app-site-association`에서 도메인에 호스팅할 수 있습니다.

HTTPS 웹 서버에 `apple-app-site-association` 파일을 업로드하십시오. 파일을 서버의 루트 또는 `.well-known` 하위 디렉토리에 배치할 수 있습니다. 파일 이름에 `.json`을 추가하지 마십시오.

{% alert important %}
iOS는 안전한 연결(HTTPS)을 통해서만 AASA 파일을 가져오려고 시도할 것입니다.
{% endalert %}

AASA 파일을 호스팅하는 동안 파일이 다음 지침을 따르는지 확인하세요.

- HTTPS를 통해 제공됩니다.
- `application/json` MIME 유형을 사용합니다.
- 128KB를 초과하지 않습니다(iOS 9.3.1 이상에서 요구됨)

### 4단계: 앱이 범용 링크를 처리할 수 있도록 준비하십시오

사용자가 iOS 기기에서 범용 링크를 탭하면, 기기가 앱을 실행하고 [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) 객체를 보냅니다. 그 앱은 NSUserActivity 오브젝트를 쿼리하여 어떻게 실행되었는지 확인할 수 있습니다.

앱에서 유니버설 링크를 지원하려면 다음 단계를 따르세요:

1. 앱이 지원하는 도메인을 지정하는 권한을 추가합니다.
2. NSUserActivity 오브젝트를 받을 때 적절하게 응답하도록 앱 대리자를 업데이트하세요.

Xcode에서 **연관된 도메인** 섹션을 **기능** 탭에서 열고, 앱이 지원하는 각 도메인에 대해 `applinks:`로 시작하는 항목을 추가합니다. 예를 들어, `applinks:www.mywebsite.com`.

{% alert note %}
Apple은 이 목록을 20~30개 도메인으로 제한할 것을 권장합니다.
{% endalert %}

### 5단계: 보편적 링크를 테스트하세요

이메일에 유니버설 링크를 추가하고 테스트 기기로 보내세요. Safari URL 필드에 유니버설 링크를 직접 붙여넣어도 앱이 자동으로 열리지 않습니다. 이 작업을 수행하면 웹사이트를 수동으로 내려서 해당 앱을 열라는 메시지가 상단에 나타나도록 해야 합니다.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

이 단계는 Android 개발자 설명서에서 가져온 것입니다. 자세한 내용은 [Android 앱 링크 추가](https://developer.android.com/training/app-links#add-app-links) 및 [앱 콘텐츠에 대한 딥 링크 생성](https://developer.android.com/training/app-links/deep-linking)을 참조하세요.

{% alert note %}
Android 앱 링크에는 다른 웹 URL과 별도로 도메인의 링크를 처리하는 로직이 포함된 커스텀 `IBrazeDeeplinkHandler`가 필요합니다. 대신 딥링크를 사용하는 것이 더 쉬울 수 있으며 이메일 이외의 채널에 대한 링크 관행을 일관되게 유지할 수 있습니다.
{% endalert %}

### 1단계: 딥 링크 생성

먼저, Android 앱에 대한 딥링크를 생성해야 합니다. 이것은 `AndroidManifest.xml` 파일에 [의도 필터](https://developer.android.com/guide/components/intents-filters)를 추가하여 수행할 수 있습니다. 의도 필터는 `VIEW` 작업 및 `BROWSABLE` 카테고리를 포함해야 하며, 데이터 요소에 웹사이트의 URL을 포함해야 합니다.

### 2단계: 앱을 웹사이트와 연결하세요

귀하의 앱을 웹사이트와 연결해야 합니다. 이는 디지털 자산 링크 파일을 생성하여 수행할 수 있습니다. 이 파일은 JSON 형식이어야 하며, 귀하의 웹사이트로 연결되는 링크를 열 수 있는 Android 앱에 대한 세부 정보를 포함합니다. 귀하의 웹사이트 `.well-known` 디렉토리에 배치해야 합니다.

### 3단계: 앱 매니페스트 파일을 업데이트하세요

귀하의 `AndroidManifest.xml` 파일에서 애플리케이션 요소 내에 메타 데이터 요소를 추가하십시오. 메타데이터 요소에는 "asset_statements"의 `android:name` 속성이 있어야 하며, 문자열 배열이 포함된 리소스 파일을 가리키는 `android:resource` 속성이 있어야 합니다.

### 4단계: 앱이 딥 링크를 처리할 수 있도록 준비하십시오

Android 앱에서 들어오는 딥 링크를 처리해야 합니다. 활동을 시작한 의도를 얻고 거기에서 데이터를 추출하여 이 작업을 수행할 수 있습니다.

### 5단계: 딥링크 테스트

마침내, 딥링크를 테스트할 수 있습니다. 메시징 앱 또는 이메일을 통해 링크를 자신에게 보내고 클릭하세요. 모든 설정이 올바르게 되어 있으면 앱이 열릴 것입니다.

{% endtab %}
{% endtabs %}

## 유니버설 링크, 앱 링크, 및 클릭-추적

{% alert note %}
클릭-추적 링크는 일반적으로 이메일 온보딩의 일부로 설정됩니다. 고객 온보딩 중에 완료되지 않은 경우 계정 매니저에게 도움을 요청하세요.
{% endalert %}

우리의 이메일 발송 파트너인 SendGrid와 SparkPost는 모든 링크를 래핑하고 Braze 이메일에서 클릭 추적을 위해 URL 매개변수를 포함하기 위해 클릭 추적 도메인을 사용합니다.

예를 들어, `https://www.example.com` 같은 링크는 `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`과 같은 것이 됩니다.

이메일 링크가 클릭 추적과 함께 유니버설 링크 또는 앱 링크로 작동하도록 하려면 추가 설정이 필요합니다. 앱이 열 수 있도록 허용된 도메인으로 클릭-추적 도메인(`links.email.example.com`)을 추가하세요. 게다가, 클릭-추적 도메인은 AASA (iOS) 또는 Digital 자산 Links(Android) 파일을 제공해야 합니다. 이것은 이메일 링크가 클릭-추적과 원활하게 작동하도록 도와줍니다.

모든 클릭-추적 링크가 유니버설 링크 또는 앱 링크가 되지 않도록 하려면, 이메일 발송 파트너를 기준으로 어떤 링크가 유니버설 링크가 되어야 하는지 지정할 수 있습니다. 다음 섹션을 참조하세요.

### SendGrid

SendGrid 클릭-추적 링크를 범용 링크로 취급하려면:

1. AASA 또는 AndroidManifest pathPrefix 값을 설정하여 URL 경로에 `/uni/`이 포함된 링크만 범용 링크로 처리하도록 하십시오.
2. 링크의 앵커 태그(`<a>`)에 속성 `universal="true"`를 추가하세요. 이것은 래핑된 링크의 URL 경로가 `/uni/`를 포함하도록 변경합니다.

{% alert note %}
AMP 이메일의 경우 이 속성은 data-universal="true"이어야 합니다.
{% endalert %}

예를 들어, 다음과 같습니다.

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. 앱이 래핑된 링크를 올바르게 처리하도록 설정되어 있는지 확인하세요. SendGrid의 [SendGrid 클릭 추적 링크 해결](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links)에 관한 기사를 참고하고 운영 체제에 맞는 단계를 따르세요. 이 기사에는 [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) 및 [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android)에 대한 예제 코드가 포함되어 있습니다.

이 구성으로 `/uni/` URL 경로가 있는 링크는 유니버셜 링크로 작동하며, 다른 모든 링크는 웹 링크로 작동합니다.

### SparkPost

SparkPost 클릭 추적 링크를 범용 링크로 처리하려면 이메일의 드래그 앤 드롭 편집기의 속성 섹션에 다음 속성을 추가하거나 링크 HTML을 수동으로 편집하여 링크의 앵커 태그에 다음 속성을 포함하십시오: `data-msys-sublink="custom_path"`.

이 커스텀 경로를 사용하면 해당 값을 가진 URL을 범용 링크로 선택적으로 처리할 수 있습니다.

예를 들어, 다음과 같습니다.

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

그런 다음, 앱이 커스텀 경로를 올바르게 처리하도록 설정되어 있는지 확인하세요. SparkPost의 [딥링크에서 SparkPost 클릭 추적 사용](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links)에 관한 기사를 참조하세요. 이 기사에는 [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) 및 [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost)에 대한 예제 코드가 포함되어 있습니다.

### 링크 대 링크 기준으로 클릭 추적 끄기

HTML 편집기의 경우 이메일 메시지에 HTML 코드를 추가하거나 드래그 앤 드롭 편집기의 경우 HTML 블록에 추가하여 특정 링크에 대한 클릭 추적을 해제할 수 있습니다.

#### SendGrid

이메일 서비스 제공업체가 SendGrid인 경우 다음과 같이 HTML 코드 `clicktracking=off` 를 사용합니다:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

이메일 서비스 제공업체가 SparkPost인 경우 다음과 같이 HTML 코드 `data-msys-clicktrack="0"` 를 사용합니다:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

이메일 서비스 제공업체가 Amazon SES인 경우 다음과 같이 HTML 코드 `ses:no-track` 를 사용합니다:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### 드래그 앤 드롭 편집기

끌어서 놓기 이메일 편집기를 사용할 때 링크가 텍스트, 버튼 또는 이미지에 첨부된 경우 사용자 지정 속성으로 HTML 코드를 입력합니다.

##### 텍스트 링크의 사용자 지정 속성

#### SendGrid

사용자 지정 속성에 대해 다음을 선택합니다:

- **이름:** `clicktracking`
- **가치:** `off`

#### SparkPost

사용자 지정 속성에 대해 다음을 선택합니다:

- **이름:** `data-msys-clicktrack`
- **가치:** `0`

![텍스트 링크의 사용자 지정 속성입니다.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### 버튼 또는 이미지의 사용자 지정 속성

#### SendGrid

사용자 지정 속성에 대해 다음을 선택합니다:

- **이름:** `clicktracking`
- **가치:** `off`
- **유형:** 링크

#### SparkPost

사용자 지정 속성에 대해 다음을 선택합니다:

- **이름:** `data-msys-clicktrack`
- **가치:** `0`
- **유형:** 링크

![버튼의 사용자 지정 속성입니다.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### 클릭-추적으로 유니버셜 링크 문제 해결

이메일에서 유니버셜 링크가 예상대로 작동하지 않는 경우, 예를 들어 수신자를 이메일 앱에서 웹 브라우저로 이동한 후 최종적으로 앱으로 리디렉션하는 경우, 유니버셜 링크 설정 문제를 해결하기 위한 다음 팁을 참조하세요.

#### 링크 파일 위치 확인

AASA 파일(iOS) 또는 Digital Asset Links 파일(Android)이 올바른 위치에 있는지 확인하십시오:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

이 파일들이 항상 공개적으로 접근 가능하도록 하는 것이 중요합니다. 액세스할 수 없는 경우 이메일에 대한 유니버셜 링크 설정에서 단계를 놓쳤을 수 있습니다.

#### 도메인 정의 확인

도메인이 앱에서 열 수 있도록 허용된 정의가 올바른지 확인하세요.

- **iOS:** Xcode에서 앱([1단계 c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c))에 대한 관련 도메인 설정을 검토하세요. 해당 목록에 클릭 추적 도메인이 포함되어 있는지 확인하십시오.
- **Android:** 앱 정보 페이지를 여세요 (앱 아이콘을 길게 누르고 ⓘ를 클릭하세요). 앱 정보 메뉴에서 **기본값으로 열기**를 찾아 탭하세요. 이것은 앱이 열 수 있도록 허용된 모든 검증된 링크가 있는 화면을 표시해야 합니다. 해당 목록에 클릭 추적 도메인이 포함되어 있는지 확인하십시오.

