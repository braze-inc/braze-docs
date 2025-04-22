---
nav_title: メールテンプレートの作成
article_title: メールテンプレートの作成
page_order: 0
description: "この記事では、メールテンプレートの作成、カスタマイズ、および管理の方法について説明します。"
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# メール テンプレートの作成

> Braze ダッシュボードにはメールテンプレートエディターがあり、これにより、カスタムの目を引くメールを作成し、後でキャンペーンで使用するために保存することができます。独自の[HTML メール テンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/)をアップロードすることもできます。

## ステップ 1: メール テンプレートエディタに移動します

[**テンプレート**] > [**メール テンプレート**] に移動します。

## ステップ 2: 編集体験を選択する 

編集するには、**ドラッグアンドドロップエディタ**または**HTMLエディタ**から選択します。 

その後、事前に指定された Braze テンプレートから選択したり、新しいテンプレートを作成したり、既存のテンプレートを編集したりすることができます (プレーンまたは [モバイルレスポンシブ][8])。

![ドラッグアンドドロップエディタまたはHTMLエディタを選択するか、Braze テンプレートs から選択するかを選択できる、企業の春物セールのメール テンプレート。][2]

{% alert note %}
既存のカスタムHTML テンプレートs は、ドラッグアンドドロップエディタを使用して再作成する必要があります。
{% endalert %}

## ステップ 3: テンプレートのカスタマイズ

エディタエクスペリエンスを選択したら、メール テンプレートをカスタマイズしてクリエイティブにすることができます。HTML を使用して、HTML エディタでブランドを作成およびエミュレートしたり、ドラッグアンドドロップエディタにさまざまな[クリエイティブな詳細]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) を含めることができます。

### 配信停止リンクを含める

メール テンプレートをデザインする際に、配信停止リンクを含めない場合、Brazeは、すべてのマーケティング メールで法的に要求されているため、これをメールに追加するように促します。この配信停止リンクは、Liquid タグ {% raw %}``${email_footer}``{% endraw %} を使用するか、テンプレートの[フッターをカスタマイズする]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer)ことで、メールの下部にフッターとして追加できます。

## ステップ 4:メール エラーの確認

メールエラーは、メッセージワークフローの**Compose** タブに表示されます。エラーが発生すると、進むことができません。「警告」は、ベストプラクティスに従うためのリマインダーです。ビジネスによっては、無視することもできます。

![サンプルメールのエラーと警告の一覧。][1]{: style="float:right;max-width:40%;margin-left:15px;"}

エディタで計算されるエラーの一覧を次に示します。

- 不正な液体構文
- [400kb を超えるメール本文。本文は102kb 未満にすることを強く推奨します][7]
- 配信停止リンクのないテンプレート
- 空白の**本文**または**Subject**のメール
- 配信停止リンクのないメール

## ステップ 5: メッセージをプレビューしてテストする

テンプレートの作成が終わったら、テストしてから送信できます。

概要画面の下部から、**Preview and Test**をクリックします。ここで、顧客の受信トレイでメールがどのように表示されるかをプレビューできます。**プレビューをユーザー**として選択すると、ランダムユーザーとしてメールをプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、コネクテッドコンテンツとパーソナライゼーションの呼び出しがコールが正常に機能していることをテストできます。

また、デスクトップビュー、モバイルビュー、およびプレーンテキストビューを切り替えるして、さまざまなコンテキストでメッセージがどのように耳にアプリするかを把握することもできます。

最終確認の準備ができたら、**Test Send**を選択し、自分またはコンテンツテスタのグループにテストメッセージを送信して、メールがさまざまな機器やメール クライアントに正しく表示されることを確認します。

![テスト用に送信されるサンプルメール プレビュー。][6]

テンプレートに問題がある場合、または変更を行いたい場合は、**Email** を編集してエディタに戻ります。

## ステップ 6:テンプレートを保存する

必ず**テンプレート保存**をクリックしてテンプレートを保存してください。これで、選択したキャンペーンまたはキャンバスコンポーネントでこのテンプレートを使用する準備が整いました。テンプレートにアクセスするには、ビルドした編集エクスペリエンスを選択し、使用可能なテンプレートの一覧から選択します。

{% alert note %}
既存のテンプレートを編集した場合、それらの変更はそのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されません。
{% endalert %}

### テンプレートの管理

メール テンプレートs をさらに作成すると、[duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) および[archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates) メール テンプレートs を作成できます。テンプレートおよびクリエイティブコンテンツのライブラリを作成して管理する方法について詳しくは、「[テンプレートとメディア]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)」を参照してください。

### API キャンペーンでのテンプレートの使用

API キャンペーンでメールを使用するには、`email_template_id` が必要です。これは、Braze で作成されたメール テンプレートの下部にあります。

![メール テンプレートの下部にあるAPI 識別子。][5]

### メール テンプレートのコメント

ドラッグ＆ドロップエディターで、メールテンプレートのコラボレーションやコメントを行うことができます。 

1. 注釈を付けたいメール本文のコンテンツブロックまたは行を選択します。
2. <i class="fas fa-comment"></i>コメントアイコンを選択します。
3. サイドバーにコメントを入力し、**Submit**をクリックします。
4. コメントを入力したら、**Done**をクリックします。
5. **Save Template**をクリックしてコメントを保存します。

テンプレートが保存されると、ユーザーに未解決のコメントのアイコンが表示されます。これらのコメントを解決するには、**Resolve**を選択します。

![「Looks good to me」と書かれたメールテンプレートコメント。][10]

メール テンプレート s に関するよくある質問への回答については、[テンプレート s FAQ][9] をご覧ください。

[1]: {% image_buster /assets/img/dnd_compose_error.png %}
[2]: {% image_buster /assets/img/email_templates/template2.png %}
[3]: {% image_buster /assets/img/email_templates/template3.png %}
[4]: {% image_buster /assets/img/email_templates/template4.png %}
[5]: {% image_buster /assets/img/email_templates/template5.png %}
[6]: {% image_buster /assets/img_archive/newEmailTest.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[10]: {% image_buster /assets/img/email_templates/template_comment.png %}
