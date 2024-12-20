---
nav_title: 受信トレイビジョン
article_title: 受信トレイビジョン
page_order: 9
description: "この参考記事では、マーケターが様々なメールクライアントやモバイルデバイスの視点からメールを見ることができる機能、Inbox Visionの設定方法を取り上げている。"
tool:
  - Dashboard
channel:
  - email

---

# 受信トレイビジョン

> 受信トレイビジョンを使用すると、さまざまなメールクライアントやモバイルデバイスの観点からメールを表示できます。 

## Inbox Visionでメールをテストする

受信トレイビジョンは、[**ユーザーとしてプレビュー**] に [**ランダムユーザー**] が選択されていて、カスタムユーザーやその他のプレビューユーザーの設定が保持されていない場合に機能します。つまり、**カスタムユーザーを**選択してInbox Visionを実行した場合、Inbox Visionに表示される内容は、他の場所でのメッセージプレビューと異なる可能性がある。 

Inbox Visionでメールメッセージをテストするには、次のようにする：

1. ドラッグアンドドロップエディターまたはHTMLメールエディターにアクセスする。 
2. **プレビューとテスト**」タブを開く。
3. [**受信トレイビジョン**] を選択し、[**受信トレイビジョンを実行**] をクリックします。<br><br> ![][3]{: style="max-width:80%;"}<br><br> すると、Braze は、世界中で使用されているさまざまなメールクライアントに HTML バージョンのメールを送信します。これは完了するまでに 2 ～ 10 分かかる場合があります。<br><br> レンダリングされたHTMLプレビューは3つのセクションに分けられる： 
- **Web クライアント** 
- **アプリケーションクライアント** 
- **モバイルクライアント**<br><br>
4. プレビューの詳細を見るにはタイルを選択する。<br><br> これらのプレビューを表示するには、メールに件名と有効な送信ドメインを含める必要があります。デスクトップとモバイルではメールのレンダリングが異なることを意識しよう。これらのプレビューを見ながら、コンテンツを確認し、メールが意図したとおりに表示されることを確認できます。

{% alert tip %}
Inbox Visionを使って、暗いモードと明るいモードでの違いをテストし、Eメールが正しく送信されているか確認しよう！
{% endalert %}

![HTMLエディター用Inbox Visionの概要。][1]

{: start="5"}
5\.必要であればテンプレートを変更し、[**Re-run Test]**をクリックして更新されたプレビューを確認する。

{% alert important %}
一般に、メールの内容がユーザープロファイル情報などのテンプレート情報に依存している場合、受信トレイビジョンは機能しません。これは、Brazeのテンプレートが、この機能を使ってEメールを送信する際に、空のユーザーになってしまうためである。
{% endalert %}

## コード解析

コード解析は、BrazeがHTMLに存在する可能性のある問題をハイライトする方法であり、各問題の発生回数を表示し、どのHTML要素がサポートされていないかについての洞察を提供する。 

### コード解析情報を見る

この情報は、[**受信トレイビジョン**] タブで <i class="fas fa-list"></i> [**リストビュー**] を選択することで確認できます。このリスト表示はHTMLメールテンプレートのみで利用できる。ドラッグ＆ドロップでメールテンプレートを作成している場合は、プレビューをチェックして、可能性のある問題を解決しよう。

![Inbox Visionプレビューのコード解析例。][2]

{% alert note %}
特定のメールクライアントでは、プレビューよりもコード解析の方が速く表示されることもある。これは、Brazeがスクリーンショットを撮る前に、メールが受信トレイに届くのを待つためだ。
{% endalert %}

## スパム検査

スパムテストでは、送信したメールがスパムフォルダーに入るか、顧客の受信トレイに入るかを予測しようとします。スパムテストは、IronPort、SpamAssassin、Barracudaなどの主要なスパムフィルタや、Gmail.com 、Outlook.com などの主要なインターネットサービスプロバイダ（ISP）フィルタで実行される。

### スパムテストの結果の表示

スパムテストの結果を確認するには、[**受信トレイビジョン**] セクションの [**スパムテスト]** タブをクリックします。**スパムテスト結果**テーブルには、スパムフィルター名、ステータス、タイプがリストされている。

![3つの列を持つスパム検査結果表：名前、ステータス、タイプ。スパムテストに合格したスパムフィルターと ISP フィルターのリストがあります。これは、メールキャンペーンがスパムフォルダーに入れられないことを示します。][4]

これらの結果を確認し、メールキャンペーンに調整を加えた後、**Re-run Testを**クリックしてスパムテスト結果を再読み込みする。

## テストの精度

私たちのテストはすべて、実際の電子メールクライアントを使って実行されている。Brazeは、すべてのレンダリングが可能な限り正確であることを確認するよう努力している。Eメールクライアントに一貫して問題が見られる場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)開く。

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
