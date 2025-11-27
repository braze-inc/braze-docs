## Roku SDKを統合する

### ステップ 1: ファイルの追加

Braze SDK ファイルは、[Braze Roku SDK リポジトリ](https://github.com/braze-inc/braze-roku-sdk) の `sdk_files` ディレクトリにあります。

1. `source` ディレクトリで、アプリに `BrazeSDK.brs` を追加します。
2. `components` ディレクトリで、アプリに `BrazeTask.brs` と `BrazeTask.xml` を追加します。

### ステップ 2:参照の追加

次の `script` 要素を使用して、メインシーンに `BrazeSDK.brs` への参照を追加します。

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### ステップ3:構成

`main.brs` 内で、グローバルノードにBrazeのコンフィギュレーションを設定する：

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

[SDK エンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)と API キーは、Braze ダッシュボード内にあります。

### ステップ4: Braze の初期化

Braze インスタンスを初期化します。

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## オプション構成

### ロギング

Braze 統合をデバッグするため、Braze ログの Roku デバッグコンソールを表示できます。詳細については、Roku Developers の [Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) を参照してください。
