---
nav_title: FAQ
article_title: 多変量およびA/B検定のFAQ
page_order: 21
page_type: reference
toc_headers: h2
description: "本稿では、Brazeを用いた多変量およびA/B試験のFAQを取り上げる。"
---

# 多変量テストと AB テストの FAQ

## テストの基本

### A/B検定と多変量検定の違いは何か。

#### A/B テスト

A/Bテストでは、マーケターはキャンペーン内で単一の変数(電子メールの件名行やメッセージの送信時間など)を試しています。これには、オーディエンスのサブセットをランダムに2つ以上のグループに分け、各グループに異なるバリエーションを提示し、どのバリエーションが最も高いコンバージョン率を示すかを観察することが含まれます。通常、パフォーマンスが最も優れたバリエーションは、その後、残りのオーディエンスに送信されます。

#### 多変量テスト 

多変量テストは、AB テストの拡張であり、マーケターは複数の変数を一度にテストし、最も有効な組み合わせを決定できます。たとえば、メールメッセージの件名行、テキストに付随するイメージ、CTA ボタンの色をテストできます。このタイプのテストでは、1 つの実験でより多くの変数とバリエーションの組み合わせを探索し、A/B テストよりも迅速で包括的な洞察を得ることができます。しかし、1つの実験内でより多くの変数や組み合わせをテストするには、統計的有意性を得るためにより多くのオーディエンスが必要です。

### A/B試験結果はどのように算出されているか?

Braze は、ピアソンのカイ二乗検定を使用して、すべてのバリアントを相互にテストします。この検定では、1つのバリアントが統計的に他のすべてのバリアントより優れているかどうかを、p<0.05の有意水準、つまり95%の有意水準で測定します。この有意しきい値を超えるすべてのバリアントで、最良のパフォーマンスのバリアントが「勝者」であると判断されます。

これは信頼スコアとは別のテストです。信頼スコアは、0～100% の数値を持つコントロールと比較したバリアントのパフォーマンスのみを示します。具体的には、バリアントとコントロール間の標準化された換算レートの差が偶然よりも有意に大きいという確信を示しています。

## テストの実行と終了

### 初回の検査はいつ終わりますか?

1回の送信キャンペーンに「勝利バリアント」を使用する場合、「勝利バリアント送信時刻」に到達するとテストは終了します。ブレーズは、最も高い転換率を統計的に有意なマージンで示した場合、バリアントを勝者とみなす。

繰り返し、アクションベース、およびAPI トリガーのキャンペーンでは、インテリジェントセレクションを使用して、各バリアントのパフォーマンスデータを継続的に追跡し、最高のパフォーマンスを示すバリアントに向けてキャンペーントラフィックを継続的に最適化できます。インテリジェント・セレクションでは、ユーザーがランダムなバリアントを受け取る実験グループを明示的に定義するのではなく、Brazeアルゴリズムは、最良のパフォーマンスのバリアントの見積もりを継続的に精緻化し、最上位のパフォーマーをより迅速に選択できる可能性があります。

### 定期的なキャンペーンまたはキャンバスのエントリステップでメッセージバリアントを受信したユーザーは、どのように Braze で処理されますか? 

ユーザは、キャンペーンを初めて受信する前に、特定のバリアントにランダムに割り当てられます。キャンペーンを受信するたびに (またはユーザーが再度キャンバスバリアントに入るたびに)、バリアントのパーセントが変更されない限り、同じバリアントを受信します。バリアントのパーセンテージが変わると、ユーザーは他のバリアントに再配分される可能性があります。再びパーセントを変更するまで、ユーザーはこれらのバリアントに留まります。ユーザは、編集されたバリアントに対してのみ再配布されます。

たとえば、3 つのバリアントを持つキャンペーンまたはキャンバスがあるとします。Variant A とVariant B のみが変更または更新された場合、Variant C のバリアントパーセンテージが変更されていないため、Variant C のユーザは再配布されません。バリアントのパーセントが変わらない限り、コントロールグループも変わりません。以前にメッセージを受信したユーザは、後で送信するコントロールグループに入ることはできません。また、コントロールグループ内のどのユーザもメッセージを受信することはできません。

#### 実験経路についてはどうだろうか。

同じことが当てはまります。なぜなら、実験に続くキャンバスのパスも、さまざまなものだからです。

#### キャンペーンやキャンバスでユーザーを再分配するアクションを取ることはできますか？

キャンバスでユーザーを再分配する唯一の方法は、[実験パスでランダム化されたパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution)を使用することです。これにより、ユーザーがキャンバスに再び入ったときに常にパスの割り当てがランダム化されます。しかし、これは標準的な実験ではなく、コントロール群が治療を受けたユーザーで汚染される可能性があるため、いかなる実験結果も無効になる可能性があります。

## 信頼度とバイアス

### 自信は時間の経過とともに高まるか?

他のすべてが一定であれば、信頼度は時間とともに増加します。保有率が一定であるということは、バリアントAがテストの途中で終了する25%オフのセールについて語るなど、バリアントに影響を与える可能性のある他のマーケティング要因がないことを意味します。

信頼度は、バリアントがコントロールと異なることを Braze がどの程度確信しているかを示す測定値です。より多くのメッセージが送信されるにつれて、テストの統計的能力が増加し、測定されたパフォーマンスの差が偶然によるものではないという信頼性が高まります。一般に、サンプルサイズが大きいほど、バリアントとコントロール間のパフォーマンスの小さな差を特定する際の信頼度が高まります。

### コントロールグループとテストグループの割り当ては、テストにバイアスをもたらす可能性がありますか?

特定のキャンペーンまたはキャンバスを作成する前のユーザの属性またはビヘイビアが、バリアントとコントロールの間で系統的に変化することは、実用的な方法ではありません。 

ユーザをメッセージバリアント、キャンバスバリアント、またはそれぞれのコントロールグループに割り当てるには、まず、ランダムに生成されたユーザー ID をランダムに生成されたキャンペーンまたはキャンバス ID にリンクします。次に、sha256 ハッシュアルゴリズムを適用し、その結果を100 で除算し、残りを保持します(100 のモジュラスとも呼ばれます)。最後に、ダッシュボードで選択されたバリアント(およびオプションのコントロール) のパーセンテージ割り当てに対応するスライスにユーザを順序付けします。

### コントロールグループでレートリミットを使用できないのはなぜですか?

Braze は現在、コントロールグループを持つ A/B テストでのレート制限をサポートしていません。これは、レート・リミティングが、バリアントと同じ方法でコントロール・グループに適用されないため、バイアスが発生するためです。代わりに、[Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) を使用することを検討してください。これにより、分析とキャンペーンのパフォーマンスに基づいて各バリアントを受け取るユーザの割合が自動的に調整されます。
