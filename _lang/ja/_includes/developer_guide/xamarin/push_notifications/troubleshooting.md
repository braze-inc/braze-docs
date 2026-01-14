## トラブルシューティング

### プッシュはタスクスイッチャーからアプリが閉じられた後に表示されません

プッシュ通知 sがタスクアプリを終了した後に耳をアプリしなくなった場合、アプリはデバッグモードである可能性が切り替えるされます。。NET MAUIは、デバッグモードで足場を追加します。これにより、プロセスが強制終了された後にアプリがプッシュを受信できなくなります。アプリをリリースモードで実行すると、タスクスイッチャーからアプリを閉じた後でもプッシュ通知が表示されるはずです。

### カスタム通知ファクトリが正しく設定されていません

カスタム通知ファクトリ (およびすべてのデリゲート) は、C# と Javaの境界を越えて適切に機能するために [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) を拡張する必要があります。詳細については、Javaインターフェイスの実装に関する[Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces)を参照してください。
