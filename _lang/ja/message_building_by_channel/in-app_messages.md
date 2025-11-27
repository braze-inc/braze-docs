---
nav_title: "アプリ内メッセージ"
article_title: アプリ内メッセージ
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "アプリ内メッセージ"
guide_top_text: "アプリ内メッセージは、プッシュ通知でユーザーの一日を邪魔することなく、コンテンツを届けるのに役立つ。これらのメッセージは、ユーザーのアプリの外に配信されることはなく、ユーザーのホーム画面を邪魔することもないからだ。<br><br>カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスを向上させ、オーディエンスがアプリから最大限の価値を得るのに役立ちます。様々なレイアウトやカスタマイズツールから選べるので、アプリ内メッセージはこれまで以上にユーザーを惹きつけます。これらは、コンテキストがあり、緊急性が低く、ユーザーがアプリ内でアクティブなときに配信される。アプリ内メッセージの例については、<a href='https://www.braze.com/customers'>顧客ストーリーを</a>ご覧いただきたい。"
description: "このランディングページには、アプリ内メッセージに関するすべての情報がまとめられています。 ここには、アプリ内メッセージの作成方法、ドラッグ＆ドロップエディター、メッセージのカスタマイズ方法、レポートなどに関する記事があります。"
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "よく読まれている記事"
guide_featured_list:
- name: "ドラッグアンドドロップエディタ"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "従来のエディタ"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "クリエイティブディテール"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "テスト"
  link: /docs/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "レポート"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "ダークモード"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "App Store評価プロンプト"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "シンプルな調査"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "メッセージのロケール"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "ベストプラクティス"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "FAQ"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} 想定されるユースケース

アプリ内メッセージは豊富なコンテンツを提供するので、このチャネルをさまざまなユースケースに活用できます。

| ユースケース | 説明 |
| --- | --- |
| プッシュプライミング | リッチなアプリ内メッセージを使用して[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)キャンペーンを実行して、自社のアプリまたはサイトのプッシュ通知にオプトインするメリットを顧客に提示し、プッシュアクセス許可を付与するためのプロンプトを表示します。
| 販売・プロモーション | モーダルのアプリ内メッセージを使用して、静的なプロモーションコードまたはオファーを含み、視覚的に魅力的なメディアで顧客を出迎えます。そのとき以外では得られないインセンティブを提供して、購入やコンバージョンを行うように促します。 |
| 機能導入の促進 | アプリの他の部分を使用したり、サービスを活用したりするように顧客に促します。 |
| 高パーソナライズされた キャンペーンs | 顧客がアプリまたはサイトに入るときに最初に表示されるものとして、アプリ内メッセージs を配置します。Braze の一部のパーソナライゼーション機能 ([コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)など) を追加して、ユーザーのアクションを起こしたいという意欲を促進し、自社のアウトリーチをより効果的なものにします。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

考慮すべき他のユースケースには、次のものがあります。

- 新しいアプリ機能
- アプリ管理
- レビュー
- アプリアップグレードsまたは更新s
- ギベアウェイや懸賞

## 標準メッセージタイプ

以下のタブは、ユーザーが、スライドアップ、モーダル、フルスクリーンアプリ内メッセージなど、当社の一般的なアプリ内メッセージタイプの1 つを開封する際の様子を示しています。

{% tabs %}
{% tab Slideup %}

スライドアップメッセージは通常、アプリ画面の上下に表示されます (メッセージの作成時に設定可能)。これらは、新しい利用規約、Cookie、および他の情報断片についてユーザーに警告するのに適しています。

![アプリ画面下部から表示されるアプリ内メッセージのスライドアップ。このスライドアップには、アイコン画像と短いメッセージが含まれています。(]({% image_buster /assets/img/slideup-behavior.gif %})){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

モーダルは、デバイスの画面の中央に表示され、アプリのバックグラウンドから目立つように画面オーバーレイが表示されます。モーダルは、ユーザーにセールや特別オファーを活用するように大々的にお勧めする場合に、非常に優れています。

![アプリやウェブサイトの中央にダイアログとして表示される、モーダルなアプリ内メッセージ。モーダルには、画像、ヘッダー、メッセージ本文、2つのボタンが含まれる。(]({% image_buster /assets/img/modal-behavior.gif %})){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

フルスクリーン・メッセージは、デバイスの画面全体を取り上げるという、まさに期待通りのものです。このメッセージタイプは、必須アプリ 更新s のように、ユーザーのアテンションが本当に必要な場合に適しています。

![アプリ内メッセージがフルスクリーンでアプリの画面を占領する。フルスクリーンのメッセージには、大きな画像、ヘッダー、メッセージ本文、2つのボタンが含まれる。(]({% image_buster /assets/img/full-screen-behavior.gif %})){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

これらのデフォルトメッセージテンプレートに加えて、カスタムHTMLアプリ内メッセージ、CSSによるWebモーダル、またはWebメールキャプチャフォームを使用してメッセージングをさらにカスタマイズすることもできる。詳細については、[カスタマイズ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/)を参照してください。

## その他のリソース

独自のアプリ内メッセージキャンペーンを作成したり、アプリ内メッセージをマルチチャネルキャンペーンで使用したりする前に、「[アプリ内メッセージ準備ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/)」を確認することを強くお勧めします。このガイドでは、アプリ内メッセージを作成するときに考慮すべきターゲット設定、コンテンツ、およびコンバージョンに関する疑問について説明しています。
