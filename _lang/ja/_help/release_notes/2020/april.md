---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には、2020年4月のリリースノートが含まれています。"
---
# 2020年4月

## Movable Ink のパートナーシップ

Movable Ink は、プッシュ、アプリ内メッセージ、およびコンテンツカードキャンペーンでカウントダウンタイマー、投票、スクラッチオフなどのインテリジェントクリエイティブ機能を使用するための機能を Braze のお客様に提供します。Movable Ink と Braze は、ダイナミックなデータドリブン型のメッセージに対するより包括的なアプローチを実現し、重要事項に関するリアルタイムのエレメントをユーザーに提供します。

キャンペーンに[ Movable Ink を統合]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/)しましょう。

## インテリジェントタイミング

キャンペーンのスケジュールを設定する場合、[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)(以前はインテリジェント配信)を使用して、Brazeが個人が参加する可能性が最も高いと判断したときに、それぞれのユーザーにメッセージを配信できます。

この機能の更新内容は次のとおりです。
- **サイレント時間の明確化**:サイレント時間機能に変更はありませんが、UI は明確化のために調整されています。
- **プレビューチャートの追加**:インテリジェントタイミングを使用して、1日の各時間にメッセージを受信するユーザー数と、最適な時間を計算するのに十分なデータがあるユーザーの割合を確認するためのチャートを生成できるようになりました。
- **カスタムフォールバックの追加**:最適な時刻を計算するのに十分なエンゲージメント情報がない場合に、ユーザーがメッセージを送信するローカル時刻を選択できるようになりました

## Facebook オーディエンス輸出

Braze では、Braze セグメントページからユーザーを手動でエクスポートして Facebook カスタムオーディエンスを作成する機能が提供されています。これは1回限りの静的オーディエンスエクスポートであり、新しい [Facebook カスタムオーディエンス]({{site.baseurl}}/partners/facebook/)のみが作成されます。

現在、すべてのクラスターで利用可能な新しいBraze Facebook オーディエンスエクスポートプロセスがあり、シンプルなインテグレーションステップs でプロセスを合理化しています。カスタムオーディエンスを送信するために OAuth リダイレクト URI をホワイトリストに登録したり、統合するために Facebook アプリ設定内で操作したりする必要がなくなります。

{% alert important %}
現在 Facebook カスタムオーディエンスを使用しているすべてのクライアントが、これらの新しいステップを使用して Braze セグメントを再統合する必要があることに注意してください。
{% endalert%}


## コンテンツブロックおよびメール テンプレート API 更新

[template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)および[content_ブロック/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)API エンドポイントsは、新しい`tags`フィールドを含むように更新されました。このフィールドは、現行のブロックまたはメール テンプレートにアプリする任意のタグs を配列として列挙します。

## パーソナライズされた差出人アドレス

メール メッセージをBraze 内で作成するときに、メール構成の**送信情報** セクションでメッセージのFrom Address をパーソナライズできるようになりました。サポートされている任意の[パーソナライゼーション タグs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用できます。

![パーソナライズされた差出人アドレス]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

