---
nav_title: "アプリ内メッセージについて"
article_title: アプリ内メッセージについて
page_order: 0
page_type: reference
description: "このリファレンス記事では、アプリ内メッセージ、潜在的なユースケース、標準メッセージタイプの概要を説明します。"
channel:
  - in-app messages
search_rank: 4.9
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"}アプリ内メッセージについて

> アプリ内メッセージは多くのことに適しています。コンテンツが豊富で、これらのメッセージはユーザーのアプリの外部に配信されず、ホーム画面に侵入しないため、切迫感は低くなります。アプリ内メッセージはアプリ内に存在し(名前の由来)、コンテキストが付属しており、歓迎されないことはほとんどありません。これらは、ユーザーがアプリ内でアクティブになったときに常に配信されます。

アプリ内メッセージの例については、 [ケーススタディ][1]をご覧ください。

## 想定されるユースケース

アプリ内メッセージが提供する豊富なコンテンツにより、このチャネルをさまざまなユースケースに活用できます。

|ユースケース |解説 |
| --- | --- |
|プッシュプライミング |リッチなアプリ内メッセージを使用して [プッシュプライミング][2] キャンペーンを実施し、アプリやサイトのプッシュをオプトインするメリットを顧客に示し、プッシュ権限を付与するプロンプトを表示します。
|販売とプロモーション |モーダルアプリ内メッセージを使用して、静的なプロモーションコードやオファーを含む視覚的に魅力的なメディアで顧客に挨拶します。他の方法では得られない購入やコンバージョンを行うようにインセンティブを与えます。|
|機能の導入を促進する |アプリの他の部分を使用したり、サービスを利用したりするようにユーザーに促します。|
|高度にパーソナライズされたキャンペーン |アプリ内メッセージは、ユーザーがアプリやサイトにアクセスしたときに最初に目にするものとして配置します。[コネクテッドコンテンツ][3]などのBrazeのパーソナライゼーション機能を追加することで、ユーザーに行動を促し、アウトリーチをより効果的にすることができます。
{: .reset-td-br-1 .reset-td-br-2}

考慮すべきその他のユースケースには、次のようなものがあります。

- アプリの新機能
- アプリ管理
- レビュー
- アプリのアップグレードまたは更新
- 景品と懸賞

## 標準メッセージ・タイプ

次のタブは、ユーザーが標準のアプリ内メッセージタイプ(スライドアップ、モーダル、フルスクリーンのアプリ内メッセージ)を開くとどのように表示されるかを示しています。

{% tabs %}
{% tab Slideup %}

スライドアップ メッセージは通常、アプリ画面の上部と下部に表示されます (これはメッセージの作成時に設定できます)。これらは、新しい利用規約、Cookie、その他の情報スニペットについてユーザーに警告するのに最適です。

![Slideup in-app message appearing from the bottom of the app screen. The slide-up includes an icon image and a brief message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

モーダルはデバイスの画面の中央に表示され、画面オーバーレイが表示されるため、バックグラウンドでアプリから目立つようになります。これらは、ユーザーにセールや景品を利用することをさりげなく提案するのに最適です。

![Modal in-app message appearing in the center of an app and website as a dialog. The modal includes an image, header, message body, and two buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

全画面表示メッセージは、まさに期待どおりのもので、デバイスの画面全体を占めます。このメッセージタイプは、必須のアプリの更新など、ユーザーの注意を本当に必要とする場合に最適です。

![Fullscreen in-app message taking over an app screen. The fullscreen message includes a large image, header, message body, and two buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

これらの標準搭載のメッセージテンプレートに加えて、カスタムHTMLアプリ内メッセージ、CSSを使用したWebモーダル、またはWebメールキャプチャフォームを使用して、メッセージングをさらにカスタマイズすることもできます。詳細については、 [カスタマイズ][4]を参照してください。

## その他の資料

独自のアプリ内メッセージキャンペーンの作成や、マルチチャネルキャンペーンでのアプリ内メッセージの使用を開始する前に、 [アプリ内メッセージの準備ガイド][5]を確認することを強くお勧めします。このガイドでは、アプリ内メッセージを作成する際に考慮すべきターゲティング、コンテンツ、コンバージョンに関する質問について説明します。


[1]: https://www.braze.com/customers
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/
[6]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/
