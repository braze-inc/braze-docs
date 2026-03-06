---
page_order: 1.2
nav_title: Authentication
article_title: Set up authentication for the Braze SDK
description: "This reference article covers SDK authentication and how to enable this feature in the Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Set up SDK authentication

> SDK Authentication allows you to supply cryptographic proof (generated server-side) to SDK requests made on behalf of logged-in users.

## How it works

After you enable this feature in your app, you can configure the Braze dashboard to reject any requests with an invalid or missing JSON Web Token (JWT), which includes:

- Sending custom events, attributes, purchases, and session data
- Creating new users in your Braze workspace
- Updating standard user profile attributes
- Receiving or triggering messages

Now you can prevent unauthenticated logged-in users from using your app's SDK API key to perform malicious actions, such as impersonating your other users.

## Setting up authentication

### Step 1: Set up your server {#server-side-integration}

#### Step 1.1: Generate a public/private key-pair {#generate-keys}

Generate an RSA256 public/private key-pair. The public key will eventually be added to the Braze dashboard, while the private key should be stored securely on your server.

We recommend an RSA Key with 2048 bits for use with the RS256 JWT algorithm.

{% alert warning %}
Remember to keep your private keys _private_. Never expose or hard-code your private key in your app or website. Anyone who knows your private key can impersonate or create users on behalf of your application.
{% endalert %}

#### Step 1.2: Create a JSON Web Token for the current user {#create-jwt}

Once you have your private key, your server-side application should use it to return a JWT to your app or website for the currently logged-in user.

Typically, this logic could go wherever your app would normally request the current user's profile; such as a login endpoint or wherever your app refreshes the current user's profile.

When generating the JWT, the following fields are expected:

**JWT Header**

| Field | Required | Description                         |
| ----- | -------- | ----------------------------------- |
| `alg` | Yes  | The supported algorithm is `RS256`. |
| `typ` | Yes  | The type should equal `JWT`.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**JWT Payload**

| Field | Required | Description                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Yes  | The "subject" should equal the User ID you supply Braze SDK when calling `changeUser`  |
| `exp` | Yes | The "expiration" of when you want this token to expire.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
To learn more about JSON Web Tokens, or to browse the many open source libraries that simplify this signing process, check out [https://jwt.io](https://jwt.io).
{% endalert %}

### Step 2: Configure the SDK {#sdk-integration}

This feature is available as of the following [SDK versions]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
For iOS integrations, this page details the steps for the Braze Swift SDK. For sample usage in the legacy AppboyKit iOS SDK, reference [this file](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) and [this file](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m).
{% endalert %}

#### Step 2.1: Enable authentication in the Braze SDK.

When this feature is enabled, the Braze SDK will append the current user's last known JWT to network requests made to Braze Servers.

{% alert note %}
Don't worry, initializing with this option alone won't impact data collection in any way, until you start [enforcing authentication](#braze-dashboard) within the Braze dashboard.
{% endalert %}

{% tabs %}
{% tab Web %}
When calling `initialize`, set the optional `enableSdkAuthentication` property to `true`.
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
SDK Authentication must be enabled during native SDK initialization. Add the following configuration to your native iOS and Android code:

**iOS (AppDelegate.swift)**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

After enabling SDK Authentication in the native layer, you can use the React Native JavaScript methods shown in the following steps.
{% endtab %}
{% tab Java %}
When configuring the Braze instance, call `setIsSdkAuthenticationEnabled` to `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Alternatively, you can add `<bool name="com_braze_sdk_authentication_enabled">true</bool>` to your braze.xml.
{% endtab %}
{% tab KOTLIN %}
When configuring the Braze instance, call `setIsSdkAuthenticationEnabled` to `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Alternatively, you can add `<bool name="com_braze_sdk_authentication_enabled">true</bool>` to your braze.xml.
{% endtab %}
{% tab Objective-C %}
To enable SDK Authentication, set the `configuration.api.sdkAuthentication` property of your `BRZConfiguration` object to `YES` before initializing the Braze instance:

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
To enable SDK Authentication, set the `configuration.api.sdkAuthentication` property of your `Braze.Configuration` object to `true` when initializing the SDK:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Currently, SDK Authentication must be enabled as part of initializing the SDK in native iOS and Android code. To enable SDK Authentication in the Flutter SDK, follow the integrations for iOS and Android from the other tabs. After SDK Authentication is enabled, the rest of the feature can be integrated in Dart.
{% endtab %}
{% tab Flutter %}
SDK Authentication must be enabled as part of initializing the SDK in native iOS and Android code. When enabled in the native layer, you can use Flutter SDK methods to pass the JWT signature.

**iOS**

To enable SDK Authentication, set the `configuration.api.sdkAuthentication` property to `true` in your native iOS code:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

After enabling SDK Authentication in the native layer, you can use the Flutter SDK methods shown in the following steps.
{% endtab %}
{% tab Unity %}
SDK Authentication must be enabled during native SDK initialization. Add the following configuration to your native iOS and Android code:

**iOS**

Set the `SDKAuthenticationEnabled` property to `true` in your configuration file:

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

After enabling SDK Authentication in the native layer, you can use the Unity C# methods shown in the following steps.
{% endtab %}
{% tab Cordova %}
SDK Authentication must be enabled during native SDK initialization. Add the following configuration to your native iOS and Android code:

**iOS**

To enable SDK Authentication, set the `enableSDKAuthentication` property to `true` in your `config.xml`:

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

After enabling SDK Authentication in the native layer, you can use the Cordova JavaScript methods shown in the following steps.
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
SDK Authentication must be enabled during native SDK initialization. Configure SDK Authentication separately for iOS and Android:

**iOS**

To enable SDK Authentication, set the `configuration.Api.SdkAuthentication` property to `true` when initializing the SDK:

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

After enabling SDK Authentication, you can use the .NET MAUI methods shown in the following steps.
{% endtab %}
{% tab Expo %}
When using the Braze Expo plugin, set the `enableSdkAuthentication` property to `true` in your app configuration. This automatically configures SDK Authentication in the native iOS and Android layers without requiring manual native code changes.

**app.json or app.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

After enabling SDK Authentication in your app configuration, you can use the React Native JavaScript methods shown in the React Native tab for the following steps.

{% alert note %}
For a complete implementation example, see the [Braze Expo plugin sample app](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx) on GitHub.
{% endalert %}
{% endtab %}
{% endtabs %}

#### Step 2.2: Set the current user's JWT

Whenever your app calls the Braze `changeUser` method, also supply the JWT that was [generated server-side](#braze-dashboard).

You can also configure the token to refresh mid-session for the current user.

{% alert note %}
Keep in mind that `changeUser` should only be called when the User ID has _actually changed_. You should not use this method as a way to update the authentication token (JWT) if the user ID has not changed.
{% endalert %}

{% tabs %}
{% tab Web %}
Supply the JWT when calling [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

Supply the JWT when calling [`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser):

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Supply the JWT when calling [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Supply the JWT when calling [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

Or, when you have refreshed the user's token mid-session:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Supply the JWT when calling [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

Or, when you have refreshed the user's token mid-session:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

Supply the JWT when calling [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Or, when you have refreshed the user's token mid-session:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

Supply the JWT when calling [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Or, when you have refreshed the user's token mid-session:

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

Supply the JWT when calling `changeUser`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

Supply the JWT when calling `ChangeUser`:

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

Supply the JWT when calling `changeUser`:

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

Supply the JWT when calling `ChangeUser`:

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

When using the Braze Expo plugin, use the same React Native SDK methods. Supply the JWT when calling `changeUser`:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Or, when you have refreshed the user's token mid-session:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### Step 2.3: Register a callback function for invalid tokens {#sdk-callback}

When this feature is set as [Required](#enforcement-options), the following scenarios will cause SDK requests to be rejected by Braze:
- JWT was expired by the time is was received by the Braze API
- JWT was empty or missing
- JWT failed to verify for the public keys you uploaded to the Braze dashboard

You can use `subscribeToSdkAuthenticationFailures` to subscribe to be notified when the SDK requests fail for one of these reasons. A callback function contains an object with the relevant [`errorCode`](#error-codes), `reason` for the error, the `userId` of the request (the user cannot be anonymous), and the authentication token (JWT) that caused the error. 

Failed requests will periodically be retried until your app supplies a new valid JWT. If that user is still logged in, you can use this callback as an opportunity to request a new JWT from your server and supply the Braze SDK with this new valid token.

When you receive an authentication error, verify the `userId` in the error matches your currently logged-in user, then fetch a new signature from your server and provide it to the Braze SDK. You can also log these errors to your monitoring or error-reporting service.

{% alert tip %}
These callback methods are a great place to add your own monitoring or error-logging service to keep track of how often your Braze requests are being rejected.
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials
  
  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");
  
  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

Set the SDK authentication delegate in your native iOS implementation:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);
  
  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

Set the SDK authentication delegate on your `Braze` instance:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
When using the Braze Expo plugin, use the same React Native SDK methods:

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### Step 3: Enable authentication in the dashboard {#braze-dashboard}

Next, you can enable authentication in the Braze dashboard for the apps you set up previously.

Keep in mind that SDK requests will continue to flow as usual without authentication unless the app's SDK Authentication setting is set to **Required** in the Braze dashboard.

Should anything go wrong with your integration (for example, your app is incorrectly passing tokens to the SDK, or your server is generating invalid tokens), disable this feature in the Braze dashboard, and data will resume to flow as usual without verification.

#### Enforcement options {#enforcement-options}

In the dashboard **Manage Settings** page, each app has three SDK Authentication states which control how Braze verifies requests.

| Setting| Description|
| ------ | ---------- |
| **Disabled** | Braze will not verify the JWT supplied for a user. (Default Setting)|
| **Optional** | Braze will verify requests for logged-in users, but will not reject invalid requests. |
| **Required** | Braze will verify requests for logged-in users and will reject invalid JWTs.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

The **Optional** setting is a useful way to monitor the potential impact this feature will have on your app's SDK traffic.

An invalid JWT will be reported in both **Optional** and **Required** states, however only the **Required** state will reject SDK requests causing apps to retry and request a new JWT.

## Managing public keys {#key-management}

### Adding a public key

You can add up to three public keys for each app: a primary, a secondary, and a tertiary. You can also add the same key to more than one app if needed. To add a public key:

1. Go to the Braze dashboard and select **Settings** > **App Settings**.
2. Choose an app from your list of available apps.
3. Under **SDK Authentication**, select **Add Public Key**.
4. Enter an optional description, paste in your public key, then select **Add Public Key**.

### Assign a new primary key

To assign a secondary or tertiary key as your new primary key:

1. Go to the Braze dashboard and select **Settings** > **App Settings**.
2. Choose an app from your list of available apps.
3. Under **SDK Authentication**, choose a key and select **Manage** > **Make Primary Key**.

### Deleting a key

To delete a primary key, first [assign a new primary](#assign-a-new-primary-key), then delete your key. To delete a non-primary key:

1. Go to the Braze dashboard and select **Settings** > **App Settings**.
2. Choose an app from your list of available apps.
3. Under **SDK Authentication**, choose a non-primary key and select **Manage** > **Delete Public Key**.

## Analytics {#analytics}

Each app will show a breakdown of SDK Authentication errors collected while this feature is in the **Optional** and **Required** state.

Data is available in real-time, and you can hover over points in the chart to see a breakdown of errors for a given date.

![A chart showing the number of instances of authentication errors. Also shown are the total number of errors, error type, and adjustable date range.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Error codes {#error-codes}

| Error code| Error reason | Description | Steps to resolve |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Expiration is a required field for Braze usage.| Add an `exp` or expiration field to your JWT creation logic. |
| 20 | `DECODING_ERROR` | Non-matching public key or a general uncaught error.| Copy your JWT into a JWT testing tool to diagnose why your JWT is an invalid format. |
| 21 | `SUBJECT_MISMATCH` | The expected and actual subjects are not the same.| The `sub` field should be the same user ID passed to the `changeUser` SDK method. |
| 22 | `EXPIRED` | The token provided has expired.| Extend your expiration or periodically refresh tokens before they expire. |
| 23 | `INVALID_PAYLOAD` | The token payload is invalid.| Copy your JWT into a JWT testing tool to diagnose why your JWT is an invalid format. |
| 24 | `INCORRECT_ALGORITHM` | The algorithm of the token is not supported.| Change your JWT to use `RS256` encryption. Other types are not supported. |
| 25 | `PUBLIC_KEY_ERROR` | The public key could not be converted into the proper format.| Copy your JWT into a JWT testing tool to diagnose why your JWT is an invalid format. |
| 26 | `MISSING_TOKEN` | No token was provided in the request.| Make sure you are passing a token when calling `changeUser(id, token)` and that your token is not blank.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | No public keys matched the provided token.| The private key used in the JWT does not match any public keys configured for your app. Confirm that you added the public keys to the correct app in your workspace that matches this API Key.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Not all user IDs in the request payload match as is required.| This is unexpected and can result in a malformed payload. Open a support ticket for assistance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Frequently Asked Questions (FAQ) {#faq}

#### Does this feature need to be enabled on all of my apps at the same time? {#faq-app-by-app}

No, this feature can be enabled for specific apps and doesn't need to be used on all of your apps, all at once.

#### What happens to users who are still on older versions of my app? {#faq-sdk-backward-compatibility}

When you begin to enforce this feature, requests made by older app versions will be rejected by Braze and retried by the SDK. After users upgrade their app to a supported version, those enqueued requests will begin to be accepted again.

If possible, you should push users to upgrade as you would for any other mandatory upgrade. Alternatively, you can keep the feature [Optional](#enforcement-options) until you see that an acceptable percentage of users have upgraded.

#### What expiration should I use when generating a JWT? {#faq-expiration}

We recommend using the higher value of average session duration, session cookie/token expiration, or the frequency at which your application would otherwise refresh the current user's profile.

#### What happens if a JWT expires in the middle of a user's session? {#faq-jwt-expiration}

Should a user's token expire mid-session, the SDK has a [callback function](#sdk-callback) it will invoke to let your app know that a new JWT is needed to continue sending data to Braze.

#### What happens if my server-side integration breaks and I can no longer create a JWT? {#faq-server-downtime}

If your server is not able to provide a JWT or you notice some integration issue, you can always disable the feature in the Braze dashboard.

Once disabled, any pending failed SDK requests will eventually be retried by the SDK and accepted by Braze.

#### Why does this feature use public/private keys instead of shared secrets? {#faq-shared-secrets}

When using shared secrets, anyone with access to that shared secret, such as the Braze dashboard page, would be able to generate tokens and impersonate your end-users.

Instead, we use public/private keys so that not even Braze Employees (let alone your company users) have access to your private keys.

#### How will rejected requests be retried? {#faq-retry-logic}

When a request is rejected because of an authentication error, the SDK will invoke your callback used to refresh the user's JWT. 

Requests will retry periodically using an exponential backoff approach. After 50 consecutive failed attempts, retries will be paused until the next session start. Each SDK also has a method to manually request a data flush.

#### Can you use JWT request protection for anonymous users? {#faq-anonymous-users}

JWT-based request protection applies only to identified users, and enforcement starts after `changeUser` is called. Before a user is identified (for example, while browsing anonymously before signing up), the SDK can still send data to Braze without a JWT. After `changeUser` is called, requests for that identified profile require a valid JWT.

This means a typical user journey might look like:

1. A user visits your site or opens your app anonymously. Braze collects this activity without a JWT.
2. The user signs up or logs in, and your app calls `changeUser` with an `external_id`.
3. Braze continues collecting activity for that user, and JWT-based request protection is enforced for requests for that identified profile.

#### Does SDK authentication work with user aliases? {#faq-aliases}

No. SDK authentication requires an `external_id`. You can't set it up when only a `braze_id` or `alias_id` is available, so alias-only profiles can't use SDK authentication.

#### Does enabling SDK authentication block unauthenticated activity collection? {#faq-unauthenticated-collection}

No. SDK authentication does not block legitimate anonymous activity collection. It only applies after a profile is identified with `changeUser`.

If an identified user logs out, their previously issued JWT can remain valid until it expires. During that time, requests for that identified profile can still be accepted.
