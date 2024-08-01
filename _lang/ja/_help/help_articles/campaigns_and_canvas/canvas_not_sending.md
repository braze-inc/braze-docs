---
nav_title: キャンバス配送問題
article_title: キャンバス配送問題
page_order: 0
page_type: solution
description: "このヘルプでは、キャンバスの配信に関する問題のトラブルシューティングについて説明する。"
tool: Canvas
---

# キャンバスの配送に関する問題

キャンバスは頑丈で複雑なものであり、あなたがキャンバスを制作する際に時間をかけ、細心の注意を払っていることを私たちは知っている。キャンバスが思い通りに送信されない場合は、キャンバスのスケジュール、エントリーのオーディエンス、エントリーの設定を確認し、[キャンバスの作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)ステップを見直すことをお勧めする。

## スケジュールされた

- キャンバスの[スケジュールは正しく]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#scheduled-delivery)組まれているか？
- 正しい日時を選択したか？
- [アクションベースの配信では]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#action-based-delivery)、キャンバスを起動してからユーザーが指定されたアクションを実行したか。

## エントリ設定

[エントリーの設定は]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas)、キャンバスがどのように送信されているかを理解するために重要である。キャンバスに入る可能性のある人数を制限しているかどうかを確認する。

ユーザーは、メッセージを受け取る資格がなくなった場合、キャンバスから退出することもできる。例えば、キャンバスがプッシュ通知のみを含む場合、ユーザーが最初のステップを受信した後にプッシュ通知を拒否すると、そのユーザーはキャンバスから脱落することになる。[異なるキャンバスステップを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components)使用して、代替ユーザージャーニーを追加することを検討する。

## オーディエンスをセグメント化する

あなたのターゲットオーディエンスについて、以下の質問を考えてみよう：

- 正しいセグメンテーションを選択したか？
- セグメンテーションはどのように設定されているのか？
- セグメンテーションにユーザーが含まれていることを確認したか？
- キャンバスに入るユーザー数を制限するようなフィルターを追加したか？
- ユーザーはバリアントの最初のステップを受ける資格があるか？例えば、キャンバスの最初のステップがプッシュ通知であるにもかかわらず、エントリーのオーディエンスが全員プッシュを無効にしている場合、どのユーザーにもメッセージは届かない。

{% alert tip %}
キャンバスのトラブルシューティングについては、過去30日分の診断ログしか残っていないため、問題発生から30日以内に必ずBrazeサポートに連絡すること。
{% endalert %}

_最終更新日：2024年6月25日_