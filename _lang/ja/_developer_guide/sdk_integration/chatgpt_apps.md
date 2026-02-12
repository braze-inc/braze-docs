---
page_order: 2.1
nav_title: ChatGPT アプリs
article_title: Braze とChatGPT アプリの統合
description: "Braze をChatGPT アプリ s と統合して、AI 電源付きアプリアプリケーション内で分析およびイベントログを有効にする方法について説明します。"
platform:
  - ChatGPT Apps
---

# Braze とChatGPT アプリ の統合

> 本書では、Braze をChatGPT アプリ s と統合して、AI を搭載したアプリアプリケーション内で分析およびイベントログを有効にする方法について説明します。

![チャットGPTアプリに統合されたコンテンツカード。]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## 概要

ChatGPT アプリは、AI 対話型アプリライセンスを構築するための強力なプラットフォームを提供します。Braze をChatGPT アプリと統合することで、次の方法を含め、AI 時代のファーストパーティデータコントロールを引き続き維持できます。

- ChatGPT アプリ内のユーザー エンゲージメントと動作を追跡する(顧客が使用する疑問またはチャット機能を特定するなど)
- AIインターアクション型をベースにしたセグメントとリターゲティングする Braze キャンペーンs(1週間に3回以上チャットを利用したユーザーsのメールなど)

### 主な効果

- **カスタマージャーニーを所有する:**ユーザーはChatGPTを介してブランドと対話する一方で、その行動、好み、およびエンゲージメント形態の可視性を維持します。このデータは、AI プラットフォームの分析だけでなく、Braze ユーザープロファイルにも直接的に流れます。
- **クロスプラットフォーム リターゲティング:**ChatGPT アプリでユーザーのインターアクションを追跡し、AI 使用パターンに基づいてパーソナライズされた キャンペーン s を使用して、所有するチャネル(メール、SMS、プッシュ通知 s、アプリ内メッセージング) 間でリターゲティングするします。
- **1:1 プロモーションコンテンツをChatGPT 会話に返します。**Braze [ アプリ内メッセージ s]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages)、[ コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) など、アプリ用に作成したカスタム会話UI コンポーネントを使用して、ChatGPT エクスペリエンス内で直接的に配信します。
- **収益アトリビューション:**ChatGPT アプリ inter アクション s から発信される購買とコンバージョンを追跡します。

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## 前提条件

Braze をChatGPT アプリに統合するには、次のものが必要です。

- Braze ワークスペースの新しいアプリとAPI キー
- A [ChatGPT アプリ](https://openai.com/index/introducing-apps-in-chatgpt/) がOpenAI プラットフォームに作成されました([OpenAI サンプルアプリ](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

