---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には、2020 年 4 月のリリースノートが含まれています。"
---
# 2020 年 4 月

## ムーバブル・インクのパートナーシップ

Movable Ink により、Braze のお客様は、プッシュ通知、アプリ内メッセージ、コンテンツカードキャンペーンで、カウントダウンタイマー、投票、スクラッチオフなどのインテリジェントクリエイティブ機能を使用できます。Movable InkとBrazeは、データ主導型の動的なメッセージへのより包括的なアプローチを強化し、重要なことに関するリアルタイムの要素をユーザーに提供します。

[Movable Inkをキャンペーンに統合し始めましょう]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/)！

## インテリジェントタイミング

キャンペーンをスケジュールする際、[インテリジェントタイミング]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/)（以前はインテリジェントデリバリー）を使用して、Braze が個人がエンゲージメントする可能性が最も高いと判断した時間に各ユーザーにメッセージを配信できます。

この機能の更新には以下が含まれます。
-**クワイエットアワーの明確化**:Quiet Hoursの機能は同じままですが、わかりやすいようにUIが調整されています。
-**プレビューチャートの追加**:これで、インテリジェントタイミングを使用して 1 日の各時間にメッセージを受信するユーザーの数と、最適な時間を計算するのに十分なデータを持っているユーザーの割合を確認できるグラフを生成できます。
-**カスタムフォールバックの追加**:最適な時間を計算するのに十分なエンゲージメントデータがない場合に、ユーザーにメッセージを送信するローカル時間を選択できるようになりました

## Facebook オーディエンスのエクスポート

Braze では、Braze セグメントページから手動でユーザーをエクスポートして Facebook カスタムオーディエンスを作成することができます。これは 1 回限りの静的オーディエンスのエクスポートで、新しい [Facebook カスタムオーディエンスのみが作成されます]({{site.baseurl}}/partners/facebook/)。

現在、すべてのクラスターで利用できる新しいBraze Facebookオーディエンスエクスポートプロセスがあり、簡単な統合手順でプロセスを合理化できます。カスタムオーディエンスを送信するためにOAuthリダイレクトURIをホワイトリストに登録したり、Facebookアプリの設定をいじって統合したりする必要はもうありません。

{% alert important %}
なお、現在Facebookカスタムオーディエンスを使用しているすべてのクライアントは、この新しい手順でブレイズセグメントを再統合する必要があります。
{% endalert%}


## コンテンツブロックとメールテンプレート API の更新

[/email/listテンプレートと]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) [content\_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API エンドポイントが更新され、新しいフィールドが追加されました。`tags`このフィールドには、現在のブロックまたはメールテンプレートに適用されるすべてのタグが配列として一覧表示されます。

## パーソナライズされた差出人住所

Braze でメールメッセージを作成する際、メール作成の「**送信情報」セクションでメッセージの送信元アドレスをカスタマイズできるようになりました**。[サポートされているパーソナライゼーションタグのいずれかを使用できます]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

![個人設定送信者住所] [0]{: style="max-width:80%"}

[0]: {% image_buster /assets/img/personalized-from-name.png %}
