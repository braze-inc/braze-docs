---
nav_title: リンクテンプレート
article_title: リンクテンプレート
page_order: 4
description: "この記事では、Eメールにさまざまなタイプのリンクテンプレートを作成する方法について説明する。"
tool:
  - Templates
channel:
  - email

---

# リンクテンプレート

> リンクテンプレートでは、Eメールメッセージ内のすべてのリンクにパラメータを追加したり、URLの先頭に追加したりすることができる。

リンク・テンプレートは、以下のような使用例でよく使われる：

1. 指定したメールメッセージ内のすべてのリンクにGoogle Analyticsのクエリパラメータを追加する
2. 指定したEメールメッセージ内のすべてのリンクにURLを付加する

{% alert note %}
リンクテンプレートはオプション機能である。**Templates**セクションに**Email Link Templates が**ない場合は、アカウントマネージャーに連絡して機能をオンにしてもらう。
{% endalert %}

## リンクテンプレートを作成する

![][11]{: style="float:right;max-width:20%;"}

リンクテンプレートは無制限に作成でき、様々なニーズに対応できる。リンクテンプレートを作成する：

1. [**テンプレート**] > [**メールリンクテンプレート**] に移動します。 
2. [**リンクテンプレートの作成**] をクリックします。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは [**エンゲージメント**] > [**テンプレートとメディア**] > [**リンクテンプレート**] にあります。
{% endalert %}

作成できるリンクテンプレートには2種類ある：

- [URLの前に挿入するリンクテンプレート](#prepend-link-template)
- [URLの後に挿入するリンクテンプレート](#append-link-template)

リンクテンプレートと [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) を使用する場合、一貫したレンダリングを保証するために、Liquid は body タグ内にのみ追加する必要があります。

### 先頭に追加: URLの前に挿入するリンクテンプレートを作成する {#prepend-link-template}

メールメッセージのリンクの前に文字列やURLを追加したい場合は、新しいリンクテンプレートを作成し、「**テンプレートの位置**」を「**URLの前**」に設定する。次に、URLの前に常に付加される文字列を入力する。 

挿入プロセスの例を示すプレビューセクションが提供されます。

![URLの前にリンクテンプレートを挿入する際の「テンプレートの位置」、「URLのプリペンド」、「テンプレートのプレビュー」フィールド。]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### 追加: URLの後に挿入するリンクテンプレートを作成する {#append-link-template}

メールメッセージのURLの後にクエリパラメータを追加したい場合は、新しいリンクテンプレートを作成し、「**Template Position**」を「**After URL**」に設定する。次に、各 URL の末尾にクエリパラメーター (`value=something`) を入力します。

URLの末尾に複数のパラメーターを付加することができる。

![URL後のリンクテンプレート挿入処理における、テンプレート位置、クエリパラメータ、テンプレートプレビューフィールド。]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Eメールキャンペーンでリンクテンプレートを使用する

リンクテンプレートの設定が完了したら、メールで使用するテンプレートを選択することができる。

- **HTMLエディター：**[**コンテンツ**] セクションの [**リンク管理**] タブに移動します。**リンクテンプレートを追加**を選択し、リンクテンプレートを選択し、**追加**を選択します。

{% alert important %}
更新されたHTMLメールエディターで**リンク管理**タブにアクセスするには、リンクエイリアスをオンにしておく必要がある。リンクエイリアスを有効にするには、アカウントマネージャーに連絡する。
{% endalert %}

- **ドラッグ＆ドロップ・エディター：****コンテンツ**＞**リンク管理**タブを選択する。次に、**Add a Link Template**を選択します。ドラッグ＆ドロップ・エディターでリンクテンプレートにアクセスするには、[リンクのエイリアシングを]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/)オンにしておく必要がある。

![ドラッグ・アンド・ドロップ・エディターの「リンク管理」タブには、リンク・テンプレートの例がリストアップされている。][1]

{% alert note %}
リンクテンプレートはプレーンテキストには適用されません。つまり、「現在」には、リンクテンプレートのパラメータを含まないクリックが表示される場合があります。これは、これらのクリックは、電子メールのプレーンテキストバージョンから取得される可能性があるためです。
{% endalert %}

**リンク管理]**タブでリンクテンプレートを追加すると、右にスクロールして追加したテンプレートを見ることができる。

## リンクテンプレートを管理する

リンクテンプレートを[複製する]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/)こともできる。テンプレートとクリエイティブ・コンテンツの作成と管理については、「[テンプレートとメディア]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)」をご覧ください。

{% alert important %}
テンプレートのアーカイブは、現在リンクテンプレートでは利用できません。
{% endalert %}

## よくある質問

リンクテンプレートに関するよくある質問については、[テンプレート FAQ][10] ] ページをチェックしよう。

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
