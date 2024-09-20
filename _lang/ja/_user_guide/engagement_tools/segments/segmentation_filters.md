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
  - name: セッション数
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
  - name: 情報と予知
  - name: 社会活動
  - name: その他のフィルタ

glossaries:
  - name: セグメント会員数
    description: フィルター s が使用されているSegmentメンバーシップ(Segment s、キャンペーン s など) に基づいてフィルターし、1 つのキャンペーン内で複数の異なるs を対象とすることができます。<br><br>Segmentsがすでにこのフィルターを使用している場合、他のSegmentsに追加またはネストできないことに注意してください。同じフィルターs を使用して、含めるSegmentを再作成する必要があります。
    tags:
      - Segment or CSV membership
  - name: Braze分野
    description: Segment拡張をBraze ダッシュボードに作成した後、それらの拡張をSegmentに含める/除外することができます。
    tags:
      - Segment or CSV membership
  - name: CSV から更新/インポート
    description: CSV アップロードの一部であるかどうかに基づいて、ユーザーをセグメント化します。
    tags:
      - Segment or CSV membership
  - name: カスタム属性
    description: "ユーザーが個別に記録された属性と一致するかどうかを決定します。(24時間) <br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom attributes
  - name: 階層化カスタム属性
    description: "カスタム属性s のプロパティーである属性s。<br><br>階層化された時間のカスタム属性にフィルターを適用する場合、基準として [年間通算日] または [時刻] を選択できます。[年間通算日] では、比較対象として月と日のみがチェックされます。[時刻] では、年を含むタイムスタンプ全体が比較されます。"
    tags:
      - Custom attributes
  - name: 定期的なイベントの日
    description: "このフィルターでは、データタイプが\"date\"のカスタム属性の月と日を調べますが、年は調べません。このフィルターは年中行事に役立つ。<br><br>タイムゾーン:<br>このフィルターは、ユーザーがどのタイムゾーンにあるかを調整します。"
    tags:
      - Custom attributes
  - name: カスタムイベント
    description: "ユーザーが特別に録音された行動を実行したかどうかを決定します。<br><br> 例: <br>プロパティ activty_name で完了したアクティビティー。<br><br>タイムゾーン:<br>UTC - カレンダ日= 1 暦日は、ユーザー履歴の24 ～48 時間を表示します"
    tags:
      - Custom events
  - name: 最初にカスタムイベントを実行した
    description: "ユーザーが特別に録音された行動を実行した最も早い時刻を決定します。(24時間) <br><br>例: <br> 1日前に放棄されたカート<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: 前回のカスタムイベント 
    description: "ユーザーが特別に録音された行動を最後に実行した時刻を決定します。(24時間) <br><br>例: <br> 前回放棄されたカート1日未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Custom events
  - name: X Y日間のカスタムイベント
    description: "ユーザーが、最後に指定されたカレンダ日数の0～50 回の間に、特別に記録されたイベントを1～30 日の間で実行したかどうかを決定します。(暦日= 1 暦日はユーザー履歴の24 ～48 時間を表示します)<br> <a href=\"/docs/x-in-y-behavior/\"> ここでは、X-in-Y の動作について詳しく説明します。</a><br><br>例: <br>最後の1 暦日にカートをちょうど0 回放棄した<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンを考慮すると、1 暦日はユーザー履歴の24 ～48 時間を、Segmentが評価される時刻に応じて、2 暦日はユーザー履歴の48 ～72 時間を、などと表示します。"
    tags:
      - Custom events
  - name: X Y 日間のカスタムイベントプロパティ
    description: "ユーザーが、1 から30 までの最後に指定されたカレンダ日数の0 から50 回の間の指定されたプロパティに関して、特別に記録されたイベントを実行したかどうかを決定します。(暦日= 1 暦日はユーザー履歴の24 ～48 時間を表示します)<br><a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a><br><br>例: <br> お気に入りに追加されましたw/プロパティ\"event_name\"最後の1 暦日で正確に0 回<br><br>タイムゾーン:<br>UTC - すべてのタイムゾーンを考慮すると、1 暦日はユーザー履歴の24 ～48 時間を、Segmentが評価される時刻に応じて、2 暦日はユーザー履歴の48 ～72 時間を、などと表示します。"
    tags:
      - Custom events
  - name: 電子メールアドレス 
    description: "テスト用の個々のメールアドレスによってキャンペーン 受信者s を指定できます。これは、&amp;quot を使用して、トランスアクション al メール s をすべてのユーザーs (配信停止d を含む) に送信するためにも使用できます。メール Address is not Blank\" specifier in the フィルター."
    tags:
      - Other Filters
  - name: 外部ユーザーID
    description: テストのために、キャンペーン 受信者sを個々のユーザー IDsで指定することができます。
    tags:
      - Other Filters
  - name: "ランダムバケット番号"
    description: ユーザーをランダムに割り当てられた番号(0～9999を含む)でセグメント化します。それは、A/Bと多変量テストに対する真の乱数ユーザーsの均一に分布したSegmentsの生成を可能にする。
    tags:
      - Other Filters
  - name: セッション数
    description: ユーザーs を、ワークスペース内のアプリs のどれかに含まれていたセッションの個数で分割します。
    tags:
      - Sessions
  - name: アプリのセッション数
    description: ユーザーを、指定されたアプリ内に保持されているセッションの個数でセグメント化します。
    tags:
      - Sessions
  - name: X 過去Y日間のセッション
    description: "ユーザーs を、1 から30 までの最後に指定されたカレンダ日数のアプリに保持されていたセッションs (0 から50) でセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Sessions
  - name: 最初に使用したアプリ
    description: "ユーザーを、アプリに開封した記録されている最も早い時刻に分割します。<em>これは、Braze SDKを組み込んだアプリを使用している最初のセッションをキャプチャすることに注意してください。</em>(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: 最初に使用した特定のアプリ
    description: "ワークスペース内の任意のアプリに開封した、記録されている最も早い時刻でユーザーをセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: 最後に使用したアプリ
    description: "ユーザーがアプリに開封された最新の時刻までにセグメント化します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: 最後に使用した特定のアプリ
    description: "ユーザーを、指定したアプリに開封した最新の時刻に分割します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Sessions
  - name: セッション期間中央値
    description: アプリ内のセッションの中央値の長さでユーザーを分割します。
    tags:
      - Sessions
  - name: キャンペーンから受信したメッセージ
    description: "指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メール sの場合、メールリクエストが(実際に配信されたかどうかに関係なく)そのプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新 d です。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: キャンペーンバリアントを受賞
    description: "受信した多変量 キャンペーンのバリアントのユーザーを分割します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メール sの場合、メールリクエストが(実際に配信されたかどうかに関係なく)そのプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新 d です。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: キャンバスステップから受信したメッセージ
    description: "特定のキャンバスコンポーネントを受信したかどうかによって、ユーザーをセグメント化します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メール sの場合、メールリクエストが(実際に配信されたかどうかに関係なく)そのプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新 d です。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: 特定のキャンバスステップから最後に受信したメッセージ
    description: 特定のキャンバスコンポーネントを受信したときに、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: 特定のキャンペーンから最後に受信したメッセージ
    description: 指定したキャンペーンを受信したかどうかによってユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: キャンペーンまたはキャンバスからタグ付きで受信したメッセージ
    description: "指定したキャンペーンを受信したかどうか、または指定したタグのキャンバスを受信したかどうかによって、ユーザーを分割します。<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが送信されたときではなく、ユーザーがインプレッションを記録するときです。<br><br>プッシュおよびwebhookの場合、これはメッセージがユーザーに送信されるときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。<br><br>メール sの場合、メールリクエストが(実際に配信されたかどうかに関係なく)そのプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新 d です。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。"
    tags:
      - Retargeting
  - name: キャンペーンまたはCanvas With Tagから最後に受信したメッセージ
    description: 指定したタグのキャンペーンまたはキャンバスを受信したときに、ユーザーをセグメント化します。(24時間)
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
  - name: アプリメッセージの最後の印象
    description: ユーザーを最後にアプリ内メッセージを表示したときにセグメント化します。
    tags:
      - Retargeting
  - name: 最後に受信した SMS
    description: "最後のメッセージがSMSプロバイダーに配信された時刻までにユーザーをセグメント化します。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後に受信したWeb
    description: "ユーザーを、BrazeがそのユーザーのWebhookを最後に送信した時刻までに分割します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最終受信WhatsApp
    description: "最後にWhatsAppを受信したときに、ユーザーをセグメント化します。これは、メッセージがユーザーの機器に配信されるときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されるときです。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 最後に閲覧したニュースフィード
    description: 最後にニュースフィードを表示したときに、ユーザーをセグメント化します。
    tags:
      - Retargeting
  - name: ニュースフィードの閲覧数
    description: ユーザーがニュースフィードを何回表示したかをセグメント化します。
    tags:
      - Retargeting
  - name: クリックされた/開封されたキャンペーン
    description: "指定したキャンペーンでインターアクションでフィルタリングします。<br><br> メールとして、複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーもプロファイルs 更新 d を持ちます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封またはクリックの前にある場合、元のユーザーではなくそのメールアドレスを持つすべての残りのユーザーに開封またはクリックがアプリされます。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーs が受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーの\"トラッキングが有効になっているSMSメッセージ内の短縮されたリンクを、特定のキャンペーンから最後に選択したユーザー。"
    tags:
      - Retargeting
  - name: クリック/開いたキャンペーンまたはタグ付きキャンバス
    description: "特定のタグを持つ特定のキャンペーンを持つアクション間でフィルタリングします。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーもプロファイルs 更新 d を持ちます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封またはクリックの前にある場合、元のユーザーではなくそのメールアドレスを持つすべての残りのユーザーに開封またはクリックがアプリされます。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーs が受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザーが\"トラッキングを有効にしたSMSメッセージの短縮リンクを、特定のキャンペーンまたはキャンバスステップのタグで最後に選択したとき。"
    tags:
      - Retargeting
  - name: クリック/オープンステップ
    description: "特定のキャンバスコンポーネントを使用して、インターアクションでフィルタリングする。<br><br>SMSの場合、インターアクションは次のように定義されます。<br>- ユーザーは、指定されたキーワードカテゴリに一致するリプライSMSを最後に送信しました。これは、この電話番号を持つすべてのユーザーs が受信した最新のキャンペーンに属性されます。キャンペーンは、過去4時間以内に受信されている必要があります。<br>- ユーザークリック\"トラッキングが有効になっているSMSメッセージ内の短縮リンクを、特定のキャンバスステップから最後に選択したユーザー。"
    tags:
      - Retargeting
  - name: キャンペーンでクリックしたエイリアス
    description: "指定したキャンペーンの特定の別名をクリックしたかどうかによって、ユーザーをフィルタリングします。この唯一のアプリはメールにあります。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーもプロファイルs 更新 d を持ちます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封またはクリックの前にある場合、元のユーザーではなくそのメールアドレスを持つすべての残りのユーザーに開封またはクリックがアプリされます。"
    tags:
      - Retargeting
  - name: キャンバスステップでクリックしたエイリアス
    description: "特定のキャンバスで特定のエイリアスをクリックしたかどうかによって、ユーザーをフィルタリングします。この唯一のアプリはメールにあります。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーもプロファイルs 更新 d を持ちます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封またはクリックの前にある場合、元のユーザーではなくそのメールアドレスを持つすべての残りのユーザーに開封またはクリックがアプリされます。"
    tags:
      - Retargeting
  - name: キャンペーンステップまたはキャンバスステップでクリックしたエイリアス
    description: "ユーザーをフィルタリングするには、キャンペーンまたはキャンバスの別名をクリックします。この唯一のアプリはメールにあります。<br><br> 複数のユーザーが同じメールアドレスを共有している場合:<br>- メールを開封またはクリックすると、同じメールアドレスを持つ他のすべてのユーザーもプロファイルs 更新 d を持ちます。<br>- 元のユーザーがメッセージの送信後にメールアドレスを変更し、開封またはクリックの前にある場合、元のユーザーではなくそのメールアドレスを持つすべての残りのユーザーに開封またはクリックがアプリされます。"
    tags:
      - Retargeting
  - name: ハードバウンス
    description: メールアドレスがハードバウンスされたかどうか(メールアドレスが不正な場合など)によって、ユーザーs をセグメント化します。
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
  - name: 最後に送信されたSMS受信キーワードカテゴリ
    description: 特定のキーワードカテゴリ内の特定のサブスクリプショングループにSMSを最後に送信したときに、ユーザーをセグメント化します。 
    tags:
      - Retargeting
  - name: キャンペーンからコンバージョン済み
    description: 指定したキャンペーンに変換されたかどうかによって、ユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
    tags:
      - Retargeting
  - name: キャンバスからコンバージョン済み
    description: 特定のキャンバスで変換されたかどうかによって、ユーザーをセグメント化します。このフィルターには、コントロールグループに含まれるユーザーは含まれません。
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
    description: "最後にキャンペーンでコントロールグループに落ちたときまでにユーザーを分割します。(24時間)<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: 入力したキャンバスバリエーション
    description: 特定のキャンバスのバリエーションパスを入力したかどうかによって、ユーザーをセグメント化します。このフィルターはすべてのユーザーs を評価します。<br><br>たとえば、キャンバスのバリエーションコントロールグループを入力していないユーザーをフィルターすると、キャンバスに入力したかどうかに関係なく、コントロールグループにないすべてのユーザーが表示されます。
    tags:
      - Retargeting
  - name: メッセージの最終受信
    description: "最後に受信したメッセージを判別して、ユーザーをセグメント化します。(24時間)<br><br> コンテンツカードs およびアプリ内メッセージs の場合、カードまたはアプリ内メッセージが最後に送信されたときではなく、ユーザーが最後にインプレッションを記録したときです。<br><br>プッシュおよびwebhookの場合、これは、任意のメッセージがユーザーに送信されたときです。<br><br> WhatsAppの場合、これは、メッセージがユーザーの機器に配信されたときではなく、最後のメッセージAPIリクエストがWhatsAppに送信されたときです。<br><br>メール sの場合、メールリクエストが(実際に配信されたかどうかに関係なく)そのプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新 d です。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、これは最後のメッセージがSMSプロバイダーに配信されたときです。これは、メッセージがユーザーの機器に配信されたことを保証するものではありません。<br><br>例: <br>前回受信メール1日未満=24時間未満<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: メッセージへの最終エンゲージ
    description: "ユーザーを前回クリックまたは開封したときに、メッセージング チャネルのいずれか(コンテンツカード、メール、インアプリ、SMS、プッシュ、WhatsApp)をセグメント化します。マシン開封s またはメールの他の開封s でフィルターするための選択肢が含まれています。(24時間)<br><br>メール sの場合、メールリクエストが(実際に配信されたかどうかに関係なく)そのプロバイダーに送信されるときです。複数のユーザーが同じメールアドレスを共有している場合:<br>- 最初の送信では、指定されたターゲットユーザーのプロファイルのみが更新 d です。<br>- メールが配信されたとき、またはユーザーがメールまたはメール内のリンクを開封する場合、そのユーザーアドレスを共有するすべてのユーザーは、メッセージを受信するように耳を傾けます。<br><br>SMSの場合、ユーザークリック\"トラッキングが有効になっているメッセージ内の短縮リンクを最後に選択したユーザー。<br><br>タイムゾーン:<br>会社のタイムゾーン"
    tags:
      - Retargeting
  - name: クリックカード 
    description: "コンテンツカードをクリックしたかどうかによって、ユーザーを分割します。このフィルターは、\"Clicked/開封/キャンペーン\"、\"Clicked/開封 またはCanvas with Tag\"、および\"Clicked/開封 \"のサブフィルターとして使用できます。ステップ\""
    tags:
      - Retargeting
  - name: フィーチャーフラグ
    description: "現在有効になっている特定の<a href=\"/docs/developer_guide/platform_wide/feature_flags/about\">フィーチャーフラグ</a>を持つユーザーのSegment。"
    tags:
      - Retargeting
  - name: サブスクリプショングループ
    description: メール、SMS/MMS、またはWhatsAppのサブスクリプショングループでユーザーを分割します。アーカイブグループは耳元をアプリせず、使用できません。
    tags:
      - Channel subscription behavior
  - name: 利用可能なメール
    description: ユーザーを、有効なメールアドレスを持っているかどうか、およびメールにサブスクライブ/オプトインしているかどうかによってセグメント化します。メール利用可能なフィルターは、ユーザーがメールsから配信停止dであるかどうか、Brazeがハードバウンスを受信したかどうか、およびスパムとしてマークされたかどうかの3つの基準を確認します。これらの基準のいずれかが満たされている場合、またはメールがユーザーに存在しない場合、ユーザーは含まれません。
    tags:
      - Channel subscription behavior
  - name: メール選択日
    description: ユーザーをメールに選択した日に分割します。
    tags:
      - Channel subscription behavior
  - name: メールサブスクリプションステータス
    description: メールのサブスクリプション ステータスでユーザーを分割します。
    tags:
      - Channel subscription behavior
  - name: メール未購読日付 
    description: ユーザーs を、将来のメールs からd を配信停止した日に分割します。
    tags:
      - Channel subscription behavior
  - name: プッシュ通知が有効
    description: 暫定的なプッシュ認証があるか、フォアグラウンドプッシュが有効になっているユーザーをセグメント化します。特に、このカウントには以下が含まれます。<br>1. 暫定的にプッシュを許可されているiOS ユーザー。<br>2.ワークスペース内の任意のアプリに対してプッシュ通知を明示的にアクティブ化したユーザ。これらのユーザーs では、この数にはフォアグラウンドプッシュのみが含まれます。<br><br>プッシュ有効は、配信停止 d を持つユーザーを含みません。<br><br>このSegmentでフィルターを実行すると、<em>Reachable Users</em> という名前のAndroid、iOS、ウェブサイトのユーザーの内訳が下部に表示されます。
    tags:
      - Channel subscription behavior
  - name: アプリのプッシュ有効化
    description: ユーザーが機器のアプリに対してプッシュを有効にしているかどうかによって区切ります。これらのユーザーs はプッシュで到達可能ですが、オプトインされない可能性があります。この数には、仮にフォアグラウンドおよびバックグラウンド プッシュトークンs を許可されたユーザーが含まれます。
    tags:
      - Channel subscription behavior
  - name: バックグラウンドプッシュ有効
    description: バックグラウンドプッシュが有効になっているかどうかに基づいて、ユーザーをセグメント化します。
    tags:
      - Channel subscription behavior
  - name: Opt In Dateを押します
    description: プッシュを選択した日にユーザーを分割します。
    tags:
      - Channel subscription behavior
  - name: プッシュサブスクリプションステータス
    description: "ユーザーを<a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">サブスクリプション ステータス</a> でセグメント化してプッシュします。"
    tags:
      - Channel subscription behavior
  - name: 登録解除日を押す
    description: ユーザーs を、将来のプッシュ通知s からd を配信停止した日に分割します。
    tags:
      - Channel subscription behavior
  - name: 購入した製品
    description: アプリで購入した商品ごとにユーザーを分割します。
    tags:
      - Purchase behavior
  - name: 購入数の合計
    description: ユーザーのアプリでの購買数を分割します。
    tags:
      - Purchase behavior
  - name: X Y日購入商品
    description: 指定の商品を購入した回数でユーザーをフィルターします。
    tags:
      - Purchase behavior
  - name: 過去 Y 日間の X 回の購入
    description: "ユーザーを、1 から30 の間の最後に指定されたカレンダー日数に購入した回数(0 から50 の間) でセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: X Y日以内に物件を購入
    description: "ユーザーs を、1 から30 の間の最後の指定されたカレンダ日数の特定の購買プロパティに関連して購買が行われた回数でセグメント化します。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: 最初に行った購入
    description: ユーザーがアプリで購買した最も早い時点までに、ユーザーを分割します。
    tags:
      - Purchase behavior
  - name: アプリでの最初の購入
    description: ユーザーがアプリから購入した最も早い時点までに、ユーザーを分割します。
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
    description: ユーザーを、アプリで費やした金額で分割します。
    tags:
      - Purchase behavior
  - name: X 日間に支出した金額
    description: "ユーザーを、1 から30 までの最後に指定されたカレンダ日数でアプリに費やした金額でセグメント化します。この金額には、最後の50 回の購入の合計のみが含まれます。<br> <a href=\"/docs/x-in-y-behavior/\">ここでは、X-in-Y の動作について詳しく説明します。</a>"
    tags:
      - Purchase behavior
  - name: 国
    description: ユーザーを最後に示された国の場所でセグメント化します。
    tags:
      - Demographic attributes
  - name: 市区町村
    description: ユーザーを、最後に示された都市の場所でセグメント化します。
    tags:
      - Demographic attributes
  - name: 言語
    description: ユーザーを好みの言語でセグメント化します。
    tags:
      - Demographic attributes
  - name: 年齢
    description: ユーザーをアプリ内から示すように、年代別に分割します。
    tags:
      - Demographic attributes
  - name: 生年月日
    description: "アプリ内から示されているように、ユーザーを誕生日ごとに分割します。<br> 2月29日に誕生日を迎える利用者は、3月1日を含むSegmentsに含まれます。<br><br>12 月または1 月の誕生日をターゲットにするには、ターゲットとする年の12 か月の期間内にフィルターロジックのみを挿入します。言い換えれば、前の暦年の12月を振り返るロジックや、翌年の1月までのフォワードロジックを挿入しないでください。たとえば、12 月の誕生日を目標にするには、\" 12 月31 日\" \" 12 月31 日\" または\" を11 月30 日\" の後にフィルターします。"
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
    description: アプリ内から示されたように、ユーザーを名で分割します。
    tags:
      - Demographic attributes
  - name: 姓
    description: ユーザーを、アプリ内から示された姓でセグメント化します。
    tags:
      - Demographic attributes
  - name: アプリあり
    description: ユーザーがアプリをインストールしたことがあるかどうかによって分割されます。これには、現在アプリがインストールされているユーザーと、以前にアンインストールされたものが含まれます。通常、このフィルターに含めるアプリを開封する(セッションを起動する)には、ユーザーsが必要です。ただし、ユーザーがBraze にインポートされ、アプリに手動で関連付けられた場合など、いくつかの例外があります。
    tags:
      - App
  - name: 最新のアプリバージョン名
    description: ユーザーのアプリの最近の名前によって分割されます。
    tags:
      - App 
  - name: 最新のアプリバージョン番号
    description: アプリのユーザーの最新版番号によって分割されます。
    tags:
      - App 
  - name: アンインストール
    description: アプリをアンインストールし、再インストールしていないかどうかによって、ユーザーを分割します。
    tags:
      - Uninstall 
  - name: デバイスの通信事業者
    description: デバイスキャリアごとにユーザーを分割します。
    tags:
      - Devices
  - name: デバイス数
    description: ユーザーを、アプリを使用した機器の数で分割します。
    tags:
      - Devices
  - name: デバイスモデル
    description: 携帯電話機の機種別にユーザーを分割します。
    tags:
      - Devices
  - name: デバイスOS
    description: 指定したオペレーティングシステムを持つ1つ以上の装置を持つユーザーをセグメント化します。
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
  - name: iOSで仮承認
    description: iOS 12 で特定のアプリに対して暫定的に許可されているユーザーを検索できます。
    tags:
      - Devices   
  - name: Webブラウザー
    description: Web サイトにアクセスするために使用するウェブブラウザによって、ユーザーをセグメント化します。
    tags:
      - Devices
  - name: デバイスIDFA
    description: テストするキャンペーン 受信者をIDFA で指定できます。
    tags:
      - Advertising use cases
  - name: デバイスIDFV
    description: テスト用にIDFV でキャンペーン 受信者を指定できます。
    tags:
      - Advertising use cases 
  - name: デバイスGoogle Ad ID
    description: ユーザーをグーグルの広告ID でセグメント化します。
    tags:
      - Advertising use cases
  - name: デバイスロク広告ID
    description: ユーザーを道路番号で分割します。
    tags:
      - Advertising use cases
  - name: デバイスのWindows Ad ID
    description: ユーザーをWindows アドID でセグメント化します。
    tags:
      - Advertising use cases  
  - name: 広告の追跡が有効
    description: "ユーザーがアド\"トラッキングを選択しているかどうかに基づいてフィルターできます。広告\"トラッキングはIDFA または&amp;quot に関連します。広告主&amp;quot の識別子。Apple によってすべてのiOS 機器に割り当てられます。これはSDK s によって設定できます。この識別子により、広告主はユーザーsを追跡し、ターゲット広告を提供することができます。"
    tags:
      - Advertising use cases
  - name: 最新の場所
    description: ユーザーを、アプリを使用した最後に記録された場所でセグメント化します。
    tags:
      - Location
  - name: 利用可能な場所
    description: "ユーザーの位置がレポートされているかどうかによって、それらをセグメント化します。このフィルターを使用するには、アプリに<a href=\"/docs/search/?query=location%20tracking\">位置\"トラッキングが統合されている必要があります。</a>"
    tags:
      - Location
  - name: Amplitudeコホート
    description: Amplitude を使用するクライアントは、Amplitude でコホートs を選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: Censusコホート
    description: Census を使用するクライアントは、Census でコホートs を選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: ヒープコホート
    description: ヒープを使用するクライアントは、ヒープ内のコホートを選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: Hightouchコホート
    description: Hightouch を使用するクライアントは、Hightouch でコホートs を選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: Kubitコホート
    description: Kubit を使用するクライアントは、Kubit でコホートs を選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: ミックスパネルコホート
    description: Mixpanel を使用するクライアントは、Mixpanel でコホートを選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: セグメントコホート
    description: Segment を使用するクライアントは、Segment でコホートを選択してインポートすることで、そのSegmentを補完できます。
    tags:
      - Cohort membership
  - name: 微小なコホート
    description: Tinyclues を使用するクライアントは、Tinyclues でコホートを選択してインポートすることで、Segmentを補完できます。
    tags:
      - Cohort membership
  - name: 属性アドのインストール
    description: インストール先がd 属性であった広告によって、ユーザーs をセグメント化します。
    tags:
      - User Attributes
  - name: 属性Adgroupのインストール
    description: ユーザーs を、そのインストール先がd 属性であった広告グループによってセグメント化します。
    tags:
      - Install Attribution
  - name: 属性のインストールキャンペーン
    description: インストール先が属性である広告キャンペーンによって、ユーザーs をセグメント化します。
    tags:
      - Install Attribution
  - name: 属性ソースのインストール
    description: ユーザーを、インストール先が属性dであった送信元別にセグメント化します。
    tags:
      - Install Attribution
  - name: チャーン・リスク分類
    description:  ユーザーを、具体的な予測に応じて、解約リスクカテゴリ別にセグメント化します。
    tags:
      - Intelligence and predictive
  - name: チャーン・リスクスコア
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
  - name: メッセージオープン可能性
    description: "指定したチャネルに0 ～100% の範囲で開封する可能性に基づいてユーザーをフィルタリングします。チャネルの可能性を測定するのに十分なデータがないユーザは、\"is blank.&amp;quot を使用して選択できます。"
    tags:
      - Intelligence and predictive
  - name: アプリを利用しているファクスeBookの友達の人数
    description: ユーザーを、同じアプリを使用しているFac eBookの友達の数でセグメント化します。
    tags:
      - Social activity
  - name: 接続されたFaceBook
    description: アプリをファクスeBookに接続したかどうかによって、ユーザーを分割します。
    tags:
      - Social activity
  - name: 接続済みTwitter
    description: アプリをX(以前のTwitter)に接続したかどうかによって、ユーザーをセグメント化します。
    tags:
      - Social activity
  - name: Twitterフォロワー数
    description: ユーザーをX (以前のTwitter) フォロワーの数でセグメント化します。
    tags:
      - Social activity
---
