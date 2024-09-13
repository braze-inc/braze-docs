---
nav_title: 문제 해결
article_title: iOS용 인앱 메시징 문제 해결
platform: Swift
page_order: 6
description: "이 참조 문서에서는 Swift 소프트웨어 개발 키트의 잠재적인 iOS 인앱 메시지 문제 해결 주제를 다룹니다."
channel:
  - in-app messages

---

# 문제 해결

> 이 참조 문서는 잠재적인 iOS 인앱 메시지 문제 해결 주제를 다룹니다.

## 노출 횟수

### 노출 횟수 or 클릭 분석 aren't being logged

인앱 메시지 표시 또는 클릭 작업을 수동으로 처리하도록 인앱 메시지 대리자를 설정한 경우, 인앱 메시지에 대한 [클릭](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) 및 [노출](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))을(를) 수동으로 기록해야 합니다.

### 인상은 예상보다 낮습니다

트리거는 세션 시작 시 기기에 동기화하는 데 시간이 걸리므로 사용자가 세션을 시작한 직후 이벤트를 기록하거나 구매하면 경합 조건이 발생할 수 있습니다. 잠재적인 해결 방법 중 하나는 캠페인을 세션 시작 시 트리거하도록 변경한 다음, 의도한 이벤트 또는 구매를 분할하는 것입니다. 이벤트가 발생한 후 다음 세션 시작 시 인앱 메시지가 전달됩니다.

## 예상된 인앱 메시지가 표시되지 않았습니다

대부분의 인앱 메시지 문제는 전달 및 디스플레이의 두 가지 주요 범주로 나눌 수 있습니다. 예상된 인앱 메시지가 기기에 표시되지 않은 이유를 해결하려면 먼저 인앱 메시지가 기기]\[iam_11]에 전달되었는지 확인한 다음 메시지 표시 문제를 해결하십시오]\[iam_12].

### 문제 해결 인앱 메시지 전달 {#troubleshooting-in-app-message-delivery}

소프트웨어 개발 키트는 세션 시작 시 Braze 서버에서 인앱 메시지를 요청합니다. 기기에서 인앱 메시지가 전달되는지 확인하려면 SDK에서 인앱 메시지를 요청하고 Braze 서버에서 반환되는지 확인해야 합니다.

#### 메시지가 요청되고 반환되는지 확인하십시오

1. 대시보드에서 \[테스트 사용자]\[iam_1]로 자신을 추가하세요.
2. 사용자를 대상으로 인앱 메시지 캠페인을 설정하세요.
3. 응용 프로그램에서 새 세션이 발생하도록 하십시오.
4. \[이벤트 사용자 로그]\[iam_3]를 사용하여 기기가 세션 시작 시 인앱 메시지를 요청하는지 확인하세요. 테스트 사용자의 세션 시작 이벤트와 관련된 소프트웨어 개발 키트 요청을 찾으십시오.
  - 앱이 인앱 메시지를 요청하도록 설계된 경우 `trigger`이(가) **요청된 응답** 필드의 **응답 데이터** 아래에 표시되어야 합니다.
  - 앱이 원래 인앱 메시지를 요청하도록 설계되었다면, **요청된 응답** 필드의 **응답 데이터** 아래에 `in_app`이(가) 표시되어야 합니다.
5. \[이벤트 사용자 로그]\[iam_3]를 사용하여 응답 데이터에서 올바른 인앱 메시지가 반환되는지 확인하십시오.<br>![]\[iam_5]

#### 요청되지 않은 메시지

앱 내 메시지가 요청되지 않는 경우 앱이 세션을 올바르게 추적하지 않을 수 있습니다. 앱 내 메시지는 세션 시작 시 새로 고쳐집니다. 또한 앱의 세션 시간 초과 의미에 따라 앱이 실제로 세션을 시작하고 있는지 확인하십시오:

![이벤트 사용자 로그에서 성공적인 세션 시작 이벤트를 표시하는 소프트웨어 개발 키트 요청을 찾았습니다.]\[iam_10]

#### 메시지가 반환되지 않음

앱 내 메시지가 반환되지 않는 경우 캠페인 타겟팅 문제일 가능성이 큽니다.

##### 귀하의 세그먼트에는 귀하의 사용자가 포함되어 있지 않습니다
사용자의 \[\*\*참여**]\[iam_6] 탭에서 올바른 세그먼트가 **세그먼트** 아래에 나타나는지 확인하세요.

##### 사용자는 이전에 인앱 메시지를 받았으며 다시 받을 자격이 없었습니다
\[캠페인 재적격성 설정]\[iam_7] 전달** 단계의 캠페인 작성기**에서 재적격성 설정이 테스트 설정과 일치하는지 확인하십시오.

##### 귀하의 사용자가 캠페인에 대한 빈도 한도에 도달했습니다
캠페인 \[빈도 제한 설정]\[iam_8] 및 테스트 설정과 일치하는지 확인하세요.

##### 사용자가 대조군에서 벗어났습니다
캠페인에 대조군이 있었다면 사용자가 대조군에 속했을 수 있습니다. 이것이 발생했는지 확인하려면 수신된 캠페인 배리언트 필터가 있는 세그먼트를 생성하고, 캠페인 배리언트를 **Control**로 설정하고 사용자가 해당 세그먼트에 포함되었는지 확인할 수 있습니다. 

통합 테스트 목적으로 캠페인을 생성할 때 대조군 추가를 선택하지 마십시오.

### 문제 해결 인앱 메시지 표시 {#troubleshooting-in-app-message-display}

앱이 성공적으로 인앱 메시지를 요청하고 수신하고 있지만 표시되지 않는 경우, 일부 기기 측 로직이 표시를 방해할 수 있습니다:

- 트리거된 인앱 메시지는 트리거 사이의 [최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
- 사용자 지정 인앱 메시지 처리를 위해 대리자를 설정한 경우, 대리자가 인앱 메시지 표시를 방해하지 않는지 확인하십시오.
- 이미지 다운로드 실패는 이미지가 포함된 앱 내 메시지 표시를 방해합니다. 기기 로그를 확인하여 이미지 다운로드가 실패하지 않았는지 확인하십시오.
- 기기 방향이 인앱 메시지에 지정된 방향과 일치하지 않으면 인앱 메시지가 표시되지 않습니다. 기기가 올바른 방향에 있는지 확인하십시오.

### 문제 해결 자산 로딩 (`NSURLError` 코드 `-1008`)

Braze를 타사 네트워크 로깅 라이브러리와 통합할 때 개발자는 일반적으로 도메인 코드 `-1008`와 관련된 `NSURLError`에 직면할 수 있습니다. 이 오류는 이미지 및 글꼴과 같은 자산을 검색할 수 없거나 캐시하는 데 실패했음을 나타냅니다. 이러한 경우를 해결하려면 Braze의 CDN URL을 무시해야 하는 도메인 목록에 등록해야 합니다.

#### 도메인

CDN 도메인의 전체 목록은 아래와 같습니다:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### 예시

다음은 Braze의 자산 캐싱과 충돌하는 것으로 알려진 라이브러리와 문제를 해결하기 위한 예제 코드입니다. 프로젝트에서 사용 중인 라이브러리가 사용 불가능한 리소스 오류를 발생시키고 아래에 나열되지 않은 경우, 해당 라이브러리의 설명서를 참조하여 유사한 사용 API를 확인하십시오.

##### 넷폭스

{% tabs %}
{% tab 스위프트 %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab 오브젝티브-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### 넷가드

{% tabs %}
{% tab 스위프트 %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab 오브젝티브-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XN로거

{% tabs %}
{% tab 스위프트 %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab 오브젝티브-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}

\[iam_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
\[iam_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[iam_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[iam_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
\[iam_6]: {{ site.baseurl }}/user_guide/참여_tools/segments/user_profiles/#engagement-tab
\[iam_7]: {{ site.baseurl }}/user_guide/참여_tools/campaigns/building_campaigns/delivery_types/reeligibility/]
\[iam_8]: {{ site.baseurl }}/user_guide/참여_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
\[iam_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
\[iam_11]: #문제 해결-앱-메시지-전달
\[iam_12]: #문제 해결-앱-메시지-디스플레이

