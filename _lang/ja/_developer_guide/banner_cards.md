---
page_order: 2.2
nav_title: バナーカード
article_title: バナーカード
description: "このランディングページには、バナーカードの作成方法やユースケースに関する記事など、すべてのバナーカードのホームページがあります。"
channel:
- Banners
---

# バナーカード

> バナーカードを使用すると、メールやプッシュ通知など、他のチャネルの到達範囲を拡張しながら、すべてのユーザにカスタマイズされたメッセージを作成できます。[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about)と同様に、ナチュラルな感じの体験を通してユーザーと関わり合いを持たせるようなカードを、あなたのアプリやウェブサイトに直接埋め込むことができます。

{% alert important %}
バナーカードは現在、早期アクセス段階です。早期アクセスに参加することに興味がある場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

## ユースケース

ユーザが新しいセッションを開始するたびに、バナーカードが期限切れになることはなく、自動パーソナライズされるため、次の目的に適しています。

- 特集コンテンツの強調表示
- 今後のイベントに関するユーザーへの通知
- ロイヤルティプログラムの更新の共有

## バナーカードについて

### カードの有効期限

デフォルトでは、バナーカードは期限切れになりませんが、必要に応じて終了日を選択できます。

### 配置 ID {#placement-ids}

バナーカードの配置は各ワークスペースに固有であり、1 つのワークスペース内の10 のキャンペーンで使用できます。さらに、各ワークスペース内の配置には一意のID を割り当てる必要があります。配置を作成し、[バナーカードキャンペーン]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) または[バナーカードをアプリ]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/) に埋め込むと、それらのID を割り当てます。

{% alert important %}
バナーカードキャンペーンの起動後に配置ID を変更しないでください。
{% endalert %}

### カード優先 {#card-priority}

複数のキャンペーンが同じ配置ID を参照している場合、カードは優先順位の高い順に表示されます。デフォルトでは、新しく作成されたバナーカードは中に設定されますが、[手動で優先度]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority)を高、中、低に設定できます。複数のカードが同じ優先度を共有している場合は、新しいカードが先頭に表示されます。

### 指標

これらは、最も重要なバナーカードメトリクスです。メトリック、定義、および計算の完全なリストについては、[レポートメトリック用語集]({{site.baseurl}}/user_guide/data/report_metrics/)を参照してください。

| 指標 | 定義 |
| --- | --- |
| [インプレッション数の合計]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | メッセージがロードされ、ユーザの画面に表示される回数(ユーザがメッセージを2 回表示された場合など、以前の操作に関係なく2 回カウントされます)。 |
| [ユニークインプレッション数]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | 1 日に特定のメッセージを受信し、閲覧したユーザーの総数。各ユーザーは1 回のみカウントされます。 |
| [クリック数の合計]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | 同じユーザが複数回クリックしたかどうかに関係なく、配信されたメッセージ内でクリックしたユーザの総数(およびパーセンテージ)。 |
| [ユニーククリック数]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | メッセージ内を少なくとも 1 回クリックし、[`dispatch_id` で測定された受信者の明確な数]({{site.baseurl}}/help/help_articles/data/dispatch_id/)。各ユーザーは1 回のみカウントされます。 |
| [1 次コンバージョン数]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | Braze キャンペーンから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数。この定義されたイベントは、キャンペーンを作成するときにあなたが決定します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 次のステップ

これで、バナーカードについて知ったので、次の手順を実行する準備が整いました。

- [バナーカードキャンペーンの作成]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [バナーカードをアプリに埋め込む]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
