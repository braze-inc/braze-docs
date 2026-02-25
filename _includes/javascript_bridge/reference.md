In-app messages and Banners support a JavaScript "bridge" to interface with the Braze SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. These methods exist with the global `brazeBridge` or `appboyBridge` variable.

{% alert important %}
Braze recommends that you use the global `brazeBridge` variable. The global `appboyBridge` variable is deprecated but will continue to function for existing users. If you are using `appboyBridge`, we suggest you migrate to `brazeBridge`. <br><br> `appboyBridge` was deprecated in the following SDK versions:<br><br>
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

For example, to log a custom attribute and custom event, then close the message, you could use the following JavaScript within your custom HTML:

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

### JavaScript Bridge methods {#bridge}

The following JavaScript methods are supported within custom HTML for in-app messages and Banners:

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
You cannot reference Liquid to insert <code>customAttributes</code> into JavaScript Bridge methods.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

### Button click tracking

Use the `brazeBridge.logClick(button_id)` method to track clicks in your custom HTML. This allows you to programmatically track "Button 1", "Button 2", and "Body Clicks" using `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')`, or `brazeBridge.logClick()`, respectively.

| Clicks     | Method                       |
| ---------- | ---------------------------- |
| Button 1   | `brazeBridge.logClick('0')` |
| Button 2   | `brazeBridge.logClick('1')` |
| Body click | `brazeBridge.logClick()`    |
| Custom button tracking |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

You can track multiple button click events per impression. For example, to close a message and log a Button 2 click:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

You can also track new custom button names—up to 100 unique names per campaign. For example, `brazeBridge.logClick('blue button')` or `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
When using JavaScript methods inside an `onclick` attribute, wrap string values in single quotes to avoid conflicts with the double-quoted HTML attribute.
{% endalert %}

#### Limitations

- You can have up to 100 unique button IDs per campaign.
- Button IDs can have up to 255 characters each.
- Button IDs can only include letters, numbers, spaces, dashes, and underscores.
