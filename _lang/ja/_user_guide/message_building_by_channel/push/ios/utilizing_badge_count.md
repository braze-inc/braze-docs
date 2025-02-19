---
nav_title: バッジ数の使用法
article_title: バッジ数の使用法
page_order: 8

page_type: reference
description: "この記事では、iOS バッジカウントを使用して、プッシュに気づかなかったユーザー、またはフォアグラウンドプッシュ通知s を無効にしたユーザーを再びエンゲージする方法について説明します。"
platform: iOS
channel: 
- push
- in-app messages

---

# バッジ数の使用法

> iOS バッジカウントには、アプリライケーション内の未読通知の数が表示されます。アプリアイコンの右上隅に赤い円が表示されます。近年、バッジングは、アプリユーザーを再エンゲージするための効果的な方法となっています。

バッジカウントを使用して、プッシュに気づかなかった、またはフォアグラウンドプッシュ通知s を無効にしたユーザーを再びエンゲージすることができます。また同様に、アプリ内更新などの未表示のメッセージをユーザーに通知するためにも使用できます。

## Braze のバッジ数

Braze ダッシュボードを通じてプッシュ通知を作成するときに、希望のバッジ数を指定できます。これをパーソナライズされたメッセージングでユーザー属性に設定して、完全なカスタマイズが可能なロジックを実現できます。ユーザーを妨害することなくバッジ数を更新するサイレントプッシュを送信する場合は、"Content-Available"フラグをプッシュに追加し、そのメッセージコンテンツを空のままにします。

{% alert note %}
Android のバッジ数を設定するにはどうしたらよいでしょう? Androidは自動的にプッシュのためのアプリバッジングを処理するので、Brazeでのバッジングのためのカスタマイズ設定はありません。
{% endalert %}

### バッジ数の削除

バッジ数を 0 または "" に設定して、アプリのアイコンからバッジ数を削除します。アプリがフォアグラウンドにある間にプッシュ通知を受信すると、Braze は自動的にバッジをクリアします。

## ベストプラクティス

バッジングの再エンゲージメント能力を最適化するには、ユーザーの操作性を最も簡素化する方法でバッジ設定を設定することが重要です。

### バッジ数を低く保つ
調査によると、バッジ数が 2 桁を超えて増えた後、ユーザーは一般に更新に関心を失い、しばしばアプリの使用を完全に中止することがわかっています。

> この規則には、アプリの性質 (メールやグループメッセージングアプリなど) によっては例外があります。

### バッジ数が表すことを制限する
バッジングの際は、できるだけ明確かつ直接的な通知を送る必要があります。バッジ通知が表現できるものの数を制限することで、アプリの機能や更新に精通しているという感覚をユーザーに与えることができます。

