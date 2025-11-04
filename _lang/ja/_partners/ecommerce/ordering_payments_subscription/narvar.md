---
nav_title: Narvar
article_title: Narvar
description: "Braze とNarvar を統合する方法を学びます。"
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar は、注文の追跡、配送の更新、返品管理を通じて顧客ロイヤルティを高める購入後のプラットフォームです。Braze と Narvar の統合により、ブランドは Narvar の通知イベントを活用して Braze から直接メッセージをトリガーし、顧客にタイムリーな更新情報を提供し続けることができます。

## 前提条件

| 必要条件           | 説明                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvar アカウント        | このパートナーシップを活用するには、Narvar アカウントが必要です。                           |
| Braze REST API キー    | `messages.send` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。                                            |
| Braze RESTエンドポイント   | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。これは Braze インスタンスの URL に応じて異なります。         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## サポートされている機能

|タイプ|サポートされている機能|
|-------|----------|
| 通知 | \- 配信予測<br>\- キャリア遅延<br>\- スタンダード |
| チャネル | プッシュ通知 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
その他の通知タイプやチャネルに興味がある場合は、Braze および Narvar CSM にお問い合わせください。
{% endalert %}

## 統合の詳細

通知イベントごとに、Narvar は Braze の[`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging)エンドポイントへのリクエストを開始し、オプトインした各消費者にプッシュメッセージを配信します。

Narvarは、各メッセージのプッシュ通知のペイロードを設定する責任がある。現在のところ、Narvarにはプッシュ通知のためのビルトイン・デザイン・インターフェイスがないため、彼らのチームはあなたのチームと協力してペイロードの要件を決定し、定義する。これらのペイロードは、注文データや消費者の詳細などの変数コンテンツプレースホルダーのサポートなど、独自のシステムを介して送信されるものと同じ範囲でカスタマイズできます。

## BrazeとNarvarの統合を始める

1. **Narvar のカスタマーサクセスマネージャーに連絡し**、統合への関心を伝えてください。
2. ステージングとプロダクション用に**Braze環境を指定する**。
3. BrazeでNarvar用の**API Keyを生成する**。
4. 必要に応じてBrazeで**キャンペーンキーを生成する**。
5. 安全なワンタイムリンクを介して **API キーとキャンペーンキーを Narvar に提供します**。
6. **プッシュ通知ペイロードの詳細を共有**して設定を完了します。
