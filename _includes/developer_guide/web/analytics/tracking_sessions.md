## Session lifecycle

By default, sessions begin when `braze.openSession()` is first called and remain open until at least 30 minutes of inactivity. This means that if the user navigates away from the site and returns less than 30 minutes later, the same session will continue. If they return after the 30 minutes have expired, a "close session" data point is automatically generated for the time they navigated away, and a new session opens.

{% alert note %}
If you need to force a new session, you can do so by changing users.
{% endalert %}

## Customizing session timeout

To customize the session timeout, pass the `sessionTimeoutInSeconds` option to your [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) function. The minimum value for `sessionTimeoutInSeconds` is 1 second.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

If you have set a session timeout, then the session semantics all extend to that customized timeout.

## Testing session tracking

To detect sessions via your user, find your user on the dashboard and navigate to **App Usage** on the user profile. You can confirm that session tracking is working by checking that the session metric increases when you would expect it to.

![A user profile component showing how many sessions have occurred, when the app was first used, and when it was last used.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%"}

