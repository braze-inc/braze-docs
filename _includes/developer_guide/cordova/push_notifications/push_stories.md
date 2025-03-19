{% multi_lang_include developer_guide/prerequisites/cordova.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Setting up push stories

### Step 1: Create a notification content extension

In your Xcode project, create a notification content extension. For a full walkthrough, see [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Step 2: Configure your push app group

In your project's `config.xml` file, configure the push app group [you just created](#cordova_step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Replace `PUSH_APP_GROUP` with the name of your push app group. Your `config.xml` should be similar to the following:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Step 3: Add a new target

Open your Podfile and add `BrazePushStory` to the notification content extension target [you created previously](#cordova_step-1-create-a-notification-content-extension). To avoid duplicate symbol errors, use static linking.

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
