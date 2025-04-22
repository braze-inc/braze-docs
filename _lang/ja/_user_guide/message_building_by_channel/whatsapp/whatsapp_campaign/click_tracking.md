---
nav_title: クリック追跡
article_title: クリック追跡
page_order: 5
description: "このリファレンス記事では、WhatsAppメッセージのクリックトラッキングをオンにする方法、短縮リンクをテストする方法、トラッキングリンクでカスタムドメインを使用する方法などについて説明します。"
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# クリックトラッキング

> このページでは、WhatsAppメッセージのクリックトラッキングをオンにする方法、短縮リンクをテストする方法、トラッキングリンクでカスタムドメインを使用する方法などについて説明します。

クリックトラッキングでは、誰かがWhatsAppメッセージのリンクをタップすると、どのコンテンツがエンゲージメントを促進しているかを明確に確認できます。ブレーズは、URL を短縮し、シーンの背後にトラッキングを追加し、クリックイベントが発生したときにログに記録します。

応答メッセージとテンプレートメッセージの両方で、クリックトラッキングをオンにできます。ボタンと本文テキストのリンクで動作し、パーソナライズされたURL とカスタムドメインをサポートします。オンにすると、WhatsAppのパフォーマンスレポートにクリックデータが表示され、誰が何をクリックしたかに基づいてユーザーをセグメンテーションできます。

{% alert important %}
WhatsAppのクリック追跡は現在初期アクセス中です。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## CDI の仕組み

### 応答メッセージ 

応答メッセージのクリック追跡を設定するには:
1. Web サイトのURL を含むアクション呼び出し(CTA) ボタンを含む応答メッセージを作成します。
2. インターフェースの指定したボタンをクリックして、クリックトラッキングを有効にします。

リンクは、Braze ドメイン、またはサブスクリプショングループに指定されたカスタムドメインに短縮され、ユーザーにカスタマイズされます。

`http://` または`https://` で始まる静的URLはすべて短縮される。流動的なパーソナライゼーション(ユーザーレベルのトラッキングターゲットなど) を含む短縮URL は、2 か月間有効です。

![コンテンツの本文とボタンを持つWhatsApp メッセージコンポーザー。][1]

### テンプレートメッセージ 

テンプレートメッセージの場合、クリックトラッキングを有効にするテンプレートを作成するときに、ベースURL を正しく送信する必要があります。

#### ステップ1:WhatsAppでクリックトラッキング対応のテンプレートを作成する

1. WhatsApp Manager で、カスタムドメインまたは`brz.ai` のいずれかのベースURL を作成します。
2. テンプレートに含まれるリンクがクリックトラッキングと互換性があることを確認します。
3. Braze でキャンペーンとして設定された後にテンプレート変数を変更しないでください。下流の変更は組み込めません。
4. CTA ボタンリンクの場合は、**Dynamic** を選択し、ベースURL (`brz.ai` またはカスタムドメイン) を指定します。<br><br>![アクションの呼び出しを作成するセクション。][2]<br><br>
5. 本文テキストのリンクの場合、WhatsApp Manager でテンプレートを記述するときに、追跡する本文に含まれているリンクの挿入済みスペースをすべて削除します。<br><br>![アクションを呼び出すためのコンテンツ本文を入力するテキストボックス。][3]

#### ステップ2: Braze でテンプレートを完成させる

作成時に、Braze は、本文とCTA ボタンの両方でサポート可能なURL ドメインを持つテンプレートを自動的に検出します。ステータスはテンプレートの下部に表示されます。 

!["Link Status"クリックトラッキングのアクティブなステータスを示すセクション。][4]{: style="max-width:70%;"}

- **対応リンク:**一致するベースURL を使用して送信されたリンクでは、クリックトラッキングが有効になります。
- **部分的にサポートされるリンク:**テンプレート内の一部のリンクが完全なURL として送信される場合は、**won't** をクリックしてこれらのリンクに適用します。
- **サポートされないリンク:**承認されたベースURL のないリンク**won't** には、クリックトラッキング機能があります。

宛先URL は、`brz.ai` またはカスタムドメインのいずれかに一致するベースURL を持つリンクに指定する必要があります。 

![" Buttons" ボタン名、ウェブサイトURL、トラッキングURL のフィールドを含むセクション。][5]{: style="max-width:70%;"}

{% multi_lang_include click_tracking.md section='カスタムドメイン' %}

## URL での Liquid パーソナライゼーション

Brazeコンポーザー内でURLをダイナミックに構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや在庫が戻った特定の商品にユーザーを誘導するなど）。
サポートされている任意のリキッドパーソナライゼーションタグを使用して、URL を動的に生成できます。

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、以下の例のように、カスタム定義の液体変数の短縮もサポートしています。

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid変数によってレンダリングされたURLを短縮する

Braze は、API トリガープロパティに含まれるURL でも、Liquid によってレンダリングされるURL を短縮します。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} が有効なURL を表す場合、WhatsApp メッセージを送信する前にそのURL を短縮して追跡します。

## テスト

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることをお勧めします。これを行うには、**Test** タブに移動してプレビューし、コンテンツテストグループまたは個々のユーザにWhatsApp を送信します。

このプレビューは、関連するパーソナライゼーションと短縮されたURL で更新されます。 

{% alert important %}
アクティブなキャンバス内にドラフトが作成された場合、短縮されたURL は生成されません。キャンバスドラフトがアクティブになると、実際の短縮URL が生成されます。
{% endalert %}

## レポート

クリックトラッキングが有効になっているか、サポートされているテンプレートで使用されている場合、WhatsAppパフォーマンステーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す列**Total Clicks**が含まれます。WhatsAppメトリクスの詳細については、[WhatsAppメッセージのパフォーマンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics#message-performance)を参照してください。

![WhatsApp Message Canvasステップ。][6]{: style="max-width:30%;"}

クリックデータは、分析ダッシュボードに自動的に報告されます。

![WhatsAppメッセージパフォーマンステーブル。][7]

## ユーザーのリターゲティング 

`Clicked/Opened Step` フィルタと`clicked tracked WhatsApp link` インタラクションを使用して、リンクとのインタラクションに基づいてユーザーをセグメント化できます。

![&quot のフィルタを使用してグループをフィルタリングします。クリックすると、追跡されたWhatsApp リンクとクォート;。][8]

{% multi_lang_include click_tracking.md section='よくある質問' %}

### URL をクリックしている個々のユーザーを特定することはできますか?

はい。クリック追跡が有効になっている(またはテンプレート設定に基づいて有効になっている) 場合は、WhatsApp のターゲット変更フィルタ、またはCurrents によって送信されたWhatsApp クリックイベント(`users.messages.whatsapp.Click`) を利用して、URL をクリックしたユーザーを再ターゲットできます。

### クリックトラッキングは、ディープリンクまたはユニバーサルリンクで機能しますか?

クリック追跡は、ディープリンクでは機能しません。BranchやAppsFlyerなどのプロバイダーからユニバーサルリンクを短縮することはできるが、Brazeでは、その際に発生する可能性のある問題（アトリビューションが壊れる、リダイレクトが発生するなど）のトラブルシューティングはできない。

### WhatsAppデバイスのプレビューはクリック数としてカウントされますか? 

いいえ、WhatsAppメッセージのクリック率には影響しません。 

[1]: {% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %}
[2]: {% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %}
[3]: {% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %}
[4]: {% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}
[5]: {% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}
[6]: {% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}
[7]: {% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %}
[8]: {% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %}

