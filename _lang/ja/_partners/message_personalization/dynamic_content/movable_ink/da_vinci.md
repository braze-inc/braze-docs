---
title: "Movable Ink ダ・ヴィンチ"
article_title: Movable Ink ダ・ヴィンチ
alias: "/partners/movable_ink_da_vinci/"
description: "BrazeとMovable Ink Da Vinciの統合により、ブランドはDa VinciのAI駆動型コンテンツ決定エンジンを活用することで、高度にパーソナライズされたメッセージングを提供できるようになる。ダ・ヴィンチはユーザーごとに最も関連性の高いコンテンツをキュレーションし、Brazeを通じてシームレスにメッセージを展開する。"
page_type: partner
search_tag: Partner

---

# Movable Ink ダ・ヴィンチ

> BrazeとMovable Ink[Da Vinciの](https://movableink.com/da-vinci)統合により、ブランドはDa VinciのAI駆動型コンテンツ決定エンジンを活用することで、高度にパーソナライズされたメッセージングを提供できるようになる。ダ・ヴィンチはユーザーごとに最も関連性の高いコンテンツをキュレーションし、Brazeを通じてシームレスにメッセージを展開する。

## 前提条件

| 必要条件 | 説明 |
|------------|-------------|
| Movable Ink ダ・ヴィンチ | このパートナーシップを利用するには、Movable Inkダ・ヴィンチのアカウントが必要である。 |
| Braze Currents - メッセージ・エンゲージメント・イベント | メッセージエンゲージメントイベントデータをMovable Inkに送信するには、Braze Custom Currents Exportが必要である。 |
| Braze REST API キー | `messages.send`,`sends.id.create`,`campaigns.details` の権限を持つREST APIキーが必要である。これはダッシュボードの**「設定\*」>「** **APIキー**」から作成できる。<br><br>Movable Inkのアカウントチームから直接、セットアップの詳細について説明がある。[統合の](#integration)セクションを参照のこと。|
| Brazeのダ・ヴィンチアプリインスタンス | Brazeでダヴィンチ専用のアプリインスタンスを作成する。新しいアプリは、Brazeダッシュボードの**設定**＞**アプリ設定**＞**＋アプリ追加で**作成できる。アプリ名を「**Movable Ink - Da Vinci**」とし、任意のプラットフォームを選択する（プラットフォームの選択は必須だが、タイプは機能に影響しない）。[新しいアプリを追加する方法については]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances)、こちらを学習する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

統合を開始するには、Movable Inkのアカウント・チームに問い合わせること。Movable Inkは、アクセス方法とセットアップ方法を適宜提供する。Da VinciがBrazeのメッセージングAPIを通じてメールデプロイメントを送信できるようにするには、Braze API認証情報のセットをMovable Inkに提供する必要がある。

接続すると、Movable Inkはこうなる：

- クライアントおよびBrazeと協力して、ブランドのダヴィンチアカウントを設定し、Brazeでの展開を成功させる。
- メッセージングのユースケースに合わせて、ブランド固有のコンフィギュレーションをキャプチャする。
- 包括的なテストと品質保証を実施し、メールが意図したとおりに配信され、すべてのパフォーマンスと運用基準を満たしていることを検証する。
