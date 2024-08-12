---
nav_title: リンクテンプレート
article_title: リンクテンプレート
page_order: 4
description: "この記事では、メールにさまざまなタイプのリンクテンプレートを作成する方法について説明します。"
tool:
  - Templates
channel:
  - email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/creating-link-templates){: style="float:right;width:120px;border:0;" class="noimgborder"}リンクテンプレート

> リンクテンプレートを使用すると、メールメッセージ内のすべてのリンクにパラメーターを追加したり、URLを先頭に追加したりできます。

リンクテンプレートは、次のユースケースで最もよく使用されます。

1. Google アナリティクスのクエリ パラメータを特定のメール メッセージ内のすべてのリンクに追加する
2. 特定の電子メール メッセージ内のすべてのリンクへの URL を先頭に追加する

{% alert note %}
リンクテンプレートはオプション機能です。[**テンプレート**] セクションに **[メールリンクテンプレート**] が表示されない場合は、アカウント マネージャーに連絡してこの機能を有効にしてください。
{% endalert %}

## リンクテンプレートの作成

![][11]{: style="float:right;max-width:20%;"}

さまざまなニーズに対応するために、リンクテンプレートを無制限に作成できます。リンクテンプレートを作成するには:

1. **[テンプレート**] > **[メールリンクテンプレート**] に移動します。 
2. 「 **リンクテンプレートの作成**」をクリックします。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは **[Engagement** > **Templates & Media** > **Link Templates** にあります。
{% endalert %}

作成できるリンク テンプレートには、次の 2 種類があります。

- [URL の前に挿入するリンクテンプレート](#prepend-link-template)
- [URL の後に挿入するリンクテンプレート](#append-link-template)

リンクテンプレートと [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を使用する場合、レンダリングの一貫性を確保するために、Liquidはbodyタグ内にのみ追加する必要があります。

### 付加：URL の前に挿入するリンクテンプレートを作成する {#prepend-link-template}

電子メール メッセージ内のリンクの前に文字列または URL を追加する場合は、新しいリンク テンプレートを作成し、[ **テンプレートの位置** ] を **[URL の前**] に設定します。次に、URLの先頭に必ず付加される文字列を入力します。 

挿入プロセスの例を示すプレビュー セクションが用意されています。

![Template Position, Prepend URL, and Template Preview fields for the link template insertion process before a URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### 追加：URL の後に挿入するリンクテンプレートを作成する {#append-link-template}

電子メール メッセージの URL の後にクエリ パラメーターを追加する場合は、新しいリンク テンプレートを作成し、[ **テンプレートの位置** ] を **[URL の後**] に設定します。次に、各 URL の末尾にクエリ パラメーター ()`value=something` を入力します。

URL の末尾に複数のパラメーターを追加できます。

![Template Position, Query Parameters, and Template Preview fields for the link template insertion process after a URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## メールキャンペーンでのリンクテンプレートの使用

リンクテンプレートを設定したら、メールで使用するテンプレートを選択できます。

- **HTML エディター:**[**コンテンツ**]セクションの[**リンク管理**]タブに移動します。「 **リンク・テンプレートの追加**」をクリックし、リンク・テンプレートを選択して、「 **追加**」をクリックします。

{% alert important %}
更新された HTML メールエディタで「 **リンク管理** 」タブにアクセスするには、リンクエイリアスをオンにする必要があります。リンク エイリアシングを有効にするには、アカウント マネージャーにお問い合わせください。
{% endalert %}

- **ドラッグ&ドロップエディタ:****「コンテンツ**>**リンク管理**」タブを選択します。「 **リンク・テンプレートの追加**」をクリックします。ドラッグ&ドロップエディタでリンクテンプレートにアクセスするには、 [リンクエイリアス]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) をオンにする必要があります。

![ドラッグ&ドロップエディタのリンク管理タブとリンクテンプレートのリストの例][1]

[ **リンク管理** ] タブでリンクテンプレートを追加したら、右にスクロールして追加したテンプレートを表示します。

## リンク・テンプレートの管理

リンクテンプレートを [複製]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) することもできます。テンプレートとクリエイティブコンテンツの作成と管理の詳細については、「 [テンプレートとメディア]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)」を参照してください。

{% alert important %}
アーカイブテンプレートは、現在、リンクテンプレートでは使用できません。
{% endalert %}

## よくある質問

リンクテンプレートに関するよくある質問の回答については、[テンプレートに関するFAQ][10]ページをご覧ください。

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
