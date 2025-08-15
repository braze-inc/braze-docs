---
nav_title: メール設定
article_title: メール設定
page_type: reference
page_order: 14
description: "このリファレンス記事では、送信設定、開封追跡ピクセル、[サブスクリプション] ページとフッターなど、Braze ダッシュボードのメール設定について説明します。"
tool: Dashboard
channel: email

---

# メール設定

> [メール設定] では、カスタムフッター、カスタムのオプトインページ、オプトアウトページなど、具体的な送信メール設定を行うことができます。送信メールにこれらのオプションを含めると、一貫して流れるようなエクスペリエンスがユーザーにもたらされます。

[**メール設定**] は、ダッシュボードの [**設定**] の下にあります。

## 送信設定

[**送信設定**] セクションのメール設定により、メールキャンペーンに含まれる詳細が決まります。特にこれらの設定は、主にユーザーが Braze からメールを受信したときに表示される内容に関連します。

### 送信メールの設定

メール設定を行うときに、送信メール設定は、Braze がユーザーにメールを送信するときに使用する名前とメールアドレスを特定します。

{% tabs local %}
{% tab 表示名とアドレス %}

このセクションでは、Braze からユーザーにメールを送信するときに使用できる名前とメールアドレスを追加できます。表示名とメールアドレスは、メールキャンペーンを作成するときに [**送信情報を編集**] オプションで使用できます。送信メール設定を更新しても、過去にさかのぼって既存の送信には影響しないことに注意してください。 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% endtab %}
{% tab 返信先アドレス %}

このセクションにメールアドレスを追加すると、そのアドレスをメールキャンペーンの返信先アドレスとして選択できます。[**デフォルトにする**] を選択して、あるメールアドレスをデフォルトのメールアドレスにすることもできます。これらのメールアドレスは、メールキャンペーンを作成するときに [**送信情報を編集**] オプションで使用できます。

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab BCCアドレス %}

このセクションでは、Braze からの送信メールメッセージに追加できる BCC アドレスの追加および管理ができます。BCC アドレスは、SendGrid およびSparkPost でのみ使用できます。BCC アドレスの代わりに、[メッセージアーカイブ]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) を使用して、アーカイブまたはコンプライアンスの目的でユーザに送信されるメッセージのコピーを保存することをお勧めします。

BCC アドレスを E メールメッセージに追加すると、ユーザーが受信したメッセージと同じコピーが BCC 受信ボックスに送信されます。これは、コンプライアンス要件またはカスタマーサポートの問題のためにユーザーに送信したメッセージのコピーを保持するのに便利なツールです。BCCメールはメールレポートやアナリティクスには含まれない。

{% alert important %}
キャンペーンまたはキャンバスにBCC アドレスを追加すると、キャンペーンまたはキャンバスコンポーネントの請求可能なメールが2 倍になります。これは、Braze が1 つのメッセージをユーザに、1 つはBCC アドレスに送信するためです。
{% endalert %}

![電子メール設定」タブの「BCCアドレス」セクション]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

アドレスを追加すると、キャンペーンまたはキャンバスステップでメールを作成するときに、アドレスを選択できるようになります。新規のメールキャンペーンまたはキャンバスコンポーネントを開始するときに、このアドレスがデフォルトで選択されるように設定するには、アドレスの横にある [**デフォルトにする**] を選択します。これをメッセージレベルでオーバーライドするには、メッセージの設定時に [**BCC なし**] を選択します。

Braze から送信されるすべてのメールメッセージに BCC アドレスを含める必要がある場合は、[**すべてのメールキャンペーンで BCC アドレスを要求する**] トグルをオンにできます。これには、デフォルトのアドレスを選択する必要があります。このアドレスは、新しいメールキャンペーンまたはキャンバスステップで自動的に選択されます。デフォルトのアドレスは、REST API を通じてトリガーされるすべてのメッセージにも自動的に追加されます。アドレスを含めるために既存の API リクエストを変更する必要はありません。

{% endtab %}
{% endtabs %}

## 開封追跡ピクセル

[![ブレイズ・ラーニング・コース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

メールの開封追跡ピクセルは、メールの HTML に自動的に挿入される非表示の 1 x 1 ピクセルの画像です。このピクセルにより、エンドユーザーがメールを開封したどうかを Braze が検出できます。メールの開封情報は非常に便利で、対応する開封率をユーザーが理解して効果的なマーケティング戦略を決定するときに役立ちます。

### 追跡ピクセルの配置

Braze のデフォルトの動作では、メールの下部に追跡ピクセルが追加されます。ほとんどのユーザーにとって、これはピクセルを配置するときに最適な場所です。ピクセルのスタイルはすでに、視覚的な変化をできるだけ小さくするように設定されていますが、意図しない視覚的な変化はメールの下部にあるとほぼまったく目立ちません。これは、SendGrid や SparkPost などのメールプロバイダーのデフォルトでもあります。

### 追跡ピクセルの位置の変更

Braze は現在、メールサービスプロバイダー (ESP) のデフォルトの開封追跡ピクセルの位置 (メールの `<body>` の最後のタグ) をオーバーライドして `<body>` の最初のタグに移動することをサポートしています。
  
![SendGrid、SparkPost、または Amazon SES の移動オプションが表示されている [開封追跡ピクセル] セクション。]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

場所を変更するには、次の手順に従います。

1. Braze で、[**設定**] > [**メール設定**] に移動します。
2. 以下のオプションから選択する：[**SendGrid の移動**]、[**SparkPost の移動**]、または [**Amazon SES の移動**]
3. [**保存**] を選択します。

保存すると、Braze はすべての HTML メールの先頭に開封トラッキングピクセルを配置するための特別な命令を メールサービスプロバイダー (ESP) に送信します。
  
{% alert important %}
SSLを有効にすると、追跡ピクセルのURLがHTTPではなくHTTPSでラップされます。SSLの設定が間違っていると、トラッキングピクセルの有効性に影響する可能性があります。
{% endalert %}

## list-unsubscribe ヘッダー {#list-unsubscribe}

{% alert note %}
2024 年 2 月 15 日以降、新規の会社では list-unsubscribe ヘッダー (ワンクリックで配信停止) がデフォルトで有効になります。
{% endalert %}

list-unsubscribe ヘッダーを使用すると、メッセージ本文ではなくメールボックス UI 内に [**購読解除**] ボタンが表示されるため、受信者はマーケティングメールから簡単に配信停止ができます。

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

受信者が **[配信停止]**をクリックすると、メールボックスプロバイダーはメールヘッダーに定義されている宛先に配信停止リクエストを送信します。

list-unsubscribe を有効にすることは、配信到達性のベストプラクティスであり、一部の主要なメールボックスプロバイダーでは要件になっています。エンドユーザーには、メールクライアントの [スパム] ボタンをクリックするのではなく、不要なメッセージの受信者から自分自身を安全に削除することが推奨されます。[スパム] ボタンをクリックすると、送信の信頼度やメールの配信到達性に悪影響を及ぼします。

### メールボックスプロバイダーのサポート

次の表に、「mailto:」ヘッダー、list-unsubscribe URL、およびワンクリック配信停止 ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) に対するメールボックスプロバイダーのサポートをまとめています。

| list-unsubscribe ヘッダー | Mailto: ヘッダー | list-unsubscribe URL | ワンクリック配信停止 （RFC 8058） | 
| ----- | --- | --- | --- |
| Gmail | 対応* | 対応 | 対応 |
| Gmailモバイル | サポートされていない | サポートされていない | サポートされていない |
| Apple メール | 対応 | サポートされていない | サポートされていない |
| Outlook.com | 対応 | サポートされていない | サポートされていない |
| Yahoo!メール | 対応* | サポートされていない | 対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo と Gmail は最終的に「mailto:」ヘッダーを廃止し、ワンクリックのみをサポートする予定です。_

ヘッダーの表示は、最終的にメールボックスプロバイダーによって決定されます。Gmail で受信者宛ての未加工 (テキスト) メールに list-unsubscribe ヘッダーが含まれているかどうかを確認するには、次の手順に従います。

1. メールの [**メッセージのソースを表示**] を選択します。これにより、メールの未加工バージョンとそのヘッダーを含む新しいタブが開きます。
2. 「List-Unsubscribe」を検索します。

このヘッダーが未加工バージョンのメールに含まれているにもかかわらず表示されない場合、メールボックスプロバイダーは配信停止オプションを表示しないと決定しています。つまり、メールボックスプロバイダーがヘッダーを表示しない理由についてはこれ以上のインサイトが得られません。list-unsubscribe ヘッダーの表示は、最終的に信頼度に基づいて行われます。ほとんどの場合、受信トレイでの送信者の信頼度が高いほど、list-unsubscribe ヘッダーが表示される可能性が低くなります。

### ワークスペースのメール配信停止ヘッダー

![送信先のユーザーとして [登録済みまたはオプトイン済みのユーザー] を選択する。]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

メール配信停止ヘッダー機能がオンになっている場合、この設定は会社レベルではなく、ワークスペース全体に適用されます。キャンペーンおよびキャンバスビルダーの**Target Audience** ステップで、登録またはオプトインのユーザーまたはオプトインのユーザーに送信するように設定されたキャンペーンおよびキャンバスに追加されます。

「ワークスペースのデフォルト」を使用する場合、Braze はトランザクションと見なされるキャンペーン ([購読解除済みのユーザーを含むすべてのユーザー] に設定されているキャンペーン) のワンクリック配信停止ヘッダーを追加しません。これをオーバーライドし、サブスクリプションされていないユーザーに送信するときにワンクリックでサブスクリプション解除ヘッダーを追加するには、メッセージレベルのワンクリックリスト-サブスクリプション解除設定で**すべてのメールからグローバルにサブスクリプション解除を選択できます**。

### デフォルトの list-unsubscribe ヘッダー

{% alert important %}
Gmail は、2024 年 6 月 1 日以降、送信するすべての商用およびプロモーション メッセージについて、ワンクリック配信停止を実装するように、送信者に要求する予定です。詳細については、Gmail の「[メール送信者のガイドライン](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe)」と「[メール送信者のガイドラインに関するよくある質問](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)」を参照してください。Yahoo は、この更新された要件について、2024 年初頭のタイムラインを発表しました。詳細については、「[More Secure, Less Spam:Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/)」を参照してください。
{% endalert %}

Braze の配信停止機能を使用して配信停止を直接処理するには、[**配信登録済みまたはオプトイン済みのユーザーに送信されるメールに One-Click List-Unsubscribe (mailto および HTTP) ヘッダーを含める**] を選択し、標準の Braze URL および mail-to として [**Braze のデフォルト**] を選択します。 

![配信登録またはオプトインしているユーザーに送信されるメールに、list-unsubscribe ヘッダーを自動的に含めるオプション。]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze は、次のバージョンの list-unsubscribe ヘッダーをサポートしています。

| リスト配信停止バージョン | 説明 | 
| ----- | --- |
| ワンクリック（RFC 8058） | 受信者がワンクリックでメールからオプトアウトする簡単な方法を提供します。これは、Yahoo と Gmail から一括送信者に課される要件です。 |
| リスト配信停止URLまたはHTTPS | 受信者に、購読を解除できるウェブページに誘導するリンクを提供する。 |
| mailto | 受信者からブランドに送信されるサブスクリプション解除要求メッセージの送信先として電子メールアドレスを指定します。<br><br> _mailto list-unsubscribe リクエストを処理するには、そのような配信停止リクエストに、配信を停止するエンドユーザーについて Braze に保存されているメールアドレスが含まれている必要があります。これは、エンドユーザーが配信を停止するメールの「差出人アドレス」、配信を停止するエンドユーザーが受信したメールのエンコードされた件名またはエンコードされた本文で提供される場合があります。ごく限られたケースでは、一部の受信トレイプロバイダーは[RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368)プロトコルに準拠していないため、メールアドレスが正しく渡されません。このため、配信停止リクエストが Braze で処理できないことがあります。_ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze が上記の方法のいずれかでユーザーから list-unsubscribe リクエストを受信すると、このユーザーのグローバルサブスクリプション状態が配信停止に設定されます。一致しない場合、Braze はこのリクエストを処理しません。

### ワンクリック配信停止

list-unsubscribe ヘッダー([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) に対してワンクリックでunsubscribe を使用すると、受信者がメールからオプトアウトするための簡単な方法を提供することに重点が置かれます。

### メッセージレベルのワンクリック・リスト配信停止

メッセージレベルのワンクリックリスト購読解除設定は、ワークスペースの電子メール購読解除ヘッダー機能を上書きする。次の用途では、キャンペーンまたはキャンバスステップごとにワンクリック配信停止動作を適用します。

- 1 つのワークスペース内で複数のブランド/リストをサポートするために、特定の購読グループに対して Braze のワンクリック配信停止機能を追加する
- デフォルトのBraze配信停止URLかカスタムURLかを切り替える
- カスタム・ワンクリック配信停止URLを追加する
- このメッセージのワンクリック配信停止を省略する

{% alert note %}
メッセージレベルの1 クリックリスト/サブスクリプション解除設定は、ドラッグアンドドロップエディタと更新されたHTML エディタを使用する場合にのみ使用できます。以前のHTMLエディターを使用している場合は、更新されたHTMLエディターに切り替えてこの機能を使用する。
{% endalert %}

メールエディターで、「**送信設定」**＞「**送信情報**」と進む。以下のオプションから選択する：

- **ワークスペースのデフォルトを使用**: **メール**設定で設定された**メール配信停止ヘッダー**設定を使用する。この設定を変更すると、すべてのメッセージに適用される。
- **すべてのメールからの配信をすべて停止**: Braze デフォルトのワンクリック配信停止ヘッダーを使用します。配信停止ボタンをクリックしたユーザーは、グローバルメール配信登録状態が「配信停止済み」に設定されます。
- **特定の購読グループから配信停止**: 指定されたサブスクリプショングループを使用する。配信停止ボタンをクリックしたユーザーは、選択した購読グループからの配信が停止されます。
    - 購読グループを選択する際、この特定グループを購読しているユーザーのみをターゲットにするには、[**ターゲットオーディエンス**] で [**購読グループフィルター**] を追加します。ワンクリック配信停止用に選択した購読グループは、ターゲットにしている購読グループと一致していなければなりません。サブスクリプション・グループに不一致がある場合、すでにサブスクリプション解除されているサブスクリプション・グループからサブスクリプションを解除しようとしているユーザーに送信する危険性があります。
- **カスタム:**配信停止を直接処理するためのカスタムのワンクリック配信停止 URL を追加します。
- **配信停止を除外**

{% alert important %}
ワンクリック配信停止や任意の配信停止メカニズムを除外するのは、パスワードのリセット、領収書、確認メールなど、トランザクションメッセージングに対してのみ行ってください。
{% endalert %}

この設定を調整すると、このメールでのワンクリックによるリスト購読解除のデフォルトの動作が上書きされる。

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 要件

独自のカスタム配信停止機能を使用してメールを送信する場合は、設定したワンクリック配信停止 URL を RFC 8058 に確実に適合させるために、次の要件を満たす必要があります。

* URL は配信停止 POST リクエストを処理できる必要があります。
* URL は `https://` で始まる必要があります。
* URLはHTTPSリダイレクトやボディを返してはならない。ランディングページや他のタイプのウェブページに移動するワンクリック退会リンクは、RFC 8058に準拠していない。
* POST リクエストがクッキーを設定してはなりません。

[**カスタムの list-unsubscribe ヘッダー**] を選択して、独自に構成したワンクリック配信停止エンドポイントと、オプションの [mailto:] を追加します。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## メールの件名行の追加

トグルを使って、テストメールとシードメールの件名に "[TEST]" と "[SEED]" を含める。これは、テストとして送信されたメールキャンペーンの識別に役立ちます。

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 新規メールで CSS をデフォルトでインライン化

CSS インライン化は、メールと新規メールの CSS スタイルを自動的にインライン化する手法です。一部のメールクライアントでは、これによりメールのレンダリング方法が改善される可能性があります。

この設定を変更しても、既存のメールメッセージやテンプレートには影響しません。メッセージまたはテンプレートの作成中に、いつでもこのデフォルトをオーバーライドできます。詳細については、[CSSインライン化]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)を参照してください。

## メールアドレスを変更したユーザーへの配信を再登録

ユーザーがメールアドレスを変更したときに、そのユーザーへの配信を自動的に再登録できます。例えば、以前に配信停止を行ったワークスペースユーザーが、自分のメールアドレスを Braze の配信停止リストにないアドレスに変更した場合、そのユーザーのサブスクリプションが自動的に再開されます。

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## サブスクリプションのページおよびフッター

{% tabs local %}
{% tab カスタムフッター %}

商用メールの場合、[CAN-SPAM 法](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)では、すべての商用メールに配信停止オプションを含めることを義務付けています。[カスタムフッター] 設定を使用すると、CAN-SPAM を遵守したうえで、メールのオプトアウトフッターをカスタマイズできます。遵守状態を維持するために、このワークスペースのキャンペーンの一部として送信されるすべてのメールにカスタムフッターを追加する必要があります。

メールメッセージングのカスタムフッターを作成するときには、次の要件に注意してください。
- 配信停止 URL と物理的な郵送先住所を含める必要があります。
- 100 KB 未満でなければなりません。

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

カスタムフッターの Liquid テンプレートの詳細については、[カスタムフッター]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)に関するドキュメントを参照してください。

{% endtab %}
{% tab カスタム配信停止ページ %}

Braze を使用すると、独自の HTML を使用して**カスタム配信停止ページ**を設定できます。このページは、ユーザーがメールの下部から配信停止を選択した後に表示されます。このページは 750 KB 未満でなければならないことに注意してください。 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% tab カスタムオプトインページ %}

独自の HTML を使用してカスタムのオプトインページを作成できます。これをメールに含めると、特にユーザーのライフサイクル全体を通じてブランディングとメッセージの一貫性を維持する場合にメリットがあります。このページは 750 KB 未満でなければならないことに注意してください。 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% endtabs %}

## よくある質問

### ワンクリック配信停止

{% details ワンクリック配信停止URL（list-unsubscribeヘッダ経由）は、プリファレンスセンターにリンクできるか？ %}
いいえ、これは RFC 8058 に準拠していません。つまり、Yahoo と Gmail のワンクリック配信停止要件に適合していません。
{% enddetails %}

{% details プリファレンスセンターを作成する際、「本文に配信停止リンクが含まれていません」というエラーメッセージが表示されるのはなぜか？ %}
ユーザー設定センターは、配信停止リンクとはみなされません。CAN-SPAMに準拠するためには、メール受信者が商業メールの配信を停止できるようにしなければならない。
{% enddetails %}

{% details ワンクリック配信停止設定を有効にした後、過去のメールキャンペーンやキャンバスを編集して適用する必要があるか？ %}
メッセージレベルのワンクリックリスト配信停止設定のユースケースに該当しない場合は、「**メール設定**」でこの設定がオンになっている限り、必要なアクションはない。Brazeは、すべての送信マーケティングおよびプロモーションメッセージにワンクリック配信停止ヘッダーを自動的に追加する。ただし、ワンクリック配信停止の動作をメッセージごとに設定する必要がある場合は、それに応じてメールで以前のキャンペーンとキャンバスステップを更新する必要があります。
{% enddetails %}

{% details 元のメッセージや生データでは、リスト配信停止やワンクリック配信停止のヘッダーが見えるのに、なぜGmailやYahooでは配信停止ボタンが見えないのか？ %}
最終的に、Gmail と Yahoo が list-unsubscribe ヘッダーまたはワンクリック配信停止ヘッダーを表示するかどうかを決定します。新しい送信者または送信者のレピュテーションが低い送信者の場合、サブスクリプション解除ボタンが表示されないことがあります。
{% enddetails %}

{% details カスタムワンクリック配信停止ヘッダはLiquidをサポートしているか？ %}
はい、Liquid および条件付きロジックがサポートされており、ヘッダーのダイナミックワンクリック配信停止 URL を使用できます。
{% enddetails %}

{% alert tip %}
条件付きロジックを追加する場合、Braze は空白を削除しないため、URL に空白を追加する出力値を含めないでください。
{% endalert %}

### メッセージレベルのワンクリック・リスト配信停止

{% details ワンクリックのメールヘッダーを手動で追加し、メールの登録解除ヘッダーがオンになっている場合、予想される動作は何ですか? %}
ワンクリックリスト配信停止のために追加されたメールヘッダは、このキャンペーンの今後のすべての送信に適用される。
{% enddetails %}

{% details 購読グループを起動するには、メッセージのバリアント間でグループが一致しなければならないのはなぜか? %}
A/Bテストのキャンペーンでは、Brazeはユーザーにランダムにバリアントの1つを送信する。同じキャンペーンに2 つの異なるサブスクリプショングループが設定されている場合(Variant A がSubscription Group A に設定され、Variant B がSubscription Group B に設定されている場合)、Subscription Group B のみにサブスクリプションされているユーザーがVariant B を取得することを保証することはできません。ユーザーがすでにオプトアウトされているサブスクリプショングループからサブスクリプションを解除するシナリオがあります。
{% enddetails %}

{% details 「メール環境設定」ではメールの配信停止ヘッダー設定が無効になっていますが、キャンペーンの送信情報では、ワンクリックリスト配信停止設定が「ワークスペースのデフォルトを使用」するように設定されています。これはバグですか? %}
いいえ。ワークスペースの設定が無効になっていて、メッセージの設定が「**ワークスペースデフォルトを使用**」に設定されている場合、Braze は**メール環境設定**で指定されている設定に従います。したがって、キャンペーンのワンクリック配信停止ヘッダーは追加されません。
{% enddetails %}

{% details 購読グループがアーカイブされるとどうなるか？この場合、送信されたメールのワンクリック配信停止は解除されるのか？ %}
ワンクリックの**送信**情報で参照されている購読グループがアーカイブされている場合でも、Brazeはワンクリックからの配信停止を処理する。サブスクリプショングループは、ダッシュボード（セグメントフィルタ、ユーザープロファイル、および同様のエリア）に表示されなくなる。
{% enddetails %}

{% details メールテンプレートでワンクリック配信停止の設定は可能か? %}
メールテンプレートは送信ドメインに割り当てられていないため、現在この機能を追加する予定はありません。Eメールテンプレートのこの機能に興味がある場合は、[製品フィードバックを]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)送信する。
{% enddetails %}

{% details この機能は、カスタムオプションに追加されたワンクリック配信停止URLが有効かどうかをチェックするのか？ %}
Braze ダッシュボードでは、リンクのチェックや検証は行っていません。ローンチする前に、URLをきちんとテストすること。
{% enddetails %}


