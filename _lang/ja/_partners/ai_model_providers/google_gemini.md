---
nav_title: グーグル双子座
article_title: グーグル双子座
description: "この参考記事では、BrazeとGoogle Geminiのパートナーシップについて概説しており、GeminiモデルをBrazeに接続し、カスタムAIエージェントで使用することができる。"
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# グーグル双子座

> [Google Geminiは](https://deepmind.google/technologies/gemini/)GoogleのAIモデルファミリーで、テキスト、コード、画像写真に高度な推論を組み合わせ、ブランドがよりスマートでパーソナライズされた体験を提供できるよう支援する。

_この統合はグーグルによって維持されている。_

## 統合について

BrazeとGoogle Geminiの統合により、Google Gemini APIキーをBrazeに接続し、カスタムAIエージェントを構築する際にGeminiモデルを使用することができる。この統合により、エージェントはパーソナライズされたコピーを生成し、リアルタイムで意思決定を行い、GoogleのGeminiモデルを使用してカタログフィールドを更新することができる。

## 前提条件

| 要件 | 説明 |
|---|---|
| Gemini APIキーを持つGoogle Cloudアカウント | Gemini APIキーを持つGoogle Cloudアカウント。ヘルプについては、管理者または[Google Cloudサポートに](https://cloud.google.com/support)問い合わせること。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)またはBrazeオンボーディングマネージャーから見つけることができる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Google Gemini APIキーをBrazeに接続する：

1. Brazeダッシュボードの**Partner Integrations**>**Technology Partnersから**Google Geminiを探す。
2. GoogleからのAPIキーを入力する。
3. [**保存**] を選択します。

保存後、エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)際にGeminiモデルを選択することができる。

統合に関する問題や質問があれば、[Google Cloudサポートに](https://cloud.google.com/support)問い合わせること。
