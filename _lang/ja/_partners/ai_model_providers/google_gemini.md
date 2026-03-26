---
nav_title: Google Gemini
article_title: Google Gemini
description: "この参照記事では、BrazeとGoogle Geminiのパートナーシップについて概説しています。GeminiモデルをBrazeに接続し、カスタムAIエージェントで使用できます。"
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/)は、GoogleのAIモデルファミリーで、テキスト、コード、画像にわたる高度な推論を組み合わせ、ブランドがよりスマートでパーソナライズ済みの体験を提供できるよう支援します。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_この統合はGoogleによって管理されています。_

## 統合について

BrazeとGoogle Geminiの統合により、Google Gemini APIキーまたはVertex AIキーをBrazeに接続し、カスタムAIエージェントを構築する際にGeminiモデルを使用できます。この統合により、エージェントはパーソナライズ済みのコピーを生成し、リアルタイムで意思決定を行い、GoogleのGeminiモデルを使用してカタログフィールドを更新できます。

## 前提条件

| 要件 | 説明 |
|---|---|
| Gemini APIキーまたはVertex AIキーを持つGoogle Cloudアカウント | Gemini APIキーまたはVertex AIキーを持つGoogle Cloudアカウントが必要です。ヘルプについては、管理者または[Google Cloudサポート](https://cloud.google.com/support)にお問い合わせください。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Google Gemini APIキーをBrazeに接続するには、以下の手順に従います。

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、Google Geminiを見つけます。
2. **API Type**で、**Gemini API**または**Vertex AI**を選択します。
3. GoogleのAPIキーを入力します。Vertex AIの場合は、プロジェクトIDを入力します。
4. **Save**を選択します。

保存後、エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)際にGeminiモデルを選択できます。

統合に関する問題や質問がある場合は、[Google Cloudサポート](https://cloud.google.com/support)にお問い合わせください。