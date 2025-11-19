{% multi_lang_include developer_guide/prerequisites/react_native.md %} [プッシュ通知を設定する必要もあります]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native)。

## プッシュストーリーの有効化

React Native SDKでは、**プッシュストーリーをデフォルト** でAndroidできます。

Expoを使ってiOSでプッシュストーリーズを有効にするには、アプリケーションにアプリグループが定義されていることを確認する。詳細については、[アプリグループの追加]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group)を参照してください。

次に、`enableBrazeIosPushStories` プロパティを `true` に構成し、`app.json` の `expo.plugins` オブジェクトの `iosPushStoryAppGroup` にアプリグループ ID を割り当てます。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

最後に、このアプリ拡張機能のバンドル識別子を、プロジェクトの認証情報設定に追加します：`<your-app-bundle-id>.BrazeExpoPushStories`.このプロセスの詳細については、[Expo Application Services でアプリ拡張機能を使用する]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions)を参照してください。

{% alert warning %}
Expo Application Services で Push Stories を使用する場合は、`eas build` を実行する際に、必ず `EXPO_NO_CAPABILITY_SYNC=1` フラグを使用してください。コマンドラインに既知の問題があり、拡張機能のプロビジョニングプロファイルからApp Groups機能が削除される。
{% endalert %}
