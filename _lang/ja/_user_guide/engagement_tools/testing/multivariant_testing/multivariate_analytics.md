---
nav_title: 分析
article_title: 多変量分析と AB テスト分析
page_order: 10
page_type: reference
description: "この記事では、多変量キャンペーンや AB キャンペーンの結果を表示して解釈する方法について説明します。"
---

# 多変量分析と AB テスト分析

> この記事では、多変量テストまたは AB テストの結果を表示する方法について説明します。テストをまだ設定していない場合は、ステップについては「[多変量テストと AB テストの作成]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)」を参照してください。

キャンペーンが開始されたら、ダッシュボードの [**キャンペーン**] セクションからキャンペーンを選択して、各バリアントのパフォーマンスを確認できます。 

## 最適化オプションによる分析

アナリティクスビューは、初期設定時に[最適化]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/)を選択したかどうかによって異なります。

### 最適化なし

キャンペーンの設定時に [**最適化なし**] を選択した場合、アナリティクスの表示は変わりません。キャンペーンの [**キャンペーン分析**] ページには、コントロールグループ (コントロールグループが含まれている場合) に対するバリアントのパフォーマンスが表示されます。

![複数のバリアントがあるメールキャンペーンのキャンペーンアナリティクスのパフォーマンスセクション。この表には、各バリアントの受信者数、バウンス数、クリック数、コンバージョン数など、さまざまなパフォーマンス指標が記載されている。]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

詳細については、メッセージングチャネルの[キャンペーン分析]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/)記事を参照してください。

### 勝者バリアント

キャンペーンの設定時に最適化対象として**勝者バリアント**を選択した場合は、キャンペーン分析の **AB テスト結果**] という別のタブにアクセスできます。勝者バリアントがテストの残りのユーザーに送信されると、このタブにはその送信の結果が表示されます。

**A/Bテスト結果は**2つのタブに分かれている：[**最初のテスト**] と [**勝者バリアント**]。

{% tabs local %}
{% tab 初回テスト %}

[**初期テスト**] タブには、ターゲットセグメントの一部に送信された初期 AB テストの各バリアントの指標が表示されます。すべてのバリアントのパフォーマンスと、テスト中に勝者が出たかどうかの概要を確認できます。

あるバリアントが95% 以上の[信頼度]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence)で他のバリアントを上回った場合、Braze はそのバリアントに「勝者」ラベルを付けます。

95% の信頼度で他のすべてのバリアントを上回るバリエーションがなく、それでも最もパフォーマンスの高いバリアントを送信することを選択した場合でも、最もパフォーマンスの高いバリアントが送信され、「勝者」というラベルが付きます。

![いずれのバリアントも統計的有意性を示す 95% の信頼しきい値を満たす十分な信頼性で他よりも優れた性能を示さなかった場合に勝者バリアントを決定するために送られた最初のテストの結果。]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### 勝者バリアントの選択方法

Braze は、[ピアソンのカイ二乗検定](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test)を使用してすべてのバリアントを相互にテストします。これは、p < 0.05の有意水準、つまり95％の有意性で1つのバリアントが他のバリアントよりも統計的に優れているかどうかを測定します。その場合、勝者バリアントには「勝者」ラベルが表示されます。

これは信頼スコアとは別のテストです。信頼スコアは、0～100% の数値を持つコントロールと比較したバリアントのパフォーマンスのみを示します。

バリアントはコントロールグループよりも優れている場合がありますが、カイ二乗検定では、1つのバリアントが他のすべてのバリアントよりも優れているかどうかを確認します。[フォローアップテスト](#recommended-follow-ups)により、より詳細な情報が得られる場合があります。

{% endtab %}
{% tab 勝者バリアント %}

[**勝者バリアント**] タブには、2回目の送信の結果が表示されます。残りの各ユーザーには、最初のテストで最もパフォーマンスの高いバリアントが送信されます。**オーディエンス率**を合計すると、勝者バリアントグループ用に予約したターゲットセグメントの割合になります。

![勝者バリアントグループに送られた勝者バリアントの結果。]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

AB テスト送信を含むキャンペーン全体での勝者バリアントのパフォーマンスを確認したい場合は、**キャンペーン分析**ページを確認してください。

### パーソナライズされたバリアント {#personalized-variant}

キャンペーンを設定する際に、最適化のために**パーソナライズド・バリアントを**選択した場合、**A/Bテスト**結果は2つのタブに分けられる：**初期テストと** **パーソナライズド・バリアント**。

{% tabs local %}
{% tab 初回テスト %}

[**初期テスト**] タブには、ターゲットセグメントの一部に送信された初期 AB テストの各バリアントの指標が表示されます。

![各ユーザーの最高パフォーマンスのバリアントを判別するために送られた最初のテストの結果。テーブルには、ターゲットチャネルのさまざまな指標に基づく各バリアントのパフォーマンスが表示されます。]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

デフォルトでは、テストではユーザーのカスタムイベントとメッセージバリアント設定との関連が検索されます。この分析では、カスタムイベントが特定のメッセージバリアントに応答する可能性を高めたり下げたりするかどうかを検出します。次に、これらの関係を使用して、最終送信時にどのユーザーがどのメッセージバリアントを受け取るかが決まります。

カスタムイベントとメッセージ設定の関係は、[**初期送信**] タブの表に表示されます。

![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

テストでカスタムイベントとバリアント設定の間に意味のある関係が見つからない場合、テストはセッションベースの分析方法にフォールバックします。

{% details フォールバック分析法 %}

**セッションベースの分析方法**<br>
フォールバック方式を使用してパーソナライズされたバリアントを決定する場合、[**初期テスト**] タブには、特定の特性の組み合わせに基づいてユーザーが好むバリアントの内訳が表示されます。 

これらの特徴は以下のとおりです。

- **リーセンシー:**最後にセッションを行った日時
- **頻度:**セッションの頻度
- **使用期間:**ユーザーになってからの期間

たとえば、このテストでは、ほとんどのユーザーがバリアント A を好むことがわかりましたが、約3日から12日前にセッションを行ったユーザー、セッションの間隔が1日から12日のユーザー、過去67日から577日以内に作成されたユーザーは、バリアント Bを好む傾向があります。したがって、その部分母集団のユーザーは2回目の送信でバリアント B を受信し、残りのユーザーはバリアント A を受信しました。

![[ユーザー特性] テーブル。ユーザーが、リーセンシー、頻度、および使用期間の 3 つのバケットでどう分類されるかに基づいて、どのユーザーがバリアント 1 およびバリアント 2 を優先するかの予測を示します。]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**パーソナライズされたバリアントの選択方法**<br>
この方法では、個々のユーザーの推奨メッセージは、特定のリーセンシー、頻度、および使用期間の効果の合計です。**ユーザー特性表**に示すように、リーセンシー、頻度、および使用期間は、バケットに分割されます。各バケットの時間範囲は、個々の各キャンペーンのユーザーデータによって決定され、キャンペーンごとに異なります。 

各バケットには、メッセージバリアントごとに異なるコントリビューションまたは「プッシュ」を設定できます。各バケットのプッシュの強さは、[ロジスティック回帰](https://en.wikipedia.org/wiki/Logistic_regression)を使用して初回送信時のユーザー応答から決定されます。この表は、各バケットのどのバリアントユーザーがエンゲージする傾向があるかを示して結果をまとめたものです。個々のユーザーの実際のパーソナライズされたバリアントは、そのユーザーが属する3つのバケツの効果の合計 (各特性に1つずつ) によって異なります。

{% enddetails %}

{% endtab %}
{% tab パーソナライズされたバリアント %}

[**パーソナライズされたバリアント**] タブには、2回目の送信結果が表示されます。残りの各ユーザーには、最も関心を持つ可能性の高いバリアントが送信されます。

このページの3枚のカードには、予想される上昇、全体的な結果、そして代わりに勝者バリアントのみを送信した場合の予測結果が表示されます。上昇が見られない場合でも (場合によっては可能性あり)、結果は勝者バリアント (従来の AB テスト) のみを送信した場合と同じです。 

- **予想される上昇:**標準の AB テストではなくパーソナライズされたバリアントを使用したことによって、この送信で選択された最適化指標の向上 (残りのユーザーが勝利バリアントのみを受信した場合)。
- **全体的な結果:**選択した最適化指標 (*ユニークオープン*、*ユニーククリック*、または*プライマリコンバージョンイベント*) に基づく2回目の送信の結果。
- **予測結果:**代わりに勝利バリアントのみを送信した場合の、選択した最適化指標に基づく 2 番目の送信の予測結果。 

![ユニーク開封数のために最適化されたキャンペーンの「パーソナライズされたバリアント」タブ。カードには、予想リフト、全体のユニーク開封数 (パーソナライズされたバリアントを使用)、および予想されるユニーク開封率 (勝者バリアントを使用) が表示されます。]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

このページの表には、パーソナライズされたバリアント送信の各バリアントの指標が表示されます。**オーディエンス率**を合計すると、パーソナライズされたバリアントグループ用に予約したターゲットセグメントの割合になります。

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## 信頼度について理解する {#understanding-confidence}

信頼度とは、コンバージョン率などのデータの違いが、単なる偶然によるものではなく、現実のものであることをどれだけ確信しているかを示す統計的尺度です。

{% alert note %}
結果に確信が持てませんか？信頼度が表示されるのは、コントロールグループが存在する場合のみになります。
{% endalert %}

結果で重要なのは、結果の信頼度です。たとえば、コントロールグループのコンバージョン率が20% で、バリアント A のコンバージョン率が 25% だったらどうなるでしょうか。これは、メッセージを送信しないよりもバリアント A を送信する方が効果的であることを示しているようです。信頼度が95% であれば、2 つのコンバージョン率の差はユーザーの反応の実際の違いによるものである可能性が高く、その差が偶然に生じた可能性は5% に過ぎないということです。

Brazeは、[Zテスト](https://en.wikipedia.org/wiki/Z-test)と呼ばれる統計的手法を使用して、各バリアントのコンバージョン率をコントロールのコンバージョン率と比較します。前の例のように、信頼度が 95% 以上の結果は、その差が統計的に有意であることを示します。これは、Braze ダッシュボードに2つのメッセージまたはユーザー集団の違いを示す信頼度指標が表示されている場合はどこにでも当てはまります。

一般に、結果がユーザーの実際の好みを反映したものであり、偶然によるものではないことを示すには、少なくとも95% の信頼度が必要です。厳密な科学的テストでは、統計的有意性を判断するために使用される一般的なベンチマークは、95% の信頼度 (つまり「p」値が0.05未満) です。95% の信頼度を継続的に達成できない場合は、サンプルサイズを増やすか、バリアントの数を減らしてみてください。 

信頼度というのは、あるバリアントが他のバリアントより優れているかどうかを表すものではありません。これは純粋に、2つまたはそれ以上) のコンバージョン率が実際には互いに異なることをどれだけ確信しているかを示すものです。これは、サンプルサイズと見かけ上のコンバージョン率の差の関数にすぎません。全体のレートが高いか低いかは、信頼度測定の強さには影響しません。あるバリアントのコンバージョン率が別のバリアントと大きく異なるにもかかわらず、95%以上の信頼度が得られない場合があります。また、2つのバリアントのセットのコンバージョン率/上昇率が似ていても、信頼度が異なる場合もあります。

### 統計的に有意でない結果

95%の信頼度がないテストでも、重要なインサイトが得られる可能性があります。統計的に有意ではない結果が出たテストから学べるいくつかのことを次に示します。

- すべてのバリアントがほぼ同じ効果をもたらした可能性があります。これを知っていれば、これらの変更に費やす時間を節約できます。行動喚起を繰り返すなどの従来のマーケティング戦術が、必ずしもオーディエンスに効果的ではないことに気づくかもしれません。
- 結果は偶然によるものかもしれませんが、次のテストの仮説に役立つ可能性があります。複数のバリアントでほぼ同じ結果が得られた場合は、そのうちのいくつかを新しいバリアントと一緒に再度実行して、より効果的な代替案が見つかるかどうかを確認してください。あるバリアントの方が良い結果を出したが、その差がそれほど大きくない場合は、このバリアントの差をさらに大きくした別のテストを実行できます。
- テストを続けてください！結果が有意でないテストでは、特定の疑問が生じるはずです。バリアントの間に本当に違いはありませんでしたか?テストを別の方法で構成すべきでしたか？フォローアップテストを実行することで、これらの質問に答えることができます。
- テストは、どのタイプのメッセージングがオーディエンスから最も多くの反応を得ているかを発見するのに役立ちますが、メッセージングのどの変更が無視できる効果しかないかを理解することも重要です。これにより、別のより効果的な代替案のテストを続けることも、2つの代替メッセージのどちらを選ぶかを決めるために費やしていた時間を節約することもできます。

テストに明確な勝者がいるかどうかに関係なく、[フォローアップテストを実行](#recommended-follow-ups)して結果を確認したり、結果を少し異なるシナリオに適用したりすると役立つ場合があります。

## おすすめのフォローアップ {#recommended-follow-ups}

1つの多変量テストと AB テストは、今後のテストのアイデアを刺激し、メッセージング戦略の変更に導くことができます (また、そうあるべきです!) 。可能なフォローアップアクションには以下が含まれます。

#### テスト結果に基づいてメッセージング戦略を変更

多変量テストの結果から、メッセージの表現方法や形式を変更することができます。

#### ユーザーを把握する方法を変更する

各テストでは、ユーザーの行動、さまざまなメッセージングチャネルに対するユーザーの反応、およびセグメント間の相違点 (および類似点) が明らかになります。

#### 今後のテストの構成方法を改善する

サンプルサイズが小さすぎましたか？バリアント間の違いが微妙でしたか？各テストは、今後のテストを改善する方法を学ぶ機会となります。信頼度が低い場合は、サンプルサイズが小さすぎるため、今後のテストに備えて拡大する必要があります。バリアントのパフォーマンスに明確な違いが見つからない場合は、その違いが微妙すぎてユーザーの反応に目立った影響を与えなかった可能性があります。

#### サンプルサイズを大きくしてフォローアップテストを実行する

サンプルが大きいほど、バリアント間の小さな違いを検出できる可能性が高くなります。

#### 別のメッセージングチャネルを使用してフォローアップテストを実行する

あるチャネルで特定の戦略が非常に効果的であることがわかった場合は、その戦略を他のチャネルでテストすることをお勧めします。あるタイプのメッセージが、あるチャネルでは有効であるが、別のチャネルでは効果がない場合、特定のチャネルが特定のタイプのメッセージに対してより役立つと結論付けることができる場合があります。あるいは、プッシュ通知を有効にする傾向が高いユーザーと、アプリ内メッセージに注意を払う傾向が高いユーザーとの間には違いがあるかもしれません。最終的には、この種のテストを実施することで、オーディエンスがさまざまなコミュニケーションチャネルとどのようにやりとりしているかを知ることができます。

#### 別のユーザーセグメントでフォローアップテストを実行する

そのためには、同じメッセージングチャネルとバリアントを使用して別のテストを作成しますが、ユーザーセグメントは異なるものを選択します。たとえば、あるタイプのメッセージングが熱心なユーザーに非常に効果的だった場合、離脱したユーザーへの影響を調査すると役立つ場合があります。離脱したユーザーも同様の反応を示す可能性もあれば、他のバリアントのいずれかを好む可能性もあります。このテストは、さまざまなセグメントと、それらがさまざまなタイプのメッセージにどのように応答するかについて詳しく知るのに役立ちます。データに基づいて戦略を立てることができるのに、なぜセグメントについて仮定を立てるのでしょうか？

#### 前回のテストで得たインサイトに基づいてフォローアップテストを実行する

過去のテストから収集したインサイトを今後のテストの指針として活用してください。以前のテストでは、あるメッセージング手法の方が効果的であることが示唆されていますか？バリアントのどの特定の側面がそれを改善したのか不明ですか?これらの質問に基づいてフォローアップテストを実施すると、ユーザーに関するインサイトに満ちた調査結果を得るのに役立ちます。

#### さまざまなバリアントの長期的な影響を比較する

リエンゲージメントメッセージを AB テストする場合は、[リテンションレポート]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)を使用してさまざまなバリアントの長期的な影響を比較することを忘れないでください。リテンションレポートを使用すると、メッセージを受信してから数日、数週間、1か月後に各バリアントがユーザーの行動にどのように影響したかを分析し、上昇が見られるかどうかを確認できます。
