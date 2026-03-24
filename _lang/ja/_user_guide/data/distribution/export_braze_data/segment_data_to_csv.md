---
nav_title: SegmentデータをCSVにエクスポート
article_title: セグメントデータをCSVにエクスポート
page_order: 2
page_type: reference
description: "このリファレンス記事では、セグメントデータをCSVにエクスポートする方法を説明します。"

---

# セグメントデータをCSVにエクスポート

> このページでは、セグメントからユーザーデータのCSVエクスポートをリクエストする方法と、エクスポートに含まれるデータについて説明します。

セグメントデータをCSVにエクスポートするには、セグメントの編集中に**User Data**ドロップダウンを選択し、そのセグメントのユーザーデータまたはメールアドレスのいずれかをエクスポートするように選択します。

![「ユーザーデータ」ドロップダウンにエクスポートオプションが表示されている「セグメントの詳細」セクション。]({% image_buster /assets/img_archive/csvexport.png %})

メインの**Segments**ページから、セグメントの<i class="fas fa-gear"></i>**設定**ドロップダウンを選択して、CSVエクスポートをリクエストすることもできます。

![メインのセグメントページの「設定」ドロップダウン。]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
すべてのユーザープロファイルからデータをエクスポートするには、フィルターなしでセグメントを作成し、CSVエクスポートをリクエストしてください。
{% endalert %}

CSV出力には、エクスポート時にセグメントに含まれる各ユーザープロファイルのデータが含まれます。歯車アイコンを選択してCSVエクスポートを選択することで、任意のセグメントをエクスポートできます。Brazeはバックグラウンドでレポートを生成し、現在ログインしているユーザーにメールで送信します。

{% alert important %} 
ファイルサイズの制限により、セグメントの推定サイズがユーザー数500,000人を超える場合、エクスポートに失敗する可能性があります。この制限は、セグメントの正確な計算ではなく推定サイズを使用することに注意してください。詳しくは、[大きなセグメントのエクスポート](#exporting-large-segments)を参照してください。
{% endalert %}

[Amazon S3の認証情報]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration)をBrazeにリンクしている場合、CSVは代わりにS3バケットのキー`segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`の下にアップロードされます。メールで届くダウンロードリンクにアクセスするには、ダッシュボードにログインしている必要があります。

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## エクスポートに含まれるデータ

以下のデータが、選択に応じてエクスポートに含まれます。

### CSVエクスポートユーザーデータ

| フィールド名                  | 説明                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 内部ID（変更不可）                           |
| country                     | 国                                    |
| created_at                  | ユーザープロファイルが作成された日時                   |
| created_from                | ユーザープロファイルの作成に使用された方法（例：REST API、SDK、CSVインポート）         |
| devices                     | デバイス情報                           |
| date_of_birth               | 生年月日                                            |
| email                       | メールアドレス                                            |
| unsubscribed_from_emails_at | メールの配信停止日                            |
| user_id                     | external ID                                              |
| first_name                  | 名                                               |
| first_session               | 初回セッションの日時                           |
| gender                      | 性別                                                   |
| google_ad_ids               | ユーザーに関連付けられたGoogle広告ID                      |
| city                        | 市区町村                                     |
| IDFAs                       | 広告用識別子（IDFA）の値                 |
| IDFVs                       | ベンダー識別子（IDFV）の値                      |
| language                    | ISO-639-1規格の言語                                        |
| last_app_version_used       | 最後に使用したアプリのバージョン                             |
| last_name                   | 姓                                                |
| last_session                | 最終セッションの日時                            |
| number_of_google_ad_ids     | 関連するGoogle広告IDの数               |
| number_of_IDFAs             | 関連するIDFAの数                                |
| number_of_IDFVs             | 関連するIDFVの数                                |
| number_of_push_tokens       | 関連するプッシュ通知トークンの数             |
| number_of_roku_ad_ids       | 関連するRoku広告IDの数                 |
| number_of_windows_ad_ids    | 関連するWindows広告IDの数              |
| phone_number                | 電話番号                                             |
| opted_into_push_at          | プッシュ通知にオプトインした日付                       |
| unsubscribed_from_push_at   | プッシュ通知の配信停止日                |
| random_bucket               | ランダムバケット番号                                 |
| roku_ad_ids                 | Roku広告ID                          |
| session_count               | セッションの総数                                 |
| timezone                    | IANAタイムゾーンデータベースと同じフォーマットによるユーザーのタイムゾーン                                         |
| in_app_purchase_total       | アプリ内購入の支出総額                   |
| user_aliases                | ユーザーエイリアスがある場合                                          |
| windows_ad_ids              | Windows広告ID                       |
| カスタムイベント               | エクスポート時の選択に基づく                             |
| カスタム属性           | エクスポート時の選択に基づく                             |
{: .reset-td-br-1 .reset-td-br-2 }

### メールアドレスをCSV形式でエクスポート

| フィールド名                  | 説明            |
| --------------------------- | ---------------------- |
| user_id                     | ユーザーのexternal ID     |
| first_name                  | 名             |
| last_name                   | 姓              |
| email                       | メール                  |
| unsubscribed_from_emails_at | メール配信停止日 |
| opted_in_to_emails_at       | メールオプトイン日      |
| user_aliases                | ユーザーエイリアスがある場合   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
CSVとAPIのエクスポートについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)の記事を参照してください。
{% endalert %} 

## 大きなセグメントのエクスポート

500,000人を超えるユーザーを含む大規模なユーザーセグメントをエクスポートするには、いくつかの方法があります。

{% tabs %}
{% tab Multiple segments %}

大きなセグメントを小さなセグメントに分割し、それぞれの小さなセグメントをBrazeからエクスポートできます。 

{% endtab %}
{% tab Random bucket numbers %}

また、[ランダムバケット番号]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/)を使用して、ユーザー群を複数のセグメントに分割し、エクスポート後にそれらを組み合わせることもできます。例えば、セグメントを2つの異なるセグメントに分割する必要がある場合は、次のフィルターを使用できます。
- セグメント1：ランダムバケット番号が5000未満（0～4999を含む）
- セグメント2：ランダムバケット番号が4999より大きい（5000～9999を含む）

{% endtab %}
{% tab Endpoints %}

また、次のエンドポイントを利用して、特定のセグメントのユーザーデータをエクスポートすることもできます。これらのエンドポイントはデータ制限の対象となりますのでご注意ください。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}