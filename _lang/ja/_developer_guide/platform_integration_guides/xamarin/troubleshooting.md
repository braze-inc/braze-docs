---
nav_title: トラブルシューティング
article_title: Xamarin のトラブルシューティング
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 6
description: "この記事では、Xamarin プラットフォームの iOS および Android のトラブルシューティングについて説明します。"

---

# トラブルシューティング

> この記事では、Xamarin のトラブルシューティング シナリオをいくつか紹介します。

## Android

### タスクスイッチャーからアプリを閉じた後にプッシュが表示されない

タスクスイッチャーからアプリを閉じた後にプッシュ通知が表示されなくなった場合は、アプリがデバッグ モードになっている可能性があります。Xamarin はデバッグ モードでスキャフォールディングを追加し、プロセスが強制終了された後にアプリがプッシュを受信しないようにします。アプリをリリース モードで実行すると、タスク スイッチャーからアプリを閉じた後でもプッシュが表示されるはずです。

### カスタム通知ファクトリが正しく設定されていない

カスタム通知ファクトリー（およびすべてのデリゲート）は、 [`Java.Lang.Object`][2]C# と Java の境界を越えて適切に動作します。詳細については、Java インターフェイスの実装に関する [Xamarin][1] を参照してください。

[1]: https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces
[2]: https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/