---
nav_title: コンテンツカード
article_title: コンテンツカード
page_order: 1
layout: dev_guide
guide_top_header: "コンテンツカード"
guide_top_text: "コンテンツ カードを使用すると、顧客のエクスペリエンスを中断することなく、顧客が選択したアプリ内で、高度にターゲットを絞ったリッチコンテンツの動的なストリームを送信できます。<br><br>コンテンツカードはアプリまたはWeb サイトに直接的に埋め込まれるため、メッセージ受信トレイesや、メールやプッシュ通知sなどの他のチャネルの到達範囲を広げるカスタムインターフェイスを作成できます。さらに、コンテンツカードは、カードの固定、カードの解雇、APIベースの配信、接続コンテンツ、カスタムカードの有効期限、カード 分析、およびプッシュ通知sとの容易な調整など、より多くのパーソナライズされた機能に対応しています。<br><br>** コンテンツカードを利用できるかどうかは、Brazeによって異なります。開始するには、アカウントマネージャーまたは顧客のサクセスマネージャーにお問い合わせください。**"
description: "このランディングページは Braze コンテンツカードのホームです。ここでは、コンテンツカードの作成方法、コンテンツカードのカスタマイズ方法、テスト、レポートなどに関する記事を検索できます。"
channel:
  - content cards
search_rank: 5
guide_featured_title: "セクションの記事"
guide_featured_list:
- name: コンテンツカードを作成する
  link: /docs/user_guide/message_building_by_channel/content_cards/create/
  image: /assets/img/braze_icons/columns-01.svg
- name: カード作成
  link: /docs/user_guide/message_building_by_channel/content_cards/create/card_creation
  image: /assets/img/braze_icons/message-check-circle.svg
- name: クリエイティブの詳細
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/
  image: /assets/img/braze_icons/brush-02.svg
- name: テスト
  link: /docs/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
  image: /assets/img/braze_icons/beaker-02.svg
- name: レポート
  link: /docs/user_guide/message_building_by_channel/content_cards/reporting/
  image: /assets/img/braze_icons/pie-chart-01.svg
- name: ベストプラクティス
  link: /docs/user_guide/message_building_by_channel/content_cards/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"}コンテンツカードの利点

開発者がアプリにコンテンツを組み込むのと比較して、コンテンツカードを使用するメリットをいくつか挙げてみよう：

- **セグメンテーションとパーソナライゼーションの容易化:**ユーザーデータは Braze に保存されているため、対象ユーザーを簡単に定義し、コンテンツカードを使用してメッセージをパーソナライズできます。
- **レポートの一元化:**コンテンツカードの分析は Braze で追跡されるため、すべてのキャンペーンのインサイトを一元管理できます。
- **一貫性のあるカスタマージャーニー:**コンテンツカードを Braze の他のチャネルと組み合わせて、一貫性のあるカスタマーエクスペリエンスを作成できます。一般的なユースケースは、プッシュ通知を送信し、プッシュ通知にエンゲージしなかったユーザー向けにその通知をコンテンツカードとしてアプリに保存することです。コンテンツが開発者によってアプリに直接組み込まれている場合、それはメッセージングの他の部分から切り離されている。
- **オプトインは不要:**アプリ内メッセージと同様に、コンテンツカードには、ユーザーによるオプトインや許可が必要ありません。アプリ内メッセージは許可が不要でも有効期間が短いのに対し、コンテンツカードは許可が不要で永続的です。つまり、アプリ内メッセージとコンテンツカードを組み合わせたメッセージング戦略は、非常にバランスが取れているということです。
- **メッセージングエクスペリエンスを詳細にコントロール:**コンテンツカードの初期設定には開発者の協力が必要だが、その後はBrazeのダッシュボードからメッセージ、受信者、タイミングなどを直接コントロールできる。

### 数字で見るコンテンツカード

マーケターは Braze でコンテンツカードを自分で作成するため、アプリや Web サイトを全面的に作成し直さなくても、メッセージングを更新することで投資対効果を得られます。コンテンツカードの ROI に関して参考になる統計をいくつかご紹介します。

- コンテンツカードは、72時間以内に売上を伸ばすうえでメールよりも **38 倍**効果的です。[^1]
- ロイヤルティ登録キャンペーンでコンテンツカードを使用すると、コンバージョンが **5 倍**増加します。[^1]
- プッシュ通知、アプリ内メッセージ、およびコンテンツカードを介してユーザーにアウトリーチを送信すると、プッシュのみでエンゲージメントされたユーザーと比較して、**6.9X**多くのセッションが発生します。[^2
- メール、アプリ内メッセージ、およびコンテンツカードを介してユーザーにアウトリーチを送信すると、メールのみを介してエンゲージされたユーザーと比較して、平均ユーザー寿命が**3.6X**長くなります。[^2

## 仕組み

Brazeには、コンテンツカードを表示するためのさまざまなコンテンツカードタイプが用意されています。クラシック、キャプションイメージ、またはイメージ。本質的に、コンテンツカードは実際にはデータのペイロードであり、データの外観ではありません。 

少し技術的な部分を説明しましょう。バックグラウンドでは、コンテンツカードの 3 つの主要な部分があります。

- **モデル:**カードに保存されているデータの種類
- **ビュー:**カードの外観
- **コントローラー:**ユーザーがカードを操作する方法

デフォルトの実装では、カードのコンテンツ（モデル）をダッシュボードから、あるいはAPIを通じて追加し、ビューとコントローラはビューコントローラと呼ばれるもので処理する。ビューコントローラーは、アプリケーション全体と画面の間の「接着剤」です。

## ユースケース

コンテンツカードの一般的なユースケースについては、このセクションを参照のこと。

{% alert tip %}
さらにインスピレーションが必要な場合は、[コンテンツカードインスピレーションガイド](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide)の参照を強くお勧めします。このガイドには、紹介プログラム、新製品の発売、サブスクリプションの更新など、20 を超えるカスタマイズ可能なキャンペーンが掲載されています。
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

新規ユーザーがアプリやWebサイトを探索する際、戦略的に配置されたコンテンツカードを使って、提供するものの価値やメリットを説明しよう。ホームページ上でコンテンツカードを使用して他のコミュニケーションチャネルにオプトインするようユーザーに奨励し、未処理のオンボーディングタスクをコンテンツカードを利用した専用のオンボーディングタブに保存します。ユーザーが目的のタスクを完了したら、カードを削除することをお忘れなく！

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event attendance %}

ユーザーのホームページの上部にコンテンツカードを表示し、イベントへの参加を促す。ロケーション・ターゲティングを使い、潜在的なユーザーがいる場所にリーチする。関連する物理的なイベントにユーザーを招待すると、特にブランドでのこれまでの活動を活用したパーソナライズされたメッセージを使用して、ユーザー向けに特別感を演出できます。

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

ユーザーの行動や好みに関するデータを使用して、ホームページまたは受信トレイのコンテンツカードから関連コンテンツをリアルタイムで表示し、それらを製品提供に引き込みます。

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

コンテンツカードを活用して、ホームページまたは専用のプロモーション受信トレイでプロモーションメッセージやまだ反応のないオファーを直接強調表示します。顧客の以前の購入に基づいて関連コンテンツを取得し、注目を集めるパーソナライズされたプロモーションを提供します。

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### その他のユースケース

これらの主な使用例以外にも、顧客は非常にさまざまな方法でコンテンツカードを使用しています。コンテンツカードの強みはその柔軟性です。欲しいユースケースがここに示されていない場合は、[キーと値のペアを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)設定し、ペイロードをアプリやWebサイトに送信することができる。

## アプリのコンテンツカード

ここでは、アプリまたはWeb サイト内にコンテンツカードを配置する最も一般的な方法について説明します。

- [メッセージの受信トレイ](#message-inbox)
- [カルーセル](#carousel)

これらの配置のロジックと実装は Braze のデフォルトではないため、これらのユースケースを実現する作業は、開発チームが実施し、サポートする必要があります。これらの配置の実装方法の概要については、[カスタムコンテンツカードの作成]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)を参照してください。

![メッセージインボックス、カルーセル、およびバナー(banner.]({% image_buster /assets/img_archive/cc_placements.png %})({: style="border:0px;"})という異なる配置オプションを示す3 つのコンテンツカードの例

### メッセージの受信トレイ

!["message inbox" placement.]({% image_buster /assets/img_archive/cc_placement_inbox.png %})({: style="float:right;margin-left:15px;max-width:30%;border:0px;"})を使用したコンテンツカードの例

メッセージ受信ボックス (通知センターまたはフィードとも呼ばれます) は、アプリまたは Web サイト内の永続的な場所であり、コンテンツカードを任意の形式で表示できます。受信トレイ内の各メッセージは、それぞれ独自のコンテンツカードです。 

メッセージ受信トレイは、開発が最小限で済むデフォルトの実装です。iOS、Android、Web のメッセージ受信トレイ用の[ビューコントローラー](#how-it-works)が提供されており、コンテンツカードを利用してこの機能を簡単に作成できます。

#### メリット

- ユーザーは一か所で多数のカードを受け取れる
- 他のチャネル（特にプッシュ通知）で見逃した、あるいは却下された情報を再浮上させる効率的な方法。
- オプトインは不要

#### 動作

ユーザーがカードの受信対象者である場合、カードは自動的に受信トレイに表示されます。コンテンツカードは一括して閲覧できるように作られているため、ユーザーは対象となるすべてのカードを一度に閲覧することができる。

デフォルトの実装では、受信トレイ内のコンテンツカードは、クラシック (タイトル、テキスト、オプションの画像を含む)、画像のみ、またはキャプション付きの画像カードとして表示されます。アプリ内でメッセージ受信トレイを配置する場所を選択します。

コンテンツカードにはデフォルトのスタイルが付属していますが、アプリのルックアンドフィールに応じてカードとフィードを表示するカスタム実装を選択できます。

### カルーセル

!["carousel" placement.]({% image_buster /assets/img_archive/cc_politer_carousel.png %})({: style="float:right;margin-left:15px;max-width:30%;border:0px;"})を使用したコンテンツカードの例

カルーセルは、顧客がスワイプして表示できる 1 つのスペースに複数のコンテンツを表示します。画像、テキスト、動画のスライドショーであったり、それらを組み合わせたものであったりする。これはカスタム実装であり、開発者による多少の作業が必要です。

#### メリット

- ユーザーは一か所で多数のカードを受け取れる
- エンゲージメントを高める方法で推奨事項を表示できる

#### 動作

ユーザーがカードを受け取る資格がある場合、カルーセルが追加されたアプリのどのページのカルーセルにもそのカードが表示されます。ユーザーは水平にスワイプして追加の注目カードを表示できます。

これはカスタム実装であるため、開発者と協力してコンテンツカードを表示する独自のビューを構築する必要があります。デフォルトのクラシック、画像のみ、キャプション付き画像カードは、この実装ではサポートされていない。

## コンテンツカードの統合

開発者は、Braze SDK を統合するときにコンテンツカードを統合します。コンテンツカードと統合する方法の詳細については、お使いのプラットフォームの開発者ガイドの記事を参照してください。

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## 情報源

<span></span>

[^1]:[カスタマーリテンションキャンペーンを最大限に活用するための 8 つのヒント](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]:[レポート:クロスチャネルマーケティングの違い](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
