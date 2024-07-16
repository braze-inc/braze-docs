---
nav_title: Adjust
article_title:Adjust
alias: /partners/adjust/
description:「この参考記事では、BrazeとAdjustのパートナーシップについて概説しています。Adjustはモバイルアトリビューションと分析を行う企業です。これにより、非オーガニックインストールアトリビューションデータをインポートして、ライフサイクルキャンペーン内でよりインテリジェントにSegment 化できるようになります。「
page_type: partner
search_tag:Partner

---

# Adjust

> [Adjustは](https://www.adjust.com/)、広告ソースアトリビューションと高度な分析組み合わせてビジネスインテリジェンススを包括的に把握するモバイルアトリビューションビューションおよび分析企業です。

BrazeとAdjustの連携により、非オーガニックインストールアトリビューションデータをインポートして、ライフサイクルキャンペーン内でよりインテリジェントにSegment 化できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| アカウントをAdjust | このパートナーシップを利用するには、Adjustアカウントが必要です。 |
| iOS またはAndroid アプリ | このインテグレーションは iOS アプリと Android アプリをサポートします。プラットフォームによっては、アプリケーションにコードスニペットが必要な場合があります。これらの要件の詳細は、統合プロセスのステップ1に記載されています。 |
| SDKをAdjust | 必要なBraze SDKに加えて、Adjust [SDKをインストールする必要があります](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk)。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:デバイス ID のマッピング

#### Android

Androidアプリをお持ちの場合は、固有のBrazeデバイスIDをAdjustに渡す必要があります。このIDはAdjust `addSessionPartnerParameter()` SDKのメソッドで設定できます。SDK を初期化する前に、次のコードスニペットを含める必要があります `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and sent to Adjust upon install as there will be no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to Adjust upon app install in order for Braze to appropriately match iOS attributions.
--->

{% tabs local %}
{% tab Objective-C %}

iOSアプリをお使いの場合、IDFVはAdjustによって収集され、Brazeに送信されます。その後、この ID は Braze の一意のデバイス ID にマッピングされます。

[iOS 14アップグレードガイドで説明されているように、BrazeでIDFAを収集する場合、BrazeはオプトインしたユーザーのIDFA値を引き続き保存します。]({{site.baseurl}}/android_12/)それ以外の場合は、IDFVがユーザーをマップするためのフォールバック識別子として使用されます。

{% endtab %}
{% tab Swift %}

iOSアプリをお持ちの場合は、`useUUIDAsDeviceId`フィールドを設定してIDFVを収集することを選択できます。`false`設定されていない場合、iOSアトリビューションはAdjustからBrazeに正確にマッピングされない可能性があります。詳細については、「[IDFV の収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
インストール後のイベントをAdjustからBrazeに送信する予定の場合は、以下のことを行う必要があります。<br><br>1) Adjust SDK内でセッション`external_id`およびイベントパラメーターとして追加してください。収益イベントの転送では、`product_id`イベントのパラメーターとしても設定する必要があります。[イベント転送のパートナーパラメーターの定義について詳しくは、Adjustのドキュメントをご覧ください](https://github.com/adjust/sdks)。<br><br>2) Adjustに入力する新しいAPI キーを生成します。これを行うには、Brazeダッシュボード Adjustパートナーページにある「**APIキーを生成**」ボタンを選択します。
{% endalert %}

### ステップ2:Braze データインポートキーを取得

**Braze で、\[**インテグレーション**] > \[**テクノロジーパートナー**] に移動し、\[Adjust] を選択します。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーとRESTエンドポイントは、Adダッシュボードでポストバック設定するステップで使用されます。<br><br>![この画像, 写真は、Adjustのテクノロジーページにある「インストールアトリビューションのデータインポート」ボックスを示しています。このボックスには、データインポートキーと REST エンドポイントが表示されます。][1]{: style="max-width:90%;"}

### ステップ3:AdjustでBraze を設定

1. Adダッシュボードで、\[**アプリ設定] に移動し、\[パートナー設定**]、\[****パートナーの追加****] の順に移動します。
2. **Braze (旧Appboy)** を選択し、データインポートキーと Braze REST エンドポイント。
3. \[**保存して閉じる**] をクリックします。

### ステップ 4:統合を確認する

BrazeがAdjustからアトリビューションデータを受信すると、BrazeのAdjustテクノロジーパートナーページのステータス接続インジケーターが「未接続」から「接続済み」に変わります。最後に成功したリクエストのタイムスタンプも含まれます。 

なお、アトリビューションされたインストールに関するデータを受け取るまでは発生しません。Adjustのポストバックから除外すべきオーガニックインストールはAPIでは無視され、接続が確立されたかどうかを判断する際にはカウントされません。

## 使用可能なデータフィールド

提案どおりに連携を設定した場合、BrazeはAdjustのデータを次の表に示すようにSegment フィルターにマッピングします。

| データフィールドをAdjust | Braze Segment フィルター |
| --- | --- |
| `{network_name}` | 属性付きソース |
| `{campaign_name}` | アトリビューションキャンペーン |
| `{adgroup_name}` | アトリビューション広告グループ |
| `{creative_name}` | アトリビューション広告 |
{: .reset-td-br-1 .reset-td-br-2}

## フェイスブックとX（旧ツイッター）アトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーがそのデータを Braze に送信することはできません。

## Braze でのクリックトラッキング, 追跡 URL のAdjust (オプション)

Brazeキャンペーンでクリックトラッキング, 追跡リンクを使用すると、どのキャンペーンがアプリインストールとエンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定し、ROIを最大化するためにどこにより多くのリソースを投資すべきかについてデータドリブン型のの意思決定を行うことができます。

Adjustのクリックトラッキング, 追跡リンクを使い始めるには、[Adjustのドキュメントをご覧ください](https://help.adjust.com/tracking/attribution/tracker-urls)。Adjustのクリックトラッキング, 追跡リンクをBrazeキャンペーンに直接挿入できます。その後、[Adjustは確率的アトリビューション手法を用いて](https://www.adjust.com/blog/attribution-compatible-with-ios14/)、リンクをクリックしたユーザーアトリビューションします。Brazeキャンペーンのアトリビューションの精度を向上させるために、Adjustのトラッキング, 追跡リンクにデバイス識別子を追加することをおすすめします。これにより、リンクをクリックしたユーザー確定的に属性します。

{% tabs local %}
{% tab Android %}
Android の場合、Braze ではユーザーが [Google 広告 ID コレクション（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection)）へのオプトインを許可しています。また、GAIDはAdjust SDKインテグレーションを通じてネイティブに収集されます。以下のLiquidロジックを利用して、Adjustのクリックトラッキング, 追跡リンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAdjustの両方がSDKインテグレーションを通じてIDFVをネイティブに自動的に収集します。これはデバイス識別子として使用できます。以下のLiquidロジックを利用して、Adjustのクリックトラッキング, 追跡リンクにIDFVを含めることができます。

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
現在、クリックトラッキング, 追跡リンクでIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Adjustは確率的モデリングを通じてこれらのクリックを属性することができます。
{% endalert %}

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
