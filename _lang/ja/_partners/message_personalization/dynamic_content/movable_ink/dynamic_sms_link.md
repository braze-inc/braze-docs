---
nav_title: ダイナミック SMS リンクプレビュー
article_title:ダイナミック SMS リンクプレビュー
description:「この参考記事では、Movable InkのSMSリンクプレビュー機能をオンにして使用する方法の概要を説明しています。「
page_type: partner
search_tag:Partner
---

# ダイナミック SMS リンクプレビュー

> Movable Inkのダイナミックな SMSリンクプレビューを使用すると、SMSと同じコストでMMSの没入感を活用できます。これにより、BrazeとMovable Inkを使用して、費用対効果が高く、パーソナライズされたリッチなメッセージングエクスペリエンスを提供できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
|  | このパートナーシップを利用するには、Movable Inkアカウントが必要です。 |
| データソース | データソースを Movable Ink に接続する必要があります。これは、CSV、Web サイトインポート、またはAPIを使用して実行できます。 |
| MMS 送信機能 | Braze で MMS の設定が完了していることを確認します。
| [リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) | リンク短縮機能がオンになっていることを確認します。 | 
| 連絡先カード | iOSでリンクプレビューを使用するには、ブランド（送信者）を連絡先としてユーザーの電話に保存する必要があります。これは、連絡先カードまたは別の方法で行うことができます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

iOS および Android オペレーティングシステム用のダイナミックな SMS リンクを送信するには、以下のそれぞれの手順に従ってください。

### iOS

{% alert important %}
iOSのリンクプレビュー画像を許可するには、ユーザーはブランド (送信者) を連絡先として追加する必要があります。
{% endalert %}

#### ステップ1:連絡先カードキャンペーンを作成する

[ユーザーがブランドを連絡先としてBrazeコンテンツカードまたは他の方法で保存すると]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)、**タップしてロードプレビューのプロンプトとMovable** Inkリンクを表示できるようになります。

![1]{: style="max-width:30%;"}

#### ステップ2:ムーバブルインクのリンクを送信

1. Movable Ink で SMS キャンペーンを作成し、クリックスルー URLを生成します。
2. **Braze ダッシュボードの「**キャンペーン**」に移動し、「キャンペーンの作成」ドロップダウンから新しい SMS/MMS キャンペーンを設定します。**
3. SMS キャンペーンコンポーザーの場合:
    - サブスクリプショングループを設定します。
    - メッセージを入力します。
    - メッセージ本文の他のテキストの後に、Movable Ink **リンクを最後に追加します**。<br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
[Liquidのパーソナライゼーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)の復習については、Liquidをご覧ください。  
{% endalert %}

{: start="4"}
4\.これで、ダイナミックな SMS リンクプレビューキャンペーンをテストして開始する準備が整いました。

![3]{: style="max-width:70%;"}

ユーザーがリンクプレビュー読み込むと、パーソナライズされた画像, 写真がレンダリングされ、Web サイト、アプリ、またはランディングページにリンクできるようになります。

![4]{: style="max-width:30%;"}

### Android (グーグルとサムスンのデバイス)

Android ユーザーは、ブランドを連絡先として保存しなくてもダイナミックな SMS リンクプレビューを受信できます。ただし、デバイスがリンクプレビューを自動的に読み込むめるようにすることをおすすめします。

![5]{: style="max-width:30%;"}

ブランドを連絡先として保存しておらず、自動プレビューを有効にしているユーザーは、プレビュー画像, 写真読み込むには \[**タップしてプレビュー読み込む]** を選択する必要があります。<br>![6]{: style="max-width:30%;"}

## 考慮事項

- メッセージにはプレビューリンクを 1 つだけ含めてください。SMS 本文に複数のリンクがあるコンテンツは生成されません。 
- プレビューリンクの後に文字を含めないでください。文字を含めると、エクスペリエンスが損なわれる可能性があります。


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
