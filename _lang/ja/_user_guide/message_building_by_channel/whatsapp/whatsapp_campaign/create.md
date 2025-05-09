---
nav_title: WhatsAppメッセージを作成する
article_title: WhatsAppメッセージを作成する
page_order: 4
description: "この記事では、WhatsApp メッセージの構築と作成に関連するステップについて説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsAppメッセージを作成する

> WhatsApp キャンペーンは、顧客に直接リーチしてプログラムを使って会話を行うのに適しています。Liquid などのダイナミックコンテンツを使用して、ユーザー一人ひとりに合わせた体験を作り出し、控えめなブランド体験を強化する環境を作ることができます。 

## 前提条件

WhatsAppメッセージを作成する前に、[WhatsAppの概要を]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)確認し、以下の項目を完了する必要がある：
  - ポリシー、制限、コンテンツのルールを認識する
  - WhatsApp接続を設定する
  - メッセージに使用する初期テンプレートをMetaで作成する

## メッセージを作成する

### ステップ 1: メッセージを作成する場所を選択する

{% alert note %}
WhatsAppは言語ごとに異なる[メッセージテンプレートを](#template-messages)作成する。ユーザーに適切なテンプレートを提供するために、セグメンテーションを使って言語ごとにキャンペーンを作成するか、キャンバスを使う。
{% endalert %}

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. [**キャンペーン**] ページに移動して、<i class="fas fa-plus"></i> [**キャンペーンを作成**] をクリックします。
2. [**WhatsApp**] を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は [**マルチチャンネルキャンペーン**] を選択します。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて、[[チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)] と [[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、[[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じコンテンツを持っている場合、バリアントを追加する前にメッセージを作成する。その後、[**バリアントを追加**] ドロップダウンから [**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. [[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルターします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. このメッセージと組み合わせる他のメッセージングチャネルを選択します。

{% alert tip %}
アクションベースのキャンバスがインバウンド WhatsApp メッセージによってトリガーされる場合、次のアクションパスまで、どのキャンバスステップでも WhatsApp プロパティを参照できます。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 2: WhatsAppメッセージを作成する

ユースケースに応じて WhatsApp [テンプレートメッセージ](#template-messages)を作成するか、応答メッセージを作成します。ビジネス主導の会話は承認されたテンプレートから始めなければならないが、応答メッセージは24時間以内のユーザーからのインバウンドメッセージへの応答で使用できる。

![「メッセージバリアント」セクションでは、サブスクリプショングループを 1 つと、2 つのメッセージタイプのいずれかを選択できます。WhatsApp テンプレートメッセージとレスポンスメッセージ。][5]{: style="max-width:80%;"}

#### テンプレートメッセージ

[承認済みの WhatsApp テンプレートメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
)を使って WhatsApp ユーザーと会話を始めることができます。これらのメッセージは事前に WhatsApp に提出され、コンテンツの承認を受けますが、承認には最大 24 時間かかります。コピーを編集した場合は、WhatsApp に再送信する必要があります。

無効なテキストフィールド(灰色でハイライト)は、承認されたWhatsAppテンプレートの一部であるため、編集することはできない。無効化されたテキストを更新するには、テンプレートを編集し、再承認を得る必要がある。

##### 言語

各テンプレートには言語が割り当てられているため、ユーザーマッチングを正しく設定するには、言語ごとにキャンペーンまたはキャンバスのステップを作成する必要がある。例えば、インドネシア語と英語が割り当てられたテンプレートを使用するキャンバスを作成する場合、インドネシア語テンプレート用のキャンバスステップと英語テンプレート用のキャンバスステップを作成する必要があります。

![メッセージのプレビュー、割り当てられた言語、承認されたステータスを含むテンプレートのリスト。][8]{: style="max-width:80%;"}

右から左に書かれた言語でコピーを追加する場合、右から左に書かれたメッセージの最終的な見た目は、サービスプロバイダーがどのようにそれらをレンダリングするかに大きく左右されることに注意してください。右から左へのメッセージを可能な限り正確に表示するためのベストプラクティスについては、[右から左へのメッセージを作成する]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

##### 変数

Meta Business Manager で WhatsApp テンプレートを作成する際に変数を追加した場合、それらはメッセージ作成画面に空白として表示されます。これらの空白をリキッドまたはプレーンテキストに置き換える。プレーン・テキストを使うには、二重中括弧で囲まれた "text here "という書式を使う。テンプレートのビルド時にイメージを含めることを選択した場合は、メディアライブラリからイメージをアップロードまたは追加するか、イメージのURL を参照することができます。

無効化されたテキストフィールド(灰色でハイライト)は、承認されたWhatsAppテンプレートの一部であるため、編集することはできない。無効化されたテキストを更新したい場合は、テンプレートを編集し、再承認を得る必要がある。

{% alert tip %}
{% raw %}
Liquidを使用する場合は、受信者のユーザープロファイルが不完全な場合、メッセージを受信しないように、選択したパーソナライゼーションのデフォルト値を必ず含めること。WhatsAppから送信されるメッセージにLiquid変数が含まれていない。
{% endraw %}
{% endalert %}

![属性 "first_name" とデフォルト値 "you" を使用したパーソナライゼーション追加ツール。][2]{: style="max-width:80%;"}

#### ダイナミック・リンク 

コールトゥアクション URL は、Meta では `{% raw %}https://example.com/{{variable}}{% endraw %}` のように URL の末尾になければなりませんが、URL に変数を含めることができます。この変数は Braze で Liquid に置き換えることができます。リンクはテンプレートの一部として本文に含めることもできる。現時点では、どちらのリンクも短縮することはできない。 

#### 応答メッセージ

ユーザーからのインバウンドメッセージに返信するために、応答メッセージを使うことができます。これらのメッセージは、作成中に Braze のアプリ内で作成され、いつでも編集できます。Liquid を使えば、応答メッセージの言語を適切なユーザーに合わせることができます。

使用できるレスポンス・メッセージのレイアウトは3種類ある：
- クイック返信
- テキストメッセージ
- メディア・メッセージ

![新規ユーザーを割引コードで歓迎する返信メッセージの作成者。][6]{: style="max-width:80%;"}

### ステップ 3: メッセージをプレビューしてテストする

Brazeでは、メッセージを送信する前にプレビューしてテストすることを常に推奨している。[**テスト**] タブに切り替えて、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups)または個々のユーザーにテスト用の WhatsApp メッセージを送信するか、ユーザーとしてメッセージを Braze で直接プレビューします。

![Suzanne という名前の既存ユーザー用のプレビューメッセージ。][3]{: style="max-width:80%;"}

{% alert note %}
テストメッセージを含む応答メッセージを送信するには、会話ウィンドウが必要です。会話ウィンドウを開くには、このメッセージに使用する購読グループに関連付けられている電話番号にWhatsAppメッセージを送信する。関連する電話番号は、**Test**タブのアラートに表示される。
{% endalert %}

![テストするには、まずWhatsAppメッセージを+1 631-202-0907に送信して会話ウィンドウを開いてください」というアラート。その後、テストユーザーに応答メッセージを送信します。」][7]{: style="max-width:80%;"}

### ステップ 4: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を作成します。WhatsAppメッセージ作成に最適なツールの使い方については以下のセクションを参照。

#### 配信スケジュールまたはトリガーを選択する

WhatsApp メッセージは、スケジュールされた時刻、アクション、または API トリガーに基づいて配信することができます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信では、キャンペーンの継続時間と [[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、配信コントロールを指定できます。例えば、ユーザーを[再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)してキャンペーンを受信できるようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりできます。

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択して[ユーザーをターゲットに設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)し、オーディエンスを絞り込む必要があります。すでにサブスクリプショングループを選択しているため、ユーザーがブランドに対して希望しているコミュニケーションの頻度やカテゴリによって、ユーザーが絞り込まれます。このステップでは、セグメントからより多くのオーディエンスを選択し、フィルターを使ってさらにセグメントを絞り込みます。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを許可することができる。

独自のユースケースに基づいて、カスタムコンバージョンイベントを設定することもできます。このキャンペーンの真の成功を測定する方法について独創的に考えてみましょう。

{% endtab %}

{% tab キャンバス %}

キャンバスコンポーネントが完成していない場合は、残りのセクションを完成させます。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)ステップを参照のこと。

対話ウィンドウはインバウンドメッセージごとに 24 時間しか継続できないため、Braze はインバウンドメッセージと応答メッセージの間に 24 時間を超える遅延がないことを確認します。 

{% endtab %}
{% endtabs %}

### ステップ 5: レビューと展開

キャンペーンやキャンバスの最後の構築が終わったら、その詳細を確認し、テストしてから送信する！

次に、[WhatsAppのレポート]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/)機能を使ってWhatsAppキャンペーンの結果を確認しよう。

## サポートされているWhatsAppの機能

### アウトバウンドメッセージ

Brazeを通じて送信するWhatsAppメッセージには、以下の機能がサポートされている：

| 機能 | 詳細 | 最大サイズ | 対応フォーマット |
| ------- | ------- | ------------- | ---------------------- |
| ヘッダーテキスト | 文字列と可変パラメーターがサポートされている。 | - | -
| 本文テキスト | 文字列と可変パラメーターがサポートされている。 | - | - |
| フッターテキスト | 文字列と可変パラメーターがサポートされている。 | - | - |
| CTAリンク | 様々なコール・トゥ・アクション（CTA）タイプがサポートされている。詳細は[コール・トゥ・アクションの種類を](#ctas)参照のこと。 | - | - |
| 画像 | 画像, 写真を本文の中に埋め込むことができる。8ビットで、RGBまたはRGBAのカラーモデルを使用しなければならない。 | < 5 MB | `.png``.jpg` 、 `.jpeg` |
| ドキュメント | ドキュメントは本文の中に埋め込むことができる。ファイルはURLを通してホストされなければならない。 | < 100 MB | `.txt``.xls`,`.xlsx`,`.doc`,`.docx`,`.ppt`,`.pttx` 、 `.pdf` |
| 動画 | 動画は本文中に埋め込むことができる。ファイルはURLまたは[Brazeメディアライブラリーで]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)ホストされていること。 | < 16 MB | `.3gp`, `.mp4` |
| オーディオ | 音声はレスポンシブ・メッセージングでのみサポートされる。ファイルはURLを通してホストされなければならない。 | < 16 MB | `.aac``.amr`,`.mp3`,`.mp4` 、 `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

<sup>_\*現在アーリーアクセス中。参加をご希望の方は、Brazeアカウントマネージャーにご連絡を。_</sup>

### インバウンドメッセージ

Brazeで受信したWhatsAppメッセージには、以下の機能がサポートされている：

| 機能 | 詳細 | 対応フォーマット |
| ------- | ------- | ------------------ |
| 本文テキスト | 標準文字列のみがサポートされている。 | - |
| 画像 | 画像は8ビットで、RGBまたはRGBAのカラーモデルを使用すること。ファイルは5MB以下でなければならない。 | `.jpg`, `.png` |
| オーディオ | OpusコーデックでエンコードされたOggファイルのみがサポートされている。他のOggフォーマットは違う。 | `.aac``.mp4`,`.mpeg`,`.amr` 、 `.ogg (Opus only)` |
| 文書 | ドキュメントはメッセージ添付でサポートされる。 | `.txt``.pdf`,`.ppt`,`.doc`,`.xls`,`.docx`,`.pptx` 、 `.xlsx` |
| 動画 | H.264 ビデオコーデックと AAC オーディオコーデックのみがサポートされます。動画は単一のオーディオストリームを持つか、オーディオストリームを持たないかのいずれかでなければならない。 | `.mp4`, `.3gp` |
| CTAリンク | 様々なコール・トゥ・アクション（CTA）タイプがサポートされている。詳細は[コール・トゥ・アクションの種類を](#ctas)参照のこと。 | - |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### コール・トゥ・アクションの種類 {#ctas}

Brazeを通じて送信するWhatsAppメッセージでは、以下のコールトゥアクションタイプがサポートされています：

| CTAタイプ    | 詳細 |
| ----------- |---------------- | 
| ウェブサイトを見る | 最大1ボタン（可変パラメーターを含む）。 |
| 電話番号にかける | メッセージテンプレートのみで利用可能。<br>ボタンは最大 1 つ。 |
| カスタムクイック返信ボタン | ボタンは最大 3 つ。 |
| マーケティング・オプトアウト・ボタン | デフォルトでは、サブスクリプションのステータスは自動更新されない。詳しい説明は、[オプトインとオプトアウトを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection)参照のこと。 |
| クーポンコードメッセージテンプレート | メッセージテンプレートのみで利用可能。<br>これらのテンプレートは、他のメッセージテンプレートと同様に開いたり編集したりできます。また、Liquid と Braze のプロモーションコードと互換性があります。 |
| CTA応答メッセージ  | アクションへの呼び出しボタンを含む応答メッセージを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
