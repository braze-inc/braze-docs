---
nav_title: 多変量テストと AB テスト
article_title: 多変量テストと AB テスト
page_order: 2
page_type: reference
description: "この参照記事では、多変量テストと AB テストおよびその利点について説明します。"
search_rank: 2
---

# 多変量テストと AB テスト

> このページでは、多変量テストと AB テストとは何か、およびそれらの利点について説明します。多変量またはA/Bテストの作成手順については、[Brazeを使用した多変量およびA/Bテストの作成]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)を参照してください。 

多変量とABテストは[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)を使用して使用できます。

## 多変量テストとABテストとは

### AB テスト

AB テストは、同じマーケティングキャンペーンの複数のバージョンに対するユーザーの反応を比較する実験です。これらのバージョンは、マーケティング目標は同じですが、文言やスタイルが異なります。

目的は、マーケティング目標を最もよく達成するキャンペーンのバージョンを特定することです。このセクションでは、コンテンツの違いによる効果をテストする方法について説明します。

{% alert note %}
メッセージのスケジュールやタイミングの違い (たとえば、非アクティブな状態が1時間続いた場合と、非アクティブな状態が1日続いた場合に、放棄カートメッセージを送信するなど) を評価する場合は、[キャンバスの設定]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)に関するセクションを参照してください。
{% endalert %}

プッシュ通知の選択肢が2つあるとします。

- 「この取引は明日が期限です!」
- 「この取引は24時間で期限が切れます!」

AB テストを使用すると、どの文言がコンバージョン率を高めるかを確認できます。次回取引に関するプッシュ通知を送信したときに、どのタイプの文言が効果的かがわかります。ただし、このテストでは、1つの変数 (プッシュ通知のコピー) の効果のみを検証します。

### 多変量テスト

多変量テストは、2つ以上の変数の効果をテストする点を除いて、AB テストに似ています。プッシュ通知の例に戻りましょう。テストしたいもう1つの変数は、メッセージの最後に絵文字を含めるかどうかです。今度は2つの変数 (または変量—バリアントと混同しないように) をテストすることになります。したがって「多変量」という用語が使われています。そのためには、メッセージの合計4つのバージョンをテストする必要があります。コピーの2つのオプションに絵文字の2つのオプション (存在するかどうか) を乗算すると、合計4つのメッセージバリアントになります。

Braze のドキュメントでは、「多変量テスト」は「AB テスト」と同じ意味で使用されています。これは、両者の設定のプロセスが同じであるためです。

## 多変量テストと AB テストのメリット {#the-benefits-of}

多変量テストと AB テストにより、オーディエンスについて簡単かつ明確に知ることができます。ユーザーが何に反応するかを推測する必要がなくなります。すべてのキャンペーンは、メッセージのさまざまなバリアントを試したり、オーディエンスの反応を測定する機会になります。

多変量テストと AB テストが役立つ具体的なシナリオとしては、次のようなものがあります。

- **メッセージングタイプを初めて試す場合**初回のアプリ内メッセージが正しく表示されるか心配ですか？多変量テストを使用すると、何がユーザーの心に響くかを実験して学習できます。
- **オンボーディングキャンペーンなど、常に送信されるキャンペーンを作成する場合：**ほとんどのユーザーがこのキャンペーンに出くわすことになるので、できるだけ効果的なものにしてはどうでしょうか。
- **送信するメッセージのアイデアが複数ある場合**どちらを選ぶか迷う場合は、テストを実施してから、データドリブン型の意思決定を行ってください。
- **ユーザーが「実証済みの」マーケティング手法に反応するかどうかを調査する場合：**マーケターはユーザーと関わるために従来の戦略に固執することが多いが、製品ごとにユーザー群は異なります。行動喚起を繰り返したり、社会的証明を使ったりしても、望んだ結果が得られないこともあります。多変量テストと AB テストにより、既成概念にとらわれず、特定のオーディエンスに有効な型破りな戦略を見つけることができます。

### バリアントの分布

バリアント間の分布は必ずしも均等ではありません。バリアント分布の仕組みを紹介します。

メッセージが多変量キャンペーンで送信されるたびに、システムは設定された割合に従ってランダムなオプションを独自に選択し、結果に基づいてバリアントを割り当てます。コインをめくるようなものです。異常はあり得ます。コインを100回めくったことのある人なら、選択肢が2つしかないのに、毎回表と裏が正確に半々になることはおそらくないだろうと知っているでしょう。表は52個、裏は48個になるかもしれません。

均等に分割したいバリアントが複数ある場合は、バリアントの数も100の倍数になるようにする必要があります。そうしないと、一部のバリアントは、他のバリアントと比較して、そのバリアントに分散されたユーザの割合が高くなります。たとえば、キャンペーンに7つのバリアントがある場合、7は整数として100で均等に割らないため、偶数のバリアント分布が存在することはできません。この場合、15%の2つのバリアント14%の5つのバリアントを持つことになります。

#### アプリ内メッセージに関する注意

アプリ内メッセージで AB テストを実行すると、あるバリアントと別のバリアントの間で、割合が均等に分割されている場合でも、分析でバリアント分布が高いように表示されることがあります。たとえば、バリアント A とバリアント C の*ユニーク受信者*の次のグラフを考えてみます。

![バリアント A とバリアント C の間に類似した形状を持つ 2 つのバリアントのユニーク受信者のグラフ。バリアント A の方が 1 日あたりのユニーク受信者数が高い]({% image_buster /assets/img/variant_distribution_iam.png %})

バリアント A は、バリアント C よりも*ユニーク受信者*の数が一貫して多いです。これは、バリアント分布によるものではなく、アプリ内メッセージの*ユニーク受信者数*の計算方法によるものです。アプリ内メッセージの場合、*ユニーク受信者数*は実際には*ユニークインプレッション数*で、アプリ内メッセージを受け取って閲覧した人の合計数です。つまり、ユーザーが何らかの理由でメッセージを受け取らなかったり、メッセージを閲覧しないことにした場合、そのユーザーは*ユニーク受信者*数に含まれず、バリアント分布が偏っているように見える可能性があります。

## 多変量テストとABテストのヒント

多変量テストと AB テストにより、ユーザーに関する優れた分析情報が提供されます。ユーザーの行動を真に反映したテスト結果を得るためには、以下のガイドラインに従うこと。

#### 多数のユーザーに対してテストを実行する

サンプルが大きいと、平均的なユーザーの嗜好を反映した結果となり、外れ値に左右されにくくなります。サンプルサイズを大きくすると、勝利マージンの小さい勝者バリアントを識別することもできます。

#### ユーザーを異なるテストグループにランダムに並べ替える

多変量テストでは、ランダムに選択したテストグループを最大8つ作成できます。ランダム化は、テストセットのバイアスを取り除き、テストグループの構成が類似している確率を高めるように設計されています。これにより、応答率の違いがサンプルではなくメッセージの違いによるものであることが保証されます。

#### テストしようとしている要素を知る

多変量テストおよび AB テストでは、メッセージの複数のバージョン間の違いをテストできます。場合によっては、単純なテストが最も効果的かもしれません。変更を分離することで、応答に最も大きな影響を与えた要素を特定できるためです。場合によっては、バリアント間のより多くの違いを提示することで、外れ値を調べ、さまざまな要素のセットを比較できます。どちらの方法も、テスト対象が最初から明確であれば、必ずしも間違っていません。

#### テストの実行期間を決め、テストを早期に終了しない

テストを始める前に、テストの実行時間を決め、それを遵守します。マーケターは、気に入った結果が出たらテストをやめたくなることが多く、調査結果にバイアスがかかってしまいます。覗き見したくなる気持ちを抑えて、テストを早く終わらせないようにしましょう。

#### キャンペーン開始後ではなく、開始前のキャンペーンにテストを追加する。

キャンペーンを開始した後にテストを追加すると、テストが正しく実行されず、不正確または誤解を招く統計データを受け取る可能性がある。例えば、開始したキャンペーンに再エントリーが可能なテストを追加した場合、キャンペーンに再エントリーしたユーザーは常に同じパスを通ることになり、テストによるデータの不正確さを防ぐことができる。さらに、テスト実行中にバリアントを変更した場合、その変更はテストを無効にして再スタートさせる。

正確な検査結果のために：
1. 開始したキャンペーンを複製します。
2. オリジナルキャンペーンを中止します。
3. 次に、複製したキャンペーンにテストを追加する。 

#### 可能であれば、コントロールグループを含める

[コントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group)を含めると、メッセージをまったく送信しないよりも、メッセージがユーザーのコンバージョンに大きな影響を与えているかどうかを知ることができます。


[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.png %}
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[180]: {% image_buster /assets/img/ab_create_4.png %}
[210]: {% image_buster /assets/img/ab_create_8.png %}
[10]: {% image_buster /assets/img/ab_send_winning_variant.png %}
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[intelselection] ：{{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
