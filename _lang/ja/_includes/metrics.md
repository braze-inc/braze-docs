{% if include.metric == "AMP Clicks" %}
<i>AMP クリック数</i>は、AMP HTML メールにおけるクリック数の合計で、HTML、プレーンテキスト、および AMP HTML バージョンのメールの累計です。
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP 開封数</i>は、AMP HTML メールおよび AMP HTML バージョンのメールの開封総数です。
{% endif %}

{% if include.metric == "Audience" %}
<i>オーディエンス</i>は、特定のメッセージを受け取ったユーザーの割合です。この数値は Braze から提供されます。
{% endif %}

{% if include.metric == "Bounces" %}
<i>バウンス数</i>とは、意図した受信者に届かなかったメッセージの総数です。
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
<i>推定実開封数</i>とは、機械による開封が存在しなかった場合にどれだけのユニーク開封があったかを推定したもので、Braze 独自の統計モデルによる結果です。
{% endif %}

{% if include.metric == "Help" %}
<i>ヘルプ</i>とは、ユーザーがメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">HELP キーワード</a>で返信し、HELP 自動応答が送信された場合を指します。
{% endif %}

{% if include.metric == "Hard Bounce" %}
<i>ハードバウンス</i>とは、永続的な配信エラーによって受信者にメールが届かないことをいいます。ドメイン名が存在しない場合や、受信者が不明な場合にハードバウンスが発生する可能性があります。
{% endif %}

{% if include.metric == "Soft Bounce" %}
<i>ソフトバウンス</i>とは、受信者のメールアドレスが有効であるにもかかわらず、一時的な配信エラーによってメールが受信者に届かないことをいいます。ソフトバウンスが発生する理由として、受信者の受信トレイがいっぱいである、サーバーが停止している、メッセージが受信者の受信トレイには大きすぎる、などがあります。
{% endif %}

{% if include.metric == "Deferral" %}
<i>延期</i>とは、メールがすぐに配信されなかった場合を指しますが、Braze はこの一時的な配信失敗の後、最大72時間にわたってメールの再送信を試行し、特定のキャンペーンの試行が停止される前に配信成功の可能性を最大化します。
{% endif %}

{% if include.metric == "Body Click" %}
Push Stories 通知は、通知がクリックされると<i>ボディクリック</i>を記録します。メッセージが展開されたとき、またはアクションボタンがクリックされたときには記録されません。
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>ボディクリック</i>は、従来のエディターで作成されたボタン（ボタン1、ボタン2）のないメッセージをユーザーがクリックしたとき、また、HTML エディターやドラッグ＆ドロップエディターで作成されたメッセージが引数なしの <code>brazeBridge.logClick()</code> を使用したときに発生します。
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>ボタン1クリック数</i>とは、メッセージのボタン1がクリックされた総数です。
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>ボタン2クリック数</i>とは、メッセージのボタン2がクリックされた総数です。
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>送信された選択肢数</i>とは、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の質問ページでユーザーが送信ボタンをクリックしたときに選択された選択肢の総数です。
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>クリック開封率</i>とは、配信されたメールのうち、1人のユーザーまたはマシンによって少なくとも1回開封されたメールの割合であり、<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>レポートビルダー</a>でのみ利用できます。
{% endif %}

{% if include.metric == "Close Message" %}
<i>メッセージを閉じる</i>とは、メッセージの [閉じる] ボタンがクリックされた合計回数です。これは、従来のエディターではなく、ドラッグ＆ドロップエディターで作成されたアプリ内メッセージにのみ存在します。
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>確認済み配信</i>とは、通信事業者がターゲットの電話番号にメッセージが配信されたことを確認した場合を指します。
{% endif %}

{% if include.metric == "Confidence" %}
<i>信頼度</i>とは、メッセージの特定のバリアントがコントロールグループよりも優れたパフォーマンスを示しているという信頼度の割合です。
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>確認ページボタン</i>とは、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の確認ページにあるコールトゥアクションボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>確認ページ却下数</i>とは、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の確認ページにある [閉じる] (x) ボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>コンバージョン率</i>は、メッセージの全受信者と比較して、定義されたイベントが発生した回数の割合です。このイベントはキャンペーンの作成時に決定します。
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>コンバージョンウィンドウ</i>とは、メッセージを受け取ってからユーザーのアクションがトラッキングされ、コンバージョンイベントに帰属されるまでの日数のことです。この期間の後に発生したコンバージョンは、コンバージョンイベントには帰属されません。
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>コンバージョン (B, C, D)</i> とは、1次コンバージョンイベントの後に追加されるコンバージョンイベントです。Braze キャンペーンから受信したメッセージとのインタラクションまたは閲覧の後に、定義されたイベントが発生した回数を表します。
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>合計コンバージョン数</i>とは、ユーザーがアプリ内メッセージキャンペーンを閲覧した後に特定のコンバージョンイベントを完了した合計回数です。
{% endif %}

{% if include.metric == "Deliveries" %}
<i>配信数</i>とは、受信サーバーが受け入れたメッセージリクエスト数の合計です。これはメッセージがデバイスに届いたことを意味するのではなく、メッセージがサーバーに受け入れられたことのみを意味します。
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>配信率 (%)</i>は、メール送信可能な相手に正常に送信および受信されたメッセージ（送信数）の合計に対する割合です。
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>配信失敗</i>とは、キューのオーバーフローにより SMS を送信できなかった場合です（ロングコードまたはショートコードが処理できるレートを超えて SMS を送信した場合）。
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>配信失敗</i>とは、キューのオーバーフローにより RCS を送信できなかった場合です（RCS 検証済み送信者が処理できるレートを超えて RCS を送信した場合）。
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
<i>配信失敗率</i>は、メッセージを送信できなかったために失敗した送信の割合です。これは、キューのオーバーフロー、アカウントの停止、MMS の場合のメディアエラーなど、さまざまな理由で発生する可能性があります。
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>直接開封数</i>は、通知を直接タップしてアプリや Web サイトを開いたユーザーの総数です。
{% endif %}

{% if include.metric == "Emailable" %}
<i>メール送信可能なユーザー数</i>とは、メールアドレスが登録されており、明示的にオプトインまたは購読中のユーザーの合計数です。
{% endif %}

{% if include.metric == "Errors" %}
<i>エラー数</i>とは、Webhook イベントによって返されたエラーの数です（送信プロセス中にインクリメントされます）。
{% endif %}

{% if include.metric == "Failures" %}
<i>失敗</i>とは、インターネットサービスプロバイダーがハードバウンスを返したために WhatsApp メッセージを送信できなかった場合を指します。ハードバウンスは永続的な配信失敗を意味します。
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>間接開封数</i>とは、プッシュ通知の送信後に、プッシュを直接開封せずにアプリを開いたユーザーの総数（および割合）です。
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>生涯収益</i>とは、開始以降に受け取った <code>PurchaseEvents</code> の価格値の合計（USD）です。
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>ユーザーあたりの生涯価値</i>は、<i>生涯収益</i>を<i>総ユーザー数</i>（ホームページに記載）で割ったものです。
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>日次平均収益</i>は、指定された日のキャンペーンおよびキャンバスの収益合計の平均です。
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>日次購入数</i>は、期間中のユニーク <code>PurchaseEvents</code> 合計の平均です。
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
<i>ユーザーあたりの日次収益</i>は、日次アクティブユーザーあたりの平均日次収益です。
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>機械開封</i>には、iOS 15 の Apple のメールプライバシー保護（MPP）の影響を受ける「開封」の割合が含まれます。例えば、ユーザーが Apple デバイスのメールアプリを使用してメールを開封した場合、これは<i>機械開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Other Opens" %}
<i>その他の開封</i>には、<i>機械開封</i>として識別されなかったメールが含まれます。例えば、ユーザーが別のプラットフォーム（スマートフォンの Gmail アプリ、デスクトップブラウザーの Gmail など）でメールを開封した場合、これは<i>その他の開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Opens" %}
<i>開封</i>とは、<i>直接開封</i>と<i>間接開封</i>の両方を含むインスタンスで、Braze SDK が独自のアルゴリズムを使用して、プッシュ通知によってユーザーがアプリを開封したと判断したものを指します。
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>オプトアウト</i>とは、ユーザーがメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">オプトアウトキーワード</a>で返信し、SMS または RCS プログラムから配信停止された場合を指します。
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>再試行保留中</i>とは、受信サーバーによって一時的に拒否されたが、メールサービスプロバイダー (ESP) によって再配信が試行されたリクエストの数です。メールサービスプロバイダー (ESP) は、タイムアウト期間（通常72時間後）に達するまで配信を再試行します。
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>1次コンバージョン (A)</i> または<i>1次コンバージョンイベント</i>とは、Braze キャンペーンからのメッセージを受信または閲覧した後に定義されたイベントを実行したユニークユーザーの数です。このイベントはキャンペーンの設定時に選択され、レポートと最適化のための主要な成功指標として使用されます。
{% endif %}

{% if include.metric == "Reads" %}
<i>既読</i>とは、ユーザーがメッセージを読んだ場合を指します。Braze が既読を追跡するには、ユーザーの既読レシートが「オン」になっている必要があります。
{% endif %}

{% if include.metric == "Read Rate" %}
<i>既読率</i>とは、送信のうち既読となった割合です。これは、既読レシートをオンにしているユーザーに対してのみ提供されます。
{% endif %}

{% if include.metric == "Received" %}
<i>受信済み</i>はチャネルごとに定義が異なり、ユーザーがメッセージを閲覧したとき、ユーザーが定義されたトリガーアクションを実行したとき、またはメッセージがメッセージプロバイダーに送信されたときのいずれかを指します。
{% endif %}

{% if include.metric == "Rejections" %}
<i>拒否</i>とは、SMS または RCS がキャリアによって拒否された場合を指します。これは、通信事業者のコンテンツフィルタリング、宛先デバイスの利用不可、電話番号の使用停止など、さまざまな理由で発生する可能性があります。
{% endif %}

{% if include.metric == "Revenue" %}
<i>収益</i>とは、設定された<a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>1次コンバージョン期間</a>内のキャンペーン受信者からのドル単位の総収益です。
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>送信済みメッセージ数</i>は、キャンペーンで送信されたメッセージの合計数です。スケジュールされたキャンペーンを開始した後、この指標にはレート制限によりまだ送信されていないものも含め、送信されたすべてのメッセージが含まれます。これはメッセージが受信またはデバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味します。
{% endif %}

{% if include.metric == "Sent" %}
<i>送信済み</i>とは、キャンペーンまたはキャンバスステップが開始またはトリガーされ、Braze から SMS または RCS が送信されたことを指します。エラーにより SMS または RCS がユーザーのデバイスに届かなかった可能性もあります。
{% endif %}

{% if include.metric == "Sends" %}
<i>送信数</i>とは、キャンペーンで送信されたメッセージの総数です。スケジュールされたキャンペーンを開始した後、この指標にはレート制限によりまだ送信されていないものも含め、送信されたすべてのメッセージが含まれます。これはメッセージが受信またはデバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味します。
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>キャリアへの送信数</i>は非推奨ですが、すでに利用しているユーザーについては引き続きサポートされます。これは、<i>確認済み配信数</i>、<i>拒否数</i>、および通信事業者によって配信または拒否が確認されなかった<i>送信数</i>の合計です。一部の通信事業者はこの確認を提供しないか、送信時に提供できないため、通信事業者が配信や拒否の確認を提供しないケースも含まれます。
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>キャリアへの送信率</i>は、送信されたメッセージの合計のうち、<i>キャリアへの送信</i>として分類されたメッセージの割合です。一部の通信事業者は配信確認や拒否確認を提供しないか、送信時に提供できないため、そのようなケースも含まれます。この指標は非推奨ですが、すでに利用しているユーザーについては引き続きサポートされます。
{% endif %}

{% if include.metric == "Spam" %}
<i>スパム</i>は、受信者によって「スパム」とマークされた配信済みメールの総数です。Braze はこれらのユーザーのサブスクリプション状態を変更しませんが、「配信停止を含むすべてのユーザーに送信する」ように設定されたトランザクションメールを送信する場合を除き、これらのユーザーは今後のメールから自動的に除外されます。
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>調査ページ却下数</i>とは、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の質問ページにある [閉じる] (x) ボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>調査送信数</i>とは、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の送信ボタンがクリックされた回数の合計です。
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>合計クリック数</i>は、配信されたメッセージ内のリンクをクリックしたユニーク受信者の数です。
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>合計却下数</i>とは、キャンペーンのコンテンツカードが却下された回数です。
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>合計インプレッション数</i>とは、以前のインタラクションに関係なく、メッセージが読み込まれてユーザーの画面に表示された回数です（例えば、ユーザーにメッセージが2回表示された場合、2回カウントされます）。
{% endif %}

{% if include.metric == "Total Opens" %}
<i>合計開封数</i>とは、開封されたメッセージの総数です。
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>総収益</i>とは、設定された1次コンバージョン期間内のキャンペーン受信者からのドル単位の総収益です。
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>ユニーククリック数</i>とは、メッセージ内のリンクを少なくとも1回クリックした受信者のユニーク数であり、<a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> で測定されます。
{% endif %}

<!-- Pull channels like Banners that don't have a Dispatch ID-->
{% if include.metric == "Unique Clicks No Dispatch ID" %}
<i>ユニーククリック数</i>とは、メッセージ内のリンクを少なくとも1回クリックした受信者のユニーク数です。
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>ユニーク却下数</i>は、キャンペーンのコンテンツカードを却下したユニーク受信者の数です。ユーザーがキャンペーンのコンテンツカードを複数回却下しても、ユニーク却下は1回としてカウントされます。
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>ユニークインプレッション数</i>とは、特定のキャンペーンからメッセージを受信して表示したユーザーの総数です。
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>ユニーク受信者数</i>とは、1日のユニーク受信者数、つまり1日に新しいメッセージを受信したユーザーの数です。このカウントが1人のユーザーに対して複数回インクリメントされるには、そのユーザーが別の日に新しいメッセージを受け取る必要があります。
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>ユニーク開封数</i>とは、配信されたメッセージのうち、1人のユーザーが少なくとも1回開封したメッセージの総数で、7日間にわたってトラッキングされます。
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Unsubscribers</i> または <i>Unsub</i> は、配信停止に至ったメッセージの数です。配信停止は、ユーザーが Braze の配信停止リンクをクリックしたときに発生します。
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>配信停止数</i>とは、Braze が提供する配信停止 URL をクリックした結果、サブスクリプション状態が配信停止に変更された受信者の数です。
{% endif %}

{% if include.metric == "Variation" %}
<i>バリエーション</i>とは、キャンペーンのバリエーションの数で、作成者の定義によって異なります。
{% endif %}