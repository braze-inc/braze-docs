---
nav_title: Jebbit
article_title:Jebbit
description:"この参考記事では、BrazeとJebbitのパートナーシップについて概説している。"Jebbitのキャンペーンからユーザーメールや属性をユーザーデータとしてリアルタイムにBrazeに渡すことができるPaaSである。
alias: /partners/jebbit/
page_type: partner
search_tag:Partner

---

# Jebbit

> [Jebbitは](https://www.jebbit.com/)、ユーザーにとって魅力的なエクスペリエンスを構築し、ファーストパーティデータを取得できるPaaSだ。

BrazeとJebbitの連携により、JebbitキャンペーンのユーザーメールやアトリビューションをユーザーデータとしてリアルタイムでBrazeに渡すことができる。このデータは、パーソナライズされたメールキャンペーンやトリガーなどのマーケティングイニシアティブを推進するために使用することができる。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Jebbitアカウント | このパートナーシップを利用するには、Jebbitアカウントが必要である。 |
| Braze REST API キー | すべてのユーザーデータ権限を持つBraze REST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
|Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Jebbitとの統合を依頼する際、厳しい納期が必要であれば伝えること。さらに、Brazeに渡したいJebbitエクスペリエンスにアトリビューションがマッピングされていることを確認する。

### ステップ1:API認証情報を提供する

API認証情報をテキストファイルでDropboxファイルリクエスト経由でJebbitに提供する。
以下の[Dropbox URLを](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx)使用してファイルを提出する。

### ステップ2:テストの提出を確認する

統合を担当するJebbitエンジニアが、JebbitからBrazeへのテスト送信をプッシュするので、Braze環境でデータがどのように見えるかを確認できる。これが統合を活性化させる最終ステップである。Jebbitデータの設定が完了したら、マーケティング施策の推進に活用しよう。

{% alert note %}
Jebbitで設定したアトリビューションIDは、Brazeでの属性フィールド名の表示方法となる。
{% endalert %}

## カスタマイズ

現在、[ユーザーデータの]({{site.baseurl}}/api/endpoints/user_data/)エンドポイントを特別にサポートしているが、異なるエンドポイントへのリクエストにも対応できる。
属性フィールド名も好みに応じてカスタマイズできる。

BrazeにJebbitの属性を追加したい場合は、Jebbitアカウントで新しい属性をマッピングする。その属性のデータを収集すると、アトリビューションに自動的に表示される。
