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
2. From the `appboy-unity-sdk/scripts` directory, run `./generate_package.sh` to export the Unity packages.
	- Unity should be open while running `generate_package.sh`.
3. The packages will be exported to `appboy-unity-sdk/unity-package/`.
4. In the Unity Editor, import the desired package into your Unity project by navigating to `Assets > Import Package > Custom Package`.
5. (Optional) Deselect any files you do not wish to import.

You can customize the exported Unity package by editing both `generate_package.sh` and the export script located at `Assets/Editor/Build.cs`.

[1]: https://github.com/appboy/appboy-unity-sdk
