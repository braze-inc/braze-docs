---
nav_title: ダイナミックSMSリンクプレビュー
article_title: ダイナミックSMSリンクプレビュー
description: "ここでは、Movable InkのSMSリンクプレビュー機能を有効にして使用する方法について説明します。"
page_type: partner
search_tag: Partner
---

# ダイナミックSMS連携プレビュー

> Movable Ink のダイナミックな SMS リンクプレビューを使用すると、SMS と同じ料金でMMS の没入感を活用できます。これにより、BrazeとMovable Inkを使用して、コスト効率の高いパーソナライズされた豊富なメッセージングエクスペリエンスを実現できます。

## 前提条件

| 要件 | 説明 |
| --- | --- |
| Movable Ink勘定 | この提携の前進タグeを考慮するには、Movable Inkな考慮が必要である。 |
| データソース | データソースをMovable Inkに接続する必要があります。これは、CSV、Web サイト読み込み、またはAPI を使用して実行できます。 |
| MMS送信機能 | Braze 経由でMMS 用に設定されていることを確認します。
| [リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) | リンク短縮がオンになっていることを確認します。 | 
| コンタクトカード | あなたのブランド(送信者)は、iOSと連携するために、リンクプレビューのためにユーザーの電話機に連絡先として保存されなければなりません。これは、連絡先カードまたは別のメソッドで行うことができます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

以下の各ステップs に従って、iOS とAndroid オペレーティングシステム s のダイナミックな SMS を送信します。

### iOS

{% alert important %}
iOSのリンクプレビュー "画像sを許可するには、ユーザーsが連絡先としてブランド(送信者)を追加する必要があります。
{% endalert %}

#### ステップ1:コンタクトカードキャンペーンの作成

ユーザー が連絡先としてブランドを保存した後、Braze [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) または別の方法で、**タップしてプレビューをロード** プロンプトとMovable Inkリンクを表示できます。

![1]{: style="max-width:30%;"}

#### ステップ2:Movable Ink送信

1. Movable InkでSMS キャンペーンを作成し、クリックスルー URLを生成します。
2. Braze ダッシュボードで、**キャンペーン s** に移動し、**キャンペーン** ドロップダウンから新しいSMS/MMS キャンペーンを設定します。
3. キャンペーン作成者:
    - サブスクリプショングループを設定する。
    - メッセージを入力します。
    - Movable Inkリンク**最後の**を、メッセージ本文の他のすべてのテキストの後に追加します。<br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
リキッドパーソナライゼーションのリフレッシュ版は[リキッド]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)をご覧ください。  
{% endalert %}

{: start="4"}
4\.ダイナミックな SMS 接続プレビュー キャンペーンをテストして起動するように設定されています。

![3]{: style="max-width:70%;"}

ユーザー s がリンクプレビューを読み込むすると、パーソナライズされた "画像がレンダリングされ、Web サイト、アプリ、またはランディングページにリンクアウトできます。

![4]{: style="max-width:30%;"}

### Android(グーグル&アンプ、サムスン端末)

Android ユーザー は、ダイナミックなのSMS リンクプレビューを受信するために、連絡先としてブランドを保存する必要はありません。ただし、自動的にリンクプレビューs を読み込むできるようにすることをお勧めします。

![5]{: style="max-width:30%;"}

連絡先としてブランドを保存しておらず、自動プレビューを有効にしているユーザは、**タップしてプレビュー"画像を読み込むするために**を選択する必要があります。<br>![6]{: style="max-width:30%;"}

## 考慮事項

- 1つのプレビューのみを表示します。SMS本体に複数のリンクがある場合、コンテンツは生成されません。 
- プレビューリンクの後に文字を含めないでください。そうしないと、破損する可能性があります。


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
