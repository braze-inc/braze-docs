---
nav_title: はじめに
article_title: Braze Pilotを使い始める
page_order: 2
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# Braze Pilotを使い始める

> この記事では、Braze Pilotの使い始め方について説明する。ここでは、アプリのダウンロード、Brazeダッシュボードとの接続の初期化、セットアップの完了までを説明する。

## ステップ 1: Braze Pilot のダウンロード

Braze Pilotを使い始めるには、まずApple App StoreかGoogle Play Storeアプリからアプリをダウンロードする必要がある。アプリストアでアプリを検索するか、以下のQRコードをスキャンして、お使いのデバイスのアプリページにアクセスすることができる。

## ステップ 2: 利用規約に同意する

次に、利用規約に同意し、あなたの仕事のメールをフォームに入力する。あなたのメールはアプリの利用分析のみに使用され、マーケティング目的には使用されない。

![Braze Pilotのウェルカムページ。]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} 仕事用のメールアドレスを入力する。]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## ステップ 3: Braze SDKとの接続を初期化する。

Braze Pilotを使用すると、任意のBrazeダッシュボードに対してBraze SDKを初期化することができる。SDKが初期化されると、PilotはエンゲージメントデータのBrazeへの送信を開始し、そのBrazeダッシュボードから起動したメッセージングをトリガーできるようになる。

PilotでSDK接続を設定するには、2つの方法がある：デモQRコードとセットアップウィザード。

{% tabs local %}
{% tab Demo QR codes %}

### 方法1:デモQRコード

SDKの初期化、ユーザープロファイルの作成、Braze Pilotの特定のアプリシミュレーションへのディープリンクに必要なすべての詳細を含むQRコードをスキャンする。デモQRコードは、無料体験の特定のデモキャンペーンのコンパニオンドローワーに表示される。

| Android用パイロット | iOS用パイロット |
| --- | --- |
| ![Android用QRコード。]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![iOS用QRコード。]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### 方法2:セットアップウィザード

Brazeダッシュボードの**アプリ設定**ページから、ダッシュボードワークスペースとの接続を初期化するためのステップバイステップガイドに従う。

![Braze Pilotのセットアップウィザードのステップ1。]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

この接続はワークスペースに依存する。つまり、デモ・ワークスペースから接続を初期化し、無料トライアル・ダッシュボードのライブ・ワークスペースに切り替えると、そこで開始されたキャンペーンを受信するには、そのワークスペースからSDKを再初期化する必要がある。

![Brazeダッシュボードのワークスペース・ドロップダウンで、アクティブなワークスペースとして "Demo - Braze "が選択されている。]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## ステップ 4: プッシュ権限を許可する

最後に、アプリを通じてプッシュ機能をテストしたい場合は、アプリがプッシュ権限を送信することを許可することをお勧めする。以下の方法でアプリに権限を与えることができる：デバイスの設定でアプリの設定を更新する、またはBrazeからアプリにプッシュプライマーメッセージを起動する。

{% tabs local %}
{% tab Update the settings for the app %}

デバイス設定を開封し、Braze Pilotを探す。そして、ロック画面に通知を表示できるように設定を更新する。

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Brazeのアプリ内メッセージを使って、自社の消費者と同じようにアプリのプッシュ権限をリクエストできる。Brazeでこのタイプのメッセージを作成する方法については、[Push primerアプリ内メッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages)参照。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## ステップ 5: PilotでBrazeのメッセージングを体験する

これで、Braze Pilotのユーザーとして、Brazeダッシュボードからキャンペーンやキャンバスの受信を開始する準備が整った！デモ・ワークスペースで開始されたキャンペーンにアクセスして、Brazeユースケースの簡単なデモをご覧いただき、その後、ライブ・ワークスペースに移動して、ご自身のキャンペーンを開始してください。

BrazeでのキャンペーンとCanvasesの設定方法については、[Getting Startedを参照のこと：キャンペーンとキャンバス]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases)。