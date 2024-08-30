---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "このリファレンス記事では、Braze と Kochava の提携について説明しています。Kochava はモバイルアトリビューションプラットフォームで、アトリビューションと分析のインサイトを提供し、データを活用して成長を促進します。"
page_type: partner
search_tag: Partner

---

# Kochava

> Kochavaは、成長のためにデータを活用するためのモバイルアトリビューションと分析を提供します。Kochavaオーディエンスプラットフォームは、アプリキャンペーンの計画、ターゲティング、アクティベーション、測定、および最適化を可能にします。

BrazeとKochavaの統合により、アトリビューションデータをBrazeに送信することで、インストール、アプリ内アクティビティなどを促進するキャンペーンをよりよく理解し、キャンペーンの全体的な理解を深めることができます。

## 前提条件

| 要件 | 説明 |
|---|---|
| Kochavaアカウント | このパートナーシップを利用するには、Kochavaアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合はiOSおよびAndroidアプリをサポートしています。プラットフォームによっては、アプリケーションにコードスニペットが必要な場合があります。これらの要件の詳細は、統合プロセスのステップ1にあります。 |
| Kochava SDK | 必須のBraze SDKに加えて、[Kochava SDK](https://support.kochava.com/sdk-integration/)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:ユーザーIDをマップする

#### Android

[Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDKは、セッション開始時にBraze IDとしてGUIDを生成します。これは、Brazeがデータを正しいユーザープロファイルに照合できるようにするために、Kochava `IdentityLink` メソッドに渡すことをお勧めする識別子です。Braze IDは次の方法で取得できます:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
2023年2月以前、当社のKochavaアトリビューション統合は、iOSアトリビューションデータを照合するための主要な識別子としてIDFVを使用していました。Brazeの顧客がサービスの中断がないため、インストール時にBraze`device_id`を取得してKochavaに送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0+を使用している方は、相互識別子としてIDFVを使用し続けたい場合、`useUUIDAsDeviceId`フィールドが`false`に設定されていることを確認して、統合が中断されないようにする必要があります。`true`に設定されている場合、アプリインストール時にBraze `device_id`をKochavaに渡すために、SwiftのiOSデバイスIDマッピングを実装する必要があります。これにより、BrazeはiOSのアトリビューションを適切に一致させることができます。

Brazeには2つのAPIがあり、1つは完了ハンドラを使用し、もう1つは新しいSWIFTの並行処理サポートを使用して同じ値を生成します。次のコードスニペットをKochavaの[iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/)の指示に従って修正する必要があることに注意してください。追加のヘルプが必要な場合は、Kochavaサポートに連絡してください。

##### 完了ハンドラ
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### SWIFTコンカレンシー
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### ステップ2:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Kochava** を選択します。 

{% alert note %}
古いナビゲーションを使用している場合は、統合の下にテクノロジーパートナーを見つけることができます。
{% endalert %}

ここでは、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成された後、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーとRESTエンドポイントは、Kochavaのダッシュボードでポストバックを設定する次のステップで使用されます。<br><br>![この画像は、Kochavaテクノロジーページにある「インストールアトリビューションのためのデータインポート」ボックスを示しています。このボックスには、データインポートキーとRESTエンドポイントが表示されます。][4]{: style="max-width:90%;"}

### ステップ3:Kochavaからのポストバックを設定する

[ポストバックを追加する][18] Kochava ダッシュボードで。Brazeのダッシュボードで見つけたデータインポートキーとRESTエンドポイントを求められます。

### ステップ4:統合を確認する

BrazeがKochavaからアトリビューションデータを受信すると、BrazeのKochavaテクノロジーパートナーページのステータス接続インジケーターが「未接続」から「接続済み」に変わります。最後の成功したリクエストのタイムスタンプも含まれます。 

このことは、帰属されたインストールに関するデータを受け取るまで発生しないことに注意してください。オーガニックインストールはKochavaポストバックから除外する必要があり、当社のAPIによって無視され、接続が成功したかどうかを判断する際にはカウントされません。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信することができません。

## BrazeでのKochavaクリックトラッキングURL（オプション）

Brazeキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールと再エンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定し、最大のROIを得るためにどこにリソースを投資するかについてデータドリブン型の意思決定を行うことができるようになります。

Kochavaのクリックトラッキングリンクを開始するには、[ドキュメント](https://support.kochava.com/reference-information/attribution-overview/)をご覧ください。BrazeキャンペーンにKochavaクリックトラッキングリンクを直接挿入できます。Kochavaはその後、[確率的アトリビューション方法論](https://www.kochava.com/getting-prepared-for-ios-14/)を使用して、リンクをクリックしたユーザーを属性します。Brazeキャンペーンからのアトリビューションの精度を向上させるために、Kochavaトラッキングリンクにデバイス識別子を追加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的に属性付けします。

{% tabs ローカル %}
{% tab Android %}
Androidの場合、Brazeを使用すると、顧客は[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAIDは、Kochava SDK統合を通じてネイティブに収集されます。次のLiquidロジックを利用して、KochavaクリックトラッキングリンクにGAIDを含めることができます:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとKochavaの両方が、SDK統合を通じてネイティブにIDFVを自動的に収集します。これはデバイスの識別子として使用できます。次のLiquidロジックを利用して、KochavaクリックトラッキングリンクにIDFVを含めることができます:

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
**この推奨事項は完全に任意です**<br>
現在、クリックトラッキングリンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または将来的に使用する予定がない場合でも、Kochavaは確率モデルを通じてこれらのクリックを属性付けすることができます。
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochavaポストバック"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
