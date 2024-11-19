{% if include.metric == "AMP Clicks" %}
<i>AMP Clicksは</i>、HTML版、プレーンテキスト版、AMP HTML版のメールの累積クリック数である。
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP Opensは</i>、AMP HTMLメールとAMP HTMLバージョンのメールの開封数の合計である。
{% endif %}

{% if include.metric == "Audience" %}
<i>オーディエンスは</i>、特定のメッセージを受け取ったユーザーの割合である。この数値は Braze から受信します。
{% endif %}

{% if include.metric == "Bounces" %}
<i>バウンスとは</i>、意図した受信者に届かなかったメッセージの総数である。
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

{% if include.metric == "Body Click" %}
プッシュストーリー通知は、通知がクリックされると<i>ボディクリックを</i>記録する。メッセージが展開されたとき、またはアクションボタンがクリックされたときには記録されません。
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>ボディ・クリックは</i>、従来のエディターで作成されたボタン（ボタン1、ボタン2）のないメッセージをユーザーがクリックしたとき、また、HTMLエディターやドラッグ＆ドロップ・エディターで作成されたメッセージをユーザーがクリックしたときに発生する。 <code>brazeBridge.logClick()</code> 引数なしで。
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Button 1 Clicksは</i>、メッセージのボタン1がクリックされた総数である。
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button 2 Clicksは</i>、メッセージのボタン2がクリックされた総数である。
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>送信された選択肢は</i>、ユーザーが<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単なアンケートの</a>質問ページで送信ボタンをクリックしたときに選択された選択肢の合計数である。
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>クリック開封率とは</i>、配信されたメールのうち、ユーザーまたはマシンが一度でも開封したメールの割合であり、<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>レポートビルダーでのみ</a>利用できる。
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>確認配信とは</i>、キャリアがターゲット電話番号にメッセージが配信されたことを確認した場合である。
{% endif %}

{% if include.metric == "Confidence" %}
<i>信頼度とは</i>、あるメッセージのバリアントが、コントロールグループより優れているという確信度のパーセンテージである。
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>確認ページボタンは</i>、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単な調査の</a>確認ページにあるコールトゥアクションボタンの総クリック数である。
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>確認ページ解散数とは</i>、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単なアンケートの</a>確認ページで閉じる (x) ボタンをクリックした合計である。
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>コンバージョン率は</i>、メッセージの全受信者と比較して、定義されたイベントが発生した回数の割合である。キャンペーンを作成するときに、このイベントを決定します。
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>コンバージョンウィンドウとは</i>、メッセージを受け取ってから、ユーザーのアクションがトラッキングされ、コンバージョンイベントに属性されるまでの日数のことである。この期間の後に発生したコンバージョンは、コンバージョンイベントに起因するものとは見なされません。
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>コンバージョン（B、C、D</i>）は、1次コンバージョンイベントの後に追加されるコンバージョンイベントである。これは、Brazeキャンペーンから受信したメッセージと対話または閲覧した後に、定義されたイベントが発生した回数である。
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>トータルコンバージョンとは</i>、ユーザーがアプリ内メッセージキャンペーンを閲覧した後、特定のコンバージョンイベントを完了した回数の合計である。
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Deliveriesは</i>、受信サーバーが受け付けたメッセージリクエストの総数である。これは、メッセージがデバイスに届いたことを意味するのではなく、メッセージがサーバーに受け入れられたことを意味する。
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Deliveries %は</i>、メール可能な相手に正常に送信され、受信されたメッセージ(Sends)の総数のパーセンテージである。
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>配信の失敗とは</i>、キューがオーバーフローしたためにSMSを送信できなかった場合である（ロングコードまたはショートコードが処理できる以上のレートでSMSを送信した）。
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>直接開封は</i>、そのプッシュ通知から直接開封されたプッシュ通知の総数（および割合）である。
{% endif %}

{% if include.metric == "Emailable" %}
<i>Eメール可能なユーザーとは</i>、Eメールアドレスが記録されており、明示的にオプトインまたはサブスクライバーになっているユーザーの総数である。
{% endif %}

{% if include.metric == "Errors" %}
<i>エラーは</i>、Webhookイベントによって返されたエラーの数である（送信プロセス中にインクリメントされる）。
{% endif %}

{% if include.metric == "Failures" %}
WhatsAppメッセージがインターネットサービスプロバイダからハードバウンスされ、送信<i>できなかった</i>。ハードバウンスとは、永続的な配信の失敗です。
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Influenced Opensは</i>、プッシュ通知が送信された後、プッシュ通知を直接開かずにアプリを開封したユーザーの総数（および割合）である。
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>生涯収入とは</i> <code>PurchaseEvents</code> 開始以来受け取った価格（米ドル）。
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>ユーザー一人当たりの生涯</i>価値は、ある日のキャンペーンとキャンバスの収益の合計の平均である。
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>平均日次収益とは</i>、<i>生涯収益を</i> <i>総ユーザー数で</i>割ったものである（ホームページに記載）。
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>1日あたりの購入</i>額は、ユニークユーザー数の平均である。 <code>PurchaseEvents</code> を超えた。
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
<i>Daily Revenue Per Userは</i>、1日のアクティブユーザーあたりの1日平均売上高である。
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>機械開封</i>」には、iOS 15のアップルのメール・プライバシー保護（MPP）の影響を受ける「開封」の割合が含まれる。例えば、ユーザーが Apple デバイスのメールアプリを使用してメールを開封した場合、これは<i>マシン開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Other Opens" %}
<i>その他の開封には</i>、<i>マシン開封として</i>識別されていないメールが含まれる。例えば、ユーザーが別のプラットフォーム (携帯電話の Gmail アプリ、デスクトップブラウザーの Gmail など) でメールを開封すると、これは<i>その他の開封</i>としてログに記録されます。
{% endif %}

{% if include.metric == "Opens" %}
<i>開封とは</i>、<i>Direct Opensと</i> <i>Influenced Opensの</i>両方を含むインスタンスで、Braze SDKが独自のアルゴリズムを用いて、プッシュ通知によってユーザーがアプリを開封したと判断したものを指す。
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>オプトアウトとは</i>、ユーザーがあなたのメッセージに<a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">オプトアウトキーワードで</a>返信し、あなたのSMSプログラムから配信停止された場合である。
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Pending Retryは</i>、受信サーバーによって一時的に拒否されたが、メールサービスプロバイダー（ESP）によって再配信が試みられたリクエストの数である。メールサービスプロバイダー (ESP) は、タイムアウト期間に達する (通常は 72 時間後) まで配信を再試行します。
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>1次コンバージョン(A)</i>または<i>1次コンバージョンイベントとは</i>、キャンペーンで受信したメッセージに接触または閲覧した後、定義されたイベントが発生した回数のことである。この定義されたイベントは、キャンペーンを構築する際にあなたが決定する。
{% endif %}

{% if include.metric == "Reads" %}
<i>Readsは</i>ユーザーがWhatsAppメッセージを読むことである。Brazeが読み取りを追跡するには、ユーザーの読み取りレシートが「オン」になっていなければならない。
{% endif %}

{% if include.metric == "Received" %}
<i>Receivedは</i>チャネルごとに定義が異なり、ユーザーがメッセージを閲覧したとき、ユーザーが定義されたトリガーアクションを実行したとき、メッセージがメッセージプロバイダに送信されたときのいずれかになる。
{% endif %}

{% if include.metric == "Rejections" %}
<i>拒否とは</i>、SMSがキャリアによって拒否された場合である。これは、通信事業者のコンテンツフィルタリング、宛先デバイスの可用性、電話番号の使用停止など、さまざまな理由から発生する可能性があります。
{% endif %}

{% if include.metric == "Revenue" %}
<i>Revenueは</i>、設定された<a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>1次コンバージョンウィンドウ</a>内のキャンペーン受信者からの総収入（ドル）である。
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Messages Sentは</i>キャンペーンで送信されたメッセージの総数である。スケジュールされたキャンペーンを開始した後、このメトリクスには、レート制限のためにまだ送信されているかどうかに関係なく、送信されたすべてのメッセージが含まれる。これは、メッセージが受信されたり、デバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味する。
{% endif %}

{% if include.metric == "Sent" %}
<i>送信済みとは</i>、キャンペーンまたはキャンバスステップが開始またはトリガーされ、BrazeからSMSが送信されるたびに送信される。エラーによってSMSがユーザーの端末に届かなかった可能性もある。
{% endif %}

{% if include.metric == "Sends" %}
<i>Sendsは</i>キャンペーンで送信されたメッセージの総数である。スケジュールされたキャンペーンを開始した後、このメトリクスには、レート制限のためにまだ送信されているかどうかに関係なく、送信されたすべてのメッセージが含まれる。これは、メッセージが受信されたり、デバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味する。
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>キャリアへの送信数</i>は非推奨になりましたが、すでにそれをお持ちのユーザーについては引き続きサポートされます。これは、<i>配達が確認されたもの</i>、<i>拒否された</i>もの、運送会社によって配達または拒否が確認されなかった<i>送信の</i>合計である。これには、運送業者が配達確認を提供しない、あるいは発送時に提供できない場合も含まれる。
{% endif %}

{% if include.metric == "Spam" %}
<i>スパムは</i>、"スパム "とマークされたメールの総数である。Braze では、メールをスパムとしてマークしたユーザーを自動的に配信停止し、そのようなユーザーは将来のメールのターゲットになりません。
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>アンケートページ解散数とは</i>、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>簡単なアンケートの</a>質問ページで閉じる (x) ボタンをクリックした合計のことである。
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>アンケートの送信数とは</i>、<a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>単純なアンケートの</a>送信ボタンをクリックした回数の合計である。
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Total Clicksは</i>、同じユーザーが複数回クリックしたかどうかにかかわらず、配信されたメッセージ内でクリックしたユーザーの総数（および割合）である。
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Total Dismissalsは</i>、キャンペーンのコンテンツカードが却下された回数である。あるユーザーがメッセージを 2 回無視しても、1 回のみカウントされます。
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>トータル・インプレッションとは</i>、事前のインタラクションに関係なく、メッセージが読み込まれ、ユーザーの画面に表示された回数のことである（例えば、ユーザーがメッセージを2回表示された場合、2回カウントされる）。
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Total Opensは開封</i>されたメッセージの総数である。
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Total Revenueは</i>、設定した1次コンバージョンウィンドウ内のキャンペーン受信者からの総収入（ドル）である。
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Unique Clicks（ユニーク・クリック数</i>）とは、メッセージ内で一度でもクリックした受信者の数で、<a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_idによって</a>計測される。
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Unique Dismissalsは</i>、キャンペーンからコンテンツカードを却下したユーザーの数である。あるユーザーがキャンペーンからコンテンツカードを複数回却下すると、ユニークな却下 1 回になります。
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>ユニーク・インプレッションとは</i>、あるメッセージを1日に受信し、閲覧したユーザーの総数である。
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Unique Recipients（ユニーク受信者数</i>）とは、1日のユニーク受信者数、つまり1日に特定のメッセージを受信したユーザー数である。
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opensとは</i>、配信されたメッセージのうち、一人のユーザーが一度でも開封したメッセージの総数で、7日間にわたってトラッキング追跡される。
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Unsubscribers</i>または<i>Unsub</i>は、配信停止に至ったメッセージの数である。配信停止は、ユーザーが Braze の配信停止リンクをクリックしたときに発生します。
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>配信停止は</i>、Brazeが提供する配信停止URLをクリックした結果、サブスクリプションの状態が配信停止に変わった受信者の数である。
{% endif %}

{% if include.metric == "Variation" %}
<i>バリエーションは</i>、クリエイターによって定義されたキャンペーンのバリエーションの数である。
{% endif %}