{% multi_lang_include developer_guide/prerequisites/cordova.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Setting up rich push notifications

### Step 1: Create a notification service extension

In your Xcode project, create a notification service extension. For a full walkthrough, see [iOS Rich Push Notifications Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Step 2: Add a new target

Open your Podfile and add `BrazeNotificationService` to the notification service extension target [you just created](#cordova_step-1-create-a-notification-service-extension). If `BrazeNotificationService` is already added to a target, remove it before continuing. To avoid duplicate symbol errors, use static linking.

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
