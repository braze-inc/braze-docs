---
nav_title: プッシュ通知
article_title: Xamarin のプッシュ通知
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "この記事では、Xamarin プラットフォームの Android、FireOS、iOS プッシュ通知の統合について説明します。"
channel: push 
---

# プッシュ通知の統合

> このリファレンス記事では、Xamarin 用に Android、FireOS、iOS のプッシュ通知を設定する方法について説明します。 

## Android

プッシュを Xamarin Android アプリに統合する方法については、 [Android 統合の手順][11] を参照してください。さらに、 [サンプル アプリケーション][12] を見ると、名前空間が Java から C# にどのように変更されるかを確認できます。

## iOS

プッシュでアプリケーションを設定し、認証情報をサーバーに保存する方法については、 [iOS統合の手順][1] を参照してください。

### プッシュ権限の要求

プッシュ権限を設定するには、次のコードを ```FinishedLaunching``` ```AppDelegate.cs```:

```csharp
// C#
UIUserNotificationSettings settings = UIUserNotificationSettings.GetSettingsForTypes(UIUserNotificationType.Badge | UIUserNotificationType.Alert | UIUserNotificationType.Sound, null);
UIApplication.SharedApplication.RegisterForRemoteNotifications();
UIApplication.SharedApplication.RegisterUserNotificationSettings(settings);
```

>  カスタム プッシュ オプトイン プロンプトを実装した場合は、アプリにプッシュ アクセス許可を付与した後、アプリが実行されるたびに上記のコードを呼び出すようにしてください。デバイストークンは任意に変更される可能性があるため、アプリは APNs に再登録する必要があります。

### プッシュトークンの登録

のメソッド```AppDelegate.cs```に```RegisteredForRemoteNotifications```次のコードを追加して、プッシュトークンに登録します。

```csharp
// C#
Appboy.SharedInstance().RegisterDeviceToken (deviceToken);
```

### プッシュ分析の有効化

プッシュ通知でオープントラッキングを有効にするには、`DidReceiveRemoteNotification``AppDelegate.cs`次のコードを :

```csharp
// C#
public override void DidReceiveRemoteNotification (UIApplication application, NSDictionary userInfo, Action<UIBackgroundFetchResult> completionHandler)
  {
    Appboy.SharedInstance().RegisterApplicationWithFetchCompletionHandler(application, userInfo, completionHandler);
  }
```

### バッジ数

[バッジカウントが有効になっている][2]場合、Brazeは顧客に未読の通知があるときにバッジを表示します。既定では、この数値は 1 です。Brazeは、Brazeプッシュ通知から直接アプリを開いた場合にのみ、バッジ数をクリアします。バッジ数をクリアするには、 [Xamarin][3] を参照し、次のコードを使用します。

```csharp
// C#
UIApplication.SharedApplication.ApplicationIconBadgeNumber = 0;
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#badge-count-with-braze
[3]: https://developer.xamarin.com/guides/cross-platform/application_fundamentals/notifications/ios/local_notifications_in_ios/#Handling_Notifications
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[12]: https://github.com/braze-inc/braze-xamarin-sdk

