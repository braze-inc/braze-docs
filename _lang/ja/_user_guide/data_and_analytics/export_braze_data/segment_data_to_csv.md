---
nav_title: CSV へのセグメントデータのエクスポート
article_title: CSV へのセグメントデータのエクスポート
page_order: 2
page_type: reference
description: "このリファレンス記事では、セグメントデータを CSV にエクスポートする方法を説明します。"

---

# CSV へのセグメントデータのエクスポート

> セグメントからのユーザーデータの CSV エクスポートをリクエストするには、セグメントの編集中に[**ユーザーデータ**] ドロップダウンをクリックし、セグメントのユーザーデータまたはメールアドレスのいずれをエクスポートするかを選択します。

![][1]

メインの [**セグメント**] ページで、セグメントの <i class="fas fa-gear"></i> [**設定**] ドロップダウンをクリックして、CSV エクスポートを要求することもできます。

![][2]

CSV 出力には、エクスポート時にセグメントに収集済みの各ユーザープロファイルのデータが含まれています。歯車アイコンと [CSV エクスポート] をクリックすると、任意のセグメントをエクスポートできます。Braze はバックグラウンドでレポートを生成し、現在ログインしているユーザーにメールで通知します。

{% alert important %}
ファイルサイズの制限により、セグメントの推定サイズがユーザー数 500,000 人を超える場合、エクスポートに失敗する可能性があります。この制限は、セグメントの正確な計算ではなく推定サイズを使用することに注意してください。詳細については、「[大規模なセグメントのエクスポート]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/)」を参照してください。
{% endalert %}

[Amazon S3 の認証情報][26]を Braze にリンクしている場合、CSV は代わりに S3 バケットのキー `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` の下にアップロードされます。メールで送信されたリンクはエクスポート後 1 日で期限切れになり、アクセスするにはダッシュボードにログインする必要があります。

## エクスポートに含まれるデータ

以下のデータが、選択に応じてエクスポートに含まれます。

### CSV エクスポートのユーザーデータ

| フィールド名                  | 説明                                              |
| --------------------------- | -------------------------------------------------------- |
| Braze ID                   | 内部 ID (変更不可)                           |
| country                     | 国                                    |
| created\_at                  | ユーザープロファイルが作成された日時                   |
| devices                     | デバイス情報                           |
| date\_of\_birth               | 生年月日                                            |
| email                       | メールアドレス                                            |
| unsubscribed\_from\_emails\_at | メールの配信停止日                            |
| user\_id                     | external ID                                              |
| first\_name                  | 名                                               |
| first\_session               | 初回セッションの日時                           |
| gender                      | 性別                                                   |
| google\_ad\_ids               | ユーザーに関連付けられた Google 広告 ID                      |
| city                        | 市区町村                                     |
| IDFAs                       | 宣伝 (IDFA) の値の識別子                 |
| IDFVs | ベンダー識別子 (IDFV) の値 |
| language                    | ISO-639-1 規格の言語                                        |
| last\_app\_version\_used       | 最後に使用したアプリのバージョン                             |
| last\_name                   | 姓                                                |
| last\_session                | 前回のセッションの日時                            |
| number\_of\_google\_ad\_ids     | 関連する Google 広告 ID の数               |
| number\_of\_IDFAs             | 関連する IDFA の数                                |
| number\_of\_IDFVs             | 関連する IDFV の数                                |
| number\_of\_push\_tokens       | 関連するプッシュ通知トークンの数             |
| number\_of\_roku\_ad\_ids       | 関連する Roku 広告 ID の数                 |
| number\_of\_windows\_ad\_ids    | 関連する Windows 広告 ID の数              |
| phone\_number                | 電話番号                                             |
| opted\_into\_push\_at          | プッシュ通知にオプトインした日付                       |
| unsubscribed\_from\_push\_at   | プッシュ通知の配信停止日                |
| random\_bucket               | ランダムバケット番号                      |
| roku\_ad\_ids                 | Roku の広告 ID                          |
| session\_count               | セッション総数                                 |
| timezone                    | IANA タイムゾーンデータベースと同じ形式でのユーザーのタイムゾーン                                         |
| in\_app\_purchase\_total       | アプリ内購入の合計金額                   |
| user\_aliases                | ユーザーエイリアス (存在する場合)                                         |
| windows\_ad\_ids              | Windows の広告 ID                       |
| カスタムイベント               | エクスポート時の選択に基づく                             |
| カスタム属性           | エクスポート時の選択に基づく                             |
{: .reset-td-br-1 .reset-td-br-2 }

### CSV エクスポートのメールアドレス

| フィールド名                  | 説明                                              |
| --------------------------- | ---------------------- |
| user\_id | ユーザーの external ID |
| first\_name                  | 名             |
| last\_name                   | 姓              |
| email                       | メール                  |
| unsubscribed\_from\_emails\_at | メールの配信停止日 |
| opted\_in\_to\_emails\_at       | メールのオプトイン日      |
| user\_aliases                | ユーザーエイリアス (存在する場合)   |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
CSV と API のエクスポートについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)の記事を参照してください。
{% endalert %} 

[1]: {% image_buster /assets/img_archive/csvexport.png %}
[2]: {% image_buster /assets/img_archive/csvexport2.png %}
[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration
