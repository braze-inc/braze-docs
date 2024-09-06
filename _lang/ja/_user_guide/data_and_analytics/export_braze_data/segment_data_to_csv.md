---
nav_title: CSV へのセグメントデータのエクスポート
article_title: CSV へのセグメントデータのエクスポート
page_order: 2
page_type: reference
description: "このリファレンス記事では、セグメントデータを CSV にエクスポートする方法を説明します。"

---

# CSV へのセグメントデータのエクスポート

> セグメントからユーザーデータのCSVエクスポートを要求するには、セグメントを編集中に**ユーザーデータドロップダウンを**選択し、セグメントのユーザーデータまたはメールアドレスのいずれかをエクスポートするように選択する。

![][1]

メイン**Segments**ページから、セグメントの<i class="fas fa-gear"></i>**設定**ドロップダウンを選択して、CSVエクスポートをリクエストすることもできます。

![][2]

{% alert tip %}
すべてのユーザープロファイルからデータをエクスポートするには、フィルタなしでセグメントを作成し、CSVエクスポートをリクエストする。
{% endalert %}

CSV 出力には、エクスポート時にセグメントに収集済みの各ユーザープロファイルのデータが含まれています。歯車のアイコンを選択し、CSVエクスポートを選択することで、任意のセグメントをエクスポートできる。Braze はバックグラウンドでレポートを生成し、現在ログインしているユーザーにメールで通知します。

{% alert important %}
ファイルサイズの制限により、セグメントの推定サイズがユーザー数 500,000 人を超える場合、エクスポートに失敗する可能性があります。この制限は、セグメントの正確な計算ではなく推定サイズを使用することに注意してください。詳細については、「[大規模なセグメントのエクスポート]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/)」を参照してください。
{% endalert %}

Amazon S3 credentials][26] をBrazeにリンクしている場合、CSVは代わりにS3バケットに`segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` というキーでアップロードされる。メールで送信されたリンクはエクスポート後 1 日で期限切れになり、アクセスするにはダッシュボードにログインする必要があります。

## エクスポートに含まれるデータ

以下のデータが、選択に応じてエクスポートに含まれます。

### ユーザーデータを CSV 形式でエクスポート

| フィールド名                  | 説明                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 内部ID（変更不可）                           |
| country                     | 国                                    |
| 作成日時                  | ユーザープロファイルが作成された日時                   |
| デバイス                     | デバイス情報                           |
| 生年月日               | 生年月日                                            |
| email                       | メールアドレス                                            |
| 配信停止_from_emails_at | メール配信停止日                            |
| user_id                     | external ID                                              |
| first_name                  | 名                                               |
| first_session               | 初回セッションの日時                           |
| gender                      | 性別                                                   |
| google_ad_ids               | ユーザーに関連付けられたGoogle広告ID                      |
| 都市                        | 市区町村                                     |
| IDFA                       | 広告用識別子（IDFA）の値                 |
| IDFVs                       | ベンダー識別子（IDFV）の値                      |
| language                    | ISO-639-1規格の言語                                        |
| 最後に使用したアプリのバージョン       | 最後に使用したアプリのバージョン                             |
| last_name                   | 姓                                                |
| ラスト・セッション                | 前回のセッション日時                            |
| Google広告のID数     | 関連するGoogle広告IDの数               |
| IDFA数             | 関連するIDFAの数                                |
| IDFV数             | 関連するIDFVの数                                |
| プッシュ・トークン数       | 関連するプッシュ通知トークンの数             |
| roku_ad_idsの数       | 関連するRoku広告IDの数                 |
| ウィンドウズ広告数    | 関連するWindows広告IDの数              |
| 電話番号                | 電話番号                                             |
| opted_into_push_at          | プッシュ通知をオプトインした日付                       |
| 配信停止_from_push_at   | プッシュ通知の配信停止日                |
| ランダムバケット               | ランダムバケット番号                                 |
| roku_ad_ids                 | ロクの広告ID                          |
| セッション数               | 総セッション数                                 |
| timezone                    | IANAタイムゾーンデータベースと同じフォーマットによるユーザーのタイムゾーン                                         |
| アプリ内購入総額       | アプリ内課金の総額                   |
| ユーザー・エイリアス                | ユーザーエイリアスがある場合                                          |
| windows_ad_ids              | ウィンドウズの広告ID                       |
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
| 配信停止_from_emails_at | メール配信停止日 |
| オプトイン・トゥ・メールアドレス       | メールオプトイン日      |
| ユーザー・エイリアス                | ユーザーエイリアスがある場合   |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
CSV と API のエクスポートについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)の記事を参照してください。
{% endalert %} 

[1]: {% image_buster /assets/img_archive/csvexport.png %}
[2]: {% image_buster /assets/img_archive/csvexport2.png %}
{{site.baseurl}} partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration/
