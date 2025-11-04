---
nav_title: ダイナミックSMSリンクプレビュー
article_title: ダイナミックSMSリンクプレビュー
description: "このリファレンス記事では、Movable Ink の SMS プレビュー機能をオンにして使用する方法について説明します。"
page_type: partner
search_tag: Partner
---

# ダイナミック SMS リンクプレビュー

> Movable Ink のダイナミック SMS リンクプレビューを使用すると、SMS と同じコストで MMS の没入感を活用できます。これにより、Braze と Movable Ink を使用して、コスト効率の高いパーソナライズされたリッチなメッセージングエクスペリエンスを実現できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| Movable Ink アカウント | このパートナーシップを活用するには、Movable Ink アカウントが必要です。 |
| データソース | データソースをMovable Inkに接続する必要があります。これは、CSV、Web サイトインポート、または API を使用して実行できます。 |
| MMS送信機能 | Braze 経由でMMS 用に設定されていることを確認します。
| [リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) | リンク短縮がオンになっていることを確認します。 | 
| 連絡先カード | あなたのブランド(送信者)は、iOSと連携するために、リンクプレビューのためにユーザーの電話機に連絡先として保存されなければなりません。これは、連絡先カードまたは別の方法で行うことができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

iOS および Android オペレーティングシステム用のダイナミック SMS リンクを送信するには、以下のそれぞれの手順に従います。

### iOS

{% alert important %}
iOS 用のリンクプレビュー画像を許可するには、ユーザーがブランド (送信者) を連絡先として追加する必要があります。
{% endalert %}

#### ステップ1:連絡先カードキャンペーンを作成する

ユーザーが [連絡先カード]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/)または別の方法でブランドを連絡先として保存したら、[**タップしてプレビューを読み込む**] プロンプトとMovable Ink リンクが表示されます。

![1]{: style="max-width:30%;"}

#### ステップ2:Movable Ink リンクを送信する

1. Movable InkでSMS キャンペーンを作成し、クリックスルー URLを生成します。
2. Braze ダッシュボードで [**キャンペーン**] に移動し、[**キャンペーンを作成**] ドロップダウンから新しい SMS/MMS キャンペーンを設定します。
3. SMS キャンペーン作成画面で、次のようにします。
    - サブスクリプショングループを設定する。
    - メッセージを入力します。
    - Movable Inkリンク**最後の**を、メッセージ本文の他のすべてのテキストの後に追加します。<br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Liquid パーソナライゼーションについて再確認するには、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) を参照してください。  
{% endalert %}

{: start="4"}
4\.ダイナミックな SMS 接続プレビュー キャンペーンをテストして起動するように設定されています。

![3]{: style="max-width:70%;"}

ユーザーがリンクプレビューを読み込むと、パーソナライズされたされた画像がレンダリングされ、Web サイト、アプリ、ランディングページにリンクアウトする機能が示されます。

![4]{: style="max-width:30%;"}

### Android (Google および Samsung デバイス)

Android ユーザーは、ダイナミック SMS リンクプレビューを受信するためにブランドを連絡先として保存する必要はありません。ただし、デバイスが自動的にリンクプレビューを読み込むことができるように、このように保存することが推奨されます。

![5]{: style="max-width:30%;"}

あなたのブランドを連絡先として保存しておらず、自動プレビューをオンにしているユーザーは、プレビュー画像を読み込むために**「プレビューをタップして読み込む**」を選択する必要がある。

![6]{: style="max-width:30%;"}

## 考慮事項

- メッセージには1つのプレビューリンクのみを含めてください。SMS本体に複数のリンクがある場合、コンテンツは生成されません。 
- プレビューリンクの後に文字を含めないでください。そうしないと、破損する可能性があります。


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
