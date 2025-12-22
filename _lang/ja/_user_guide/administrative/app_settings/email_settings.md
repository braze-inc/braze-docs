---
nav_title: メール設定
article_title: メール設定
page_type: reference
page_order: 14
description: "このリファレンス記事では、送信設定、開封追跡ピクセル、[サブスクリプション] ページとフッターなど、Braze ダッシュボードのメール設定について説明します。"
tool: Dashboard
channel: email
toc_headers: h2

---

# メール設定

> [メール設定] では、カスタムフッター、カスタムのオプトインページ、オプトアウトページなど、具体的な送信メール設定を行うことができます。送信メールにこれらのオプションを含めると、一貫して流れるようなエクスペリエンスがユーザーにもたらされます。

[**メール設定**] は、ダッシュボードの [**設定**] の下にあります。

## 送信設定

[**送信設定**] セクションのメール設定により、メールキャンペーンに含まれる詳細が決まります。特にこれらの設定は、主にユーザーが Braze からメールを受信したときに表示される内容に関連します。

### 送信メールの設定

メール設定を行うときに、送信メール設定は、Braze がユーザーにメールを送信するときに使用する名前とメールアドレスを特定します。

{% tabs local %}
{% tab Display Name Address %}

このセクションでは、Brazeがユーザーにメールを送信する際に使用できる名前とメールアドレスを追加することができる。表示名とメールアドレスは、メールキャンペーンを作成する際に、**送信情報の編集**オプションで利用できる。送信メール設定を更新しても、過去にさかのぼって既存の送信には影響しないことに注意してください。

!["送信メール設定 "セクションには、さまざまな表示名とドメインのフィールドがある。]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### リキッドでパーソナライズされる

また、**From Display Nameと** **Local Part**フィールドで[Liquidを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)使用すると、カスタム属性に基づいて送信メールをダイナミックにテンプレート化できる。例えば、条件付きロジックを使って、異なるブランドや地域から送信することができる：

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

このセクションにメールアドレスを追加すると、そのアドレスをメールキャンペーンの返信先アドレスとして選択できます。[**デフォルトにする**] を選択して、あるメールアドレスをデフォルトのメールアドレスにすることもできます。これらのメールアドレスは、メールキャンペーンを作成するときに [**送信情報を編集**] オプションで使用できます。

![「返信先アドレス」セクションには、複数の返信先アドレスを入力するフィールドがある。]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### リキッドでパーソナライズされる

カスタム属性に基づいて返信先をダイナミックにテンプレート化するために、**返信先**フィールドで[リキッドを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)使うこともできる。例えば、条件付きロジックを使って、異なる地域や部署に返信を送ることができる：

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
us-support@company.com
{% elsif {{custom_attribute.${region}}} == 'EU' %}
eu-support@company.com
{% else %}
global-support@company.com
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

このセクションでは、Brazeから送信されるメールメッセージに付加できるBCCアドレスを追加、管理できる。BCC アドレスは、SendGrid およびSparkPost でのみ使用できます。BCC アドレスの代わりに、[メッセージアーカイブ]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) を使用して、アーカイブまたはコンプライアンスの目的でユーザに送信されるメッセージのコピーを保存することをお勧めします。

BCC アドレスを E メールメッセージに追加すると、ユーザーが受信したメッセージと同じコピーが BCC 受信ボックスに送信されます。これは、コンプライアンス要件またはカスタマーサポートの問題のためにユーザーに送信したメッセージのコピーを保持するのに便利なツールです。BCCメールはメールレポートやアナリティクスには含まれない。

{% alert important %}
キャンペーンまたはキャンバスにBCC アドレスを追加すると、キャンペーンまたはキャンバスコンポーネントの請求可能なメールが2 倍になります。これは、Braze が1 つのメッセージをユーザに、1 つはBCC アドレスに送信するためです。
{% endalert %}

![メール設定」タブの「BCCアドレス」セクション。]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

アドレスを追加すると、キャンペーンまたはキャンバスステップでメールを作成するときに、アドレスを選択できるようになります。新規のメールキャンペーンまたはキャンバスコンポーネントを開始するときに、このアドレスがデフォルトで選択されるように設定するには、アドレスの横にある [**デフォルトにする**] を選択します。これをメッセージレベルでオーバーライドするには、メッセージの設定時に [**BCC なし**] を選択します。

Braze から送信されるすべてのメールメッセージに BCC アドレスを含める必要がある場合は、[**すべてのメールキャンペーンで BCC アドレスを要求する**] トグルをオンにできます。これには、デフォルトのアドレスを選択する必要があります。このアドレスは、新しいメールキャンペーンまたはキャンバスステップで自動的に選択されます。デフォルトのアドレスは、REST API を通じてトリガーされるすべてのメッセージにも自動的に追加されます。アドレスを含めるために既存の API リクエストを変更する必要はありません。

{% endtab %}
{% endtabs %}

## 開封追跡ピクセル

[![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

メールの開封追跡ピクセルは、メールの HTML に自動的に挿入される非表示の 1 x 1 ピクセルの画像です。このピクセルにより、エンドユーザーがメールを開封したどうかを Braze が検出できます。メールの開封情報は非常に便利で、対応する開封率をユーザーが理解して効果的なマーケティング戦略を決定するときに役立ちます。

### 追跡ピクセルの配置

Braze のデフォルトの動作では、メールの下部に追跡ピクセルが追加されます。ほとんどのユーザーにとって、これはピクセルを配置するときに最適な場所です。ピクセルのスタイルはすでに、視覚的な変化をできるだけ小さくするように設定されていますが、意図しない視覚的な変化はメールの下部にあるとほぼまったく目立ちません。これは、SendGrid や SparkPost などのメールプロバイダーのデフォルトでもあります。

### 追跡ピクセルの位置の変更

Braze は現在、メールサービスプロバイダー (ESP) のデフォルトの開封追跡ピクセルの位置 (メールの `<body>` の最後のタグ) をオーバーライドして `<body>` の最初のタグに移動することをサポートしています。
  
!["Open Tracking Pixel "セクションで、SendGrid、SparkPost、Amazon SESのいずれかに移動するオプションを選択する。]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

場所を変更するには、次の手順に従います。

1. Braze で、[**設定**] > [**メール設定**] に移動します。
2. 以下のオプションから選択する：[**SendGrid の移動**]、[**SparkPost の移動**]、または [**Amazon SES の移動**]
3. [**保存**] を選択します。

保存後、Brazeはメールサービスプロバイダーに特別な指示を送り、開封トラッキングピクセルをすべてのHTMLメールの上部に設置する（ESP）。
  
{% alert important %}
SSLイネーブルメントは、トラッキングピクセルのURLをHTTPではなくHTTPSでラップする。SSLの設定が間違っていると、トラッキングピクセルの有効性に影響する可能性があります。
{% endalert %}

## list-unsubscribe ヘッダー {#list-unsubscribe}

{% alert note %}
2024年2月15日以降、新規参入企業はlist-unsubscribeヘッダー（ワンクリックで配信停止）がデフォルトでイネーブルメントになっている。
{% endalert %}

list-unsubscribe ヘッダーを使用すると、メッセージ本文ではなくメールボックス UI 内に [**購読解除**] ボタンが表示されるため、受信者はマーケティングメールから簡単に配信停止ができます。

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

受信者が**配信停止を**選択すると、メールボックスプロバイダはメールヘッダーで定義された送信先に配信停止リクエストを送信する。

list-unsubscribe を有効にすることは、配信到達性のベストプラクティスであり、一部の主要なメールボックスプロバイダーでは要件になっています。これは、エンドユーザーが迷惑なメッセージから自分自身を安全に削除することを奨励するもので、メールクライアントのスパムボタンを押すのとは異なり、後者は送信の信頼度やメールの配信到達性に悪影響を与える。

[Gmailでサブスクリプションを管理する](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC)場合、Gmailはメッセージ本文から配信停止リンクを取り込むこともできるが、ヘッダーにある場合はリスト配信停止を優先する。

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

_\*YahooとGmailは最終的に "mailto: "ヘッダーを廃止し、ワンクリックのみに対応する。_

ヘッダーの表示は、最終的にメールボックスプロバイダーによって決定されます。Gmail で受信者宛ての未加工 (テキスト) メールに list-unsubscribe ヘッダーが含まれているかどうかを確認するには、次の手順に従います。

1. メールの [**メッセージのソースを表示**] を選択します。これにより、メールの未加工バージョンとそのヘッダーを含む新しいタブが開きます。
2. 「List-Unsubscribe」を検索します。

このヘッダーが未加工バージョンのメールに含まれているにもかかわらず表示されない場合、メールボックスプロバイダーは配信停止オプションを表示しないと決定しています。つまり、メールボックスプロバイダーがヘッダーを表示しない理由についてはこれ以上のインサイトが得られません。list-unsubscribe ヘッダーの表示は、最終的に信頼度に基づいて行われます。たいていの場合、メールボックス・プロバイダでのあなたの送信者の評判が高ければ高いほど、配信停止ヘッダーが表示される可能性は高くなる。

### ワークスペースのメール配信停止ヘッダー

![どのユーザーに送信するかは、「サブスクライバーまたはオプトインしているユーザー」を選択する。]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

メール配信停止ヘッダー機能がオンになっている場合、この設定は会社レベルではなく、ワークスペース全体に適用されます。キャンペーンおよびキャンバスビルダーの**Target Audience** ステップで、登録またはオプトインのユーザーまたはオプトインのユーザーに送信するように設定されたキャンペーンおよびキャンバスに追加されます。

「ワークスペースのデフォルト」を使用する場合、Braze はトランザクションと見なされるキャンペーン ([購読解除済みのユーザーを含むすべてのユーザー] に設定されているキャンペーン) のワンクリック配信停止ヘッダーを追加しません。これをオーバーライドし、サブスクリプションされていないユーザーに送信するときにワンクリックでサブスクリプション解除ヘッダーを追加するには、メッセージレベルのワンクリックリスト-サブスクリプション解除設定で**すべてのメールからグローバルにサブスクリプション解除を選択できます**。

### デフォルトの list-unsubscribe ヘッダー

{% alert important %}
Gmail は、2024 年 6 月 1 日以降、送信するすべての商用およびプロモーション メッセージについて、ワンクリック配信停止を実装するように、送信者に要求する予定です。詳細については、Gmail の「[メール送信者のガイドライン](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe)」と「[メール送信者のガイドラインに関するよくある質問](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)」を参照してください。Yahoo は、この更新された要件について、2024 年初頭のタイムラインを発表しました。詳細については、「[More Secure, Less Spam:Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/)」を参照してください。
{% endalert %}

Braze の配信停止機能を使用して配信停止を直接処理するには、[**配信登録済みまたはオプトイン済みのユーザーに送信されるメールに One-Click List-Unsubscribe (mailto および HTTP) ヘッダーを含める**] を選択し、標準の Braze URL および mail-to として [**Braze のデフォルト**] を選択します。 

![サブスクライバーまたはオプトインユーザーに送信されるメールに、自動的に配信停止ヘッダーを含めるオプション。]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze は、次のバージョンの list-unsubscribe ヘッダーをサポートしています。

| リスト配信停止バージョン | 説明 | 
| ----- | --- |
| ワンクリック（RFC 8058） | 受信者がワンクリックでメールからオプトアウトする簡単な方法を提供します。これは、Yahoo と Gmail から一括送信者に課される要件です。 |
| リスト配信停止URLまたはHTTPS | 受信者に、購読を解除できるウェブページに誘導するリンクを提供する。 |
| mailto | 受信者からブランドに送信されるサブスクリプション解除要求メッセージの送信先として電子メールアドレスを指定します。<br><br> _mailto list-unsubscribe リクエストを処理するには、そのような配信停止リクエストに、配信を停止するエンドユーザーについて Braze に保存されているメールアドレスが含まれている必要があります。これは、エンドユーザーが配信を停止するメールの「差出人アドレス」、配信を停止するエンドユーザーが受信したメールのエンコードされた件名またはエンコードされた本文で提供される場合があります。ごく限られたケースでは、一部の受信トレイプロバイダーは[RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368)プロトコルに準拠していないため、メールアドレスが正しく渡されません。このため、配信停止リクエストが Braze で処理できないことがあります。_ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze が上記の方法のいずれかでユーザーから list-unsubscribe リクエストを受信すると、このユーザーのグローバルサブスクリプション状態が配信停止に設定されます。一致しない場合、Brazeはこのリクエストを処理しない。

### ワンクリック配信停止

list-unsubscribe ヘッダー([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) に対してワンクリックでunsubscribe を使用すると、受信者がメールからオプトアウトするための簡単な方法を提供することに重点が置かれます。

### メッセージレベルのワンクリック・リスト配信停止

メッセージレベルのワンクリックリスト配信停止設定は、ワークスペースのメール配信停止ヘッダー機能を上書きする。次の用途では、キャンペーンまたはキャンバスステップごとにワンクリック配信停止動作を適用します。

- 1 つのワークスペース内で複数のブランド/リストをサポートするために、特定の購読グループに対して Braze のワンクリック配信停止機能を追加する
- デフォルトのBraze配信停止URLかカスタムURLかを切り替える
- カスタム・ワンクリック配信停止URLを追加する
- このメッセージのワンクリック配信停止を省略する

{% alert note %}
メッセージレベルの1 クリックリスト/サブスクリプション解除設定は、ドラッグアンドドロップエディタと更新されたHTML エディタを使用する場合にのみ使用できます。以前のHTMLエディターを使用している場合は、更新されたHTMLエディターに切り替えてこの機能を使用する。
{% endalert %}

メールエディターで、「**送信設定」**＞「**送信情報**」と進む。以下のオプションから選択する：

- **ワークスペースのデフォルトを使用**: **メール**設定で設定された**メール配信停止ヘッダー**設定を使用する。この設定を変更すると、すべてのメッセージに適用される。
- **すべてのメールからの配信をすべて停止**: Braze デフォルトのワンクリック配信停止ヘッダーを使用します。配信停止ボタンをクリックしたユーザーは、グローバルメールのサブスクリプション状態が「配信停止」に設定される。
- **特定の購読グループから配信停止**: 指定されたサブスクリプショングループを使用する。Brazeは、選択したサブスクリプショングループから配信停止ボタンをクリックしたユーザーの配信を停止する。
    - 購読グループを選択する際、この特定グループを購読しているユーザーのみをターゲットにするには、[**ターゲットオーディエンス**] で [**購読グループフィルター**] を追加します。ワンクリック配信停止用に選択した購読グループは、ターゲットにしている購読グループと一致していなければなりません。サブスクリプション・グループに不一致がある場合、すでにサブスクリプション解除されているサブスクリプション・グループからサブスクリプションを解除しようとしているユーザーに送信する危険性があります。

{% alert important %}
**特定のサブスクリプショングループからの配信停止**設定は、ワンクリックリストの配信停止ヘッダーにのみ適用される。このオプションを選択しても、mailto list-配信停止ヘッダーは影響を受けない。つまり、この方法で配信停止した受信者は、特定のサブスクリプショングループからの配信停止ではなく、グローバルな配信停止のログを記録することになる。mailto list-unsubscribeヘッダーをグローバルに配信停止するユーザーから除外するには、この設定を選択する際に、[サポートに]({{site.baseurl}}/support_contact/)連絡する。
{% endalert %}

- **カスタム:**配信停止を直接処理するためのカスタムのワンクリック配信停止 URL を追加します。
- **配信停止を除外**

{% alert important %}
ワンクリック配信停止や任意の配信停止メカニズムを除外するのは、パスワードのリセット、領収書、確認メールなど、トランザクションメッセージングに対してのみ行ってください。
{% endalert %}

この設定を調整することで、このメールでのワンクリックによるリスト配信停止のデフォルトの動作が上書きされる。

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

テストメールとシードメールの件名行に「[TEST]」と「[SEED]」を含めるには、次のトグルを使用します。これは、テストとして送信されたメールキャンペーンの識別に役立ちます。

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 新規メールで CSS をデフォルトでインライン化

CSS インライン化は、メールと新規メールの CSS スタイルを自動的にインライン化する手法です。一部のメールクライアントでは、これによりメールのレンダリング方法が改善される可能性があります。

この設定を変更しても、既存のメールメッセージやテンプレートには影響しない。メッセージまたはテンプレートの作成中に、いつでもこのデフォルトをオーバーライドできます。詳細については、[CSSインライン化]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)を参照してください。

## メールアドレスを変更したユーザーへの配信を再登録

ユーザーがメールアドレスを変更したときに、そのユーザーへの配信を自動的に再登録できます。例えば、以前に配信停止したワークスペース・ユーザーが、Brazeの配信停止リストにないメールアドレスに変更した場合、自動的に再登録となる。

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## サブスクリプションのページおよびフッター

{% tabs local %}
{% tab Custom Footer %}

商用メールの場合、[CAN-SPAM 法](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)では、すべての商用メールに配信停止オプションを含めることを義務付けています。[カスタムフッター] 設定を使用すると、CAN-SPAM を遵守したうえで、メールのオプトアウトフッターをカスタマイズできます。遵守状態を維持するために、このワークスペースのキャンペーンの一部として送信されるすべてのメールにカスタムフッターを追加する必要があります。

メールメッセージングのカスタムフッターを作成するときには、次の要件に注意してください。
- 配信停止 URL と物理的な郵送先住所を含める必要があります。
- 100 KB 未満でなければなりません。

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

カスタムフッターの Liquid テンプレートの詳細については、[カスタムフッター]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)に関するドキュメントを参照してください。

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze を使用すると、独自の HTML を使用して**カスタム配信停止ページ**を設定できます。このページは、ユーザーがメールの下部から配信停止を選択した後に表示される。このページは 750 KB 未満でなければならないことに注意してください。 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% tab Custom Opt-In Page %}

独自の HTML を使用してカスタムのオプトインページを作成できます。これをメールに含めると、特にユーザーのライフサイクル全体を通じてブランディングとメッセージの一貫性を維持する場合にメリットがあります。このページは 750 KB 未満でなければならないことに注意してください。 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert tip %}
サブスクリプションページまたはフッターの**プレビュー**セクションで、**プレビューリンクをコピー**するを選択し、ランダムなユーザーに対してメールフッター、配信停止ページ、またはオプトインページがどのように見えるかを示す共有可能なプレビューリンクを生成してコピーする。リンクは7日間持続し、その後再生が必要となる。
{% endalert %}

## よくある質問

### ワンクリック配信停止

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
いいえ、これは RFC 8058 に準拠していません。つまり、Yahoo と Gmail のワンクリック配信停止要件に適合していません。
{% enddetails %}

{% details Why do I receive the error message "Your email body does not include an unsubscribe link" when composing my preference center? %}
ユーザー設定センターは、配信停止リンクとはみなされません。CAN-SPAMに準拠するためには、メール受信者が商業メールの配信を停止できるようにしなければならない。
{% enddetails %}

{% details Do I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
メッセージレベルのワンクリックリスト配信停止設定のユースケースに該当しない場合は、「**メール設定**」でこの設定がオンになっている限り、必要なアクションはない。Brazeは、ワンクリック配信停止ヘッダーをすべての送信マーケティングやプロモーションメッセージに自動的に追加する。ただし、ワンクリック配信停止の動作をメッセージごとに設定する必要がある場合は、それに応じてメールで以前のキャンペーンとキャンバスステップを更新する必要があります。
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
最終的に、Gmail と Yahoo が list-unsubscribe ヘッダーまたはワンクリック配信停止ヘッダーを表示するかどうかを決定します。新しい送信者または送信者のレピュテーションが低い送信者の場合、サブスクリプション解除ボタンが表示されないことがあります。
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
はい、Liquid および条件付きロジックがサポートされており、ヘッダーのダイナミックワンクリック配信停止 URL を使用できます。
{% enddetails %}

{% alert tip %}
条件付きロジックを追加する場合、Braze は空白を削除しないため、URL に空白を追加する出力値を含めないでください。
{% endalert %}

### メッセージレベルのワンクリック・リスト配信停止

{% details If I add the email headers for one-click manually, and I have the email unsubscribe header turned on, what is the expected behavior? %}
ワンクリックリスト配信停止のために追加されたメールヘッダーは、このキャンペーンの今後のすべての送信に適用される。
{% enddetails %}

{% details Why do subscription groups have to match across message variants in order to launch? %}
ABテストのキャンペーンでは、Brazeはランダムにユーザーにバリアントの1つを送信する。同じキャンペーンに2つの異なるサブスクリプショングループが設定されている場合（バリアントAがサブスクリプショングループAに設定され、バリアントBがサブスクリプショングループBに設定されている）、サブスクリプショングループBのみにサブスクライブしているユーザーがバリアントBを受信することは保証できません。
{% enddetails %}

{% details The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug? %}
ワークスペース設定がオフで、メッセージ設定が**Use workspace defaultに**設定されている場合、Brazeは**メール**設定で設定された内容に従う。これは、キャンペーンのワンクリック配信停止ヘッダーを追加しないことを意味する。
{% enddetails %}

{% details What happens if a subscription group is archived? Does this break the one-click unsubscribe on emails sent? %}
ワンクリックの**送信**情報で参照したサブスクリプショングループがアーカイブ化されている場合、Brazeはワンクリックからの配信停止を引き続き処理する。サブスクリプショングループがダッシュボード（セグメンテーションフィルター、ユーザープロファイル、および同様のエリア）に表示されなくなった。
{% enddetails %}

{% details Is the one-click unsubscribe setting available for email templates? %}
メールテンプレートは送信ドメインに割り当てられていないため、現在この機能を追加する予定はありません。Eメールテンプレートのこの機能に興味がある場合は、[製品フィードバックを]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)送信する。
{% enddetails %}

{% details Does this feature check that the one-click unsubscribe URL added to the custom option is valid? %}
Braze ダッシュボードでは、リンクのチェックや検証は行っていません。ローンチする前に、URLをきちんとテストすること。
{% enddetails %}
