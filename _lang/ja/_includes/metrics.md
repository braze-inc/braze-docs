{% if include.metric == "AMP Clicks" %}
<i>AMP クリック数</i>は、AMP HTML メールのクリック数の合計、HTML、プレーンテキスト、および AMP HTML バージョンのメールの総計です。
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP 開封数</i>は AMP HTML メールおよび AMP HTML バージョンのメールの開封総数です。
{% endif %}

{% if include.metric == "Audience" %}
<i>オーディエンスは</i>、特定のメッセージを受け取ったユーザーの割合である。この数値は Braze から受信します。
{% endif %}

{% if include.metric == "Bounces" %}
<i>バウンス数</i>とは、意図した受信者に届かなかったメッセージの総数です。
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
<i>推定実開封数とは</i>、もし機械による開封が存在しなかったとしたら、どれだけのユニークな開封が存在するかを推定したもので、Braze独自の統計モデルの結果である。
{% endif %}

{% if include.metric == "Help" %}
<i>ヘルプとは</i>、ユーザーがあなたのメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">HELPキーワードで</a>返信し、HELP自動レスポンスが送信された場合である。
{% endif %}

{% if include.metric == "Hard Bounce" %}
<i>ハードバウンスとは</i>、永久的な配信エラーによって受信者にメールが届かないことをいう。ドメイン名が存在しないか、受信者が不明なため、ハードバウンスが発生する可能性があります。
{% endif %}

{% if include.metric == "Soft Bounce" %}
<i>ソフトバウンスとは</i>、受信者のメールアドレスが有効であるにもかかわらず、一時的な配信エラーによってメールが受信者に届かないことをいう。ソフトバウンスが発生する理由として、受信者の受信トレイがいっぱいである、サーバーが停止している、メッセージが受信者の受信トレイには大きすぎる、などがあります。
{% endif %}

{% if include.metric == "Deferral" %}
<i>延期とは</i>、メールがすぐに配信されなかった場合であるが、Brazeは、この一時的な配信失敗の後、最大72時間までメールを再試行し、特定のキャンペーンの試行が停止される前に、配信成功の可能性を最大化する。
{% endif %}

{% if include.metric == "Body Click" %}
プッシュストーリー通知は、通知がクリックされると<i>ボディクリックを</i>記録する。メッセージが展開されたとき、またはアクションボタンがクリックされたときには記録されません。
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>ボディ・クリックは</i>、従来のエディターで作成されたボタン（ボタン1、ボタン2）のないメッセージをユーザーがクリックしたとき、また、HTMLエディターやドラッグ＆ドロップ・エディターで作成されたメッセージが引数のない <code>brazeBridge.logClick()</code>  を使用したときに発生します。
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>ボタン1クリック数</i>とはメッセージのボタン1をクリックした総数です。
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>ボタン2クリック数</i>とはメッセージのボタン2をクリックした総数です。
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>送信された選択肢数</i>とは<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の質問ページでユーザーが送信ボタンをクリックしたときに選択される選択肢の総数です。
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>クリック開封率とは</i>、配信されたメールのうち、ユーザーまたはマシンが一度でも開封したメールの割合であり、<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>レポートビルダーでのみ</a>利用できる。
{% endif %}

{% if include.metric == "Close Message" %}
<i>メッセージを閉じる</i>とはメッセージの [閉じる] ボタンをクリックした合計回数です。これは、従来のエディターではなく、ドラッグ＆ドロップエディターで作成されたアプリ内メッセージにのみ存在します。
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>確認配信とは</i>、通信事業者が、ターゲットの電話番号にメッセージが配信されたことを確認した場合のことを言います。
{% endif %}

{% if include.metric == "Confidence" %}
<i>信頼度</i>とはメッセージの特定のバリアントのパフォーマンスがコントロールグループよりも優れているという信頼度の割合です。
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>確認ページボタン</i>とは<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の確認ページにあるコールトゥアクションボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>確認ページ却下数</i>とは<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の確認ページにある [閉じる] (x) ボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>コンバージョン率は</i>、メッセージの全受信者と比較して、定義されたイベントが発生した回数の割合である。キャンペーンを作成するときに、このイベントを決定します。
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>コンバージョンウィンドウとは</i>、メッセージを受け取ってから、ユーザーのアクションがトラッキングされ、コンバージョンイベントに属性されるまでの日数のことである。この期間の後に発生したコンバージョンは、コンバージョンイベントに起因するものとは見なされません。
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>コンバージョン (B, C, D)</i> とは1次コンバージョンイベントの後に追加されるコンバージョンイベントです。これは、Brazeキャンペーンから受信したメッセージと対話または閲覧した後に、定義されたイベントが発生した回数である。
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>合計コンバージョン数</i>とは、ユーザーがアプリ内メッセージキャンペーンを閲覧した後、特定のコンバージョンイベントを完了した合計回数です。
{% endif %}

{% if include.metric == "Deliveries" %}
<i>配信数</i>とは受信サーバーが受け入れたメッセージリクエスト数の合計です。これは、メッセージがデバイスに届いたことを意味するのではなく、メッセージがサーバーに受け入れられたことを意味する。
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>配信数%</i>は、メール可能な相手に正常に送受信されたメール (送信) のの合計数に対する割合です。
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>配信の失敗とは</i>、キューがオーバーフローしたためにSMSを送信できなかった場合である（ロングコードまたはショートコードが処理できる以上のレートでSMSを送信した）。
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>配信失敗</i>とは、キューがオーバーフローしたために RCS を送信できなかった (RCS を検証済みの送信者が処理できる以上の速度で RCS を送信した) 場合です。
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
<i>配信失敗率</i>は、メッセージが送信できなかったために失敗した送信の割合です。これは、キューのオーバーフロー、アカウントの停止、MMSの場合のメディアエラーなど、さまざまな理由で起こりうる。
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>直接開封数</i>は、通知を直接押してアプリや Web サイトを開いたユーザーの総数です。
{% endif %}

{% if include.metric == "Emailable" %}
<i>メール可能なユーザー数</i>とは、レコードにメールアドレスがあり、明示的にオプトインまたは登録を行ったユーザーの合計数です。
{% endif %}

{% if include.metric == "Errors" %}
<i>エラー数</i>とは、Webhook イベントによって返されたエラーの数 (送信プロセス中に増加)。
{% endif %}

{% if include.metric == "Failures" %}
<i>失敗</i>とは、インターネットサービスプロバイダーがハードバウンスを返したため、WhatsApp メッセージを送信できなかった場合のことをいいます。ハードバウンスとは、永続的な配信の失敗です。
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>誘発された開封数</i>とはプッシュ通知の送信後に、プッシュを直接開封せずにアプリを開いたユーザーの総数 (および割合) です。
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>生涯収益</i>とは開始以降に受け取った <code>PurchaseEvents</code>  価格の合計 (USD) です。
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>Lifetime Value Per Userは</i>、<i>生涯収益を</i> <i>総ユーザー数で</i>割ったものである（ホームページに記載）。
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>Average Daily revenue</i> は、指定された日のキャンペーンとキャンバスの収益の合計の平均です。
{% endif %}

{% if include.metric == "Daily Purchases" %}
[<i>日割り購入数</i>] は、期間中のユニークの合計 <code>PurchaseEvents</code>  を平均した数です。
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
[<i>ユーザーあたりの日割り収益</i>] は、日次収益を日次アクティブユーザー数で除算した商の平均です。
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>機械開封</i>」には、iOS 15 の Apple のメール・プライバシー保護（MPP）の影響を受ける「開封」の割合が含まれる。例えば、ユーザーが Apple デバイスのメールアプリを使用してメールを開封した場合、これは<i>マシン開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Other Opens" %}
<i>その他の開封</i>には、<i>マシン開封</i>として識別されないメールが含まれます。例えば、ユーザーが別のプラットフォーム (携帯電話の Gmail アプリ、デスクトップブラウザーの Gmail など) でメールを開封すると、これは<i>その他の開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Opens" %}
<i>開封</i>とは、<i>直接開封</i>と<i>誘発された開封</i>の両方を含むインスタンスで、Braze SDK が独自のアルゴリズムを用いて、プッシュ通知によってユーザーがアプリを開封したと判断したものを指します。
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>オプトアウト</i>とは、ユーザーがあなたのメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">オプトアウトキーワード</a>で返信し、あなたの SMS または RCS プログラムから購読解除された時のことをいいます。
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>再試行保留中数</i>とは受信サーバーによって一時的に拒否されたが、メールサービスプロバイダー (ESP) によって再配信が試行されたリクエストの数です。メールサービスプロバイダー (ESP) は、タイムアウト期間に達する (通常は 72 時間後) まで配信を再試行します。
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>1次コンバージョン（A）</i>または<i>1次コンバージョンイベントとは</i>、Brazeキャンペーンからのメッセージを受信または閲覧した後、定義されたイベントを実行したユニークユーザーの数である。このイベントはキャンペーンの設定時に選択され、レポートと最適化のための主要な成功指標として使用される。
{% endif %}

{% if include.metric == "Reads" %}
<i>既読</i>とは、ユーザーがメッセージを読んだ時のことを言います。Braze が既読数を追跡するには、ユーザーの既読レシートが「オン」になっている必要があります。
{% endif %}

{% if include.metric == "Read Rate" %}
<i>読み取り率とは</i>、送信のうち、読み取りが行われた割合である。これは、読み取りレシートをオンにしているユーザーにのみ与えられる。
{% endif %}

{% if include.metric == "Received" %}
<i>受信済み</i>はチャネルごとに定義が異なり、ユーザーがメッセージを閲覧したとき、ユーザーが定義されたトリガーアクションを実行したとき、またはメッセージがメッセージプロバイダに送信されたときのいずれかのことを言います。
{% endif %}

{% if include.metric == "Rejections" %}
<i>拒否</i>とは、SMS またはRCS がキャリアによって拒否された時のことをいいます。これは、通信事業者のコンテンツフィルタリング、宛先デバイスの可用性、電話番号の使用停止など、さまざまな理由から発生する可能性があります。
{% endif %}

{% if include.metric == "Revenue" %}
<i>収益</i>とは、設定された<a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>1次コンバージョン期間</a>内のキャンペーン受信者からのドル単位の総収益のことを言います。
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>送信済みメッセージ数</i>は、キャンペーンで送信されたメッセージの合計数です。スケジュールされたキャンペーンを開始した後、このメトリクスには、レート制限のためにまだ送信されているかどうかに関係なく、送信されたすべてのメッセージが含まれる。これは、メッセージが受信されたり、デバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味する。
{% endif %}

{% if include.metric == "Sent" %}
<i>送信済み</i>とは、キャンペーンまたはキャンバスステップが開始またはトリガーされ、Braze から SMS または RCS が送信されることをいいます。エラーによって SMS または RCS がユーザーの端末に届かなかった可能性もあります。
{% endif %}

{% if include.metric == "Sends" %}
<i>送信数</i>とは、1つのキャンペーンで送信されたメッセージの総数です。スケジュールされたキャンペーンを開始した後、このメトリクスには、レート制限のためにまだ送信されているかどうかに関係なく、送信されたすべてのメッセージが含まれる。これは、メッセージが受信されたり、デバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味する。
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>キャリアへの送信数</i>は非推奨になりましたが、すでにそれをお持ちのユーザーについては引き続きサポートされます。これは、<i>確認済み配信数</i>、<i>拒否数</i>、および通信事業者によって配信または拒否が確認されなかった<i>送信数</i>の合計です。これには、一部の通信事業者がこの確認を提供していないか、送信時に提供できないため、通信事業者が配信や拒否された確認を提供していない場合も含まれます。
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>キャリアへの送信率</i>は、送信されたメッセージのうち、<i>キャリアへの送信</i>として分類されたメッセージの割合です。これには、運送業者が配達確認や配達拒否確認を提供しない場合も含まれる。運送業者によっては、配達確認を提供しないか、発送時に提供できない場合もあるからだ。この指標は非推奨ですが、すでにそれをお持ちのユーザーについては引き続きサポートされます。
{% endif %}

{% if include.metric == "Spam" %}
<i>スパム</i>は、受信者によって「スパム」とマークされたメールの総数です。Braze はこれらのユーザーの購読状態を変更しませんが、「購読解除を含むすべてのユーザーに送信する」ように設定されているトランザクションメールを送信しない限り、これらのユーザーは今後のメールで自動的に除外されます。
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>調査ページ却下数</i>とは<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査</a>の調査の質問ページにある [閉じる] (x) ボタンのクリック数の合計です。
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>アンケートの送信数とは</i>、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>単純なアンケートの</a>送信ボタンをクリックした回数の合計である。
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>クリック数の合計</i>は、配信されたメッセージ内のリンクをクリックしたユニークな受信者の数です。
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>却下数の合計</i>とは、キャンペーンのコンテンツカードが却下された回数です。
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>トータル・インプレッションとは</i>、事前のインタラクションに関係なく、メッセージが読み込まれ、ユーザーの画面に表示された回数のことである（例えば、ユーザーがメッセージを2回表示された場合、2回カウントされる）。
{% endif %}

{% if include.metric == "Total Opens" %}
<i>開封数の合計</i>とは、開封されたメッセージ数の合計です。
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>総収益</i>とは、設定された1次コンバージョン期間内のキャンペーン受信者からのドル単位の総収益のことを言います。
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>ユニーククリック数とは</i>、メッセージ内のリンクを一度でもクリックした受信者の数であり、以下の方法で測定される。 <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>.
{% endif %}

<!-- Pull channels like Banners that don't have a Dispatch ID-->
{% if include.metric == "Unique Clicks No Dispatch ID" %}
<i>ユニーククリック数とは</i>、メッセージ内のリンクを一度でもクリックした受信者の数である。
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>ユニーク却下数</i>は、キャンペーンからコンテンツカードを却下した受信者の一意の数です。あるユーザーがキャンペーンからコンテンツカードを複数回却下すると、ユニークな却下 1 回になります。
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>ユニークインプレッション数</i>とは、特定のキャンペーンからメッセージを受信して表示したユーザーの総数です。
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>ユニーク受信者数</i>とは、1日のユニーク受信者数、つまり、1日に新しいメッセージを受信したユーザーの数です。このカウントが1人のユーザーに対して複数回増分されるためには、そのユーザーが別の日に新しいメッセージを受け取る必要があります。
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opensとは</i>、配信されたメッセージのうち、一人のユーザーが一度でも開封したメッセージの総数で、7日間にわたってトラッキング追跡される。
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Unsubscribers</i>または<i>Unsub</i>は、配信停止に至ったメッセージの数である。配信停止は、ユーザーが Braze の配信停止リンクをクリックしたときに発生します。
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>購読解除数</i>とは、Braze が提供する配信停止 URL をクリックした結果、サブスクリプション状態が配信停止に変更された受信者の数です。
{% endif %}

{% if include.metric == "Variation" %}
<i>バリエーション数</i>とは、キャンペーンのバリエーションの総数です。作成者の定義によって異なります。
{% endif %}
