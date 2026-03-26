---
nav_title: Nift
article_title: Nift
description: "このリファレンス記事では、Braze と Nift のパートナーシップについて説明します。Nift は、企業が顧客を獲得し、関与し、維持するのを支援する双方向プラットフォームです。"
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) は、企業が顧客を獲得し、関与し、維持するのを支援します。この双方向プラットフォームでは、パートナーが Nift ギフトカードで顧客への感謝を示すことができます。顧客に感謝を示すことで、顧客生涯価値が高まり、収益が増加します。

_この統合は Nift によって管理されます。_

## 統合について

Braze と Nift の統合により、カスタマーライフサイクルにおいて重要なタイミングで Nift ギフトを含む「お礼 (thank-yous)」を自動的にトリガーし、どの顧客がギフトを使用したかを特定できます。Nift ギフトカードは、Nift のマッチメイキング技術を利用して、費用対効果の高い大規模で新規顧客を獲得するブランドが提供する製品やサービスにアクセスするために使用できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Nift アカウント | このパートナーシップを活用するには、Nift アカウントが必要です。 |
| Braze REST API キー | すべてのユーザーデータ権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Nift で Braze に接続する

[Nift ダッシュボード](https://www.gonift.com/users/sign_in)にアクセスし、**Accounts**> **Integrations**> **Braze**に移動し、**Connect**をクリックします。

### ステップ2:Braze 認証情報を追加s

**Brazeアカウント**ページをリンクするには、Braze REST API キーを入力し、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLに応じてBraze エンドポイントを選択します。

顧客に送信される紹介リンクの顧客 ID パラメーター名を変更できます。Ｎｉｆｔ は、顧客が Braze のブランドのギフトを選択している場合に、顧客を Braze で処理済みとしてマークします。

[**Link Account**] をクリックします。

!["ユーザーに Braze API キーと Braze ダッシュボード URL の入力を求める Nift サービス統合ページ。]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## 統合を使用する

インテグレーションを使用するには、メッセージングでリファラルリンクを配布します。顧客が紹介リンクを使用し、当社のブランドの1つからギフトを選択すると、ニフトはそれらをBrazeで処理されたものとしてマークします。

Braze との統合後、Nift は以下のデータを含む既存の顧客の Braze レコードにイベントを自動的にプッシュします。

- イベント名: `nift_processed`
- 時間:顧客がプレゼントを選択/使用した時刻



