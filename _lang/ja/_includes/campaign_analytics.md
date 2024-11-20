## キャンペーン分析

キャンペーンを開始したら、そのキャンペーンの詳細ページに戻って主要な指標を見ることができる。**キャンペーン**ページに移動し、キャンペーンを選択して詳細ページを開封する。{% if include.channel == "Content Card" %}コンテンツカード{% elsif include.channel == "email" %}メール{% elsif include.channel == "in-app message" %}アプリ内メッセージ{% elsif include.channel == "push" %}プッシュメッセージ{% elsif include.channel == "SMS" %}SMSメッセージ{% elsif include.channel == "whatsapp" %}WhatsAppメッセージ{% elsif include.channel == "webhook" %}Webhooks{% endif %}キャンバスで送信されたものについては、[キャンバス分析を]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)参照のこと。

{% alert tip %}
レポートに記載されている用語や指標の定義をお探しですか？を参照されたい。
  {% if include.channel == "email" %}[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "Content Card" %}[レポート指標用語集と]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)コンテンツカードによるフィルター
  {% elsif include.channel == "in-app message" %}[レポートメトリクス用語集と]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)アプリ内メッセージによるフィルター
  {% elsif include.channel == "push" %}[レポート指標 用語集と]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)フィルター 押す
  {% elsif include.channel == "SMS" %}[レポート指標用語集と]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)SMSによるフィルター
  {% elsif include.channel == "whatsapp" %}[レポート指標用語集と]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)WhatsAppによるフィルター
  {% elsif include.channel == "webhook" %}[Report Metrics Glossary]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)and filter by Webhook{% endif %}.
{% endalert %}

**キャンペーン分析**タブから、一連のパネルでレポートを見ることができる。以下のセクションに列挙されているものよりも多く見たり少なく見たりするかもしれないが、それぞれに有用な目的がある。

### キャンペーンの詳細

**キャンペーンの詳細**パネルには、キャンペーン全体のパフォーマンスのハイレベルな概要が表示される。
  {% if include.channel == "Content Card" %}コンテンツカードだ。
  {% elsif include.channel == "email" %}メール.
  {% elsif include.channel == "in-app message" %}アプリ内メッセージ.
  {% elsif include.channel == "push" %}メッセージをプッシュする。
  {% elsif include.channel == "SMS" %}SMSだ。
  {% elsif include.channel == "whatsapp" %}WhatAppのメッセージ。
  {% elsif include.channel == "webhook" %}Webhook.
  {% endif %}

このパネルでは、受信者に送信されたメッセージの数、1 次コンバージョン率、このメッセージによって生み出された総収益などの全体的な指標を確認します。このページから、配信、オーディエンス、コンバージョン設定を確認することもできます。

{% if include.channel == "whatsapp" %}
{% alert note %}
WhatsAppチャネルにはリードレートが含まれる。この指標は、読み取りレシートをオンにしているユーザーに対してのみ配信される。
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![]({% image_buster /assets/img/cc-campaign-details.png %}) キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。

{% elsif include.channel == "email" %}
![]({% image_buster /assets/img/campaign_details_email.png %}) キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。

{% elsif include.channel == "push" %}
![]({% image_buster /assets/img/campaign_details_push.png %}) キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。

{% elsif include.channel == "SMS" %}
![]({% image_buster /assets/img/campaign_details_sms.png %}) キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。

{% elsif include.channel == "in-app message" %}
![]({% image_buster /assets/img/campaign_details_iam.png %}) キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。

キャンバスでは、作成したキャンバスにアプリ内メッセージのパフォーマンスがマッピングされる。ページ上部にあるコントロールパネルを使って、他のメッセージングタイプ（チャネル）を消去し、キャンバス内のアプリ内メッセージのみを表示することができる。

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![]({% image_buster /assets/img/campaign_details_webhook.png %}) キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。

{% endif %}

{% if include.channel == "Content Card" %}

#### コントロールグループ {#cc-control-group}

個々のコンテンツカードのインパクトを測定するために、A/Bテストに[コントロールグループを][2]追加することができる。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% elsif include.channel == "SMS" %}

#### コントロールグループ {#sms-control-group}

個々のSMSメッセージのインパクトを測定するには、A/Bテストに[コントロールグループを][2]追加することができる。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% elsif include.channel == "whatsapp" %}

#### コントロールグループ {#whatsapp-control-group}

個々のWhatsAppメッセージのインパクトを測定するには、A/Bテストに[コントロールグループを][2]追加する。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% elsif include.channel == "webhook" %}

#### コントロールグループ {#webhook-control-group}

個々のWebhookメッセージの影響を測定するには、A/Bテストに[コントロールグループを][2]追加することができる。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% endif %}

#### 最後に表示してからの変更

あなたのチームの他のメンバーからのキャンペーンへの更新数は、キャンペーン概要ページの*Changes Since Last Viewed*メトリックによってトラッキング, 追跡される。キャンペーンの名前、スケジュール、タグ、メッセージング、オーディエンス、承認ステータス、またはチームアクセス設定の更新の変更履歴を表示するには、[**Changes Since Last Viewed]**を選択する。各更新について、誰がいつ更新を行ったかを見ることができる。この変更ログを使ってキャンペーンの変更を監査することができる。

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### コンテンツカードのパフォーマンス

**コンテンツカードパフォーマンスパネルは**、メッセージが様々な次元でどの程度のパフォーマンスを示したかを概説する。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コンテンツカード メッセージパフォーマンス分析]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### 電子メールのパフォーマンス

**メールパフォーマンスパネルでは**、メッセージのパフォーマンスを様々な角度から見ることができる。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![メールメッセージのパフォーマンス分析]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### アプリ内メッセージパフォーマンス

**アプリ内メッセージパフォーマンスパネルは**、メッセージが様々な次元でどの程度のパフォーマンスを示したかを概説する。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![アプリ内メッセージパフォーマンス分析]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### プッシュ通知のパフォーマンス

**プッシュ・パフォーマンス・**パネルでは、メッセージがさまざまな次元でどの程度うまくいったかを概説する。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![プッシュ・メッセージのパフォーマンス分析]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMSパフォーマンス

**SMSパフォーマンス・**パネルでは、様々な側面からメッセージのパフォーマンスを概説する。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![]({% image_buster /assets/img_archive/sms_message_performance.png %}) コントロールグループ、バリアント1、バリアント2のメトリクスの表を含むSMS/MMSパフォーマンスパネル。

{% elsif include.channel == "webhook" %}
### Webhook のパフォーマンス

**Webhook パフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度うまくいったかを概説する。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループとバリアント1のメトリクスの表を含むWebhookパフォーマンスパネル。]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp のパフォーマンス

**WhatsApp パフォーマンス**パネルでは、様々な角度からメッセージのパフォーマンスを見ることができる。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![バリアント1のメトリクスの表を含むWhatsAppパフォーマンスパネル]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

表示をシンプルにしたい場合は、<i class="fas fa-plus"></i> **Add/Remove Columnsを**クリックし、必要なメトリクスをクリアする。デフォルトでは、すべての指標が表示されます。

{% if include.channel == "email" %}

#### ヒートマップ

ヒートマップを使えば、1つのメールキャンペーンで異なるリンクがどれだけ成功したかを見ることができる。**メッセージ分析**セクションから、**メールパフォーマンスパネルに**移動する。メールキャンペーンのプレビューとヒートマップを表示するには、**プレビューとヒートマップを**クリックする。または、バリアント名のハイパーリンクをクリックしてヒートマップを表示することもできる。

このビューでは、**ヒートマップを表示する**トグルを使って、キャンペーン期間中のクリックの全体的な頻度と場所を示すメールのビジュアルビューを表示することができる。**合計クリック数によるリンクテーブル**]パネルでは、メールキャンペーン内のすべてのリンクを表示し、合計クリック数で並べ替えることができる。これにより、ユーザーがどこをナビゲートしているのかについてのインサイトが得られる。参照用にヒートマップのコピーを保存するには、ダウンロード・ボタンをクリックする。

![メールキャンペーンを含むプレビューとヒートマップページの例と、リンクエイリアスの例とその総クリック数のパネル。]({% image_buster /assets/img_archive/email_heatmap_example.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### コンテンツカードの指標

以下は、メッセージのパフォーマンスを確認する際に目にする可能性のある主な指標の内訳である。すべてのコンテンツカードメトリクスの完全な定義については、[レポートメトリクス用語集を][1]参照し、コンテンツカードでフィルターをかける。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#messages-sent">送信済みメッセージ</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='送信されたメッセージ' %}<br><br>
                この計算方法は、選択した項目によって異なる。 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">カードを作成する</a>：<br><br>
                <ul>
                    <li><b>ローンチ時またはステップエントリ時：</b>作成され、見ることができるカードの数。ユーザーがカードを見たかどうかはカウントされない。</li>
                    <li><b>最初のインプレッション発生時:</b>ユーザーに表示されるカードの枚数。</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %} これは同じユーザーに対して複数回インクリメントできる。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">このカウントは</span>、ユーザーがカードを閲覧した2回目以降は増加しない。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユニーク受信者' %}<br><br> 視聴者は毎日ユニークな受信者になる可能性があるため、これは<i>ユニークインプレッションよりも</i>高くなると予想すべきである。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Brazeが提供する配信停止リンクのクリックも含まれる。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-dismissals">ユニーク却下数</a></td>
            <td>{% multi_lang_include metrics.md metric='ユニークな解雇' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
インプレッションの記録方法については、Web、Android、iOSで若干のニュアンスの違いがある。一般的にBrazeは、ユーザーがフィードの特定のコンテンツカードまでスクロールした後、カードが表示されたときにインプレッションを記録する。
{% endalert %}

#### ユニーク受信者とユニーク・インプレッションの比較

メッセージの可視性をカバーする指標はいくつかある。これには、_送信メッセージ_、_ユニーク受信者_、_ユニークインプレッションが_含まれる。特に、_ユニーク受信_者と_ユニーク・インプレッションの_違いは、少し分かりにくいかもしれない。これらの指標をよりよく理解するために、いくつかのシナリオ例を使ってみよう。

例えば、あなたが今日コンテンツカードを閲覧し、明日も同じカードを閲覧し、明後日もまた_同じ_カードを閲覧したとしよう。ただし、_ユニーク・インプレッションは_1回のみカウントされる。また、あなたのデバイスでカードが利用可能だったため、「_送信済みメッセージ_」の数にも含まれる。

別の例として、150,000_メッセージが送信された_コンテンツカードキャンペーンで、5つの_ユニークインプレッションが_表示されたとする。つまり、カードは（バックエンドで）15万人のユーザーに利用可能になったが、その送信後に以下のステップをすべて実行したのは、わずか5人のユーザーのデバイスだけだったということだ：

1. セッションを開始した、またはアプリが明示的にコンテンツカードの同期を要求した（またはその両方）。
2. コンテンツカードビューに移動する
3. SDKがインプレッションを記録し、サーバーにログを記録した。

_送信されたメッセージ_」は閲覧可能なコンテンツカードを指し、「_ユニーク受信者_」は実際に閲覧されたコンテンツカードを指す。

{% elsif include.channel == "email" %}

#### メール指標

他のチャネルでは見られない、メール特有の主な指標をいくつか紹介しよう。Brazeで使用されているすべてのメールメトリクスの完全な定義は、[メール分析用語集を]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)参照。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Clicks' %} これはメールの7日間のトラッキングで、<a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_idによって</a>測定される。これには、Brazeが提供する配信停止リンクのクリックも含まれる。この数値は5～10％であるべきだ。10％を超えるものは例外的である！
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">ユニーク開封数</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Opens' %} メールの場合、これは7日間にわたってトラッキング 追跡される。この数字は10～20％の間であるべきだ。20％を超えるものは例外的である！
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">クリック開封率</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='クリック開封率' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">スパム率</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Spam' %} このメトリックが0.08より大きい場合、あなたのメッセージのコピーが営業的すぎるか、メールアドレスの収集方法を再考する（あなたの通信に興味のある人にメッセージングしていることを確認する）必要がある兆候である可能性がある。
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">配信停止数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='配信停止または退会' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">その他の開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='その他の開封' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">推定実質オープン数</a></td>
            <td class="no-split"> {% multi_lang_include metrics.md metric='Estimated Real Opens' %} 詳細は以下のセクションを参照のこと。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">マシン開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='マシン開封' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">バウンス数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='バウンス' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">ハードバウンス</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ハード・バウンス' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">ソフトバウンス</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ソフトバウンス' %}</td>
        </tr>
    </tbody>
</table>

##### 推定実質開封率 {#estimated-real-open-rate}

この統計は、Brazeが独自に作成した分析モデルを使用して、機械開封が存在しないかのようにキャンペーン独自の開封率の推定値を再構築する。メール送信者からいくつかの開封イベントに*Machine Opensという*ラベルを受け取るが（上記参照）、これらのラベルはしばしば実際の開封をラベル付けすることがある。言い換えれば、「*その他の開封*」は（実際のユーザーによる）実際の開封を過小評価している可能性が高い。その代わり、Brazeは各キャンペーンのクリックデータを使って、実際の人間がメッセージを開封した率を推測している。これにより、Apple の MPP を含むさまざまなマシン開封メカニズムが補われます。

_推定開封_率はメール送信開始から36時間後に算出され、その後24時間ごとに再計算される。キャンペーンが再発した場合、見積もりは別の送信が発生してから36時間後に再計算される。

クリック率によって異なるが、通常、統計を取るには10,000通前後の配信メールが必要である。統計量が計算できない場合、その列は"--"と表示される。

###### 制限事項

推定実質開封率はキャンペーンでのみ利用可能で、Currentsではレポートされない。この指標は、2023年11月14日以前に開始されたアクティブキャンペーンにのみ遡及して算出される。

{% elsif include.channel == "in-app message" %}

#### アプリ内メッセージ・メトリクス

以下は、あなたが分析で目にする可能性のある、アプリ内メッセージの主な指標である。Brazeで使用されているすべてのアプリ内メッセージメトリクスの完全な定義については、[レポートメトリクス用語集を][1]参照のこと。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">本文クリック数 (複数回)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ボディ・クリック' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">ボタン 1 のクリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ボタン1のクリック数' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">ボタン 2 のクリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ボタン2クリック' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユニーク・インプレッション' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='総インプレッション数' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">コンバージョン (B、C、D)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='コンバージョン（B、C、D）' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">コンバージョン数合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='総コンバージョン数' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">コンバージョン率</a></td>
            <td>{% multi_lang_include metrics.md metric='コンバージョン率' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### プッシュ指標

以下は、メッセージのパフォーマンスを確認する際に目にする可能性のある主な指標の内訳である。すべてのプッシュ・メトリクスの完全な定義については、[レポート・メトリクス用語集を][1]参照し、プッシュでフィルターをかける。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>説明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">バウンス数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %} <a href="#bounced-push">バウンスしたプッシュ通知を</a>参照。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">直接開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ダイレクト開封' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='開封' %}</td>
        </tr>
    </tbody>
</table>

プッシュ配信停止はキャンペーン分析の指標には含まれない。この指標を手動で追跡するステップについては、[プッシュ配信停止の追跡を]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)参照のこと。

{% alert tip %}
_Direct Opensと_ _Influenced Opensには_「開封」という言葉が含まれているが、実際には異なる指標である。_ダイレクト開封とは_、上の表にあるように、プッシュ通知を直接開封することを指す。_Influenced Opensとは_、プッシュ通知を受け取った後、特定の時間内にプッシュ通知を開かずにアプリを開封することを指す。つまり、_Influenced Opensとは_アプリ開封のことであり、プッシュ通知開封のことではない。
{% endalert %}

> 通知の配信はAPNによる「ベストエフォート」である。アプリにデータを配信することは意図しておらず、ユーザーに新しいデータが利用可能であることを通知することだけを目的としている。重要な違いは、APNへのメッセージ配信に成功した数を表示するのであって、APNからデバイスへの配信に成功した数を表示するとは限らないということだ。

#### バウンスしたプッシュ通知 {#bounced-push}

##### アップルのプッシュ通知サービス

バウンスは、プッシュ通知が、意図したアプリがインストールされていないデバイスに配信しようとしたときにAPNで発生する。APNはまた、デバイスのトークンを恣意的に変更する権利も持っている。ユーザーのプッシュトークンを登録してから送信するまでの間に、ユーザーのプッシュトークンが変更された端末に送信しようとすると、バウンスが発生する。

ユーザーが次回アプリ開封時に端末設定でプッシュを無効にした場合、SDKはプッシュが無効にされたことを検知し、Brazeに通知する。この時点で、プッシュ有効状態を無効に更新する。無効化されたユーザーが新しいセッションを持つ前にプッシュキャンペーンを受信すると、キャンペーンは正常に送信され、配信されたように表示される。このユーザーに対してプッシュがバウンスすることはない。その後のセッションで、ユーザーにプッシュ通知を送ろうとしても、Brazeはすでにフォアグラウンド・トークンがあるかどうかを認識しているため、通知は送られない。

配信前に期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されることもない。

##### Firebaseクラウドメッセージング

Firebase Cloud Messaging (FCM)のバウンスは3つのケースで発生する可能性がある：

| シナリオ | 説明 |
| -- | -- |
| アンインストールされたアプリケーション | メッセージがデバイスに配信されようとして、そのデバイスで意図したアプリがアンインストールされると、メッセージは破棄され、デバイスの登録IDは無効になる。今後、デバイスにメッセージングを試みると、NotRegisteredエラーが返される。 |
| バックアップされたアプリケーション | アプリケーションがバックアップされると、アプリケーションが復元される前に登録IDが無効になる可能性がある。この場合、FCMはアプリケーションの登録IDを保存しなくなり、アプリケーションはメッセージを受信しなくなる。そのため、アプリケーションのバックアップ時に登録IDを保存すべきでは**ない**。 |
| 更新申請 | アプリケーションが更新されると、以前のバージョンの登録IDが使えなくなることがある。そのため、更新されたアプリケーションは、既存の登録IDを置き換える必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

{% elsif include.channel == "SMS" %}

#### SMSメトリックス

以下は、メッセージのパフォーマンスを確認する際に目にする可能性のある主な指標の内訳である。すべてのSMS指標の完全な定義については、[レポート指標用語集を][1]参照し、SMSでフィルターをかける。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">送信済み</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='送信済み' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends-to-carrier">キャリアへの送信数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='キャリアに送る' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">配信失敗数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='配達の失敗' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">配達確認済み</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='確認された配達' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">拒否数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='不合格' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">オプトアウト</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='オプトアウト' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">ヘルプ</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ヘルプ' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">クリック数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='総クリック数' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook メトリクス

以下は、あなたが分析で目にする可能性のある主なWebhookのメトリクスである。Brazeで使用されるすべてのWebhookメトリクスの完全な定義については、[レポートメトリクス用語集を][1]参照。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユニーク受信者' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">送信数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='送信' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">エラー数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='エラー' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp メトリクス

WhatsAppの主な分析指標をいくつか紹介しよう。Brazeで使用されているすべてのWhatsApp指標の完全な定義については、[レポート指標用語集を][1]参照のこと。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">送信数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='送信' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">配信数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='配達' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">既読数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='リード' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">失敗数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='失敗' %}</td>
        </tr>
    </tbody>
</table>

#### エンドツーエンドのブロックとレポート指標

[WhatsApp マネージャーのダッシュボードから](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx)追加メトリクスにアクセスすることも可能だが、利用可能な全てのインサイトにアクセスするには[アクセス権の確認が](https://www.facebook.com/business/help/218116047387456)必要である。 

{% endif %}

### 過去のパフォーマンス

[**過去のパフォーマンス**] パネルでは、[**メッセージのパフォーマンス**] パネルの指標を時系列でグラフ表示できます。パネル上部のフィルターを使用して、グラフに表示される統計やチャネルを変更します。このグラフの時間範囲は、常にページ上部で指定された時間範囲を反映します。 

日ごとの内訳を知りたい場合は、<i class="fas fa-bars"></i> のハンバーガーメニューをクリックし、「**CSVダウンロード**」を選択すると、レポートのCSVエクスポートを受け取ることができる。

![]({% image_buster /assets/img/cc-historical-performance.png %}) 2021年2月から2022年5月までのメールの統計例を示した「過去のパフォーマンス」パネルのグラフ。

{% if include.channel == "in-app message" %}

{% alert note %}
アプリ内メッセージの最新バージョン(Generation 3)を見ることができるユーザーにのみ送信するように選択した場合、**ターゲットオーディエンスは**あなたの選択を反映するように調整されない。
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### キーワード応答

**キーワードレスポンスパネルには**、あなたのメッセージを受け取った後にユーザーが返信したインバウンドキーワードのタイムラインが表示される。  

![キャンペーンレベルのSMS/MMSキーワードレスポンスパネルには、経時的なキーワード分布の折れ線グラフと、オプトイン、オプトアウト、ヘルプ、その他、その他、コーチングのチェックボックスが選択されたキーワードカテゴリーセクションが含まれている。]({% image_buster /assets/img/sms/keyword_responses.png %}).

ここでは、[リターゲティング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns)するための次のステップを決定し、便利に[セグメンテーションを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)するために、各キーワードカテゴリのレスポンシブ分布を表示することもできる。

![折れ線グラフの下の表には、キーワードカテゴリ、レスポンス分布、リターゲティングのカラムがあり、キーワードカテゴリでセグメンテーションを作成するオプションが与えられている。]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### コンバージョンイベントの詳細

[**コンバージョンイベントの詳細**] パネルには、キャンペーンのコンバージョンイベントのパフォーマンスが表示されます。詳しくは[コンバージョンイベントを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results)参照のこと。

![コンバージョンイベント詳細パネル]({% image_buster /assets/img/cc-conversion.png %})

### コンバージョンの相関

[**コンバージョンの相関**] パネルでは、どのようなユーザー属性と行動が、キャンペーンに設定した結果に役立つか、または悪影響を与えるかを把握できます。詳細については、「[コンバージョンの相関]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/)」を参照してください。

![1次コンバージョンイベントからユーザー属性と行動を分析したコンバージョン相関パネル - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### メタ分析

Brazeの分析に加え、WhatsAppビジネスマネージャーではテンプレートレベルの分析にもアクセスできる。詳しくは[メタのドキュメントを](https://www.facebook.com/business/help/218116047387456)参照されたい。 

{% endif %}

{% if include.channel == "SMS" %}

### SMSカレントのイベント

メールと同様に、BrazeはSMSメッセージがユーザーに届く過程で、メッセージに関連するユーザーレベルのイベントを受信する。受信SMSイベントはすべて、[SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events)イベントを通してカレントイベントとしても送信される。これにより、ユーザーがBrazeプラットフォーム外でテキスト入力したメッセージに対して、追加のアクションやレポートを実行することができる。 

{% alert note %}
インバウンドメッセージは1,600文字を超えると切り捨てられる。
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## リテンションレポート

リテンションレポートは、特定のキャンペーンまたはキャンバスにおいて、ユーザーが選択したリテンションイベントを実行した割合を表示する。詳しくは[リテンションレポートを]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/)参照のこと。

## 目標到達プロセスレポート

ファネルレポートは、キャンペーンやキャンバスを受け取った後の顧客のジャーニーを分析できるビジュアルレポートを提供する。キャンペーンやキャンバスでコントロールグループや複数のバリアントを使用している場合、異なるバリアントがコンバージョンファネルにどのような影響を与えたかをより細かいレベルで理解し、このデータに基づいて最適化することができる。

詳細は[ファンネルレポートを]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/)参照のこと。

{% endif %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[2]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants
