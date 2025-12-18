---
nav_title: クリックトラッキング
article_title: クリック追跡
page_order: 3
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

クリックトラッキングでは、誰かがWhatsAppメッセージのリンクをタップすると、どのコンテンツがエンゲージメントを促進しているかを明確に確認できます。Braze により URL が短縮され、裏でトラッキング追跡が追加され、発生するクリックイベントがログに記録されます。

応答メッセージとテンプレートメッセージの両方で、クリックトラッキングをオンにできます。ボタンと本文テキストのリンクで動作し、パーソナライズされたURL とカスタムドメインをサポートします。オンにすると、WhatsAppのパフォーマンスレポートにクリックデータが表示され、誰が何をクリックしたかに基づいてユーザーをセグメンテーションできます。

{% alert note %}
クリック追跡は、ディープリンクでは機能しません。BranchやAppsFlyerなどのプロバイダーからユニバーサルリンクを短縮することはできるが、Brazeでは、その際に発生する可能性のある問題（アトリビューションが壊れる、リダイレクトが発生するなど）のトラブルシューティングはできない。
{% endalert %}

## 仕組み

### 応答メッセージ 

応答メッセージのクリック追跡を設定するには、次のようにします。
1. Web サイトのURL を含むアクション呼び出し(CTA) ボタンを含む応答メッセージを作成します。
2. インターフェースの指定したボタンをクリックして、クリックトラッキングを有効にします。

リンクは、Braze ドメイン、またはサブスクリプショングループに指定されたカスタムドメインに短縮され、ユーザーにカスタマイズされます。

`http://` または`https://` で始まる静的URLはすべて短縮される。流動的なパーソナライゼーション(ユーザーレベルのトラッキングターゲットなど) を含む短縮URL は、2 か月間有効です。

![内容物本体とボタン付きのWhatsApp メッセージ作成画面。]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### テンプレートメッセージ 

テンプレートメッセージの場合、クリックトラッキングを有効にするテンプレートを作成するときに、ベースURL を正しく送信する必要があります。

#### ステップ1:WhatsAppでクリックトラッキング対応のテンプレートを作成する

1. WhatsApp Manager で、カスタムドメインまたは`brz.ai` のいずれかのベースURL を作成します。
2. テンプレートに含まれるリンクがクリックトラッキングと互換性があることを確認します。
3. Braze でキャンペーンとして設定された後にテンプレート変数を変更しないでください。下流の変更は組み込めません。
4. CTA ボタンリンクの場合は、**Dynamic** を選択し、ベースURL (`brz.ai` またはカスタムドメイン) を指定します。<br><br>![アクション の呼び出しを作成する項目。]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. 本文テキストのリンクの場合、WhatsApp Manager でテンプレートを記述するときに、追跡する本文に含まれているリンクの挿入済みスペースをすべて削除します。<br><br>![アクションを呼び出すための内容の本文を入力するテキストボックス。]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### ステップ 2:Braze でテンプレートを完成させる

作成時に、Braze は、本文とCTA ボタンの両方でサポート可能なURL ドメインを持つテンプレートを自動的に検出します。ステータスはテンプレートの下部に表示されます。 

!["Link ステータス"クリック"トラッキングの有効なステータスを示す節。]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **対応リンク:**一致するベースURL を使用して送信されたリンクでは、クリックトラッキングが有効になります。
- **部分的にサポートされるリンク:**テンプレート内の一部のリンクが完全な URL として送信される場合、これらのリンクにはクリック追跡が適用**されません**。
- **サポートされていないリンク:**承認済みのベース URL がないリンクには、クリック追跡機能が**含まれません**。

宛先URL は、`brz.ai` またはカスタムドメインのいずれかに一致するベースURL を持つリンクに指定する必要があります。 

!["Buttons"ボタンの名前、Web サイト URL、および"トラッキング URL のフィールドがs のセクション。]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## URL での Liquid パーソナライゼーション

Brazeコンポーザー内でURLをダイナミックに構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや在庫が戻った特定の商品にユーザーを誘導するなど）。
サポートされている任意のリキッドパーソナライゼーションタグを使用して、URL を動的に生成できます。

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、次の例に示すようなカスタム定義の Liquid 変数の短縮もサポートしています。

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid変数によってレンダリングされたURLを短縮する

Liquid によってレンダリングされる URL は、API トリガーのプロパティに含まれている場合でも短縮されます。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} が有効なURL を表す場合、WhatsApp メッセージを送信する前にそのURL を短縮して追跡します。

## テスト

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることをお勧めします。そのためには、[**テスト**] タブに移動し、WhatsApp メッセージをプレビューして、コンテンツテストグループまたは個々のユーザーに送信します。

このプレビューは、関連するパーソナライゼーションと短縮されたURL で更新されます。 

{% alert important %}
アクティブなキャンバス内にドラフトが作成された場合、短縮されたURL は生成されません。実際に短縮されたURL は、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

## レポート

クリックトラッキングが有効になっているか、サポートされているテンプレートで使用されている場合、WhatsAppパフォーマンステーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す列**Total Clicks**が含まれます。WhatsAppメトリクスの詳細については、[WhatsAppメッセージのパフォーマンス]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics)を参照してください。

![メッセージキャンバスステップをWhatsAppします。]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

クリックデータは、分析ダッシュボードに自動的に報告されます。

![WhatsApp電文パフォーマンステーブル。]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## ユーザーのリターゲティング 

`Clicked/Opened Step` フィルタと`clicked tracked WhatsApp link` インタラクションを使用して、リンクとのインタラクションに基づいてユーザーをセグメント化できます。

![&quot のフィルターを持つフィルター群。クリックされたトラッキングされたWhatsAppのリンクとクォート。]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URL をクリックしている個々のユーザーを特定することはできますか?

はい。クリック追跡が有効になっている(またはテンプレート設定に基づいて有効になっている) 場合は、WhatsApp のターゲット変更フィルタ、またはCurrents によって送信されたWhatsApp クリックイベント(`users.messages.whatsapp.Click`) を利用して、URL をクリックしたユーザーを再ターゲットできます。

### WhatsAppデバイスのプレビューはクリック数としてカウントされますか? 

いいえ、WhatsAppメッセージのクリック率には影響しません。 

