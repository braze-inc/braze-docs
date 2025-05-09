---
nav_title: キャンバスの下書きを保存する
article_title: キャンバスの下書きを保存する
alias: "/save_as_draft/"
page_order: 1
description: "この参照記事では、すでに開始されているキャンバスの下書きを保存する方法について説明します。"
page_type: reference
tool: Canvas
---

# キャンバスの下書きを保存する

> キャンバスを作成して開始するときに、アクティブなキャンバスを編集して下書きとして保存することができます。これにより、開始前に変更を試すことができます。 

大規模な変更を必要とするアクティブなキャンバスがある場合は、この機能を使用して、アクティブなキャンバスでこれらの変更を開始する**前に**、ビルド、保存、および品質チェックを行うことができます。 

すべてのキャンバスと同様に、一度に1人のユーザーのみが1つの下書きを編集でき、一度に1つのキャンバスには1つの下書きしか作成できません。これらの下書きは、ドラフトの変更がまだ開始されていないため、アナリティクスがありません。

![たとえば、下書きキャンバスに、アクティブキャンバスを表示するためのオプションを持つ下書きキャンバスを編集していることをユーザーに示すバナーが付いています。フッターには、分析ビューに戻る、下書きとして保存する、または下書きを開始するオプションがあります。][1]

## ドラフトの作成

下書きを作成するには

1. アクティブなキャンバスに移動します。
2. キャンバスフッタで**下書きとして保存**ボタンを選択します。 

アクティブなキャンバスは、キャンバスの下書きが存在する間は編集できないことに注意してください。キャンバスを更新して変更を適用することも、下書きを破棄することもできます。

## アクティブドラフトの参照

アクティブなキャンバスを参照するには、分析ビューのフッターまたは下書きのキャンバスヘッダーで [**アクティブなキャンバスを表示**] をクリックします。アクティブなキャンバス に戻るには、分析ビューまたはアクティブなキャンバスビューから [**下書きを編集**] を選択します。

下書きが作成される前にすでに起動されているステップのみを参照できます。つまり、下書きが作成された**後に**ステップまたはチャネルを作成した場合、下書きでは参照できません。

{% alert note %}
コンテンツブロックがキャンバスドラフトで参照されている場合、キャンバスはコンテンツブロックの包含カウントにリストされます。ただし、コンテンツブロックが**active**キャンバスのドラフトで参照されている場合、キャンバスはコンテンツブロックの包含カウントにリストされません。
{% endalert %}

### アプリ内メッセージの優先順位付け

アクティブなキャンバスの下書きでユーザーが優先順位を変更すると、キャンバスビルダー内のアプリ内メッセージの優先順位がすぐに更新されます。つまり、キャンバスレベルのアプリ内メッセージの優先順位は、下書きが存在する場合でも、アクティブなキャンバスにすぐに適用されます。 

ただし、ステップレベルのアプリ内メッセージの優先順位の変更は下書きとして保存され、キャンバスが更新されると適用されます。例えば、メッセージステップでは、ステップ設定がステップレベルで適用されるため、ユーザーが下書きを開始すると、優先順位の並べ替えが更新されます。

[1]: {% image_buster /assets/img_archive/canvas_draft1.png %}
