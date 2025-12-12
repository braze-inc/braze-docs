{% multi_lang_include developer_guide/prerequisites/react_native.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native)必要だ。

## Expoを使ってリッチプッシュ通知を可能にする

React Native SDKでは、**リッチプッシュ通知はデフォルトでAndroidで利用できる**。

Expo を使用して iOS でリッチプッシュ通知を有効にするには、`app.json` の `expo.plugins` オブジェクトで `enableBrazeIosRichPush` プロパティを `true` に構成します。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

最後に、このアプリ拡張機能のバンドル識別子を、プロジェクトの認証情報設定に追加します：`<your-app-bundle-id>.BrazeExpoRichPush`.このプロセスの詳細については、[Expo Application Services でアプリ拡張機能を使用する]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions)を参照してください。
