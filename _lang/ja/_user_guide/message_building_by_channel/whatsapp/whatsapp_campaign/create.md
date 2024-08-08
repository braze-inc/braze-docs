---
nav_title: WhatsAppメッセージの作成
article_title: WhatsAppメッセージの作成
page_order: 4
description: "このリファレンス記事では、WhatsApp メッセージの構築と作成に必要な手順について説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsAppメッセージの作成

> WhatsApp キャンペーンは、顧客に直接アプローチし、プログラム的に会話するのに最適です。Liquid やその他の動的コンテンツを使用すると、ユーザーとのパーソナルなエクスペリエンスを生み出し、ブランドのユーザー エクスペリエンスを邪魔にならない形で促進し強化する環境を作り出すことができます。 

## 前提条件

WhatsApp メッセージを作成し、WhatsApp チャネルを活用するには、まず WhatsApp の [概要]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) を読み、次の操作を行う必要があります。
  \- ポリシー、制限、コンテンツルールを理解する
  \- WhatsApp接続を設定する
  \- メッセージで使用するための初期テンプレートをMetaで作成する

## ステップ 1:メッセージを構築する場所を選択する

{% alert note %}
WhatsApp は言語ごとに異なる [メッセージ テンプレート](#template-messages) を作成します。ユーザーに適切なテンプレートを提供するために、セグメンテーションを使用して各言語のキャンペーンを作成するか、Canvas を使用します。
{% endalert %}

メッセージをキャンペーンを使用して送信するべきか、キャンバスを使用して送信するべきか分からない場合キャンペーンは単一のシンプルなメッセージング キャンペーンに適しており、キャンバスは複数ステップのユーザー ジャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. **キャンペーン** ページに移動してクリックします <i class="fas fa-plus"></i>**キャンペーンを作成します**。
2. **WhatsApp**を選択するか、複数のチャネルを対象とするキャンペーンの場合は、 **マルチチャネルキャンペーン**を選択します。
3. キャンペーンには明確で意味のある名前を付けます。
4. 必要に応じて [チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) と [タグを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) 追加します。
   * タグを使用すると、キャンペーンを簡単に見つけてレポートを作成できるようになります。たとえば、 [レポート ビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数のバリエーションを追加して名前を付けます。追加したバリエーションごとに、異なるプラットフォーム、メッセージ タイプ、レイアウトを選択できます。このトピックの詳細については、[「多変量テストと A/B テスト」]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容である場合は、バリエーションを追加する前にメッセージを作成してください。次に、**「バリアントの追加」** ドロップダウンから **「バリアントからコピー」を** 選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**ステップ:**

1. Canvas コンポーザーを使用して[Canvas を作成します]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) 。
2. キャンバスを設定したら、キャンバス ビルダーにステップを追加します。ステップに明確で意味のある名前を付けます。
3. [ステップ スケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップの対象者をフィルタリングします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込みます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [前進行動を]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)選択してください。
6. メッセージと組み合わせるその他のメッセージング チャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2:WhatsAppメッセージを作成する

使用事例に応じて、WhatsApp [テンプレート メッセージ](#template-messages) または応答メッセージを作成するかどうかを選択します。ビジネスで開始される会話はすべて承認されたテンプレートから開始する必要がありますが、応答メッセージは 24 時間以内にユーザーからの受信メッセージに応答するために使用できます。 

![メッセージ バリアント セクションでは、サブスクリプション グループと 2 つのメッセージ タイプのいずれかを選択できます。WhatsApp テンプレートメッセージと応答メッセージ。][5]{: style="max-width:80%;"}

### テンプレートメッセージ

[承認された WhatsApp テンプレート メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) を使用して、WhatsApp でユーザーとの会話を開始できます。これらのメッセージはコンテンツの承認のために事前に WhatsApp に送信され、承認には最大 24 時間かかる場合があります。コピーに加えた編集はすべて編集して WhatsApp に再送信する必要があります。

無効なテキスト フィールド (灰色で強調表示) は、承認された WhatsApp テンプレートの一部であるため、編集できません。無効になったテキストを更新するには、テンプレートを編集して再承認を受ける必要があります。

#### 言語

各テンプレートには言語が割り当てられているため、ユーザー マッチングを正しく設定するには、言語ごとにキャンペーンまたはキャンバス ステップを作成する必要があります。たとえば、インドネシア語と英語が割り当てられたテンプレートを使用する Canvas を構築する場合は、インドネシア語テンプレート用の Canvas ステップと英語テンプレート用の Canvas ステップを作成する必要があります。

![メッセージのプレビュー、割り当てられた言語、承認ステータスを含むテンプレートのリスト。][8]{: style="max-width:80%;"}

#### 変数

Meta Business Manager で WhatsApp テンプレートを作成するときに変数を追加した場合、それらの変数はメッセージ コンポーザーで空白として表示されます。これらの空白を Liquid またはプレーンテキストに置き換えます。プレーンテキストを使用するには、二重中括弧で囲まれた「text here」という形式を使用します。テンプレートを作成するときに画像を含めることを選択した場合は、メディア ライブラリから画像をアップロードまたは追加します。

無効なテキスト フィールド (灰色で強調表示) は、承認された WhatsApp テンプレートの一部であるため、編集できないことに注意してください。無効になっているテキストを更新する場合は、テンプレートを編集して再承認を受ける必要があります。

{% alert tip %}
{% raw %}
Liquid を使用する予定の場合は、選択したパーソナライズのデフォルト値を必ず含めてください。そうすれば、受信者のユーザー プロファイルが不完全な場合に、受信者はメッセージを受信しません。Liquid 変数が欠落しているメッセージは WhatsApp 経由で送信されません。
{% endraw %}
{% endalert %}

![属性「first\_name」とデフォルト値「you」を持つパーソナライゼーションの追加ツール。][2]{: style="max-width:80%;"}

### ダイナミックリンク 

行動喚起のURLには変数を含めることができますが、MetaではURLの末尾に変数を置く必要があります。 `{% raw %}https://example.com/{{variable}}{% endraw %}`ここで、変数は Braze で Liquid に置き換えることができます。リンクはテンプレートの一部として本文テキストとして含めることもできます。現時点では、どちらのリンクも短縮できません。 

### 応答メッセージ

{% alert note %}
応答メッセージは現在早期アクセス段階です。早期アクセスへの参加にご興味がある場合は、Braze アカウント マネージャーにお問い合わせください。
{% endalert %}

応答メッセージを使用して、ユーザーからの受信メッセージに返信できます。これらのメッセージは、Braze のアプリ内で作成され、いつでも編集できます。Liquid を使用すると、応答メッセージの言語を適切なユーザーに一致させることができます。

使用できる応答メッセージ レイアウトは 3 つあります。
\- 素早い返信
\- メール
\- メディアメッセージ

![割引コードで新規ユーザーを歓迎する返信メッセージの応答メッセージ作成者。][6]{: style="max-width:80%;"}

## ステップ 3:メッセージをプレビューしてテストする

Braze では、メッセージを送信する前に必ずプレビューしてテストすることをお勧めします。**[テスト]** タブに切り替えて、 [コンテンツ テスト グループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) または個々のユーザーにテスト WhatsApp メッセージを送信するか、Braze でユーザーとして直接メッセージをプレビューします。

![Suzanne という既存のユーザーへのプレビュー メッセージ。][3]{: style="max-width:80%;"}

{% alert note %}
テスト メッセージを含む応答メッセージを送信するには、会話ウィンドウが必要です。会話ウィンドウを開始するには、このメッセージに使用しているサブスクリプション グループに関連付けられている電話番号に WhatsApp メッセージを送信します。関連付けられている電話番号は、**[テスト]** タブのアラートに表示されます。
{% endalert %}

![「テストするには、まず +1 631-202-0907 に WhatsApp メッセージを送信して会話ウィンドウを開いてください」という警告が表示されます。次に、応答メッセージをテストユーザーに送信します。"][7]{: style="max-width:80%;"}

## ステップ 4: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab Campaign %}

次に、キャンペーンの残りの部分を構築します。WhatsApp メッセージを作成するために当社のツールを最適に使用する方法の詳細については、次のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

WhatsApp メッセージは、スケジュールされた時間、アクション、または API トリガーに基づいて配信できます。詳細については、[「キャンペーンのスケジュール設定」]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信では、キャンペーンの期間と [休止時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)を設定することもできます。

このステップでは、ユーザーがキャンペーンを [再度]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) 受信できるようにする、 [フリークエンシー キャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) ルールを有効にするなどの配信コントロールを指定することもできます。

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、 [ユーザーをターゲットにする]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 必要があります。すでにサブスクリプション グループを選択しているはずです。これにより、ユーザーがあなたとのコミュニケーションを希望するレベルまたはカテゴリによって、ユーザーが絞り込まれます。このステップでは、セグメントからより大きなオーディエンスを選択し、フィルターを使用してそのセグメントをさらに絞り込みます。おおよそのセグメント人口が現在どのような状態であるかを示すスナップショットが自動的に表示されます。正確なセグメント メンバーシップは常に、メッセージが送信される直前に計算されることに注意してください。

#### コンバージョンイベントを選択する

Braze を使用すると、キャンペーンを受け取った後にユーザーが特定のアクション、 [つまりコンバージョン イベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる期間を最大 30 日間に設定できます。

特定のユースケースに基づいてカスタム変換イベントを設定することもできます。創造力を働かせて、このキャンペーンの成功を実際にどのように測定したいか考えてみましょう。

{% endtab %}

{% tab Canvas %}

まだ行っていない場合は、Canvas コンポーネントの残りのセクションを完了します。キャンバスの残りの部分を構築する方法、多変量テストとインテリジェント選択を実装する方法などの詳細については、キャンバスのドキュメントの [キャンバスの構築]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) 手順を参照してください。

会話ウィンドウは受信メッセージごとに 24 時間しか持続しないため、Braze は受信メッセージと応答メッセージの間に 24 時間を超える遅延がないことを確認します。 

{% endtab %}
{% endtabs %}

## ステップ 5: レビューと展開

キャンペーンまたはキャンバスの最後の部分の作成が完了したら、詳細を確認し、テストしてから送信してください。

次に、[WhatsApp レポート]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) をチェックして、WhatsApp キャンペーンの結果にアクセスする方法を学びます。

## サポートされているWhatsApp機能

Braze は次の WhatsApp メッセージング機能をサポートしています。

### 送信メッセージ

WhatsApp メッセージでユーザーに次の内容を送信できます。

メッセージ機能 | 詳細
----------- |----------------
ヘッダー |
テキスト | 可変パラメータをサポート
画像 (JPEG および PNG) | 8 ビット、RGB または RGBA で、どのタイプでも最大 5 MB である必要があります。
本文 | 可変パラメータをサポート
フッターテキスト | 可変パラメータをサポート
CTA | 「CTA[(行動喚起)」を](#ctas)参照してください。
{: .reset-td-br-1 .reset-td-br-2}

#### 行動喚起 {#ctas}

WhatsApp メッセージに次の行動喚起を追加できます。

CTAタイプ | 詳細
----------- |----------------
ウェブサイトにアクセス | メッセージ テンプレートのみで利用可能です。<br>ボタンは最大 1 つ (可変パラメータを含む)。
電話番号に電話する | メッセージ テンプレートでのみ使用できます。<br>ボタンは最大 1 つ。
カスタム クイック返信ボタン | 最大 3 つのボタン。
マーケティング オプトアウト ボタン | このオプションでは、サブスクリプション ステータスは自動的に更新されません。<br><br>セットアップ手順については、[「オプトインとオプトアウト」]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection)を参照してください。
{: .reset-td-br-1 .reset-td-br-2}

### 受信メッセージ

ユーザーは WhatsApp メッセージで次の内容を送信できます。

メッセージ機能 | 詳細
----------- |----------------
テキスト |
画像（JPEG および PNG）| 8 ビット、RGB または RGBA で、どのタイプでも最大 5 MB である必要があります。
オーディオ| audio/aac<br>オーディオ/mp4<br>オーディオ/mpeg<br>オーディオ/AMR<br>オーディオ/ogg (only Opus Codecs, base audio/ogg is not supported)
ドキュメント | テキスト/プレーン<br>アプリケーション/pdf<br>アプリケーション/vnd.ms-powerpoint<br>アプリケーション/msword<br>アプリケーション/vnd.ms-excel<br>アプリケーション/vnd.openxmlformats-officedocument.wordprocessingml.document<br>アプリケーション/vnd.openxmlformats-officedocument.presentationml.presentation<br>アプリケーション/vnd.openxmlformats-officedocument.spreadsheetml.sheet
CTA | 「CTA[(行動喚起)」を](#ctas)参照してください。
ビデオ | ビデオ/mp4, video/3gp<br><br>H.264 ビデオ コーデックと AAC オーディオ コーデックのみがサポートされます。単一のオーディオ ストリームまたはオーディオ ストリームのないビデオをサポートします。
{: .reset-td-br-1 .reset-td-br-2}



[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
