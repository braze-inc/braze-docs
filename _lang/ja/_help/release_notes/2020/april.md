---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には、2020年4月のリリースノートが含まれている。"
---
# 2020年4月

## Movable Inkとのパートナーシップ

Movable Inkは、Brazeの顧客に、カウントダウンタイマー、投票、スクラッチオフなどのIntelligent Creative機能をプッシュ、アプリ内メッセージ、コンテンツカードのキャンペーンで使用する機能を提供する。Movable InkとBrazeは、ダイナミックなデータドリブン型のメッセージに対するより充実したアプローチを提供し、ユーザーに重要な事柄に関するリアルタイムの要素を提供する。

[Movable Inkを]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/)キャンペーンに[組み込もう]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/)！

## インテリジェントタイミング

キャンペーンをスケジュールされる際、[インテリジェントタイミング]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/)（旧インテリジェントデリバリー）を使用することで、ユーザーが最もエンゲージメントしやすいとBrazeが判断したタイミングでメッセージを配信することができる。

この機能の更新は以下の通りである：
- **静粛時間の明確化**：クワイエット・アワーの機能は変わらないが、UIはわかりやすく調整されている。
- **プレビューチャートの**追加：インテリジェントタイミングを使用して、1日の各時間帯に何人のユーザーがメッセージを受信するか、また、最適な時間を計算するのに十分なデータを持っているユーザーの割合を確認するためのチャートを作成することができる。
- **カスタムフォールバックの**追加：最適な時間を計算するのに十分なエンゲージメントデータがない場合、ユーザーにメッセージを送信するローカライゼーション時間を選択できるようになった。

## Facebook オーディエンスのエクスポート

Brazeは、Facebookカスタムオーディエンスを作成するために、Brazeセグメンテーションページからユーザーを手動でエクスポートする機能を提供している。これは1回限りの静的オーディエンスのエクスポートであり、新しい[Facebookカスタムオーディエンスのみを]({{site.baseurl}}/partners/facebook/)作成する。

現在すべてのクラスタで利用可能で、新しいBraze Facebook オーディエンスエクスポートプロセスが存在し、シンプルな統合ステップでプロセスを合理化する。カスタムオーディエンスを送信するためにOAuthリダイレクトURIをホワイトリストに登録したり、Facebookアプリ設定内で統合のために弄ったりする必要がなくなる。

{% alert important %}
現在Facebookカスタムオーディエンスを使用している顧客は、これらの新しいステップでBrazeセグメンテーションを再統合する必要がある。
{% endalert%}


## コンテンツブロックとメールテンプレートのAPI更新

とcontent_block/list APIエンドポイントが更新された。 [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)と[content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)APIエンドポイントが更新され、新しい`tags` フィールドが追加された。このフィールドは、現在のブロックまたはメールテンプレートに適用されるタグを配列としてリストアップする。

## パーソナライズされたフロムアドレス

Brazeでメールメッセージを作成する際、メール作成の**送信情報**セクションでメッセージの差出人アドレスをパーソナライズできるようになった。サポートされている[パーソナライゼーション・タグを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)使用することができる。

![パーソナライズされたFromアドレス][0]{: style="max-width:80%"}

[0]: {% image_buster /assets/img/personalized-from-name.png %}
