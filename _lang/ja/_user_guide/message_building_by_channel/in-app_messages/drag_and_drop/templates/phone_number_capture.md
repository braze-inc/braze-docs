---
nav_title: SMSおよびWhatsAppサインアップフォーム
article_title: SMSおよびWhatsAppサインアップフォーム
alias: "/phone_number_capture/"
page_order: 1
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使ってSMSやWhatsAppの登録フォームを作成する方法をご紹介します。"
---

# SMSとWhatsAppのサインアップフォーム

> SMSおよびWhatsAppサインアップフォームは、アプリ内メッセージ用のドラッグアンドドロップエディターで利用できるテンプレートです。これらのテンプレートを使用してユーザーの電話番号を収集し、SMSおよびWhatsAppのサブスクリプショングループを成長させましょう。

![電話サインアップフォームテンプレートを使用して作成されたアプリ内メッセージの3つの例。][img7]

{% multi_lang_include drag_and_drop/templates.md section='SDKの要件' %}

## 電話番号登録フォームの作成

### ステップ 1: テンプレートを選ぶ

ドラッグアンドドロップのアプリ内メッセージを作成する際は、テンプレートに**SMS サインアップ**または **WhatsApp サインアップ**を選択し、[**メッセージを作成**] を選択します。これらのテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![アプリ内メッセージを作成する際に、SMSサインアップまたはWhatsAppサインアップをテンプレートとして選択するためのモーダル。][img2]{: style="max-width:70%"}

### ステップ 2: メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![カスタムフォントのアップロードと選択のワークフロー。][img6]

### ステップ 3: 電話番号入力コンポーネントをカスタマイズする

サインアップフォームの作成を開始するには、エディターで電話番号の入力コンポーネントを選択します。

![電話番号の入力コンポーネントを選択したサインアップフォーム作成時のプレビューエリア][img3]]{: style="max-width:40%"}

サイドメニューから、このテンプレートが電話番号を収集するサブスクリプショングループを指定します。コンプライアンスのベストプラクティスに従うために、電話番号のサインアップフォームごとに 1 つの購読グループに対する同意のみを収集できます。ただし、必要に応じて、他の購読グループの同意を収集するために複数のフォームを使用できます。

![サブスクリプショングループドロップダウンにサブスクリプショングループが選択されています。][img4]{: style="max-width:40%"}

デフォルトでは、グローバルに数値を収集しますが、収集する国の数は制限できます。これは、特定の国の電話番号を持つユーザーにのみメッセージを送信する場合に役立ち、リストの清潔さを保つのに役立ちます。そのためには、**すべての国から番号を収集する**をオフにして、ドロップダウンを使用して特定の国を選択します。ユーザーは、あなたが明示的に追加した国のみを選択できるようになります。

![国のドロップダウンから、番号を収集したい国を選択します。][img5]{: style="max-width:40%"}

#### 無効な電話番号

ユーザーが受け入れられない特殊文字を含む電話番号を入力した場合、カスタマイズできない一般的なエラー指標が表示され、フォームを送信できません。**プレビュー & テスト** タブおよびテストデバイスでエラーの動作を確認できます。この記事を参照して、[Brazeが電話番号をフォーマットする方法][2]を学んでください。

### ステップ 4: 免責事項の言語を追加する（SMSサインアップフォーム用）

SMSサインアップフォームでは、送信するSMSの種類を明確に伝えることが重要です。フォームに次の情報を含めることで、リストの増加がコンプライアンスに準拠していることを確認してください。

- お客様が受け取る可能性のあるSMSメッセージの種類の説明（カートのリマインダー、プロモーションやお得情報、予約のリマインダーなど）。すべてのユースケースを列挙する必要はありませんが、ブランドが送信するメッセージの種類について説明する必要があります。
- 同意は購入の条件ではないことに注意してください（該当する場合）。
- メッセージの頻度とメッセージおよびデータ料金が適用されることを思い出させる。正確なメッセージ頻度がわからない場合は、頻度が変動する可能性があると言うことができます。
- 利用規約およびSMSプライバシーポリシーへのリンク。
- ヘルプとオプトアウトキーワードのリマインダー（ヘルプの場合はHELP、キャンセルするにはSTOP）。

テンプレートにプレースホルダーの免責事項を例として提供していますが、これは法的助言を構成するものではなく、コンプライアンスの目的で依拠すべきではありません。法務チームと協力して、特定のブランドに合わせた文面を作成してください。

{% alert note %}
このドキュメントは、法律上の助言を提供することを意図したものではなく、完全に依存することもできません。
{% endalert %}

詳細については、[SMSの法律と規制][4]を参照してください。

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント][3]を使用して、メッセージの外観と感触をカスタマイズします。

## 結果を分析する

{% multi_lang_include drag_and_drop/templates.md section='レポート' %}

![アプリ内メッセージパフォーマンスパネルは、アプリ内メッセージ内の各リンクのクリック数を表示します。][img8]

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}
