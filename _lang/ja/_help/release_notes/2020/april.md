---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事は、2020年4月のリリースノートを含んでいます。"
---
# 2020年4月

## Movable Ink提携

Movable Ink は、Braze 顧客 のプッシュ、アプリ内メッセージ、コンテンツカードキャンペーンで、カウントダウンタイマー、ポーリング、スクラッチオフなどのインテリジェントクリエイティブ機能を使用できます。Movable InkとBrazeの力は、より丸みを帯びたアプリをダイナミックな データドリブン型のの伝言に訴え、問題の内容に関するリアルタイムの要素をユーザーに提供する。

[ Movable Ink]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/) をキャンペーンs に統合します!

## インテリジェントタイミング

キャンペーンのスケジュールを設定する場合、[インテリジェントタイミング]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/)(以前はインテリジェント配信)を使用して、Brazeが個人が参加する可能性が最も高いと判断したときに、それぞれのユーザーにメッセージを配信できます。

この機能の更新内容は次のとおりです。
- **静音時間の明確化**:Quiet Hours 機能は同じままですが、UI は明確化のために調整されています。
- **プレビューチャートの追加**:これで、インテリジェント・タイミングを使用して、1 時間ごとにメッセージを受け取るユーザーの数と、最適な時刻を計算するために十分なデータを持っているユーザーの割合を示すグラフを作成できます。
- **カスタムフォールバックの追加**:最適な時刻を計算するのに十分なエンゲージメント情報がない場合に、ユーザーがメッセージを送信するローカル時刻を選択できるようになりました

## Facebook オーディエンス輸出

Braze では、Brazeセグメントページからユーザーを手動でエクスポートして、Fac eBook カスタムオーディエンスを作成できます。これは、1 回限りのスタティックオーディエンスエクスポートであり、新しい[Fac eBook ユーザ定義オーディエンスs]({{site.baseurl}}/partners/facebook/) のみを作成します。

現在、すべてのクラスターで利用可能な新しいBraze Facebook オーディエンスエクスポートプロセスがあり、シンプルなインテグレーションステップs でプロセスを合理化しています。OAuth リダイレクトURI のホワイトリストを作成して、Fac eBook アプリ設定内でカスタムオーディエンスまたは混乱を送信して統合する必要がなくなりました。

{% alert important %}
現在Fac eBook カスタムオーディエンスを使用しているすべてのクライアントは、これらの新しいステップでBrazeセグメントを再統合する必要があります。
{% endalert%}


## コンテンツブロックおよびメール テンプレート API 更新

[template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)および[content_ブロック/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)API エンドポイントsは、新しい`tags`フィールドを含むように更新されました。このフィールドは、現行のブロックまたはメール テンプレートにアプリする任意のタグs を配列として列挙します。

## カスタマイズされた発信元アドレス

メール メッセージをBraze 内で作成するときに、メール構成の**送信情報** セクションでメッセージのFrom Address をパーソナライズできるようになりました。サポートされている任意の[パーソナライゼーション タグs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用できます。

![アドレスからカスタマイズ][0]{: style="max-width:80%"}

[0]: {% image_buster /assets/img/personalized-from-name.png %}
