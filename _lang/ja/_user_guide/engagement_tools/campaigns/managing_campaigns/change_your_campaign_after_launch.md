---
nav_title: 開始後のキャンペーンの編集
article_title: 開始後のキャンペーンの編集
page_order: 1
tool: Campaigns
page_type: reference
description: "この記事では、キャンペーン開始後に特定の要素を編集した場合の結果について概要を説明します。"

---

# 開始後のキャンペーンの編集

> この記事では、キャンペーン開始後に特定の要素を編集した場合の結果について概要を説明します。

## キャンペーンの停止

キャンペーンを停止するには、**Campaign Details**ページを開き、**Stop Campaign**を選択します。キャンペーンが停止されると、

- 送信予定のメールは破棄されます。
- イニシャルテストがすでに送信されているA/Bテストは永久にキャンセルされます。
- すでに送信されているメッセージのイベント(クリックを開くなど)は引き続き追跡されます。

キャンペーンを再開するには、**Resume** を選択します。キャンペーンでは、メッセージとA/Bテストの送信が続行されますが、失われたメッセージは再送信または再スケジュールされません。

## トリガーキャンペーン

アクションベースの配信キャンペーンおよびAPI トリガ配信キャンペーンに対するすべての変更は、go-forward 送信に対してただちに有効になります。 

これらのキャンペーンがトリガされたが、まだ送信されていない場合(たとえば、1 日間の遅延があるアクションベースの配信キャンペーンが1 日間の遅延期間中に編集された場合)、スケジュールされたキャンペーンについては、次のガイダンスを参照してください。

### スケジュールされたキャンペーン

キャンペーンの開始後に変更を加える必要がある場合は、キャンペーンを編集する際に以下の項目に注意して、変更が意図したとおりの効果をもたらすことを確認してください。

### メッセージの内容

メッセージコンテンツの変更(タイトル、本文、および画像を含む)は、今後すべてのメッセージ送信の保存時にすぐに有効になります。すでにディスパッチされているメッセージの内容を変更することはできません。

### スケジュールとオーディエンス

キャンペーンの送信予定時間やオーディエンスを編集した場合、それらの変更は実際のキャンペーンにすぐに反映されます。

### 送信レート

送信レート制限を使用する場合、Braze はメッセージを分単位のタイムスロットで「スケジュール」するため、メッセージの送信レートを変更する場合、即時変更するには以下のプロセスに従ってください。

## 変更を即有効にする

変更をすぐに有効にする必要がある場合は、次の手順を実行します。

1. 影響を受けるキャンペーンを停止します。
2. キャンペーンを複製します。
3. 複製のキャンペーンを編集します。

{% alert important %}
これにより、元のキャンペーンをすでに受け取っているユーザーの適格性がリセットされるため、必要に応じて元のキャンペーンを受け取っていないユーザーのために複製キャンペーンをフィルタリングしてください。
{% endalert %}

## アクティブキャンペーンのドラフトの保存 {#campaign-drafts}

草稿は、積極的なキャンペーンに大規模な変更を加えるのに適しています。ドラフトを作成することで、次回の起動前に計画された変更をパイロットすることができます。

{% alert note %}
キャンペーンに含められる下書きは、一度に1つまでです。また、ドラフトされた変更がまだ起動されていないため、アナリティックは使用できません。
{% endalert %}

ドラフトを作成するには、以下のようにする：

1. アクティブなキャンペーンにアクセスする。
2. 変更を加える。
3. **下書き保存**を選択します。ドラフトを作成した後、ドラフトを起動または破棄するまで、アクティブなキャンペーンを編集できないことに注意してください。

![アクティブなキャンペーンを表示するオプションを持つアクティブなキャンペーンのドラフト。]({% image_buster /assets/img/campaign_draft.png %})

ドラフトを編集するときに、キャンペーンドラフトのヘッダーまたはキャンペーンアナリティクスのフッターでアクティブなキャンペーンを参照することもできます。 

アクティブなキャンペーンに戻るには、分析ビューまたはアクティブなキャンペーンビューから [**下書きを編集**] を選択します。

### アプリ内メッセージの優先順位付け

アプリ内メッセージの優先度は、[**厳密な優先度を設定**] を選択し、他のキャンペーンやキャンバスとの関連で優先度を指定すると、(下書きが開始される前に) 即座に更新されます。
