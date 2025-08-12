## 分析を表示する

キャンペーンを開始したら、そのキャンペーンの詳細ページに戻って主要な指標を見ることができる。[**キャンペーン**] ページに移動し、キャンペーンを選択して詳細ページを開く。{% if include.channel != "banner" %}キャンバス内で送信された{% if include.channel == "Content Card" %}コンテンツカード{% elsif include.channel == "banner" %}バナー{% elsif include.channel == "email" %}メール{% elsif include.channel == "in-app message" %}アプリ内メッセージ{% elsif include.channel == "push" %}プッシュメッセージ{% elsif include.channel == "SMS" %} SMS メッセージ{% elsif include.channel == "whatsapp" %} WhatsApp メッセージ{% elsif include.channel == "webhook" %} Webhook {% endif %}については、[キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)を参照してください。{% endif %}

{% alert tip %}
レポートに記載されている用語や指標の定義をお探しですか？以下を参照してください。
  {% if include.channel == "email" %}[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "banner" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)とバナーによるフィルタリング。
  {% elsif include.channel == "Content Card" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)とコンテンツカードによるフィルタリング。
  {% elsif include.channel == "in-app message" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)とアプリ内メッセージによるフィルタリング。
  {% elsif include.channel == "push" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)とプッシュによるフィルタリング。
  {% elsif include.channel == "SMS" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)と SMS / MMS および RCS によるフィルタリング。
  {% elsif include.channel == "whatsapp" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)と WhatsApp によるフィルタリング。
  {% elsif include.channel == "webhook" %}[レポート指標用語集]({{site.baseurl}}/user_guide/data/report_metrics/)と Webhook によるフィルタリング。{% endif %}
{% endalert %}

**キャンペーン分析**タブから、一連のパネルでレポートを見ることができる。以下のセクションに列挙されているものよりも多く見たり少なく見たりするかもしれないが、それぞれに有用な目的がある。

### キャンペーンの詳細

**キャンペーンの詳細**パネルには、キャンペーン全体のパフォーマンスのハイレベルな概要が表示される。
  {% if include.channel == "banner" %}バナー。
  {% elsif include.channel == "Content Card" %}コンテンツカード
  {% elsif include.channel == "email" %}メール。
  {% elsif include.channel == "in-app message" %}アプリ内メッセージ.
  {% elsif include.channel == "push" %}プッシュメッセージ
  {% elsif include.channel == "SMS" %}SMS、MMS、RCS。
  {% elsif include.channel == "whatsapp" %}WhatApp メッセージ。
  {% elsif include.channel == "webhook" %}Webhook。
  {% endif %}

このパネルでは、受信者に送信されたメッセージの数、1 次コンバージョン率、このメッセージによって生み出された総収益などの全体的な指標を確認します。このページから、配信、オーディエンス、コンバージョン設定を確認することもできます。

{% if include.channel == "whatsapp" %}
{% alert note %}
WhatsAppチャネルにはリードレートが含まれる。この指標は、既読通知がオンになっているユーザーにのみ配信されますが、これは異なる場合があります。
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_iam.png %})

キャンバスでは、作成したキャンバスにアプリ内メッセージのパフォーマンスがマッピングされます。ページ上部にあるコントロールパネルを使って、他のメッセージングタイプ（チャネル）を消去し、キャンバス内のアプリ内メッセージのみを表示することができる。

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![キャンペーンのパフォーマンスを決定するために使用されるメトリクスの概要が記載されたキャンペーン詳細パネル。]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### コントロールグループ {#cc-control-group}

個々のコンテンツカードの影響を測定するには、AB テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% elsif include.channel == "SMS" %}

#### コントロールグループ {#sms-control-group}

個々のSMS、MMS、または RCS メッセージの効果を測定するには、AB テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% elsif include.channel == "whatsapp" %}

#### コントロールグループ {#whatsapp-control-group}

個々のWhatsAppメッセージのインパクトを測定するには、A/Bテストに[コントロールグループを]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)追加する。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% elsif include.channel == "webhook" %}

#### コントロールグループ {#webhook-control-group}

個々の Webhook メッセージの影響を測定するには、AB テストに[コントロールグループ]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)を追加できます。トップレベルの**キャンペーン詳細**パネルには、コントロールグループのバリアントのメトリクスが含まれない。

{% endif %}

#### 最後に表示してからの変更

あなたのチームの他のメンバーからのキャンペーンへの更新数は、キャンペーン概要ページの*Changes Since Last Viewed*メトリックによってトラッキング, 追跡される。キャンペーンの名前、スケジュール、タグ、メッセージング、オーディエンス、承認ステータス、またはチームアクセス設定の更新の変更履歴を表示するには、[**Changes Since Last Viewed]**を選択する。各更新について、誰がいつ更新を行ったかを見ることができます。この変更ログを使ってキャンペーンの変更を監査することができる。

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
### SMS/MMS/RCSのパフォーマンス

[**SMS/MMS/RCS のパフォーマンス**] パネルでは、さまざまな角度からメッセージのパフォーマンスを確認できます。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループ、バリアント1、バリアント2の指標の表を含む [SMS/MMS/RCS パフォーマンス] パネル。]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### バナーのパフォーマンス

[**バナーのパフォーマンス]** パネルでは、さまざまな角度からメッセージのパフォーマンスを確認できます。これらの指標は、メッセージングチャネルや多変量テストを実施しているかどうかによって異なります。

![コントロールグループ、バリアント1、バリアント2の指標の表を含む SMS/MMS パフォーマンスパネル。]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "webhook" %}
### Webhook のパフォーマンス

**Webhook パフォーマンス**パネルでは、メッセージがさまざまな側面でどの程度うまくいったかを概説する。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![コントロールグループとバリアント1のメトリクスの表を含むWebhookパフォーマンスパネル。]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp のパフォーマンス

**WhatsApp パフォーマンス**パネルでは、様々な角度からメッセージのパフォーマンスを見ることができる。このパネルの指標は、選択したメッセージングチャネルや、多変量テストを実行しているかどうかに応じて異なります。<i class="fa fa-eye preview-icon"></i>[**プレビュー**] アイコンをクリックすると、バリアントやチャネルごとにメッセージを表示できます。

![バリアント1のメトリクスの表を含むWhatsAppパフォーマンスパネル]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

表示を簡素化する場合は、[<i class="fas fa-plus"></i>**\+ 列を追加/削除**] をクリックし、必要に応じて指標をクリアします。デフォルトでは、すべての指標が表示されます。

{% if include.channel == "email" %}

#### ヒートマップ

ヒートマップを使えば、1つのメールキャンペーンで異なるリンクがどれだけ成功したかを見ることができる。[**メッセージ分析**] セクションから、[**メールパフォーマンス**] パネルに移動します。メールキャンペーンのプレビューとヒートマップを表示するには、**プレビューとヒートマップを**選択する。または、バリアント名のハイパーリンクを選択してヒートマップを表示することもできます。

このビューでは、**ヒートマップ表示**トグルを使用して、キャンペーンの存続期間中のクリックの全体的な頻度と場所を示すメールの視覚的なビューを表示できます。**合計クリック数によるリンクテーブル**]パネルでは、メールキャンペーン内のすべてのリンクを表示し、合計クリック数で並べ替えることができる。これにより、ユーザーが移動する場所に関する詳細な情報が得られます。参照用にヒートマップのコピーを保存するには、ダウンロード・ボタンを選択する。

![メールキャンペーンを含むプレビューとヒートマップページの例と、リンクエイリアスの例とその総クリック数のパネル。]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### 画像

ヒートマップのプレビューやエクスポートで画像が壊れるのを防ぐために、画像URLのCORSをイネーブルメントにすることをお勧めする。

{% endif %}

{% if include.channel == "Content Card" %}

#### コンテンツカードの指標

以下は、メッセージのパフォーマンスを確認する際に目にする可能性のある主な指標の内訳である。すべてのコンテンツカード指標の完全な定義については、[レポート指標の用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照し、コンテンツカードでフィルタリングを行います。

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
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">送信済みメッセージ</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Messages Sent' %}<br><br>
                この計算方法は、選択した項目によって異なる。 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">カード作成</a>：<br><br>
                <ul>
                    <li><b>開始時またはステップエントリ時：</b>作成され、見ることができるカードの数。ユーザーがカードを見たかどうかはカウントされない。</li>
                    <li><b>最初のインプレッション発生時:</b>ユーザーに表示されるカードの枚数。</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %} これは同じユーザーに対して複数回インクリメントできる。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">このカウント</span>は、ユーザーがコンテンツカードを表示した2回目以降は増加しません。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}<br><br> コンテンツカードは1枚につき1回しか受け取れないため、同じコンテンツカードを2回目以降に表示しても、日にちに関係なくカウントは増加しません。閲覧者は毎日のユニーク受信者となる可能性があるため、<i>ユニークインプレッション数</i>よりもこの数値の方が高くなると予想されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Brazeが提供する配信停止リンクのクリックも含まれる。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">ユニーク却下数</a></td>
            <td>{% multi_lang_include metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
インプレッションの記録方法については、Web、Android、iOSで若干のニュアンスの違いがある。一般的にBrazeは、ユーザーがフィードの特定のコンテンツカードまでスクロールした後、カードが表示されたときにインプレッションを記録する。
{% endalert %}

#### ユニーク受信者数とユニークインプレッション数

メッセージの可視性をカバーする指標はいくつかある。これには、_送信メッセー数_、_ユニーク受信者数_、_ユニークインプレッション数_が含まれます。特に、_ユニーク受信者数_と_ユニークインプレッション数_の違いは、少し分かりにくいかもしれません。これらの指標をよりよく理解するために、いくつかのシナリオ例を使ってみよう。

例えば、今日コンテンツカードを表示し、明日、明後日も同じキャンペーンから新しいカードを受け取ると、_ユニーク受信者_として3回カウントされることになります。ただし、_ユニークインプレッション_は1回のみカウントされます。また、そのカードがお使いのデバイスで使用可能であったため、_送信済みメッセージ_の数にもカウントされます。

別の例として、15万件の_メッセージが送信された_ことを示すコンテンツカードキャンペーンに5つの_ユニークインプレッション_があるとします。つまり、カードは (バックエンドで) 15万人のユーザーに利用可能になったが、その送信後に以下のステップをすべて実行したのは、わずか5人のユーザーのデバイスだけだったということです。

1. セッションを開始した、またはアプリが明示的にコンテンツカードの同期を要求した（またはその両方）。
2. コンテンツカードビューに移動する
3. SDK がインプレッションを記録し、サーバーにログを記録しました

_送信済みメッセージ_」は閲覧可能なコンテンツカードを指し、「_ユニーク受信者_」は実際に閲覧されたコンテンツカードを指します。

{% elsif include.channel == "banner" %}

### バナー指標

これらは、バナーキャンペーンのパフォーマンスを確認する際に追跡すべき重要な指標です。バナーのクリック数とインプレッション数は SDK で自動的に追跡されます。 

すべてのバナー指標の完全な定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照し、バナーでフィルタリングしてください。

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
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">各ユーザーは1回のみカウントされます。</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">クリック数の合計</a></td>
            <td class="no-split"><i>Total Clicksは</i>、同じユーザーが複数回クリックしたかどうかにかかわらず、配信されたメッセージ内でクリックしたユーザーの総数（および割合）である。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">ユニーククリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">1 次コンバージョン数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">ユニーク受信者数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}<br><br> 閲覧者は毎日のユニーク受信者となる可能性があるため、<i>ユニークインプレッション数</i>よりもこの数値の方が高くなると予想されます。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">収益</a></td>
            <td>{% multi_lang_include metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">信頼度</a></td>
            <td>{% multi_lang_include metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### ユニーク受信者数とユニークインプレッション数

メッセージの可視性をカバーする指標はいくつかある。これには、_送信メッセー数_、_ユニーク受信者数_、_ユニークインプレッション数_が含まれます。特に、_ユニーク受信者数_と_ユニークインプレッション数_の違いは、少し分かりにくいかもしれません。これらの指標をよりよく理解するために、いくつかのシナリオ例を使ってみましょう。

例えば、今日バナーを表示し、明日、明後日も同じバナーを表示すると、_ユニーク受信者_として3回カウントされることになります。ただし、_ユニークインプレッション_は1回のみカウントされます。また、そのカードがお使いのデバイスで使用可能であったため、_送信済みメッセージ_の数にもカウントされます。

別の例として、150,000件の_メッセージが送信された_ことを示すバナーキャンペーンに5つの_ユニークインプレッション_があるとします。つまり、バナーは (バックエンドで) 150,000人のユーザーに利用可能になったが、その送信後に以下のステップをすべて実行したのは、わずか5人のユーザーのデバイスだけだったということです。

1. セッションを開始した、またはアプリが明示的にバナーの同期を要求した（またはその両方）
2. バナービューに移動した
3. SDK がインプレッションを記録し、サーバーにログを記録しました

[_送信済みメッセージ_] は表示可能なバナーを指し、[_ユニーク受信者_] は実際に表示されたバナーを指します。

{% elsif include.channel == "email" %}

#### メール指標

他のチャネルでは見られない、メール特有の主な指標をいくつか紹介しよう。Braze で使用されているすべてのメール指標の完全な定義については、「[メール分析用語集]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)」を参照してください。

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
                {% multi_lang_include metrics.md metric='Unique Clicks' %} これは、メールの場合、7日間にわたって追跡され、<a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'> dispatch_id</a> によって測定されます。これには、Brazeが提供する配信停止リンクのクリックも含まれる。この数値は5から10% の範囲内でなければなりません。10%を超えるものは例外です。
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Unique Opens</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Opens' %}メールの場合、これは 7 日間にわたって追跡されます。この数値は30から40% の範囲内でなければなりません。40%を超えるものは例外です。
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">クリック開封率</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">スパム率</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Spam' %} この指標が0.08を超える場合は、メッセージのコピーがセールス的すぎるか、メールアドレスの収集方法を再検討する必要があることを示している可能性があります (関心のある人にメッセージを送信していることを確認するため) 。
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">配信停止数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">その他の開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">推定実質開封数</a></td>
            <td class="no-split"> {% multi_lang_include metrics.md metric='Estimated Real Opens' %} 詳細は以下のセクションを参照のこと。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">マシン開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">バウンス数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">ハードバウンス</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">ソフトバウンス</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">延期</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### 延期

「Deferred」または「deferral」とは、メールがすぐに配信されなかったが、Braze がこの一時的な配信エラーの後、その特定のキャンペーンの試行が停止される前に配信成功の可能性を最大化するために、最大72時間メールを再試行することです。「deferrals (延期)」の一般的な理由には、受信トレイプロバイダーからのレピュテーションに基づくメールボリュームのレート制限、一時的な接続の問題、DNS エラーなどがあります。

_延期は_ _ソフトバウンスとは_異なる。この再試行期間中にメールが正常に配信されなかった場合、Brazeは送信されたキャンペーンごとに1つのソフトバウンスイベントを送信する。2025年2月25日以前は、これらの再試行は1回のキャンペーン送信に対して複数のソフトバウンスとしてカウントされていた。

_延期は_現在、CurrentsまたはBraze Snowflake機能（Query Builder、SQLセグメンテーション、Snowflakeデータ共有など）を使用した場合のみ利用可能であることに注意。キャンペーンやキャンバスの分析にこれを含めたい場合は、[製品フィードバックを送信して]({{site.baseurl}}/user_guide/administrative/access_braze/portal)ください。

##### 推定実質開封率 {#estimated-real-open-rate}

この統計は、Brazeが独自に作成した分析モデルを使用して、機械開封が存在しないかのようにキャンペーン独自の開封率の推定値を再構築する。メール送信者からいくつかの開封イベントに *Machine Opens* というラベルを受け取りますが (上記参照)、これらのラベルは、実際の開封を本物の開封としてラベル付けすることができます。言い換えれば、「*その他の開封*」は（実際のユーザーによる）実際の開封を過小評価している可能性が高い。その代わり、Brazeは各キャンペーンのクリックデータを使って、実際の人間がメッセージを開封した率を推測している。これにより、Apple の MPP を含むさまざまなマシン開封メカニズムが補われます。

_推定実質開封率_はメール送信開始から36時間後に算出され、その後24時間ごとに再計算されます。キャンペーンが繰り返される場合、推定は別の送信が発生してから36時間後に再計算されます。

通常、統計を正常に計算するには、配信済みのメールが10,000通程度必要ですが、この数はクリック率によって異なります。統計量が計算できない場合、その列は"--"と表示される。

###### 制限事項

推定実質開封率はキャンペーンでのみ利用可能で、Currents のイベントではレポートされません。この指標は、2023年11月14日以前に開始されたアクティブキャンペーンにのみ遡及して算出される。

{% elsif include.channel == "in-app message" %}

#### アプリ内メッセージ指標

分析に表示される主なアプリ内メッセージの指標を一部ご紹介します。Braze で使用されているすべてのアプリ内メッセージ指標の完全な定義については、[レポート指標の用語]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照してください。

{% alert note %}
_ボタン1のクリック数_と_ボタン2のクリック数_のレポートは、アプリ内メッセージで [**レポート用の識別子**] をそれぞれ「0」と「1」に指定した場合にのみ機能します。

![値が「0」の [レポート用の識別子] フィールド。]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">ボタン 1 のクリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">ボタン 2 のクリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">コンバージョン (B、C、D)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">コンバージョン数合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">コンバージョン率</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">メッセージを閉じる</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### プッシュ指標

以下は、メッセージのパフォーマンスを確認する際に目にする可能性のある主な指標の内訳である。すべてのプッシュ・メトリクスの完全な定義については、[レポート・メトリクス用語集を]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)参照し、プッシュでフィルターをかける。

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %} <a href="#bounced-push">バウンスされたプッシュ通知数</a>を参照してください。</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">直接開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">開封数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> 通知の配信は、Appleプッシュ通知サービス（APN）による「ベストエフォート」である。アプリにデータを配信することは意図しておらず、ユーザーに新しいデータが利用可能であることを通知することだけを目的としている。重要な違いは、デバイスに正常に配信された APNs の数ではなく、APNs に正常に配信されたメッセージの数が表示されることです。

##### 配信停止のトラッキング

プッシュの配信停止は、キャンペーン分析の指標として含まれません。この指標を手動で追跡するステップについては、[プッシュ配信停止の追跡]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)を参照してください。

##### 開封を把握する

_直接開封数_と_誘発された開封数_には「開封」という言葉が含まれていますが、実際には異なる指標です。_ダイレクト開封とは_、上の表にあるように、プッシュ通知を直接開封することを指す。_誘発された開封数_とは、プッシュ通知を受け取った後、特定の時間内にプッシュ通知を開かずにアプリを開封することを指します。つまり、_Influenced Opensとは_アプリ開封のことであり、プッシュ通知開封のことではない。

##### プッシュ通知の送信数がユニーク受信者数を超える可能性がある理由

以下の理由により、_送信_数が_ユニーク受信者_数を上回る場合があります。

- **再適格性がオンになっています:**キャンペーンまたはキャンバスの設定で再適格性が有効になっている場合、セグメントと配信条件を満たすユーザーは、同じプッシュ通知を複数回受け取ることができます。その結果、総送信数が多くなります。
- **ユーザーは複数のデバイスを持っている：**再適格性が有効になっていない場合は、ユーザーが複数のデバイスをプロフィールに関連付けていることで、その違いが説明されることがあります。例えば、ユーザーがスマートフォンとタブレットの両方を持っていて、プッシュ通知が登録されたすべてのデバイスに送信される。各配信は送信としてカウントされるが、1人のユニークな受信者だけが記録されます。
- **ユーザーは複数のアプリに割り当てられます。**ユーザーが複数のアプリに関連付けられている場合（新しいアプリのテスト時など）、それぞれのアプリで同じプッシュ通知を受け取ることがある。これが送信数の増加につながります。

##### バウンスが起こる理由 {#bounced-push}

{% tabs %}
{% tab Appleプッシュ通知サービス %}

バウンスは、Appleのプッシュ通知サービス（APN）において、プッシュ通知が目的のアプリがインストールされていないデバイスに配信されようとするときに発生する。APNはまた、デバイスのトークンを恣意的に変更する権利も持っている。以前にトークンを登録した時 (ユーザーに対してプッシュトークンを登録する各セッションの開始時など) から送信時刻までの間にプッシュトークンが変更されたユーザーのデバイスに送信しようとすると、バウンスが発生します。

ユーザーが次回アプリ開封時に端末設定でプッシュを無効にした場合、SDKはプッシュが無効にされたことを検知し、Brazeに通知する。この時点で、プッシュ有効状態を無効に更新します。無効化されたユーザーが新しいセッションを持つ前にプッシュキャンペーンを受信すると、キャンペーンは正常に送信され、配信されたように表示される。このユーザーに対してプッシュがバウンスすることはない。その後のセッションで、ユーザーにプッシュを送信しようとすると、Braze はフォアグラウンドトークンがあるかどうかを既に認識しているため、通知は送信されません。

配信前に期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されることもない。

{% endtab %}
{% tab Firebaseクラウドメッセージング %}

Firebase Cloud Messaging (FCM) のバウンスは3つのケースで発生する可能性があります。

| シナリオ | 説明 |
| -- | -- |
| アンインストールされたアプリケーション | メッセージがデバイスに配信されようとして、そのデバイスで意図したアプリがアンインストールされると、メッセージは破棄され、デバイスの登録IDは無効になる。今後デバイスにメッセージを送信しようとすると、NotRegistered エラーが返されます。 |
| バックアップされたアプリケーション | アプリケーションがバックアップされると、アプリケーションが復元される前に登録 ID が無効になる可能性があります。この場合、FCMはアプリケーションの登録IDを保存しなくなり、アプリケーションはメッセージを受信しなくなる。そのため、アプリケーションのバックアップ時に登録 ID を保存すべきでは**ありません**。 |
| 更新されたアプリケーション | アプリケーションが更新されると、以前のバージョンの登録IDが使えなくなることがある。そのため、更新されたアプリケーションは、既存の登録 ID を置き換える必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS、MMS、RCS 指標

以下は、メッセージのパフォーマンスを確認する際に目にする可能性のある主な指標の内訳である。すべてのSMS、MMS、RCS 指標の完全な定義については、[レポート指標用語集を]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)参照し、SMS / MMS および RCS でフィルタリングしてください。

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">配信失敗数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">確認済み配信</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">拒否数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">オプトアウト</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">ヘルプ</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Help' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">クリック数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook メトリクス

以下は、あなたが分析で目にする可能性のある主なWebhookのメトリクスである。Brazeで使用されるすべてのWebhookメトリクスの完全な定義については、[レポートメトリクス用語集を]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)参照。

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">送信数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">エラー数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp メトリクス

WhatsAppの主な分析指標をいくつか紹介しよう。Braze で使用されているすべてのWhatsApp 指標の完全な定義については、[レポート指標の用語]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照してください。

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">配信数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">既読数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">失敗数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### エンドユーザーのブロックとレポートの指標

追加の指標には [WhatsApp マネージャー](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx)ダッシュボードからアクセスできますが、利用可能なすべてのインサイトにアクセスするには、[アクセス権の確認](https://www.facebook.com/business/help/218116047387456)が必要です。 

{% endif %}

### 過去のパフォーマンス

[**過去のパフォーマンス**] パネルでは、[**メッセージのパフォーマンス**] パネルの指標を時系列でグラフ表示できます。パネル上部のフィルターを使用して、グラフに表示される統計やチャネルを変更します。このグラフの時間範囲は、常にページ上部で指定された時間範囲を反映します。 

日ごとの内訳を知りたい場合は、<i class="fas fa-bars"></i> のハンバーガーメニューをクリックし、「**CSVダウンロード**」を選択すると、レポートのCSVエクスポートを受け取ることができる。

![]({% image_buster /assets/img/cc-historical-performance.png %}) 2021年2月から2022年5月までのメールの統計例を示した「過去のパフォーマンス」パネルのグラフ。

{% if include.channel == "in-app message" %}

{% alert note %}
最新バージョンの Braze のアプリ内メッセージ (第3世代) を表示できるユーザーにのみ送信することを選択した場合、**ターゲットオーディエンス**は選択内容を反映するようには調整されません。
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### キーワード応答

**キーワード応答**パネルには、メッセージ受信後にユーザーが返信した受信キーワードのタイムラインが表示されます。  

![キャンペーンレベルの [SMS/MMS/RCS キーワードレスポンス] パネル。経時的なキーワード分布の折れ線グラフと、オプトイン、オプトアウト、ヘルプ、その他、追加、コーチングのチェックボックスが選択されたキーワードカテゴリーセクションが含まれています。]({% image_buster /assets/img/sms/keyword_responses.png %})

ここでは、[リターゲティング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns)するための次のステップを決定し、便利に[セグメンテーションを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)するために、各キーワードカテゴリのレスポンシブ分布を表示することもできる。

![折れ線グラフの下の表には、キーワードカテゴリ、レスポンス分布、リターゲティングのカラムがあり、キーワードカテゴリでセグメンテーションを作成するオプションが与えられている。]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### コンバージョンイベントの詳細

[**コンバージョンイベントの詳細**] パネルには、キャンペーンのコンバージョンイベントのパフォーマンスが表示されます。詳細については、「[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results)」を参照してください。

![コンバージョンイベントの詳細パネル。]({% image_buster /assets/img/cc-conversion.png %})

### コンバージョンの相関

[**コンバージョンの相関**] パネルでは、どのようなユーザー属性と行動が、キャンペーンに設定した結果に役立つか、または悪影響を与えるかを把握できます。詳細については、「[コンバージョンの相関]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/)」を参照してください。

![1次コンバージョンイベントのユーザー属性と行動に関する分析を含むコンバージョン相関パネル - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### メタ分析

Brazeの分析に加え、WhatsAppビジネスマネージャーではテンプレートレベルの分析にもアクセスできる。詳細については、[Meta のドキュメント](https://www.facebook.com/business/help/218116047387456)を参照してください。 

{% endif %}

{% if include.channel == "SMS" %}

### SMS Currents のイベント

メールと同様に、BrazeはSMSメッセージがユーザーに届く過程で、メッセージに関連するユーザーレベルのイベントを受信する。受信SMSイベントはすべて、[SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events)イベントを通して Currents イベントとしても送信される。これにより、ユーザーがBrazeプラットフォーム外でテキスト入力したメッセージに対して、追加のアクションやレポートを実行することができる。 

{% alert note %}
インバウンドメッセージは1,600文字を超えると切り捨てられる。
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## リテンションレポート

リテンションレポートには、特定のキャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}において、指定した期間に選択したリテンションイベントをユーザーが実行した割合が表示されます。詳細については、「[リテンションレポート]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)」を参照してください。

## 目標到達プロセスレポート

目標到達プロセスレポートは、キャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}を受け取った後の顧客のジャーニーを分析できるビジュアルレポートを提供します。キャンペーン{% if include.channel != "banner" %}またはキャンバス{% endif %}でコントロールグループや複数のバリアントを使用している場合、異なるバリアントがコンバージョンの目標到達にどのような影響を与えたかをより細かいレベルで理解し、このデータに基づいて最適化することができます。

詳細については、「[目標到達プロセスレポート]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)」を参照してください。

{% endif %}

