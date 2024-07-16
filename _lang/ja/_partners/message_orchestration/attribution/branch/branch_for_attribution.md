---
nav_title: アトリビューションBranch
article_title:アトリビューションBranch
alias: /partners/branch_for_attribution/
description:「この参考記事では、あらゆるデバイス、チャネル、プラットフォームにわたる獲得、エンゲージメント、測定を支援するモバイルリンクプラットフォームであるBrazeとBranchのパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner

---

# アトリビューション用Branch {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [モバイルリンクプラットフォームであるBranchは](https://docs.branch.io/pages/integrations/braze/)、すべてのユーザーータッチポイントの全体像を提供することで、すべてのデバイス、チャネル、プラットフォームにわたる獲得、エンゲージメント、測定を支援します。

[BrazeとBranchの統合により、いつ、どこでユーザーが獲得されたかを正確に把握できるだけでなく、堅牢なアトリビューションとディープリンクを通じてユーザーのジャーニーをパーソナライズする方法も理解できます。]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/)

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Branch 口座 | このパートナーシップを利用するには、Branch アカウントが必要です。 |
| iOS またはAndroid アプリ | このインテグレーションは iOS アプリと Android アプリをサポートします。プラットフォームによっては、アプリケーションにコードスニペットが必要な場合があります。これらの要件の詳細は、統合プロセスのステップ1に記載されています。 |
| Branch SDK | 必要な Braze SDK に加えて、[Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview) をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:デバイス ID のマッピング

#### Android 

Android アプリをお持ちの場合は、一意の Braze デバイス ID をBranch に渡す必要があります。この ID はBranch SDK `setRequestMetadataKey()` のメソッドで設定できます。`initSession`呼び出す前に、次のコードスニペットを含める必要があります。また、Branch SDK でリクエストメタデータを設定する前に Braze SDK を初期化する必要があります。

{% tabs local %}
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
2023年2月以前は、Branchアトリビューション統合では、iOSのアトリアトリビューションデータを照合するためのプライマリ識別子としてIDFVを使用していました。Objective-Cを使用しているBrazeのお客様は、サービスが中断されないため、`device_id`インストール時にBrazeを取り出してBranchに送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0以降を使用している場合、引き続きIDFVを相互識別子として使用する場合は、`useUUIDAsDeviceId``false`統合が中断されないようにフィールドがに設定されていることを確認する必要があります。 

に設定した場合`true`、BrazeがiOSのアトリビューションと適切に一致するようにするには、アプリ`device_id`インストール時にBrazeをBranchに渡すために、SwiftのiOSデバイスIDマッピングを実装する必要があります。

{% tabs local %}
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

### ステップ2:Braze データインポートキーを取得

**Braze で、\[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[Branch] を選択します。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーと REST エンドポイントは、ステップで Branch のダッシュボードでポストバック設定するときに使用されます。<br><br>![この画像, 写真は、Branch テクノロジーページにある「インストールアトリビューションのデータインポート」ボックスを示しています。このボックスには、データインポートキーと REST エンドポイントが表示されます。][4]{: style="max-width:90%;"}

### ステップ3:データフィードの設定

1. Branch の「**エクスポート**」セクションで、「**データフィード**」をクリックします。
2. **データフィードマネージャーページで**、ページ上部の「**データ統合**」タブをクリックします。 
3. 利用可能なデータパートナーのリストから Braze を選択します。 
4. **Braze エクスポートページで、Braze のダッシュボードで見つかったデータインポートキーと REST エンドポイントを入力し、\[有効にする] をクリックします。**

### ステップ 4:統合を確認する

BrazeがBranchからアトリビューションデータを受信すると、BrazeのBranch テクノロジーパートナーページのステータス接続インジケーターが「未接続」から「接続済み」に変わります。最後に成功したリクエストのタイムスタンプも含まれます。 

なお、アトリビューションされたインストールに関するデータを受け取るまでは発生しません。Branch ポストバックから除外すべきオーガニックインストールはAPIでは無視され、接続が確立されたかどうかを判断する際にはカウントされません。

## フェイスブックとX（旧ツイッター）アトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーがそのデータを Braze に送信することはできません。

## Braze のBranch クリックトラッキング, 追跡 URL (オプション)

Brazeキャンペーンでクリックトラッキング, 追跡リンクを使用すると、どのキャンペーンがアプリインストールとエンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定し、ROIを最大化するためにどこにより多くのリソースを投資すべきかについてデータドリブン型のの意思決定を行うことができます。

Branch のクリックトラッキング, 追跡リンクを使い始めるには、[リンク先のドキュメントを参照してください](https://help.branch.io/using-branch/docs/ad-links)。Branch クリックトラッキング, 追跡リンクは Braze キャンペーンに直接挿入できます。その後、[Branchは確率的アトリビューション手法を用いて](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings)、リンクをクリックしたユーザーアトリビューションします。Brazeキャンペーンのアトリビューションの精度を向上させるために、Branchトラッキング, 追跡リンクにデバイス識別子を追加することをおすすめします。これにより、リンクをクリックしたユーザー確定的に属性します。

{% tabs local %}
{% tab Android %}
Android の場合、Braze ではユーザーが [Google 広告 ID コレクション（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）へのオプトインを許可しています。また、GAID は Branch SDK インテグレーションを通じてネイティブに収集されます。以下のLiquidロジックを利用して、Branch クリックトラッキング, 追跡リンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとBranchの両方がSDKインテグレーションを通じてIDFVをネイティブに自動的に収集します。これはデバイス識別子として使用できます。次の Liquid ロジックを利用して、Branch クリックトラッキング, 追跡リンクに IDFV を含めることができます。

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
**この推奨はあくまで任意です。**<br>
現在、クリックトラッキング, 追跡リンクでIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Branchは確率的モデリングを通じてこれらのクリックを属性することができます。
{% endalert %}

[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch ウェブフック"
[4]: {% image_buster /assets/img/attribution/branch.png %}
