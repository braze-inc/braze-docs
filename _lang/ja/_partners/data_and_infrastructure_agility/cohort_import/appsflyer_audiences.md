---
nav_title: AppsFlyer Audiences
article_title:AppsFlyerオーディエンス
alias: /partners/appsflyer_audiences/
description:「この参考記事では、オーディエンスセグメントを効率的に構築してパートナーネットワークに接続できるAppsFlyerプラットフォームの機能であるBrazeとAppsFlyerオーディエンスのパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner

---

# AppsFlyerオーディエンス

> [この記事では、AppsFlyerオーディエンス統合を使用してAppsFlyerからBrazeにユーザーコホートをインポートする方法について説明します。][2][AppsFlyerと他の機能（モバイルアトリビューションなど）の統合について詳しくは、AppsFlyerのメイン記事を参照してください。][3]

## 前提条件

| 必要条件 | 説明 |
|---|---|
| アプリフライヤーアカウント | このパートナーシップを利用するには、AppsFlyerアカウントが必要です。 |
| iOS またはAndroid アプリ | このインテグレーションは iOS アプリと Android アプリをサポートします。プラットフォームによっては、アプリケーションにコードスニペットが必要な場合があります。これらの要件の詳細は、統合プロセスのステップ1に記載されています。 |
| AppsFlyer SDK | 必要な Braze SDK に加えて、[AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview) SDK をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## データインポート統合

### ステップ1:AppsFlyer SDKの設定

このインテグレーションを使用するには、AppsFlyer SDK `setPartnerData()` 関数を使用してユーザーのBraze外部IDをAppsFlyerに渡す必要があります。

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

### ステップ2:Braze データインポートキーを取得

**Brazeで、「**パートナー統合」>「テクノロジーパートナー****」に移動し、AppsFlyerを選択します**。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーとRESTエンドポイントは、AppsFlyerダッシュボードでポストバック設定する際のステップで使用されます。<br><br>![AppsFlyerテクノロジーページの「コホートインポートによるデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されます。][5]{: style="max-width:90%;"}

### ステップ3:AppsFlyerオーディエンスでBraze 接続を設定します

1. [AppsFlyerオーディエンスで][4]**、「**接続」タブに移動し、「パートナー接続を追加**」をクリックします。**
2. パートナーとして Braze を選択し、接続に名前を付けます。
3. データインポートキーと Braze REST エンドポイント。
4. 接続を保存すると、新規または既存のオーディエンススにリンクできるようになります。

![AppsFlyerオーディエンスプラットフォームパートナー接続設定ページ。画像の下部は、Braze外部IDボックスがチェックされていることを示しています。][6]{: style="max-width:80%;"}

### ステップ 4:BrazeでAppsFlyerオーディエンスコホートを使用する

**AppsFlyerオーディエンス Brazeにアップロードしたら、AppsFlyerコホートフィルターを選択することで、Brazeでセグメントを定義する際のフィルターとして使用できます。**

![ユーザー属性フィルター「AppsFlyerコホート」が選択されました。][7]

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: {{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}