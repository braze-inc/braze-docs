---
nav_title: Brazeパイロット
page_order: 10.5
layout: dev_guide
guide_top_header: "Brazeパイロット"
guide_top_text: "Braze Pilotは、Brazeのダッシュボードとシームレスに連携するように設計されたモバイルアプリだ。これにより、アプリにキャンペーンやキャンバスを配信できるようになる。つまり、自分のスマホ上でBrazeのメッセージを実際に体験できるのだ。Braze Pilotには、様々な業界を代表する架空のブランド向けアプリシミュレーションのライブラリーが含まれている。これにより、顧客の視点から見た自社のメッセージングがどのように見えるかを体験できる。"
description: "Brazeのダッシュボードから自分の携帯電話にメッセージを送信する方法をいくつか確認してみろ。"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: Braze Pilotの始め方
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: データディクショナリ
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: ディープリンク
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## パイロットアプリのシミュレーション

Braze Pilotの中核は、アプリシミュレーションのライブラリーである。各アプリは業界特化型の架空ブランドをリアルにシミュレートしたもので、豊富なイベントや属性を記録する仕組みを備えている。これにより、Brazeの一般的なユースケースを実現する無限の可能性が生まれる。

{% tabs local %}
{% tab Fitness %}

### ステッピントン

ステッピントンは、ワークアウトや運動目標、そしてステッピントンプラスというプレミアムサービスを備えたフィットネスアプリだ。[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)を表示する複数の場所を提供し、[フィーチャーフラグ]({{site.baseurl}}/developer_guide/feature_flags)で表示可能なセクションを備え、さらに豊富なカスタムイベントロギングライブラリーにより、この業界における多様なカスタマージャーニーを可視化できる。

![ステッピントンのホームページには、マラソンのトレーニング、ヨガ、サイクリング、ウェイトトレーニングのアイコンがある。]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

パンツラビリンスは、パンツを売るe コマースアプリだ！パンツラビリンスアプリには、ショッピングカートの決済機能、フィーチャーフラグでイネーブルメントできるオプションのウィッシュリスト機能、そして英国の友達と小賢しい冗談を交わす機会が数多く含まれている。

![パンツラビリンスの商品ページで、ジーンズをカートに入れるオプションがある。]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### 映画カノン 

MovieCanonは、コンテンツエンゲージメントに関するBrazeの一般的なユースケースを完璧に説明するために設計されたストリーミングサービスだ。 

![様々なスリラー映画が観られるMovieCanonアプリだ。]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## PilotがBrazeダッシュボードと連携する方法

Braze SDKは、アプリやWeb サイトに統合されると、ユーザーからデータを収集するコードパッケージだ。Pilotをダッシュボードに接続する際、スマートフォン上のPilotアプリとBraze SDK間の接続を初期化する。さらに、ダッシュボードのAPI キー識別子をPilotに提供することで、Brazeインスタンスとの固有の接続を確立する。

![パイロットの設定の最初のステップだ。]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

PilotがBrazeダッシュボードに接続した後、アプリ内のBraze SDKは、自社のアプリやWeb サイトにSDKを統合した場合と同様に機能する。これは、Brazeが以下のことを意味する。

- Pilotにユーザー活動データを保存する。これにはアプリ内の架空ブランド固有のカスタムデータも含まれる。
- セッションデータ、デバイス情報、プッシュトークンを自動的に収集する。
- SDKの統合が必要となる機能である、プッシュ通知、アプリ内メッセージ、コンテンツカードメッセージングチャネル。

Braze SDKの詳細については、[統合]({{site.baseurl}}/user_guide/getting_started/integration)を参照せよ。

![Brazeのカスタマーエンゲージメントスタックは、データ取り込み、分類、オーケストレーション、パーソナライゼーション、アクションのための統合、API、SDKを含み、顧客との双方向フィードバックループを実現するメッセージングチャネルを備えている。]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Brazeのユーザープロファイル

アプリやWeb サイトにおける特定のユーザーに紐づくユーザープロファイルに、Brazeに送信されるデータは全て保存される。パイロットをBrazeのダッシュボードに接続すると、Brazeはパイロットのユーザーであるあなたに関するデータの記録を開始する。この接続を通じて作成されるユーザーには、匿名ユーザーと識別子を持つユーザーという二種類がある。

### 匿名 

この接続ステータスは、まだログインしていないアプリやWeb サイトのゲストの体験を表している。パイロットを匿名ユーザーとして初期化すると、Brazeは自動的に[匿名ユーザープロファイル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users)を作成し、そのプロファイルにユーザーの活動データを記録する。匿名ユーザーはキャンペーンの対象とすることはできるが、Brazeダッシュボードで直接そのユーザープロファイルを閲覧することはできない。

### 識別された

この接続ステータスは、Brazeがあなたに割り当てられた一意の識別子（外部識別子と呼ばれる）を通じて、あなたのユーザープロファイルを認識していることを意味する。ダッシュボードの**ユーザー検索**ページでこの外部識別子を検索すれば、ユーザープロファイルを見つけられる。そこにはアプリ内での活動に基づき、Pilotから記録された全てのユーザー属性とイベントが保存される。

![ユーザー「torchie-208117」のBrazeユーザープロファイルの例だ。]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### 接続タイプ

接続の種類を確認するには、画面の右上に表示されている接続ステータスを確認すればよい。

{% tabs local %}
{% tab Anonymous user  %}

**匿名とは、**匿名ユーザーとしてデータを記録していることを示す。

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

識別されたユーザーとしてデータを記録している場合、external IDの横にユーザーアイコンが表示される。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**接続されていないとは、**まだBraze SDKとPilotの接続を初期化していないことを示す。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## キャンペーンとキャンバス

キャンペーンとキャンバスは、ユーザーにメッセージを送信する手段です。 

- キャンペーンは、さまざまなチャネルにわたって特定のオーディエンスセグメントに送信される単一のメッセージに最適です。 
- キャンバスは、複数のチャネルにわたってパーソナライズされたカスタマージャーニーを自動化およびオーケストレーションできる高度なキャンペーンワークフローです。キャンバス内で、分岐ロジック、遅延、決定ポイント、コンバージョンイベントを設定して、一連のやり取りを通じて顧客を導くことができます。キャンバスは、異なる接点間で一貫性のあるシームレスなコミュニケーションを確保するのに役立つ。これによりカスタマーエンゲージメントとコンバージョンの可能性が高まる。

## サポートされているメッセージングチャネル

Braze Pilotは現在、[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about)をサポートしている。これはアプリ内に表示され、ユーザーが積極的にエンゲージメントを行っている最中にタイムリーなメッセージを届ける。

![MovieCanonアプリ内のメッセージ「MovieCanonを楽しんでいますか？」友達を紹介しよう！」と表示され、紹介メールを送るためのメールアドレスの入力欄がある。]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}