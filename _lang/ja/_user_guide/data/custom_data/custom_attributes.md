---
nav_title: カスタム属性
article_title: カスタム属性
page_order: 10
page_type: reference
description: "このページでは、カスタム属性について説明し、さまざまなカスタム属性データ型について説明します。"
search_rank: 1
---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタム属性

> このページでは、ユーザの一意の特性のコレクションであるカスタム属性について説明します。カスタム属性は、ユーザーに関する属性や、アプリケーション内の価値の低いアクションに関する情報を格納するために最適です。 

Braze に保存すると、カスタム属性を使用してオーディエンスセグメントを構築し、Liquid を使用してメッセージングをパーソナライズできます。カスタムイベントとは異なり、カスタム属性の時系列情報は保存されないので、時系列情報に基づくグラフを取得できないことに注意してください。

## カスタム属性の管理

ダッシュボードでカスタム属性の作成および管理を行うには、[**データ設定**] > [**カスタム属性**] に移動します。 

![4 つのカスタム属性 (ブール値)。]({% image_buster /assets/img/export_custom_attributes.png %})

「**最終更新日**」の列には、カスタム属性が最後に編集された時間（ブロックリストやアクティブに設定された時間など）が表示される。

{% alert important %}
メッセージのターゲットを正しく設定するには、カスタム属性のデータ型が実際のカスタム属性と一致していることを確認します。
{% endalert %}

このページから、既存のカスタム属性の表示、管理、作成、または禁止リストへの追加ができます。カスタム属性の横にあるメニューから、以下のアクションを選択します。

### ブロックリスト

カスタム属性は、アクションメニューに個別にブロックリストすることも、最大100 個の属性を選択して一括でブロックリストすることもできます。カスタム属性をブロックすると、その属性に関するデータは収集されず、既存のデータは再アクティブ化しない限り利用できなくなります。また、禁止リストに追加された属性はフィルターやグラフに表示されません。さらに、この属性が現在、Brazeダッシュボードの他の領域のフィルタまたはトリガによって参照されている場合、その属性を参照するフィルタまたはトリガのすべてのインスタンスが削除され、アーカイブされることを示す警告モードが表示されます。

### 個人識別情報(PII)としてのマーキング

管理者は、カスタム属性を作成し、このページからPII としてマークすることもできます。これらの属性は、「PII としてマークされたカスタム属性の表示」権限を持つ管理者とダッシュボードユーザーにのみ表示されます。

### 説明を加える

`Manage Events, Attributes, Purchases` [ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合、カスタム属性の作成後に説明を追加できます。カスタム属性を編集し、チームへのメモなど好きなものを入力する。

### タグを追加する

「イベント、属性、購入を管理する」[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合、カスタム属性の作成後にタグを追加できます。その後、タグを使用して、属性のリストをフィルター処理できます。 

### カスタム属性を削除する

ユーザープロファイルからカスタム属性を削除する方法には、次の 2 つがあります。

* [ユーザー更新ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes)で、削除するカスタム属性名を選択する。
* API リクエスト内で `null` 値を[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)に設定する。

### 利用レポートを見る

使用状況レポートは、特定のカスタム属性を使用しているすべてのキャンバス、キャンペーン、およびセグメントを一覧表示する。このリストには、Liquid の使用状況は含まれていません。 

各カスタム属性の横にあるチェックボックスを選択し、**使用状況レポートの表示**を選択すると、一度に最大100件の使用状況レポートを表示できます。

### データのエクスポート

カスタム属性のリストを CSV ファイルとしてエクスポートするには、ページ上部の [**すべてエクスポート**] を選択します。CSVファイルが生成され、ダウンロードリンクがEメールで送信される。

## カスタム属性の設定

さまざまなプラットフォームで、カスタム属性の設定に使用する方法を以下に示します。

{% details プラットフォーム別のドキュメントの拡張 %}

- [Android と FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## カスタム属性の保存

カスタム属性データを含めて、**ユーザープロファイル**に保存されているデータはすべて、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users)である限り、無期限に保持されます。

## カスタム属性のデータ型

カスタム属性は、優れたターゲット設定を可能にする非常に柔軟なツールです。

カスタム属性として格納できるデータ型を以下に示します。

- [ブール値](#booleans)
- [数値](#numbers)
- [文字列](#strings)
- [配列](#arrays)
- [時刻](#time)
- [オブジェクト]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [オブジェクトの配列]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### ブール値（真/偽）{#booleans}

ブール値を持つ属性は、サブスクリプションステータスなど、ユーザーに関する単純な 2 値データを格納する場合に便利です。その属性のレコードがまだ記録されていないユーザーに加えて、変数が明示的に true または false の値に設定されているユーザーを検出できます。

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| ブール値がtrue、false、trueまたは未設定、falseまたは未設定のいずれか**で**あるかをチェックする | **該当する**  | **TRUE**,**FALSE**,**TRUE OR NOT SET**, または**FALSE OR NOT SET** | このフィルターが`coffee_drinker` を指定した場合、ユーザーは以下の状況でこのフィルターにマッチする：<br> {::nomarkdown}<ul><li>このフィルターが <code>true</code> かつユーザーが次の値を持っている:  <code>coffee_drinker</code></li><li>このフィルターが <code>false</code> かつユーザーが次の値を持っていない:  <code>coffee_drinker</code></li><li>このフィルターが <code>true or not set</code> かつユーザーが次の値を持っている:  <code>coffee_drinker</code> または値なし</li><li>このフィルターが <code>false or not set</code> かつユーザーが次の値:  <code>coffee_drinker</code> またはいずれの値も持っていない</li></ul>{:/} |
| ユーザーのプロファイルにboolean値が**存在**し、かつnullでないことを確認する。 | **空白でない**  | **該当なし** | このフィルターが`coffee_drinker` を指定し、ユーザーが属性`coffee_drinker` の値を持つ場合、そのユーザーはこのフィルターにマッチする。 | 
| ユーザーのプロファイルにboolean値が**存在しないか**、NULLであるかをチェックする。 | **空白である**  | **該当なし** | このフィルターが`coffee_drinker`を指定し、ユーザーが属性`coffee_drinker` を持たないか、`coffee_drinker` の値がNULLの場合、そのユーザーはこのフィルターにマッチする。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 数値 {#numbers}

数値属性には[整数](https://en.wikipedia.org/wiki/Integer)や[浮動小数点](https://en.wikipedia.org/wiki/Floating-point_arithmetic)などがあり、さまざまなユースケースがあります。数値のカスタム属性を増分すると、特定のアクションやイベントが発生した回数を、データキャップにカウントせずに保存する場合に便利です。標準数には、以下の記録など、あらゆる用途があります。

- 靴のサイズ
- ウェストサイズ
- ユーザーが特定の製品機能またはカテゴリを表示した回数

{% alert tip %}
支出した金額はこの方法で記録すべきではありません。むしろ、[購入方法](#purchase-revenue-tracking)で記録すべきです。
{% endalert %}

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 数値属性が**正確に****数値**であるかどうかをチェックする| **完全一致** | **数値** | このフィルターが`10` を指定し、ユーザープロファイルが値`10` を持つ場合、そのユーザーはこのフィルターにマッチする。 |
| 数値属性が**数値と** **等しくないか**チェックする| **等しくない** | **数値** | このフィルターが`10` を指定し、ユーザープロファイルが値`10` を持たない場合、そのユーザーはこのフィルターにマッチする。 |
| 数値属性が**数値** **以上か**どうかをチェックする| **より大きい** | **数値** | このフィルターが`10` を指定し、ユーザープロファイルが`10` より大きい値を持つ場合、そのユーザーはこのフィルターにマッチする。 |
| 数値属性が**数値より** **小さいか**どうかをチェックする| **未満** | **数値** | このフィルターが`10` を指定し、ユーザープロファイルの値が`10` より小さい場合、そのユーザーはこのフィルターにマッチする。 |
| ユーザーのプロファイルにnumeric属性が**存在**し、nullでないことを確認する。 | **空白でない** | **該当なし** | ユーザー・プロファイルに指定された数値属性が含まれる場合、値に関係なく、そのユーザーはこのフィルタにマッチする。 |
| numeric属性がユーザーのプロファイルに**存在しないか**、NULLであるかをチェックする。 | **空白である** | **該当なし** | ユーザ・プロファイルに指定された数値属性が含まれていないか、属性の値がNULLの場合、そのユーザはこのフィルタにマッチする。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 数値属性の詳細

- 「正確に 0」と「未満」のフィルターは NULL フィールドを持つユーザーを含みます。
  - カスタム属性の値を持たないユーザーを除外するには、[**空白でない**] フィルターを含める必要があります。

### 文字列 (英数字) {#strings}

文字列属性は、お気に入りのブランド、電話番号、アプリケーション内での最後の検索文字列など、ユーザー入力の保存に役立ちます。文字列属性の長さは最大 255 文字です。

単語の間、前後、または後にスペースを含む値を入力すると、Braze はそのスペースもチェックすることに注意してください。

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 文字列属性が入力された文字**列と完全に一致**するかどうかをチェックする| **等しい** | **STRING**<br>大文字と小文字を区別する | このフィルターが`book` を指定し、ユーザープロファイルが`last_item_purchased` の文字列属性に`book` を含む場合、そのユーザーはこのフィルターにマッチする。 |
| 文字列属性が入力された文字列に**部分的にマッチ**するかどうかをチェックする**OR**正規表現 | **正規表現に一致する** | **文字列** **OR** **正規表現**<br>大文字と小文字は区別されない。 | 
| 文字列属性が入力された文字**列と部分的に一致しないか** **OR**正規表現でチェックする | **正規表現に一致しない** \* | **文字列** **OR** **正規表現**<br>大文字と小文字は区別されない。 |
| 文字列属性が入力された文字**列と一致しないか**チェックする| **等しくない** | **文字列**<br>大文字と小文字を区別しない  | このフィルターが`book` を指定し、ユーザープロファイルが`book` を含まない`last_item_purchased` の文字列属性を持つ場合、そのユーザーはこのフィルターにマッチする。|
| ユーザーのプロファイルにstring属性が**存在**し、かつ空文字列でないかチェックする。 | **空白でない** | **該当なし** | このフィルターが`favorite_genre` を指定し、ユーザープロファイルが属性`favorite_genre` を持つ場合、そのユーザーは属性値に関係なくこのフィルターにマッチする。例えば、ユーザーは `sci-fi`、`romance`、または他の値を持つことができます。|
| ユーザーのプロファイルに文字列属性が**存在しないか**チェックする | **空白** | **該当なし** | このフィルターが`favorite_genre` を指定し、ユーザープロファイルが属性`favorite_genre` を持たない場合、そのユーザーはこのフィルターにマッチする。|
| 入力された文字列の**いずれかと**完全に一致するかどうかをチェックする。 | **次のいずれかである** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`book` 、`bookmark` 、`reading light` を指定し、ユーザー・プロファイルがこれらの文字列の少なくとも1つを持つ場合、そのユーザーはこのフィルターにマッチする。 |
| 文字列属性が、入力された文字列の**いずれとも完全に一致しないか**どうかをチェックする | **次のいずれでもない** |**文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターに `book`、`bookmark`、および `reading light` が指定され、ユーザープロファイルにこれらの文字列がいずれも含まれていない場合、ユーザーはフィルターに一致する。|
| 文字列属性が、入力された文字列の**いずれかと部分的に一致**するかどうかをチェックする | **次のいずれかを含む** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`gold` を指定し、ユーザープロファイルが`gold_tier` や`former_gold_tier` などの文字列の中に`gold` を含む場合、そのユーザーはフィルターにマッチする。 |
| 文字列属性が、入力された文字列の**いずれとも部分的に一致しないか**どうかをチェックする | **次のいずれも含まない** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`gold` を指定し、ユーザープロファイルがどの文字列にも`gold` を含まない場合、そのユーザーはこのフィルターにマッチする。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
「12-1-2021」や「12/1/2021」などの日付文字列は、日時オブジェクトに変換され、[時間属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) として扱われます。
{% endalert %}

{% alert important %}
[**正規表現に一致しない**] フィルターを使用してセグメント化する場合、そのユーザープロファイルに、値を持つカスタム属性がすでに存在している必要があります。ターゲットがユーザーに適切に設定されていることを確認するために、「または」ロジックを使用してカスタム属性が空白であるかどうかチェックすることをお勧めします。
{% endalert %}

### 配列 {#arrays}

配列属性は、ユーザーに関する情報の関連リストの保存に適しています。例えば、ユーザーが視聴した最後のコンテンツ 100 個を配列内に保存すると、特定の関心に基づくセグメンテーションができます。

属性の配列の最大長は、デフォルトで 25 に設定されており、個々の配列について 100 に増やすことができます。例えば、"Movies Watched "のような属性を送信し、それが100に設定されている場合、ユーザーが101本目の映画を見ると、最初の映画は配列から削除され、最新の映画が追加される。

この最大値を増やしたい場合は、カスタマーサクセスマネージャーにお問い合わせください。ダッシュボード管理者は、[**設定の管理**] ページの [**カスタム属性**] タブから、個々の配列の最大長を 100 より大きくすることができます。

単語の間、前後、または後にスペースを含む値を入力すると、Braze はそのスペースもチェックすることに注意してください。

{% alert note %}
属性がデータ型を自動的に検出するように設定されている場合、最大長を増やすオプションは使用できません。データ型を配列に設定する必要があります。
{% endalert %}

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 配列属性に、入力された値と**完全一致する値が含まれている**かどうかをチェックする| **値を含む** | **文字列** | このフィルターが`sci-fi` を指定し、ユーザープロファイルが値`sci-fi` を持つ場合、そのユーザーはこのフィルターにマッチする。|
| 配列属性に、入力された値と**完全一致する値が含まれていない**かどうかをチェックする| **値を含まない** | **文字列** | このフィルターが`sci-fi` を指定し、ユーザープロファイルが値`sci-fi` を持たない場合、そのユーザーはこのフィルターにマッチする。|
| 配列属性に、入力された値、**または**正規表現と**部分一致する値が含まれている**かを確認します | **正規表現に一致する** | **文字列** **OR** **正規表現**<br>最大32,764文字 | |
| 配列**属性に値があるか**、空でないかをチェックする | **値がある** | **該当なし** | このフィルターが`favorite_genres` を指定し、ユーザープロファイルが`favorite_genres` を任意の値で含む場合、ユーザーはこのフィルターにマッチする。 |
| 配列属性が**空である**か、存在しないことをチェックする | **空である** | **該当なし** | このフィルターに `favorite_genres` を指定し、ユーザープロファイルが `favorite_genres` を含まないか、`favorite_genres` を含むが値がない場合、そのユーザーはこのフィルターに一致する。|
| 配列属性に、入力された値と**完全一致する値が含まれている**かどうかをチェックする | **次のいずれかの値を含む** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターに `sci-fi, fantasy, romance` が指定され、ユーザープロファイルに `sci-fi`、`fantasy`、`romance` の任意の組み合わせがある場合 (`sci-fi` のみなど、1 つのみの場合も含む)。`sci-fi`、`fantasy`、`romance` のいずれかがある場合、文字列に `horror` や他の値があってもよい。|
| 配列属性に、入力された値と**完全一致する値が含まれていない**かどうかをチェックする | **次のいずれの値も含まない** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`sci-fi, fantasy, romance` を指定し、ユーザープロファイルが`sci-fi` 、`fantasy` 、`romance` のどの組み合わせも持っていない場合、そのユーザーはこのフィルターにマッチする。`sci-fi`、`fantasy`、`romance` のいずれもない場合、`horror` や他の値があってもよい。|
| 配列属性が、入力された値の**いずれかに部分一致する値を含む**かどうかをチェックする | **値が次のいずれかを含む** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`gold` を指定し、ユーザープロファイル配列が少なくとも1つの文字列に`gold` を含む場合、ユーザーはこのフィルターにマッチする。`gold_tier`、`former_gold_tier` などの文字列値が該当します。||
| 配列属性に、入力された値と**部分一致する値を含まない**かどうかをチェックする | **値が次のいずれも含まない** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`gold` を指定し、ユーザープロファイル配列がどの文字列にも`gold` を含まない場合、そのユーザーはこのフィルターにマッチする。つまり、`gold_tier` や`former_gold_tier` のような文字列値を持つユーザーは、このフィルターにマッチしない。|
| 配列属性が入力された値を**すべて含むか**どうかをチェックする | **次の全ての値が一致する** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。 | このフィルターが`sci-fi, fantasy, romance` を指定し、ユーザープロファイルがそれらの値をすべて持っている場合、ユーザーはこのフィルターにマッチする。ユーザーに `horror` や他の値があっても、このフィルターに一致する。|
| 配列属性が、入力された値の**いずれかを含まない**かどうかをチェックする | **次の全ての値が一致するわけではない** | **文字列**<br>大文字と小文字を区別する。複数の文字列を使用可能 (最大 256 個)。|  このフィルターが`sci-fi, fantasy, romance` を指定し、ユーザープロファイルがそれらの値をすべて持っていない場合、そのユーザーはこのフィルターにマッチする。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
正規表現（regex）の使い方については、以下のリソースをチェックしてほしい：
- [Perl 互換正規表現 (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Braze での正規表現]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [正規表現のデバッガーおよびテスター](https://www.regex101.com/)
- [正規表現のチュートリアル](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### 時刻 {#time}

時刻属性は、特定のアクションが最後に実行された時刻の保存に役立ちます。そのため、コンテンツ固有の再エンゲージメントメッセージをユーザーに提供できます。

相対日付 (1 日超前、2 日未満など) を使用した時刻フィルターでは、1 日を 24 時間として扱います。これらのフィルターを使用して実行するキャンペーンには、24 時間範囲のすべてのユーザーが含まれます。例えば、`last used app more than 1 day ago` はキャンペーンが実行される正確な時刻から「アプリの最終使用が 24 時間超前」のすべてのユーザーを取得します。より長い日付範囲が設定されているキャンペーンも同様です。つまり、「アクティブ化から 5 日間」は、以前の 120 時間を意味します。

例えば、24 ～ 48 時間後に含まれる時刻属性を持つユーザーを対象にするセグメントを構成するには、フィルター `in more than 1 day in the future` と `in less than 2 days in the future` を適用します。

{% alert warning %}
カスタムイベントまたは購入イベントが最後に発生した日付は自動的に記録されます。カスタム時刻属性を使用して再度記録しないでください。
{% endalert %}

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 時間属性が**選択された日付より** **前か**どうかをチェックする| **前** | **カレンダー日付セレクター** | このフィルターが`2024-01-31` を指定し、ユーザー・プロフィールの日付が`2024-1-31` より前の場合、そのユーザーはこのフィルターにマッチする。 |
| 時間属性が、**選択した日付****よりも後**であるかどうかをチェックする| **AFTER** | **カレンダー日付セレクター** | このフィルターが`2024-01-31` を指定し、ユーザー・プロフィールの日付が`2024-1-31` より後の場合、そのユーザーはこのフィルターにマッチする。 |
| 時間属性が**X** **日以上前か**どうかをチェックする | **より大きい** | **過去の日数** | このフィルターに `7` が指定され、ユーザープロファイルの日付が過去 7 日間より前である場合、ユーザーはこのフィルターに一致する。 |
| 時間属性が**X日未満**の**数日前**かどうかを確認します| **未満** | **過去の日数** | このフィルターに `7` が指定され、ユーザープロファイルの日付が過去 7 日間以内である場合、ユーザーはこのフィルターに一致する。|
| 時間属性が**X日以上**先の**未来の日数**であるかどうかを確認します | **超 (未来)** | **未来の日数** | このフィルターに `7` が指定され、ユーザープロファイルの日付が未来 7 日間より後である場合、ユーザーはこのフィルターに一致する。|
| 時間属性が**X日未満**の**未来の日数**であるかどうかを確認します | **未満 (未来)** | **未来の日数**  | このフィルターが`7` を指定し、ユーザー・プロフィールの日付が7日未満先のものである場合、そのユーザーはこのフィルターにマッチする。|
| ユーザーのプロファイルにtime属性が**存在**し、かつnullでないことを確認する。 | **空白でない** | **該当なし** | このフィルターがユーザープロファイルにある時間属性を指定した場合、そのユーザーはこのフィルターにマッチする。|
| ユーザーのプロファイルにtime属性が**存在しないか**、NULLであるかをチェックする。 | **空白である** | **該当なし** | このフィルターがユーザープロファイルにない時間属性を指定した場合、そのユーザーはこのフィルターにマッチする。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 時間属性の詳細

- 定期的なイベントの日
  - [定期的なイベントの日] フィルターを使用し、その後に [定期的なイベントのカレンダー日] を選択するように求められたときに、`IS LESS THAN` または `IS MORE THAN` を選択すると、現在の日付がそのセグメンテーションフィルターでカウントされます。
  - 例えば、2020 年 3 月 10 日に選択した属性の日付が `LESS THAN ... March 10, 2020` である場合、その属性で考慮される日付は 2020 年 3 月 10 日まで (2020 年 3 月10 日を含む) になります。 
- 過去 X 日間以内:「過去 X 日間以内」フィルターには、過去 X 日から現在の日付 / 時刻までの日付が含まれます。
- 未来 X 日間以内: 現在の日付 / 時刻から未来 X 日までの日付が含まれます。

### オブジェクト

階層化カスタム属性を使用して、カスタム属性のデータ型としてオブジェクトを送信できます。詳細については、「[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)」を参照してください。

### オブジェクト配列

関連する属性をグループ化するには、オブジェクト配列を使用します。詳細については、「[オブジェクト配列]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)」の記事を参照してください。

### 演算子の集約

属性フィルター、カスタム属性フィルター、階層化カスタム属性フィルターで使用できる演算子のリストを整理しました。既存のフィルターでこれらの演算子を使用している場合、新しい演算子を使用するように自動的に更新されます。

| データタイプ | 旧オペレーター | 新オペレーター | 値 |
| --- | --- | --- | --- |
| string | イコール | 次のいずれかである | 少なくとも1つの値 |
| string | 等しくない | 次のいずれでもない | 少なくとも1つの値 |
| 配列 | 価値を含む | 次のいずれかの値を含む | 少なくとも1つの値 |
| 配列 | 価値を含まない | 次のいずれの値も含まない | 少なくとも1つの値 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 購入と収益の追跡{#purchase-revenue-tracking}

アプリ内購入の記録に弊社の購入方法を使用すると、個々のユーザープロファイルに生涯価値 (LTV) が設定されます。このデータは、弊社の [収益] ページに表示できます。

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 使用されたドルの合計がある**数値より** **大きいか**どうかをチェックする。| **より大きい** | **数値** | このフィルターが`500` を指定し、ユーザープロファイルが`500` より大きい値を持つ場合、そのユーザーはこのフィルターにマッチする。 |
| 使用されたドルの合計がある**数値より** **小さいか**どうかをチェックする。| **未満** | **数値** | このフィルターが`500` を指定し、ユーザープロファイルの値が`500` より小さい場合、そのユーザーはこのフィルターにマッチする。|
| 合計支出額が**完全一致する****数値**であるかどうかをチェックする| **完全一致** | **数値** | このフィルターが`500` を指定し、ユーザープロファイルが値`500` を持つ場合、そのユーザーはこのフィルターにマッチする。 |
| 最後に購入したのが**X日以降か**どうかをチェックする | **AFTER** | **時間** | このフィルターが`2024/31/1` を指定し、ユーザーの最後の購入が`2024/31/1` 以降である場合、そのユーザーはこのフィルターにマッチする。|
| 最後に購入したのが**X日より前か**どうかをチェックする | **前** | **時間** | このフィルターが`2024/31/1` を指定し、ユーザーの最後の購入が`2024/31/1` より前の場合、そのユーザーはこのフィルターに一致する。|
| 最後に購入したのが**X日以上前か**どうかをチェックする | **より大きい** | **時間** | このフィルターに `7` が指定され、ユーザーの最終購入日が今日から過去 7 日間より前である場合、ユーザーはこのフィルターに一致する。|
| 最後に購入したのが**X日以内か**チェックする | **未満** | **時間** |  このフィルターに `7` が指定され、ユーザーの最終購入日が今日から過去 7 日間以内である場合、ユーザーはこのフィルターに一致する。|
| 購入が**X（最大50）回以上**行われたかどうかをチェックする。 | **より大きい** | 過去**Y日間 (Y = 1,3,7,14,21,30)** |  このフィルターが`7` 回と`21` 日を指定し、ユーザーが過去21日間に7回以上購入した場合、ユーザーはこのフィルターに一致する。|
| 購入**回数がX回（最大50回）以下か**どうかをチェックする。 | **未満** | 過去**Y日間 (Y = 1,3,7,14,21,30)** | このフィルターが`7` 回と`21` 日を指定し、ユーザーが過去21日間に7回未満の購入をした場合、ユーザーはこのフィルターに一致する。|
| 購入が**正確にX回（最大50回）**行われたかどうかをチェックする。 | **完全一致** | 過去**Y日間 (Y = 1,3,7,14,21,30)** | このフィルターが`7` 回と`21` 日を指定し、ユーザーが過去21日間に7回購入した場合、そのユーザーはこのフィルターにマッチする。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
特定の購入の発生回数でセグメンテーションを行う場合は、その購入を個別に[増分カスタム属性]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes)として記録する必要もあります。
{% endalert %}

カスタム属性のデータ型を変更できますが、[データ型の変更]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/)による影響に注意する必要があります。

