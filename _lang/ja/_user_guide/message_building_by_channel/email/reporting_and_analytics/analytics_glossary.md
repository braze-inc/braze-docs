---
nav_title: 電子メール分析用語集
article_title: 電子メール分析用語集 
page_order: 0
layout: glossary_page
glossary_top_header: "Email analytics glossary"
glossary_top_text: "These are terms you'll find in the analytics section of your email campaign or Canvas, post-launch. Search for the metrics you need in this glossary. <br><br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

description: "この用語集には、起動後にメール キャンペーンまたはキャンバスの分析の項に記載されている用語が含まれています。この用語集には、Currents測定基準は含まれていません。"
channel:
  - email

glossaries:
  - name: "バリエーション"
    description: キャンペーンのバリエーション。作成者の定義によって異なります。
    calculation: Count
  - name: "電子メール"
    description: レコードにメールの住所があり、明示的にオプトインまたは登録されているユーザ。
    calculation: Count
  - name: "対象者%"
    description: 特定のバリアントを受信したユーザー s のパーセンスタグe。
    calculation: Number of Recipients in Variant / Unique Recipients
  - name: "ユニーク受信者数"
    description: 日次ユニーク受信者数。1 日に特定のメッセージを受信したユーザー数。この数値は Braze から受信します。
    calculation: Count
  - name: "送信済みまたは送信済みのメッセージ"
    description: メール キャンペーンで送信されたメールの総数。この数値は Braze から受信します。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。
    calculation: Count
  - name: "配信数"
    description: メール可能な相手に正常に送受信されたメール(送信)の総数。
    calculation: Sends - Bounces
  - name: "配送率"
    description: メール可能な相手に正常に送受信されたメール(送信)の総数。
    calculation: (Sends - Bounces) / (Sends)
  - name: "バウンス数"
    description: "送信に失敗した、または\"returned\"または\"received\"not received\"送信サービスが使用されているか、またはメール可能なユーザーが受信していないメッセージの総数原因として、有効なプッシュトークンがない、メールアドレスが間違っているか無効になっている、またはキャンペーンの開始後にユーザーが配信停止した、などがあります。<br><br> <b>ハードバウンス</b>:ハードバウンスとは、受信者のアドレスが不正であるために送信者に返されたメールのことです。ドメイン名が存在しないか、受信者が不明なため、ハードバウンスが発生する可能性があります。メールがハードバウンスを受信した場合、このメール住所への今後のリクエストは中止されます。<br><br><b>ソフトバウンス</b>:ソフト・バウンスは、受信者のメール・サーバーまで送信されますが、配信されずにバウンスされてから受信者に送信されるメールなメッセージです。受信者の受信トレイがいっぱいであるか、サーバーが停止しているか、メッセージが受信者の受信トレイには大きすぎるため、ソフトバウンスが発生する可能性があります。メールがソフトバウンスを受信した場合、通常は72時間以内に再試行されますが、再試行回数は受信側によって異なります。<br><br> <a href='/docs/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/#message-activity-log-tab'>Message Activity Log</a>でハードバウンスとソフトバウンスを追跡することもできます。<br><br><i> 不正なアドレスに送信されたハードバウンス、メール、および顧客 s のSendGridによるバウンスは、不正なアドレスに送信されるスパム、および s で構成されます。 </i>"
    calculation: Count
  - name: "バウンス%またはバウンス・レート"
    description: "送信に失敗した、または\"returned\"または\"not received\" from send services used またはnot received メール可能なユーザーs によって受信されなかったメッセージのパーセンテージe。原因として、有効なプッシュトークンがない、メールアドレスが間違っているか無効になっている、またはキャンペーンの開始後にユーザーが配信停止した、などがあります。<br> <i> メール は、顧客 s のSendGrid を使用したバウンスで、ハードバウンス、スパム (`スパム_レポート_drops`)、および不正なアドレス(`invalid_メール') に送信されます。 </i>"
    calculation: Bounces / Sends
  - name: "スパム"
    description: 「スパム」としてマークされたメール配信数の合計。Braze は自動的に配信停止 s ユーザー s をメールとしてマークし、それらのユーザーは将来のメール s にターゲットされません。
    calculation: (Marked as Spam) / (Sends)
  - name: "スパム%またはスパム・レート"
    description: "マークされた、または&amp;quot として指定された配信済みメールのパーセンテージe;スパム.\"Braze は自動的に配信停止 s ユーザー s をメールとしてマークし、それらのユーザーは将来のメール s にターゲットされません。"
    calculation: (Marked as Spam) / (Sends)
  - name: "ユニーク開封数"
    description: 1 つのユーザーまたはマシンによって少なくとも1 回開封された配信メールの総数。これは、Eメールの7日間にわたって追跡されます。
    calculation: (Unique Opens) / (Deliveries)
  - name: "一意のオープン率%または一意のオープン率"
    description: 少なくとも1回のユーザーによって開封された、送達されたメールsのパーセンテージe。これは、Eメールの7日間にわたって追跡されます。
    calculation: (Unique Opens) / (Deliveries)
  - name: "ユニーククリック数"
    description: "メッセージ内を少なくとも 1 回クリックしたユニーク受信者の数。これは、電子メールの7 日間にわたって追跡され、<a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> によって測定されます。"
    calculation: Count
  - name: "一意のクリック率%またはクリック率"
    description: メッセージ内を少なくとも 1 回クリックしたユニーク受信者の数。これは、Eメールの7日間にわたって追跡されます。
    calculation: Unique Clicks / Deliveries
  - name: "Un サブスクライバー sまたはUnsub"
    description: サブスクリプションが解除された件数。Un サブスクリプション s は、ユーザーがBraze 配信停止リンクをクリックしたときに発生します。
    calculation: Count
  - name: "Un サブスクライバー s % またはUnsub Rate"
    description: 未サブスクリプションとなった配信メールのパーセンスタグe。Un サブスクリプション s は、ユーザーがBraze 配信停止リンクをクリックしたときに発生します。
    calculation: Unsubscribes / Deliveries
  - name: "収益"
    description: "設定された<a href='/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event'>1次コンバージョンウィンドウ</a>内のキャンペーン 受信者sからの総収益(ドル単位)。"
    calculation: Count
  - name: "1 次コンバージョン (A) または 1 次コンバージョンイベント"
    description: Braze キャンペーンから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数。このイベントは、キャンペーンを作成するときにマーケターが決定します。
    calculation: Count
  - name: "1 次コンバージョン (A) または 1 次コンバージョンイベント"
    description: Braze キャンペーンとやり取りした後、またはBraze キャンペーンから受信したメッセージを表示した後に、定義されたイベントが発生した時間のパーセンタグe。このイベントは、キャンペーンを作成するときにマーケターが決定します。
    calculation: "Primary Conversions / Unique Recipients"
  - name: "信頼度"
    description: メッセージの特定のバリアントのパフォーマンスがコントロールグループよりも優れているという信頼度の割合。
  - name: "マシンオープン"
    description: "「\" 開封 s\"」の割合を含みます。iOS 15 のアップルのメールプライバシー保護(MPP)の影響を受けます。たとえば、ユーザー 開封がアプリ le デバイスのメールアプリを使用してメールを送信した場合、これは<i>Machine 開封 s</i> としてログに記録されます。このメトリクスは、SendGridの場合は2021年11月11日から、SparkPostの場合は2021年12月2日から追跡されます。"
    calculation: Count
  - name: "その他のオープン"
    description: <i>Machine Opens</i>と識別されていないメールを含みます。たとえば、ユーザー 開封が別のプラットフォーム(電話機のGmail アプリ、デスクトップブラウザのGmail など) でメールを送信すると、これは<i>Other 開封 s</i> としてログに記録されます。ユーザーは、<i>マシン開封s</i>数が記録される前に、(<i>他の開封s</i>に対する開封数などの)メールも開封できることに注意してください。ユーザー 開封が、Apple Mail 以外のメールからマシン開封を受信トレイした後、1 回(またはそれ以上) にメールが発生した場合、ユーザー 開封が<i>Other 開封 s</i> に向かって計算され、<i>Unique 開封 s</i> に向かって1 回だけ計算されます。
    calculation: Count
  - name: "クリックして率を開く"
    description: 一意のメールのパーセンテージe は、少なくとも1 回クリックされた開封です。
    calculation: Unique Clicks / Unique Opens

---
