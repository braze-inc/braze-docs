---
nav_title: メールのボットフィルタリング
article_title: メールのボットフィルタリング
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "この記事では、メールのボットフィルタリングの概要について説明します。"
---

# メールのボットフィルタリング

> [[メール設定]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings)] でボットフィルタリングを設定して、すべての疑わしいマシンまたはボットクリックを除外します。メールの「ボットクリック」とは、自動プログラムにより生成されたメール内のハイパーリンのクリックを指します。これらのボットクリックをフィルタリングすることで、メッセージを意図的にトリガーし、参加している受信者に配信できます。

{% alert important %}
2025年7 月9 日以降、作成されたすべての新しいワークスペースでボットフィルタリング設定がオンになり、Braze でのクリックレポートがより正確になります。
{% endalert %}

## ボットクリックについて

Braze には、疑わしいボットクリック (人間以外とのインタラクション (NHI) とも呼ばれます) を特定するために複数の入力を使用する検出システムがあります。ボットクリックは、クリック率を人為的に増大させて、メールエンゲージメントの指標を歪める可能性があります。このアプローチでは、クリックエンゲージメント指標とインサイトの完全性を確保するために、真の人間とのインタラクションと疑わしいボットアクティビティを区別できるようになります。

## ボットクリックの影響を受ける指標

{% alert note %}
自動クリックの疑いがある場合は、ボットフィルターがアクティブにブロックし、エンゲージメントメトリクスの精度を向上させます。しかし、スキャナやボットは時とともに進化し続けるので、Brazeは人間以外のすべてのアクションを取り除くことを保障することはできません。
{% endalert %}

以下の Braze 指標は、ボットクリックの影響を受ける可能性があります。

- 総クリック率
- ユニーククリック率
- クリック開封率
- コンバージョンレート (コンバージョンイベントとして「クリックキャンペーン」が選択されている場合)
- ヒートマップ
- 一部のセグメントフィルタ

[ Braze Intelligence の機能]({{site.baseurl}}/user_guide/brazeai/intelligence) は、検出システムの上にあるクリックデータを活用するため、影響を受ける場合があります。この設定をオンにすると、検出システムが一時的に中断する可能性があります。その結果、疑わしいボットクリックが除外されることから、指標または入力が減少する可能性があります。

- インテリジェントセレクション
- インテリジェントチャネル
- インテリジェントタイミング
- 実験ステップ
    - 勝者パス
    - パーソナライズされたパス
- キャンペーン
    - 勝者バリアント
    - パーソナライズされたバリアント
- 推定実質開封率

疑わしいボットクリックからの購読解除は、影響を受けません。Braze は引き続き、すべての購読解除リクエストを通常どおり処理します。Braze でこれらの登録解除をブロックする場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal) を送信します。

## ボットフィルタリングの影響を受けるセグメンテーションフィルタ

以下の[セグメンテーションフィルタ]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) は、メールメッセージのボットフィルタリングの影響を受ける可能性があります。

- [クリック/開いたキャンペーンまたはタグ付きキャンバス]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [クリックされた/開封されたステップ]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-step)
- [キャンペーンでクリックしたエイリアス]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-campaign)
- [キャンバスステップでクリックしたエイリアス]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [キャンペーンステップまたはキャンバスステップでクリックしたエイリアス]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [メッセージへの最終エンゲージ]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#last-engaged-with-message)
- [インテリジェントチャネル]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#intelligent-channel)

## ボットフィルタリングをオンにする

[**設定**] > [**メール設定**] に移動します。次に、[**ボットクリックを削除**] を選択します。この設定はワークスペースレベルで適用されます。

疑わしいボットクリックは、この設定をオンにした後でのみ削除され、ワークスペースの指標に遡及的に適用されることはありません。

![「メール」環境設定でボットフィルターの実行メール 設定が有効になっている。]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
この設定をオンにして、後でオフにすると、Braze は以前に削除したボットアクティビティをアナリティクスに復元できません。
{% endalert %}

## Currents と Snowflake のメールクリックイベントのフィールド

Braze は、Currents および Snowflake のメールクリックイベントのフィールド `is_suspected_bot_click` と `suspected_bot_click_reason` を送信します。

| フィールド| データ型| 説明|
| `is_suspected_bot_click` | ブール値 | これが疑わしいボットクリックであることを示します。これは、[**ボットクリックを削除**] ワークスペース設定をオンにするまで、NULL 値として送信されます。この方法を使用すると、ワークスペースでボットクリックが疑われるフィルタリングがいつ開始されたかをプログラムで理解できるため、Currents およびSnowflake のデータと正確に比較できます。|
| `suspected_bot_click_reason` | Array | これがボットクリックの疑いがある理由を示します。これにより、ボットフィルタリングのワークスペース設定が無効になっている場合でも、`user_agent` や`ip_address` などの値が入力されます。このフィールドでは、疑わしいボットクリックから得られるクリック数を、人間のインタラクションと比較することで、この設定をオンにした場合の潜在的な影響に関するインサイトを得ることができます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## よくある質問

### ボットフィルタリングは、キャンペーンのパフォーマンスにどのように影響しますか?

すでに送信された以前のキャンペーンの指標には影響しません。ワークスペースでボットフィルタリングをオンにすると、Braze はすべてのクリックから疑わしいボットクリックをフィルタリングで除外します。クリック率が低下することがありますが、クリック率は、メールでのユーザーのエンゲージメントをより正確に表しています。

### ボットをフィルタリングすることで、ボットが Braze 購読解除リンクをクリックしても購読解除できなくなりますか?

いいえ。引き続きすべての購読解除リクエストが処理されます。

### ボットクリックフィルタリングでマシンのオープンを考慮していますか?

いいえ。
