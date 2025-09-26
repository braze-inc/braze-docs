---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "Braze と Movable Ink Da Vinci の統合により、ブランドはDa Vinci の AI ドリブン型コンテンツ決定エンジンを活用して、高度なパーソナライズメッセージングを配信できます。Da Vinci はユーザーごとに最も関連性の高いコンテンツをキュレートし、Braze を通じてメッセージをシームレスに展開します。"
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> Braze と Movable Ink [Da Vinci](https://movableink.com/da-vinci) の統合により、ブランドは Da Vinci の AI ドリブン型コンテンツ決定エンジンを活用して、高度なパーソナライズメッセージングを配信できます。Da Vinci はユーザーごとに最も関連性の高いコンテンツをキュレートし、Braze を通じてメッセージをシームレスに展開します。

## 前提条件

| 必要条件 | 説明 |
|------------|-------------|
| Movable Ink Da Vinci | このパートナーシップを利用するには、MMovable Ink Da Vinci のアカウントが必要です。 |
| Braze Currents - メッセージ・エンゲージメント・イベント | メッセージエンゲージメントイベントデータを Movable Ink に送信するには、Braze カスタム Currents エクスポートが必要です。 |
| Braze REST API キー | `messages.send`、`sends.id.create`、`campaigns.details` の権限が付与された Braze REST API キーが必要です。これは、Braze ダッシュボードの [**設定**]* > [**API キー**] で作成できます。<br><br>詳細な設定方法については、Movable Ink のアカウントチームに直接、お問い合わせください。「[統合](#integration)」セクションを参照してください。|
| Brazeのダ・ヴィンチアプリインスタンス | Braze で Da Vinci 専用のアプリインスタンスを作成します。新しいアプリは、Braze ダッシュボードの [**設定**] > [**アプリ設定**] > [**\+ アプリを追加**] で作成できます。アプリ名を「**Movable Ink - Da Vinci**」とし、任意のプラットフォームを選択する（プラットフォームの選択は必須だが、タイプは機能に影響しない）。[新しいアプリを追加する方法については]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances)、こちらを学習する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

統合を開始する際は、Movable Ink のアカウントチームにお問い合わせください。Movable Ink からアクセスと設定に関する手順が適宜提供されます。Da Vinci が Braze の Messaging API を通じてメールデプロイメントを送信できるようにするには、Braze API 認証情報のセットを Movable Ink に提供する必要があります。

接続後、Movable Ink は以下を実行します。

- クライアントおよびBrazeと協力して、ブランドのダヴィンチアカウントを設定し、Brazeでの展開を成功させる。
- メッセージングのユースケースに合わせて、ブランド固有のコンフィギュレーションをキャプチャする。
- 包括的なテストと品質保証を実施し、メールが意図したとおりに配信され、パフォーマンスと運用のすべての基準を満たしていることを検証します。
