---
nav_title: 유니버설 링크 및 앱 링크
article_title: 유니버설 링크 및 앱 링크
page_order: 6.4
page_type: reference
description: "이 도움말 문서에서는 Apple 유니버설 링크 및 Android 앱 링크를 설정하는 방법을 안내합니다."
channel: email
---

# 유니버설 링크 및 앱 링크

Apple 유니버설 링크와 Android 앱 링크는 웹 콘텐츠와 모바일 앱 간의 원활한 전환을 제공하기 위해 고안된 메커니즘입니다. 유니버설 링크는 iOS에만 해당되는 반면, Android 앱 링크는 Android 애플리케이션에도 동일한 용도로 사용됩니다.

## 유니버설 링크 및 앱 링크 작동 방식

유니버설 링크(iOS) 및 앱 링크(Android)는 웹 페이지와 앱 내부의 콘텐츠를 모두 가리키는 표준 웹 링크(`http://mydomain.com`)입니다.

유니버설 링크 또는 앱 링크가 열리면 운영 체제는 해당 도메인에 설치된 앱이 등록되어 있는지 확인합니다. 앱이 발견되면 웹 페이지를 로드할 필요 없이 바로 실행됩니다. 앱을 찾을 수 없는 경우 사용자의 기본값 웹 브라우저에 웹 URL이 로드되며, 이 웹 브라우저는 각각 앱 스토어 또는 구글 플레이 스토어로 리디렉션되도록 구성할 수도 있습니다.

유니버설 링크를 사용하면 웹 사이트에서 웹 페이지를 특정 앱 화면과 연결할 수 있으므로 사용자가 앱 화면에 해당하는 웹 페이지의 링크를 클릭하면 앱이 바로 열립니다(현재 앱이 설치되어 있는 경우).

이 표에는 유니버설 링크와 기존 딥링크의 주요 차이점이 요약되어 있습니다:

|                        | 유니버설 링크 및 앱 링크                                  | 딥링크                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| 플랫폼 호환성 | iOS(버전 9 이상) 및 Android(버전 6.0 이상)  | 다양한 모바일 OS에서 사용    |
| 목적                | iOS 및 Android 기기에서 웹과 앱 콘텐츠를 원활하게 연결하세요. | 특정 앱 콘텐츠 링크 |
| 기능               | 컨텍스트에 따라 웹 페이지 또는 앱 콘텐츠로 이동합니다.           | 특정 앱 화면 열기   |
| 앱 설치       | 앱이 설치되어 있으면 앱을 열고, 그렇지 않으면 웹 콘텐츠를 엽니다. | 앱 설치 필요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용 사례

유니버설 링크와 앱 링크는 데스크톱과 모바일 기기 모두에서 이메일을 열고 클릭할 수 있으므로 이메일 캠페인에 가장 일반적으로 사용됩니다.

일부 채널은 이러한 링크가 제대로 작동하지 않습니다. 예를 들어 푸시 알림, 인앱 메시지, 콘텐츠 카드는 스키마 기반 딥링크를 사용해야 합니다(`mydomain://`).

{% alert note %}
Android 앱 링크에는 해당 도메인의 링크를 다른 웹 URL과 별도로 처리하는 로직이 포함된 커스텀 `IBrazeDeeplinkHandler` 이 필요합니다. 대신 딥링크를 사용하고 이메일 이외의 채널에 대해 일관된 링크 방식을 유지하는 것이 더 쉬울 수 있습니다.
{% endalert %}

## 전제 조건

유니버설 링크 및 앱 링크를 사용하려면:

- 웹사이트는 HTTPS를 통해 액세스할 수 있어야 합니다.
- 앱은 앱 스토어(iOS) 또는 구글 플레이 스토어(Android)에서 사용할 수 있어야 합니다.

## 유니버설 링크 및 앱 링크 설정하기

앱이 유니버설 링크 또는 앱 링크를 지원하려면 iOS와 Android 모두 링크 도메인에 특수 권한 파일을 호스팅해야 합니다. 이 파일에는 해당 도메인의 링크를 열 수 있는 앱과 iOS의 경우 이러한 앱이 열 수 있는 경로에 대한 정의가 포함되어 있습니다:

- **iOS:** 애플 앱 사이트 협회(AASA) 파일
- **Android:** 디지털 자산 링크 파일

이 권한 파일 외에도 앱 내에서 설정된 앱이 열 수 있는 링크 도메인에 대한 하드코딩된 정의가 있습니다:

- **iOS:** Xcode에서 "연결된 도메인"으로 설정
- **Android:** 앱의 `AndroidManifest.xml` 파일에 정의되어 있습니다.

이 두 부분으로 구성된 도메인-앱 연결은 유니버설 링크 또는 앱 링크가 작동하는 데 필요하며 특정 도메인의 링크를 앱이 가로채거나 특정 도메인이 특정 앱을 열지 못하도록 방지합니다.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

이 단계는 Apple 개발자 설명서를 기반으로 합니다. 자세한 내용은 [앱 및 웹사이트가 내 콘텐츠에 링크하도록 허용하기를](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc) 참조하세요.

### 1단계: 앱 권한 구성하기

{% alert note %}
[Xcode 13 이상에서는](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/) Xcode에서 자동으로 권한 프로비저닝을 처리할 수 있습니다. 문제가 있는 경우 [1c 단계로](#step-1c) 건너뛰고 이 지침을 다시 참조해도 됩니다.
{% endalert %}

#### 1a단계: 앱 등록하기 {#step-1a}

1. developer.apple.com 으로 이동하여 로그인합니다.
2. **인증서, 식별자 & 프로필을** 클릭합니다.
3. **식별자를** 클릭합니다.
4. 아직 등록된 앱 식별자가 없는 경우 +를 클릭하여 생성하세요.
   a. **이름을** 입력합니다. 원하는 것은 무엇이든 가능합니다.
   b. **번들 ID를** 입력합니다. 적절한 빌드 타겟팅을 위해 Xcode 프로젝트의 **일반** 탭에서 번들 ID를 찾을 수 있습니다.

#### 1b단계: 앱 식별자에서 연결된 도메인 켜기

1. 기존 또는 새로 생성한 앱 식별자에서 **앱 서비스** 섹션을 찾습니다.
2. **연결된 도메인을** 선택합니다.
3. **저장을** 클릭합니다.

\![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### 1c단계: Xcode 프로젝트에서 연관 도메인 켜기 {#step-1c}

계속하기 전에 Xcode 프로젝트에 방금 앱 식별자를 등록한 곳과 동일한 팀이 선택되어 있는지 확인하세요. 

1. Xcode에서 프로젝트 파일의 **기능** 탭으로 이동합니다.
2. **연결된 도메인을** 켭니다.

##### 문제 해결 팁

"식별자가 'your-app-id'인 앱 ID를 사용할 수 없습니다."라는 오류가 표시되는 경우. 다른 문자열을 입력하세요"라는 메시지가 표시되면 다음을 수행합니다:

1. 올바른 팀을 선택했는지 확인하세요.
2. Xcode 프로젝트의 번들 ID[(1a 단계)](#step-1a)가 앱 식별자 등록에 사용된 ID와 일치하는지 확인합니다.

#### 1d 단계: 도메인 권한 추가하기

도메인 섹션에서 적절한 도메인 태그를 추가합니다. 접두사 앞에 `applinks:` 를 붙여야 합니다. 이 경우 `applinks:yourdomain.com` 을 추가한 것을 볼 수 있습니다.

\![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### 1e 단계: 구축 시 자격 파일이 포함되어 있는지 확인합니다.

프로젝트 브라우저에서 새 자격 파일이 **대상 멤버십** 아래에 선택되어 있는지 확인합니다.

Xcode는 이를 자동으로 처리해야 합니다.

### 2단계: AASA 파일을 호스팅하도록 웹사이트를 구성하세요.

웹사이트 도메인을 iOS의 기본 앱과 연결하려면 웹사이트에 AASA(Apple 앱 사이트 협회) 파일을 호스팅해야 합니다. 이 파일은 iOS에 도메인 소유권을 확인하는 안전한 방법으로 사용됩니다. iOS 9 이전에는 개발자가 아무런 인증 없이 아무 URI 체계나 등록하여 앱을 열 수 있었습니다. 하지만 AASA를 사용하면 이 프로세스가 훨씬 더 안전하고 신뢰할 수 있게 되었습니다.

AASA 파일에는 유니버설 링크로 포함하거나 제외해야 하는 앱 목록과 도메인의 URL 경로가 포함된 JSON 객체가 포함되어 있습니다. 다음은 샘플 AASA 파일입니다:

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

- `appID`: 앱의 **팀** ID( `https://developer.apple.com/account/#/membership/` 에서 팀 ID를 확인)와 **번들 식별자를** 결합하여 구축합니다. 위의 예에서 "JHGFJHHYX"는 팀 ID이고 "com.facebook.ios"는 번들 ID입니다.
- `paths`: 연결에서 포함하거나 제외할 경로를 지정하는 문자열 배열입니다. 경로 앞에 `NOT` 을 사용하여 경로를 비활성화할 수 있습니다. 이 예제에서는 이 경로의 모든 링크가 앱을 여는 대신 웹으로 이동합니다. 디렉터리의 모든 경로를 인에이블먼트하려면 `*`, 단일 문자를 일치시키려면 `?` (예: 2010년부터 2019년까지의 모든 숫자를 일치시키려면 /archives/201?/)을 와일드카드로 사용할 수 있습니다.

{% alert note %}
이러한 문자열은 대소문자를 구분하며 쿼리 문자열과 조각 식별자는 무시됩니다.
{% endalert %}

### 3단계: 도메인에서 AASA 파일 호스팅하기

AASA 파일이 준비되면 이제 `https://<<yourdomain>>/apple-app-site-association` 또는 `https://<<yourdomain>>/.well-known/apple-app-site-association` 에서 도메인에 호스팅할 수 있습니다.

`apple-app-site-association` 파일을 HTTPS 웹 서버에 업로드합니다. 서버의 루트 또는 `.well-known` 하위 디렉터리에 파일을 저장할 수 있습니다. 파일 이름에 `.json` 을 추가하지 마세요.

{% alert important %}
iOS는 보안 연결(HTTPS)을 통해서만 AASA 파일 가져오기를 시도합니다.
{% endalert %}

AASA 파일을 호스팅하는 동안 파일이 다음 가이드라인을 따르고 있는지 확인하세요:

- HTTPS를 통해 제공됩니다.
- `application/json` MIME 유형을 사용합니다.
- 128KB를 초과하지 않음(iOS 9.3.1 이상에서 요구 사항)

### 4단계: 유니버설 링크를 처리하도록 앱 준비하기

사용자가 iOS 기기에서 유니버설 링크를 탭하면 기기는 앱을 실행하고 [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) 객체를 전송합니다. 그런 다음 앱은 NSUserActivity 객체를 쿼리하여 앱이 어떻게 실행되었는지 확인할 수 있습니다.

앱에서 유니버설 링크를 지원하려면 다음 단계를 따르세요:

1. 앱이 지원하는 도메인을 지정하는 권한을 추가합니다.
2. 앱 델리게이트가 NSUserActivity 객체를 수신할 때 적절하게 응답하도록 업데이트하세요.

Xcode에서 **기능** 탭의 **연결된 도메인** 섹션을 열고 앱이 지원하는 각 도메인에 대해 접두사가 `applinks:` 로 시작하는 항목을 추가합니다. 예: `applinks:www.mywebsite.com`.

{% alert note %}
Apple은 이 목록을 20~30개 이하의 도메인으로 제한할 것을 권장합니다.
{% endalert %}

### 5단계: 유니버설 링크 테스트

이메일에 유니버설 링크를 추가하고 테스트 기기로 전송합니다. 유니버설 링크를 Safari URL 필드에 직접 붙여넣어도 앱이 자동으로 열리지 않습니다. 이렇게 하면 해당 앱을 열라는 메시지가 상단에 표시되도록 웹사이트를 수동으로 아래로 내려야 합니다.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

이 단계는 Android 개발자 설명서를 기반으로 합니다. 자세한 내용은 [Android 앱 링크 추가](https://developer.android.com/training/app-links#add-app-links) 및 [앱 콘텐츠에 딥링크 생성을](https://developer.android.com/training/app-links/deep-linking) 참조하세요.

{% alert note %}
Android 앱 링크에는 해당 도메인의 링크를 다른 웹 URL과 별도로 처리하는 로직이 포함된 커스텀 `IBrazeDeeplinkHandler` 이 필요합니다. 대신 딥링크를 사용하고 이메일 이외의 채널에 대해 일관된 링크 방식을 유지하는 것이 더 쉬울 수 있습니다.
{% endalert %}

### 1단계: 딥링크 만들기

먼저 Android 앱에 대한 딥링크를 만들어야 합니다. `AndroidManifest.xml` 파일에 [의도 필터를](https://developer.android.com/guide/components/intents-filters) 추가하여 이 작업을 수행할 수 있습니다. 의도 필터에는 데이터 요소에 웹사이트의 URL과 함께 `VIEW` 작업 및 `BROWSABLE` 카테고리가 포함되어야 합니다.

### 2단계: 앱을 웹사이트와 연동하기

앱을 웹사이트와 연결해야 합니다. 이 작업은 디지털 자산 링크 파일을 생성하여 수행할 수 있습니다. 이 파일은 JSON 형식이어야 하며 웹사이트 링크를 열 수 있는 Android 앱에 대한 세부 정보가 포함되어 있어야 합니다. 웹사이트의 `.well-known` 디렉토리에 배치해야 합니다.

### 3단계: 앱 매니페스트 파일 업데이트하기

`AndroidManifest.xml` 파일에서 애플리케이션 요소 안에 메타데이터 요소를 추가합니다. 메타데이터 요소에는 "asset_statements" 속성이 `android:name`, 웹사이트의 URL이 포함된 문자열 배열이 있는 리소스 파일을 가리키는 `android:resource` 속성이 있어야 합니다.

### 4단계: 앱이 딥링킹을 처리할 수 있도록 준비하기

Android 앱에서는 들어오는 딥링킹을 처리해야 합니다. 활동을 시작한 의도를 파악하고 거기서 데이터를 추출하면 됩니다.

### 5단계: 딥링크 테스트하기

마지막으로 딥링킹을 테스트할 수 있습니다. 메시징 앱이나 이메일을 통해 링크를 전송하고 클릭합니다. 모든 것이 올바르게 설정되었다면 앱을 열어야 합니다.

{% endtab %}
{% endtabs %}

## 유니버설 링크, 앱 링크 및 클릭 추적

{% alert note %}
클릭 추적 링크는 일반적으로 이메일 온보딩의 일부로 설정됩니다. 고객 온보딩 중에 이 작업이 완료되지 않은 경우 계정 매니저에게 도움을 요청하세요.
{% endalert %}

이메일 전송 파트너인 SendGrid와 SparkPost는 클릭 추적 도메인을 사용하여 모든 링크를 래핑하고 Braze 이메일에 클릭 추적을 위한 URL 매개변수를 포함합니다.

예를 들어 `https://www.example.com` 과 같은 링크는 `https://links.email.example.com/uni/wf/click?upn=abcdef123456…` 과 같은 링크가 됩니다.

클릭 추적 기능이 있는 이메일 링크가 유니버설 링크 또는 앱 링크로 작동하도록 허용하려면 몇 가지 추가 설정을 수행해야 합니다. 클릭 추적 도메인(`links.email.example.com`)을 앱이 열 수 있는 도메인으로 추가해야 합니다. 또한 클릭 추적 도메인은 AASA(iOS) 또는 디지털 자산 링크(Android) 파일을 제공해야 합니다. 이렇게 하면 클릭 추적 기능이 있는 이메일 링크가 원활하게 작동하는 데 도움이 됩니다.

모든 클릭 추적 링크를 유니버설 링크 또는 앱 링크가 아닌 경우 이메일 전송 파트너에 따라 유니버설 링크가 될 링크를 지정할 수 있습니다. 자세한 내용은 다음 섹션을 참조하세요.

### SendGrid

SendGrid 클릭 추적 링크를 범용 링크로 취급하려면:

1. URL 경로에 `/uni/` 가 포함된 링크만 유니버설 링크로 취급하도록 AASA 또는 AndroidManifest 경로 접두사 값을 설정하세요.
2. 링크의 앵커 태그(`<a>`)에 `universal="true"` 속성을 추가합니다. 이렇게 하면 래핑된 링크의 URL 경로가 `/uni/` 를 포함하도록 변경됩니다.

{% alert note %}
AMP 이메일의 경우 이 속성은 데이터 유니버설="true"여야 합니다.
{% endalert %}

예를 들어

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. 앱이 래핑된 링크를 올바르게 처리하도록 설정되어 있는지 확인하세요. SendGrid [클릭 추적 링크 해결에](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) 대한 문서를 참조하여 운영 체제에 맞는 단계를 따르세요. 이 문서에는 [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) 및 [Android용](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android) 예제 코드가 포함되어 있습니다.

이 구성을 사용하면 URL 경로에 `/uni/` 이 포함된 링크는 유니버설 링크로 작동하고 다른 모든 링크는 웹 링크로 작동합니다.

### SparkPost

스팍포스트 클릭 추적 링크를 유니버설 링크로 취급하려면 이메일용 드래그 앤 드롭 편집기의 속성 섹션에 다음 속성을 추가하거나 링크의 앵커 태그에 다음 속성을 포함하도록 링크 HTML을 수동으로 편집하세요: `data-msys-sublink="custom_path"`.

이 커스텀 경로를 사용하면 해당 값을 가진 URL을 선택적으로 유니버설 링크로 취급할 수 있습니다.

예를 들어

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

그런 다음 앱이 커스텀 경로를 올바르게 처리하도록 설정되어 있는지 확인하세요. 스팍포스트의 [딥링크에서 스팍포스트 클릭 추적 사용하기](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links) 문서를 참조하세요. 이 문서에는 [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) 및 [Android용](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost) 예제 코드가 포함되어 있습니다.

### 링크 대 링크 기준으로 클릭 추적 끄기

HTML 편집기의 경우 이메일 메시지에 HTML 코드를 추가하거나 드래그 앤 드롭 편집기의 경우 HTML 블록에 추가하여 특정 링크에 대한 클릭 추적을 해제할 수 있습니다.

#### SendGrid

이메일 서비스 제공업체가 SendGrid인 경우 HTML 코드 `clicktracking=off` 를 다음과 같이 사용하세요:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

이메일 서비스 제공업체가 SparkPost인 경우 다음과 같이 HTML 코드 `data-msys-clicktrack="0"` 를 사용하세요:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

이메일 서비스 제공업체가 Amazon SES인 경우 다음과 같은 HTML 코드 `ses:no-track` 를 사용합니다:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### 드래그 앤 드롭 편집기

드래그 앤 드롭 이메일 편집기를 사용할 때 링크가 텍스트, 버튼 또는 이미지에 첨부된 경우 HTML 코드를 커스텀 속성으로 입력합니다.

##### 텍스트 링크의 커스텀 속성

#### SendGrid

커스텀 속성에 대해 다음을 선택합니다:

- **이름:** `clicktracking`
- **가치:** `off`

#### SparkPost

커스텀 속성에 대해 다음을 선택합니다:

- **이름:** `data-msys-clicktrack`
- **가치:** `0`

텍스트 링크에 대한 커스텀 속성입니다.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### 버튼 또는 이미지에 대한 커스텀 속성

#### SendGrid

커스텀 속성에 대해 다음을 선택합니다:

- **이름:** `clicktracking`
- **가치:** `off`
- **유형:** 링크

#### SparkPost

커스텀 속성에 대해 다음을 선택합니다:

- **이름:** `data-msys-clicktrack`
- **가치:** `0`
- **유형:** 링크

버튼에 대한 커스텀 속성입니다.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### 클릭 추적을 통한 유니버설 링크 문제 해결

수신자가 이메일 앱에서 웹 브라우저로 이동한 후 앱으로 리디렉션되는 등 이메일에서 유니버설 링크가 예상대로 작동하지 않는 경우 다음 팁을 참조하여 유니버설 링크 설정 문제를 해결하세요.

#### 링크 파일 위치 확인

AASA 파일(iOS) 또는 디지털 자산 링크 파일(Android)이 올바른 위치에 있는지 확인합니다:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

이러한 파일은 항상 공개적으로 액세스할 수 있도록 하는 것이 중요합니다. 액세스할 수 없는 경우 이메일용 유니버설 링크 설정 단계를 놓친 것일 수 있습니다.

#### 도메인 정의 확인

앱이 열 수 있는 도메인에 대한 정의가 올바른지 확인하세요.

- **iOS:** 앱에 대해 Xcode에서 설정된 연관 도메인을 검토합니다[(1c 단계)]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c). 클릭 추적 도메인이 해당 목록에 포함되어 있는지 확인합니다.
- **Android:** 앱 정보 페이지를 엽니다(앱 아이콘을 길게 누른 후 ⓘ 클릭). 앱 정보 메뉴에서 **기본값으로 열기를** 찾아서 탭합니다. 앱에서 열 수 있도록 허용된 모든 확인된 링크가 있는 화면이 표시됩니다. 클릭 추적 도메인이 해당 목록에 포함되어 있는지 확인합니다.

