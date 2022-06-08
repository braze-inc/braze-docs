---
nav_title: Sample Apps
article_title: Sample Apps for iOS
platform: iOS
page_order: 9
description: "This article covers iOS sample apps."

---

# Sample apps

Braze's SDKs each come with sample applications within the repository for your convenience. Each of these apps is fully buildable, so you can test Braze features alongside implementing them within your own applications. Testing behavior within your own application versus expected behavior and codepaths within the sample applications is an excellent way to debug any problems you may run into.

## Building test applications
Several test applications are available within the [iOS SDK GitHub repository][1]. Follow these instructions to build and run our test applications.

1. Create a new [app group][25] and note the app identifier API key.
2. Place your API key within the appropriate field in the `AppDelegate.m` file.

Push notifications for the iOS test application require additional configuration. Refer to our [iOS Push integration][7] for details.

[1]: https://github.com/appboy/appboy-ios-sdk "Appboy iOS GitHub Repository"
[25]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
