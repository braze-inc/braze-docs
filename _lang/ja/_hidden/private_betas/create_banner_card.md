---
nav_title: バナーカードの作成
article_title: バナーカードの作成
permalink: "/create_banner_card/"
description: "この参照記事では、ブレーズキャンペーンを使用してバナーカードを作成および送信する方法について説明します。"
page_type: reference
---

# バナーカードの作成

> この記事では、キャンペーンの作成時にBraze でバナーカードを作成する方法について説明します。

[Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)と同様に、バナーカードはあなたのアプリやウェブサイトに直接埋め込まれており、自然な感じの体験でユーザーを巻き込むことができます。これらは、他のチャネル(電子メールやプッシュ通知など)の到達範囲を拡張しながら、すべてのユーザにパーソナライズされたメッセージングを作成するための迅速かつシームレスなソリューションです。 

バナーカードは以下の用途に最適です。

- 特集コンテンツの強調表示
- 今後のイベントに関するユーザーへの通知
- ロイヤルティプログラムの最新情報の共有

Banner Cardは、ユーザーが新しいセッションを開始するたびにカスタマイズされ、期限切れにならないように設定できるため、エンゲージメント戦略に追加するのに役立つツールです。

{% alert important %}
Banner Cardは現在初期アクセス中です。早期アクセスに参加することに興味がある場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

## 前提条件:配置の決定

バナーカードを作成する前に、バナーカードを表示するアプリ内の領域を指定する必要があります。これは配置とも呼ばれます。配置を作成した後、バナーカードキャンペーンを作成するときに選択できます。配置済みの場合は、[step 1](#step-1-create-your-campaign) にスキップします。

配置を作成するには:

1. **Settings**> **Banner Card Placements**に移動します。
2. バナーカードの場所に名前を付けます。
3. (オプション) このバナーカードを配置する場所を説明する説明を追加します。
4. 一意の配置ID を入力します。開発者チームと協力してこのID を定義します。統合中に使用する必要があるためです。起動後に配置ID を編集することは避けてください。これにより、アプリやウェブサイトとの統合が損なわれる可能性があります。
5. [**保存**] を選択します。

各配置は、最大10のキャンペーンで使用できます。 

{% alert important %}
配置ID は、ワークスペースごとに一意です。
{% endalert %}

## ステップ 1: キャンペーンを作成

バナーカードの配置を決定したら、キャンペーンを構築する時間になります。

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。
2. **バナーカード**を選択します。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じてチームとタグを追加します。タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。たとえば、レポートビルダを使用する場合、関連するタグでフィルタリングできます。
5. キャンペーンに関連付ける[配置](#prerequisite-determine-placement)を選択します。ここでは、バナーカードがアプリまたはサイトに表示されます。
6. キャンペーンに必要な数のバリアントを追加し、名前を付けます。追加したバリアントごとに異なるメッセージタイプとレイアウトを選択できます。バリアントの詳細については、[多変量およびA/B 検定]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)を参照してください。

## ステップ2:バナーカードを作成する

メッセージの内容の詳細を編集するには:

1. **Edit message**を選択します。作曲者が開きます。
2. メッセージに合った行スタイルを選択します。行をキャンバス領域にドラッグアンドドロップします。
3. ブロックを行にドラッグアンドドロップして、メッセージを作成します。
4. メッセージの[style](#styles)を定義します。

### スタイル

**Style**を選択して、メッセージ内のすべてのブロックに適用する設定を調整します。

![Banner Card composer.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})のスタイルパネル

ここでは、バックグラウンドプロパティ、ボーダー設定、デフォルトのバナーカードなどのカスタムスタイルを指定できます。ここで適用されるスタイルは、特定のブロックまたは行に対してオーバーライドできます。スタイルを上書きするには、特定のブロックまたは行を選択してそのプロパティを表示し、変更を加えます。

### オン・クリック動作

顧客がバナーカードのリンクをクリックすると、アプリの奥深くに移動するか、別のWeb ページにリダイレクトできます。

カスタム属性またはカスタムイベントをログに記録することもできます。これにより、バナーカードをクリックすると、カスタマーのプロファイルがカスタムデータで更新されます。

## ステップ 3:キャンペーンの残りの部分をビルドする

次に、キャンペーンの残りの部分を作成します。Banner Card を構築するためのツールの最適な使用方法については、次のセクションを参照してください。

### キャンペーン期間を選択する

バナーカードキャンペーンの開始日時を選択します。 

デフォルトでは、バナーカードは無期限に存続します。必要に応じて、**End Time**を選択して終了日時を指定します。

### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルタを選択して対象ユーザーを絞り込みます。現在のおおよそのセグメント集団のスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

### コンバージョンイベントを選択する

Braze を使用すると、キャンペーンを受信した後、ユーザが特定のアクションおよび変換イベントを実行する頻度を追跡できます。ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを許可することができる。

## ステップ4:テストとデプロイ

キャンペーンを構築したら、テストして確認し、キャンペーンが期待どおりに機能することを確認します。それでは、バナーカードキャンペーンを開始する準備ができました！

## 知っておくべきこと

### バナーカードの有効期限

デフォルトでは、バナーカードには有効期限はありませんが、オプションの終了日を追加できます。

### 配置管理

配置はワークスペースごとに一意であり、各配置は最大10 のキャンペーンで使用できます。

配置ID はワークスペースに一意である必要があり、起動後は編集しないでください。開発者チームと協力してこのID を定義します。統合中に使用する必要があるためです。 

### 分析

次の表は、主要なバナーカードのメトリクスを定義しています。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href='https://braze.com/docs/user_guide/data_and_analytics/report_metrics#total-impressions'>インプレッション数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-impressions'>ユニークインプレッション数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#total-clicks'>クリック数の合計</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-clicks'>ユニーククリック数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event'>1 次コンバージョン数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}<ul><li>{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</li><li>{% multi_lang_include metrics.md metric='Conversion Rate' %}</li></ul></td>
        </tr>
    </tbody>
</table>

メトリック、定義、および計算の完全なリストについては、[レポートメトリック用語集]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)を参照してください。