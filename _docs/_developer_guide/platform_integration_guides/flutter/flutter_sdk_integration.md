---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for Flutter
platform: Flutter
page_order: 1
description: "This reference introduces the Flutter SDK and explains how to integrate it natively on Android and iOS."

---

# Initial SDK setup

Follow these instructions to install the [Braze Flutter SDK](https://pub.dev/packages/braze_plugin) that contains a specialized package that allows integrators to use certain Braze APIs from Flutter app code written in Dart. This plugin provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with a single codebase.

You will need to complete installation steps on both platforms separately.

To complete the installation, you will need the [App Identifier API key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) as well as the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints). Both are located in the **Developer Console** under **Settings** in the dashboard.

Please visit the Flutter [official website](https://flutter.dev/) to learn more about it and complete the [setup of the Flutter SDK](https://docs.flutter.dev/get-started/install).

## Step 1: Integrate the Braze library

Add the Braze Flutter SDK package from the command line. This will also add the appropriate line to your `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

To import the plugin into your Dart code, you can use:

```
import 'package:braze_plugin/braze_plugin.dart';
```

## Step 2: Complete native setup

