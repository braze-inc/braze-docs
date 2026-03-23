---
page_order: 1.1
nav_title: iOS 딥링킹 가이드
article_title: iOS 딥링킹 가이드
description: "iOS 앱에 사용할 딥링크 유형, AASA 파일 필요 시점, 구현해야 할 앱 델리게이트 메서드를 알아보세요."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# iOS 딥링킹 가이드

> 이 가이드는 사용 중인 메시징 채널과 Branch와 같은 타사 링크 제공업체 사용 여부에 따라 iOS 앱에 적합한 딥링킹 전략을 선택하는 데 도움을 줍니다.

구현 세부 사항은 [딥링킹을]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift) 참조하십시오. 문제 해결을 위해서는 [딥링킹 문제 해결을]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) 참조하십시오.

## 링크 유형 선택

iOS 앱에서 Braze 메시지의 링크를 처리하는 방법은 세 가지입니다. 각각의 방식은 서로 다르게 작동하며, 서로 다른 채널과 사용 사례에 적합합니다.

| 링크 유형 | 예시 | Best for | 앱이 설치되지 않은 상태에서도 열리나요? |
|---|---|---|---|
| **커스텀 구성표** | `myapp://products/123` | 푸시 알림, 인앱 메시지, 콘텐츠 카드 | 아니요 — 링크 오류 |
| **유니버설 링크** | `https://myapp.com/products/123` | 이메일, SMS, 클릭 추적 기능이 있는 채널 | 예 — 웹으로 대체됩니다 |
| **앱에서 웹 URL 열기** | 어떤`https://`URL | 모달 WebView에서 웹 콘텐츠 표시 | 해당 없음 — WebView에 표시됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 커스텀 구성 딥링크

커스텀 스킴 딥링크(예: `myapp://products/123`)는 앱을 특정 화면으로 직접 엽니다. 제3자에 의해 링크가 수정되지 않는 채널에 대한 가장 간단한 옵션입니다.

**다음과 같은 경우 커스텀 스킴 딥링크를 사용하십시오:**
- 푸시 알림, 인앱 메시지 또는 콘텐츠 카드 전송
- 앱이 설치되어 있지 않으면 링크가 작동할 필요가 없습니다
- 클릭 추적(이메일 서비스 공급자 링크 래핑)이 필요하지 않습니다.

**다음과 같은 경우에는 커스텀 스킴 딥링크를 사용하지 마십시오:**
- 이메일 발송 — 이메일 서비스 공급자는 클릭 추적을 위해 링크를 감싸는데, 이로 인해 커스텀 스키마가 깨집니다.
- 앱이 설치되지 않은 경우 웹 페이지로 돌아갈 수 있는 링크가 필요합니다.

### 유니버설 링크

유니버설 링크(예: `https://myapp.com/products/123`)는 iOS가 브라우저에서 열지 않고 앱으로 연결할 수 있는 표준 HTTPS URL입니다. 서버 측 구성(AASA 파일)과 앱 측 설정(연동 도메인 권한 부여)이 필요합니다.

**다음과 같은 경우에 유니버설 링크를 사용하세요:**
- 이메일 발송 중. 귀사의 이메일 서비스 공급자는 클릭 추적을 위해 링크를 감싸므로, 링크는 반드시 HTTPS여야 합니다.
- 링크가 감싸지거나 단축되는 SMS 또는 기타 채널을 통해 전송.
- 앱이 설치되지 않았을 때 웹 페이지로 돌아갈 수 있는 링크가 필요합니다.
- 귀사는 Branch 또는 Appsflyer와 같은 제3자 링크 제공업체를 사용하고 있습니다.

**다음과 같은 경우에는 유니버설 링크를 사용하지 마십시오:**
- 푸시 알림, 인앱 메시지 또는 콘텐츠 카드에서만 딥링크가 필요합니다. 커스텀 구성은 더 간단합니다.

### 앱 내에서 웹 URL 열기

이 옵션은 앱 내에서 모달 WebView 안에 웹 페이지를 엽니다. Braze 소프트웨어 개발 키트가 완전히 처리합니다.`Braze.WebViewController`— URL 처리 코드를 직접 작성할 필요가 없습니다.

**다음과 같은 경우에 "앱 내에서 웹 URL 열기"를 사용하세요:**
- 앱을 벗어나지 않고도 웹 페이지(예: 프로모션이나 기사)를 표시하고 싶습니다.
- 해당 URL은 특정 앱 화면으로의 딥링크가 아닌 표준 HTTPS 웹 페이지입니다.

**다음과 같은 경우에는 "앱 내에서 웹 URL 열기"를 사용하지 마십시오:**
- 앱에서 특정 보기로 이동해야 합니다. 대신 커스텀 스킴이나 유니버설 링크를 사용하세요.
- 해당 웹 페이지는 인증이 필요하거나 임베딩을 차단하는 콘텐츠 보안 정책 헤더를 가지고 있습니다.

## 각 링크 유형에 필요한 사항

### 커스텀 구성 딥링크

| Requirement | 세부 정보 |
|---|---|
| AASA 파일 | 필요하지 않음 |
| `Info.plist` | 귀하의 계획을 아래에 등록하고`CFBundleURLTypes` 추가하십시오 `LSApplicationQueriesSchemes` |
| 앱 델리게이트 메서드 | URL을 구문 분석하고 `application(_:open:options:)`이동하도록 구현 |
| Braze 소프트웨어 개발 키트 구성 | 없음 — 소프트웨어 개발 키트는 기본값으로 커스텀 스킴 URL을 엽니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 유니버설 링크

| Requirement | 세부 정보 |
|---|---|
| AASA 파일 | 필요 사항 — 호스트 `https://yourdomain.com/.well-known/apple-app-site-association` |
| 관련 도메인 | Xcode의 **'서명'** `applinks:yourdomain.com`아래에 **&'기능'을** 추가하세요 |
| 앱 델리게이트 메서드 | 처리하기 위해 `application(_:continue:restorationHandler:)`구현하다 `NSUserActivity` |
| Braze 소프트웨어 개발 키트 구성 | 설정 `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (선택 사항) | 커스텀 라우팅 구현`braze(_:shouldOpenURL:)` (예: Branch) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze를 통해 이메일을 발송할 경우, 귀하의 이메일 서비스 공급자(SendGrid, SparkPost 또는 Amazon SES)는 링크를 클릭 추적 도메인으로 감쌉니다. AASA 파일은 기본 도메인뿐만 아니라 클릭 추적 도메인에도 반드시 호스팅해야 합니다. 전체 설정 방법은 [유니버설 링크 및 앱 링크를]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/) 참조하십시오.
{% endalert %}

### 앱 내에서 웹 URL 열기

| Requirement | 세부 정보 |
|---|---|
| AASA 파일 | 필요하지 않음 |
| 앱 델리게이트 메서드 | 필요 없음 — 소프트웨어 개발 키트가 자동으로 처리합니다 |
| Braze 소프트웨어 개발 키트 구성 | 없음 — 캠페인 작성기에서 **'앱 내에서 웹 URL 열기'** 선택 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## AASA 파일이 필요할 때 {#when-aasa}

애플 앱 사이트 연결(AASA) 파일은 **유니버설 링크를** 사용할 때만 필요합니다. 앱이 처리할 수 있는 URL을 iOS에 알려줍니다.

다음과 같은 경우 AASA 파일이 필요합니다:

- 이메일 캠페인에서 딥링크를 전송합니다(이메일 서비스 공급자가 링크를 HTTPS 클릭 추적 URL로 감싸기 때문입니다).
- SMS 캠페인에서 딥링크를 전송합니다(링크가 HTTPS URL로 단축될 수 있기 때문입니다).
- 귀사는 Branch, Appsflyer 또는 다른 연결 제공업체를 사용합니다(해당 업체들이 자체 HTTPS 도메인을 사용하기 때문입니다).
- 푸시 알림, 인앱 메시지 또는 콘텐츠 카드(덜 흔하지만 가능`forwardUniversalLinks = true`)에서 유니버설 링크를 사용합니다.

다음과 같은 경우에는 AASA 파일이 필요하지 않습니다:

- 커스텀 스킴 딥링크(예: `myapp://`)는 푸시 알림, 인앱 메시지 또는 콘텐츠 카드에서만 사용됩니다.
- **앱 내에서 웹 URL 열기** 옵션을 사용합니다.

AASA 설정 방법에 대해서는 [유니버설 링크 및 앱 링크를]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links) 참조하십시오.

## 앱 코드가 링크를 처리해야 할 때 {#when-app-code}

사용하는 링크 유형에 따라 구현할 위임자 메서드가 달라집니다:

| 위임 메서드 | 핸들 | 언제 구현할 것인가 |
|---|---|---|
| `application(_:open:options:)` | 커스텀 구성표 딥링크 (`myapp://`) | 모든 채널에서 커스텀 스킴 딥링크를 사용합니다 |
| `application(_:continue:restorationHandler:)` | 유니버설 링크 (`https://`) | 이메일, SMS 또는 `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | 소프트웨어 개발 키트로 열려진 모든 URL | 커스텀 라우팅 로직이 필요합니다(예: 분기, 조건 로직, 분석). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Branch와 같은 제3자 링크 제공업체를 사용하는 경우, URL을 가로채어 해당 제공업체의 소프트웨어 개발 키트로 전달하도록 `BrazeDelegate.braze(_:shouldOpenURL:)`구현하십시오. [딥링킹에]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) [대한]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) 완전한 예제는 [Branch를]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) 참조하십시오.
{% endalert %}

## Braze와 함께 브랜치 사용하기 {#branch}

[Branch를]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) 링크 제공자로 사용하는 경우, 표준 유니버설 링크 설정 외에도 몇 가지 추가 단계가 필요합니다:

1. **브랜치 소프트웨어 개발 키트**: [Branch의 설명서에](https://help.branch.io/developers-hub/docs/native-sdks-overview) 따라 Branch 소프트웨어 개발 키트를 통합하십시오.
2. **관련 도메인**: Xcode의 **서명&기능**(**Signing Capabilities)** 아래에 브랜치 도메인(예: `applinks:yourapp.app.link`)을 추가하세요.
3. **브레이즈 델리게이트**: 브랜치 링크를 Braze가 직접 처리하도록 두지 않고 브랜치 소프트웨어 개발 키트로 라우팅하도록`braze(_:shouldOpenURL:)` 구현하십시오.
4. **전환형 유니버설 링크**: Braze 소프트웨어 개발 키트 `configuration.forwardUniversalLinks = true`구성에서 설정하십시오.

구현 세부 사항 및 디버깅 안내는 [딥링킹용 브랜치를]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) 참조하십시오.