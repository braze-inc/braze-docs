---
nav_title: 埋め込みサインアップ
article_title: WhatsApp 埋め込みサインアップ
page_order: 0
description: "このリファレンス記事では、Braze のWhatsApp 埋め込みサインアップワークフローのステップ-by-ステップのチュートリアルについて説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp埋め込みサインアップ

> このリファレンス記事では、Braze のWhatsApp 埋め込みサインアップワークフローのステップ-by-ステップのチュートリアルについて説明します。

WhatsApp の埋め込みサインアップワークフローは、最初に Braze ワークスペースに [WhatsApp を統合]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)したとき、および [WhatsAppのビジネスアカウント]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)を既存の WhatsApp 連携に追加するときにアクセスされます。

{% alert note %}
Braze ワークスペースに[複数の WhatsApp Business アカウント](({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/))を追加できます。ただし、各 WhatsApp Business アカウントは 1 つの Braze ワークスペースにのみ追加できます。
{% endalert %}

## ワークフローへのアクセス

**Partner Integrations**> **Technology Partners**に進み、**WhatsApp**を検索して選択します。次に選択する内容は、ユースケースによって異なります。

- WhatsApp をワークスペースに統合する場合は、**統合を開始** を選択します。<br><br>![連携開始ボタンがある WhatsApp パートナーページ。]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- 既存のWhatsAppインテグレーションにWhatsAppの法人取引先を追加する場合は、**WhatsAppの法人取引先を追加**を選択します。<br><br>![WhatsApp Business アカウントまたは購読グループと番号を追加するオプションがある [WhatsApp メッセージング統合]。]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

ここからの作業フローは、両方のユースケースs で同じです。

## WhatsApp埋め込みサインアップワークフロー

1. Meta (Facebook) ログインウィンドウで、**Login as** または **Continue** を選択します。<br><br>![Meta ログインウィンドウ。]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Braze と共有する権限を読み、**Get Started** を選択します。<br><br>![連携のために Braze と共有する権限のリスト。]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. **ビジネスポートフォリオ** ドロップダウンで、ビジネスポートフォリオを選択し、**Next** を選択します。これにより、WhatsAppビジネスアカウントに接続されるため、期待するビジネスポートフォリオが表示されない場合は、権限を確認します。<br><br>![ビジネスポートフォリオ名など、ビジネス情報を入力するフィールドを含むウィンドウ。]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. ドロップダウン・フィールドsで以下を選択し、**Next**を選択します。
- **WhatsAppの取引先を選択します**:WhatsApp Business アカウントを作成します
- **WhatsApp Business プロファイルの作成**: 新しい WhatsApp Business プロファイルを作成します <br><br>![WhatsApp Business アカウントとプロファイルを選択または作成するかどうかを指定するフィールド。]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. 以下を入力し、**Next**を選択します。
- WhatsApp Business アカウント名
- WhatsApp Business 表示名
- カテゴリー <br><br>![新しい WhatsApp Business アカウントの詳細を入力するフィールド]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. 電話番号を入力し、**テキストメッセージ**または**電話コール**のいずれかを選択します。この番号は、他のWhatsAppアカウントに登録されていないことも含め、WhatsAppの電話番号のすべての要求事項に従う必要があります。<br><br>![電話番号を追加するフィールド。]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. 2 要素認証 コードを入力し、**Next**を選択します。<br><br>![2 要素認証コードの入力フィールド。]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. WhatsAppビジネスアカウントが受信する権限を確認し、**Continue**を選択します。<br><br>![WhatsApp Business アカウントによって要求される権限のリスト]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. 完了です！<br><br>![ユーザーにメッセージできる準備ができたことを示すウィンドウ。]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}

