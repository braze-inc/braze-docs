## トラブルシューティング

### プッシュはタスクスイッチャーからアプリが閉じられた後に表示されません

アプリがタスクスイッチャーから閉じられた後にプッシュ通知が表示されなくなった場合、アプリがデバッグモードになっている可能性があります。Xamarin はデバッグモードでスキャフォールディングを追加し、プロセスが強制終了された後にアプリがプッシュを受信できないようにします。アプリをリリースモードで実行すると、タスクスイッチャーからアプリを閉じた後でもプッシュ通知が表示されるはずです。

### カスタム通知ファクトリが正しく設定されていません

カスタム通知ファクトリ (およびすべてのデリゲート) は、C# と Javaの境界を越えて適切に機能するために [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) を拡張する必要があります。詳細については、Javaインターフェイスの実装に関する[Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces)を参照してください。
