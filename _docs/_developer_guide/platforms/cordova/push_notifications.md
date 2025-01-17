---
nav_title: Push Notifications
article_title: Push Notifications for the Cordova Braze SDK
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "This article covers implementing push notifications on Cordova."
channel: push
---

# Push notifications

> Learn how to integrate push notifications for the Cordova Braze SDK, including rich push notifications and push stories.

## Prerequisites

Before you can use this feature, you'll need to integrate the [Braze Cordova SDK]({{site.baseurl}}/developer_guide/platforms/cordova/sdk_integration/) into your app.  After you integrate the SDK, basic push notification functionality is enabled by default. To use [rich push notifications](#setting-up-rich-push-notifications) and [push stories](#setting-up-push-stories), you'll need to set them up individually.

{% alert warning %}
Anytime you add, remove, or update your Cordova plugins, Cordova will overwrite the Podfile in your iOS app's Xcode project. This means you’ll need to set these features up again anytime you modify your Cordova plugins.
{% endalert %}

## Setting up rich push notifications

### Step 1: Create a notification service extension

In your Xcode project, create a notification service extension. For a full walkthrough, see [iOS Rich Push Notifications Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Step 2: Add a new target

Open your Podfile and add `BrazeNotificationService` to the notification service extension target [you just created](#step-1-create-a-notification-service-extension). If `BrazeNotificationService` is already added to a target, remove it before continuing. To avoid duplicate symbol errors, use static linking.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

Replace `NOTIFICATION_SERVICE_EXTENSION` with the name of your notification service extension. Your Podfile should be similar to the following:

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

### Step 3: Reinstall your CocoaPods dependencies

In the terminal, go to your project's iOS directory and reinstall your CocoaPod dependencies.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

## Setting up push stories

### Step 1: Create a notification content extension

In your Xcode project, create a notification content extension. For a full walkthrough, see [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Step 2: Configure your push app group

In your project's `config.xml` file, configure the push app group [you just created](#step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Replace `PUSH_APP_GROUP` with the name of your push app group. Your `config.xml` should be similar to the following:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Step 3: Add a new target

Open your Podfile and add `BrazePushStory` to the notification content extension target [you created previously](#step-1-create-a-notification-content-extension). To avoid duplicate symbol errors, use static linking.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

Replace `NOTIFICATION_CONTENT_EXTENSION` with the name of your notification content extension. Your Podfile should be similar to the following:

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

### Step 4: Reinstall your CocoaPods dependencies

In the terminal, go to your iOS directory and reinstall your CocoaPod dependencies.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

## Disabling basic push notifications (iOS only)

After you integrate the Braze Cordova SDK for iOS, basic push notification functionality is enabled by default. To disable this functionality in your iOS app, add the following to your `config.xml` file. For more information, see [Optional configurations]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/sdk_integration#optional-configurations).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
