---
nav_title: SMS、RCS、WhatsApp登録フォーム
article_title: SMS、RCS、WhatsApp登録フォーム
alias: "/phone_number_capture/"
page_order: 1
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使ってSMS、RCS、WhatsAppの登録フォームを作成する方法を説明する。"
---

# SMS、RCS、WhatsApp登録フォーム

> SMS、RCS、WhatsAppのサインアップフォームは、アプリ内メッセージのドラッグ＆ドロップエディターで利用できるテンプレートである。これらのテンプレートを使ってユーザーの電話番号を収集し、SMS、MMS、RCS、WhatsAppサブスクリプショングループを拡大しよう。

![電話サインアップフォームのテンプレートを使って作成したアプリ内メッセージの3つの例。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDKの要件' %}

## 電話番号登録フォームの作成

### ステップ 1: テンプレートを選ぶ

アプリ内メッセージをドラッグ＆ドロップで作成する場合、テンプレートに**SMSサインアップ**（RCSサインアップに対応）または**WhatsAppサインアップを**選択し、**メッセージの作成を**選択する。これらのテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}) アプリ内メッセージ作成時に、SMSサインアップまたはWhatsAppサインアップをテンプレートとして選択するモーダル。{: style="max-width:80%"}

### ステップ 2: メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![カスタムフォントのアップロードと選択のワークフロー]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### ステップ 3: 電話番号入力コンポーネントをカスタマイズする

サインアップフォームの作成を開始するには、エディターで電話番号の入力コンポーネントを選択します。

![電話番号の入力コンポーネントを選択したサインアップフォーム作成時のプレビューエリア]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

サイドメニューから、このテンプレートが電話番号を収集するサブスクリプショングループを指定します。コンプライアンスのベストプラクティスに従うために、電話番号のサインアップフォームごとに 1 つの購読グループに対する同意のみを収集できます。ただし、必要に応じて、他の購読グループの同意を収集するために複数のフォームを使用できます。

![サブスクリプショングループドロップダウンにサブスクリプショングループが選択されています。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

デフォルトでは、グローバルに数値を収集しますが、収集する国の数は制限できます。これは、特定の国の電話番号を持つユーザーにのみメッセージを送信する場合に役立ち、リストの清潔さを保つのに役立ちます。そのためには、**すべての国から番号を収集する**をオフにして、ドロップダウンを使用して特定の国を選択します。ユーザーは、あなたが明示的に追加した国のみを選択できるようになります。

![国のドロップダウンから、番号を収集したい国を選択します。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### 無効な電話番号

ユーザーが受け入れられない特殊文字を含む電話番号を入力した場合、カスタマイズできない一般的なエラー指標が表示され、フォームを送信できません。**プレビュー & テスト** タブおよびテストデバイスでエラーの動作を確認できます。この記事を参照して、[Brazeが電話番号をフォーマットする方法]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers)を学んでください。

### ステップ 4: 免責条項を追加する（SMSおよびRCS登録フォーム用）

SMSやRCSの登録フォームでは、送信するSMSやRCSの種類を明確に伝えることが重要だ。フォームに次の情報を含めることで、リストの増加がコンプライアンスに準拠していることを確認してください。

- 顧客が期待できるSMSやRCSメッセージの種類（カートのリマインダー、プロモーションやお得な情報、アポイントメントのリマインダーなど）の説明。すべてのユースケースを列挙する必要はありませんが、ブランドが送信するメッセージの種類について説明する必要があります。
- 同意は購入の条件ではないことに注意してください（該当する場合）。
- メッセージの頻度とメッセージおよびデータ料金が適用されることを思い出させる。正確なメッセージ頻度がわからない場合は、頻度が変動する可能性があると言うことができます。
- 利用規約、SMSおよびRCSプライバシーポリシーへのリンク。
- ヘルプとオプトアウトキーワードのリマインダー（ヘルプの場合はHELP、キャンセルするにはSTOP）。

テンプレートにプレースホルダーの免責事項を例として提供していますが、これは法的助言を構成するものではなく、コンプライアンスの目的で依拠すべきではありません。法務チームと協力して、特定のブランドに合わせた文面を作成してください。

{% alert note %}
このドキュメントは、法律上の助言を提供することを意図したものではなく、完全に依存することもできません。
{% endalert %}

SMSとRCSのコンプライアンスに関する詳細は、[SMS、MMS、RCSに関する法規制を]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)参照のこと。

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)を使用して、メッセージの外観と感触をカスタマイズします。

## 結果を分析する

{% multi_lang_include drag_and_drop/templates.md section='レポート' %}

![アプリ内メッセージの各リンクのクリック数を表示するアプリ内メッセージパフォーマンスパネル]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


