---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "このリファレンス記事では、WhatsAppフローメッセージの作成と作成に関連するステップについて説明します。"
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsAppフローは、既存のWhatsApp チャネルを拡張したもので、インタラクティブでダイナミックな メッセージングなエクスペリエンスを作成できます。このページでは、アーリーアクセスプログラムに参加し、WhatsAppフローを使用するためのステップごとの手順について説明します。

## WhatsAppの流れの設定

1. Meta アカウントにログインします。
2. 2 つの主要な場所のいずれかからフローを作成します。
    - **アカウントツール:****Flows** タブに移動して、フローID を表示し、新しいフローを作成します。
    - **テンプレートの管理s:**これは、フローを作成する場合に推奨される方法です。ここでは、テンプレートs を生成し、テンプレート作成処理中にフローオプションを選択できます。

![「マネージャ」をWhatsAppしてフローテンプレートを作成します。]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

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

![サインアップを終了するユーザーのフォームを表示するプレビューウィンドウ。]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## フルフロー応答の保存 {#full-flow}

WhatsAppフローメッセージをBrazeキャンバスまたはキャンペーンに組み込む場合、ユーザーがフローを通じて送信する具体的な情報をキャプチャして活用することができます。Braze は、必要な階層化カスタム属性 (NCA) スキーマを生成するために、ユーザーレスポンスの構造、特にJSON レスポンスの予想される形状に関する追加情報を受け取る必要があります。

### ステップ 1: フローカスタム属性の生成

{% tabs local %}
{% tab Recommended method %}

レスポンス構造に関する情報をBrazeに与える最も簡単な方法は、フローレスポンスをカスタム属性として保存し、テスト送信を完了することです。

#### Brazeで使用されていないフローの使用

Braze 内で使用されていないフローを使用している場合、**メッセージの合成** の**フローカスタム属性** セクションを表示しても、情報が表示されないことがあります。つまり、スキーマはまだ生成されていません。

![メタフローセクション。フローカスタム属性を表示できます。]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

これを解決するには、次の手順を実行します。

1. WhatsApp表示ステップの設定を完了します。
2. **フローレスポンスをカスタム属性**として保存することを確認します。

![フロー応答をカスタム属性として保存するには、チェックボックスを持つメタフローセクション。]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\.テストメッセージを送信し、ユーザーとしてフローを完了します。

これで、Braze はフローレスポンスJSON のシェイプを持ち、カスタム属性を生成できます。

{% endtab %}
{% tab Alternative methods %}

高度なJSON エディタを使用して、フローレスポンスの属性をカスタム属性s に保存するか、マルチステップキャンバスを使用してレスポンスを階層化カスタム属性に保存します。 

{% subtabs %}
{% subtab Advanced JSON editor %}

高度なJSON エディタで、{% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} と入力します。ここで、“flow_1” はフローを保存するカスタム属性です。

![高度なJSONエディタを使用したユーザアップデートステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. オブジェクトデータタイプ("flow_1" のカスタム属性がワークスペースデータ設定s 内にすでに作成されていることを確認します。
2. UI エディタで、Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` を使用してカスタム属性に入力し、ユーザー全体のフローレスポンスを保存します。作成したカスタム属性を選択するには、キー値を```{{whats_app.${inbound_flow_response}}}```{% endraw %} として入力する必要があります。

![UI エディタを使用するユーザアップデートステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Braze がフローレスポンスを受信した後、指定された名前の階層化カスタム属性をユーザープロファイルに保存します。そのカスタム属性は、キャンバスを構築するときに引き出すことができます。 

!["flow_1" カスタム属性のコンテンツを表示するウィンドウ。]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 2:保存されたフロー応答を表示する

フローが完了すると、Braze はフローID に基づく名前のフローカスタム属性を自動的に作成します。その後、ユーザープロファイルに移動して、**カスタム属性** セクションのネストされたオブジェクトとして保存されたフローレスポンスを表示できます。

スキーマが生成された後、Flow **Custom Attribute** セクションには、応答ごとに予想されるデータ型("String" または"String Array" など) を含む期待される構造が表示されます。

![フローカスタム属性s の詳細ウィンドウ(スキーマドロップダウン)。]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### 考慮事項

- **既設属性s:**特定のフローのカスタム属性がすでに生成されている場合、フローには使用可能な属性情報が読み込むされます。このような場合、Braze は予期される応答メッセージをすでに認識しているため、スキーマを生成するためにテストメッセージを送信する必要はありません。
- **フローの変更:**スキーマの生成後にフローに変更を加えた場合は、Brazeがフローレスポンスのシェイプが変更されたことを理解し、それに応じて属性構成を調整できるように、追加のテストメッセージを送信する必要があります。このアクションは、24 時間ごとに1 回に制限されます。 
- **整合性**生成されるフローカスタム属性は一貫性があり、使用されているキャンバスに関係なく、この特定のフローの属性と同じになります。
- **手動オプション:****フローレスポンスをカスタム属性**として保存チェックボックスを選択する必要はありません。カスタム属性は、[フローレスポンスから特定のカスタム属性](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute)への特定のフィールドを保存することで手動で生成できます。これにより、ユーザー ステップsの重複を回避できます。

## フローレスポンスから特定のカスタム属性への特定のフィールドの保存 

### ステップ 1: アクションパスの作成

[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)キャンバスステップまたはアクションベースのキャンペーンを作成します。**WhatsApp着信メッセージを送信する**トリガーと**フロー**に応答する条件を選択し、該当するフローまたは**任意のフロー**を選択します。

![着信WhatsAppを送信してフローに応答したユーザーのトリガー。]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### ステップ 2:フローレスポンスからのフィールドの抽出

階層化カスタム属性 s または`json_parse` 液体タグを使用して、フローレスポンスから固有のフィールドs を抽出できます。

{% tabs %}
{% tab Nested custom attributes %}

ユーザーのフローレスポンスの特定の部分を保存するには、[フルフローレスポンスの保存](#full-flow)、**のすべてのステップをキャンバスの起動も含めて完了します。参照する階層化カスタム属性を作成するには、キャンバスを起動する必要があります。キャンバスを起動してフローを完了したら、次のステップを実行します。

1. UI エディタを使用する後続のユーザアップデートステップを作成します。
2. **Add Personalization**を選択し、**ネストされたカスタム属性**と、フローが保存されている対応する最上位属性を選択します。  

![ネストされたカスタム属性パーソナライゼーションを使用したユーザアップデートステップ。]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\.保存するキー属性を選択し、**キー値**フィールドに挿入します。

!["flow_1" のウィンドウで、属性がs から選択されます。]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. 保存する属性を選択します。
5. テストメッセージを送信してフローをテストします。

{% endtab %}
{% tab Parse function %}

`json_parse` 液体タグを使用して、フローから固有のレスポンスを抽出します。たとえば、フロートークンと選択したオプションを引き出して、フォローアップメッセージをカスタマイズできます。

UI エディタで、以下を選択します。 

- **属性名:** YOUR_CUSTOM_ATTRIBUTE (この例では: “First_name”)
- **アクション:**更新
- **キー値:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

!["パーソナライゼーション" コンポーネントを追加して、カスタム属性`inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %} でWhatsAppプロパティーパーソナライゼーションを挿入します。

準備ができたら、テストメッセージを送信してフローをテストします。それでは、キャンバスを起動してください！

{% endtab %}
{% endtabs %}

{% alert note %}
新しいWhatsAppメッセージは、液体フロー応答を使用(および再利用)するキャンバスの機能を「消去」します。そのため、すべてのユーザーアップデートステップs、webhook、または液体フロー応答を使用する他のステップs の後に、フォローアップメッセージがあることを確認してください。
{% endalert %}

## フローパーソナライゼーション タグの追加

[サポートされているパーソナライゼーション タグ s]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) で液体を通るフローレスポンスを使用するには、次のステップs を実行します。

1. WhatsAppを作成するときは、プラスアイコンを選択して**Add Personalization**ウィンドウを開封します
2. パーソナライゼーションの種類は** WhatsApp Properties**、カスタム属性は**inbound_flow_response**を選択します。これは、情報をユーザープロファイルs に保存したり、メッセージに含めたり、webhook などの他のサービスに転送したりするために使用できます。

!["パーソナライゼーション" コンポーネントを追加して、カスタム属性inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %} でWhatsAppプロパティーパーソナライゼーションを挿入します。{: style="max-width:80%;"}

質問またはその他のサポートについては、[Support]({{site.baseurl}}/braze_support/)にお問い合わせください。