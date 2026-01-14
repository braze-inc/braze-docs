---
nav_title: Klaviyoで構成する
article_title: KlaviyoでBrazeAI Decisioning Studioを設定する
page_order: 3
description: "BrazeAI Decisioning<sup>StudioTM</sup>Goで使用するKlaviyo Flowの設定方法を学ぶ。"
toc_headers: h2
---

# KlaviyoでBrazeAI Decisioning Studio™ Goを設定する

> Klaviyoでプレースホルダーテンプレートとフローを設定し、BrazeAI Decisioning Studio™ Goを通じてアクティベーションをトリガーする。

{% alert important %}
新しい実験者を設定するごとに、Klaviyoで新しいフローを作成しなければならない。テンプレートをインポートするためのプレースホルダーフローを以前に作成した場合は、新しいフローを作成する必要があり、以前のプレースホルダーフローを再利用することはできない。
{% endalert %}

Klaviyoでフローを作成する前に、BrazeAI Decisioning Studio™ Goポータルから以下の詳細を参照できるようにしておく必要がある：

- フロー名
- トリガーイベント名

## Klaviyoでプレースホルダーテンプレートを作成する

BrazeAI Decisioning Studio™ Goは、Klaviyoアカウントの既存のフローに関連付けられたテンプレートをインポートする。どのフローにも関連付けられていないテンプレートを使用するには、使用したいテンプレートを含むプレースホルダーフローを作成すればよい。流れは下書きとして残しておくことができる。

### ステップ 1: 流れを設定する

{% alert note %}
このプレースホルダーフローの目的は、希望するコンテンツをBrazeAI Decisioning Studio™ Goにインポートすることである。後のステップで別のフローを作成する必要があり、BrazeAI Decisioning Studio™ Goは、実験者がライブになった時点で、このフローを使ってアクティベーションをトリガーする。
{% endalert %}

1. Klaviyoで、**Flowsを**選択する。 
2. **フローを作成**>**ゼロから作成を**選択する。
3. プレースホルダーフローにわかりやすい名前を付け、「**フローを作成**」を選択する。

![OFEプレースホルダーフロー」という名前のフロー。]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4. 任意のトリガーを選択し、フローを保存する。
5. **Confirmを**選択**し、保存する**。 

### ステップ 2:プレースホルダー・テンプレートを作成する

次に、プレースホルダー・テンプレートを作成する： 

1. **トリガーの**後に**メール**ノードをドラッグ＆ドロップする。

![トリガーノードの後にメールノードが続くフロー。]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\.**メール」**ノードで、「**テンプレートの選択**」を選択する。
3\.次に、使用するテンプレートを選択し、**Use templateを**選択する。
4. **Save**>**Doneを**選択する。
5. (オプション) BrazeAI Decisioning Studio™ Goで使用するテンプレートをさらに追加するには、別の**メール**ノードを追加し、ステップ2～4を繰り返す。
6. すべてのメールを**下書き**モードにしたまま、フローを終了する。

BrazeAI Decisioning Studio™ Goポータルでは、テンプレートはプレースホルダーフローの下で選択できるはずである。

![Decisioning Studio GoポータルのプレースホルダーKlaviyoテンプレートの例。]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## Klaviyoでフローを作成する

### ステップ 1: 流れを設定する

1. Klaviyoで、**フロー**>**フローの作成を**選択する。
2. **自分で作る**」を選択する。
3. **Nameには**、BrazeAI Decisioning Studio™ Goポータルのフロー名を入力する。次に、**Create manuallyを**選択する。

![フロー例で「手動で作成」オプションを選択した。]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4. トリガーを選択する。
5. BrazeAI Decisioning Studio™ Goポータルから、メトリック名とトリガーイベント名を一致させる。

![トリガー・イベント名にマッチするメトリクス名の例"OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6. [**保存**] を選択します。

{% alert note %}
実験者がベーステンプレートを1つ持っている場合は、以下のステップに進む。実験者が2つ以上のベーステンプレートを持っている場合は、[ステップ3にスキップする：](#step-3-add-a-trigger-split-to-your-flow) あなたのフローにトリガースプリットを追加する。
{% endalert %}

### ステップ 2:フローにメールを追加する 

1. **トリガー・**ノードの後に**メール・**ノードをドラッグ＆ドロップする。
2. **メールの詳細**で、**テンプレートの選択を**選択する。

!["メールの詳細 "セクションで "テンプレートを選択 "オプションを選択する。]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\.ベーステンプレートを探して選択する。BrazeAI Decisioning Studio™ Goポータルの**使用するリソース**セクションで、テンプレート名からテンプレートを検索できる。

![Klaviyoのベーステンプレートの例。]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4. **テンプレートを使用**＞**保存を**選択する。
5. **件名には** {% raw %}`{{event.SubjectLine}}`{% endraw %} と入力する。
6. **Sender name（送信者名**）と**Sender email address（送信者メールアドレス**）には、使用したい詳細を入力する。

![メール1」の件名、送信者名、送信者メールアドレスの例。]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7. ［**完了**] を選択します。
8. **最近メールしたプロファイルをスキップする**]チェックボックスの選択を外し、[**保存]**を選択する。
9\.メールノードで、モードを**下書きから** **本番に**更新する。

![Klaviyoフローエディターでは、トリガーノードがメールノードに接続されている。]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

すべて完了しました。BrazeAI Decisioning Studio™ Goでトリガーできるようになった。 

### ステップ 3:フローにトリガー・スプリットを追加する 

1. **トリガー** **ノードの**後に**トリガースプリットノードを**ドラッグ＆ドロップする。
2. **トリガー分割**ノードを選択し、**ディメンションを** **EmailTemplateID** に設定する。

![Klaviyoのフロー図は、ディメンションEmailTemplateIDで設定されたトリガースプリットにトリガーノードをフィードしている。]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### ステップ 3.1:メールテンプレートを追加する

1. BrazeAI Decisioning Studio™ Goポータルで、**使用するリソース**セクションの下にある、最初の**テンプレートのメールテンプレートIDを**見つける。**Dimension**フィールドに**メールテンプレートIDを**入力し、**Saveを**選択する。
2. **Eメール**ノードを**トリガースプリットの** **Yes**ブランチにドラッグ＆ドロップする。 

![トリガー分岐ノードを持つKlaviyoフローで、Yes分岐はメールノードにつながり、No分岐は別のトリガー分岐につながる。]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\.**メールの詳細**で、**テンプレートの選択を**選択する。
4. ベーステンプレートを探して選択する。BrazeAI Decisioning Studio™ Goポータルの**使用するリソース**セクションで、ベーステンプレート名からテンプレートを検索できる。
5. **テンプレートを使用**＞**保存を**選択する。
6. **件名には** {% raw %}`{{event.SubjectLine}}`{% endraw %} と入力する。
7. **Sender name（送信者名**）と**Sender email address（送信者メールアドレス**）には、使用したい詳細を入力する。

![選択されたメールテンプレートと、件名、送信者名、送信者メールアドレスのフィールド。]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8. ［**完了**] を選択します。
9\.**最近メールしたプロファイルをスキップする**]チェックボックスの選択を外し、[**保存]**を選択する。
10\.メールノードで、モードを**下書きから** **本番に**更新する。

#### ステップ 3.2:新しいトリガースプリットを追加する

次に、実験者が使用する追加のベーステンプレートごとに、新しい**トリガースプリットと** **メール**ノードを作成する。 

1. 別の**トリガー分割**ノードを、前の**トリガー分割**ノードの**No**Branchにドラッグ＆ドロップする。
2. **Dimensionを** **EmailTemplateIDに**設定し、設定するベース**テンプレートのメールテンプレートIDを** **Dimensionの**値に記入する。
3. [**保存**] を選択します。

![Klaviyoフローエディターの図。トリガーノードがトリガースプリットにつながっている。トリガースプリットには、メールノードにつながるYesブランチと、追加のメールノードにつながる別のトリガースプリットに接続するNoブランチがある。]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4. 新しいトリガースプリットの**Yes**Branchに**Email**ノードをドラッグ＆ドロップする。
5. [ステップ3.](#step-31-add-your-email-template)1のステップ1～5を繰り返し、対応するテンプレートを選択する。
5. **件名を** {% raw %}`{{event.SubjectLine}}`{% endraw %} に設定し、**最近メールしたプロファイルをスキップする**チェックボックスのチェックを外す。
6. 実験者が使用しているベーステンプレートごとに、**トリガー分割**ノードと**メール**ノードが1つずつできるまで、このプロセスを繰り返す。最後のトリガー・スプリットでは、"No "ブランチには何も入っていないはずだ。

![複数のメールノードに分岐する複数のトリガー分岐ノードを持つKlaviyoフロー。]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7. **各Eメール**ノードで、モードを**下書きから** **ライブに**更新する。

![ノードのステータスを「ライブ」に更新するオプション。]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

すべて完了しました。BrazeAI Decisioning Studio™ Goでトリガーできるようになった。 