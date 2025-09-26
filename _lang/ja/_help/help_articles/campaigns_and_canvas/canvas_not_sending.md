---
nav_title: キャンバス配信の問題
article_title: キャンバス配信の問題
page_order: 0
page_type: solution
description: "このヘルプ記事では、キャンバスの配信に関する問題のトラブルシューティングについて説明します。"
tool: Canvas
---

# キャンバス配信の問題

キャンバスは堅牢かつ複雑であり、作成する際には多くの時間と注意を要します。そのため、キャンバスが思いどおりに送信されない場合は、キャンバススケジュール、エントリオーディエンス、およびエントリ設定を確認し、[キャンバスの作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)ステップを見直すことをお勧めします。

## スケジュール

- キャンバスは[正しくスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#scheduled-delivery)されていますか?
- 正しい日付と時間を選択しましたか?
- キャンバスを起動してから、[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#action-based-delivery)のために、ユーザーが指定されたアクションを実行しましたか?

## エントリ設定

[エントリ設定]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas)は、キャンバスの送信方法を理解するために重要です。キャンバスにエントリする可能性のある人数を制限しているかどうかを確認してください。

メッセージを受信する資格がなくなったユーザーは、キャンバスを終了することもできます。例えば、キャンバスにプッシュ通知のみが含まれている場合、最初のステップを受信した後にプッシュ通知をオプトアウトしたユーザーはキャンバスから離脱します。[異なるキャンバスステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)を使用して、代わりのユーザー ジャーニーを追加することを検討してください。

## オーディエンスをセグメント化する

ターゲットオーディエンスに関する次の質問を考慮します。

- 正しいセグメントを選択しましたか?
- セグメントはどのように設定されていますか?
- セグメントにユーザーが含まれていることを確認しましたか?
- キャンバスにエントリするユーザーの数を制限するフィルターを追加しましたか?
- ユーザーがバリアントの最初のステップを受信する条件を満たしていますか? 例えば、キャンバスの最初のステップがプッシュ通知で、エントリオーディエンスがすべてプッシュ通知無効である場合、ユーザーはメッセージを受信しません。

{% alert tip %}
キャンバスのトラブルシューティングに関して追加のサポートが必要な場合は、問題が発生してから 30 日以内に Braze サポートにお問い合わせください。これは、診断ログが過去 30 日分しか保存されないためです。
{% endalert %}

_最終更新日: 2024年6月25日_