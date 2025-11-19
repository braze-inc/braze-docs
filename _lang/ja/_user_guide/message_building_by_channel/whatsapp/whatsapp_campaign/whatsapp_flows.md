---
nav_title: WhatsApp フロー
article_title: WhatsApp フロー
page_order: 1
description: "このリファレンス記事では、WhatsAppフローメッセージの作成と作成に関連するステップについて説明します。"
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp フロー

> WhatsAppフローは、既存のWhatsApp チャネルを拡張したもので、インタラクティブでダイナミックな メッセージングなエクスペリエンスを作成できます。このページでは、アーリーアクセスプログラムに参加し、WhatsAppフローを使用するためのステップごとの手順について説明します。

## WhatsAppの流れの設定

1. Meta アカウントにログインします。
2. 2 つの主要な場所のいずれかからフローを作成します。
    - **アカウントツール:****Flows** タブに移動して、フローID を表示し、新しいフローを作成します。
    - **テンプレートの管理s:**これは、フローを作成する場合に推奨される方法です。ここでは、テンプレートs を生成し、テンプレート作成処理中にフローオプションを選択できます。

![マネージャをWhatsAppして、フローテンプレートを作成します。]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\.既存のフローを選択するか、作成します。フローを作成する場合は、次の2 つのオプションから選択します。
  - **カスタムフォーム:**特定の要件については
  - **設計済みエレメント:**セットアップを迅速に行うには

## WhatsAppフローメッセージとレスポンスの設定

{% tabs local %}
{% tab Template message %}

1. Brazeキャンバスで、それぞれのフローを含むテンプレートメッセージを使用するWhatsAppメッセージステップを作成します。
2. テンプレートの作成を続行します。必要に応じて、メッセージにメディア、変数コンテンツ、またはその両方を追加します。フロー選択は、テンプレートが行われたときに選択されるため、フローエクスペリエンスの追加情報は必要ありません。

![WhatsApp流量テンプレートを使用したWhatsApp メッセージ作成画面。]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Brazeキャンバスで、レスポンスメッセージとフローメッセージを使用するWhatsAppメッセージステップを作成します。

![WhatsAppレスポンスメッセージタイプとフローメッセージレイアウトのメッセージステップ。]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\.それぞれのフローを選択し、メッセージの作成を続行します。 

![フローを選択するための拡張ドロップダウンを持つフローメッセージ応答コンポーザー。]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### フローをプレビュー

フローを使用してキャンバスを起動するには、** プレビュー Flow** を選択して、Braze でフローを直接的にプレビューし、期待どおりに動作することを確認します。また、プレビューのフローを操作して、ユーザーがフローをナビゲートする方法を体験し、リアルタイムで調整することもできます。フローに複数のページが含まれている場合は、各ページを操作できます。

![ユーザーの登録が完了するフォームを表示するプレビュー画面。]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## フルフロー応答の保存 {#full-flow}

### ステップ 1: アクションパスの作成

[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)キャンバスステップまたはアクションベースのキャンペーンを作成します。**WhatsApp着信メッセージを送信する**トリガーと**フロー**に応答する条件を選択し、該当するフローまたは**任意のフロー**を選択します。

![着信WhatsAppを送信し、フローに応答したユーザーのトリガー。]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### ステップ 2: WhatsAppメッセージを作成する

WhatsAppを作成するときは、**パーソナライゼーション**ウィンドウを開封するプラスアイコンを選択し、パーソナライゼーションの種類は**WhatsAppのプロパティー**を、カスタム属性は**inbound_flow_response**を選択します。これにより、情報がユーザープロファイルs に保存されたり、webhook などの他のサービスに転送されたりします。

![WhatsApp メッセージ作成画面 with "パーソナライゼーション" コンポーネントを追加して、カスタム属性`inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %} のWhatsAppプロパティーパーソナライゼーションを挿入します。{: style="max-width:60%;"}

### ステップ 3: フルフロー応答を保存する

高度なJSON エディタを使用して、フローレスポンスの属性をカスタム属性s に保存したり、マルチステップキャンバスを使用してレスポンスを階層化カスタム属性に保存したりできます。 

{% tabs %}
{% tab Advanced JSON editor %}

高度なJSON エディタで、{% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} と入力します。ここで、“flow_1” はフローを保存するカスタム属性です。

![高度なJSONエディタを使用したユーザアップデートステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endtab %}
{% tab UI editor %}

1. オブジェクトデータタイプ("flow_1" のカスタム属性がワークスペースデータ設定s 内にすでに作成されていることを確認します。
2. UI エディタで、Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` を使用してカスタム属性に入力し、ユーザー全体のフローレスポンスを保存します。作成したカスタム属性を選択するには、キー値を```{{whats_app.${inbound_flow_response}}}```{% endraw %} として入力する必要があります。

![ユーザーエディターを使用するユーザーアップデートステップ]]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Braze がフローレスポンスを受信した後、指定された名前の階層化カスタム属性をユーザープロファイルに保存します。そのカスタム属性は、キャンバスを構築するときに引き出すことができます。 

!["flow_1"カスタム属性の内容を表示するウィンドウ。]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endtab %}
{% endtabs %}

準備ができたら、テストメッセージを送信してフローをテストします。それでは、キャンバスを起動してください！

## フローレスポンスから特定のカスタム属性への特定のフィールドの保存 

階層化カスタム属性 s または`json_parse` 液体タグを使用して、フローレスポンスから固有のフィールドs を抽出できます。

{% tabs %}
{% tab Nested custom attributes %}

ユーザーのフローレスポンスの特定の部分を保存するには、[フルフローレスポンスの保存](#full-flow)、**のすべてのステップをキャンバスの起動も含めて完了します。参照する階層化カスタム属性を作成するには、キャンバスを起動する必要があります。キャンバスを起動してフローを完了したら、次のステップを実行します。

1. UI エディタを使用する後続のユーザアップデートステップを作成します。
2. **Add Personalization**を選択し、**ネストされたカスタム属性**と、フローが保存されている対応する最上位属性を選択します。  

![ネストされたカスタム属性パーソナライゼーションを使用したユーザアップデートステップ。]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\.保存するキー属性を選択し、**キー値**フィールドに挿入します。

!["flow_1" のウィンドウ。属性 s で選択します。]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\.保存する属性を選択します。
5. テストメッセージを送信してフローをテストします。

{% endtab %}
{% tab Parse function %}

`json_parse` 液体タグを使用して、フローから固有のレスポンスを抽出します。たとえば、フロートークンと選択したオプションを引き出して、フォローアップメッセージをカスタマイズできます。

### ステップ 1: アクションパスの作成

[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)を**WhatsApp受信メッセージ**トリガーで作成し、フロー情報を処理します。

{% alert note %}
早期アクセス時に追加機能がリリースされると、フローを指定できるようになります。
{% endalert %}

### ステップ 2: WhatsAppメッセージを作成する

WhatsAppを作成するときは、**パーソナライゼーション**ウィンドウを開封するプラスアイコンを選択し、パーソナライゼーションの種類は**WhatsAppのプロパティー**を、カスタム属性は**inbound_flow_response**を選択します。これにより、情報がユーザープロファイルs に保存されたり、webhook などの他のサービスに転送されたりします。

### ステップ 3: フローレスポンスから指定したフィールドを保存する

UI エディタで、以下を選択します。 

- **属性名:** YOUR_CUSTOM_ATTRIBUTE (この例では: “First_name”)
- **アクション:**更新
- **キー値:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp メッセージ作成画面 with "パーソナライゼーション" コンポーネントを追加して、カスタム属性`inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %} のWhatsAppプロパティーパーソナライゼーションを挿入します。

{% alert note %}
新しいWhatsAppメッセージは、液体フロー応答を使用(および再利用)するキャンバスの機能を「消去」します。そのため、すべてのユーザーアップデートステップs、webhook、または液体フロー応答を使用する他のステップs の後に、フォローアップメッセージがあることを確認してください。
{% endalert %}

準備ができたら、テストメッセージを送信してフローをテストします。それでは、キャンバスを起動してください！

{% endtab %}
{% endtabs %}

{% alert note %}
フロー要素を組み込んだ高度なアクション ステップ フィルターやレスポンスメッセージを含む、追加のフロー機能が導入されます。
{% endalert %}

質問またはその他のサポートについては、[Support]({{site.baseurl}}/braze_support/)にお問い合わせください。