---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "この参考記事は、WhatsApp Flowsメッセージを構築し作成するステップを説明する。"
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flowsは既存のWhatsAppチャネルを強化する機能であり、インタラクティブでダイナミックなメッセージング体験を構築することを可能にする。このページでは、WhatsApp Flowsの使用方法をステップごとに説明する。

## WhatsApp Flowsの設定

1. Metaアカウントにログインする。
2. フローは主に二つの場所から作成する：
    - **アカウントツール：****フロー**タブに移動してフローIDを確認し、新しいフローを作成する。
    - **テンプレートの管理：**これがフローを作成するための推奨方法だ。ここでは、テンプレートを生成でき、テンプレート作成プロセス中にフローオプションを選択できる。

![WhatsAppマネージャーにはフローテンプレートを作成するページがある。]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\.既存のフローを選択するか、新規に作成する。フローを作成する場合、次の2つの選択肢から選ぶ：
  - **カスタムフォーム：**特定の要件については
  - **あらかじめデザインされた要素：**より速い設定のために

## WhatsApp Flowのメッセージと応答の設定

{% tabs local %}
{% tab Template message %}

1. Braze キャンバス内で、該当するフローを含むテンプレートメッセージを使用するWhatsApp メッセージステップを作成する。
2. テンプレートの作成を続けろ。必要なら、メッセージにメディアや可変コンテンツ、あるいはその両方を含めろ。フローの選択はテンプレート作成時に決定されるため、フロー体験に関する追加情報は不要だ。

![WhatsApp Flowテンプレートを使用したWhatsAppメッセージ作成画面。]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Braze キャンバスで、返信メッセージとフローメッセージを使用するWhatsAppメッセージステップを作成する。

![WhatsAppの返信メッセージタイプとフローメッセージレイアウトのためのメッセージステップだ。]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\.該当するフローを選択し、メッセージの作成を続ける。 

![フローメッセージ応答作成画面で、フローを選択するための拡張ドロップダウンを備えている。]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### フローをプレビュー

フロー付きのキャンバスを起動する前に、**[フローのプレビュー]**を選択できる。これにより、Braze内で直接フローをプレビューし、期待通りに動作することを確認できる。プレビュー画面でフローを操作することもできる。ユーザーがどのようにフローをナビゲートするか体験し、リアルタイムで調整を加えられる。フローに複数のページが含まれている場合、各ページとやり取りできる。

![ユーザーが登録を完了するためのフォームを表示するプレビューウィンドウ。]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## フロー応答全体を保存する {#full-flow}

WhatsApp FlowメッセージをBraze キャンバスやキャンペーンに組み込む際、ユーザーがFlowを通じて送信する特定の情報を取得して活用したい場合がある。Brazeは、必要な階層化カスタム属性（NCA）スキーマを生成するために、ユーザー応答の構造に関する追加情報、特にJSON応答の期待される形状を受け取る必要がある。

### ステップ 1: フローのカスタム属性を生成する

{% tabs local %}
{% tab Recommended method %}

レスポンス構造に関する情報をBrazeに提供する最も簡単な方法は、フローのレスポンスをカスタム属性として保存し、テスト送信を完了させることだ。

#### Brazeで使用されていないフローを使用する

Braze内で以前に使用されたことがないフローを使用している場合、**メッセージ作成**画面の**「フローカスタム属性」**セクションを表示しても、情報が表示されないことがある。これはスキーマがまだ生成されていないことを意味する。

![メタフローセクションには、フローのカスタム属性を表示するオプションがある。]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

これを解決するには、次のことを行え：

1. WhatsAppメッセージの設定のステップを完了する。
2. **フローの応答をカスタム属性として保存する**設定を確認したか確認せよ。

![メタフローセクションには、フローの応答をカスタム属性として保存するためのチェックボックスがある。]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\.テストメッセージを自分に送信し、ユーザーとしてフローを完了する。

さて、Brazeはフロー応答JSONの形式を取得し、カスタム属性を生成できる。

{% endtab %}
{% tab Alternative methods %}

高度なJSONエディターを使って、フローの応答から属性値をカスタム属性に保存する。あるいは、複数ステップのキャンバスを使って、応答を階層化カスタム属性に保存する。 

{% subtabs %}
{% subtab Advanced JSON editor %}

高度なJSONエディタで、\`{% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %},`を入力する。ここで`,`はフローを保存“flow_1”したいカスタム属性である。

![高度なJSONエディタを備えたユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. ワークスペースのデータ設定内で、オブジェクトデータ型("flow_1"（この例では）のカスタム属性を既に作成していることを確認せよ。
2. UIエディタでは、カスタム属性を埋める{% raw %}```{{whats_app.${inbound_flow_response}}}```ためにLiquidを使用し、ユーザーのフロー応答全体をそこに保存する。作成したカスタム属性を選択する前に```{{whats_app.${inbound_flow_response}}}```{% endraw %}、キー値を事前に設定しておく必要がある。

![UIエディタを使用するユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

BrazeがFlowからの応答を受信した後、指定された命名規則に従って階層化カスタム属性をユーザープロファイルに保存する。そのカスタム属性はキャンバスを作成する際に取得できる。 

![カスタム"flow_1"属性の内容を表示するウィンドウ。]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 2:保存されたフロー応答を表示する

フローが完了すると、Brazeは自動的にフローIDを基にした名前のフローカスタム属性を生成する。その後、ユーザープロファイルに移動し、**カスタム属性**セクション内のネストされたオブジェクトとして保存されたフロー応答を確認できる。

スキーマが生成されると、フローの**カスタム属性**セクションには、各応答に対する想定されるデータ型（例えば「文字列」や「文字列配列」）を含む、期待される構造が表示される。

![フローのカスタム属性詳細ウィンドウにスキーマのドロップダウンを表示する。]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### 考慮事項

- **既存の属性：**特定のフローに対してカスタム属性が既に生成されている場合、そのフローは属性情報と共に読み込まれる。これらのケースでは、スキーマを生成するためにテストメッセージを送信する必要はない。Brazeは既に想定される応答メッセージを認識しているからだ。
- **流れの変化：**フローのスキーマ生成後にフローに変更を加えた場合、追加のテストメッセージを送信しなければならない。これによりBrazeはフロー応答の構造が変更されたことを認識し、属性構造を適切に調整できる。このアクションは24時間に1回のみ行える。 
- **一貫性：**生成されたフローのカスタム属性は一貫しており、使用されるキャンバスに関わらず、この特定のフローに対して同じ属性となる。
- **手動オプション：****「フローの回答をカスタム属性として保存する**」チェックボックスを選択する必要はない。[フローの応答から特定のフィールドを特定のカスタム属性に保存](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute)することで、カスタム属性を手動で生成できる。これにより、ユーザーのステップを重複させる必要がなくなる。

## フローの応答から特定のフィールドを特定のカスタム属性に保存する 

### ステップ 1: アクションパスを作成する

[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)キャンバスステップか、アクションベースのキャンペーンを作成する。**WhatsApp受信メッセージ送信**トリガーと**応答済みフロー**条件を選択し、関連するフローまたは**任意のフロー**を選択する。

![WhatsAppで受信メッセージを送信し、いずれかのフローに応答したユーザー向けのトリガーである。]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### ステップ 2:フロー応答からフィールドを抽出する

Flowの応答から特定のフィールドを抽出するには、階層化カスタム属性かLiquid`json_parse`タグを使用できる。

{% tabs %}
{% tab Nested custom attributes %}

ユーザーのフロー応答の特定部分を保存するには、[フルフロー応答の保存](#full-flow)のステップをすべて完了させる必要がある。**これにはキャンバスの起動も含まれる**。参照する階層化カスタム属性を作成するには、キャンバスを起動しなければならない。キャンバスを起動し、フローを完了したら、次のステップを実行する：

1. UIエディタを使用する後続のユーザー更新ステップを作成する。
2. **「パーソナライゼーションの追加」**を選択し、次に**「階層化カスタム属性**」と、フローが保存されている対応する最上位属性を選択する。  

![ユーザー更新ステップに、階層化カスタム属性のパーソナライゼーションを適用する。]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\.保存したいキー属性を選択し、その**キー値**フィールドにLiquidを挿入する。

![属性から選択"flow_1"するウィンドウ。]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. それを保存したい属性を選ぶんだ。
5. フローをテストするためにテストメッセージを送信する。

{% endtab %}
{% tab Parse function %}

Liquid`json_parse`タグを使って、フローから特定の応答を抽出する。例えば、フロートークンと選択したオプションを取り出して、フォローアップメッセージをカスタマイズできる。

UIエディタで、以下の項目を選択する： 

- **属性名:**YOUR_CUSTOM_ATTRIBUTE(この例では: “First_name”)
- **アクション:**更新
- **キー値：** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsAppメッセージ作成画面に「パーソナライゼーションを追加」コンポーネントを組み込み、カスタム属性/assets/img/whatsapp/flows/parsed_json.pngimage_buster`inbound_flow_response`.]({%    %}) を含むWhatsAppプロパティのパーソナライゼーションを挿入する。

準備ができたら、フローをテストするためにテストメッセージを送れ。さあ、キャンバスを始めよう！

{% endtab %}
{% endtabs %}

{% alert note %}
新しいWhatsAppメッセージは、CanvasがLiquid Flowの応答を使用（および再利用）する機能を「クリア」する。したがって、フォローアップメッセージは、すべてのユーザー更新ステップ、Webhook、またはLiquid Flowの応答を使用するその他のステップの後に行われるようにすること。
{% endalert %}

## フローのパーソナライゼーションタグを追加する

Liquidを通じてFlowレスポンスを使用し、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を活用するには、次のステップを完了する：

1. WhatsAppのメッセージを作成する際は、プラスアイコンを選択して**「パーソナライゼーションを追加」**ウィンドウを開く。
2. パーソナライゼーションタイプには**WhatsAppプロパティ**を選択し、カスタム**inbound_flow_response**属性にはWhats**Appプロパ**ティを選択する。これはユーザープロファイルへの情報保存、メッセージングへの組み込み、あるいはWebhookなどの他のサービスへの転送に利用できる。

![WhatsAppメッセージ作成画面に「パーソナライゼーションを追加」コンポーネントを組み込み、カスタム属性/assets/img/whatsapp/flows/inbound_flow_response.pngimage_busterinbound_flow_response.]({%    %}) を含むWhatsAppプロパティのパーソナライゼーションを挿入する。{: style="max-width:80%;"}

質問や追加のサポートが必要な場合は、[サポートに]({{site.baseurl}}/braze_support/)連絡する。