---
nav_title: Currents の Zeotap
article_title: Currents の Zeotap
description: "このリファレンス記事では、Braze Currents とZeotap のパートナーシップについて概説します。Zeotap は、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。"
page_type: partner
tool: Currents
search_tag: Partner
---

# Currents の Zeotap

> [Zeotap](https://zeotap.com/) は、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。

Braze と Zeotap の統合により、Zeotap の顧客セグメントを Braze のユーザープロファイルに同期することで、キャンペーンの規模とリーチを拡大できます。[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) では、データを Zeotap に接続し、グローススタック全体で実用的なデータにすることもできます。

{% alert important %}
カスタムHTTPコネクターは現在ベータ版である。この統合の設定に興味がある場合は、カスタマーサクセスマネージャーにご連絡ください。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
|Zeotap アカウント | このパートナーシップを活用するには、[Zeotap アカウント](https://zeotap.com/)が必要です。 |
| Currents | Zeotap にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 実装

### ステップ1:Currentsソースを作成する

1. Zeotap で、[**統合**] の下の [**ソース**] に移動します。
2. [**ソースの作成**] を選択します。
3. カテゴリーとして [**カスタマーエンゲージメントチャネル**] を選択します。<br><br>![「カスタマーエンゲージメントチャネル」など、さまざまなカテゴリーを一覧表示する [ソースの作成] ウィンドウ。][1]{: style="max-width:70%;"}<br><br>
4. データソースとして **Braze** を選択します。
5. ソース名を入力します。
6. 地域を選択します。<br><br>![地域とデータ・エンティティを選択するためのオプションがあるウィンドウ。][6]{: style="max-width:70%;"}<br><br>
7. [**ソースの作成**] を選択します。
8. [**実装の詳細**] タブに行き、**API URL** と **書き込みキー**をメモします。<br><br>![API URL と書き込みキーを含む Braze Currents の実装詳細。][2]

### ステップ2:Currentsでデータストリーミングを設定する

1. Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。
2. [**Currents の新規作成**] および [**カスタム Currents エクスポート**] を選択します。<br><br>![「Current の新規作成」ボタンのドロップダウンに「カスタム Currents のエクスポート」の表示があります。][3]{: style="max-width:60%;"}<br><br>
3. 統合でエラーが発生した場合に連絡を受ける統合名とメールを入力する。
4. **認証情報**の下に、[ステップ1](#step-1-create-a-currents-source)でメモした次の情報を入力します。
- **エンドポイント**としての API URL
- **ベアラートークン**としての書き込みキー<br><br>![統合の詳細および認証情報を入力するセクション。][4]<br><br>
5. Zeotap に送信するメッセージエンゲージメントイベントを選択します。<br><br>![メッセージエンゲージメントイベントを選択するセクションがある [一般設定] タブ。][5]
6. [**Currents を起動**] を選択して変更を保存し、イベントの Zeotap への送信を開始します。

{% alert important %}
Currentsコネクターは匿名ユーザー（`external_id` を持たないユーザー）をサポートしていない。
{% endalert %}

[1]: {% image_buster /assets/img/zeotap/cec.png %}
[2]: {% image_buster /assets/img/zeotap/implementation_details.png %}
[3]: {% image_buster /assets/img/zeotap/custom_currents_export.png %}
[4]: {% image_buster /assets/img/zeotap/credentials.png %}
[5]: {% image_buster /assets/img/zeotap/message_engagement_events.png %}
[6]: {% image_buster /assets/img/zeotap/select_region.png %}