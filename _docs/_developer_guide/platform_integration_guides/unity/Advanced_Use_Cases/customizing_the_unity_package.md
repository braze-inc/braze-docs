---
nav_title: Customizing the Unity Package
platform: Unity
page_order: 0
---
## Customizing the Unity Package

You can choose to customize and export the Braze Unity package using the provided scripts.

1. Clone the [Braze Unity SDK Github project][1]:

	```bash
	git clone git@github.com:Appboy/appboy-unity-sdk.git
	```
2. From the root `appboy-unity-sdk` directory, run `./scripts/generate_package.sh` to export the Unity package.
	- Adding the `--nodeps` command line option will bundle the Unity package without the [SDWebImage][2] iOS SDK dependency. Please note that SDWebImage is required for proper functionality of Braze's In-App Messaging and News Feed features on iOS.
	- Unity __cannot__ be open while running `generate_package.sh`, or the script will fail.
3. The package will be exported to `unity-package/Appboy.unitypackage`.
	- If you generated the package with the `--nodeps` option, it will be named `Appboy-nodeps.unitypackage`.
4. In the Unity Editor, import the package into your Unity project by navigating to Assets > Import Package > Custom Package.
5. (Optional) Deselect any files you do not wish to import.

You can customize the exported Unity package by editing both `generate_package.sh` and the export script located at `Assets/Editor/Build.cs`.

[1]: https://github.com/appboy/appboy-unity-sdk
[2]: https://github.com/rs/SDWebImage
