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

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは [**メール設定**] と呼ばれ、[**設定**] > [**設定の管理**] > [**メール設定**] の下にあります。
{% endalert %}

## 送信設定

[**送信設定**] セクションのメール設定により、メールキャンペーンに含まれる詳細が決まります。特にこれらの設定は、主にユーザーが Braze からメールを受信したときに表示される内容に関連します。

### 送信メールの設定

メール設定を行うときに、送信メール設定は、Braze がユーザーにメールを送信するときに使用する名前とメールアドレスを特定します。

{% tabs local %}
{% tab Display Name Address %}

このセクションでは、Braze からユーザーにメールを送信するときに使用できる名前とメールアドレスを追加できます。表示名とメールアドレスは、メールキャンペーンを作成するときに [**送信情報を編集**] オプションで使用できます。送信メール設定を更新しても、過去にさかのぼって既存の送信には影響しないことに注意してください。 

![\]({% image_buster /assets/img/email_settings/display_name_address.png %})

「差出人」のアドレスを設定するときには、必ず「差出人」のメールドメインを送信ドメイン (marketing.yourdomain.com など) に一致させてください。一致しない場合、SPF と DKIM の不一致が生じる可能性があります。ダイナミックな「差出人」のアドレスを持つメールは、対応する送信ドメインの IP プールから送信されます。すべての返信先メールアドレスをルートドメインに設定できます。

{% endtab %}
{% tab Reply-To Address %}

このセクションにメールアドレスを追加すると、そのアドレスをメールキャンペーンの返信先アドレスとして選択できます。[**デフォルトにする**] を選択して、あるメールアドレスをデフォルトのメールアドレスにすることもできます。これらのメールアドレスは、メールキャンペーンを作成するときに [**送信情報を編集**] オプションで使用できます。

![\]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab BCC Address %}

このセクションでは、Braze からの送信メールメッセージに追加できる BCC アドレスの追加および管理ができます。メールメッセージに BCC アドレスを追加すると、ユーザーが受信するメッセージと同一のコピーが自分の BCC 受信トレイに送信されます。これは、コンプライアンス要件やカスタマーサポートの問題に関して、ユーザーに送信したメッセージのコピーを保持するうえで便利なツールです。

{% alert important %}
BBC アドレスをキャンペーンまたはキャンバスに追加すると、Braze はユーザーに 1 件のメッセージを送信し、BCC アドレスに 1 件のメッセージを送信するため、キャンペーンまたはキャンバスコンポーネントの請求対象メールが 2 倍になります。
{% endalert %}

![BCC Address section of the Email Settings tab.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

アドレスを追加すると、キャンペーンまたはキャンバスのステップでメールを作成するときにそのアドレスを選択できます。新規のメールキャンペーンまたはキャンバスコンポーネントを開始するときに、このアドレスがデフォルトで選択されるように設定するには、アドレスの横にある [**デフォルトにする**] を選択します。これをメッセージレベルでオーバーライドするには、メッセージの設定時に [**BCC なし**] を選択します。

Braze から送信されるすべてのメールメッセージに BCC アドレスを含める必要がある場合は、[**すべてのメールキャンペーンで BCC アドレスを要求する**] トグルをオンにできます。オンにすると、新しいメールキャンペーンまたはキャンバスステップで自動的に選択されるデフォルトのアドレスを選択する必要があります。デフォルトのアドレスは、REST API を通じてトリガーされるすべてのメッセージにも自動的に追加されます。アドレスを含めるために既存の API リクエストを変更する必要はありません。

{% endtab %}
{% endtabs %}

## 開封追跡ピクセル

[![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

メールの開封追跡ピクセルは、メールの HTML に自動的に挿入される非表示の 1 x 1 ピクセルの画像です。このピクセルにより、エンドユーザーがメールを開封したどうかを Braze が検出できます。メールの開封情報は非常に便利で、対応する開封率をユーザーが理解して効果的なマーケティング戦略を決定するときに役立ちます。

### 追跡ピクセルの配置

Braze のデフォルトの動作では、メールの下部に追跡ピクセルが追加されます。ほとんどのユーザーにとって、これはピクセルを配置するときに最適な場所です。ピクセルのスタイルはすでに、視覚的な変化をできるだけ小さくするように設定されていますが、意図しない視覚的な変化はメールの下部にあるとほぼまったく目立ちません。これは、SendGrid や SparkPost などのメールプロバイダーのデフォルトでもあります。

### 追跡ピクセルの位置の変更

Braze は現在、メールサービスプロバイダー (ESP) のデフォルトの開封追跡ピクセルの位置 (メールの `<body>` の最後のタグ) をオーバーライドして `<body>` の最初のタグに移動することをサポートしています。
  
![][13]{: style="max-width:80%;" }

場所を変更するには、次の手順に従います。

1. Braze で、[**設定**] > [**メール設定**] に移動します。
2. [**カスタム開封トラッキングピクセルの設定**} の下のチェックボックスをクリックします。 
3. [**保存**] をクリックします。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これは [**設定の管理**] > [**メール設定**] にあります。
{% endalert %}

保存すると、Braze はすべての HTML メールの先頭に開封トラッキングピクセルを配置するための特別な命令を メールサービスプロバイダー (ESP) に送信します。
  
{% alert important %}
SSL を有効にすると、トラッキングピクセルの URL が HTTP ではなく HTTPS でラップされます。SSL が正しく設定されていない場合、トラッキングピクセルの効果に影響する可能性があります。
{% endalert %}

## list-unsubscribe ヘッダー

{% alert note %}
2024 年 2 月 15 日以降、新規の会社では list-unsubscribe ヘッダー (ワンクリックで配信停止) がデフォルトで有効になります。
{% endalert %}

list-unsubscribe ヘッダーを使用すると、メッセージ本文ではなくメールボックス UI 内に [**購読解除**] ボタンが表示されるため、受信者はマーケティングメールから簡単に配信停止ができます。

![\]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

受信者が **[配信停止]**をクリックすると、メールボックスプロバイダーはメールヘッダーに定義されている宛先に配信停止リクエストを送信します。

list-unsubscribe を有効にすることは、配信到達性のベストプラクティスであり、一部の主要なメールボックスプロバイダーでは要件になっています。エンドユーザーには、メールクライアントの [スパム] ボタンをクリックするのではなく、不要なメッセージの受信者から自分自身を安全に削除することが推奨されます。[スパム] ボタンをクリックすると、送信の信頼度やメールの配信到達性に悪影響を及ぼします。

### 仕組み

![\]({% image_buster /assets/img/email_settings/target_audiences_example.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

この機能をオンにすると、会社レベルではなくワークスペース全体に機能が適用されます。これは、サブスクリプション登録済みまたはオプトインしているユーザー、あるいはキャンペーンとキャンバスビルダーの [**ターゲットオーディエンス**] ステップでのみオプトインしているユーザーに送信するように設定されているキャンペーンとキャンバスに追加されます。

Braze はトランザクションと見なされるものにヘッダーを追加しないため、配信停止済みユーザーを含むすべてのユーザーにメッセージが送信されるように設定されている場合、list-unsubscribe ヘッダーはメッセージに添付されません。さらに、list-unsubscribe ヘッダーは Braze 内の対象ユーザープロファイルについてのみ生成と追加が行われるため、テスト送信によって配信されるメッセージにヘッダーは追加されません。

### デフォルトの list-unsubscribe ヘッダー

{% alert important %}
Gmail は、2024 年 6 月 1 日以降、送信するすべての商用およびプロモーション メッセージについて、ワンクリック配信停止を実装するように、送信者に要求する予定です。詳細については、Gmail の「[メール送信者のガイドライン](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe)」と「[メール送信者のガイドラインに関するよくある質問](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)」を参照してください。Yahoo は、この更新された要件について、2024 年初頭のタイムラインを発表しました。詳細については、「[More Secure, Less Spam:Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/)」を参照してください。
{% endalert %}

Braze の配信停止機能を使用して配信停止を直接処理するには、 [**配信登録済みまたはオプトイン済みのユーザーに送信されるメールに One-Click List-Unsubscribe (mailto および HTTP) ヘッダーを含める**] を選択し、標準の Braze URl および mail-to として [**Braze のデフォルト**] を選択します。 

![Option to automatically include a list-unsubscribe header for emails sent to subscribed or opted-in users.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %}){: style="max-width:80%;"}

Braze は、次のバージョンの list-unsubscribe ヘッダーをサポートしています。

| list-unsubscribe のバージョン | 説明 |
| ----- | --- |
| ワンクリック (RFC 8058) | 受信者がワンクリックでメールをオプトアウトできる簡単な方法を提供します。これは、一括送信者に対する Yahoo および Gmail の要件です。 |
| list-unsubscribe の URL または HTTPS | 受信者に、配信停止ができる Web ページに移動するリンクを提供します。 |
| mailto | 受信者からブランドに送信される配信停止リクエストメッセージの宛先メールアドレスを指定します。<br><br> _mailto list-unsubscribe リクエストを処理するには、そのような配信停止リクエストに、配信を停止するエンドユーザーについて Braze に保存されているメールアドレスが含まれている必要があります。これは、エンドユーザーが配信を停止するメールの「差出人アドレス」、配信を停止するエンドユーザーが受信したメールのエンコードされた件名またはエンコードされた本文で提供される場合があります。非常に限られたケースですが、一部の受信トレイプロバイダーが [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) プロトコルに準拠していないため、メールアドレスが適切に渡されません。これにより、配信停止リクエストが Braze で処理できない可能性があります。_ |
{: .reset-td-br-1 .reset-td-br-2}

Braze が上記の方法のいずれかでユーザーから list-unsubscribe リクエストを受信すると、このユーザーのグローバルサブスクリプション状態が配信停止に設定されます。一致しない場合、Braze はこのリクエストを処理しません。

### ワンクリック配信停止

list-unsubscribe ヘッダーにワンクリック配信停止を使用すること ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) は、受信者がメールからオプトアウトする簡単な方法を提供することに重点を置いています。 

#### 要件

独自のカスタム配信停止機能を使用してメールを送信する場合は、設定したワンクリック配信停止 URL を RFC 8058 に確実に適合させるために、次の要件を満たす必要があります。

* URL は配信停止 POST リクエストを処理できる必要があります。
* URL は `https://` で始まる必要があります。
* URL は `<` と `>` で囲む必要があります。
* URL が HTTPS リダイレクトを返してはなりません。ランディングページまたは他のタイプの Web ページに移動するワンクリック配信停止リンクは、RFC 8058 に準拠していません。
* メッセージには有効な DKIM 署名が必要です。

[**カスタムの list-unsubscribe ヘッダー**] を選択して、独自に構成したワンクリック配信停止エンドポイントと、オプションの [mailto:] を追加します。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

![\]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

#### メールボックスプロバイダーのサポート

次の表に、「mailto:」ヘッダー、list-unsubscribe URL、およびワンクリック配信停止 ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) に対するメールボックスプロバイダーのサポートをまとめています。

| list-unsubscribe ヘッダー | mailto: ヘッダー | list-unsubscribe URL | ワンクリック配信停止 (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | サポート* | サポート | サポート |
| Gmail Mobile | 未サポート | 未サポート | 未サポート |
| Apple Mail | サポート* | 未サポート | 未サポート |
| Outlook.com | サポート | 未サポート | 未サポート |
| Yahoo!Mail | サポート* | 未サポート | サポート |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

_\*Yahoo と Gmail は最終的に「mailto:」ヘッダーを廃止し、ワンクリックのみをサポートする予定です。_

ヘッダーの表示は、最終的にメールボックスプロバイダーによって決定されます。Gmail で受信者宛ての未加工 (テキスト) メールに list-unsubscribe ヘッダーが含まれているかどうかを確認するには、次の手順に従います。

1. メールの [**メッセージのソースを表示**] を選択します。これにより、メールの未加工バージョンとそのヘッダーを含む新しいタブが開きます。
2. 「List-Unsubscribe」を検索します。

このヘッダーが未加工バージョンのメールに含まれているにもかかわらず表示されない場合、メールボックスプロバイダーは配信停止オプションを表示しないと決定しています。つまり、メールボックスプロバイダーがヘッダーを表示しない理由についてはこれ以上のインサイトが得られません。list-unsubscribe ヘッダーの表示は、最終的に信頼度に基づいて行われます。ほとんどの場合、受信トレイでの送信者の信頼度が高いほど、list-unsubscribe ヘッダーが表示される可能性が低くなります。

#### ワンクリック配信停止をメールヘッダーに追加

多数のブランドやリストを管理するために、単一のワークスペースにカスタム配信停止フローが複数ある場合は、カスタムのワンクリック配信停止ヘッダーをメールヘッダーに手動で追加できます。

1. メールキャンペーンの [**送信設定**] に移動します。
2. [**詳細設定**] を選択します。
3. [**\+ 新しいヘッダーを追加**] をクリックし、以下を追加します。
* [**List-Unsubscribe-Post**] に、「`List-Unsubscribe=One-Click`」を入力します。
* [**List-Unsubscribe**] に、ワンクリック配信停止リンクを入力します。

![\]({% image_buster /assets/img/email_settings/one-click_unsubscribe_to_email_header.png %})

#### よくある質問

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
いいえ、これは RFC 8058 に準拠していません。つまり、Yahoo と Gmail のワンクリック配信停止要件に適合していません。
{% enddetails %}

{% details Will I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
いいえ、[**メール設定**] で設定が有効になると、Braze は送信するすべてのマーケティングおよびプロモーションメッセージにワンクリック配信停止ヘッダーを自動的に追加します。
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
最終的に、Gmail と Yahoo が list-unsubscribe ヘッダーまたはワンクリック配信停止ヘッダーを表示するかどうかを決定します。新規送信者、または信頼度の低い送信者の場合、これにより [配信停止] ボタンが表示されない場合があります。
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
はい、Liquid および条件付きロジックがサポートされており、ヘッダーのダイナミックワンクリック配信停止 URL を使用できます。
{% enddetails %}

#### ヒント

* URL が `<` と `>` に囲まれていない場合、および `https://` で始まらない場合には、 次のメッセージが表示されます。「設定の保存に失敗しました。保存する前にエラーを修正してください。」
* 条件付きロジックを追加する場合、Braze は空白を削除しないため、URL に空白を追加する出力値を含めないでください。

## メールの件名行の追加

テストメールとシードメールの件名行に「[TEST]」と「[SEED]」を含めるには、次のトグルを使用します。これは、テストとして送信されたメールキャンペーンの識別に役立ちます。

![\]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 新規メールで CSS をデフォルトでインライン化

CSS インライン化は、メールと新規メールの CSS スタイルを自動的にインライン化する手法です。一部のメールクライアントでは、これによりメールのレンダリング方法が改善される可能性があります。

この設定を変更しても、既存のメールメッセージやテンプレートには影響しません。メッセージまたはテンプレートの作成中に、いつでもこのデフォルトをオーバーライドできます。詳細については、[CSS インライン化][10] を参照してください。

## メールアドレスを変更したユーザーへの配信を再登録

ユーザーがメールアドレスを変更したときに、そのユーザーへの配信を自動的に再登録できます。例えば、以前に配信停止を行ったワークスペースユーザーが、自分のメールアドレスを Braze の配信停止リストにないアドレスに変更した場合、そのユーザーのサブスクリプションが自動的に再開されます。

![\]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## サブスクリプションのページおよびフッター

{% tabs local %}
{% tab Custom Footer %}

商用メールの場合、[CAN-SPAM 法](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)では、すべての商用メールに配信停止オプションを含めることを義務付けています。[カスタムフッター] 設定を使用すると、CAN-SPAM を遵守したうえで、メールのオプトアウトフッターをカスタマイズできます。遵守状態を維持するために、このワークスペースのキャンペーンの一部として送信されるすべてのメールにカスタムフッターを追加する必要があります。

メールメッセージングのカスタムフッターを作成するときには、次の要件に注意してください。
\- 配信停止の URL と郵送先住所を含める必要があります。
\- 100 KB 未満である必要があります。

![\]({% image_buster /assets/img/email_settings/custom_footer.png %})

カスタムフッターの Liquid テンプレートの詳細については、[カスタムフッター]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)に関するドキュメントを参照してください。

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze を使用すると、独自の HTML を使用して**カスタム配信停止ページ**を設定できます。このページは、ユーザーがメールの下部から配信停止を選択した後に表示されます。このページは 750 KB 未満でなければならないことに注意してください。 

![\]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% tab Custom Opt-In Page %}

独自の HTML を使用してカスタムのオプトインページを作成できます。これをメールに含めると、特にユーザーのライフサイクル全体を通じてブランディングとメッセージの一貫性を維持する場合にメリットがあります。このページは 750 KB 未満でなければならないことに注意してください。 

![\]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

メールリスト管理のベストプラクティスの詳細については、「[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)」を参照してください。

{% endtab %}
{% endtabs %}


[0]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[6]: https://learning.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[13]: {% image_buster /assets/img/open_pixel.png %}
