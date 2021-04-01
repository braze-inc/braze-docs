---
nav_title: Advanced Use Cases
platform: Unity
page_order: 0
---

## Customizing the Unity Package

You can choose to customize and export the Braze Unity package using the provided scripts.

1. Clone the [Braze Unity SDK Github project][1]:

	```bash
	git clone git@github.com:Appboy/appboy-unity-sdk.git
	```
2. From the `appboy-unity-sdk/scripts` directory, run `./generate_package.sh` to export the Unity packages.
	- Unity should be open while running `generate_package.sh`.
3. The packages will be exported to `appboy-unity-sdk/unity-package/`.
4. In the Unity Editor, import the desired package into your Unity project by navigating to `Assets > Import Package > Custom Package`.
5. (Optional) Deselect any files you do not wish to import.

You can customize the exported Unity package by editing both `generate_package.sh` and the export script located at `Assets/Editor/Build.cs`.

## Manual iOS Integration

### Initial SDK Setup

Follow the instructions below to manually integrate Braze into your built Xcode project.

#### Step 1: Clone the Unity SDK

Clone the [Braze Unity SDK Github project][1]

```bash
git clone git@github.com:Appboy/appboy-unity-sdk.git
```

#### Step 2: Copy Required Plugins

1. `Plugins/Appboy` -> `/<your-project>/Assets/Plugins/Appboy`
2. `Plugins/iOS` -> `/<your-project>/Assets/Plugins/iOS`

#### Step 3: Test Xcode Project Generation

Now that you've copied over the requisite plugins, the following steps will help you generate your Xcode project and add the required classes for the Braze SDK to function:

1. Generate your Xcode project in Unity by clicking on File > Build Settings...
2. Select iOS as the platform and click "Build".
3. Select `/your-project/your-iOS-project/` as the build location.
4. Confirm that Unity has copied the source files from `Plugins/iOS` to your generated project under the "Libraries" directory.

#### Step 4: Add the Braze iOS SDK framework and required system frameworks

You must now add the Braze iOS SDK framework into your project.

1. Add `Appboy_iOS_SDK.framework` and `SDWebImage.framework` to your project as embedded frameworks.
  - Your "Build Phases" panel's "Embed Frameworks" step should contain `Appboy_iOS_SDK.framework` and `SDWebImage.framework`
2. Add Required iOS Libraries
	1. Click on the target for your project (using the left-side navigation), and select the “Build Phases” tab
	2. Click the + button under “Link Binary With Libraries”
	3. In the menu, select `SystemConfiguration.framework` and press the Add button.
    ![Add SystemConfiguration.framework][10]
	4. Mark this library as "Required" using the pull-down menu next to `SystemConfiguration.framework`
    ![Mark SystemConfiguration.framework as Required][11]
	5. Repeat Steps 3 and 4 to add each of the following required frameworks to your project, marking each as “Required”
		- `QuartzCore.framework`
		- `CoreImage.framework`
		- `libz.tbd`
    ![Rinse and Repeat][12]
	6. Add the following frameworks and mark them as "Optional":
		- `CoreTelephony.framework`
		- `ImageIO.framework`
		- `Accounts.framework`
		- `StoreKit.framework`
		- `CoreLocation.framework`

#### Step 5: Update Project Build Settings

   1. Click on the target for your project (using the left-side navigation), and select the “Build Settings" tab
   2. Find "Other Linker Flags" and add `-ObjC` to the row

#### Step 5: Initialize the SDK

You now must make modifications to your `UnityAppController` subclass. Typically, this is generated in `Classes/UnityAppController.mm`:

1. At the top of your `UnityAppController` subclass, add the following import statements:

```objc
#import <Appboy_iOS_SDK/AppboyKit.h>
#import "AppboyUnityManager.h"
```

2. In the `UIApplicationDelegate` method `applicationDidFinishLaunchingWithOptions`, add the following code snippet above the return statement. Be sure to replace `"YOUR-API-KEY"` with the Braze API key from the [Braze dashboard][19].

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
				inApplication:application
				withLaunchOptions:launchOptions];
```

#### Step 6: Basic SDK Integration Complete

Braze should now be collecting data from your application and your basic integration should be complete.

[1]: https://github.com/appboy/appboy-unity-sdk
[5]: #transitioning-from-manual-to-automated-integration
[7]: #step-1-importing-the-braze-unity-package
[10]: {% image_buster /assets/img_archive/unity-ios-sysconfig.png %}
[11]: {% image_buster /assets/img_archive/unity-ios-sysconfigreq.png %}
[12]: {% image_buster /assets/img_archive/iosunitystep3part5.gif %}
[19]: https://dashboard-01.braze.com/app_settings/app_settings
