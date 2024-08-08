---
nav_title: Currents の設定
article_title: Currents の設定
page_order: 0
page_type: tutorial
description: "このハウツー記事では、Braze Currents の連携と設定を行うプロセスを順に説明します。"
tool: Currents
search_rank: 8
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents の設定

> このページでは、Braze Currents の連携と設定を行う一般的なプロセスを概説します。

{% alert important %}
Currents は特定の Braze パッケージに含まれています。質問がある場合、またはアクセスを希望する場合は、Braze の担当者にお問い合わせください。
{% endalert %}

## 要件

弊社のパートナーと連携して Currents を使用するには、同じ基本パラメーターと接続方法が必要です。

各パートナーは Braze がデータファイルを書き込んでパートナーに送信する権限を有することを要求し、Braze は、それらのファイルをパートナーが書き込む場所、具体的にはバケット名またはキーを尋ねます。

以下の要件は、ほとんどのパートナーと連携するための基本的な最小要件です。パートナーによっては、追加のパラメーターが必要になります。それらのパラメーターは、これらの基本要件とのわずかな違いとともに、それぞれの[パートナーのドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)にリストされています。

| 要件 | Origin | アクセス | 説明
|---|---|---|---|
| パートナーでのアカウント | そのパートナーでのアカウントを手配するか、Braze アカウントマネージャーに推奨事項をお問い合わせください。 | パートナーのサイトを確認するか、そのパートナーに連絡してサインアップします。 | お客様が会社のアカウントからデータにアクセスできない場合、Braze はパートナーにそのデータを送信しません。
| パートナーの API キーまたはトークン | 通常はパートナーのダッシュボード。 | コピーして、指定された Braze のフィールドに貼り付けます。 | Braze には、そのパートナーの [連携] ページに、このための指定フィールドがあります。これは、データの送信先をマッピングするために必要です。**パートナーのキー / トークンを最新の状態に維持することが重要です。認証情報が無効の場合、コネクターが無効になり、イベントがドロップする可能性があります。**
| 認証コード / キー、秘密キー、証明書ファイル | そのパートナーのアカウント担当者にお問い合わせください。パートナーのダッシュボードに存在する場合もあります。 | キーをコピーして、指定された Braze のフィールドに貼り付けます。`.json` または他の証明書ファイルを生成して、 Braze の適切な場所にアップロードします。 | Braze には、そのパートナーとの [連携] ページに、このための指定フィールドがあります。これにより Braze に認証情報が付与され、パートナーでのお客様のアカウントに Braze がファイルを書き込むことができます。**認証の詳細を最新の状態に維持することが重要です。認証情報が無効の場合、コネクターが無効になり、イベントがドロップする可能性があります。**
| バケット、フォルダーのパス | パートナーによっては、バケット別にデータを整理し、並べ替えます。これはパートナーのダッシュボードにあります。 | これが必要な場合は、バケット名またはファイルパスを Braze 内の指定されたスペースに正確にコピーしてください。データの喪失が起きてはなりません。 |一部のパートナーではこれが必要ですが、本当に必要なときに正しく行うことが重要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert important %}
パートナーのキー / トークンと認証の詳細を最新の状態に維持することが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態のまま **48 時間**を超えると、コネクターのイベントがドロップし、データが永久に喪失します。
{% endalert %}

## ステップ 1: パートナーの選択

Braze Currents を使用すると、フラットファイルを使用したデータストレージ経由での連携、またはバッチ化された JSON ペイロードを指定されたエンドポイントに送信して、行動分析を行ったり顧客データを扱ったりするパートナーとの連携ができます。  

連携を開始する前に、目的に最適な連携を決定することをお勧めします。例えば、すでに mParticle と Segment を利用していて、そこに Braze データをストリーミングする場合は、バッチ化された JSON ペイロードを使用することが最も優れた方法です。データを独自に操作する場合、またはより複雑なデータ分析システムがある場合は、データ ストレージを使用することが最も優れた方法です ([Braze ではこの方法を採用]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/))。

## ステップ 2: Currents への移動

まず、[**パートナー連携**] > [**データのエクスポート**] に移動します。Currents の [連携管理] ページが表示されます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは [**連携**] > [**Currents**] にあります。
{% endalert %}

![Currents page in the Braze dashboard]({% image_buster /assets/img_archive/currents-main-page.png %})

## ステップ 3: パートナーの追加

画面上部のドロップダウンをクリックして、パートナー (「Currents コネクター」とも呼ばれる) を追加します。

パートナーごとに異なる設定ステップが必要です。各連携を有効にするには、 [利用可能なパートナー]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) のリストを参照し、それぞれのページの指示に従います。

## ステップ 4: イベントの設定

利用可能なオプションから、パートナーに渡すイベントのチェックボックスをオンにします。これらのイベントのリストは、[顧客行動イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)ライブラリと[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)ライブラリにあります。

![\]({% image_buster /assets/img/current4.png %})

必要に応じて、イベントの詳細について「[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/)」の記事を参照してください。

## ステップ 5: フィールド変換

Currents のフィールド変換を使用すると、Currents の特定の文字列フィールドの削除 (空の文字列に置換)、またはハッシュ (SHA-256 ハッシュアルゴリズムの適用) を指定できます。 

これらのいずれかの変換を行う対象のフィールドを選択すると、そのフィールドのあるすべてのイベントにその変換が適用されます。例えば、ハッシュ化の対象として `email_address` を選択すると、メール送信数、メール開封数、メールバウンス数、サブスクリプショングループの状態の変更の `email_address` フィールドがハッシュ化されます。

![Adding field transformations]({% image_buster /assets/img/current3.png %})

## ステップ 6: 連携のテスト

連携をテストしたり、Currents の例の [GitHub リポジトリ](https://github.com/Appboy/currents-examples)にあるサンプルの Currents データを確認したりできます。

{% alert important %}
Currents は、900 KB を超える過度に大きなペイロードを持つイベントをドロップすることに注意してください。
{% endalert %}

### Currents のテストコネクター

Currents のテストコネクターは、弊社の既存のコネクターの無料版であり、さまざまな送信先のテストと試行に使用できます。Currents のテストは次のとおりです。
\- 作成できる Currents のテストコネクターの数に制限はありません。
\- 30 日間の移動期間あたり、集計するイベントは最大 10,000 件です。このイベントの合計はダッシュボードで 1 時間ごとに更新されます。

Currents のテストコネクターが送信制限に達すると、コネクターは次の 30 日間まで、イベントを送信しません。

Currents のテストコネクターをアップグレードするには、ダッシュボードで連携を編集し、[**アップグレード**] を選択します。

## Currents の更新

{% multi_lang_include updating_currents.md %}