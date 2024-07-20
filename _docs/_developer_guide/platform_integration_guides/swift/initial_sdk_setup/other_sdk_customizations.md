---
nav_title: Other SDK Customizations
article_title: Other SDK customizations for Swift
platform: Swift
description: "This document covers additional steps to configure the Braze Swift SDK."
page_order: 3

---

# Other SDK customizations for Swift

> The Braze Swift SDK can be configured by modifying the member properties of the `Braze.Configuration` object attached to your Braze instance. Note that configuration can only be done prior to initializing the Braze instance with `Braze(configuration:)`.

For a full list of available configurations, refer to the [Braze.Configuration class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

## Braze log level

The default log level for the Braze Swift SDK is `.error` in the following chart. This level is the most minimal level above fully disabled logging.

See the following list of available log levels:

| Swift       | Objective-C              | Description                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | Log debugging information + `.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | Log general SDK information (user changes, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Log errors.                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | No logging occurs.                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Setting log level

The log level can be assigned at runtime on your `Braze.Configuration` object:

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
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

For full usage of the Braze Logger, refer to the [Logger class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class
[2]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class
