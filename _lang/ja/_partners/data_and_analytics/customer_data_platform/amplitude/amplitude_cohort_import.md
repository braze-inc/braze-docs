---
nav_title: Amplitude
article_title: Amplitude コホートインポート
description: "このリファレンス記事では、Amplitude のコホートインポート機能について説明します。Amplitude は、プロダクト分析およびビジネスインテリジェンスのプラットフォームです。"
page_type: partner
search_tag: Partner
---

# Amplitude コホートインポート

> ここでは、[Amplitude](https://amplitude.com/)からBrazeへのユーザー コホートの読み込み方法について説明します。Amplitudeと他の機能の統合の詳細については、主な[Amplitudeの記事]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/)を参照してください。

## データインポート統合

設定するすべての統合は、アカウントのデータポイントボリュームの対象となります。

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Amplitude** を選択します。ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。 

生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとREST エンドポイントは、Amplitude のダッシュボードでポストバックアップを設定するときに次回のステップで使用されます。<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### ステップ 2:Amplitude でのBrazeインテグレーションの設定

Amplitudeで、**Sources & Destinations**> **[プロジェクト名]**> **Destinations**> **Braze** に移動します。表示されるプロンプトで Braze データインポートキーと REST エンドポイントを指定し、[**Save**] をクリックします。

![]({% image_buster /assets/img/amplitude.png %})

### ステップ 3:Amplitude コホートをBrazeにエクスポートする

まず、Amplitude から Braze にユーザーをエクスポートするため、エクスポートするユーザーの[コホート](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts)を作成します。Amplitude は、以下の識別子を使用してコホートを Braze に同期できます。
- ユーザー別名
- デバイス ID
- ユーザーID(外部ID)

Amplitude は、多数の識別子 m アプリ ing プロパティーを優先順位でサポートします。プライマリ、セカンダリ、およびターシャリ識別子m アプリ ing を設定できます。同期中に、ユーザーにプライマリがない場合、Amplitude は次に使用可能なものを使用します。これにより、同期c 超過料金が向上し、ドロップされたユーザーが削減され、同期に匿名および部分的に識別されたユーザーが追加されます。 

コホートを作成したら、**Sync to...**を押して、これらのユーザーsをBrazeにエクスポートします。

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

#### 同期ケイデンスの定義

コホート同期は、1回限りの同期、毎日または毎時間のスケジュールされた同期、1分ごとに更新されるリアルタイム同期として設定できます。 

設定したインテグレーションは、データポイントs を記録します。Braze データポイントsのニュアンスについて疑問があれば、Braze アカウントマネージャーが答えることができます。

### ステップ 4: Braze でユーザーをセグメント化する

Braze でこれらのユーザーのセグメントを作成するには、[**エンゲージメント**] の下の [**セグメント**] に移動し、セグメントに名前を付け、フィルターとして [**Amplitude コホート**] を選択します。次に、"includes"オプションを使用し、Amplitude で作成したコホートを選択します。 

![Braze Segment ビルダでは、フィルター"amplitude_cohorts" は"includes_value" および" Amplitude コホート test" に設定されます。]({% image_buster /assets/img/amplitude2.png %})

保存後、キャンバスまたはキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照できる。

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。
