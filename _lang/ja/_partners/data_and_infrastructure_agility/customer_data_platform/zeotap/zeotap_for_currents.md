---
nav_title: 百花繚乱のZeotap
article_title: 百花繚乱のZeotap
description: "この参考記事では、Braze Currentsと次世代顧客データプラットフォームであるZeotapのパートナーシップについて概説している。Zeotapは、アイデンティティ解決、インサイト、データエンリッチメントを提供することで、モバイルオーディエンスの発見と理解を支援する。"
page_type: partner
tool: Currents
search_tag: Partner
---

# 百花繚乱のZeotap

> [Zeotap](https://zeotap.com/) は、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。

BrazeとZeotapの統合により、Zeotapの顧客セグメントをBrazeのユーザープロファイルに同期させることで、キャンペーンの規模とリーチを拡大することができる。[Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/)使えば、データをZeotapに接続して、成長スタック全体でアクション可能にすることもできる。

{% alert important %}
カスタムHTTPコネクターは現在ベータ版である。この統合の設定に興味がある場合は、カスタマー・サクセス・マネージャーに連絡してほしい。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
|Zeotap アカウント | このパートナーシップを活用するには、[Zeotap アカウント](https://zeotap.com/)が必要です。 |
| Currents | データをZeotapにエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 実装

### ステップ 1: Currentsソースを作成する

1. Zeotapで、**Integrateの**下の**Sourcesに**行く。
2. **ソースの作成**」を選択する。
3. カテゴリーとして**カスタマーエンゲージメントチャネルを**選択する。<br><br>![顧客エンゲージメント・チャネル」など、さまざまなカテゴリーをリストアップした「ソースの作成」ウィンドウ。][1]{: style="max-width:70%;"}<br><br>
4. データソースとして**Brazeを**選択する。
5. ソース名を入力する。
6. 地域を選択する。<br><br>![地域とデータ・エンティティを選択するためのオプションがあるウィンドウ。][6]{: style="max-width:70%;"}<br><br>
7. **ソースの作成**」を選択する。
8. **Implementation Details**タブに行き、**API URLと** **Write Keyを**メモする。<br><br>![API URLとWrite Keyを含むBraze Currentsの実装詳細。][2]

### ステップ2:Currentsでデータストリーミングを設定する

1. Brazeで、**Partner Integrations**>**Data Exportに**進む。
2. **Create New Currentsと** **Custom Currents Exportを**選択する。<br><br>![新しいカレントを作成」ボタンのドロップダウンに「カスタムカレントエクスポート」が含まれる。][3]{: style="max-width:60%;"}<br><br>
3. 統合でエラーが発生した場合に連絡を受ける統合名とメールを入力する。
4. **認証情報**」の下に、[ステップ](#step-1-create-a-currents-source)1で確認した以下の情報を入力する：
- **エンドポイントとしての**API URL
- **ベアラートークンとしての**ライトキー<br><br>![セクションに統合の詳細と認証情報を入力する。][4]<br><br>
5. Zeotapに送信したいメッセージエンゲージイベントを選択する。<br><br>![一般設定」タブには、メッセージ・エンゲージメント・イベントを選択するセクションがある。][5]
6. **Launch Currents]**を選択して変更を保存し、Zeotap へのイベント送信を開始する。

{% alert important %}
Currentsコネクターは匿名ユーザー（`external_id` を持たないユーザー）をサポートしていない。
{% endalert %}

[1]: {% image_buster /assets/img/zeotap/cec.png %}
[2]: {% image_buster /assets/img/zeotap/implementation_details.png %}
[3]: {% image_buster /assets/img/zeotap/custom_currents_export.png %}
[4]: {% image_buster /assets/img/zeotap/credentials.png %}
[5]: {% image_buster /assets/img/zeotap/message_engagement_events.png %}
[6]: {% image_buster /assets/img/zeotap/select_region.png %}