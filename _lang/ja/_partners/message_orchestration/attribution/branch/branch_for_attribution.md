---
nav_title: Branch (アトリビューション)
article_title: Branch (アトリビューション)
alias: /partners/branch_for_attribution/
description: "この参考記事では、あらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援するモバイルリンクプラットフォームであるBrazeとBranchのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# Branch (アトリビューション) {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/) はあらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援するモバイルリンクプラットフォームで、すべてのユーザータッチポイントの一元的なビューを提供しています。

_この統合は Branch によって管理されます。_

## 統合について

Branch と Braze の統合では、堅牢なアトリビューションと[ディープリンク]({{site.baseurl}}/partners/message_orchestration/attribution/branch/branch_for_deeplinking/)により、ユーザーがいつ、どこで獲得されたかを正確に把握し、ユーザーのジャーニーをパーソナライズできるようになります。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Branch アカウント | このパートナーシップを活用するには、Branch アカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOS アプリと Android アプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| ブランチSDK | 必要な Braze SDK に加えて、[Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview) をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:デバイスIDをマップする

#### Android 

Android アプリを使用している場合は、Braze のデバイス ID を Branch に渡す必要があります。この ID は、Branch SDK の `setRequestMetadataKey()` メソッドで設定できます。`initSession`を呼び出す前に、次のコードスニペットを含める必要があります。また、Branch SDK でリクエストメタデータを設定する前に、Braze SDK を初期化する必要があります。

{% tabs ローカル %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
2023年2月までは、Branch アトリビューション統合は、iOS アトリビューションデータを照合するための主な識別子として IDFV を使用していました。Objective-C を使用している Braze のお客様は、サービスが中断されることはないため、インストール時に Braze`device_id` を取得して Branch に送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0+ を使用しているお客様は、相互識別子として IDFV を引き続き使用するには、`useUUIDAsDeviceId` フィールドが `false` に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。 

`true` に設定している場合、Brazeが iOS アトリビューションを適切に照合できるように、アプリのインストール時に Branch に Braze`device_id` を渡すために、Swift用の iOS デバイス ID マッピングを実装する必要があります。

{% tabs ローカル %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### ステップ2:Brazeデータインポートキーを取得する

Brazeで、[**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Branch**] を選択します。 

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。Branch のダッシュボードでポストバックを設定する場合、次のステップでデータインポートキーと REST エンドポイントが使用されます。<br><br>![Branch テクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されている。][4]{: style="max-width:90%;"}

### ステップ3:データフィードを設定する

1. Branch の**エクスポート**セクションで、**データフィード**を選択します。
2. **データフィードマネージャー**ページで、ページ上部の**データ統合**タブを選択します。 
3. 利用可能なデータパートナーのリストから Braze を選択します。 
4. Braze エクスポートページで、Braze ダッシュボードで見つけたデータインポートキーと REST エンドポイントを入力し、**有効**を選択します。

### ステップ4:統合を確認する

Braze が Branch からアトリビューションデータを受信すると、Braze の Branch テクノロジーパートナーページのステータス接続インジケーターが [接続されていません] から [接続済み] に変わります。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。Branch のポストバックから除外する必要があるオーガニックインストールは、Braze の API では無視され、接続の確立が成功したかどうかを判断する際に考慮されません。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。

## Braze での Branch クリックトラッキング URL (オプション)

Brazeのキャンペーンでクリック追跡リンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROI を最大化するためにどこにリソースを投資すべきかについて、データに基づいた意思決定ができるようになります。

Branch のクリックトラッキングリンクを使用するには、Branchの[ドキュメント](https://help.branch.io/using-branch/docs/ad-links)を参照してください。Braze のキャンペーンに Branch のクリックトラッキングリンクを直接挿入できます。その後 Branch は、リンクをクリックしたユーザーを紐づけるため、Branch の[確率的アトリビューション手法](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings)を使用します。Braze キャンペーンのアトリビューションの精度向上のために、Branch トラッキングリンクにデバイス識別子を付加することをお勧めします。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab Android %}
Android の場合、Braze ではお客様が [Google 広告 ID (GAID) 収集]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAID はまた、Branch SDK 統合によってネイティブに収集されます。以下の Liquid ロジックを利用して、Branch のクリックトラッキングリンクに GAID を組み込むことができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとBranchの両方が、SDKの統合を通じてネイティブにIDFVを自動的に収集する。これはデバイス識別子として使用できる。以下の Liquid ロジックを利用して、Branch のクリックトラッキングリンクに IDFV を組み込むことができます。

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
**この推奨事項の適用は完全に任意です。**<br>
現在、クリック追跡リンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、ブランチは確率的モデリングによってこれらのクリックを識別することができる。
{% endalert %}


[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhook"
[4]: {% image_buster /assets/img/attribution/branch.png %}
