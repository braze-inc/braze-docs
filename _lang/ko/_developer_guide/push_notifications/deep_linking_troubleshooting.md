---
nav_title: 딥링킹 문제 해결
article_title: 딥링킹 문제 해결
description: "iOS에서 흔히 발생하는 딥링킹 문제와 진단 방법, 커스텀 스킴 링크, 유니버설 링크, 이메일 링크, Branch와 같은 타사 제공업체를 포함합니다."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# 딥링킹 문제 해결

> 이 페이지는 iOS에서 발생하는 일반적인 딥링킹 문제와 그 진단 방법을 다룹니다. 적합한 링크 유형 선택에 대한 도움말은 [iOS 딥링킹 가이드를]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide) 참조하십시오. 구현 세부 사항은 [딥링킹을]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift) 참조하십시오.

## 커스텀 스킴 딥링크가 올바른 뷰를 열지 않습니다

커스텀 스킴 딥링크(예: `myapp://products/123`)가 앱을 열지만 의도한 화면으로 이동하지 않는 경우:

1. **해당 계획이 등록되었는지 확인하십시오.** Xcode에서 스킴이  아래에 나열되어 `CFBundleURLTypes``Info.plist`있는지 확인하십시오.
2. **핸들러를 확인하세요.** 에 중단점을 설정하여`application(_:open:options:)` 호출되는지 확인하고 `url`매개변수를 검사하십시오.
3. **링크를 독립적으로 테스트하십시오.** 터미널에서 다음 명령어를 실행하여 Braze 외부에서 딥링크를 테스트하세요:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   해당 링크가 작동하지 않는다면, 문제는 Braze가 아닌 앱의 URL 처리 방식에 있습니다.
4. **URL 형식을 확인하십시오.** 캠페인에 포함된 URL이 핸들러가 예상하는 것과 일치하는지 확인하십시오. 흔히 발생하는 오류로는 경로 구성 요소가 누락되거나 대소문자가 잘못된 경우가 있습니다.

## 유니버설 링크가 앱 대신 사파리에서 열립니다

만약 유니버설 링크(예: `https://myapp.com/products/123`)가 앱 대신 Safari에서 열린다면:

### 연동 도메인 권한 확인

Xcode에서 앱 타깃 > **서명&기능**으로 이동하여 **'연관된 도메인'** 아래에 다음 항목이 나열되어 있는지`applinks:yourdomain.com` 확인하십시오.

### AASA 파일 유효성 검사

Apple 앱 사이트 연결(AASA) 파일은 다음 위치 중 하나에 호스팅되어야 합니다:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

다음 사항을 확인하십시오:

- 해당 파일은 유효한 인증서로 HTTPS를 통해 제공됩니다.
- 그것은 `Content-Type``application/json`.
- 파일 크기는 128KB 미만입니다.
- 해당 항목은 귀하의 팀 ID`appID` 및 번들 ID와 일치합니다(예: `ABCDE12345.com.example.myapp`).
- 해당`components``paths`배열에는 예상하는 URL 패턴이 포함됩니다.

AASA를 검증하려면 [Apple의 검색 검증 도구를](https://search.developer.apple.com/appsearch-validation-tool/) 사용하거나 다음 명령어를 실행하세요:

```bash
swcutil dl -d yourdomain.com
```

### 확인하십시오 `AppDelegate`

다음이`application(_:continue:restorationHandler:)`구현되었는지 확인하고`AppDelegate` 올바르게 `NSUserActivity`처리하는지 검증하십시오:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Braze 소프트웨어 개발 키트 구성 확인

Braze에서 전송된 푸시 알림, 인앱 메시지 또는 콘텐츠 카드에서 유니버설 링크를 사용하는 경우 다음이`forwardUniversalLinks`활성화되었는지 확인하십시오:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
유니버설 링크를 전달하려면 애플리케이션 권한에 대한 액세스 권한이 필요합니다. 시뮬레이터에서 실행할 때는 이러한 권한이 직접적으로 사용할 수 없습니다. 시뮬레이터에서 테스트하려면 **Copy Bundle Resources** 구축 단계에 파일을`.entitlements` 추가하십시오.
{% endalert %}

### 길게 누르기 문제 확인

유니버설 링크를 길게 눌러 **'열기'를** 선택하면 iOS가 해당 도메인의 유니버설 링크 연결을 '해제'할 수 있습니다. 이는 iOS의 알려진 동작입니다. 재설정하려면 링크를 다시 길게 누르고 **[앱 이름]에서 열기를** 선택하세요.

## 이메일의 딥링크가 앱을 열지 않습니다

이메일 링크는 귀사의 이메일 서비스 공급자의 클릭 추적 시스템을 거치며, 이 시스템은 링크를 추적 도메인(예: `https://click.yourdomain.com/...`)으로 감쌉니다. 이메일에서 유니버설 링크가 작동하려면 클릭 추적 도메인(기본 도메인뿐만 아니라)에 AASA 파일을 구성해야 합니다.

### 클릭 추적 도메인 AASA 확인

1. 이메일 서비스 공급자 설정(SendGrid, SparkPost 또는 Amazon SES)에서 클릭 추적 도메인을 식별하세요.
2. AASA 파일을 호스팅하십시오`https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. 클릭 추적 도메인의 AASA 파일에 동일한 `appID`유효한 경로 패턴이 포함되도록 하십시오.

ESP 전용 설정 지침은 [유니버설 링크 및 앱 링크를]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/) 참조하십시오.

### 리디렉션 체인을 확인하십시오

일부 이메일 서비스 공급자는 클릭 추적 URL에서 최종 URL로 리디렉션을 수행합니다. 유니버설 링크는 iOS가 *초기* 도메인(클릭 추적 도메인)을 해당 앱과 연관된 것으로 인식할 때만 작동합니다. 리디렉션이 AASA 검사를 우회하면 링크가 Safari에서 열립니다.

테스트:

1. 자신에게 테스트 이메일을 보내세요.
2. 링크를 길게 누르고 URL을 확인하세요 — 이것이 클릭 추적 URL입니다.
3. 이 도메인에 유효한 AASA 파일이 있는지 확인하십시오.

## 딥링크는 푸시 알림에서는 작동하지만 인앱 메시지에서는 작동하지 않습니다(또는 그 반대의 경우도 마찬가지입니다).

### BrazeDelegate를 확인하십시오

구현 시`BrazeDelegate.braze(_:shouldOpenURL:)`, 채널 전반에 걸쳐 링크를 일관되게 처리하는지 확인하십시오. 매개변수에는`context` 소스 채널이 포함됩니다. 특정 채널의 링크를 실수로 필터링할 수 있는 조건 로직을 확인하십시오.

### 상세 로깅 활성화

[상세 로깅 인에이블먼트를]({{site.baseurl}}/developer_guide/verbose_logging) 활성화하고 문제를 재현하십시오. 다음 로그 `Opening`항목을 찾으십시오:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

작동 채널과 비작동 채널의 로그 출력을 비교하십시오. 또는 로`useWebView` 표시된 차이는 소프트웨어 개발 `isUniversalLink`키트가 링크를 다르게 해석하는 방식을 나타냅니다.

### 커스텀 디스플레이 델리게이트 확인

사용자 정의 인앱 메시지 표시 델리게이트 또는 콘텐츠 카드 클릭 핸들러를 사용하는 경우, 링크 이벤트가 처리되도록 Braze SDK로 올바르게 전달되는지 확인하십시오.

## "앱 내에서 웹 URL 열기" 시 공백 또는 깨진 페이지가 표시됨

**앱 내에서 웹 URL 열기를** 선택했을 때 웹뷰가 비어 있거나 깨지는 경우:

1. **URL이 HTTPS를 사용하는지 확인하십시오.** 소프트웨어 개발 키트의 WebView는 ATS(App Transport Security)를 준수하는 URL을 요구합니다. HTTP 링크는 오류가 발생해도 아무런 알림 없이 실패합니다.
2. **콘텐츠 보안 정책 헤더를 확인하십시오.** 대상 웹 페이지가  또는 제한적인  `X-Frame-Options: DENY`을 설정하면 `Content-Security-Policy`WebView에서 렌더링이 차단됩니다.
3. **커스텀 스킴으로의 리디렉션을 확인하십시오.** 웹 페이지가 커스텀 스킴(예: `myapp://`)으로 리디렉션되는 경우 WebView는 이를 처리할 수 없습니다.
4. **Safari에서 URL을 테스트하세요.** 해당 기기의 Safari에서 페이지가 로드되지 않는다면, WebView에서도 로드되지 않습니다.

## Braze를 통한 문제 해결 브랜치 {#branch}

[Branch를]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) 연결 서비스 제공자로 사용하는 경우:

### 브레이즈 델리게이트 경로를 브랜치로 검증하십시오

Branch 링크를 가로채서 Branch 소프트웨어 개발 키트로 전달해야 합니다`BrazeDelegate`. 다음 사항을 확인하십시오:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Branch 링크에 대해 \`if\``true`가`shouldOpenURL`반환되면, Braze는 Branch로 라우팅하지 않고 직접 처리합니다.

### 지점 링크 도메인 확인

귀하의 Branch 도메인이 실제 `BrazeDelegate`Branch 링크 도메인과 일치하는지 확인하십시오. Branch는 여러 도메인 형식을 사용합니다:

- `yourapp.app.link` (기본값)
- `yourapp-alternate.app.link` (대체)
- 커스텀 도메인 (Branch 대시보드에서 설정된 경우)

### 두 SDK의 로깅을 모두 인에이블하십시오

연쇄에서 연결이 끊어지는 지점을 진단하기 위해:

1. [Braze 상세 로깅]({{site.baseurl}}/developer_guide/verbose_logging) 인에이블먼트 — 소프트웨어 개발 키트가 링크를 수신했는지 확인하기 위해 항목을 `Opening '<URL>':`찾으십시오.
2. [브랜치 테스트 모드](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) 활성화 — 브랜치 대시보드에서 링크 클릭 이벤트를 확인하세요.
1. [Braze 상세 로깅을]({{site.baseurl}}/developer_guide/verbose_logging) 활성화합니다. 소프트웨어 개발 키트가 링크를 수신했는지 확인하기 위해 항목을 `Opening '<URL>':`찾으십시오.
2. [브랜치 테스트 모드를](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) 인에이블합니다. 브랜치 대시보드에서 링크 클릭 이벤트를 확인하세요.
3. Braze가 링크를 기록했지만 Branch에서 클릭이 감지되지 않는다면, 라우팅 `BrazeDelegate`로직에 문제가 있을 가능성이 높습니다.

### 지점 대시보드 구성 확인

브랜치 대시보드에서 다음을 확인하십시오:

- 앱의 **번들 ID**와 **팀 ID가** Xcode 프로젝트와 일치합니다.
- 귀하의 **연결된 도메인에는** 브랜치 링크 도메인이 포함됩니다.
- 귀하의 Branch AASA 파일이 유효합니다(Branch가 `app.link`도메인에서 자동으로 호스팅합니다).

### 테스트 브랜치 링크를 독립적으로

문제를 격리하기 위해 Braze 외부에서 Branch 링크를 테스트하십시오:

1. 기기에서 Safari로 'Branch' 링크를 열어주세요. 앱이 열리지 않는다면, 문제는 Braze가 아닌 귀하의 Branch 또는 AASA 구성에 있습니다.
2. 브랜치 링크를 메모 앱에 붙여넣고 탭하세요. 노츠에서는 사파리 주소창보다 유니버설 링크가 더 안정적으로 작동합니다.

## 일반적인 디버깅 팁

### 상세 로깅 사용

[상세 로그를 인에이블하여]({{site.baseurl}}/developer_guide/verbose_logging) 소프트웨어 개발 키트가 링크를 처리하는 방식을 정확히 확인하십시오. 주요 항목:

| 로그 항목 | 의미 |
|---|---|
| `Opening '<URL>': - channel: notification` | 소프트웨어 개발 키트가 푸시 알림에서 링크를 처리 중입니다 |
| `Opening '<URL>': - channel: inAppMessage` | 소프트웨어 개발 키트가 인앱 메시지의 링크를 처리 중입니다 |
| `Opening '<URL>': - channel: contentCard` | 소프트웨어 개발 키트가 콘텐츠 카드의 링크를 처리 중입니다 |
| `useWebView: true` | 소프트웨어 개발 키트는 앱 내 웹뷰에서 URL을 엽니다 |
| `isUniversalLink: true` | 소프트웨어 개발 키트가 해당 URL을 유니버설 링크로 식별자로 사용했습니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이러한 로그를 읽는 방법에 대한 자세한 내용은 [상세 로그 읽기를]({{site.baseurl}}/developer_guide/verbose_logging) 참조하십시오.

### 테스트 링크를 독립적으로 실행

Braze를 통해 테스트하기 전에, 딥링크 또는 유니버설 링크가 단독으로 작동하는지 확인하십시오:

- **커스텀 구성**: 터미널에서`xcrun simctl openurl booted "myapp://path"` 실행하십시오.
- **유니버설 링크**: URL을 물리적 기기의 메모 앱에 붙여넣고 탭하세요. Safari 주소창에서 테스트하지 마십시오. iOS는 입력된 URL과 탭한 링크를 다르게 처리합니다.
- **지점 링크**: 기기에서 노트 앱의 '브랜치' 링크를 엽니다.

### 물리적 기기에서 테스트

유니버설 링크는 iOS 시뮬레이터에서 제한적으로 지원됩니다. 정확한 결과를 위해 항상 실제 기기에서 테스트하십시오. 시뮬레이터에서 테스트해야 하는 경우, **Copy Bundle Resources** 구축 단계에 파일을`.entitlements` 추가하십시오.