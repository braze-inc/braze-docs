---
page_order: 2
nav_title: セグメンテーションフィルター
article_title: セグメンテーションフィルター
layout: glossary_page
glossary_top_header: "セグメンテーションフィルター"
glossary_top_text: "Braze SDK には、特定の機能と属性に基づいてユーザーをセグメント化し、ターゲットにするための強力なフィルターが備わっています。フィルターカテゴリごとに、これらのフィルターを検索または絞り込むことができます。<br><br>ユーザーをセグメント化するために使用できる各種カスタム属性データタイプについては、<a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">カスタム属性データタイプ</a>を参照してください。"

page_type: glossary
tool: Segments
description: "この用語集には、ユーザーをセグメント化およびターゲット化するための使用可能なフィルターが一覧表示されています。"
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
# NOTE: glossary_tags names must match the "tags" under each glossary entry exactly (filter/checkbox logic).
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: "Segment Membership"
    description: フィルターが使用されている任意のセグメントメンバーシップ (セグメントやキャンペーンなど) に基づいてフィルターし、1 つのキャンペーン内で複数の異なるセグメントをターゲットにすることができます。<br><br>すでにこのフィルターを使用しているセグメントをさらに追加したり、他のセグメントにネストしたりすることはできません。これは、セグメント A にセグメント B が含まれ、セグメント B に再びセグメント A が含まれるというサイクルが発生する可能性があるためです。もしそうなれば、セグメントは自分自身を参照し続けることになり、誰が実際にそのセグメントに属しているのかを計算することができなくなります。また、このようにセグメンテーションを入れ子にすると、複雑さが増し、動作が遅くなる。代わりに、同じフィルターを使用して、含めようとしているセグメンテーションを再作成する。
    tags:
      - Segment or CSV membership
  - name: "Braze Segment Extensions"
    description: セグメントエクステンションを Braze ダッシュボードで作成した後、それらのエクステンションをセグメントに含めたり除外したりできます。
    tags:
      - Segment or CSV membership
  - name: "Updated/Imported from CSV"
    description: CSV アップロードの一部であるかどうかに基づいてユーザーをセグメント化します。
    tags:
      - Segment or CSV membership
  - name: "Custom Attributes"
    description: "ユーザーが、記録されたカスタム属性値と一致するかどうかを決定します。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom attribute
  - name: "Created At"
    description: ユーザープロファイルが作成された時期でユーザーをセグメンテーションする。ユーザーがCSVまたはAPIによって追加された場合、このフィルターは追加された日付を反映する。ユーザーがCSVまたはAPIによって追加されておらず、SDKによって最初のセッションがトラッキングされている場合、このフィルターはその最初のセッションの日付を反映する。
    tags:
      - Other Filters
  - name: "Nested Custom Attributes"
    description: "カスタム属性のプロパティである属性。<br><br>階層化された時間のカスタム属性にフィルターを適用する場合、基準として [年間通算日] または [時刻] を選択できます。「年の日」は比較対象として月と日のみを確認する。「時間」は、年を含む完全なタイムスタンプを比較する。"
    tags:
      - Custom attribute
  - name: "Day of Recurring Event"
    description: "このフィルターでは、データタイプが\"date\"のカスタム属性の月と日を調べますが、年は調べません。このフィルターは毎年発生するイベントに役立ちます。<br><br>タイムゾーン:<br>このフィルターは、メッセージがローカル時間のスケジュールオプションで送信される限り、ユーザーのタイムゾーンに合わせて調整する。そうでない場合、このフィルターは会社のタイムゾーンを使用する。"
    tags:
      - Custom attribute
  - name: "Custom Event"
    description: "ユーザーが特別に記録された行動を実行したかどうかを決定します。<br><br> 例: <br>プロパティ activity_name によるアクティビティが完了した。<br><br>タイムゾーン:<br>UTC - カレンダー日 = 1カレンダー日は、ユーザーの過去24～48時間の履歴を参照する"
    tags:
      - Custom events
  - name: "First Did Custom Event"
    description: "ユーザーが特別に記録された行動を実行した最も早い時刻を決定します。(24時間) <br><br>例: <br> 初回のカート放棄が過去 1 日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: "Last Did Custom Event"
    description: "ユーザーが特別に記録された行動を最後に実行した時刻を決定します。このフィルターでは、0.25時間のような小数値がサポートされています。(24時間) <br><br>例: <br> 最後のカート放棄が過去 1 日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: "X Custom Event In Y Days"
    description: "ユーザーが、最後に指定された暦日数 (1 ～ 30 日) の間に、特別に記録されたイベントを 0 ～ 50 回実行したかどうかを決定します。(カレンダー日＝1カレンダー日は、ユーザーの過去24～48時間の履歴を参照する)<br> <a href=\"/docs/x-in-y-behavior/\"> ここでは、X-in-Y の動作について詳しく説明します。</a><br><br>例: <br>過去 1 暦日内にカートをちょうど 0 回放棄した<br><br>タイムゾーン:<br>UTC - 全てのタイムゾーンを考慮するため、1暦日ではセグメント評価時刻に応じて24～48時間のユーザー履歴を分析する。2暦日では48～72時間のユーザー履歴を分析し、以下同様である。"
    tags:
      - Custom events
  - name: "X Custom Event Property In Y Days"
    description: "ユーザーが、最後に指定された暦日数 (1 ～ 30 日) の間に、特別に記録されたイベントを特定のプロパティについて 0 ～ 50 回実行したかどうかを決定します。(カレンダー日＝1カレンダー日は、ユーザーの過去24～48時間の履歴を参照する)<br><a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a><br><br>例: <br> 過去 1 暦日内にカートをちょうど 0 回お気に入りに追加した<br><br>タイムゾーン:<br>UTC - 全てのタイムゾーンを考慮するため、1暦日ではセグメント評価時刻に応じて24～48時間のユーザー履歴を分析する。2暦日では48～72時間のユーザー履歴を分析し、以下同様である。"
    tags:
      - Custom events
  - name: "Email Address"
    description: "テスト用に個々のメールアドレスによってキャンペーン 受信者を指定できます。これは、フィルターで「メールアドレスが空白でない」指定子を使用して、トランザクションメールをすべてのユーザー (配信停止済みユーザーを含む) に送信するためにも使用できます。このため、オプトインのステータスに関わらずメール配信を最大限に高めることができます。<br><br>このフィルターではユーザープロファイルにメールアドレスがあるかどうかだけがチェックされますが、[<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">利用可能なメール</a>] フィルターでは追加の条件がチェックされます。"
    tags:
      - Other Filters
  - name: "External User ID"
    description: テストのために、キャンペーン受信者を個々のユーザー ID で指定することができます。
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: ユーザーをランダムに割り当てられた番号(0～9999を含む)でセグメント化します。これにより、AB テストと多変量テストに対する真のランダムユーザーの一様分布セグメントを生成できるようになります。
    tags:
      - Other Filters
  - name: "Session Count"
    description: ユーザーをワークスペース内のいずれかのアプリでこれまでに行ったセッション数でセグメント化します。
    tags:
      - Sessions
  - name: "Session Count For App"
    description: 指定されたアプリ内でこれまでに行ったセッション数によってユーザーをセグメント化します。
    tags:
      - Sessions
  - name: "X Sessions In Last Y Days"
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、貴社のアプリで行ったセッション数 (0 ～ 50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Sessions
  - name: "First Used App"
    description: "アプリを開封した記録の最も早い時刻によってユーザーをセグメント化します。<em>これは、Braze SDKが統合されたバージョンのアプリを初めて使用したセッションを記録するものである。</em>(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: "First Used Specific App"
    description: "ワークスペース内の任意のアプリを開封した記録の最も早い時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: "Last Used App"
    description: "アプリを開封した最後の時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: "Last Used Specific App"
    description: "指定されたアプリを開封した最後の時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: "Median Session Duration"
    description: アプリ内のセッションの長さの中央値によってユーザーをセグメント化します。
    tags:
      - Sessions
  - name: "Received Message from Campaign"
    description: "指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉する。同じメールアドレスのユーザーや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外だ。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用する。<br><br> コンテンツカード、バナー、アプリ内メッセージについては、カードやアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録したときである。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: "Received Campaign Variant"
    description: "受信した多変量キャンペーンのバリアントによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉する。同じメールアドレスのユーザーや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外だ。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用する。<br><br> コンテンツカード、バナー、アプリ内メッセージについては、カードやアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録したときである。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: "Received Message from Canvas Step"
    description: "特定のキャンバスコンポーネントを受信したかどうかによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉する。同じメールアドレスのユーザーや電話番号を持つ他のユーザーで、重複したメッセージを受信した者は対象外だ。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">キャンペーンまたはタグ付きキャンバスからの受信メッセージ</a>を使用する。<br><br> コンテンツカードおよびアプリ内メッセージの場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: "Last Received Message from Specific Canvas Step"
    description: "特定のキャンバスコンポーネントを受信した日時によってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉する。同じメールアドレスのあるユーザーや、同じ電話番号のあるユーザー、つまり重複メッセージを受信したユーザーは捕捉しない。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">「キャンペーンからの受信メッセージ」または「タグ付きキャンバス」</a>を使用せよ。このフィルターでは、ユーザーが他のキャンバスコンポーネントをいつ受信したかは考慮されません。"
    tags:
      - Retargeting
  - name: "Last Received Message from Specific Campaign"
    description: "指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。このフィルターは、明示的にメッセージが送信されたユーザーのみを捕捉する。同じメールアドレスのあるユーザーや、同じ電話番号のあるユーザー、つまり重複メッセージを受信したユーザーは捕捉しない。重複ユーザーを捕捉するには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">「キャンペーンからの受信メッセージ」または「タグ付きキャンバス」</a>を使用せよ。このフィルターは、ユーザーがいつ他のキャンペーンを受けたかを考慮しない。"
    tags:
      - Retargeting
  - name: "Received Message from Campaign or Canvas with Tag"
    description: "指定したキャンペーンを受信したかどうか、または指定したタグのキャンバスを受信したかどうかによって、ユーザーを分割します。「キャンペーンからのメッセージを受信」や「キャンバスステップからのメッセージを受信」とは異なり、このフィルターは重複メッセージを受信した同一のメールアドレスまたは電話番号を持つ全ユーザーを捕捉する。<br><br> コンテンツカード、バナー（キャンペーンのみ）、アプリ内メッセージについては、カードやアプリ内メッセージが送信された時点ではなく、ユーザーがインプレッションを記録した時点となる。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>メールが配信された時、あるいはユーザーがそのメールやメール内のリンクを開封した時、そのメールアドレスを共有している全てのユーザーがメッセージを受信したように見える。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: "Last Received Message from Campaign or Canvas With Tag"
    description: 特定のタグを持つ特定のキャンペーンまたはキャンバスを受信した日時によってユーザーをセグメント化します。このフィルターは、ユーザーが他のキャンペーンやキャンバスを受け取った場合は考慮しない。(24時間)
    tags:
      - Retargeting
  - name: "Has Never Received a Message from Campaign or Canvas Step"
    description: キャンペーンまたはキャンバスコンポーネントを受信したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: "Last Received Email"
    description: "最後にメールを受信したときに、ユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Last Received Push"
    description: "ユーザーを最後にプッシュ通知のいずれかを受信したときにセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Last In App Message Impression"
    description: ユーザーを最後にアプリ内メッセージを表示したときにセグメント化します。
    tags:
      - Retargeting
  - name: "Last Received SMS"
    description: "最後のメッセージがSMSプロバイダーに配信された時刻までにユーザーをセグメント化します。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Last Received Webhook"
    description: "ユーザーを、BrazeがそのユーザーのWebhookを最後に送信した時刻までに分割します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Last Received WhatsApp"
    description: "最後にWhatsAppを受信したときに、ユーザーをセグメント化します。これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Live Activities Push to Start Registered for App"
    description: ユーザーを、特定のアプリ向けにiOSプッシュ通知を通じてライブアクティビティを開始するために登録しているかどうかでセグメントする。
    tags:
      - Devices
  - name: "Clicked/Opened Campaign"
    description: "特定のキャンペーンとのインタラクションでフィルタリングします。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。<br><br> メールについては、「開封済みメール（機械開封）」と「開封済みメール（その他開封）」でフィルターをかけるオプションもある。配信停止リンクやユーザー設定センターでのクリックは、このフィルターの対象外だ。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーは、指定のキャンペーンから、ユーザーのクリック追跡が有効になっている SMS メッセージ内の短縮リンクを最後に選択しました。"
    tags:
      - Retargeting
  - name: "Clicked/Opened Campaign or Canvas With Tag"
    description: "特定のタグを持つ特定のキャンペーンとのインタラクションでフィルタリングします。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。<br><br> メールについては、「開封済みメール（機械開封）」と「開封済みメール（その他の開封）」でフィルターをかけるオプションがある。複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーがタグを持つ指定のキャンペーンまたはキャンバスステップから、ユーザーのクリック追跡が有効になっている SMS メッセージ内の短縮リンクを最後に選択した日時。"
    tags:
      - Retargeting
  - name: "Clicked/Opened Step"
    description: 特定のキャンバスコンポーネントとのインタラクションでフィルタリングします。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。<br><br>メールについては、「開封済みメール（機械開封）」と「開封済みメール（その他の開封）」でフィルターをかけるオプションがある。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーが受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーは、指定のキャンバスステップから、ユーザーのクリック追跡が有効になっている SMS メッセージ内の短縮リンクを最後に選択しました。
    tags:
      - Retargeting
  - name: "Clicked Alias in Campaign"
    description: "指定したキャンペーンの特定の別名をクリックしたかどうかによって、ユーザーをフィルタリングします。これはメールメッセージだけに適用されます。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: "Clicked Alias in Canvas Step"
    description: "特定のキャンバスで特定のエイリアスをクリックしたかどうかによって、ユーザーをフィルタリングします。これはメールメッセージだけに適用されます。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: "Clicked Alias in Any Campaign or Canvas Step"
    description: "ユーザーを、任意のキャンペーンまたはキャンバス内で特定のエイリアスをクリックしたかどうかによってフィルタリングします。これはメールメッセージだけに適用されます。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: "Hard Bounced"
    description: ユーザーを、メールアドレスがハードバウンスされたかどうか (メールアドレスが不正な場合など) によってセグメント化します。
    tags:
      - Retargeting
  - name: "Soft Bounced"
    description: Y日間にX回バウンスしたかどうかでユーザーをセグメントします。セグメントフィルターでは30日間しか遡ることができないが、セグメントエクステンションを使えばさらに遡ることができる。<br><br>このフィルターは、Currents のソフトバウンスイベントとは異なる動作をします。ソフトバウンスセグメンテーションフィルターは、72時間のリトライ期間中に配信が成功しなかった場合、ソフトバウンスをカウントします。Currents では、失敗した再試行はすべてソフトバウンスイベントとして送信されます。 
    tags:
      - Retargeting
  - name: "Has Marked You As Spam"
    description: メッセージをスパムとしてマークしたかどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: "Invalid Phone Number"
    description: 電話番号が不正かどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: "Last Sent Specific SMS Inbound Keyword Category"
    description: 特定のキーワードカテゴリ内の特定のサブスクリプショングループにSMSを最後に送信したときに、ユーザーをセグメント化します。 
    tags:
      - Retargeting
  - name: "Converted From Campaign"
    description: 特定のキャンペーンでコンバージョンしたかどうかによってユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: "Converted From Canvas"
    description: 特定のキャンバスでコンバージョンしたかどうかによってユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: "In Campaign Control Group"
    description: ユーザーを、指定した多変量 キャンペーンのコントロールグループにあるかどうかによってセグメント化します。
    tags:
      - Retargeting
  - name: "In Canvas Control Group"
    description: ユーザーを、指定したキャンバスのコントロールグループにあるかどうかによって分割します。このフィルターはキャンバスに入ったユーザーのみを評価する。したがって、一度も入らなかったユーザーは結果から完全に除外される。<br><br>例えば、キャンバスのコントロールグループに属さないユーザーをフィルターでフィルタリングすると、キャンバスにアクセスし非コントロールバリアントに割り当てられたユーザーのみが対象となる。キャンバスに一度もアクセスしなかったユーザーは含まれない。キャンバスへのエントリに関わらず、全てのユーザーを含めるには、 <code>Entered Canvas Variation</code> 代わりにフィルターを使う。
    tags:
      - Retargeting
  - name: "Last Enrolled in Any Control Group"
    description: "キャンペーンで最後にコントロールグループに割り当てられた時刻によってユーザーをセグメント化します。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Entered Canvas Variation"
    description: 特定のキャンバスのバリエーションパスを入力したかどうかによって、ユーザーをセグメント化します。このフィルターはすべてのユーザーを評価します。<br><br>例えば、キャンバスのバリエーションコントロールグループに入っていないユーザーをフィルターで検索すると、コントロールグループに属していない全ユーザーが対象となる。キャンバスに入ったかどうかは関係なく、コントロールグループに属していないユーザーが対象となるのだ。
    tags:
      - Retargeting
  - name: "Last Received Any Message"
    description: "最後に受信したメッセージを判別して、ユーザーをセグメント化します。(24時間)<br><br> コンテンツカード、バナー、アプリ内メッセージについては、カードやアプリ内メッセージが最後に送信されたときではなく、ユーザーが最後にインプレッションを記録したときである。<br><br>プッシュおよびwebhookの場合、これは、任意のメッセージがユーザーに送信されたときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されたときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>メールが配信された時、あるいはユーザーがそのメールやメール内のリンクを開封した時、そのメールアドレスを共有している全てのユーザーがメッセージを受信したように見える。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。<br><br>例: <br>前回受信メール1日未満=24時間未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Last Engaged With Message"
    description: "メッセージングチャネル（バナー、コンテンツカード、メール、アプリ内メッセージ、SMS、プッシュ、WhatsApp）のいずれかを最後にクリックまたは開封した回数でユーザーをセグメンテーション。メールメッセージングの場合、開封イベントにはマシン開封とマシン以外の開封の両方が含まれます。(24時間)<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。これには、「開封済みメール（機械開封）」と「開封済みメール（その他開封）」でフィルターをかけるオプションも含まれている。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>メールが配信された時、あるいはユーザーがそのメールやメール内のリンクを開封した時、そのメールアドレスを共有している全てのユーザーがメッセージを受信したように見える。<br><br>SMSの場合、ユーザークリック\"トラッキングが有効になっているメッセージ内の短縮リンクを最後に選択したユーザー。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: "Clicked card"
    description: 特定のコンテンツカードをクリックしたかどうかによってユーザーをセグメント化します。このフィルターは、「キャンペーンをクリック/開封」、「タグ付きのキャンペーンまたはキャンバスをクリック/開封」、および「ステップをクリック/開封」のサブフィルターとして使用できます。
    tags:
      - Retargeting
  - name: "Feature Flags"
    description: "現在有効になっている特定の<a href=\"/docs/developer_guide/feature_flags/\">フィーチャーフラグ</a>を持つユーザーのSegment。"
    tags:
      - Retargeting
  - name: "Subscription Group"
    description: メール、SMS/MMS、またはWhatsAppのサブスクリプショングループでユーザーを分割します。アーカイブされたグループは表示されず、使用できない。
    tags:
      - Channel subscription behavior
  - name: "Email Available"
    description: "ユーザーを、有効なメールアドレスを持っているかどうか、およびメール配信の購読またはオプトインの有無によってセグメント化する。このフィルターは、ユーザーがメールの配信停止をしているか、Brazeがハードバウンスを受け取っているか、メールがスパムとしてマークされているかの3つの条件をチェックする。これらの条件のいずれかが満たされる場合、またはユーザーにメールが存在しない場合、そのユーザーは含まれない。<br><br>メールが利用可能なユーザーは <code>false</code> キャンペーンのオーディエンスから除外され、メールを受け取らない。たとえ送信設定が全ユーザー（配信停止ユーザーを含む）に送信するよう設定されていても、同様である。<br><br>オプトインステータスが重要なメールについては、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">メールアドレスの</a>代わりに「利用可能なメールアドレス」を使用する。追加の条件は、メールを受け取る資格があるユーザーをターゲットにするのに役立つ。"
    tags:
      - Channel subscription behavior
  - name: "Email Opt In Date"
    description: メールをオプトインした日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: "Email Subscription Status"
    description: メールの購読ステータスによってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: "Email Unsubscribed Date"
    description: 今後のメールを配信停止した日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: "Foreground Push Enabled"
    description: 暫定的なプッシュ認証があるか、フォアグラウンドプッシュが有効になっているユーザーをセグメント化します。具体的には、このカウントには以下が含まれます。<br>1. 暫定的にプッシュが承認されている iOS ユーザー。<br>2.フォアグラウンドプッシュをイネーブルメントしているユーザーで、プッシュサブスクリプションのステータスが配信停止になっていないユーザー。これは、あなたのアプリのいずれかについて言えることだ。これらのユーザーの場合、この数にはフォアグラウンドプッシュのみが含まれます。<br><br>フォアグラウンドプッシュイネーブルメントには、配信停止を行ったユーザーは含まれない。<br><br>このフィルターでセグメンテーションを行った後、下部の「<em>リーチ可能なユーザー</em>」パネルで、Android、iOS、Webの各プラットフォームごとにそのセグメントに含まれるユーザーの内訳を確認できる。
    tags:
      - Channel subscription behavior
  - name: "Foreground Push Enabled for App"
    description: デバイス上のアプリでプッシュ通知を有効にしているかどうかによってユーザーをセグメント化します。アプリに対してフォアグラウンドプッシュのイネーブルメントを有効にしているユーザー。これはプッシュサブスクリプションのステータスを考慮していない。この数には、仮にフォアグラウンドおよびバックグラウンドのプッシュトークンを暫定的に承認されたユーザーが含まれます。
    tags:
      - Channel subscription behavior
  - name: "Background or Foreground Push Enabled"
    description: ユーザーがプッシュトークンを持っており配信停止していないかどうかに基づいてセグメント化します。あなたのアプリのいずれかでバックグラウンドまたはフォアグラウンドプッシュをイネーブルしているユーザー。
    tags:
      - Channel subscription behavior
  - name: "Push Opt In Date"
    description: プッシュ通知をオプトインした日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: "Push Subscription Status"
    description: "ユーザーを<a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">サブスクリプション ステータス</a> でセグメント化してプッシュします。"
    tags:
      - Channel subscription behavior
  - name: "Push Unsubscribed Date"
    description: 今後のプッシュ通知を配信停止した日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: "Purchased Product"
    description: アプリで購入した商品ごとにユーザーを分割します。
    tags:
      - Purchase behavior
  - name: "Total Number of Purchases"
    description: アプリでの購入数によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: "X Product Purchased In Y Days"
    description: 指定の商品を購入した回数でユーザーをフィルターします。
    tags:
      - Purchase behavior
  - name: "X Purchases in Last Y Days"
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、購入を行った回数 (0 ～ 50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: "X Purchase Property In Y Days"
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、特定の購入プロパティに関連して購入を行った回数 (0 ～ 50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: "First Made Purchase"
    description: アプリ内で購入を行った最も早い時刻によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: "First Purchase For App"
    description: アプリから購入を行った最も早い時刻によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: "Last Made Purchase"
    description: 前回購入時までにユーザーを絞り込みます。
    tags: 
      - Purchase behavior
  - name: "Last Purchased Product"
    description: 特定の商品を最後に購入した時点でユーザーを絞り込みます。
    tags:
      - Purchase behavior
  - name: "Money Spent"
    description: アプリで費やした金額によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: "X Money Spent in Y Days"
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、アプリで費やした金額によってユーザーをセグメント化します。この金額は直近50回の購入の合計のみを含んでいる。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: "Last order placed (last 730 days)"
    description: "ユーザーを、最後に注文した時期でセグメント化する。これは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文完了」に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しない）。ユーザーはこのフィルターに対して1日1回評価され、最大遡及期間は過去2年間である。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total orders count (last 730 days)"
    description: "ユーザーを、過去2年間における注文総数でセグメント化する。<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">これはe コマース推奨イベント</a>「注文完了」に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しない）。この集計にはキャンセルされた注文は含まれない。キャンセルされた注文は、<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文キャンセル」を使用してトラッキングする必要がある。ユーザーはこのフィルターの評価を1日1回受ける。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total orders count"
    description: "ユーザーの生涯における注文総数に基づいてユーザーをセグメント化する。これは注文<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">確定のe コマース推奨イベント</a>に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しない）。この集計にはキャンセルされた注文は含まれない。キャンセルされた注文は、<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>「注文キャンセル」を使用してトラッキングする必要がある。ユーザーはこのフィルターに対してリアルタイムで評価される。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total canceled orders count (last 730 days)"
    description: "ユーザーを、過去2年間にキャンセルした注文の総数でセグメント化する。<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">これはe コマース推奨イベント</a>「注文成立」に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しない）。ユーザーはこのフィルターの評価を1日1回受ける。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Customer lifetime value (last 730 days)"
    description: "ユーザーを、そのユーザーが貴社ブランドとの購入履歴を通じて生み出すと予想される総収益によってセグメント化する。計算では過去730日間を対象とし、平均注文金額（AOV）を注文総数で乗算する。その後、ユーザーのアクティブな購入期間（初回注文から直近の注文までの期間）を考慮に入れる。このフィルターは<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨</a>イベントで追跡されたデータを使用する（e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しない）。ユーザーはこのフィルターの評価を1日1回受ける。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total refund value (last 730 days)"
    description: "ユーザーを、過去2年間に付与された返金額に基づいてセグメント化する。<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">これはe コマース推奨イベント</a>「注文返金」に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しない）。ユーザーはこのフィルターの評価を1日1回受ける。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total refund value"
    description: "ユーザーを、その生涯にわたって付与された返金総額に基づいてセグメント化する。<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">これはe コマース推奨イベント</a>「注文返金」に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しない）。ユーザーはこのフィルターに対してリアルタイムで評価される。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total revenue (last 730 days)"
    description: "ユーザーを、過去2年間の注文から生じた総収益額でセグメント化する。この収益額は、注文確定時の<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e</a> コマースイベントに関連する収益から、注文返金時の<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>に関連する収益を差し引いて算出される（e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しない）。ユーザーはこのフィルターの評価を1日1回受ける。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Total revenue"
    description: "ユーザーの生涯にわたる注文から生じた総収益に基づいてユーザーをセグメント化する。この収益は、注文確定時のe コマースイベントに関連する収益から、注文返金時の<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">e コマース推奨イベント</a>に関連する収益を差し引いて算出される（e コマースイベントをトラッキングしていないワークスペースでは、このフィルターのデータは存在しない）。ユーザーはこのフィルターに対してリアルタイムで評価される。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Average order value (last 730 days)"
    description: "ユーザーの過去2年間の注文平均額に基づいてユーザーをセグメント化する。<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">これはe コマース推奨イベント</a>「注文完了」に基づく（e コマースイベントをトラッキングしていないワークスペースでは、このフィルター用のデータは存在しない）。ユーザーはこのフィルターの評価を1日1回受ける。<br><br>このフィルターはベータ版だ。このフィルターを利用したい場合は、Brazeのアカウントマネージャーに連絡する。"
    tags:
      - eCommerce
  - name: "Country"
    description: ユーザーを最後に示された国の場所でセグメント化します。
    tags:
      - Demographic attributes
  - name: "City"
    description: 最後に示された市区町村の場所によってユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: "Language"
    description: ユーザーを好みの言語でセグメント化します。
    tags:
      - Demographic attributes
  - name: "Age"
    description: ユーザーをアプリ内で示した年齢によってセグメント化します。
    tags:
      - Demographic attributes
  - name: "Birthday"
    description: ユーザーをアプリ内で示した誕生日によってセグメント化します。<br> 2月29日が誕生日のユーザーは、3月1日を含むセグメントに含まれる。<br><br>12 月または 1 月の誕生日をターゲットにするには、ターゲットとする年の 12 か月の期間内のフィルターロジックのみを挿入してください。言い換えれば、前の暦年の12月を振り返るロジックや、翌年の1月までのフォワードロジックを挿入しないでください。たとえば、12 月の誕生日をターゲットにするには、「12 月 31 日」、「12 月 31 日の前」、または「11 月 30 日の後」でフィルタリングすることができます。
    tags:
      - Demographic attributes
  - name: "Gender"
    description: アプリ内から示されたとおり、ユーザーを性別でセグメント化します。
    tags:
      - Demographic attributes
  - name: "Unformatted Phone Number"
    description: フォーマットされていない電話番号でユーザーをセグメンテーションする。括弧、ダッシュ、その他の記号は含まない。
    tags:
      - Demographic attributes
  - name: "First Name"
    description: ユーザーをアプリ内で示した名によってセグメント化します。
    tags:
      - Demographic attributes
  - name: "Last Name"
    description: ユーザーをアプリ内で示した姓でセグメント化します。
    tags:
      - Demographic attributes
  - name: "Has App"
    description: ユーザーがアプリをインストールしたことがあるかどうかによって分割されます。これには、現在アプリをインストールしているユーザーと、過去にアンインストールしたユーザーが含まれる。通常、このフィルターに一致するには、ユーザーがアプリを開封する (セッションを開始する) 必要があります。ただし、ユーザーがBraze にインポートされ、アプリに手動で関連付けられた場合など、いくつかの例外があります。
    tags:
      - App
  - name: "Most Recent App Version Name"
    description: ユーザーのアプリの最新の名前によってセグメント化します。<br><br>「より小さい」または「以下」を使用する場合、メインアプリのバージョンが存在しない場合、このフィルターは`true`を返す。ユーザーがアプリバージョンより古いからである。これは、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致することを意味する。
    tags:
      - App
  - name: "Most Recent App Version Number"
    description: ユーザーのアプリの最新バージョン番号によってセグメント化します。<br><br>「より小さい」または「以下」を使用する場合、メインアプリのバージョンが存在しない場合、このフィルターは`true`を返す。ユーザーがアプリバージョンより古いからである。これは、ユーザーの最後のメインアプリバージョンが存在しない場合、自動的にフィルターに一致することを意味する。<br><br>現在のアプリバージョンが表示されるまで時間がかかるかもしれない。ユーザープロファイル上のアプリバージョンは、SDKが情報を取得した時点で更新される。これはユーザーがアプリを開封したタイミングに依存する。ユーザーがアプリを開封しない場合、現在のバージョンは更新されない。これらのフィルターは遡って適用されることもない。現在版や将来版に対しては「より大きい」や「等しい」を使うのが良いが、過去版のフィルターを使うと予期せぬ動作を引き起こす可能性がある。
    tags:
      - App
  - name: "Uninstalled"
    description: アプリをアンインストールした後、再インストールしていないかどうかによって、ユーザーをセグメント化します。
    tags:
      - Uninstall
  - name: "Device Carrier"
    description: デバイスの通信事業者によってユーザーをセグメント化します。
    tags:
      - Devices
  - name: "Device Count"
    description: アプリを使用したデバイスの数でユーザーをセグメント化します。
    tags:
      - Devices
  - name: "Device Model"
    description: 携帯電話機の機種別にユーザーを分割します。
    tags:
      - Devices
  - name: "Device OS"
    description: "指定のオペレーティングシステムを持つ 1 台以上のデバイスを持つユーザーをセグメント化します。ユーザーをオペレーティングシステムの種類でセグメントするには、<a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">デバイスOSバージョン番号</a>フィルターを使用する。"
    tags:
      - Devices
  - name: "Device OS Version Number"
    description: 指定された範囲内のオペレーティングシステムバージョンを持つデバイスを1台以上所有するユーザーをセグメント化する。例えば、iOSのオペレーティングシステムバージョンが26.0以上であるユーザーをターゲットにできる。
    tags:
      - Devices
  - name: "Most Recent Device Locale"
    description: "最後に使用した機器の<a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">ロケール情報</a>でユーザーを分割します。"
    tags:
      - Devices
  - name: "Most Recent Watch Model"
    description: ユーザーを最新のスマートウォッチモデルでセグメント化します。
    tags:
      - Devices
  - name: "Provisionally Authorized on iOS"
    description: iOS 12 で特定のアプリに対して暫定的に許可されているユーザーを検索できます。
    tags:
      - Devices
  - name: "Web Browser"
    description: Web サイトにアクセスするために使用するウェブブラウザによって、ユーザーをセグメント化します。
    tags:
      - Devices
  - name: "Device IDFA"
    description: テスト用のキャンペーン受信者を IDFA で指定できます。
    tags:
      - Advertising use cases
  - name: "Device IDFV"
    description: テスト用にIDFV でキャンペーン 受信者を指定できます。
    tags:
      - Advertising use cases
  - name: "Device Google Ad ID"
    description: ユーザーをグーグルの広告ID でセグメント化します。
    tags:
      - Advertising use cases
  - name: "Device Roku Ad ID"
    description: ユーザーを Roku 広告 ＩＤ でセグメント化します。
    tags:
      - Advertising use cases
  - name: "Device Windows Ad ID"
    description: ユーザーをWindows アドID でセグメント化します。
    tags:
      - Advertising use cases
  - name: "Ad Tracking Enabled"
    description: ユーザーが広告の追跡をオプトインしているかどうかに基づいてフィルターできます。広告の追跡は IDFA または Apple によってすべての iOS 機器に割り当てられている「広告主用の識別子」に関連します。これは SDK によって設定できます。この識別子により、広告主はユーザーを追跡し、ターゲット広告を提供することができます。
    tags:
      - Advertising use cases
  - name: "Most Recent Location"
    description: ユーザーを、アプリを使用した最後に記録された場所でセグメント化します。
    tags:
      - Location
  - name: "Location Available"
    description: "ユーザーの位置がレポートされているかどうかによって、それらをセグメント化します。このフィルターを使用するには、アプリに<a href=\"/docs/search/?query=location%20tracking\">位置情報の追跡が統合</a>されている必要があります。"
    tags:
      - Location
  - name: "Amplitude Cohorts"
    description: Amplitude を使用するクライアントは、Amplitude でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Census Cohorts"
    description: Census を使用するクライアントは、Census でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Heap Cohorts"
    description: Heap を使用するクライアントは、Heap 内のコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Hightouch Cohorts"
    description: Hightouch を使用するクライアントは、Hightouch でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Kubit Cohorts"
    description: Kubit を使用するクライアントは、Kubit でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Mixpanel Cohorts"
    description: Mixpanel を使用するクライアントは、Mixpanel でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Segment Cohorts"
    description: Segment を使用するクライアントは、Segment でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Tinyclues Cohorts"
    description: Tinyclues を使用するクライアントは、Tinyclues でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: "Install Attribution Ad"
    description: インストールアトリビューションとなった広告によってユーザーをセグメント化します。
    tags:
      - User Attributes
  - name: "Install Attribution Adgroup"
    description: インストールアトリビューションとなった広告グループによってユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: "Install Attribution Campaign"
    description: インストール先が属性である広告キャンペーンによって、ユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: "Install Attribution Source"
    description: インストールアトリビューションとなったソースによってユーザーをセグメント化します。
    tags:
      - Install attribution
  - name: "Churn Risk Category"
    description:  ユーザーを、具体的な予測に応じて、解約リスクカテゴリ別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: "Churn Risk Score"
    description: ユーザーを、具体的な予測に応じて、チャーンリスクスコア別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: "Event Likelihood Category"
    description: ユーザーを、特定の予測に従ってイベントを実行する可能性によってセグメント化します。
    tags:
      - Intelligence and predictive
  - name: "Event Likelihood Score"
    description: ユーザーを、特定の予測に従ってイベントを実行する可能性によってセグメント化します。
    tags:
      - Intelligence and predictive
  - name: "Intelligent Channel"
    description: 過去3 カ月間で最も有効なチャネルごとにユーザーを分割します。
    tags:
      - Intelligence and predictive
  - name: "Message Open Likelihood"
    description: "<a href=\"/docs/user_guide/brazeai/intelligence/intelligent_channel/#individual-channels\">指定したチャネルでメッセージを開封</a>する可能性を0～100％の尺度で評価し、それに基づいてユーザーをフィルタリングする。チャネルの可能性を測定するのに十分なデータがないユーザーは、「空白である」を使用して選択できます。<br><br>メールの場合、機械による開封は可能性の計算から除外される。"
    tags:
      - Intelligence and predictive
  - name: "Number of Facebook Friends Using App"
    description: 同じアプリを使用している Facebook の友達の人数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: "Connected Facebook"
    description: アプリを Facebook に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: "Connected Twitter"
    description: アプリをX(以前のTwitter)に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: "Number of Twitter Followers"
    description: ユーザーをX (以前のTwitter) フォロワーの数でセグメント化します。
    tags:
      - Social activity
  - name: "Phone Number"
    description: "E.164形式の電話番号フィールドでユーザーをセグメンテーションする。<br><br> 電話番号がBrazeに送信されると、BrazeはそれをSMSやWhatsAppチャネルで使用される<a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">e.164</a>フォーマットに変換しようとする。番号が適切にフォーマットされていない場合、強制処理は失敗する可能性がある。その結果、ユーザープロファイルはフォーマットされていない電話番号を持つが、送信電話番号は持たないことになる。このセグメントフィルターは、e.164形式の電話番号 (利用可能な場合) でユーザーを返します。<br><br>ユースケース:<br> - SMSやWhatsAppメッセージを送信する際、このフィルターを使って最も正確なターゲットオーディエンスのサイズを把握しよう。 <br>- このフィルターで正規表現（regex）を使って、特定の国コードを持つ電話番号をセグメンテーションする。<br>- このフィルターを使用して、e.164強制処理に失敗した電話番号でユーザーをセグメンテーションする。"
    tags:
      - Other Filters
---
