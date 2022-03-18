---
nav_title: Unit Tests (Optional)
article_title: Push Notification Unit Tests for iOS
platform: iOS
page_order: 29
description: "This article describes how to implement optional unit tests for your iOS push implementation."
channel:
  - push

---

# Unit Tests {#unit-tests}

This guide describes how to implement some unit tests that will verify whether your app delegate correctly follows the steps described in Braze's [push integration instructions][1]. 

If all the tests pass, generally this means the code-based part of your push setup is functional. If a test fails, this might mean that you incorrectly followed a step, or it may be a result of a valid customization that don't precisely align with Braze's default instructions.

Either way, this can be a helpful approach to verify you've followed the integration steps and to help monitor for any regressions.

## Step 1: Creating a unit tests target

Skip this step if your app project in Xcode already contains a Unit Testing Bundle.

In your app project, go to menu "File"->"New"->"Target" and add a new "Unit Testing Bundle". This bundle can use either Objective-C or Swift and have any name. Set the "Target to be Tested" to your main app target.

## Step 2: Add the Braze SDK to your unit tests

Using the same method that you used initially to [install the Braze SDK][2], make sure the same installation of the SDK is also available to your unit tests target. For example, if using Cocoapods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```


## Step 3: Add OCMock to your unit tests

Add [OCMock][3] to your test target via Cocoapods, Carthage, or its static library. For example, if using Cocoapods:

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

Finish installing the Braze SDK and OCMock. For example, if using Cocoapods, navigate to the directory of your Xcode app project within your terminal and run the following command:

```
pod install
```

At this point, you should be able to open the Xcode project workspace created by CocoaPods.

## Step 5: Adding push tests

Create a new Objective-C file in your unit tests target. 

If the unit tests target is in Swift, Xcode may ask "Would you like to configure an Objective-C bridging header?" If it does, select "Create Bridging Header." 
#TODO is this needed?

Add the following contents to this new file:

```objc
#import "Appboy.h"
#import <OCMock/OCMock.h>
#import <UIKit/UIKit.h>
#import <UserNotifications/UserNotifications.h>
#import <XCTest/XCTest.h>

/**
 * A collection of test cases to verify a successful implementation of push
 * notifications using Braze.

 * In a unit testing target, as long as the `AppboyPushTests` module is included,
 * the target will run all of this class's unit tests. No added code is required.
 *
 * @seealso https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/
 */
@interface AppboyPushUnitTests : XCTestCase

@end

@implementation AppboyPushUnitTests

// MARK: - Push Registration

/**
 * Checks whether the app registers for push notifications when launching.
 *
 * @discussion This test case will pass if the AppDelegate's
 * @c application:didFinishLaunchingWithOptions: method results in a call to:
 *
 * @code
 * [[UIApplication sharedApplication] registerForRemoteNotifications];
 * @endcode
 *
 * @seealso https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-3-register-for-push-notifications
 */
- (void)testDidFinishLaunchingWithOptions_RegistersForPush {
  id partialMock = [OCMockObject partialMockForObject:UIApplication.sharedApplication];
  UIApplication *application = UIApplication.sharedApplication;

  // Launch app
  [application.delegate application:application didFinishLaunchingWithOptions:nil];

  // Confirm app registered for push
  OCMVerify([partialMock registerForRemoteNotifications]);
}

// MARK: - Push Tokens

/**
 * Checks whether the app registers the device's push token with the
 * Braze SDK when the system registers for push notifications.
 *
 * @discussion This test case will pass if the AppDelegate's
 * @c application:didRegisterForRemoteNotificationsWithDeviceToken: method
 * results in a call to:
 *
 * @code
 * [[Appboy sharedInstance] registerDeviceToken:deviceToken];
 * @endcode
 *
 * @seealso https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
 */
- (void)testDidRegisterForRemoteNotificationsWithDeviceToken {
  id partialMock = [OCMockObject partialMockForObject:[Appboy sharedInstance]];
  UIApplication *application = UIApplication.sharedApplication;
  NSData *token = [[NSData alloc] init];

  // Register with device token
  [application.delegate application:application didRegisterForRemoteNotificationsWithDeviceToken:token];

  // Confirm device token logged to Braze
  OCMVerify([partialMock registerDeviceToken:token]);
}

// MARK: - Push Analytics and Handling

/**
 * Checks whether the app uses Braze to handle newly received push notifications.
 *
 * @discussion This test case will pass if the AppDelegate's
 * @c application:didFinishLaunchingWithOptions: method sets a valid
 * @c UNUserNotificationCenterDelegate as the
 *
 * @code
 * [UNUserNotificationCenter currentNotificationCenter].delegate
 * @endcode
 *
 * AND the AppDelegate's
 * @c application:didReceiveRemoteNotification:fetchCompletionHandler: method
 * results in a call to:
 *
 * @code
 * [[Appboy sharedInstance] registerApplication:application
 *                 didReceiveRemoteNotification:userInfo
 *                       fetchCompletionHandler:completionHandler];
 * @endcode
 *
 * @seealso https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
 */
- (void)testDidReceiveRemoteNotification {
  id partialMock = [OCMockObject partialMockForObject:[Appboy sharedInstance]];
  UIApplication *application = UIApplication.sharedApplication;

  // Receive notification
  [application.delegate application:application
       didReceiveRemoteNotification:@{}
             fetchCompletionHandler:^(UIBackgroundFetchResult result) {}];

  // Confirm notification logged to Braze
  OCMVerify([partialMock registerApplication:application
                didReceiveRemoteNotification:@{}
                      fetchCompletionHandler:[OCMArg any]]);
}

/**
 * Checks whether the app uses Braze to handle any interaction with a push notification.
 *
 * @discussion This test case will pass if the AppDelegate's
 * @c application:didFinishLaunchingWithOptions: method sets a valid
 * @c UNUserNotificationCenterDelegate as the
 *
 * @code
 * [UNUserNotificationCenter currentNotificationCenter].delegate
 * @endcode
 *
 * AND the AppDelegate's
 * @c userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler: method
 * results in a call to:
 *
 * @code
 * [[Appboy sharedInstance] userNotificationCenter:center
 *                  didReceiveNotificationResponse:response
 *                           withCompletionHandler:completionHandler];
 * @endcode
 *
 * @seealso https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
 */
- (void)testDidReceiveNotificationResponse {
  id partialMock = [OCMockObject partialMockForObject:[Appboy sharedInstance]];
  UNUserNotificationCenter *notificationCenter = UNUserNotificationCenter.currentNotificationCenter;
  UNNotificationResponse *response = OCMClassMock([UNNotificationResponse class]);

  // Receive notification response
  [notificationCenter.delegate userNotificationCenter:notificationCenter
                       didReceiveNotificationResponse:response
                                withCompletionHandler:^{}];

  // Confirm response logged to Braze
  OCMVerify([partialMock userNotificationCenter:notificationCenter
                 didReceiveNotificationResponse:response
                          withCompletionHandler:[OCMArg any]]);
}

/**
 * Checks whether the app handles push notifications while foregrounded.
 *
 * @discussion This test case will pass if the AppDelegate's
 * @c userNotificationCenter:willPresentNotification:withCompletionHandler: method
 * results in calling the provided @c completionHandler
 *
 * @seealso https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
 */
- (void)testForegroundPushHandling {
  UNUserNotificationCenter *notificationCenter = UNUserNotificationCenter.currentNotificationCenter;
  UNNotification *notification = OCMClassMock([UNNotification class]);

  XCTestExpectation *expectation = [[XCTestExpectation alloc] initWithDescription:@"Completion handler should be called"];

  [notificationCenter.delegate userNotificationCenter:notificationCenter
                              willPresentNotification:notification
                                withCompletionHandler:^(UNNotificationPresentationOptions options) {
    [expectation fulfill];
  }];

  [self waitForExpectations:@[expectation] timeout:0.5];
}

@end
```

## Step 5: Run test suite

Run your app's unit tests. This can be a one-time verification step, or you can include this indefinitely in your test suite to help catch any changes.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/
[3]: https://ocmock.org/