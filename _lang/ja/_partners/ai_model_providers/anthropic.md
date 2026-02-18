---
nav_title: アンソロピック
article_title: アンソロピック
description: "この参考記事では、BrazeとAnthropicのパートナーシップについて概説しており、クロードモデルをBrazeに接続し、カスタムAIエージェントで使用することができる。"
alias: /partners/anthropic/
page_type: partner
search_tag: Partner

---

# アンソロピック

> [Anthropicは](https://www.anthropic.com/)、AIの安全性と研究を行っている会社で、幅広い言語タスクに役立ち、正直で、安全な次世代AIアシスタント、Claudeを開発している。

_この統合はAnthropicによって維持されている。_

## 統合について

BrazeとAnthropicの統合により、Anthropic APIキーをBrazeに接続し、カスタムAIエージェントを構築する際にクロードモデルを使用することができる。この統合により、エージェントはパーソナライズされたコピーを生成し、リアルタイムで意思決定を行い、Anthropicのクロードモデルを使用してカタログフィールドを更新することができる。

## 前提条件

| 要件 | 説明 |
|---|---|
| APIキーを持つAnthropicアカウント | APIキーを持つAnthropicアカウント。ヘルプについては、管理者または[Anthropicサポートに](https://support.anthropic.com/)連絡すること。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)またはBrazeオンボーディングマネージャーから見つけることができる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

AnthropicのAPIキーをBrazeに接続する：

1. Brazeダッシュボードの**パートナー連携**>**テクノロジーパートナーから**Anthropicを探す。
2. AnthropicのAPIキーを入力する。
3. [**保存**] を選択します。

保存後、エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)際に、クロードモデルを選択することができる。

統合に関する問題や質問があれば、[Anthropicサポートに](https://support.anthropic.com/)連絡すること。
