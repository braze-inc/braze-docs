{% multi_lang_include developer_guide/prerequisites/react_native.md %} [プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native)も[設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native)しなければならない。

## React Nativeのカスタマイズを推進する

Braze React Native SDKは、そのJavaScript APIを通じてプッシュ通知のカスタマイズ（アクションボタン、カテゴリ、カスタム通知ファクトリ）を公開していない。これらの機能は、iOSおよびAndroidプロジェクトでネイティブの設定が必要だ。

以下の表は、どの機能がネイティブ設定を必要とするかを示している：

| 機能 | iOS | Android |
| --- | --- | --- |
| アクションボタン | ネイティブのSWIFT/OBJECTIVE-Cで設定する | ネイティブのJava/Kotlinで設定する |
| カテゴリーを押す | ネイティブのSWIFT/OBJECTIVE-Cで設定する | ネイティブのJava/Kotlinで設定する |
| カスタム通知ファクトリ | N/A | ネイティブのJava/Kotlinで設定する |
| バッジのカスタマイズ | ネイティブのSWIFT/OBJECTIVE-Cで設定する | N/A |
| カスタムサウンド | ネイティブのSWIFT/OBJECTIVE-Cで設定する | ネイティブのJava/Kotlinで設定する |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### iOSのカスタマイズ

iOSでプッシュアクションボタン、カテゴリ、バッジ、またはカスタムサウンドを追加するには、ネイティブ設定をSWIFT`AppDelegate`またはOBJECTIVE-Cで実装する。[プッシュ通知のカスタマイズ方法については、SWIFTの]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift)ステップバイステップ手順を参照せよ。

### Androidのカスタマイズ

Androidでプッシュアクションボタン、カテゴリ、またはカスタム通知ファクトリを追加するには、Androidプロジェクト内でネイティブ設定を実装する。[プッシュ通知のカスタマイズ方法]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android)については[、Android版の]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android)ステップを参照せよ。
