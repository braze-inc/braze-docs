## トラブルシューティング

### プッシュはタスクスイッチャーからアプリが閉じられた後に表示されません

タスク切替画面からアプリを閉じた後、プッシュ通知が表示されなくなった場合、アプリはデバッグモードになっている可能性が高い。.NET MAUIはデバッグモード時に、アプリのプロセスが終了した後にプッシュ通知を受信できないようにするスキャフォールディングを追加する。アプリをリリースモードで実行すると、タスクスイッチャーからアプリを閉じた後でもプッシュ通知が表示されるはずです。

### カスタム通知ファクトリが正しく設定されていません

カスタム通知ファクトリ (およびすべてのデリゲート) は、C# と Javaの境界を越えて適切に機能するために [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) を拡張する必要があります。詳細については、Javaインターフェイスの実装に関する[Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces)を参照してください。
