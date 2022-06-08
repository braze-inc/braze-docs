---
nav_title: Advanced Use Cases
article_title: Advanced SDK Use Cases for Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 7
description: "This reference article covers advanced SDK use cases for the Unity platform."
---

# Customizing the Unity package

You can choose to customize and export the Braze Unity package using the provided scripts.

1. Clone the [Braze Unity SDK GitHub project][1]:

	```bash
	git clone git@github.com:Appboy/appboy-unity-sdk.git
	```
2. From the `appboy-unity-sdk/scripts` directory, run `./generate_package.sh` to export the Unity packages. Unity should be open while running `generate_package.sh`.
3. The packages will be exported to `appboy-unity-sdk/unity-package/`.
4. In the Unity Editor, import the desired package into your Unity project by navigating to **Assets > Import Package > Custom Package**.
5. (Optional) Deselect any files you do not wish to import.

You can customize the exported Unity package by editing both `generate_package.sh` and the export script located at `Assets/Editor/Build.cs`.

## Prime 31 compatibility

To use the Braze Unity plugin with Prime31 plugins, edit your project's `AndroidManifest.xml` to use the Prime31 compatible Activity classes. Change all references of
`com.appboy.unity.AppboyUnityPlayerActivity` to `com.appboy.unity.prime31compatible.AppboyUnityPlayerActivity`

## Amazon ADM push

Braze supports integrating [Amazon ADM push][10] into Unity apps. If you would like to integrate Amazon ADM push, create a file called `api_key.txt` containing your ADM API key and place it in the `Plugins/Android/assets/` folder.  For more information on integrating Amazon ADM with Braze, visit our [ADM push integration instructions][11].

[1]: https://github.com/appboy/appboy-unity-sdk
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/
