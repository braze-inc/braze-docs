---
nav_title: "Playable"
article_title: Playable
description: "このリファレンス記事では、Braze とPlayable の連携について説明します。この動画 プラットフォームでは、Braze メール キャンペーンs に動画内容を追加できます。"
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable][1] では、自動再生動画をBraze メール キャンペーンs に追加できます。

BrazeとPlayableインテグレーションにより、最高のコンテンツ(高品質の動画)を最高のオーディエンス(メール)に届けることができ、受信トレイ内で自動的に再生される刺激的な高品質のコンテンツで、クリックスルーとポストクリックのメトリクスを向上させることができます。

## 前提条件

| 要件 | 説明 | 
| ----------- | ----------- |
| Playable会計 | この提携の前進タグeを考慮するには、Playableな考慮が必要である。Playable アカウントをまだ持っていない場合は、[ここで][signup] にサインアップします。
ビデオコンテンツ | Fac eBook、Ins タグ ram、YouTube、X (旧Twitter)、TikTokなどのWeb サイトから動画URLをPlayableしたり、提供したりするための読み込む 動画。 |
{: .reset-td-br-1 .reset-td-br-2}

## 実装

### ステップ1:動画をPlayableに追加する

Playable プラットフォームでは、Fac eBook、Ins タグ ram、YouTube、X (旧Twitter)、TikTok などの動画のURL を指定して、s をアップロード 動画または追加します。

### ステップ2:埋め込みコードをPlayableからコピーする

アップロードが「ed」になると、Playableはコードを生成します。このコードは、Braze キャンペーンに挿入すると、メールに動画が埋め込まれ、開封が鳴ったときに自動再生されます。メールが開封されている場合、Playableサーバーは、メール クライアント、機器、スクリーンサイズ、およびネットワーク状況に応じて、最適な動画を提供します。

{% alert tip %}
ビデオは、iPhone Mail、Gmail、Apple Mail、Outlook for iOS、Outlook for Android、Outlook for Mac、Outlook 365 for Windowsなど、受信トレイの98%以上で自動再生されます。従来のWindows版のOutlookのユーザには、代わりにスタティック"画像が表示されます。
{% endalert %}

### ステップ3:埋め込みコードをBrazeに貼り付けます

最後に、コードをBraze メール キャンペーンに貼り付けてから、メール キャンペーンのデザイン、テスト、公開を続行します。

[1]: https://playable.video
[signup]: https://signup.playable.video