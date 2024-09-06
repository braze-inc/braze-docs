---
nav_title: WhatsAppメッセージを作成する
article_title: WhatsAppメッセージを作成する
page_order: 4
description: "この参考記事では、WhatsAppメッセージの作成手順を説明する。"
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsAppメッセージを作成する

> WhatsAppキャンペーンは、顧客に直接アプローチし、プログラム上で会話するのに適している。Liquid などのダイナミックコンテンツを使用して、ユーザー一人ひとりに合わせた体験を作り出し、控えめなブランド体験を強化する環境を作ることができます。 

## 前提条件

WhatsAppメッセージを作成し、WhatsAppチャンネルを活用するには、まずWhatsAppの[概要に]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)目を通し、以下のことを行う必要がある：
  - ポリシー、制限、コンテンツのルールを認識する
  - WhatsApp接続を設定する
  - メッセージに使用する初期テンプレートをMetaで作成する

## ステップ 1:メッセージを作成する場所を選択する

{% alert note %}
WhatsAppは言語ごとに異なる[メッセージテンプレートを](#template-messages)作成する。ユーザーに適切なテンプレートを提供するために、セグメンテーションを使って言語ごとにキャンペーンを作成するか、キャンバスを使う。
{% endalert %}

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. **Campaigns**ページに行き、<i class="fas fa-plus"></i> **Create Campaignを**クリックする。
2. **WhatsAppを**選択するか、複数のチャンネルを対象とするキャンペーンの場合は**マルチチャンネルキャンペーンを**選択する。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて、\[[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)] と \[[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、\[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じコンテンツを持っている場合、バリアントを追加する前にメッセージを作成する。その後、\[**バリアントを追加**] ドロップダウンから \[**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して \[[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. \[[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルターします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. \[[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせたい他のメッセージング・チャンネルを選択する。

{% endtab %}
{% endtabs %}

## ステップ 2:WhatsAppメッセージを作成する

WhatsApp[テンプレートメッセージを](#template-messages)作成するか、レスポンスメッセージを作成するか、用途に応じて選択する。ビジネス主導の会話は承認されたテンプレートから始めなければならないが、応答メッセージは24時間以内のユーザーからのインバウンドメッセージへの応答で使用できる。

{% alert note %}
現在、WhatsAppテンプレートはクーポンコードボタンをサポートしていない。
{% endalert %}

![Message Variantsセクションでは、サブスクリプション・グループと2つのメッセージ・タイプから1つを選択できる：WhatsApp テンプレートメッセージとレスポンスメッセージ。][5]{: style="max-width:80%;"}

### テンプレートメッセージ

[承認されたWhatsAppテンプレートメッセージを使って]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
)WhatsAppユーザーと会話を始めることができる。これらのメッセージは事前にWhatsAppに提出され、内容の承認を受けるが、承認には最大24時間かかる。コピーを編集した場合は、WhatsAppに再送信する必要がある。

無効なテキストフィールド(灰色でハイライト)は、承認されたWhatsAppテンプレートの一部であるため、編集することはできない。無効化されたテキストを更新するには、テンプレートを編集し、再承認を得る必要がある。

#### 言語

各テンプレートには言語が割り当てられているため、ユーザーマッチングを正しく設定するには、言語ごとにキャンペーンまたはキャンバスのステップを作成する必要がある。例えば、インドネシア語と英語が割り当てられたテンプレートを使用するキャンバスを構築する場合、インドネシア語テンプレート用のキャンバス・ステップと英語テンプレート用のキャンバス・ステップを作成する必要がある。

![メッセージのプレビュー、割り当てられた言語、承認されたステータスを含むテンプレートのリスト。][8]{: style="max-width:80%;"}

#### 変数

Meta Business Manager で WhatsApp テンプレートを作成する際に変数を追加した場合、その変数はメッセージ作成時に空白として表示される。これらの空白をリキッドまたはプレーンテキストに置き換える。プレーン・テキストを使うには、二重中括弧で囲まれた "text here "という書式を使う。テンプレート作成時に画像を含めることを選択した場合は、メディアライブラリから画像をアップロードするか追加する。

無効化されたテキストフィールド(灰色でハイライト)は、承認されたWhatsAppテンプレートの一部であるため、編集することはできない。無効化されたテキストを更新したい場合は、テンプレートを編集し、再承認を得る必要がある。

{% alert tip %}
{% raw %}
Liquidを使用する場合は、受信者のユーザープロファイルが不完全な場合、メッセージを受信しないように、選択したパーソナライゼーションのデフォルト値を必ず含めること。Liquid変数が欠落しているメッセージはWhatsAppで送信されない。
{% endraw %}
{% endalert %}

![パーソナライズの追加ツールで、属性 "first_name "とデフォルト値 "you "を指定する。][2]{: style="max-width:80%;"}

### ダイナミック・リンク 

コールトゥアクションのURLは変数を含むことができるが、Metaは`{% raw %}https://example.com/{{variable}}{% endraw %}` のようにURLの末尾に置くことを要求している。リンクはテンプレートの一部として本文に含めることもできる。現時点では、どちらのリンクも短縮することはできない。 

### 応答メッセージ

{% alert note %}
レスポンス・メッセージは現在、早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

ユーザーからのインバウンドメッセージに返信するために、レスポンスメッセージを使うことができる。これらのメッセージは、作曲体験中にBrazeのアプリ内に組み込まれ、いつでも編集することができる。リキッドを使えば、応答メッセージの言語を適切なユーザーに合わせることができる。

使用できるレスポンス・メッセージのレイアウトは3種類ある：
- クイック・リプライ
- テキストメッセージ
- メディア・メッセージ

![新規ユーザーを割引コードで歓迎する返信メッセージの作成者。][6]{: style="max-width:80%;"}

## ステップ 3:メッセージをプレビューしてテストする

Brazeでは、メッセージを送信する前にプレビューしてテストすることを常に推奨している。**テスト]**タブに切り替えると、テスト用のWhatsAppメッセージを[コンテンツテストグループや]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups)個々のユーザーに送信したり、Brazeで直接ユーザーとしてメッセージをプレビューすることができる。

![スザンヌという名前の既存ユーザーのプレビュー・メッセージ。][3]{: style="max-width:80%;"}

{% alert note %}
テスト・メッセージを含む応答メッセージを送信するには、会話ウィンドウが必要である。会話ウィンドウを開くには、このメッセージに使用する購読グループに関連付けられている電話番号にWhatsAppメッセージを送信する。関連する電話番号は、**Test**タブのアラートに表示される。
{% endalert %}

![テストするには、まずWhatsAppメッセージを+1 631-202-0907に送信して会話ウィンドウを開いてください」というアラート。その後、テストユーザーに応答メッセージを送信する。"][7]{: style="max-width:80%;"}

## ステップ 4:キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を構築する。WhatsAppメッセージ作成に最適なツールの使い方については以下のセクションを参照。

#### 配信スケジュールまたはトリガーを選択する

WhatsAppメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信することができる。詳しくは、[キャンペーンのスケジューリングを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)参照のこと。

アクションベースの配信では、キャンペーンの継続時間と \[[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、ユーザーがキャンペーンを受信する[再資格を]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)得ることを許可したり、[頻度の上限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりするなど、配信コントロールを指定することもできる。

#### ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択することで、[ユーザーを絞り込む]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)必要がある。すでにサブスクリプショングループを選択しているため、ユーザーがブランドに対して希望しているコミュニケーションの頻度やカテゴリによって、ユーザーが絞り込まれます。このステップでは、セグメントからより多くのオーディエンスを選択し、フィルターを使ってさらにセグメントを絞り込む。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメント・メンバーシップは、常にメッセージが送信される直前に計算されることを覚えておいてほしい。

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを許可することができる。

独自のユースケースに基づいて、カスタムコンバージョンイベントを設定することもできます。クリエイティブになり、このキャンペーンの成功をどのように測りたいかを考えよう。

{% endtab %}

{% tab キャンバス %}

まだやっていない場合は、キャンバス・コンポーネントの残りのセクションを完成させる。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)ステップを参照のこと。

会話ウィンドウは1つの受信メッセージにつき24時間しか使用できないため、Brazeは受信メッセージと応答メッセージの間に24時間を超える遅延がないことを確認する。 

{% endtab %}
{% endtabs %}

## ステップ 5: レビューと展開

キャンペーンやキャンバスの最後の構築が終わったら、その詳細を確認し、テストしてから送信する！

次に、[WhatsAppのレポート]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/)機能を使ってWhatsAppキャンペーンの結果を確認しよう。

## サポートされているWhatsAppの機能

Brazeは以下のWhatsAppメッセージ機能をサポートしている。

### アウトバウンドメッセージ

WhatsAppのメッセージで以下の内容をユーザーに送ることができる：

メッセージ機能    | 詳細
----------- |---------------- 
ヘッダー | 
テキスト | 可変パラメーターをサポートする
画像（JPEGおよびPNG） | 8ビット、RGBまたはRGBAでなければならない。 
本文 | 可変パラメーターをサポートする
フッターテキスト | 可変パラメーターをサポートする 
CTA | [行動喚起を](#ctas)参照のこと。
{: .reset-td-br-1 .reset-td-br-2}

#### 行動への呼びかけ {#ctas}

WhatsAppメッセージに次のような行動喚起を追加できる：

CTAタイプ    | 詳細
----------- |---------------- 
ウェブサイトを見る | メッセージテンプレートのみで利用可能。<br>最大1ボタン（可変パラメーターを含む）。
電話番号 | メッセージテンプレートのみで利用可能。<br>ボタンは最大1つだ。
カスタムクイック返信ボタン | ボタンは3つまでだ。 
マーケティング・オプトアウト・ボタン | このオプションは、購読ステータスを自動的に更新しない。<br><br>設定方法については、[オプトインとオプトアウトを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection)参照のこと。
{: .reset-td-br-1 .reset-td-br-2}

### インバウンドメッセージ

ユーザーはWhatsAppのメッセージで以下の内容を送ることができる：

メッセージ機能    | 詳細
----------- |---------------- 
テキスト | 
画像（JPEGおよびPNG）| 8ビット、RGBまたはRGBAでなければならない。 
オーディオ| オーディオ/AAC<br>オーディオ/mp4<br>オーディオ/MPEG<br>オーディオ/AMR<br>audio/ogg （Opus コーデックのみ、ベース audio/ogg はサポートされていない）
文書 | テキスト/プレーン<br>アプリケーション/pdf<br>application/vnd.ms-powerpoint<br>アプリケーション/msword<br>application/vnd.ms-excel<br>application/vnd.openxmlformats-officedocument.wordprocessingml.document<br>application/vnd.openxmlformats-officedocument.presentationml.presentation<br>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
CTA | [行動喚起を](#ctas)参照のこと。
動画 | ビデオ/MP4、ビデオ/3GP<br><br>H.264 ビデオコーデックとAACオーディオコーデックのみがサポートされている。オーディオ・ストリームが1つだけのビデオや、オーディオ・ストリームがないビデオもサポートしている。
{: .reset-td-br-1 .reset-td-br-2}



[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
