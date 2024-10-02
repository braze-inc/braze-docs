---
nav_title: 帰属ブランチ
article_title: 帰属ブランチ
alias: /partners/branch_for_attribution/
description: "この参考記事では、あらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援するモバイルリンクプラットフォームであるBrazeとBranchのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# 帰属のためのブランチ {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> モバイルリンクプラットフォームである[Branchは](https://docs.branch.io/pages/integrations/braze/)、すべてのユーザータッチポイントを総合的に把握することで、あらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援する。

BrazeとBranchの統合は、ユーザーがいつ、どこで獲得されたかを正確に理解し、強固なアトリビューションと[ディープリンクを通じて]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/)、ユーザーのジャーニーをパーソナライズする方法を理解するのに役立つ。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 支店口座 | このパートナーシップを利用するには、支店口座が必要である。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。これらの要件の詳細は、統合プロセスのステップ1に記載されている。 |
| ブランチSDK | 必要なBraze SDKに加えて、[Branch SDKを](https://help.branch.io/developers-hub/docs/native-sdks-overview)インストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:デバイスIDをマップする

#### Android 

Androidアプリの場合、Branchに固有のBrazeデバイスIDを渡す必要がある。このIDは、Branch SDKの`setRequestMetadataKey()` 。`initSession` を呼び出す前に、以下のコード・スニペットをインクルードする必要がある。また、Branch SDKでリクエストメタデータを設定する前に、Braze SDKを初期化する必要がある。

{% tabs ローカル %}
{% tab ジャワ %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```
{% endtab %}
{% tab コトリン %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
2023年2月以前は、Branchのアトリビューション統合は、iOSのアトリビューションデータを照合するための主要な識別子としてIDFVを使用していた。Objective-Cを使用しているBrazeの顧客が、インストール時にBraze`device_id` を取得し、Branchに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+を使用している場合、相互識別子としてIDFVを引き続き使用したい場合は、`useUUIDAsDeviceId` フィールドが`false` に設定されていることを確認する必要があるため、統合が中断されることはない。 

`true` に設定した場合、BrazeがiOSアトリビュートに適切に一致するように、アプリインストール時にBranchにBraze`device_id` を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要がある。

{% tabs ローカル %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab スウィフト %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### ステップ2:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Branchを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。データインポートキーとRESTエンドポイントは、Branchのダッシュボードでポストバックを設定するときに、次のステップで使用される。<br><br>![この画像は、ブランチ・テクノロジー・ページにある "Data Import for Install Attribution "ボックスを示している。このボックスには、データ・インポート・キーとRESTエンドポイントが表示される。][4]{: style="max-width:90%;"}

### ステップ3:データフィードを設定する

1. ブランチの**エクスポートセクションで**、**データフィードを**クリックする。
2. **Data Feeds Manager**ページで、ページ上部の**Data Integrations**タブをクリックする。 
3. 利用可能なデータパートナーのリストからBrazeを選択する。 
4. Brazeのエクスポートページで、Brazeのダッシュボードで見つけたデータインポートキーとRESTエンドポイントを入力し、**Enableを**クリックする。

### ステップ4:統合を確認する

BrazeがBranchからアトリビューションデータを受信すると、BrazeのBranchテクノロジーパートナーページのステータス接続インジケータが "Not Connected "から "Connected "に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、帰属するインストールに関するデータを受け取るまでは起こらないことに注意してほしい。Branchのポストバックから除外されるべきオーガニックインストールは、APIによって無視され、成功した接続が確立されたかどうかを判断する際にカウントされない。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。

## BrazeのクリックトラッキングURLのブランチ（オプション）

Brazeのキャンペーンでクリック追跡リンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきか、データに基づいた意思決定ができるようになる。

Branchのクリック・トラッキング・リンクを使い始めるには、その[ドキュメントを](https://help.branch.io/using-branch/docs/ad-links)参照のこと。BrazeのキャンペーンにBranchのクリックトラッキングリンクを直接挿入することができる。ブランチは、リンクをクリックしたユーザーを[帰属](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings)さ[せる](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings)ために[、確率的帰属手法を](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings)使用する。Brazeキャンペーンからの帰属の精度を高めるために、Branchトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab アンドロイド %}
Androidの場合、Brazeは[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）にオプトインすることができる。GAIDはまた、Branch SDKの統合によってネイティブに収集される。以下のリキッドロジックを利用することで、ブランチのクリックトラッキングリンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとBranchの両方が、SDKの統合を通じてネイティブにIDFVを自動的に収集する。これはデバイス識別子として使用できる。以下のリキッドロジックを利用することで、ブランチのクリックトラッキングリンクにIDFVを含めることができる：

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**この推奨は純粋にオプションである。**<br>
現在、クリック追跡リンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、ブランチは確率的モデリングによってこれらのクリックを識別することができる。
{% endalert %}

[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "ブランチ・ウェブフック"
[4]: {% image_buster /assets/img/attribution/branch.png %}
