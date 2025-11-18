---
nav_title: Brazeパイロット
page_order: 10.5
layout: dev_guide
guide_top_header: "Brazeパイロット"
guide_top_text: "Braze Pilotは、Brazeダッシュボードとシームレスに接続できるように設計されたモバイルアプリである。これにより、アプリにキャンペーンやキャンバスを立ち上げることができるようになり、Brazeのメッセージに自分の携帯電話で命を吹き込むことができる。Braze Pilotには、さまざまな業界を代表する架空のブランドのアプリシミュレーションライブラリーがあり、カスタマーエクスペリエンスから見たメッセージングを体験することができる。"
description: "Brazeのダッシュボードから携帯電話にメッセージを送るための、Brazeのさまざまな使い方をチェックしよう。"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: Braze Pilotを使い始める
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: データ辞書
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: ディープリンク
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## アプリの試験的シミュレーション

Braze Pilotの核となるのは、アプリシミュレーションのライブラリーだ。各アプリは、業界に特化した架空のブランドのリアルなシミュレーションであり、豊富なイベントやアトリビューションのログを記録するようインストルメント化されているため、一般的なBrazeのユースケースをパワーアップする機会が無限に生まれる。

{% tabs local %}
{% tab Fitness %}

### ステッピントン

Steppingtonは、ワークアウト、エクササイズゴール、Steppington+プレミアムサービスを備えたフィットネスアプリだ。[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)、[フィーチャーフラグで]({{site.baseurl}}/developer_guide/feature_flags)明らかにできるセクション、カスタムイベントログの強力なライブラリーなど、この業界向けのカスタマージャーニーを数多く示すことができる。

![マラソントレーニング、ヨガ、サイクリング、ウェイトトレーニングのアイコンがある。]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinthはパンツを販売するeコマースアプリだ！PantsLabyrinthアプリには、完全なショッピングカートのチェックアウト体験、フィーチャーフラグでイネーブルメントにできるオプションのウィッシュリスト機能、英国の友人と下品なジョークを言い合う多くの機会が含まれている。

![PantsLabyrinthの商品ページで、ジーンズをカートに入れることができる。]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### ムービーキャノン 

MovieCanonは、コンテンツ・エンゲージメントに関するBrazeの一般的なユースケースを説明するために完璧に設計されたストリーミング・サービスである。 

![MovieCanonアプリで、様々なスリラー映画を観ることができる。]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## PilotとBrazeダッシュボードとの接続方法

Braze SDKは、アプリやWebサイトに統合されるとユーザーからデータを収集するコードパッケージである。Pilotをダッシュボードに接続するときは、携帯電話のPilotアプリとBraze SDK間のこの接続を初期化し、ダッシュボードのAPIキー識別子をPilotに与えてBrazeインスタンスとの一意の接続を確立する。

![パイロットを設定する最初のステップだ。]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

PilotがあなたのBrazeダッシュボードに接続した後、Braze SDKは、あなたがSDKをあなた自身のアプリやWebサイトと統合したときと同じようにアプリで機能する。つまり、Brazeはそうなるということだ：

- アプリ内の架空のブランドに特化したカスタムデータを含む、ユーザーアクティビティのデータをPilotに保存する。
- セッションデータ、デバイス情報、プッシュトークンを自動的に収集する。
- SDKとの統合が必要なプッシュ通知、アプリ内メッセージ、コンテンツカードのメッセージングチャネルを機能させる。

Braze SDKについては、[Integrationを]({{site.baseurl}}/user_guide/getting_started/integration)参照のこと。

![Brazeカスタマーエンゲージメントスタックには、データ取り込み、分類、オーケストレーション、パーソナライゼーション、および顧客とのインタラクティブなフィードバックループのためのメッセージングチャネルとのアクションのための統合、API、SDKが含まれる。]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Brazeのユーザープロファイル

Brazeに送信されたすべてのデータは、アプリやWebサイトの特定のユーザー専用のユーザープロファイルに保存される。Pilotをダッシュボードに接続すると、BrazeはPilotのユーザーとしてのあなたのデータを記録し始める。この接続によって作成されるユーザーには、匿名と識別子の2種類がある。

### 匿名 

この接続ステータスは、まだログインしていないアプリやWebサイトのゲストの体験を表している。お客様が匿名ユーザーとしてPilotを初期化した場合、Brazeはお客様用の[匿名ユーザープロファイルを]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users)作成し、そこでのお客様の活動に関するデータを記録する。匿名ユーザーをキャンペーンのターゲットにすることはできるが、ダッシュボードで直接ユーザープロファイルを調べることはできない。

### 識別子

この接続ステータスは、外部識別子と呼ばれるユーザーに割り当てられた一意の識別子を通じて、Brazeがユーザープロファイルを認識することを意味する。ダッシュボードの**ユーザー検索**ページでこの外部識別子を検索して、ユーザープロファイルを見つけることができる。このプロファイルには、アプリでのアクティビティに基づいて Pilot から記録されたすべてのユーザー属性とイベントが保存される。

![ユーザー "torchie-208117 "のBrazeユーザープロファイルの例。]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### 接続タイプ

接続の種類を確認するには、画面右上の接続ステータスをチェックすればいい。

{% tabs local %}
{% tab Anonymous user  %}

**Anonymousは**、匿名ユーザーとしてデータを記録していることを示す。

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

識別子ユーザーとしてデータを記録している場合、ユーザーアイコンが外部IDの横に表示される。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**未接続は**、Braze SDKとPilotの接続をまだ初期化していないことを示す。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## キャンペーンとキャンバス

キャンペーンとキャンバスは、ユーザーにメッセージを送信する手段です。 

- キャンペーンは、さまざまなチャネルにわたって特定のオーディエンスセグメントに送信される単一のメッセージに最適です。 
- キャンバスは、複数のチャネルにわたってパーソナライズされたカスタマージャーニーを自動化およびオーケストレーションできる高度なキャンペーンワークフローです。キャンバス内で、分岐ロジック、遅延、決定ポイント、コンバージョンイベントを設定して、一連のやり取りを通じて顧客を導くことができます。キャンバスは、さまざまなタッチポイントで一貫性のあるシームレスなコミュニケーションを実現し、カスタマーエンゲージメントとコンバージョンの可能性を高めるのに役立つ。

## 対応メッセージングチャネル

Braze Pilotは現在、[アプリ内メッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about)サポートしており、アプリ内に表示され、ユーザーがアクティブにエンゲージしている間にタイムリーなメッセージを配信する。

![MovieCanonアプリ内メッセージ「MovieCanonを楽しんでいますか？お友達を紹介してください！」と表示され、メールアドレスを入力して紹介状を送ることができる。]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}