---
nav_title: CSV へのセグメントデータのエクスポート
article_title: CSV へのセグメントデータのエクスポート
page_order: 2
page_type: reference
description: "このリファレンス記事では、セグメントデータを CSV にエクスポートする方法を説明します。"

---

# CSV へのセグメントデータのエクスポート

> このページでは、セグメントからのユーザデータのCSV エクスポートとエクスポートに含まれるデータをリクエストする方法について説明します。

セグメントデータをCSV にエクスポートするには、セグメントの編集中に**User Data** ドロップダウンを選択し、そのセグメントのユーザーデータまたは電子メールアドレスのいずれかをエクスポートするように選択します。

![ユーザーデータのドロップダウンにエクスポートオプションが表示されたセグメンテーションの詳細セクション]({% image_buster /assets/img_archive/csvexport.png %})

メイン**Segments**ページから、セグメントの<i class="fas fa-gear"></i>**設定**ドロップダウンを選択して、CSVエクスポートをリクエストすることもできます。

![メインのセグメントページの [設定] ドロップダウン。]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
すべてのユーザープロファイルからデータをエクスポートするには、フィルタなしでセグメントを作成し、CSVエクスポートをリクエストする。
{% endalert %}

CSV 出力には、エクスポート時にセグメントに収集済みの各ユーザープロファイルのデータが含まれています。歯車アイコンを選択して CSV エクスポートを選択することで、任意のセグメントをエクスポートできます。Braze はバックグラウンドでレポートを生成し、現在ログインしているユーザーにメールで通知します。

{% alert important %}
ファイルサイズの制限により、セグメントの推定サイズがユーザー数 500,000 人を超える場合、エクスポートに失敗する可能性があります。この制限は、セグメントの正確な計算ではなく推定サイズを使用することに注意してください。詳細については、「[大規模なセグメントのエクスポート]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/)」を参照してください。
{% endalert %}

[Amazon S3 の認証情報]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration)を Braze にリンクしている場合、CSV は代わりに S3 バケットのキー `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` の下にアップロードされます。メールで送信されたリンクは、エクスポートの1 日後に期限切れになり、アクセスのためにダッシュボードにログインする必要があります。

## エクスポートに含まれるデータ

以下のデータが、選択に応じてエクスポートに含まれます。

### ユーザーデータを CSV 形式でエクスポート

| フィールド名                  | 説明                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 内部ID（変更不可）                           |
| country                     | 国                                    |
| created_at                  | ユーザープロファイルが作成された日時                   |
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
| IDFA                       | 広告用識別子（IDFA）の値                 |
| IDFVs                       | ベンダー識別子 (IDFV) の値                      |
| language                    | ISO-639-1規格の言語                                        |
| last_app_version_used       | 最後に使用したアプリのバージョン                             |
| last_name                   | 姓                                                |
| last_session                | 最終セッションの日時                            |
| number_of_google_ad_ids     | 関連するGoogle広告IDの数               |
| number_of_IDFAs             | 関連するIDFAの数                                |
| number_of_IDFVs             | 関連する IDFV の数                                |
| number_of_push_tokens       | 関連するプッシュ通知トークンの数             |
| number_of_roku_ad_ids       | 関連するRoku広告IDの数                 |
| number_of_windows_ad_ids    | 関連するWindows広告IDの数              |
| phone_number                | 電話番号                                             |
| opted_into_push_at          | プッシュ通知にオプトインした日付                       |
| unsubscribed_from_push_at   | プッシュ通知の配信停止日                |
| random_bucket               | ランダムバケット番号                                 |
| roku_ad_ids                 | ロクの広告ID                          |
| session_count               | セッションの総数                                 |
| timezone                    | IANAタイムゾーンデータベースと同じフォーマットによるユーザーのタイムゾーン                                         |
| in_app_purchase_total       | アプリ内購入の支出総額                   |
| user_aliases                | ユーザーエイリアスがある場合                                          |
| windows_ad_ids              | Windows の広告 ID                       |
| カスタムイベント               | 輸出時の選択に基づく                             |
| カスタム属性           | 輸出時の選択に基づく                             |
{: .reset-td-br-1 .reset-td-br-2 }

### メールアドレスを CSV 形式でエクスポート

| フィールド名                  | 説明            |
| --------------------------- | ---------------------- |
| user_id                     | ユーザーの外部ID     |
| first_name                  | 名             |
| last_name                   | 姓              |
| email                       | メール                  |
| unsubscribed_from_emails_at | メール配信停止日 |
| opted_in_to_emails_at       | メールオプトイン日      |
| user_aliases                | ユーザーエイリアスがある場合   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
CSV と API のエクスポートについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)の記事を参照してください。
{% endalert %} 

