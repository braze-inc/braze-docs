---
nav_title: レポートビルダー (レガシー)
article_title: レポートビルダー (レガシー)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "このページでは、従来のレポートビルダを使用してレポートを実行する方法について説明します。これには、キャンペーンとキャンバスによる比較レポートの作成、レポートとグラフの作成などが含まれます。"
tool: 
  - Reports

---

# レポートビルダー (レガシー)

> レポートビルダーを使用すると、複数のキャンペーンまたはキャンバスの結果を 1 つのビューで比較できるため、主要な指標に最も影響を与えたエンゲージメント戦略を簡単に判断できます。キャンペーンとキャンバスの両方で、データをエクスポートしてレポートを保存し、将来閲覧することができる。<br><br>レポートに表示されるメトリックの説明リストについては、[レポートメトリック用語集][16]を参照してください。

![キャンペーン比較例][5]{: style="max-width:80%;"}

このレポートを使用して、主要なエンゲージメントに関する質問の答えを求めます。以下に例を示します。

- 特定のタグやチャネルについて、パフォーマンスが最も高かったキャンペーンまたはキャンバスはどれですか?
- マルチバリアントキャンペーンで、コントロールから上昇が最大だったバリアントはどれですか?  
- 夏のセール、秋のセール、または冬のセールの季節のプロモーションキャンペーンで、購入率が最も高かったものはどれですか?
- このキャンバス内で開封率が最も高かったプッシュ通知はどれですか?
- このキャンバスグループで、コンバージョンが最大のステップはどれですか?
- ウェルカムメールのバージョン 1 やウェルカムメールのバージョン 2 は、エンゲージメントとコンバージョンの向上に結び付きましたか? 変更は良好に機能しましたか?
- 異なる配信方法 (例えば、スケジュールされたプッシュ 3 つ、アクションベースのプッシュ 3つ、 API トリガープッシュ 3 つ) は、開封率、コンバージョン率、または購入率にどのように影響を与えますか?
- 離脱ユーザーへのメッセージに関する継続的な改善は、時間の経過とともに KPIs に良い影響を与えましたか?

{% alert tip %}
コンバージョンA、コンバージョンBなど、比較したいキャンペーンやキャンバス間で同じコンバージョンイベントを使用し、レポートビルダーのレポートでこれらのコンバージョンを並べることができるようにしよう。
{% endalert %}

## レポートを実行する

### ステップ1:新規レポートの作成

ダッシュボード内で、[**分析]** > [**レポートビルダー**] に移動します。

[**新しいレポートを作成**] を選択して、キャンペーン比較レポートまたはキャンバス比較レポートのいずれかを選択します。

キャンペーンに関するレポートを実行する場合は、**手動**レポートまたは**自動**レポートを選択できます。レポートには、キャンペーンまたはキャンバスのいずれかを含めることができますが、両方を含めることはできません。過去12 か月以内に最後にメッセージを送信したキャンペーンおよびキャンバスは、レポートの対象となります。

![キャンペーン・ダッシュボード][6]{: style="max-width:80%;"}

この 2 つのオプションの違いを以下に示します。

| **アクション (Action)** | **マニュアル** | **自動** |
| ---- | ---------- | ------------- |
| **レポートを作成** | フィルターを使用してキャンペーンリストを絞り込み、特定のキャンペーンを除外できます。 | フィルターオプションを使ってキャンペーンリストを絞り込み、レポートを作成する。 |
| **レポートの保存と表示** | レポートを保存できます。これらのキャンペーンはまだ「最後に送信されたもの」フィルターに該当するため、次に表示するときは、以前に追加したのと同じキャンペーンを表示することができる。 | レポートを保存できます。次回の閲覧時には、レポートが自動的に更新され、現在フィルターに一致するすべてのキャンペーンが含まれるようになる。 |
| **レポートの編集** | **レポートの編集**を選択すると、レポートからキャンペーンを追加または削除できます。 | フィルター基準を調整することで、レポートを編集することができる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
**手動**レポートと**自動**レポートの両方で、レポートに最大 250 件のキャンペーンを含めることができます。
{% endalert %}

キャンバスレポートは手動のキャンペーンレポートと同様に機能し、キャンバスの選択とレポートの更新も手動で行う必要があります。1 つのレポートに最大 5 つのキャンバスを含めることができます。

### ステップ2:指標の選択

レポートを作成すると、各行にキャンペーンを含む空白の表が表示される。[**列を編集**] を選択し、追加する指標を選択すると、テーブルにデータが読み込まれます。

![キャンペーンのオプション][15]{: style="max-width:80%;"}

選択した指標がテーブルに読み込まれます。指標の定義については、「[レポート指標の用語集][16]」を参照してください。一部の指標は、キャンペーン比較レポートでのみ使用できます。

また、任意の比率指標または数値指標の**平均**と、任意の数値指標の**合計**の計算を切り替えることもできます。

### ステップ 3:期間の選択

特定の期間を選択して、レポートのデータを表示できます。特定のキャンペーン、キャンバス、キャンバスバリアント、またはキャンバスコンポーネントに選択した期間のデータがない場合、その行の結果は空白になる。 

![キャンペーンの数値指標][4]{: style="max-width:60%;"}

### ステップ 4:レポートに名前を付けて保存

レポートを保存する前に、レポートに名前を付けます。レポートに名前を付けずに保存すると、Braze によりデフォルトの名前である「キャンペーン比較レポート」が適用されます。

![キャンペーンノート][7]{: style="max-width:60%;"}

準備ができたら、[**保存**] を選択します。保存されたレポートは、後で [**レポートビルダー**] ページに表示できます。

## 多変量キャンペーンとのキャンペーン比較レポート

多変量キャンペーンの場合、キャンペーン名の横にある矢印をクリックして、指標をバリアント別、およびコントロールグループ別に表示できます。バリアントを含む行にはそのバリアントのパフォーマンス結果が含まれ、コントロールを含む行にはコンバージョンイベントの結果のみが含まれます。 

![キャンペーンノート][3]{: style="float:right;max-width:15%;margin-left:15px;"}

キャンペーン全体の行に入力されるメトリクスは、そのバリアントのパフォーマンスを反映するが、コントロールのパフォーマンスは含まれない。例えば、キャンペーン全体の1次コンバージョンイベント A は、バリアントの1次コンバージョンイベント A の合計になり、コントロールの1次コンバージョンイベント A は含まれません。

{% alert important %}
マルチバリアントキャンペーンからバリアントを削除すると、そのバリアントのデータは今後のレポートで使用できなくなります。
{% endalert %}

## キャンバス比較レポートの内訳

キャンバスレポートでは、キャンバスをバリアント別、ステップ別、メッセージ別に表示できます。

### バリアント

**バリアント別の内訳を**選択すると、キャンバス全体のハイレベルな統計と、キャンバス名の横にある矢印を選択すると拡大できるバリアントごとの統計を見ることができる。

![バリアント][12]{: style="max-width:90%;"}

### ステップ 

**ステップごとの内訳を**選択すると、レポートの各行がステップの行を含む、ステップ・レベルのメトリクスを表示できる。

![ステップ][13]{: style="max-width:90%;"}

### メッセージ

ステップレベルの内訳と同様に、[**メッセージごとの内訳**] を選択すると各行にステップ名が表示されます。ただし、[**列を編集**] では、メールクリック数やプッシュ通知の開封数など、チャネル固有の統計情報のようなメッセージレベルの指標にアクセスできます。

![レポート][14]{: style="max-width:90%;"}

なお、Braze ダッシュボードでは、キャンバスレポートの最初の 50 行をプレビューできます。CSV をエクスポートすると、レポート全体にアクセスできます。

## 保存したレポートへのアクセス

保存した**手動レポート**にアクセスすると、前回追加したものと同じキャンペーンを表示できます。それらのキャンペーンがまだ「最終送信」フィルターに該当するためです。

保存した**自動レポート**にアクセスすると、レポートが自動的に更新され、現在フィルターに一致するすべてのキャンペーンが含まれます。例えば、レポートで「プロモーション」タグを指定したフィルターをキャンペーンに適用した場合、このレポートを表示するたびに、「プロモーション」タグの付いたすべてのキャンペーンを表示できます。これには、このレポートの作成後に作成されたキャンペーンも含まれます。

## レポートの編集

**マニュアル・レポートでは**、「**編集**」を選択してレポートを編集することができる。それから、レポートに含めるキャンペーンの選択または選択解除ができます。

**自動レポート**では、フィルターを切り替えるだけで、レポートの結果を絞り込むことができます。

## レポートのエクスポート

また、**エクスポートを**選択してレポートをCSVでダウンロードすることもできる。

レポートにマルチバリアントキャンペーンが含まれている場合、エクスポートには次の 2 つのCSVファイルが含まれます。 

- 各キャンペーンのトップレベルの指標のみを含むファイル
- バリアントレベルの指標を含むファイル

バリアントの指標を含むファイルでは、その名前の先頭に `variant_` が付け加えられます。自動レポートを初めてエクスポートするときに、複数ファイルのダウンロードの許可を求めるポップアップが表示されます。[**許可**] をクリックします。

![キャンペーンダウンロード][8]{: style="max-width:60%;"}

### キャンバス比較レポートのエクスポート

CSVエクスポートには、**エクスポートを**選択したときに表示されていた内訳ビューが反映される。例えば、ステップレベルのブレイクダウン・ビューを表示していた場合、エクスポートにはステップのメトリクスのデータが含まれる。別の内訳のデータをエクスポートするには、まずその内訳に移動してから、[**エクスポート**] を選択する必要があります。

バリアントの内訳を持つキャンバスレポートをダウンロードすると、次の 2 つの CSV ファイルを受信します。

- 各キャンバスのトップレベルの指標のみを含むファイル
- バリアントレベルの指標を含むファイル

## チャートの作成 

レポートで選択した指標を可視化するには、チャートを使用します。チャートは、キャンペーンに関するレポートで、その列に少なくとも 1 つの指標が追加されている場合に使用できます。

![[送信済みメッセージ] 指標が選択されたキャンペーンパフォーマンスのチャート][17]

デフォルトでは、各レポートのチャートに、レポートの最初の列の指標が表示されます。チャートに表示する別の指標を選択するには、ドロップダウンから指標を選択します。レポートのテーブルにある任意の指標をチャートに表示できます。

最大 3 つの指標をチャートに表示できます。すべての指標の単位は同じでなければなりません。例えば、最初のドロップダウンで比率を選択すると、2 番目のドロップダウンでは比率のみが選択可能になります。

チャートに 1 つの指標のみが含まれている場合、選択した指標に基づいて降順で最大 30 件のキャンペーンが表示されます。例えば、チャートの指標がメールクリック数の場合、チャートにはクリック数の多いメールキャンペーン 30 件がクリック数の多い順に表示されます。レポートに 30 件を超えるキャンペーンが含まれている場合、上位 30 件のみがチャートに表示されます。複数の指標を選択した場合、最初に選択した指標に基づいて上位 5 件のキャンペーンのみがチャートに表示されます。

現在、レポートの保存時にチャートは保存されません。


[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
[4]: {% image_buster /assets/img/campaign_comparison/metric.png %}
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %}
[6]: {% image_buster /assets/img/campaign_comparison/create_report.png %}
[7]: {% image_buster /assets/img/campaign_comparison/comparison_name.png %}
[8]: {% image_buster /assets/img/campaign_comparison/download.png %}
[12]: {% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}
[13]: {% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}
[14]: {% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}
[15]: {% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}
[17]: {% image_buster /assets/img/campaign_comparison/report_builder_charts.png %}

[16]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
