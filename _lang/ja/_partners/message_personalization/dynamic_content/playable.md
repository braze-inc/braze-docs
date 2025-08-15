---
nav_title: "Playable"
article_title: Playable
description: "このリファレンス記事では、Braze と Playable のパートナーシップについて説明します。Playable は動画プラットフォームであり、動画コンテンツを Braze メールキャンペーンに追加できます。"
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable][1] では、自動再生動画をBraze メール キャンペーンs に追加できます。

_この統合は Playable によって管理されます。_

## 統合について

Braze と Playable の統合により、最高のコンテンツ( 高品質動画) を最高のオーディエンスに配信でます (メール)。受信トレイで自動的に再生されるエキサイティングな高品質のコンテンツにより、クリックスルーとポストクリックの指標が向上します。

## 前提条件

| 必要条件 | 説明 | 
| ----------- | ----------- |
| Playable アカウント | このパートナーシップを活用するには、Playable アカウントが必要です。Playable アカウントをまだお持ちでない場合は、[こちら][signup]からご登録ください。
ビデオコンテンツ | 動画ファイルを Playable にアップロードするか、または Facebook、Instagram、YouTube、X (旧 Twitter)、TikTok などの Web サイトの動画 URL を指定します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 実装

### ステップ1:動画を Playable に追加する

Playable プラットフォームで、動画ファイルをアップロードするか、または Facebook、Instagram、YouTube、X (旧 Twitter)、TikTok などの動画の URL を指定して動画を追加します。

### ステップ2:埋め込みコードをPlayableからコピーする

アップロードが完了すると、Playable によりコードが生成されます。このコードが Braze キャンペーンに挿入されると、メールに動画が埋め込まれ、メールを開封すると自動再生されます。メールが開封されると、メールクライアント、デバイス、スクリーンサイズ、およびネットワーク状況に応じて最適な動画が Playable サーバーから配信されます。

{% alert tip %}
動画は、iPhone Mail、Gmail、Apple Mail、Outlook for iOS、Outlook for Android、Outlook for Mac、Outlook 365 for Windows など、受信トレイの 98% 以上で自動再生されます。従来の Outlook for Windows をご利用の場合は、動画の代わりに静止画像が表示されます。
{% endalert %}

### ステップ3:埋め込みコードをBrazeに貼り付けます

最後に、コードをBraze メール キャンペーンに貼り付けてから、メール キャンペーンのデザイン、テスト、公開を続行します。


[1]: https://playable.video
[signup]: https://signup.playable.video