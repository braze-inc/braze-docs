---
page_order: 2.1
nav_title: ChatGPTアプリ
article_title: BrazeをChatGPTアプリと統合する
description: "BrazeをChatGPTアプリと統合する方法を学習し、AI搭載アプリケーション内で分析とイベント記録をイネーブルメントせよ。"
platform:
  - ChatGPT Apps
---

# BrazeをChatGPTアプリと連携させる

> このガイドでは、BrazeをChatGPTアプリと統合し、AI搭載アプリケーション内で分析とイベント記録をイネーブルメントする方法を説明する。

![ChatGPTアプリに統合されたコンテンツカード。]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## 概要

ChatGPTアプリは、AI対話型アプリケーションを構築するための強力なプラットフォームを提供する。BrazeをChatGPTアプリと統合することで、AI時代においてもファーストパーティデータのコントロール権限を維持し続けられる。具体的には以下の方法がある：

- ChatGPTアプリ内でのユーザーのエンゲージメントと行動をトラッキングする（例えば、顧客がどの質問やチャット機能を利用しているかを識別する）
- AIのインタラクションパターンに基づいてBrazeキャンペーンをセグメント化し、リターゲティングする（例：週に3回以上チャットを利用したユーザーにメールを送る）

### 主な利点

- **カスタマージャーニーを掌握せよ：**ユーザーがChatGPTを通じてあなたのブランドとやり取りする間、あなたは彼らの行動、好み、エンゲージメントパターンを把握し続ける。このデータはAIプラットフォームの分析機能だけでなく、Brazeのユーザープロファイルに直接流れ込む。
- **クロスプラットフォーム・リターゲティング：**ChatGPTアプリでのユーザーの操作をトラッキングし、そのAI利用パターンに基づいたパーソナライズされたキャンペーンで、自社所有チャネル（メール、SMS、プッシュ通知、アプリ内メッセージ）全体でリターゲティングする。
- **ChatGPTの会話に1:1のプロモーションコンテンツを返す：**チームがアプリ用に構築したカスタム対話型UIコンポーネントを使って、ChatGPT体験内で直接、Brazeの[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages)や[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)などを配信する。
- **収益アトリビューション：**ChatGPTアプリのやり取りから発生した購入とコンバージョンをトラッキングする。

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## 前提条件

BrazeをChatGPTアプリと統合する前に、以下の準備が必要だ：

- Brazeワークスペースに新しいWebアプリとAPI キーが追加された
- OpenAIプラットフォームで作成された[ChatGPTアプリ](https://openai.com/index/introducing-apps-in-chatgpt/)（[OpenAIサンプルアプリ](https://github.com/openai/openai-apps-sdk-examples)）

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

