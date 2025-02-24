## About the Unreal Engine Braze SDK

With the Braze Unreal SDK plugin, you can:

* Measure and track sessions within your app or game
* Track in-app purchases and custom events
* Update user profiles with standard and custom attributes
* Send push notifications
* Integrate your Unreal apps with larger Canvas journeys
* Send cross-channel messaging, like email or SMS, based on in-app behavior

## Integrating the Unreal Engine SDK

### Step 1: Add the Braze plugin

In your terminal, clone the [Unreal Engine Braze SDK GitHub repository](https://github.com/braze-inc/braze-unreal-sdk).

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

Then, copy the `BrazeSample/Plugins/Braze` directory, and add it into your app's Plugin folder.

### Step 2: Enable the plugin

Enable the plugin for your C++ or Blueprint project.

{% tabs %}
{% tab C++ %}
For C++ projects, configure your module to reference the Braze module. In your `\*.Build.cs file`, add `"Braze"` to your `PublicDependencyModuleNames`.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab Blueprint %}
For Blueprint projects, go to **Settings** > **Plugins**, then next to **Braze** check **Enabled**.

![EnablePlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### Step 3: Set your API key and endpoint

Set your API key and endpoint in your project's `DefaultEngine.ini`.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
For projects targeting Android SDK 31+ Unreal will generate builds that will fail during installation on Android 12+ devices with the INSTALL_PARSE_FAILED_MANIFEST_MALFORMED error. To fix this, locate the `UE4_Engine_AndroidSDK_31_Build_Fix.patch` git patch file in the root of this repository and apply it to your Unreal source build.
{% endalert %}

## Optional configurations

### Logging

{% tabs local %}
{% tab Android %}
You can set the log level at runtime using C++ or in a Blueprint node.

{% subtabs %}
{% subtab C++ %}
To set the log level at runtime, call `UBrazeSubsystem::AndroidSetLogLevel`.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
In Blueprint, you can use the **Android Set Log Level** node:

![The Android Set Log Level node in Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

In order to ensure logging is set when the Braze SDK Initialize is called, it is recommended to call this before `InitializeBraze`.
{% endtab %}

{% tab iOS %}
To enable the log level in the `info.plist`, go to **Settings** > **Project Settings**, then select **iOS** under **Platforms**. Under **Extra PList Data**, find **Additional Plist Data**, then enter your log level:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

The default log level is 8, which is minimal logging. Read more about log levels: [Other SDK Customization](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
