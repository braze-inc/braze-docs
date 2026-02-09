---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "このリファレンス記事では、Braze と Antavo のパートナーシップについて説明します。Antavo は、特典付きの購入からさらに進んだ次世代ロイヤルティプログラムです。"
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/)社は、包括的なロイヤリティ・プログラムを構築し、ブランド愛を育み、顧客の行動を変える、エンタープライズ・グレードのSaaS型ロイヤリティ・テクノロジー・プロバイダーである。

_この統合は Alpaco によって管理されます。_

## 統合について

AntavoとBrazeの統合により、ロイヤルティプログラム関連データを利用してパーソナライズされたキャンペーンを構築し、顧客体験を向上させることができる。Antavo では、2つのプラットフォーム間のロイヤルティデータ同期 (Antavo から Braze への一方向データ同期のみ) がサポートされています。この統合は、`external_id` Brazeフィールドをサポートしており、Antavo はこのフィールドを使ってロイヤルティ会員 ID を同期しています。

## 前提条件

| 必要条件          | 説明                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo アカウント       | このパートナーシップを利用するには、Brazeとの統合を有効にした[Antavo](https://antavo.com/)アカウントが必要である。                                                |
| Braze REST API キー   | 次の権限がある Braze REST API キー。`users.track`、`events.list`、`events.data_series`、`events.get`。<br><br>これは、Braze ダッシュボードの [**設定**] > [**API キー**] で作成できます。  |
| Braze REST エンドポイント  | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。                |
| Brazeアプリの識別子 | アプリ識別子キー。<br><br>Braze ダッシュボードでこのキーを確認するには、[**設定**] > [**API キー**] に進み、[**識別**] セクションを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Antavo で Braze に接続する

Antavo で [**Modules**] > [**Braze**] に移動し、[**Configure**] をクリックします。Antavo の Braze 統合設定ページに初めて移動すると、2つのシステムを接続するように促されます。

以下の認証情報を指定します。

- **Instance URL:**プロビジョニング先のインスタンスのBraze RESTエンドポイント。
- **APIトークン（識別子）：**AntavoがBrazeにリクエストを送信する際に使用するBraze REST APIキー。
- **App Identifier:**Brazeアプリの識別子。

認証情報を入力したら、[**Connect**] をクリックします。

![「Instance URL」、「API Token」、「App Identifier」が表示されている Antavo の「Connect Braze」画面。]({% image_buster /assets/img/antavo/connect_braze.png %})

### ステップ2:フィールドマッピングを設定する

接続が確立されると、Antavoの「**Sync Fields」**ページに自動的にリダイレクトされ、2つのシステム間のフィールド同期を設定する。  このページへは、**モジュール**＞**Brazeから**いつでもアクセスできる。

Antavoでフィールドマッピングを設定する：

1. [**Add new field**] をクリックします<i class="fas fa-plus" alt=""></i>。
2. ドロップダウンフィールドを使用して、Braze に同期する Antavo の**ロイヤルティフィールド**を選択します。
3. データの取り込み先となる Braze の対応するカスタム属性を表す**リモートフィールド**を入力します。  

{% alert note %}
カスタム属性のリストは、Brazeの「**データ設定**」＞「**カスタム属性**」で確認できる。入力したフィールドがBrazeで定義されていない場合、最初の同期で新しいフィールドが自動的に生成される。
{% endalert %}

{:start="4"}
4\.フィールドの組み合わせを追加するには、ステップ1〜3を繰り返す。
5. 同期されるデータのリストからフィールドを削除するには、行の終わりにある <i class="fa-solid fa-rectangle-xmark" title="Delete"></i> をクリックします。
6. [**保存**] をクリックします。

Antavoで設定されたフィールドのいずれかの値が変更されると、その単一の値の同期がトリガーされるだけでなく、フィールドマッピングに追加されたすべてのフィールドがリクエストに含まれる。

![Antavo の「Sync Fields」ページ。]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
データポイントの使用量を最小限に抑えるため、Braze内でアクションを起こすフィールドのみをマッピングすることを推奨する。
{% endalert %}

#### サポートされるデータ型

この統合では、Braze のすべてのカスタム属性[データ型]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) (数値 (整数、浮動小数点)、文字列、配列、ブール値、オブジェクト、オブジェクト配列、日付) がサポートされています。

![さまざまなカスタム属性を示す Braze プロファイル。]({% image_buster /assets/img/antavo/braze_profile.png %})

データフィールドは、設定されたフィールドマッピングに基づいて入力される。

## トリガー

フィールドマッピングの設定に加え、Antavoの[ワークフローツールに](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629)組み込まれた機能により、統合はさらなる機能を提供する。すべての Braze カスタム属性[データ型]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) とカスタムイベントプロパティ[データ型]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format)も、ワークフローを介して同期できます。

### ロイヤルティデータを随時同期する

データがAntavoのロイヤリティフィールドに格納されていない場合、またはデータがマップされたフィールドリストに追加されていない場合は、このオプションを使用する。要求されたデータの同期は、設定されたワークフロー条件が満たされたときにトリガーされます。

[最後の購入に関連するロイヤルティデータ](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase)の同期を設定する方法については、ステップバイステップガイドを参照してください。

### ロイヤリティ・プログラムのイベントを同期させる

Antavo から同期されたイベントを使用して、アクションベースの Braze キャンバスにロイヤルティメンバーを入力します。この統合は、Braze にカスタムイベントとして表示されるあらゆる Antavo イベント (購入イベントを含む) を同期できます。

[ロイヤルティプログラム登録イベント](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!)の同期および[ロイヤルティプログラム特典獲得イベント](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!)の同期の設定方法については、ステップバイステップガイドを参照してください。


