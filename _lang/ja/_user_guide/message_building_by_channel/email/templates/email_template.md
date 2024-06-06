---
nav_title: メールテンプレートの作成
article_title: メールテンプレートの作成
page_order: 0
description: "この参考記事では、メールテンプレートを作成、カスタマイズ、および管理する方法について説明します。"
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# メールテンプレートの作成

> Brazeダッシュボードにはメールテンプレートエディターがあり、カスタムメイドの人目を引くメールを作成し、後でキャンペーンで使用できるように保存できます。[独自の HTML メールテンプレートをアップロードすることもできます]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/)。

## ステップ 1:メールテンプレートエディターに移動

[**テンプレート**] > [**メールテンプレート**] に移動します。

{% alert note %}
[古いナビゲーションを使用している場合]({{site.baseurl}}/navigation)、このページは [**エンゲージメント**] > [**テンプレートとメディア**] > [**メールテンプレート**] にあります。
{% endalert %}

## ステップ 2:編集体験を選択 

編集内容に合わせて、**ドラッグアンドドロップエディタまたは** **HTML エディタのどちらかを選択します**。 

次に、あらかじめデザインされたBrazeテンプレートから選択したり、新しいテンプレートを作成したり、既存のテンプレートを編集したりできます（プレーンまたは [モバイルレスポンシブ] [8]）。

![][2]

{% alert note %}
既存のカスタム HTML テンプレートは、ドラッグアンドドロップエディタを使用して再作成する必要があります。
{% endalert %}

## ステップ 3:テンプレートをカスタマイズ

編集経験を積んだら、メールテンプレートをクリエイティブにカスタマイズするチャンスです。HTML を使用して HTML エディターでブランドを作成し、エミュレートしたり、[ドラッグアンドドロップエディターにさまざまなクリエイティブな詳細を追加したりできます]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details)。

### 購読解除リンクを含む

メールテンプレートのデザイン時に、登録解除リンクを含めない場合は、すべてのマーケティングメールに法律で義務付けられているため、Brazeはメールにこのリンクを追加するように促します。Liquidタグを使用するか、[テンプレートのフッターをカスタマイズすることで{% raw %}``${email_footer}``{% endraw %}、この購読解除リンクをメールの下部のフッターとして追加できます]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer)。

## ステップ 4: メールエラーをチェック

メールエラーは、メッセージワークフローの「**作成**」タブに表示されます。エラーがあると、先に進むことができません。「警告」は、ベストプラクティスに従うのに役立つリマインダーです。ビジネスによっては、それらを無視することもできます。

![サンプルメールのエラーと警告のリスト。] [1]{: style="float:right;max-width:40%;margin-left:15px;"}

エディターで発生しているエラーのリストは次のとおりです。

- リキッドの構文が正しくありません
- [メール本文は400kb以上、本文は102kb未満にすることを強く推奨します] [7]
- 購読解除リンクのないテンプレート
- ****本文または件名が空白のメール****
- 登録解除リンクのないメール

## ステップ 5: メッセージをプレビューしてテストする

テンプレートの作成が完了したら、送信する前にテストできます。

概要画面の下部から、「**プレビューとテスト**」をクリックします。ここでは、メールが顧客の受信トレイにどのように表示されるかをプレビューできます。「**ユーザーとしてプレビュー**」を選択すると、電子メールをランダムなユーザーとしてプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、コネクテッドコンテンツとパーソナライゼーションコールが正常に機能していることをテストできます。

デスクトップ、モバイル、プレーンテキストの表示を切り替えて、さまざまなコンテキストでメッセージがどのように表示されるかを把握することもできます。

最終チェックの準備が整ったら、「**テスト送信**」を選択し、自分またはコンテンツテスターのグループにテストメッセージを送信して、メールがさまざまなデバイスやメールクライアントで正しく表示されることを確認します。

![テスト用に送信する電子メールプレビューの例] [6]

テンプレートに問題がある場合や変更を加えたい場合は、[**メールを編集**] をクリックしてエディターに戻ります。

## ステップ 6:テンプレートを保存する

必ず [テンプレートを保存] **をクリックしてテンプレートを保存してください**。これで、選択したキャンペーンまたはキャンバスコンポーネントでこのテンプレートを使用する準備が整いました。テンプレートにアクセスするには、作成した編集環境を選択し、使用可能なテンプレートのリストから選択します。

{% alert note %}
既存のテンプレートを編集しても、その変更はそのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されません。
{% endalert %}

### テンプレートを管理する

メールテンプレートをさらに作成するにつれて、[[メールテンプレートを複製してアーカイブできます]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates)]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates)。テンプレートとクリエイティブコンテンツのライブラリの作成と管理について詳しくは、「[テンプレートとメディア]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)」をご覧ください。

### API キャンペーンでのテンプレートの使用

メールを API キャンペーンに使用するには、Braze で作成したメールテンプレートの下部にあるが必要です。`email_template_id`

![メールテンプレートの下部にある API 識別子] [5]

### メールテンプレートへのコメント

ドラッグアンドドロップエディターでメールテンプレートを共同編集したり、コメントしたりできます。 

1. コメントしたいメール本文のコンテンツブロックまたは行をクリックします。
2. <i class="fas fa-comment"></i>コメントアイコンを選択します。
3. サイドバーにコメントを入力し、[**送信**] をクリックします。
4. コメントを入力したら、[**完了**] をクリックします。
5. [**テンプレートを保存**] をクリックしてコメントを保存します。

テンプレートを保存すると、宛先のないコメントの上にアイコンが表示されます。**これらのコメントを解決するには**、「解決」を選択します。

![「私には似合う」と書かれたメールテンプレートのコメント。] [10]

メールテンプレートに関するよくある質問への回答については、[テンプレートFAQ] [9] をご覧ください。

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
