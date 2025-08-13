---
nav_title: Jebbit
article_title: Jebbit
description: "この参考記事では、BrazeとJebbitのパートナーシップについて概説している。Jebbitのキャンペーンからユーザーメールや属性をユーザーデータとしてリアルタイムでBrazeに渡すことができるPaaSである。"
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) は、ユーザーがファーストパーティデータを取得するための魅力的なエクスペリエンスを構築できる PaaS です。

_この統合は Jebbit によって管理されます。_

## 統合について

Braze と Jebbit の統合により、Jebbit キャンペーンのユーザーメールと属性をユーザーデータとして Blaze にリアルタイムで渡すことができます。その後、パーソナライズされたメールキャンペーンやトリガーなどのマーケティングイニシアチブを推進するためにこのデータを利用できます。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Jebbitアカウント | このパートナーシップを活用するには、Jebbit アカウントが必要です。 |
| Braze REST API キー | すべてのユーザーデータ権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
|Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Jebbitとの統合を依頼する際、厳しい納期が必要であれば伝えること。さらに、Braze に渡す属性が Jebbit エクスペリエンスにマッピングされていることを確認します。

### ステップ1:API認証情報を提供する

API認証情報をテキストファイルでDropboxファイルリクエスト経由でJebbitに提供する。
以下の [Dropbox URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx) を使用してファイルを送信します。

### ステップ2:テスト送信を確認する

統合を担当するJebbitエンジニアが、JebbitからBrazeへのテスト送信をプッシュするので、Braze環境でデータがどのように見えるかを確認できる。これは、統合アクティブ化の最後の手順です。Jebbitのデータがセットアップされたので、それを使ってマーケティングイニシアティブを推進しよう。

{% alert note %}
Jebbitで設定した属性IDが、Brazeでの属性フィールド名の表示方法となる。
{% endalert %}

## カスタマイズ

現在、[ユーザーデータの]({{site.baseurl}}/api/endpoints/user_data/)エンドポイントを特別にサポートしているが、異なるエンドポイントへのリクエストもサポート可能だ。

属性フィールド名も好みに応じてカスタマイズできる。

Braze で Jebbit から追加の属性が必要な場合は、Jebbit アカウントで新しい属性をマッピングします。その属性のデータを収集すると、Brazeにその属性が自動的に表示される。

