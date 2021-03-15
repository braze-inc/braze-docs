## Session Tracking

The Braze SDK reports session data that is used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Based on the below session semantics, our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze Dashboard.

### Session Lifecycle

{% if include.platform == "iOS" %}A session is started when you call `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`, after which by default sessions start when the `UIApplicationWillEnterForegroundNotification` notification is fired (i.e. the app enters the foreground) and end when the app leaves the foreground (i.e. when the `UIApplicationDidEnterBackgroundNotification` notification is fired or when the app dies).

{% elsif include.platform == "Android" %}If you have integrated Braze using our recommended [Activity Lifecycle Callback Integration] [session_tracking_8], `openSession()` and `closeSession()` will be called automatically for each Activity in your app. By default, sessions on Android are opened upon the first call to `openSession()` and are closed after an app has been out of the foreground for longer than 10 seconds.  Note that calling `closeSession()` does not close a session immediately. Rather, it closes a session in 10 seconds if the user doesn't call `openSession()` (e.g., by navigating to another Activity) in the interim.

An Android session times out after 10 seconds without any communication from the host application. This means if a user backgrounds the app and returns 9 seconds later, the same session will be continued.

__Note:__ If a session closes while the user has the app backgrounded, that data may not be flushed to the server until the app is opened again.

{% elsif include.platform == "Web" %}By default, sessions begin when `appboy.openSession()` is first called and remain open until there are at least 30 minutes of inactivity. This means that if the user navigates away from the site and then returns less than 30 minutes later, the same session will be continued. If they return after the 30 minutes have expired, a "close session" datapoint is automatically generated for the time at which they navigated away, and a new session opens.

{% elsif include.platform == "Windows"%}Our Windows integration logs session opens when the app is launched and logs session closes when the application is closed.{% endif %}

**Note**: If you need to force a new session, you can do so by changing users.

{% if include.platform != "Windows" %}
### Customizing Session Timeout

{% if include.platform == "iOS" %}
Starting with Braze iOS SDK v3.14.1, you can set the session timeout using the Info.plist file. Add the `Appboy` dictionary to your Info.plist file. Inside the `Appboy` dictionary, add the `SessionTimeout` number subentry and set the value to your custom session timeout.

To customize the session timeout in versions prior to v3.14.1, set the [`ABKSessionTimeoutKey`][session_tracking_2] so that the value is a number of seconds in the Braze initialization method [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][session_tracking_1].

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.platform == "Android" %}To customize the session timeout, add [`com_appboy_session_timeout`][session_tracking_4] to your [`braze.xml`][session_tracking_3] file:

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open"
otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_appboy_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
``` {% endif %}

{% if include.platform == "Web" %}To customize the session timeout, pass the `sessionTimeoutInSeconds` option to your [`initialize`][session_tracking_5] function.

```js
// Sets the session timeout to 15 minutes instead of the default 30
appboy.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` {% endif %}

If you have set a session timeout, then the above session semantics all extend to that customized timeout.
{% endif %}

**Note**: The minimum value for `sessionTimeoutInSeconds` is 1 second.

### Testing Session Tracking

To detect sessions via your user, find your user on the dashboard and navigate to "App Usage" on the user profile. You can confirm that session tracking is working by checking that the "Sessions" metric increases when you would expect it to.

![test_session] [session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup
[session_tracking_2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L101
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
