---
nav_title: 位置情報の追跡
article_title: iOS の位置情報の追跡
platform: iOS
page_order: 6
description: "この記事では、iOS アプリケーションの位置情報の追跡の設定方法を説明します。"
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS の位置情報の追跡

デフォルトでは、Braze で位置情報の追跡は無効になっています。位置情報の追跡は、ホストアプリケーションで位置情報の追跡がオプトインされ、ユーザーから許可を得た後に有効になります。ユーザーが位置情報の追跡をオプトインしている場合、Braze ではセッション開始時に各ユーザーの単一の位置情報がロギングされます。

{% alert important %}
おおよその位置情報をユーザーが許可している場合に iOS 14 で位置情報の追跡を確実に機能させるには、SDK バージョンを少なくとも `3.26.1` にアップデートする必要があります。
{% endalert %}

## 位置情報の自動追跡を有効にする

Braze iOS SDK `v3.17.0` 以降、位置情報の追跡はデフォルトで無効になっています。位置情報の自動追跡を有効にするには、`Info.plist` ファイルを使用します。`Braze` ディクショナリを `Info.plist` ファイルに追加します。`Braze` ディクショナリ内にブール値の `EnableAutomaticLocationCollection` サブエントリを追加し、値を `YES` に設定します。なお、Braze iOS SDK v4.0.2 より前のバージョンでは、`Braze` の代わりにディクショナリキー `Appboy` を使用する必要があります。

[`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) メソッドを使用して、アプリの起動時に位置情報の自動追跡を有効にすることもできます。`appboyOptions` ディクショナリで、`ABKEnableAutomaticLocationCollectionKey` を `YES` に設定します。以下に例を示します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### 位置データを Braze に渡す

以下の 2 つのメソッドは、ユーザーの既知の最終位置情報を手動で設定するために使用できます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy)
```

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy, altitude: altitude, verticalAccuracy: verticalAccuracy)
```

{% endtab %}
{% endtabs %}

詳細については、[`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h) を参照してください。

