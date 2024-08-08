---
nav_title: アプリ内メッセージング
article_title: Xamarin のアプリ内メッセージング
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "この記事では、Xamarin プラットフォームの iOS、Android、FireOS のアプリ内メッセージングについて説明します。"
channel: in-app messages

---

# アプリ内メッセージの統合

> この記事では、Xamarin プラットフォーム用に iOS、Android、FireOS のアプリ内メッセージを設定する方法について説明します。

## Android
アプリ内メッセージを Xamarin Android アプリに統合する方法については、 [Android 統合の手順][11] を参照してください。 さらに、実装サンプルについては、 [サンプルアプリケーション][12] を参照できます。

## iOS

アプリ内メッセージは、アプリにAppboy.bundleフォルダーを含めている場合、デフォルトで機能します。Xamarin では、現在、アプリ内メッセージのカスタム スタイル設定はサポートされていません。アプリ内メッセージUIをカスタマイズする場合は、ABKInAppMessageControllerDelegateメソッド `ABKInAppMessageViewController InAppMessageViewControllerWithInAppMessage(ABKInAppMessage inAppMessage);` を実装し、カスタムビューコントローラーを返します。これにより、Brazeはアプリ内メッセージオブジェクトを表示するのではなく、渡すようになります。その後、アプリ内メッセージオブジェクトのコンテンツを手動で表示するオプションが表示されます。

アプリ内のベストプラクティスについては、 [iOS統合の手順][1] を参照してください。さらに、実装サンプルについては、 [サンプルアプリケーション][2] を参照できます。

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/
[2]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/overview/
[12]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples
