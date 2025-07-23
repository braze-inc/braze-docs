{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### 자산 로딩 문제 해결(`NSURLError` 코드 `-1008`)

Braze를 서드파티 네트워크 로깅 라이브러리와 통합할 때 개발자는 일반적으로 도메인 코드 `-1008`과 관련된 `NSURLError`에 직면할 수 있습니다. 이 오류는 이미지 및 글꼴과 같은 자산을 검색할 수 없거나 캐시하는 데 실패했음을 나타냅니다. 이러한 경우를 해결하려면 이러한 라이브러리에서 무시해야 하는 도메인 목록에 Braze CDN URL을 등록해야 합니다.

#### 도메인

CDN 도메인의 전체 목록은 아래와 같습니다:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### 예시

다음은 Braze 에셋 캐싱과 충돌하는 것으로 알려진 라이브러리와 문제 해결을 위한 예제 코드입니다. 프로젝트에서 사용 불가능한 리소스 오류를 발생시키고 아래에 나열되지 않은 라이브러리를 사용하는 경우, 유사한 사용 API와 관련하여 해당 라이브러리의 설명서를 참조하세요.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### NetGuard

{% tabs %}
{% tab Swift %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XNLogger

{% tabs %}
{% tab Swift %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab Objective-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}


