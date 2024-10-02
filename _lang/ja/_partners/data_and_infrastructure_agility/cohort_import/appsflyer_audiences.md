---
nav_title: AppsFlyerの利用者
article_title: AppsFlyerの利用者
alias: /partners/appsflyer_audiences/
description: "このリファレンス記事では、Braze とAppsFlyer オーディエンス s 間のパートナーシップについて説明します。これは、AppsFlyer プラットフォームの機能で、オーディエンス Segment s を効率的に構築し、パートナーネットワークに接続することができます。"
page_type: partner
search_tag: Partner

---

# AppsFlyerの利用者

> ここでは、[AppsFlyer Audiences][2]統合を使用して、AppsFlyerからBrazeにユーザー コホートを読み込む方法について説明します。AppsFlyerとその他の機能(携帯アトリビューションなど)の統合の詳細については、メインの[AppsFlyerの記事][3]を参照してください。

## 前提条件

| 要件 | 説明 |
|---|---|
| AppsFlyerアカウント | AppsFlyerアカウントは、この提携の事前タグeを考慮する必要があります。 |
| iOSやAndroid アプリ | この統合は、iOS とAndroid アプリ s をサポートします。お使いのプラットフォームによっては、アプリのライセンスにコードの抜粋が必要な場合があります。これらの要件の詳細は、インテグレーションプロセスの第1ステップに記載されています。 |
| AppsFlyer SDK | 必要なBraze SDKに加えて、[AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## データインポート統合

### ステップ1:AppsFlyer SDKの設定

この統合を使用するには、AppsFlyer SDKの`setPartnerData()` 関数を使用して、ユーザーのBraze外部ID をAppsFlyer に渡す必要があります。

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

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Technology Partners** は**Integrations** にあります。
{% endalert %}

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとREST エンドポイントは、AppsFlyerのダッシュボードでポストバックアップを設定するときに次回のステップで使用されます。<br><br>![AppsFlyerテクノロジページの"Data Import Using Cohort Import"ボックスデータインポートキーとREST エンドポイントが表示されます。][5]{: style="max-width:90%;"}

### ステップ3:AppsFlyer オーディエンスでのBraze コネクションの設定

1. [AppsFlyer Audiences][4]で、**Connections**タブに移動し、**Add partner connection**をクリックします。
2. パートナーとしてBraze を選択し、コネクションに名前を付けます。
3. データインポートキーとBraze REST エンドポイントを入力します。
4. 接続を保存すると、新規または既存のオーディエンスにリンクできるようになります。

![AppsFlyer オーディエンスは、プラットフォームパートナ接続設定ページを表示します。"画像sの下部には、Brazeの外部IDがチェックされていることが表示されます。][6]{: style="max-width:80%;"}

### ステップ 4:Braze でのAppsFlyer オーディエンスコホートの使用

AppsFlyer オーディエンスがアップロードされてBrazeされると、**AppsFlyer Cohorts**フィルターを選択して、BrazeでSegmentsを定義するときにフィルターとして使用できます。

![ユーザ属性s フィルター "AppsFlyer Cohorts"選択。][7]

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: {{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}