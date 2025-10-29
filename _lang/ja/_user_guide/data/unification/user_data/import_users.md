---
nav_title: ユーザーをインポートする
article_title: ユーザーをインポートする
page_order: 4.1
description: "CSV インポート、REST API、クラウドデータ取り込みなど、Braze のさまざまなユーザーインポートオプションについて説明します。"

---
# ユーザーをインポートする

> CSV インポート、REST API、クラウドデータ取り込みなど、Braze のさまざまなユーザーインポートオプションについて説明します。

## HTML 検証について

Braze は、インポート中にHTML データをサニタイズ、検証、または再フォーマットしないことに注意してください。つまり、スクリプトタグは、Web パーソナライゼーションに使用するすべてのインポートデータから削除する必要があります。

特に Web ブラウザーでのパーソナライゼーションを目的としているデータを Braze にインポートする場合、Web ブラウザーのレンダリング時に悪意を持って利用される可能性のある HTML、JavaScript、その他のスクリプトタグを必ず除去してください。

別の方法として、HTML の場合は、Braze の Liquid フィルター (`strip_html`) を HTML のエスケープ付きテキストに使用できます。以下に例を示します。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 読み込みオプション

### Braze CSV インポート

CSV インポートを使用して、次のユーザー属性およびカスタムイベントを記録および更新できます。開始するには、「[CSV インポート]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import)」を参照してください。

|タイプ|定義|例|最大ファイルサイズ|
|---|---|---|---|
|デフォルト属性|Braze によって認識される予約ユーザ属性。|`first_name`, `email`|500 MB|
|カスタム属性|ビジネス固有のユーザー属性。|`last_destination_searched`|500 MB|
|カスタムイベント|ユーザーアクションを表すビジネス固有のイベント。|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Lambda でのユーザー CSV インポート

サーバーレス S3 Lambda CSV インポートスクリプトを使用して、ユーザー属性を Braze にアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードします。

1,000,000 行を持つ 1 ファイルの推定実行時間は約 5 分です。詳細については、「[Braze へのユーザー属性 CSV のインポート](https://www.braze.com/docs/user_guide/data/cloud_ingestion/)」を参照してください。

### REST API

[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、カスタムイベント、ユーザー属性、およびユーザーの購入を記録します。

### クラウドデータ取り込み

Braze の[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/)を使用して、ユーザー属性のインポートと管理を行います。

## 法的に義務付けられているトランザクションメール

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}
