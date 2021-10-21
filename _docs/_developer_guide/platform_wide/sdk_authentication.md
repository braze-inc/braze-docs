---
nav_title: SDK Authentication
article_title: SDK Authentication
page_order: 5
description: "This reference article covers SDK authentication and how to enable this feature in the Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# SDK authentication

SDK Authentication allows you to supply cryptographic proof (generated server-side) to SDK requests made on behalf of logged-in users. When this feature is enabled in your app, the Braze dashboard can be configured to reject requests with a missing or invalid JWT signature.

When enabled, this feature will prevent unauthorized requests that use your app's SDK API Key for logged in users, including:
- Sending custom events, attributes, purchases, and session data
- Creating new users in your Braze App Group
- Updating standard user profile attributes
- Receiving or triggering messages

{% alert important %}
To enable this feature, please contact our support team or your customer success manager.
{% endalert %}

## Getting started

There are four high-level steps to get started:

1. [Server-Side Integration][1] - Generate a public and private key-pair, and use your private key to create a JWT (_JSON Web Token_) for the current logged-in user.<br><br>
2. [SDK Integration][2] - Enable this feature in the Braze SDK and request the JWT Token generated from your server.<br><br>
3. [Adding Public Keys][3] - Add your _public key_ to the Braze dashboard in the "Manage Settings" page.<br><br>
4. [Toggle Enforcement within the Braze Dashboard][4] - Toggle this feature's enforcement within the Braze dashboard on an app-by-app basis.

## Server-Side Integration {#server-side-integration}

### Generate a public/private key-pair {#generate-keys}

Generate an RSA public/private key-pair. The Public Key will eventually be added to the Braze dashboard, while the Private Key should be stored securely on your server.

We recommend an RSA Key with 2048 bits for use with the RS256 JWT algorithm.

{% alert warning %}
Remember to keep your private keys _private_. Never expose or hard-code your private key in your app or website. Anyone who knows your private key can impersonate or create users on behalf of your application.
{% endalert %}

### Create a json web token for the current user {#create-jwt}

Once you have your private key, your server-side application should use it to return a JWT to your app or website for the currently logged-in user.

Typically, this logic could go wherever your app would normally request the current user's profile; such as a login endpoint or wherever your app refreshes the current user's profile.

When generating the JWT, the following fields are expected:

**JWT Header**

| Field | Required | Description                         |
| ----- | -------- | ----------------------------------- |
| `alg` | **Yes**  | The supported algorithm is `RS256`. |
| `typ` | **Yes**  | The type should equal `JWT`.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**JWT Payload**

| Field | Required | Description                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | **Yes**  | The "subject" should equal the User ID you supply Braze SDKs when calling `changeUser` |
| `exp` | **Yes**  | The "expiration" of when you want this token to expire.                                |
| `aud` | No       | The "audience" claim is optional, and if set should equal `braze`                      |
| `iss` | No       | The "issuer" claim is optional, and if set should equal your SDK API Key.              |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### JWT libraries

To learn more about JSON Web Tokens, or to browse the [many open source libraries](https://jwt.io/#libraries-io) that simplify this signing process, check out [https://jwt.io](https://jwt.io).

## SDK integration {#sdk-integration}

This feature is available as of the following [SDK versions]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions web:3.3.0 ios:4.3.0 android:14.0.0 %}

### Enable this feature in the braze sdk.

When this feature is enabled, the Braze SDK will append the current user's last known JWT to network requests made to Braze Servers.

{% alert note %}
Don't worry, initializing with this option alone won't impact data collection in any way, until you start [enforcing authentication](#braze-dashboard) within the Braze dashboard.
{% endalert %}

{% tabs %}
{% tab Javascript %}
When calling `initialize`, set the optional `sdkAuthentication` property to `true`.
```javascript
import braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
When configuring the Appboy instance, call `setIsSdkAuthenticationEnabled` to `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% tab KOTLIN %}
When configuring the Appboy instance, call `setIsSdkAuthenticationEnabled` to `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}
{% tab Objective-C %}
To enable SDK Authentication, add the key `EnableSDKAuthentication` to the `Braze` dictionary in your `.plist` file and set it to true.

Alternatively, you can enable SDK Authentication when initializing the SDK:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
            inApplication:application
        withLaunchOptions:launchOptions
        withAppboyOptions:@{ABKEnableSDKAuthenticationKey : @YES}];
```
{% endtab %}
{% tab Swift %}
To enable SDK Authentication, add the key `EnableSDKAuthentication` to the `Braze` dictionary in your `.plist` file and set it to true.

Alternatively, you can enable SDK Authentication when initializing the SDK:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableSDKAuthenticationKey : true ])
```
{% endtab %}
{% endtabs %}

### Set the current user's jwt token

Whenever your app calls the Braze `changeUser` method, also supply the JWT token that was [generated server-side][4].

You can also update the token to refresh the token mid-session for the current user.

{% alert note %}
Keep in mind that `changeUser` should only be called when the User ID has _actually changed_. You should not use this method as a way to update the signature if the user ID has not changed.
{% endalert %}

{% tabs %}
{% tab Javascript %}
Supply the JWT Token when calling `changeUser`:

```javascript
import braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```javascript
import braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Supply the JWT Token when calling `appboy.changeUser`:

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Supply the JWT Token when calling `appboy.changeUser`:

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

Or, when you have refreshed the user's token mid-session:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Supply the JWT Token when calling `changeUser`:

```objc
[[Appboy sharedInstance] changeUser:@"userId" sdkAuthSignature:@"signature"];
```

Or, when you have refreshed the user's token mid-session:

```objc
[[Appboy sharedInstance] setSdkAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab Swift %}

Supply the JWT Token when calling `changeUser`:

```swift
Appboy.sharedInstance()?.changeUser("userId", sdkAuthSignature: "signature")
```
Or, when you have refreshed the user's token mid-session:

```swift
Appboy.sharedInstance()?.setSdkAuthenticationSignature("signature")
```
{% endtab %}
{% endtabs %}

### Register a callback function for invalid tokens {#sdk-callback}

When this feature is set as ["Required"](#enforcement-options), the following scenarios will cause SDK requests to be rejected by Braze:
- JWT was expired by the time is was received by the Braze API
- JWT was empty or missing
- JWT failed to verify for the Public Keys you uploaded to the Braze dashboard

When the SDK requests fail for one of these reasons, a callback function you supply will be invoked with a relevant [Error Code][9]. Failed requests will periodically be retried until your app supplies a new valid JWT.

This callback includes the User ID for which the request failed, the relevant [Error Code][9], and the failed signature. If _that user_ is still logged in, you can use this callback as an opportunity to request a new JWT from your server and supply Braze's SDK with this new valid token.

{% alert tip %}
These callback methods are a great place to add your own monitoring or error-logging service to keep track of how often your Braze requests are being rejected.
{% endalert %}

{% tabs %}
{% tab Javascript %}
```javascript
import braze from "@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((authFailure) => {
  // TODO: optionally log to your error-reporting service
  // TODO: check if the errorEvent user matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(errorEvent);
  appboy.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(errorEvent -> {
    // TODO: optionally log to your error-reporting service
    // TODO: check if the errorEvent user matches the currently logged-in user
    String newToken = getNewTokenSomehow(errorEvent);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ errorEvent: BrazeSdkAuthenticationErrorEvent ->
    // TODO: optionally log to your error-reporting service
    // TODO: check if the errorEvent user matches the currently logged-in user
    val newToken: String = getNewTokenSomehow(errorEvent)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}
```objc
[[Appboy sharedInstance] setSdkAuthenticationDelegate:delegate];

// Method to implement in delegate
- (void)handleSdkAuthenticationError:(ABKSdkAuthenticationError *)errorEvent {
  // TODO: optionally log to your error-reporting service
  // TODO: check if the errorEvent user matches the currently logged-in user
  NSLog(@"Invalid SDK Authentication signature.");
  NSString *newSignature = getNewSignatureSomehow(errorEvent);
  [[Appboy sharedInstance] setSdkAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}
```swift
Appboy.sharedInstance()?.setSdkAuthenticationDelegate(delegate)

// Method to implement in delegate
func handle(_ errorEvent: ABKSdkAuthenticationError?) {
        // TODO: optionally log to your error-reporting service
        // TODO: check if the errorEvent user matches the currently logged-in user
        print("Invalid SDK Authentication signature.")
        let newSignature = getNewSignatureSomehow(errorEvent)
        Appboy.sharedInstance()?.setSdkAuthenticationSignature(newSignature)
    }
```
{% endtab %}
{% endtabs %}

The `errorEvent` argument passed to this callback will contain the following information:

| Property | Description |
| -------- | ----------- |
| `reason` | A description of why the request failed. |
| `error_code` | An internal error code used by Braze. |
| `user_id` | The user ID from which the request failed. |
| `signature` | The JWT that failed.|
{: .reset-td-br-1 .reset-td-br-2}

## Adding public keys {#key-management}

In the "Manage Settings" page of the dashboard, add your Public Key to a specific app in the Braze dashboard. Each app supports up to 3 Public Keys. Note that the same Public/Private keys may be used across apps.

To add a Public Key:
1. Choose the app in the left-hand side menu
2. Click the **Add Public Key** button within the SDK Authentication settings
3. Paste in the Public Key, and add an optional description
4. After saving your changes, the key will appear in the list of Public Keys.

To delete a key, or to promote a key to the Primary key, choose the corresponding action in the overflow menu next to each key.

## Enabling in the braze dashboard {#braze-dashboard}

Once your [Server-side Integration][1] and [SDK Integration][2] are complete, you can begin to enable this feature for those specific apps.

Keep in mind, SDK requests will continue to flow as usual - without authentication - _unless_ the app's SDK Authentication setting is switched to **required** in the Braze dashboard.

Should anything go wrong with your integration (i.e. your app is incorrectly passing tokens to the SDK, or your server is generating invalid tokens), simply **disable** this feature in the Braze dashboard and data will resume to flow as usual, without verification.

### Enforcement options {#enforcement-options}

In the dashboard `Settings` page, each app has three SDK Authentication states which control how Braze verifies requests.

| Setting| Description|
| ------ | ---------- |
| **Disabled** | Braze will not verify the JWT supplied for a user. (Default Setting)|
| **Optional** | Braze will verify requests for logged-in users, but will not reject invalid requests. |
| **Required** | Braze will verify requests for logged-in users and will reject invalid JWTs.|
{: .reset-td-br-1 .reset-td-br-2}

![dashboard][8]

The "**Optional**" setting is a useful way to monitor the potential impact this feature will have on your app's SDK traffic.

Invalid JWT signatures will be reported in both **Optional** and **Required** states, however only the **Required** state will reject SDK requests causing apps to retry and request new signatures.

## Analytics {#analytics}

Each app will show a breakdown of SDK Authentication errors collected while this feature is in the **Optional** and **Required** state.

Data is available in real-time, and you can hover over points in the chart to see a breakdown of errors for a given date.

![analytics][10]

## Error codes {#error-codes}

| Error Code| Error Reason | Description |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Expiration is a required field for Braze usage.|
| 20 | `DECODING_ERROR` | Non-matching public key or a general uncaught error.|
| 21 | `SUBJECT_MISMATCH` | The expected and actual subjects are not the same.|
| 22 | `EXPIRED` | The token provided has expired.|
| 23 | `INVALID_PAYLOAD` | The token payload is invalid.|
| 24 | `INCORRECT_ALGORITHM` | The algorithm of the token is not supported.|
| 25 | `PUBLIC_KEY_ERROR` | The public key could not be converted into the proper format.|
| 26 | `MISSING_TOKEN` | No token was provided in the request.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | No public keys matched the provided token.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Not all user ids in the request payload match as is required.|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## Frequently asked questions {#faq}

#### Can i use this feature on only some of my apps? {#faq-app-by-app}

Yes, this feature can be enabled for specific apps and doesn't need to be used on all of your apps.

#### What happens to users who are still on older versions of my app? {#faq-sdk-backward-compatibility}

When you begin to enforce this feature, requests made by older app versions will be rejected by Braze and retried by the SDKs. Once users upgrade their app to a supported version, those enqueued requests will begin to be accepted again.

If possible, you should push users to upgrade as you would for any other mandatory upgrade. Alternatively, you can keep the feature ["optional"][6] until you see that an acceptable percentage of users have upgraded.

#### What expiration should i use when generating jwt tokens? {#faq-expiration}

We recommend using the higher value of: average session duration, session cookie/token expiration, or the frequency at which your application would otherwise refresh the current user's profile.

#### What happens if a jwt expires in the middle of a user's session? {#faq-jwt-expiration}

Should a user's token expire mid-session, the SDK has a [callback function][7] it will invoke to let your app know that a new JWT token is needed to continue sending data to Braze.

#### What happens if my server-side integration breaks and i can no longer create a jwt? {#faq-server-downtime}

If your server is not able to provide JWT tokens or you notice some integration issue, you can always disable the feature in the Braze dashboard.

Once disabled, any pending failed SDK requests will eventually be retried by the SDK and accepted by Braze.

#### Why does this feature use public/private keys instead of shared secrets? {#faq-shared-secrets}

When using Shared Secrets, anyone with access to that shared secret (i.e. the Braze dashboard page) would be able to generate tokens and impersonate your end-users.

Instead, we use Public/Private Keys so that not even Braze Employees (let alone your dashboard users) have access to your Private Keys.

#### How will rejected requests be retried? {#faq-retry-logic}

When a request is rejected because of an authentication error, the SDKs will invoke a your callback used to refresh the user's JWT signature. 

Requests will retry periodically using an exponential backoff approach. After 50 consecutive failed attempts, retries will be paused until the next session start. Each SDK also has a method to manually request a data flush.

[1]: #server-side-integration
[2]: #sdk-integration
[3]: #key-management
[4]: #braze-dashboard
[5]: #create-jwt
[6]: #enforcement-options
[7]: #sdk-callback
[8]: {% image_buster /assets/img/sdk-auth-settings.png %}
[9]: #error-codes
[10]: {% image_buster /assets/img/sdk-auth-analytics.png %}
