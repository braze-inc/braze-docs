---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "このリファレンス記事では、Braze と Singular のパートナーシップについて説明します。Singular は、有料インストールアトリビューションデータをインポートできる統合マーケティング分析プラットフォームです。"
page_type: partner
search_tag: Partner

---

# Singular

> [Singularは](https://www.singular.net/)、アトリビューション、コスト集計、マーケティング分析、クリエイティブレポート、ワークフローオートメーションを提供する統合マーケティング分析プラットフォームである。

_この統合は Singular によって管理されます。_

## 統合について

BrazeとSingularの統合により、有料インストーラのアトリビューションデータをインポートして、ライフサイクルキャンペーン内でインテリジェントにセグメントすることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Singular アカウント | このパートナーシップを活用するには、Singular アカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOS アプリと Android アプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| シンギュラーSDK | 必要な Braze SDK に加えて、[Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S) をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:ユーザーIDをマップする

#### Android

Androidアプリをお持ちの場合は、SingularにBrazeのユニークなユーザーIDを渡す、以下のコードスニペットを含める必要がある。

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
2023年2月以前は、Singularのアトリビューション統合は、iOSアトリビューションデータを照合するための主要識別子としてIDFV（Identifier for Vendor）を使用していた。OBJECTIVE-Cを使用しているBraze顧客は、サービスの中断がないため、インストール時にBraze`device_id` を取得し、Singularに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+ を使用しているお客様は、相互識別子として IDFV を引き続き使用するには、`useUUIDAsDeviceId` フィールドが `false` に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。 

`true` に設定している場合、Brazeが iOS アトリビューションを適切に照合できるように、アプリのインストール時に Singular に Braze`device_id` を渡すために、Swift用の iOS デバイス ID マッピングを実装する必要があります。

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

### ステップ2:Brazeデータインポートキーを取得する

Brazeで、[**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Singular**] を選択します。 

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。 

統合を完了するには、データインポートキーとRESTエンドポイントをSingularアカウントマネージャーに提供する必要がある。<br><br>![Singular テクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されている。]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### ステップ3:統合を確認する

Braze が Singular からアトリビューションデータを受信すると、Braze の Singular テクノロジーパートナーページのステータス接続インジケーターが [接続されていません] から [接続済み] に変わります。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。Singular のポストバックから除外する必要があるオーガニックインストールは、Braze の API では無視され、接続の確立が成功したかどうかを判断する際に考慮されません。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。

## Brazeの単一クリックトラッキングURL（オプション）

Brazeのキャンペーンでクリック追跡リンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROI を最大化するためにどこにリソースを投資すべきかについて、データに基づいた意思決定ができるようになります。

Singularクリック・トラッキング・リンクを使い始めるには、[ドキュメントを](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true)参照すること。SingularのクリックトラッキングリンクをBrazeのキャンペーンに直接挿入することができる。その後、Singularは[確率的アトリビューション手法を用いて](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true)、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからの帰属の精度を高めるために、Singularトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーを決定論的に属性付けします。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeを使用すると、顧客は[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAID はまた、Singular SDK統合によってネイティブに収集されます。以下のLiquidロジックを利用することで、SingularクリックトラッキングリンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとSingularの両方が、SDKの統合を通じてネイティブにIDFVを自動的に収集する。これはデバイス識別子として使用できる。以下のリキッドロジックを利用することで、シンギュラークリックトラッキングリンクにIDFVを含めることができる：

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
**この推奨事項の適用は完全に任意です。**<br>
現在、クリックトラッキングのリンクにIDFVやGAIDのようなデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Singularは確率的モデリングによってこれらのクリックを識別することができる。
{% endalert %}


