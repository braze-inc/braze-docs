---
nav_title: Contentsquare
article_title: Contentsquare
description: "この参考記事では、BrazeとContentsquareの提携について概説している。Contentsquareは、デジタル体験分析プラットフォームであり、顧客のデジタル体験に基づいてメッセージをターゲティングすることで、キャンペーンの関連性とコンバージョン率を向上させることができる。"
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) は、カスタマーエクスペリエンスを今までにない方法で理解できるようにするデジタルエクスペリエンス分析プラットフォームです。

BrazeとContentsquareの統合により、Brazeのカスタムイベントとしてライブシグナル（不正行為、フラストレーションシグナルなど）を送信することができる。Contentsquareのエクスペリエンスインサイトを活用し、顧客のデジタルエクスペリエンスとボディランゲージに基づいてメッセージをターゲティングすることで、キャンペーンの関連性とコンバージョン率を向上させる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Contentsquare アカウント | このパートナーシップを活用するには、Contentsquare アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。Braze ダッシュボードで新しいキーを作成するには、**Settings** > **API Keys** に移動します。 |
| Braze RESTエンドポイント | [REST エンドポイント URL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

BrazeとContentsquareの一般的な使用例には、以下のようなものがある：
- Braze 内でカスタマーエクスペリエンスデータを表面化することで、顧客の意図に基づいてメッセージをハイパーパーパーパーソナライズする。
- 顧客のデジタル行動、躊躇、不満、意図に基づいて顧客をリターゲティングする。
- Contentsquare 内で不十分なエクスペリエンスを特定し、ターゲットを絞ったメッセージとリテンションオファーで顧客を取り戻す。
- 適切なタイミングと場所で、より適切で共感的なメッセージを送ることで、リスクのある顧客を回復させる。

## 統合

Contentsquare を Braze に統合するには、Contentsquare 統合カタログからの「Live Signals」のインストールをリクエストする必要があります。

1. Contentsquare で [**Settings**] メニューの [**Console**] をクリックします。これにより、現在取り組んでいるプロジェクトにリダイレクトされる。 
2. **Projects**ページで、**Integrations**タブに行き、**\+ Add integration**ボタンをクリックする。
3. 統合カタログで **Live Signals** 統合を見つけ、[**Add**] をクリックします。その後 Contentsquare チームが、ライブシグナルを Braze に送信するようにコードスニペットを設定することを依頼します。
4. Contentsquare により統合が処理されます。インジケーターのテキストは、統合完了後に更新される。

詳細については、「[Contentsquareの統合をリクエストする](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186)」を参照のこと。

## この統合を使う

統合が完了すると、Contentsquareのカスタムイベントがキャンペーンやキャンバスで使用できるようになる。[**Data Settings**] > [**Custom Events**] から、どのイベントが Braze に送信されているかを確認できます。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは**Manage Settings**>**Custom Events** にある。
{% endalert %}

![Braze の [カスタムイベント] タブのContentsquare ライブシグナルデータ][1]

[1]: {% image_buster /assets/img/contentsquare_custom_events.png %} 
