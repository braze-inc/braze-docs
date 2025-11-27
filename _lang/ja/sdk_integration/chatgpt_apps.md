---
page_order: 2.1
nav_title: ChatGPTアプリ
article_title: BrazeとChatGPTアプリを統合する
description: "BrazeとChatGPTアプリを統合し、AI搭載アプリケーションで分析とイベントロギングをイネーブルメントする方法を学習する。"
platform:
  - ChatGPT Apps
---

# BrazeとChatGPTアプリを統合する

> このガイドでは、ChatGPTアプリとBrazeを統合し、AI搭載アプリ内で分析とイベントロギングを可能にする方法を説明する。

![ChatGPTアプリに統合されたコンテンツカード。]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## 概要

ChatGPTアプリは、AI会話アプリケーションを構築するための強力なプラットフォームを提供する。BrazeをChatGPTアプリに統合することで、AI時代においてもファーストパーティデータコントロールを維持し続けることができる：

- ChatGPTアプリ内のユーザーエンゲージメントや行動をトラッキング 追跡する（顧客がどの質問やチャット機能を使用しているかを特定するなど）
- AIのインタラクションパターンに基づいて、Brazeキャンペーンをセグメンテーションしリターゲティングする（例えば、週に3回以上チャットを利用したユーザーにメールを送信するなど）。

### 主なメリット

- **カスタマージャーニーを自分のものにする：**ユーザーがChatGPTを通じてあなたのブランドと交流している間、あなたはユーザーの行動、好み、エンゲージメントのパターンを可視化することができる。このデータは、AIプラットフォームの分析だけでなく、Brazeのユーザープロファイルに直接流れ込む。
- **クロスプラットフォームでリターゲティングする：**ChatGPTアプリ内のユーザーインタラクションをトラッキングし、AI利用パターンに基づいてパーソナライズされたキャンペーンでオウンドチャネル（メール、SMS、プッシュ通知、アプリ内メッセージング）を横断してリターゲティングする。
- **ChatGPTの会話に1:1のプロモーションコンテンツを返す：**アプリ用にチームが構築したカスタム会話UIコンポーネントを使用して、[アプリ内メッセージや]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) [コンテンツカードなどを]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)ChatGPTエクスペリエンス内で直接配信。
- **収益アトリビューション：**ChatGPTアプリのインタラクションに起因する購入やコンバージョンをトラッキング、追跡する。

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## 前提条件

BrazeとChatGPTアプリを統合する前に、以下のものを用意する必要がある：

- Brazeワークスペースに新しいWebアプリとAPIキーを追加する。
- OpenAIプラットフォームで作成された[ChatGPTアプリ](https://openai.com/index/introducing-apps-in-chatgpt/)[（OpenAIサンプルアプリ）](https://github.com/openai/openai-apps-sdk-examples)

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

