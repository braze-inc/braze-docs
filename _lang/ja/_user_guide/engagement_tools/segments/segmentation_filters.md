---
page_order: 1.2
nav_title: セグメンテーションフィルター
article_title: セグメンテーションフィルター
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "この用語集には、ユーザーをセグメント化およびターゲット化するための使用可能なフィルターが一覧表示されています。"
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: セグメントまたはCSVメンバーシップ
  - name: カスタム属性
  - name: カスタムイベント
  - name: セッション
  - name: リターゲット
  - name: チャンネルサブスクリプションの動作
  - name: 購買行動
  - name: 人口統計属性
  - name: アプリ
  - name: Uninstall
  - name: デバイス
  - name: ロケーション
  - name: コホート会員
  - name: アトリビューションのインストール
  - name: インテリジェンスと予測
  - name: 社会活動
  - name: その他のフィルタ

glossaries:
  - name: セグメントのメンバーシップ
    description: フィルターが使用されている任意のセグメントメンバーシップ (セグメントやキャンペーンなど) に基づいてフィルターし、1 つのキャンペーン内で複数の異なるセグメントをターゲットにすることができます。<br><br>すでにこのフィルターを使用しているセグメントは、他のセグメントに追加しり、ネストしたりできないことに注意してください。同じフィルターを使用して、含めるセグメントを再作成する必要があります。
    tags:
      - Segment or CSV membership
  - name: Braze のセグメントエクステンション
    description: セグメントエクステンションを Braze ダッシュボードで作成した後、それらのエクステンションをセグメントに含めたり除外したりできます。
    tags:
      - Segment or CSV membership
  - name: CSV から更新/インポート
    description: CSV アップロードの一部であるかどうかに基づいてユーザーをセグメント化します。
    tags:
      - Segment or CSV membership
  - name: カスタム属性
    description: "ユーザーが、記録されたカスタム属性値と一致するかどうかを決定します。(24時間) <br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom attributes
  - name: 階層化カスタム属性
    description: "カスタム属性のプロパティである属性。<br><br>階層化された時間のカスタム属性にフィルターを適用する場合、基準として [年間通算日] または [時刻] を選択できます。[年間通算日] では、比較対象として月と日のみがチェックされます。[時刻] では、年を含むタイムスタンプ全体が比較されます。"
    tags:
      - Custom attributes
  - name: 定期的なイベントの日
    description: "このフィルターでは、データタイプが\"date\"のカスタム属性の月と日を調べますが、年は調べません。このフィルターは毎年発生するイベントに役立ちます。<br><br>タイムゾーン:<br>このフィルターは、ユーザーがどのタイムゾーンにあるかを調整します。"
    tags:
      - Custom attributes
  - name: カスタムイベント
    description: "ユーザーが特別に記録された行動を実行したかどうかを決定します。<br><br> 例: <br>プロパティ activty_name で完了したアクティビティー。<br><br>タイムゾーン:<br>UTC - 暦日 = 1 暦日は、ユーザー履歴の 24 ～ 48 時間を含みます"
    tags:
      - Custom events
  - name: 最初にカスタムイベントを実行した
    description: "ユーザーが特別に記録された行動を実行した最も早い時刻を決定します。(24時間) <br><br>例: <br> 初回のカート放棄が過去 1 日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: 最後に実行したカスタムイベント 
    description: "ユーザーが特別に記録された行動を最後に実行した時刻を決定します。(24時間) <br><br>例: <br> 最後のカート放棄が過去 1 日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: X Y日間のカスタムイベント
    description: "ユーザーが、最後に指定された暦日数 (1 ～ 30 日) の間に、特別に記録されたイベントを 0 ～ 50 回実行したかどうかを決定します。(暦日 = 1 暦日は、ユーザー履歴の 24 ～ 48 時間を含みます)<br> <a href=\"/docs/x-in-y-behavior/\"> ここでは、X-in-Y の動作について詳しく説明します。</a><br><br>例: <br>過去 1 暦日内にカートをちょうど 0 回放棄した<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンを考慮すると、1 暦日はユーザー履歴の24 ～48 時間を、Segmentが評価される時刻に応じて、2 暦日はユーザー履歴の48 ～72 時間を、などと表示します。"
    tags:
      - Custom events
  - name: X Y 日間のカスタムイベントプロパティ
    description: "ユーザーが、最後に指定された暦日数 (1 ～ 30 日) の間に、特別に記録されたイベントを特定のプロパティについて 0 ～ 50 回実行したかどうかを決定します。(暦日 = 1 暦日は、ユーザー履歴の 24 ～ 48 時間を含みます)<br><a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a><br><br>例: <br> 過去 1 暦日内にカートをちょうど 0 回お気に入りに追加した<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンを考慮すると、1 暦日はユーザー履歴の24 ～48 時間を、Segmentが評価される時刻に応じて、2 暦日はユーザー履歴の48 ～72 時間を、などと表示します。"
    tags:
      - Custom events
  - name: 電子メールアドレス 
    description: テスト用に個々のメールアドレスによってキャンペーン 受信者を指定できます。これは、「メールアドレスが空白でない」指定子を使用して、トランザクションメールをすべてのユーザー (配信停止済みユーザーを含む) に送信するためにも使用できます。
    tags:
      - Other Filters
  - name: 外部ユーザーID
    description: テストのために、キャンペーン受信者を個々のユーザー ID で指定することができます。
    tags:
      - Other Filters
  - name: "ランダムバケット番号"
    description: ユーザーをランダムに割り当てられた番号(0～9999を含む)でセグメント化します。これにより、AB テストと多変量テストに対する真のランダムユーザーの一様分布セグメントを生成できるようになります。
    tags:
      - Other Filters
  - name: セッション数
    description: ユーザーをワークスペース内のいずれかのアプリでこれまでに行ったセッション数でセグメント化します。
    tags:
      - Sessions
  - name: アプリのセッション数
    description: 指定されたアプリ内でこれまでに行ったセッション数によってユーザーをセグメント化します。
    tags:
      - Sessions
  - name: 過去 Y 日間の X 回のセッション
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、貴社のアプリで行ったセッション数 (0 ～ 50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Sessions
  - name: 最初に使用したアプリ
    description: "アプリを開封した記録の最も早い時刻によってユーザーをセグメント化します。<em>これは、ユーザーが Braze SDK を統合したアプリを使用した最初のセッションをキャプチャすることに注意してください。</em>(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: 最初に使用した特定のアプリ
    description: "ワークスペース内の任意のアプリを開封した記録の最も早い時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: 最後に使用したアプリ
    description: "アプリを開封した最後の時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: 特定のアプリの最終使用
    description: "指定されたアプリを開封した最後の時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: セッション時間の中央値
    description: アプリ内のセッションの長さの中央値によってユーザーをセグメント化します。
    tags:
      - Sessions
  - name: キャンペーンから受信したメッセージ
    description: "指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: キャンペーンバリアントを受信
    description: "受信した多変量キャンペーンのバリアントによってユーザーをセグメント化します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: キャンバスステップからメッセージを受信
    description: "特定のキャンバスコンポーネントを受信したかどうかによってユーザーをセグメント化します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: 特定のキャンバスステップから最後に受信したメッセージ
    description: 特定のキャンバスコンポーネントを受信した日時によってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: 特定のキャンペーンから最後に受信したメッセージ
    description: 指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: キャンペーンまたはキャンバスからタグ付きで受信したメッセージ
    description: "指定したキャンペーンを受信したかどうか、または指定したタグのキャンバスを受信したかどうかによって、ユーザーを分割します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: キャンペーンまたはCanvas With Tagから最後に受信したメッセージ
    description: 特定のタグを持つ特定のキャンペーンまたはキャンバスを受信した日時によってユーザーをセグメント化します。(24時間)
    tags:
      - Retargeting
  - name: キャンペーンステップまたはキャンバスステップからメッセージを受信していない
    description: キャンペーンまたはキャンバスコンポーネントを受信したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: 最後に受信したメール
    description: "最後にメールを受信したときに、ユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後に受信したプッシュ
    description: "ユーザーを最後にプッシュ通知s のいずれかを受信したときにセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後のアプリ内メッセージインプレッション
    description: ユーザーを最後にアプリ内メッセージを表示したときにセグメント化します。
    tags:
      - Retargeting
  - name: 最後に受信した SMS
    description: "最後のメッセージがSMSプロバイダーに配信された時刻までにユーザーをセグメント化します。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後に受信した Webhook
    description: "ユーザーを、BrazeがそのユーザーのWebhookを最後に送信した時刻までに分割します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後に受信した WhatsApp
    description: "最後にWhatsAppを受信したときに、ユーザーをセグメント化します。これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後に閲覧したニュースフィード
    description: 最後にニュースフィードを表示したときに、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: ニュースフィードの閲覧数
    description: ニュースフィードを表示した何回によってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: クリックされた/開封されたキャンペーン
    description: "特定のキャンペーンとのインタラクションでフィルタリングします。<br><br> メールとして、複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーs が受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーは、指定のキャンペーンから、ユーザーのクリック追跡が有効になっている SMS メッセージ内の短縮リンクを最後に選択しました。"
    tags:
      - Retargeting
  - name: クリック/開いたキャンペーンまたはタグ付きキャンバス
    description: "特定のタグを持つ特定のキャンペーンとのインタラクションでフィルタリングします。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーs が受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーがタグを持つ指定のキャンペーンまたはキャンバスステップから、ユーザーのクリック追跡が有効になっている SMS メッセージ内の短縮リンクを最後に選択した日時。"
    tags:
      - Retargeting
  - name: クリックされた/開封されたステップ
    description: 特定のキャンバスコンポーネントとのインタラクションでフィルタリングします。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーs が受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーは、指定のキャンバスステップから、ユーザーのクリック追跡が有効になっている SMS メッセージ内の短縮リンクを最後に選択しました。
    tags:
      - Retargeting
  - name: キャンペーンでクリックしたエイリアス
    description: "指定したキャンペーンの特定の別名をクリックしたかどうかによって、ユーザーをフィルタリングします。これはメールメッセージだけに適用されます。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: キャンバスステップでクリックしたエイリアス
    description: "特定のキャンバスで特定のエイリアスをクリックしたかどうかによって、ユーザーをフィルタリングします。これはメールメッセージだけに適用されます。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: キャンペーンステップまたはキャンバスステップでクリックしたエイリアス
    description: "ユーザーを、任意のキャンペーンまたはキャンバス内で特定のエイリアスをクリックしたかどうかによってフィルタリングします。これはメールメッセージだけに適用されます。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーのプロファイルも更新されます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封/クリックをまだ行っていない場合、元のユーザーではなく、そのメールアドレスを持つすべての残りのユーザーに開封またはクリックが適用されます。"
    tags:
      - Retargeting
  - name: ハードバウンス
    description: ユーザーを、メールアドレスがハードバウンスされたかどうか (メールアドレスが不正な場合など) によってセグメント化します。
    tags:
      - Retargeting
  - name: スパムとしてマークされた
    description: メッセージをスパムとしてマークしたかどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: 不正な電話番号 
    description: 電話番号が不正かどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: 最後に送信された特定の SMS インバウンドキーワードカテゴリ
    description: 特定のキーワードカテゴリ内の特定のサブスクリプショングループにSMSを最後に送信したときに、ユーザーをセグメント化します。 
    tags:
      - Retargeting
  - name: キャンペーンからコンバージョン済み
    description: 特定のキャンペーンでコンバージョンしたかどうかによってユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: キャンバスからコンバージョン済み
    description: 特定のキャンバスでコンバージョンしたかどうかによってユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: キャンペーンのコントロールグループ内
    description: ユーザーを、指定した多変量 キャンペーンのコントロールグループにあるかどうかによってセグメント化します。
    tags:
      - Retargeting
  - name: キャンバスのコントロールグループ内
    description: ユーザーを、指定したキャンバスのコントロールグループにあるかどうかによって分割します。このフィルターは、キャンバスに入ったユーザーのみを評価します。<br><br>たとえば、キャンバスのユーザーをフィルターすると、キャンバスに入ったがコントロールグループには入っていないすべてのユーザーが表示されます。
    tags:
      - Retargeting
  - name: 任意のコントロールグループに最後に登録された
    description: "キャンペーンで最後にコントロールグループに割り当てられた時刻によってユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 入力したキャンバスバリエーション
    description: 特定のキャンバスのバリエーションパスを入力したかどうかによって、ユーザーをセグメント化します。このフィルターはすべてのユーザーs を評価します。<br><br>たとえば、キャンバスのバリエーションコントロールグループを入力していないユーザーをフィルターすると、キャンバスに入力したかどうかに関係なく、コントロールグループにないすべてのユーザーが表示されます。
    tags:
      - Retargeting
  - name: メッセージの最終受信
    description: "最後に受信したメッセージを判別して、ユーザーをセグメント化します。(24時間)<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが最後に送信されたときではなく、ユーザーが最後にインプレッションを記録したときです。<br><br>プッシュおよびwebhookの場合、これは、任意のメッセージがユーザーに送信されたときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されたときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されたときです。<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。<br><br>例: <br>前回受信メール1日未満=24時間未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: メッセージへの最終エンゲージ
    description: "メッセージングチャネルのいずれか (コンテンツカード、メール、アプリ内、SMS、プッシュ通知、WhatsApp) を最後にクリックまたは開封した日時によって、ユーザーをセグメント化します。マシン開封数またはメールのその他の開封数でフィルタリングするオプションが含まれています。(24時間)<br><br>メールの場合、メールリクエストが (実際に配信されたかどうかに関係なく) メールサービスプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新されます。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、ユーザークリック\"トラッキングが有効になっているメッセージ内の短縮リンクを最後に選択したユーザー。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: クリックされたカード 
    description: 特定のコンテンツカードをクリックしたかどうかによってユーザーをセグメント化します。このフィルターは、「キャンペーンをクリック/開封」、「タグ付きのキャンペーンまたはキャンバスをクリック/開封」、および「ステップをクリック/開封」のサブフィルターとして使用できます。
    tags:
      - Retargeting
  - name: フィーチャーフラグ
    description: "現在有効になっている特定の<a href=\"/docs/developer_guide/platform_wide/feature_flags/about\">フィーチャーフラグ</a>を持つユーザーのSegment。"
    tags:
      - Retargeting
  - name: サブスクリプショングループ
    description: メール、SMS/MMS、またはWhatsAppのサブスクリプショングループでユーザーを分割します。アーカイブ済みグループは表示されず、使用できません。
    tags:
      - Channel subscription behavior
  - name: 利用可能なメール
    description: ユーザーを、有効なメールアドレスを持っているかどうか、およびメールにサブスクライブ/オプトインしているかどうかによってセグメント化します。「メールが利用可能」フィルターは、ユーザーがメールを配信停止したかどうか、Braze がハードバウンスを受信したかどうか、およびスパムとしてマークされたかどうかの 3 つの基準を確認します。これらの基準のいずれかが満たされている場合、またはメールがユーザーに存在しない場合、ユーザーは含まれません。
    tags:
      - Channel subscription behavior
  - name: メールオプトイン日
    description: メールをオプトインした日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: メールサブスクリプションステータス
    description: メールの購読ステータスによってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: メールの配信停止日 
    description: 今後のメールを配信停止した日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: プッシュ通知が有効
    description: 暫定的なプッシュ認証があるか、フォアグラウンドプッシュが有効になっているユーザーをセグメント化します。具体的には、このカウントには以下が含まれます。<br>1. 暫定的にプッシュが承認されている iOS ユーザー。<br>2.ワークスペース内の任意のアプリに対してプッシュ通知を明示的にアクティブ化したユーザー。これらのユーザーの場合、この数にはフォアグラウンドプッシュのみが含まれます。<br><br>「プッシュ通知が有効」には、配信停止済みのユーザーは含まれません。<br><br>このSegmentでフィルターを実行すると、<em>Reachable Users</em> という名前のAndroid、iOS、ウェブサイトのユーザーの内訳が下部に表示されます。
    tags:
      - Channel subscription behavior
  - name: アプリのプッシュ有効化
    description: デバイス上のアプリでプッシュ通知を有効にしているかどうかによってユーザーをセグメント化します。これらのユーザーはプッシュで到達可能ですが、オプトインされない可能性があります。この数には、仮にフォアグラウンドおよびバックグラウンドのプッシュトークンを暫定的に承認されたユーザーが含まれます。
    tags:
      - Channel subscription behavior
  - name: バックグラウンドプッシュ有効
    description: バックグラウンドプッシュが有効になっているかどうかに基づいて、ユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: プッシュ通知のオプトイン日
    description: プッシュ通知をオプトインした日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: プッシュ通知のサブスクリプションのステータス
    description: "ユーザーを<a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">サブスクリプション ステータス</a> でセグメント化してプッシュします。"
    tags:
      - Channel subscription behavior
  - name: プッシュ通知の配信停止日
    description: 今後のプッシュ通知を配信停止した日付によってユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: 購入した製品
    description: アプリで購入した商品ごとにユーザーを分割します。
    tags:
      - Purchase behavior
  - name: 購入数の合計
    description: アプリでの購入数によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: Y 日間に購入した製品 X
    description: 指定の商品を購入した回数でユーザーをフィルターします。
    tags:
      - Purchase behavior
  - name: 過去 Y 日間の X 回の購入
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、購入を行った回数 (0 ～ 50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: X Y日以内に物件を購入
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、特定の購入プロパティに関連して購入を行った回数 (0 ～ 50 回) によってユーザーをセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: 最初に行った購入
    description: アプリ内で購入を行った最も早い時刻によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: アプリでの最初の購入
    description: アプリから購入を行った最も早い時刻によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: 前回購入
    description: 前回購入時までにユーザーを絞り込みます。
    tags: 
      - Purchase behavior
  - name: 最後に購入した製品
    description: 特定の商品を最後に購入した時点でユーザーを絞り込みます。
    tags:
      - Purchase behavior
  - name: 支出金額
    description: アプリで費やした金額によってユーザーをセグメント化します。
    tags:
      - Purchase behavior
  - name: X 日間に支出した金額
    description: "最後に指定された暦日数 (1 ～ 30 日) の間に、アプリで費やした金額によってユーザーをセグメント化します。この金額には、最後の50 回の購入の合計のみが含まれます。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: 国
    description: ユーザーを最後に示された国の場所でセグメント化します。
    tags:
      - Demographic attributes
  - name: 市区町村
    description: 最後に示された市区町村の場所によってユーザーをセグメント化します。
    tags:
      - Demographic attributes
  - name: 言語
    description: ユーザーを好みの言語でセグメント化します。
    tags:
      - Demographic attributes
  - name: 年齢
    description: ユーザーをアプリ内で示した年齢によってセグメント化します。
    tags:
      - Demographic attributes
  - name: 生年月日
    description: ユーザーをアプリ内で示した誕生日によってセグメント化します。<br> 2 月 29 日に誕生日を迎えるユーザーは、3 月 1 日を含むセグメントに含まれます。<br><br>12 月または 1 月の誕生日をターゲットにするには、ターゲットとする年の 12 か月の期間内のフィルターロジックのみを挿入してください。言い換えれば、前の暦年の12月を振り返るロジックや、翌年の1月までのフォワードロジックを挿入しないでください。たとえば、12 月の誕生日をターゲットにするには、「12 月 31 日」、「12 月 31 日の前」、または「11 月 30 日の後」でフィルタリングすることができます。
    tags:
      - Demographic attributes
  - name: 性別
    description: アプリ内から示されたとおり、ユーザーを性別でセグメント化します。
    tags:
      - Demographic attributes
  - name: 電話番号
    description: "ユーザーを電話番号でセグメント化します。数字[0-9]のみを使用してください。括弧、ダッシュなどは使用しないでください。"
    tags:
      - Demographic attributes
  - name: 名
    description: ユーザーをアプリ内で示した名によってセグメント化します。
    tags:
      - Demographic attributes
  - name: 姓
    description: ユーザーをアプリ内で示した姓でセグメント化します。
    tags:
      - Demographic attributes
  - name: アプリあり
    description: ユーザーがアプリをインストールしたことがあるかどうかによって分割されます。これには、現在アプリがインストールされているユーザーと、以前にアンインストールされたものが含まれます。通常、このフィルターに一致するには、ユーザーがアプリを開封する (セッションを開始する) 必要があります。ただし、ユーザーがBraze にインポートされ、アプリに手動で関連付けられた場合など、いくつかの例外があります。
    tags:
      - App
  - name: 最新のアプリバージョン名
    description: ユーザーのアプリの最新の名前によってセグメント化します。
    tags:
      - App 
  - name: 最新のアプリバージョン番号
    description: ユーザーのアプリの最新バージョン番号によってセグメント化します。
    tags:
      - App 
  - name: アンインストール
    description: アプリをアンインストールした後、再インストールしていないかどうかによって、ユーザーをセグメント化します。
    tags:
      - Uninstall 
  - name: デバイスの通信事業者
    description: デバイスの通信事業者によってユーザーをセグメント化します。
    tags:
      - Devices
  - name: デバイス数
    description: アプリを使用したデバイスの数でユーザーをセグメント化します。
    tags:
      - Devices
  - name: デバイスモデル
    description: 携帯電話機の機種別にユーザーを分割します。
    tags:
      - Devices
  - name: デバイス OS
    description: 指定のオペレーティングシステムを持つ 1 台以上のデバイスを持つユーザーをセグメント化します。
    tags:
      - Devices
  - name: 最新のデバイスロケール
    description: "最後に使用した機器の<a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">ロケール情報</a>でユーザーを分割します。"
    tags:
      - Devices      
  - name: 最新のウォッチモデル
    description: ユーザーを最新のスマートウォッチモデルでセグメント化します。
    tags:
      - Devices    
  - name: iOS で暫定的に承認済み
    description: iOS 12 で特定のアプリに対して暫定的に許可されているユーザーを検索できます。
    tags:
      - Devices   
  - name: Webブラウザー
    description: Web サイトにアクセスするために使用するウェブブラウザによって、ユーザーをセグメント化します。
    tags:
      - Devices
  - name: デバイスIDFA
    description: テスト用のキャンペーン受信者を IDFA で指定できます。
    tags:
      - Advertising use cases
  - name: デバイス IDFV
    description: テスト用にIDFV でキャンペーン 受信者を指定できます。
    tags:
      - Advertising use cases 
  - name: デバイスの Google 広告 ID
    description: ユーザーをグーグルの広告ID でセグメント化します。
    tags:
      - Advertising use cases
  - name: デバイスの Roku 広告 ID
    description: ユーザーを Roku 広告 ＩＤ でセグメント化します。
    tags:
      - Advertising use cases
  - name: デバイスのWindows Ad ID
    description: ユーザーをWindows アドID でセグメント化します。
    tags:
      - Advertising use cases  
  - name: 広告の追跡が有効
    description: ユーザーが広告の追跡をオプトインしているかどうかに基づいてフィルターできます。広告の追跡は IDFA または Apple によってすべての iOS 機器に割り当てられている「広告主用の識別子」に関連します。これは SDK によって設定できます。この識別子により、広告主はユーザーを追跡し、ターゲット広告を提供することができます。
    tags:
      - Advertising use cases
  - name: 最新の場所
    description: ユーザーを、アプリを使用した最後に記録された場所でセグメント化します。
    tags:
      - Location
  - name: 利用可能な場所
    description: "ユーザーの位置がレポートされているかどうかによって、それらをセグメント化します。このフィルターを使用するには、アプリに<a href=\"/docs/search/?query=location%20tracking\">位置情報の追跡が統合</a>されている必要があります。"
    tags:
      - Location
  - name: Amplitude コホート
    description: Amplitude を使用するクライアントは、Amplitude でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Census コホート
    description: Census を使用するクライアントは、Census でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Heap コホート
    description: Heap を使用するクライアントは、Heap 内のコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Hightouch コホート
    description: Hightouch を使用するクライアントは、Hightouch でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Kubitコホート
    description: Kubit を使用するクライアントは、Kubit でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Mixpanel コホート
    description: Mixpanel を使用するクライアントは、Mixpanel でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: セグメントコホート
    description: Segment を使用するクライアントは、Segment でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: Tinyclues コホート
    description: Tinyclues を使用するクライアントは、Tinyclues でコホートを選択してインポートすることで、セグメントを補完できます。
    tags:
      - Cohort membership
  - name: インストールアトリビューション広告
    description: インストールアトリビューションとなった広告によってユーザーをセグメント化します。
    tags:
      - User Attributes
  - name: インストールアトリビューション広告グループ
    description: インストールアトリビューションとなった広告グループによってユーザーをセグメント化します。
    tags:
      - Install Attribution
  - name: インストールアトリビューションキャンペーン
    description: インストール先が属性である広告キャンペーンによって、ユーザーs をセグメント化します。
    tags:
      - Install Attribution
  - name: インストールアトリビューションソース
    description: インストールアトリビューションとなったソースによってユーザーをセグメント化します。
    tags:
      - Install Attribution
  - name: 解約リスクカテゴリ
    description:  ユーザーを、具体的な予測に応じて、解約リスクカテゴリ別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: 解約リスクスコア
    description: ユーザーを、具体的な予測に応じて、チャーンリスクスコア別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: 事象発生可能性区分
    description: ユーザーを、特定の予測に従ってイベントを実行する可能性によってセグメント化します。
    tags:
      - Intelligence and predictive
  - name: イベント尤度スコア
    description: ユーザーを、特定の予測に従ってイベントを実行する可能性によってセグメント化します。
    tags:
      - Intelligence and predictive
  - name: インテリジェントチャネル
    description: 過去3 カ月間で最も有効なチャネルごとにユーザーを分割します。
    tags:
      - Intelligence and predictive
  - name: メッセージ開封の可能性
    description: 指定したチャネルに0 ～100% の範囲で開封する可能性に基づいてユーザーをフィルタリングします。チャネルの可能性を測定するのに十分なデータがないユーザーは、「空白である」を使用して選択できます。
    tags:
      - Intelligence and predictive
  - name: アプリを使用している Facebook の友達の人数
    description: 同じアプリを使用している Facebook の友達の人数でユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Facebook でつながりがある
    description: アプリを Facebook に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Twitter でつながりがある
    description: アプリをX(以前のTwitter)に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Twitterフォロワー数
    description: ユーザーをX (以前のTwitter) フォロワーの数でセグメント化します。
    tags:
      - Social activity
  - name: 送信電話番号
    description: "e.164 送信電話番号フィールドでユーザーをセグメント化します。<br><br>電話番号がBrazeに送信されると、BrazeはそれをSMSやWhatsAppチャネルで使用される<a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">e.164</a>フォーマットに変換しようとする。番号が適切にフォーマットされていない場合、強制処理は失敗する可能性がある。その結果、ユーザープロファイルは電話番号を持つが、送信電話番号は持たないことになる。<br><br>ユースケース:<br> - このフィルターで正規表現（regex）を使って、特定の国コードを持つ電話番号をセグメンテーションする。<br>- このフィルターを使用して、e.164強制処理に失敗した電話番号でユーザーをセグメンテーションする。"
    tags:
      - Other filters
---
