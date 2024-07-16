---
nav_title: Antavo
article_title:アンタボ・ロイヤリティ・クラウド
description:"この参考記事では、BrazeとAntavoのパートナーシップについて概説している。"このパートナーシップは、購入に対する報酬を超えた次世代のロイヤルティプログラムである。
alias: /partners/antavo/
page_type: partner
search_tag:Partner
---

# アンタボ・ロイヤリティ・クラウド

> [Antavoは](https://antavo.com/)、包括的なロイヤルティプログラムを構築し、ブランド愛を育み、顧客行動を変化させるエンタープライズグレードのSaaS型ロイヤルティ・テクノロジー・プロバイダーである。

AntavoとBrazeの統合により、ロイヤルティプログラム関連データを利用してパーソナライズされたキャンペーンを構築し、カスタマーエクスペリエンスを向上させることができる。Antavoは2つのプラットフォーム間のロイヤルティデータの同期をサポートしている-これはAntavoからBrazeへの一方向のデータ同期のみである。この統合は、`external_id` Brazeフィールドをサポートしている。このフィールドは、Antavoがロイヤルティ会員のIDを同期するフィールドである。

## 前提条件

| 必要条件          | 説明                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| アンタボアカウント       | このパートナーシップを利用するには、Brazeインテグレーションを有効にした[Antavo](https://antavo.com/)アカウントが必要である。                                                |
| Braze REST API キー   | `users.track` 権限を持つ Braze REST API キー。<br><br>ダッシュボードで新しいAPIキーを作成するには、「**設定**」>「**APIキー**」と進み、「**新しいAPIキーを作成**」をクリックする。  |
| Braze RESTエンドポイント  | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに依存する。                |
| Brazeアプリ識別子 | アプリ識別子の鍵だ。<br><br>ダッシュボードでこのキーを見つけるには、**設定** **>APIキーと**進み、**識別**セクションを見つける。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:アンタボでBrazeをつなぐ

Antavoで、**Modules**>**Brazeに**進み、**Configureを**クリックする。AntavoのBraze統合設定ページに最初に移動すると、インターフェイスが2つのシステムを接続するよう促す。

以下の認証情報を提供すること：

- **インスタンスのURL：**プロビジョニング先のインスタンスのBraze RESTエンドポイント。
- **APIトークン（識別子）：**AntavoがBrazeにリクエストを送信する際に使用するBraze REST APIキー。
- **アプリ識別子：**Brazeアプリの識別子。

認証情報を入力したら、**Connectを**クリックする。

![インスタンスURL、APIトークン、アプリ識別子でAntavoのBraze画面を接続する。][1]

### ステップ2:フィールドマッピングを設定する

接続が確立されると、自動的にAntavoの**Sync Fields**ページにリダイレクトされ、2つのシステム間のフィールド同期を設定する。  **モジュール**＞**Brazeから**いつでもこのページにアクセスできる。

Antavoでフィールドマッピングを設定する：

1. **Add new field** <i class="fas fa-plus" alt=""></i> をクリックする。
2. ドロップダウンフィールドを使って、Brazeに同期させたいAntavo**ロイヤリティフィールドを**選択する。
3. データを入力するBrazeのカスタム属性に相当する**リモートフィールドを**入力する。  

{% alert note %}
カスタム属性のリストは、Brazeの「**データ設定**」>「カスタム属性」で確認できる。入力したフィールドがBrazeで定義されていない場合、最初の同期で新しいフィールドが自動的に生成される。
{% endalert %}

{:start="4"}
4\.フィールドの組み合わせを追加するには、ステップ1〜3を繰り返す。
5. 同期データのリストからフィールドを削除するには <i class="fa-solid fa-rectangle-xmark" title="をクリックする。"></i>をクリックする。
6. \[**保存**] をクリックします。

Antavoで設定されたフィールドのいずれかの値が変更されると、その単一の値の同期がトリガーされるだけでなく、フィールドマッピングに追加されたすべてのフィールドがリクエストに含まれる。

![AntavoのSync Fieldsページ。][2]

{% alert important %}
データポイントの消費を最小限に抑えるため、Braze内でアクションを起こすフィールドのみをマッピングすることを推奨する。
{% endalert %}

#### サポートされるデータ型

統合は、すべてのBrazeカスタム属性[データ型]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage)、すなわち、数値（整数、浮動小数点）、文字列、配列、ブーリアン、オブジェクト、オブジェクトの配列、および日付をサポートする。

![さまざまなカスタム属性を示すBrazeプロファイル。][3]

データフィールドは、設定されたフィールドマッピングに基づいて入力される。

## トリガー

フィールドマッピングの設定に加え、Antavoの[ワークフローツールに](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629)組み込まれた機能により、この統合はさらなる機能を提供する。すべてのBrazeカスタム属性[データタイプと]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) [カスタムイベントプロパティデータタイプは]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format)、ワークフローを通しても同期することができる。

### ロイヤルティ・データを時々同期させる

データがAntavoのロイヤルティフィールドに格納されていない場合、またはデータがマップされたフィールドリストに追加されていない場合は、このオプションを使用する。要求されたデータの同期は、設定されたワークフロー基準が満たされたときにトリガーされる。

ステップバイステップガイドで、[前回の購入に関連するロイヤルティデータの](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase)同期を設定する方法を学習する。

### ロイヤルティプログラムのイベントを同期させる

Antavoから同期されたイベントを使用して、アクションベースのBraze Canvasesにロイヤルティメンバーを入力する。この統合は、Brazeにカスタムイベントとして表示されるAntavoイベント（購入イベントを含む）を同期することができる。

[ロイヤルティプログラム入会イベントの](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!)同期と[ロイヤルティプログラム特典獲得イベントの](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!)同期の設定方法については、ステップバイステップガイドを参照のこと。

[1]: {% image_buster /assets/img/antavo/connect_braze.png %}
[2]: {% image_buster /assets/img/antavo/data_field_mapping.png %}
[3]: {% image_buster /assets/img/antavo/braze_profile.png %}