---
nav_title: コンテンツスクエア
article_title: コンテンツスクエア
description: "この参考記事では、BrazeとContentsquareの提携について概説している。Contentsquareは、デジタル体験分析プラットフォームであり、顧客のデジタル体験に基づいてメッセージをターゲティングすることで、キャンペーンの関連性とコンバージョン率を向上させることができる。"
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# コンテンツスクエア

> [Contentsquareは](https://contentsquare.com/)、前例のない顧客体験の理解を可能にするデジタル体験分析プラットフォームである。

BrazeとContentsquareの統合により、Brazeのカスタムイベントとしてライブシグナル（不正行為、フラストレーションシグナルなど）を送信することができる。Contentsquareのエクスペリエンスインサイトを活用し、顧客のデジタルエクスペリエンスとボディランゲージに基づいてメッセージをターゲティングすることで、キャンペーンの関連性とコンバージョン率を向上させる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| コンテンツクエアアカウント | このパートナーシップを利用するには、Contentsquareのアカウントが必要だ。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとContentsquareの一般的な使用例には、以下のようなものがある：
- Braze内の顧客経験データを表面化することで、顧客の意図に基づいてメッセージを高度にパーソナライズする。
- 顧客のデジタル行動、躊躇、フラストレーション、意図に基づいてリターゲティングを行う。
- Contentsquareの中で悪い経験を特定し、ターゲットを絞ったメッセージとリテンション・オファーで顧客を回復させる。
- 適切なタイミングと場所で、より適切で共感的なメッセージを送ることで、リスクのある顧客を回復させる。

## 統合

ContentsquareをBrazeに統合するには、Contentsquare統合カタログから「Live Signals」統合のインストールをリクエストする必要がある：

1. Contentsquareで、**設定**メニューの**Consoleを**クリックする。これにより、現在取り組んでいるプロジェクトにリダイレクトされる。 
2. **Projects**ページで、**Integrations**タブに行き、**\+ Add integration**ボタンをクリックする。
3. 統合カタログで、**Live Signals**統合を見つけ、**Addを**クリックする。Contentsquareチームは、Brazeにライブシグナルを送信するためのコードスニペットを設定するために連絡を取る。
4. Contentsquareがあなたの統合を処理する。インジケーターのテキストは、統合完了後に更新される。

詳細については、「[Contentsquareの統合をリクエストする](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186)」を参照のこと。

## この統合を使う

統合が完了すると、Contentsquareのカスタムイベントがキャンペーンやキャンバスで使用できるようになる。どのイベントがBrazeに送信されているかは、**Data Settings**>**Custom Eventsから**確認できる。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは**Manage Settings**>**Custom Events** にある。
{% endalert %}

![BrazeカスタムイベントタブのContentsquareライブシグナルデータ][1]

[1]: {% image_buster /assets/img/contentsquare_custom_events.png %} 