사용자 정의 HTML 인앱 메시지 및 배너는 Braze SDK와 연동하기 위한 JavaScript "브릿지"를 지원하여, 사용자가 링크가 포함된 요소를 클릭하거나 콘텐츠와 참여할 때 커스텀 Braze 액션을 트리거할 수 있도록 합니다. 이러한 메서드는 전역 `brazeBridge` 또는 `appboyBridge` 변수와 함께 존재합니다.

{% alert important %}
Braze는 글로벌 `brazeBridge` 변수를 사용할 것을 권장합니다. 전역 `appboyBridge` 변수는 더 이상 사용되지 않지만 기존 사용자에게는 계속 작동합니다. `appboyBridge`를 사용 중인 경우 `brazeBridge`로 마이그레이션할 것을 권장합니다. <br><br> `appboyBridge`는 다음 SDK 버전에서 사용되지 않게 되었습니다.<br><br>
- 웹: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

예를 들어, 커스텀 속성과 커스텀 이벤트를 기록한 후 메시지를 닫으려면 커스텀 HTML 내에서 다음과 같은 JavaScript를 사용할 수 있습니다:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScript 브리지 메서드 {#bridge}

앱 내 메시지 및 배너용 커스텀 HTML 내에서 다음 JavaScript 메서드가 지원됩니다:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Liquid을(를) 삽입하기 위해 참조할 수 없습니다 <code>customAttributes</code> JavaScript 브리지 메서드로.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

### 버튼 클릭 추적

사용자 정의 HTML에서 클릭을 추적하려면  `brazeBridge.logClick(button_id)`메서드를 사용하십시오.

{% alert note %}
**배너:** 오직`brazeBridge.logClick()`(인수 없이)만 지원됩니다. 버튼 ID 및 커스텀 버튼 추적은 인앱 메시지에만 지원됩니다.
{% endalert %}

인앱 메시지의 경우, 각각 `brazeBridge.logClick()`,`brazeBridge.logClick('1')` , 를 사용하여 "버튼 1", "버튼 2", "본문 클릭"`brazeBridge.logClick('0')`을 프로그래밍 방식으로 추적할 수 있습니다.

| 클릭 수     | 방법                       | Supported |
| ---------- | ---------------------------- | --------- |
| 본문 클릭 | `brazeBridge.logClick()`    | 앱 내 메시지 및 배너 |
| 버튼 1   | `brazeBridge.logClick('0')` | 인앱 메시지만 |
| 버튼 2   | `brazeBridge.logClick('1')` | 인앱 메시지만 |
| 커스텀 버튼 추적 |`brazeBridge.logClick('your custom name here')`| 인앱 메시지만 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

인앱 메시지의 경우, 노출 횟수당 여러 버튼 클릭 이벤트를 추적할 수 있습니다. 예를 들어, 메시지를 닫고 버튼 2 클릭을 기록하려면:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

캠페인당 최대 100개의 고유한 이름까지 새 커스텀 버튼 이름을 추적할 수 있습니다. 예를 들어, `brazeBridge.logClick('blue button')` 또는 `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
속성`onclick` 내부에 JavaScript 메서드를 사용할 때는 HTML 속성의 이중 따옴표와 충돌을 피하기 위해 문자열 값을 작은따옴표로 묶어야 합니다.
{% endalert %}

#### 제한 사항 (인앱 메시지만 해당)

- 캠페인당 최대 100개의 고유 버튼 ID를 가질 수 있습니다.
- 버튼 ID는 각각 최대 255자의 문자를 가질 수 있습니다.
- 버튼 ID는 문자, 숫자, 공백, 대시 및 밑줄만 포함할 수 있습니다.
