---
nav_title: はじめに
article_title: Braze Pilotを始める
page_order: 2
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# Braze Pilotを始める

> この記事では、Braze Pilotの使用を開始する方法について説明する。ここでは、アプリのダウンロード方法、Brazeダッシュボードとの接続初期化、そして設定完了までの手順を説明する。

## ステップ 1: Braze Pilot のダウンロード

Braze Pilotを使い始めるには、まずApple App StoreかGoogle Play Storeからアプリをダウンロードする必要がある。アプリストアでアプリを検索するか、以下のQRコードをスキャンして、お使いの端末用のアプリページにアクセスできる。

## ステップ 2:利用規約に同意する

次に、利用規約に同意し、フォームに職場のメールを入力する。あなたのメールはアプリの利用状況分析にのみ使用され、マーケティング目的には一切使用されない。

![Braze Pilotのウェルカムページ。]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"}![仕事用のメールを入力するオプション。]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## ステップ 3:Braze SDKとの接続を初期化する

Braze Pilotは、任意のBrazeダッシュボードに対してBraze SDKを初期化することをイネーブルメントする。SDKが初期化されると、PilotはエンゲージメントデータをBrazeに送信し始め、そのBrazeダッシュボードから起動されるあらゆるメッセージングをトリガーできるようになる。

PilotでSDK接続を設定するには、以下の2つの方法がある：デモ用QRコードとセットアップウィザード。

{% tabs local %}
{% tab Demo QR codes %}

### 方法1:デモQRコード

SDKを初期化するために必要な全詳細情報を含むQRコードをスキャンする。ユーザープロファイルを作成し、Braze Pilot内の特定のアプリシミュレーションへディープリンクする。無料トライアル期間中、特定のデモキャンペーンでは、デモ用QRコードがコンパニオンドロワーに表示される。

| Android用パイロット | パイロット for iOS |
| --- | --- |
| ![Android用QRコード。]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![iOS用のQRコード。]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### 方法2:セットアップウィザード

Brazeダッシュボードの**アプリ設定**ページから、ダッシュボードワークスペースとの接続を初期化するステップを順を追って実行する。

![Braze Pilot セットアップウィザードのステップ1。]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

この接続はワークスペース固有である。つまり、デモワークスペースから接続を初期化した後、無料トライアルダッシュボードでライブワークスペースに切り替えた場合、そのワークスペースで開始されたキャンペーンを受信するには、そのワークスペースからSDKを再初期化する必要がある。

![Brazeダッシュボードのワークスペースドロップダウンで、「Demo - Braze」がアクティブなワークスペースとして選択されている状態だ。]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## ステップ 4: プッシュ権限を許可する

最後に、アプリを通じてプッシュ通知機能をテストしたい場合は、アプリにプッシュ通知の送信権限を許可することを推奨する。アプリにこれらの権限を与える方法は以下の通りだ：端末の設定でアプリの設定を更新するか、Brazeからアプリにプッシュ通知メッセージを送信する。

{% tabs local %}
{% tab Update the settings for the app %}

デバイスの設定を開封し、Braze Pilotを探せ。次に、設定を更新して通知がロック画面に表示されるようにする。

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

アプリ内でBrazeのアプリ内メッセージを使って、プッシュ通知の権限をリクエストできる。これは自社の消費者向けに行う場合と同じだ。このタイプのメッセージをBrazeで作成する方法については、[「プッシュ通知入門：アプリ内メッセージ」]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages)を参照せよ。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## ステップ 5: パイロットでBrazeメッセージングを体験する

これで、Braze Pilotのユーザーとして、Brazeダッシュボードからキャンペーンやキャンバスを受け取る準備が整った。デモワークスペースで公開済みのキャンペーンを閲覧すれば、Brazeのユースケースを簡単に確認できる。その後、本番ワークスペースに移動して、自身のキャンペーン配信を開始するのだ。

Brazeでのキャンペーンとキャンバスの設定方法の詳細については、「はじめに[」を参照のこと。キャンペーンとキャンバス]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases)。