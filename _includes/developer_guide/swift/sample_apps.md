---
nav_title: Sample Apps
article_title: Sample Apps for iOS
platform: Swift
page_order: 9
search_rank: 2
description: "This article covers iOS Swift SDK sample apps."

---

# Sample apps

> Braze SDKs each come with sample applications within the repository for your convenience. Each of these apps is fully buildable, so you can test Braze features alongside implementing them within your own applications. 

Testing behavior within your own application versus expected behavior and codepaths within the sample applications is an excellent way to debug any problems you may run into.

## Navigating examples

Several test applications are available within the `Examples` folder of the [Swift SDK GitHub repository](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples). The README describes all of the different permutations of sample integrations, such as:

1. Integration types (Swift Package Manager, CocoaPods, Manual)
2. Coding languages (Swift and Objective-C)
3. Platforms (iOS, tvOS, Mac Catalyst, etc.)
4. Features (In-App Messages, Content Cards, Location, Rich Push, Push Stories, etc.)
5. Customization types (default UI, fully custom UI)

## Building test applications

Follow these instructions to build and run our test applications.

1. Create a new [workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) and note the app identifier API key and endpoint.
2. Based on your integration method (Swift Package Manager, CocoaPods, Manual), select the appropriate `xcodeproj` file to open.
3. Place your API key and your endpoint within the appropriate field in the `Credentials` file.

