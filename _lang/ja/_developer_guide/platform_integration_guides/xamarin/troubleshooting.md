---
nav_title: トラブルシューティング
article_title: Xamarinのトラブルシューティング
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 6
description: "この記事では、XamarinプラットフォームのiOSおよびAndroidのトラブルシューティングについて説明します。"

---

# トラブルシューティング

> この記事では、いくつかのXamarinトラブルシューティングシナリオを提供しています。

## Android

### プッシュはタスクスイッチャーからアプリが閉じられた後に表示されません

アプリがタスクスイッチャーから閉じられた後にプッシュ通知が表示されなくなった場合、アプリがデバッグモードになっている可能性があります。Xamarinは、プロセスが終了した後にアプリがプッシュを受信するのを防ぐデバッグモードでスキャフォールディングを追加します。アプリをリリースモードで実行すると、タスクスイッチャーからアプリを閉じた後でもプッシュ通知が表示されるはずです。

### カスタム通知ファクトリが正しく設定されていません

カスタム通知ファクトリ（およびすべてのデリゲート）は、C#とJavaの分割全体で適切に機能するために[`Java.Lang.Object`][2]を拡張する必要があります。詳細については、Javaインターフェイスの実装に関する[Xamarin][1]を参照してください。

[1]: https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces
[2]: https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/