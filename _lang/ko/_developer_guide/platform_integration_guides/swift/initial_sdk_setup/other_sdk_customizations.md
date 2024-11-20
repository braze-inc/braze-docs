---
nav_title: 기타 SDK 사용자 지정
article_title: Swift를 위한 기타 SDK 사용자 지정
platform: Swift
description: "이 문서에서는 Braze Swift SDK를 구성하는 추가 단계를 다룹니다."
page_order: 3

---

# Swift를 위한 기타 SDK 사용자 지정

> Braze 인스턴스에 연결된 `Braze.Configuration` 객체의 멤버 속성을 수정하여 Braze Swift SDK를 구성할 수 있습니다. 구성은 `Braze(configuration:)`를 사용하여 Braze 인스턴스를 초기화하기 전에만 수행할 수 있습니다.

사용 가능한 구성의 전체 목록은 [Braze.Configuration 클래스 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class)를 참조하세요.

## 브레이즈 로그 레벨

Braze Swift SDK의 기본 로그 수준은 다음 차트에서 `.error`입니다. 이 수준은 완전히 비활성화된 로깅 위의 최소 수준입니다.

사용 가능한 로그 수준은 다음 목록을 참조하세요:

| Swift       | Objective-C              | 설명                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | 로그 디버깅 정보 + `.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | 일반 SDK 정보(사용자 변경 사항 등) + `.error`를 기록합니다. |
| `.error`    | `BRZLoggerLevelError`    | 로그 오류.                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | 로깅이 발생하지 않습니다.                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 로그 수준 설정

로그 수준은 `Braze.Configuration` 객체에서 런타임에 할당할 수 있습니다:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab 목표-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

Braze 로거의 전체 사용법은 [로거 클래스 문서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class)를 참조하세요.

