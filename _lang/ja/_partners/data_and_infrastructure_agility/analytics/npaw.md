---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "このレファレンス記事では、Brazeと、有力なオンラインメディアプロフェッショナルにアクション可能なインサイトを提供するインテリジェントデータ分析 プラットフォームであるNPAWとの提携について概説します。"
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/)は、_素敵な勤務者_としても知られており、アクション可能なインサイトをオンラインメディアプロフェッショナルに提供するインテリジェントなデータ分析 プラットフォームです。NPAW の YOUBORA ツールスイートにより、Braze をご利用のお客様は予測的で強力な AI を活用して顧客行動をより深く理解し、プラットフォーム間のエンゲージメントを促進できるようになります。

# 前提条件

| 要件   |提供元| 説明 |
| --------------|------|-------------|
| YOUBORA APIキー |[YOUBORA の設定](https://youbora.nicepeopleatwork.com/users/login)|ユーザー登録時に生成されるAPI キーで、**設定** に配置できます。 |
| ID |[Braze の設定](https://dashboard.braze.com/sign_in) | YOUBORA では、***Braze ID***、***外部ユーザー ID***、または***ユーザー ID*** のいずれかを使ってソフトウェアを Braze にリンクできます。 |
| エンドポイント |[Braze の設定](https://dashboard.braze.com/sign_in)| Braze ダッシュボードで設定可能な完全にカスタマイズ可能なURL エンドポイント。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# 分析の統合

## 統合ページへのアクセス

YOUBORA ツールスイートアカウントにログインしたら、ドロップダウンアカウントメニューから**Integrations** オプションを選択してIntegrations ページに移動します。

![NPAWドロップダウン]({% image_buster /assets/img/npaw_dropdown.png %})

## 統合の設定

Integration(統合)ページにアクセスしたら、スクロールダウンします
**Braze**インテグレーションオプションを参照してください。これをクリックすると、拡張され、入力するために必要なパラメータがいくつか提供されます。

![NPAW 統合]({% image_buster /assets/img/npaw_integration.png %})

前提条件のセクションで確認した適切な情報を使用して詳細を入力します。
* [**Connector Name**] は、将来この統合を参照するために使用される**英数字**の文字列です。この値は、文字と数字**のみ**が含まれている限り、任意の値に設定できます。
* **ユーザID**は、あなたのYOUBORAソフトとあなたのBrazeアカウントを結びつけるために以前に選ばれたIDです。たとえば、**Braze ID**でリンクを実行する場合は、ドロップダウンから**Braze ID**を選択して、適切なフィールドに値を割り当てます。
* [**API Key**] は、[**API**] セクションの [**Settings**] にある YOUBORA ツールスイートの API キーです。
* **エンドポイント** は、以前にBraze ダッシュボード内で設定したカスタマイズ可能なURL エンドポイントです。

すべてのフィールドが入力されたら、**Connect**ボタンをクリックしてコネクションを確立し、変更を保存します。

## NPAW 統合の使用

Braze との統合の設定が完了したら、**Users** 製品に移動し、**Sample Manager** を**セクションマネージャ** 内で選択します。

**Sample Manger** でサンプルを作成した後、右側の3つのドットのアイコンをクリックすると、サンプル内のすべてのユーザーを Braze に送信できます。

![NPAW Sample Manger]({% image_buster /assets/img/npaw_sample_manager.png %})

ユーザーを Braze に送信したら、アクションを実行し、ユーザーセグメントへのキャンペーンに集中して取り組み、非アクティブなユーザーの再獲得、最も忠実なユーザーへのコンタクトなど、あらゆるユーザーセグメントに対するアクションを実行できます。
