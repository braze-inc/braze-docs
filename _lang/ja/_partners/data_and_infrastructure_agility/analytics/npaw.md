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

> [NPAW](https://nicepeopleatwork.com/)は、_素敵な勤務者_としても知られており、アクション可能なインサイトをオンラインメディアプロフェッショナルに提供するインテリジェントなデータ分析 プラットフォームです。NPAWのYOUBORAツールスイートにより、Braze 顧客は予測的で堅牢なAIを活用して、顧客行動をより深く理解し、プラットフォームS間のエンゲージメントを促進できるようになりました。

# 前提条件

| 要件   |Origin| 説明 |
| --------------|------|-------------|
| YOUBORA APIキー |[YOUBORAの設定](https://youbora.nicepeopleatwork.com/users/login)|ユーザー登録時に生成されるAPI キーで、**設定** に配置できます。 |
| ID |[Braze設定](https://dashboard.braze.com/sign_in) | YOUBORAでは、***Braze ID***、***外部ユーザID***、または***ユーザID***のいずれかを選択できます。 |
| エンドポイント |[Braze設定](https://dashboard.braze.com/sign_in)| Braze ダッシュボードで設定可能な完全にカスタマイズ可能なURL エンドポイント。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

# 分析の統合

## 統合ページへのアクセス

YOUBORA ツールスイートアカウントにログインしたら、ドロップダウンアカウントメニューから**Integrations** オプションを選択してIntegrations ページに移動します。

![NPAW ドロップダウン]({% image_buster /assets/img/npaw_dropdown.png %})

## 統合の設定

Integration(統合)ページにアクセスしたら、スクロールダウンします
**Braze**インテグレーションオプションを参照してください。これをクリックすると、拡張され、入力するために必要なパラメータがいくつか提供されます。

![NPAW 統合]({% image_buster /assets/img/npaw_integration.png %})

役得欄から集めたアプリの適切な情報を詳しく記入してください。
* **Connector Name** は、将来この統合を参照するために使用される**英数字** 文字列です。この値は、****の文字と数字のみが含まれている限り、任意の値に設定できます。
* **ユーザID**は、あなたのYOUBORAソフトとあなたのBrazeアカウントを結びつけるために以前に選ばれたIDです。たとえば、**Braze ID**でリンクを実行する場合は、ドロップダウンから**Braze ID**を選択して、適切なフィールドに値を割り当てます。
* **API Key** は、**API** セクションの**Settings** にあるYOUBORA ツールスイートAPI Key です。
* **エンドポイント** は、以前にBraze ダッシュボード内で設定したカスタマイズ可能なURL エンドポイントです。

すべてのフィールドが入力されたら、**Connect**ボタンをクリックしてコネクションを確立し、変更を保存します。

## NPAW 統合の使用

Braze との統合の設定が完了したら、**Users** 製品に移動し、**Sample Manager** を**セクションマネージャ** 内で選択します。

**Sample Manger**内にサンプルを作成した後、右側のトリプルドットアイコンをクリックすると、サンプル内のすべてのユーザーsをBrazeに送信できます。

![NPAW 標本マネージャー]({% image_buster /assets/img/npaw_sample_manager.png %})

これで、ユーザーsをBrazeに送った後、アクションを取ってキャンペーンsをユーザー Segmentsに集中させ、sを再びアクティブユーザーしたり、あなたの最も忠実なsやアクションにどんなユーザー Segmentでも連絡を取ることができます!
