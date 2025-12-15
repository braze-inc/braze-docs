---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "このリファレンス記事では、Braze と AppsFlyer Audiences のパートナーシップについて説明します。AppsFlyer Audiences は、オーディエンスセグメントを効率的に作成してパートナーネットワークに接続できる AppsFlyer プラットフォームの機能です。"
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> この記事では、[AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/) 統合を使用して AppsFlyer から Braze にユーザーコホートをインポートする方法について説明します。AppsFlyerとその他の機能(携帯アトリビューションなど)の統合の詳細については、メインの[AppsFlyerの記事]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/)を参照してください。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| AppsFlyerアカウント | このパートナーシップを活用するには、AppsFlyer アカウントが必要です。 |
| iOSやAndroid アプリ | この統合では、iOS アプリと Android アプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| AppsFlyer SDK | 必要なBraze SDKに加えて、[AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## データインポート統合

### ステップ1:AppsFlyer SDKの設定

この統合を使用するには、AppsFlyer SDK の`setPartnerData()` 関数を使用して、ユーザーの Braze external ID をAppsFlyer に渡す必要があります。

#### Android 
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### ステップ2:Braze データインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**AppsFlyer** を選択します。 

ここでRESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとREST エンドポイントは、AppsFlyerのダッシュボードでポストバックアップを設定するときに次回のステップで使用されます。<br><br>![AppsFlyer テクノロジーページの「コホートインポートを使用したデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されている。]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### ステップ3:AppsFlyer オーディエンスでのBraze コネクションの設定

1. [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections)で、**Connections**タブに移動し、**Add partner connection**をクリックします。
2. パートナーとしてBraze を選択し、コネクションに名前を付けます。
3. データインポートキーとBraze REST エンドポイントを入力します。
4. 接続を保存します。保存した接続は、新しいオーディエンスまたは既存のオーディエンスにリンクできます。

![AppsFlyer Audiences プラットフォームのパートナー接続設定ページ。画像下部で「Braze external ID」ボックスがオンになっている。]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### ステップ4:Braze でのAppsFlyer オーディエンスコホートの使用

AppsFlyer オーディエンスがアップロードされてBrazeされると、**AppsFlyer Cohorts**フィルターを選択して、BrazeでSegmentsを定義するときにフィルターとして使用できます。

![ユーザー属性フィルター「AppsFlyer Cohorts」アが選択されている。]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。

