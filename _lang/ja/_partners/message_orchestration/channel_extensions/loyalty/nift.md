---
nav_title: Nift
article_title:ギフト
description:"この参考記事では、企業のカスタマー獲得、エンゲージメント、顧客維持を支援するツーサイドプラットフォームであるBrazeとNiftのパートナーシップについて概説している。"
alias: /partners/nift/
page_type: partner
search_tag:Partner

---

# ギフト

> [Niftは](https://gonift.com/)企業が顧客を獲得し、エンゲージメントし、維持するのを支援する。この両面プラットフォームは、パートナーが顧客に対してNiftギフトカードで感謝の気持ちを伝えることを支援する。顧客に感謝することは、顧客の生涯価値を高め、収益の増加を生み出す。

BrazeとNiftの統合により、カスタマーライフサイクルの重要な瞬間にNiftギフトを含む「お礼の品」を自動的にトリガーし、どの顧客がギフトを利用したかを識別することができる。Niftギフトカードは、Niftのマッチメイキング技術を利用するブランドが提供する商品やサービスにアクセスするために使用することができ、コスト効率よく大規模に新規顧客を獲得することができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Niftアカウント | このパートナーシップを利用するには、Niftアカウントが必要である。 |
| Braze REST API キー | すべてのユーザーデータ権限を持つBraze REST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:NiftでBrazeに接続する

[Niftのダッシュボードに][2]アクセスし、**Accounts**>**Integrations**>**Brazeに**移動し、**Connectを**クリックする。

### ステップ2:認証情報を追加する

**Link your Braze Account**ページで、Braze REST APIキーを入力し、[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLによって異なるBrazeエンドポイントを選択する。

顧客に送信される紹介リンクの顧客IDパラメータ名を変更できる。Niftは、顧客がBrazeのブランドからギフトを選択した場合、Brazeで処理されたことを示すためにこれを使用する。

**アカウントのリンクを**クリックする。

!["BrazeAPIキーとBrazeダッシュボードURLの入力をユーザーに促すNiftサービス統合ページ。][5]

## 統合を利用する

統合を利用するには、メッセージングで紹介リンクを配布する。あなたの顧客が紹介リンクを使い、私たちのブランドのギフトを選択すると、NiftはBrazeで処理されたとマークする。

Brazeとの統合後、Niftは自動的に以下のデータを持つ既存の顧客Brazeレコードにイベントをプッシュする：

- イベント名だ： `nift_processed`
- Time: 顧客がギフトを選択／利用した時間


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.gonift.com/users/sign_in
[5]: {% image_buster /assets/img/nift/link_your_braze_account.png %}
[6]: {% image_buster /assets/img/nift/braze_account_linked.png %}