## Disabling data tracking

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
To disable data-tracking activity on the Web SDK, use the method [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). This will sync any data logged before `disableSDK()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored.
{% endtab %}

{% tab google tag manager %}
Use the **Disable Tracking** or **Resume Tracking** tag type to disable or re-enable web tracking, respectively. These two options call [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) and [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Best practices

To provide users with the option to stop tracking, we recommend building a simple page with two links or buttons: one that calls `disableSDK()` when clicked, and another that calls `enableSDK()` to allow users to opt back in. You can use these controls to start or stop tracking via other data sub-processors as well.

{% alert note %}
The Braze SDK does not need to be initialized to call `disableSDK()`, allowing you to disable tracking for fully anonymous users. Conversely,`enableSDK()` does not initialize the Braze SDK so you must also call `initialize()` afterward to enable tracking.
{% endalert %}

## Resuming data tracking

To resume data collection, you can use the [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) method.
