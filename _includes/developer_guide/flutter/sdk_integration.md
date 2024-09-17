## About the SDK

With the Braze Flutter SDK, you can allow integrators to use Braze APIs in [Flutter apps](https://flutter.dev/) written in Dart. This plugin provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with a single codebase.

## Prerequisites

Before you start, you'll need to complete the following:

|Prerequisite|Description|
|------------|-----------|
| [An app identifier API key]({{site.baseurl}}/api/identifier_types/)|In the Braze dashboard, go to **Manage Settings** > **API keys**.|
| [A Braze SDK endpoint]({{site.baseurl}}/api/basics/#endpoints)| In the Braze dashboard, go to **Manage Settings** > **API keys**.|
| [The Flutter SDK](https://docs.flutter.dev/get-started/install)|Ensure your machine and project are running the minimum required Flutter and Dart versions [noted here](https://github.com/braze-inc/braze-flutter-sdk#readme).|

## Step 1: Integrate the Braze library

Add the Braze Flutter SDK package from the command line.

```bash
flutter pub add braze_plugin
```

This will add the appropriate line to your `pubspec.yaml`.

## Step 2: Complete native setup

{% tabs %}
{% tab Android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endtab %}
{% endtabs %}

## Step 3: Import the plugin

To import the plugin into your Dart code, use the following:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Then, initialize an instance of the Braze plugin by calling `new BrazePlugin()` like in [our sample app](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

## Step 4: Test the integration (optional)

You can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the **Overview** section).

Open a session for a particular user by calling the following code in your app.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Then, search for the user with `{some-user-id}` in the dashboard under **Audience** > **Search Users**. There, you can verify that session and device data have been logged.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can search for users from **Users** > **User Search**.
{% endalert %}
