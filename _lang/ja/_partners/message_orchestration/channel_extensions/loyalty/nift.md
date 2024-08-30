---
nav_title: ニフト
article_title: ニフト
description: "この参考文献では、企業が顧客を獲得し、関与し、維持するのを助ける2つの側面から成るプラットフォームであるBrazeとニフトの提携について概説する。"
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# ニフト

> [Nift](https://gonift.com/)は、企業が顧客を獲得し、エンゲージし、維持するのを助ける。両面プラットフォームは、提携企業がニッツギフトカードsで顧客に感謝するのを助ける。顧客sのおかげで、生涯価値が高まり、増分収益を生み出す。

Braze とNift の統合により、自動的にトリガー " thank-yous" カスタマーライフサイクルの主要な瞬間にNift ギフトが含まれ、どの顧客が自分のギフトを使用したかを特定することができます。ニフト・ギフト・カードは、ニフトのマッチメーキング・テクノロジーに依存しているブランドが提供する商品やサービスを利用して、コスト効率の良い新しい顧客を獲得することができます。

## 前提条件

| 要件 | 説明 |
|---|---|
| ニフト口座 | この提携の前進タグeを考慮するためには、ニフトの勘定が必要である。 |
| Braze REST API キー | すべてのユーザーデータ権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | REST エンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:ニフトのBrazeに接続する

[Nift ダッシュボード][2]にアクセスし、**Accounts**> **Integrations**> **Braze**に移動し、**Connect**をクリックします。

### ステップ2:Braze 認証情報を追加s

**Brazeアカウント**ページをリンクするには、Braze REST API キーを入力し、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLに応じてBraze エンドポイントを選択します。

顧客 s に送信される参照リンクの顧客 ID パラメータ名を変更できます。ニフトはこれを使って、あなたの顧客sが私たちのブランドの1つからプレゼントを選んだときに、Brazeで処理されたものとして印付けます。

**Link Account**をクリックします。

!["Nift サービスインテグレーションページで、ユーザーにBraze API キーとBraze ダッシュボードのURL を入力します。][5]

## 統合の使用

インテグレーションを使用するには、メッセージングでリファラルリンクを配布します。顧客が紹介リンクを使用し、当社のブランドの1つからギフトを選択すると、ニフトはそれらをBrazeで処理されたものとしてマークします。

Braze との統合後、Nift は次の情報を含む顧客 Brazeレコードにイベントを自動的にプッシュします。

- イベント名: `nift_processed`
- 時間:顧客がプレゼントを選択/使用した時刻


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.gonift.com/users/sign_in
[5]: {% image_buster /assets/img/nift/link_your_braze_account.png %}
[6]: {% image_buster /assets/img/nift/braze_account_linked.png %}