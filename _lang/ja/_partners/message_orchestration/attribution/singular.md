---
nav_title: Singular
article_title:Singular
alias: /partners/singular/
description:「この参考記事では、有料インストールアトリビューションデータをインポートできる統合マーケティング分析プラットフォームであるBrazeとSingular のパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner

---

# Singular

> Singular は、アトリビューション、コスト集計、マーケティング分析、クリエイティブレポート、ワークフローオートメーションを提供する統合マーケティング分析プラットフォームです。

BrazeとSingular の統合により、有料インストールアトリビューションデータをインポートして、ライフサイクルキャンペーン内でインテリジェントにSegment できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Singular 口座 | このパートナーシップを利用するには、Singular アカウントが必要です。 |
| iOS またはAndroid アプリ | このインテグレーションは iOS アプリと Android アプリをサポートします。プラットフォームによっては、アプリケーションにコードスニペットが必要な場合があります。これらの要件の詳細は、統合プロセスのステップ1に記載されています。 |
| Singular SDK | 必要な Braze SDK に加えて、[Singular](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S) SDK をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:ユーザー ID のマッピング

#### Android

Androidアプリをお持ちの場合は、次のコードスニペットを含める必要があります。これにより、固有のBrazeユーザー ID がSingular に渡されます。

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
2023年2月以前は、Singular アトリビューション統合では、iOSのアトリアトリビューションデータを照合するためのプライマリ識別子としてIDFVを使用していました。Objective-Cを使用しているBrazeのお客様は、サービスが中断されないため、`device_id`インストール時にBrazeを取り出してSingular に送る必要はありません。
{% endalert%}

Swift SDK v5.7.0以降を使用している場合、引き続きIDFVを相互識別子として使用する場合は、`useUUIDAsDeviceId``false`統合が中断されないようにフィールドがに設定されていることを確認する必要があります。 

に設定した場合`true`、BrazeがiOSのアトリビューションと適切に一致するようにするには、アプリ`device_id`インストール時にBrazeをSSingular に渡すために、SwiftのiOSデバイスIDマッピングを実装する必要があります。

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### ステップ2:Braze データインポートキーを取得

**Braze で、**パートナーインテグレーション > テクノロジーパートナーに移動し****、Singular** を選択します。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。 

統合を完了するには、データインポートキーとRESTエンドポイントをSingular アカウントマネージャーに提供する必要があります。<br><br>![この画像, 写真は、SSingular テクノロジーページにある「インストールアトリビューションのデータインポート」ボックスを示しています。このボックスには、データインポートキーと REST エンドポイントが表示されます。][4]{: style="max-width:90%;"}

### ステップ3:統合を確認する

BrazeがSingular からアトリビューションデータを受信すると、BrazeのSingular テクノロジーパートナーページのステータス接続インジケーターが「未接続」から「接続済み」に変わります。最後に成功したリクエストのタイムスタンプも含まれます。 

なお、アトリビューションされたインストールに関するデータを受け取るまでは発生しません。SSingular ポストバックから除外すべきオーガニックインストールは、APIでは無視され、接続が確立されたかどうかを判断する際にはカウントされません。

## フェイスブックとX（旧ツイッター）アトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーがそのデータを Braze に送信することはできません。

## Braze のSingular クリックトラッキング, 追跡 URL (オプション)

Brazeキャンペーンでクリックトラッキング, 追跡リンクを使用すると、どのキャンペーンがアプリインストールとエンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定し、ROIを最大化するためにどこにより多くのリソースを投資すべきかについてデータドリブン型のの意思決定を行うことができます。

Singular クリックトラッキング, 追跡リンクを使い始めるには、[リンク先のドキュメントをご覧ください](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true)。Singular クリックトラッキング, 追跡リンクをBrazeキャンペーンに直接挿入できます。その後、Singular [は確率的アトリビューション手法を用いて](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true)、リンクをクリックしたユーザーアトリビューションします。Brazeキャンペーンのアトリビューションの精度を向上させるために、Singular トラッキング, 追跡リンクにデバイス識別子を追加することをおすすめします。これにより、リンクをクリックしたユーザー確定的に属性します。

{% tabs local %}
{% tab Android %}
Android の場合、Braze ではユーザーが [Google 広告 ID コレクション（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）へのオプトインを許可しています。また、GAID は Singular SDK インテグレーションを通じてネイティブに収集されます。以下のLiquidロジックを利用して、Singular クリックトラッキング, 追跡リンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとSingular の両方がSDKインテグレーションを通じてIDFVをネイティブに自動的に収集します。これはデバイス識別子として使用できます。以下のLiquidロジックを利用して、IDFVをSingular クリックトラッキング, 追跡リンクに含めることができます。

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**この推奨はあくまで任意です。**<br>
現在、クリックトラッキング, 追跡リンクでIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Singular は確率的モデリングを通じてこれらのクリックを属性ビューションできます。
{% endalert %}

[4]: {% image_buster /assets/img/attribution/singular.png %}
