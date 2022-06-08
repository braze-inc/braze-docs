---
nav_title: Unit Tests (Optional)
article_title: Push Notification Unit Tests for iOS
platform: iOS
page_order: 29.5
description: "This article describes how to implement optional unit tests for your iOS push implementation."
channel:
  - push

---

# Unit tests {#unit-tests}

This optional guide describes how to implement some unit tests that will verify whether your app delegate correctly follows the steps described in Braze's [push integration instructions][1]. 

If all the tests pass, generally, this means the code-based part of your push setup is functional. If a test fails, this might mean that you incorrectly followed a step, or it may result from a valid customization that doesn't align precisely with Braze's default instructions.

Either way, this can be a helpful approach to verify you've followed the integration steps and to help monitor for any regressions.

## Step 1: Creating a unit tests target

Skip this step if your app project in Xcode already contains a Unit Testing Bundle.

In your app project, go to menu **File > New > Target** and add a new "Unit Testing Bundle". This bundle can use either Objective-C or Swift and have any name. Set the "Target to be Tested" to your main app target.

## Step 2: Add the Braze SDK to your unit tests

Using the same method you used initially to [install the Braze SDK][2], make sure the same SDK installation is also available to your unit tests target. For example, using Cocoapods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Step 3: Add OCMock to your unit tests

Add [OCMock][3] to your test target via Cocoapods, Carthage, or its static library. For example, using Cocoapods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Step 4: Finish installing the added libraries

Finish installing the Braze SDK and OCMock. For example, using Cocoapods, navigate to the directory of your Xcode app project within your terminal and run the following command:

```
pod install
```

At this point, you should be able to open the Xcode project workspace created by CocoaPods.

## Step 5: Adding push tests

Create a new Objective-C file in your unit tests target. 

If the unit tests target is in Swift, Xcode may ask, "Would you like to configure an Objective-C bridging header?" The bridging header is optional, so you can click **Don't Create** and still run these unit tests successfully.

Add the contents of the HelloSwift sample app's [`AppboyPushUnitTests.m`][4] to the new file.

## Step 6: Run test suite

Run your app's unit tests. This can be a one-time verification step, or you can include this indefinitely in your test suite to help catch any regressions.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/
[3]: https://ocmock.org/
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m