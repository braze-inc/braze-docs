---
nav_title: Currents の設定
article_title: Currents の設定
page_order: 0
page_type: tutorial
description: "このハウツー記事では、Braze Currents の連携と設定を行うプロセスを順に説明します。"
tool: Currents
search_rank: 8
---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents の設定

> このページでは、Braze Currents の連携と設定を行う一般的なプロセスを概説します。

{% alert important %}
Currents は特定の Braze パッケージに含まれています。質問がある場合、またはアクセスを希望する場合は、Braze の担当者にお問い合わせください。
{% endalert %}

## 要件

弊社のパートナーと連携して Currents を使用するには、同じ基本パラメーターと接続方法が必要です。

各パートナーは Braze がデータファイルを書き込んでパートナーに送信する権限を有することを要求し、Braze は、それらのファイルをパートナーが書き込む場所、具体的にはバケット名またはキーを尋ねます。

以下の要件は、ほとんどのパートナーと連携するための基本的な最小要件です。パートナーによっては、追加のパラメーターが必要になります。それらのパラメーターは、これらの基本要件とのわずかな違いとともに、それぞれの[パートナーのドキュメント]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)にリストされています。

| 要件 | 提供元 | アクセス | 説明
|---|---|---|---|
| パートナーのアカウント | そのパートナーにアカウントを手配するか、Brazeのアカウントマネージャーに提案を求める。 | パートナーのサイトをチェックするか、パートナーに連絡して登録します。 | Brazeは、あなたの会社のアカウントを通じてそのデータにアクセスできない場合、パートナーにデータを送信しない。
| パートナーAPIキーまたはトークン | 通常はパートナーのダッシュボードにあります。 | それをコピーして指定のBrazeフィールドに貼り付けます。 | Braze には、パートナーの「連携」ページに、このための指定フィールドがあります。これは、データの送信先をマッピングするために必要です。**パートナーのキーまたはトークンを最新の状態に維持することが重要です。認証情報が無効の場合、コネクターが無効になり、イベントがドロップする可能性があります。**
| 認証コード/キー、秘密キー、認証ファイル | そのパートナーのアカウント担当者に連絡します。パートナーのダッシュボードに記載されている可能性もあります。 | キーをコピーして指定のBrazeフィールドにペーストする。`.json` または他の証明書ファイルを生成して、Braze の適切な場所にアップロードします。 | Braze には、パートナーの「連携」ページに、このための指定フィールドがあります。これにより Braze に認証情報が付与され、パートナーでのお客様のアカウントに Braze がファイルを書き込むことができます。**認証の詳細を最新の状態に維持することが重要です。認証情報が無効の場合、コネクターが無効になり、イベントがドロップする可能性があります。**
| バケツ、フォルダパス | 一部のパートナーは、バケツごとにデータを整理し、分類している。これはパートナーのダッシュボードにあります。 | これが必要な場合は、バケット名またはファイルパスを Braze の指定スペースに正確にコピーしてください。私たちは、あなたのデータが失われることを望んでいない！ | これはパートナーによっては必要なことではあるが、必要なときに正しく行うことが重要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
パートナーのキーまたはパートナーのトークンと認証の詳細を最新の状態に保つことが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態のまま **48 時間**を超えると、コネクターのイベントがドロップし、データが永久に喪失します。
{% endalert %}

## Currents の設定

### ステップ1:パートナーの選択

Braze Currents を使用すると、フラットファイルを使用したデータストレージ経由での連携、またはバッチ化された JSON ペイロードを指定されたエンドポイントに送信して、行動分析を行ったり顧客データを扱ったりするパートナーとの連携ができます。  

連携を開始する前に、目的に最適な連携を決定することをお勧めします。例えば、すでに mParticle と Segment を利用していて、そこに Braze データをストリーミングする場合は、バッチ化された JSON ペイロードを使用することが最も優れた方法です。データを独自に操作する場合、またはより複雑なデータ分析システムがある場合は、データ ストレージを使用することが最も優れた方法です ([Braze ではこの方法を採用]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/))。

### ステップ2:Currents　を開く

まず、[**パートナー連携**] > [**データのエクスポート**] に移動します。Currents の [連携管理] ページが表示されます。

![Braze ダッシュボードの Currents ページ]({% image_buster /assets/img_archive/currents-main-page.png %})

### ステップ 3:パートナーを追加する

画面上部のドロップダウンを選択し、パートナー（「Currentsコネクター」と呼ばれることもある）を追加する。

パートナーごとに異なる設定ステップが必要です。各連携を有効にするには、 [利用可能なパートナー]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) のリストを参照し、それぞれのページの指示に従います。

### ステップ 4:イベントを設定する

利用可能なオプションから、パートナーに渡すイベントのチェックボックスをオンにします。これらのイベントのリストは、[顧客行動イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)ライブラリと[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)ライブラリにあります。

![]({% image_buster /assets/img/current4.png %})

必要に応じて、イベントの詳細について「[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/)」の記事を参照してください。

### ステップ 5: フィールド変換の設定

Currents フィールド変換を使用して、文字列フィールドを削除またはハッシュできます。

- **削除:**文字列フィールドを`[REDACTED]` に置き換えます。これは、パートナーが欠落フィールドまたは空のフィールドを持つイベントを拒否する場合に役立ちます。
- **ハッシュ:**SHA-256ハッシュアルゴリズムを文字列フィールドに適用します。

これらのいずれかの変換を行う対象のフィールドを選択すると、そのフィールドのあるすべてのイベントにその変換が適用されます。例えば、ハッシュ化の対象として `email_address` を選択すると、メール送信数、メール開封数、メールバウンス数、サブスクリプショングループの状態の変更イベントの `email_address` フィールドがハッシュ化されます。

![フィールド変換の追加]({% image_buster /assets/img/current3.png %})

### ステップ 6:連携のテスト

{% alert important %}
Currents は、900 KB を超える過度に大きなペイロードを持つイベントをドロップします。
{% endalert %}

テストする前に、[GitHub のサンプル Currents データ](https://github.com/Appboy/currents-examples)をご確認ください。テストの準備ができたら、以下のオプションを選択します。

#### テストイベントの送信

連携をテストするには、[**テストイベントを送信**] を選択して、選択した各イベントタイプからこの Current に 1 つのイベントを送信します。各イベントタイプの詳細については、[顧客行動イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)ライブラリと[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)ライブラリを参照してください。

![Braze ダッシュボードの [Currents Test (Currents テスト)] ページ]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### 電流コネクタのテスト

Currents のテストコネクターは、弊社の既存のコネクターの無料版であり、さまざまな送信先のテストと試行に使用できます。Currents のテストは次のとおりです。

- Currents のテストコネクターの数に制限はありません。
- 7 日間の移動期間あたり、集計するイベントは最大 10,000 件です。このイベントの合計はダッシュボードで 1 時間ごとに更新されます。

Currents のテストコネクターが送信制限に達すると、コネクターは次の 7 日間まで、イベントを送信しません。

Currents のテストコネクターをアップグレードするには、ダッシュボードで連携を編集し、[**テスト連携をアップグレード**] を選択します。

## Currents の更新

{% multi_lang_include updating_currents.md %}

## IP許可リスト

Braze は、リストされた IP から Currents データを送信します。

{% multi_lang_include data_centers.md datacenters='ips' %}
