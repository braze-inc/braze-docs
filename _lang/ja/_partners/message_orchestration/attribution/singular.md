---
nav_title: 単数形
article_title: 単数形
alias: /partners/singular/
description: "この参考記事では、BrazeとSingularのパートナーシップについて概説している。Singularは、統合マーケティング分析プラットフォームで、有料インストーラのアトリビューションデータをインポートすることができる。"
page_type: partner
search_tag: Partner

---

# 単数形

> Singularは、アトリビューション、コスト集計、マーケティング分析、クリエイティブレポート、ワークフローの自動化を実現する統合マーケティング分析プラットフォームである。

BrazeとSingularの統合により、有料インストーラのアトリビューションデータをインポートして、ライフサイクルキャンペーン内でインテリジェントにセグメントすることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 単一アカウント | このパートナーシップを利用するには、Singularアカウントが必要である。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。これらの要件の詳細は、統合プロセスのステップ1に記載されている。 |
| シンギュラーSDK | 必要なBraze SDKに加えて、[Singular SDKを](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S)インストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

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
2023年2月以前は、当社のSingularアトリビューション統合は、iOSアトリビューションデータを照合するための主要識別子としてIDFVを使用していた。Objective-Cを使用しているBrazeの顧客が、インストール時にBraze`device_id` を取得し、Singularに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+を使用している場合、相互識別子としてIDFVを引き続き使用したい場合は、`useUUIDAsDeviceId` フィールドが`false` に設定されていることを確認する必要があるため、統合が中断されることはない。 

`true` に設定した場合、BrazeがiOSアトリビュートに適切に一致するように、アプリインストール時にSingularにBraze`device_id` を渡すために、Swift用にiOSデバイスIDマッピングを実装する必要がある。

{% tabs ローカル %}
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

Brazeで、**Partner Integrations**>**Technology Partnersと**進み、**Singularを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。 

統合を完了するには、データインポートキーとRESTエンドポイントをSingularアカウントマネージャーに提供する必要がある。<br><br>![この画像は、Singularテクノロジーのページにある「Data Import for Install Attribution」ボックスを示している。このボックスには、データ・インポート・キーとRESTエンドポイントが表示される。][4]{: style="max-width:90%;"}

### ステップ3:統合を確認する

BrazeがSingularからアトリビューションデータを受信すると、BrazeのSingularテクノロジーパートナーページのステータス接続インジケーターが、"Not Connected "から "Connected "に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、帰属するインストールに関するデータを受け取るまでは起こらないことに注意してほしい。Singularのポストバックから除外されるべきオーガニック・インストールは、APIによって無視され、接続が成功したかどうかを判断する際にカウントされない。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。

## Brazeの単一クリックトラッキングURL（オプション）

Brazeのキャンペーンでクリック追跡リンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきか、データに基づいた意思決定ができるようになる。

Singularクリック・トラッキング・リンクを使い始めるには、[ドキュメントを](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true)参照すること。SingularのクリックトラッキングリンクをBrazeのキャンペーンに直接挿入することができる。その後、Singularは[確率的アトリビューション手法を用いて](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true)、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからの帰属の精度を高めるために、Singularトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab アンドロイド %}
Androidの場合、Brazeは[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）にオプトインすることができる。GAIDはまた、Singular SDKの統合によってネイティブに収集される。以下のLiquidロジックを利用することで、SingularクリックトラッキングリンクにGAIDを含めることができる：
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
**この推奨は純粋にオプションである。**<br>
現在、クリックトラッキングのリンクにIDFVやGAIDのようなデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Singularは確率的モデリングによってこれらのクリックを識別することができる。
{% endalert %}

[4]: {% image_buster /assets/img/attribution/singular.png %}
