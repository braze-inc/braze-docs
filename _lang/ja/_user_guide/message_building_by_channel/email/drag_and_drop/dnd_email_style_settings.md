---
nav_title: メールグローバルスタイルの設定
article_title: メールグローバルスタイルの設定
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "このリファレンス記事では、キャンペーンとキャンバスのドラッグアンドドロップエディタでグローバルメールスタイル設定を設定する方法について説明します。"
tool: 
  - Campaigns
  - Canvas
---

# メールグローバルスタイルの設定

> グローバルスタイル設定を使用すると、メールキャンペーンとキャンバスの外観をカスタマイズできます。ドラッグアンドドロップエディタのデフォルトテーマを追加およびカスタマイズできます。これには、メールタイトル、テキスト、ボタンなどのスタイルの編集が含まれます。これらの設定を組み合わせて使用すると、メールメッセージの一貫した外観を作成できます。

グローバルスタイル設定を編集するには、**Settings**> **Email Preferences**> **Drag-and-Drop Email Preferences** に移動します。ドラッグアンドドロップ電子メールエディタでスタイルを編集した後、**Save**をクリックします。メールキャンペーンとキャンバスをさらにカスタマイズするには、[ドラッグアンドドロップエディタブロック][8] の組み込み方法を確認してください。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは**Manage Settings**> **Email Settings**> **ドラッグアンドドロップEmail Editor Settings**にあります。
{% endalert %}

![][1]

{% alert note %}
グローバルスタイル設定に対する更新は、今後のすべてのメールキャンペーンおよびキャンバスに適用されます。
{% endalert %} 

## 基本的なスタイル指定 

**Basic Styling**では、メールキャンペーンとキャンバスのデフォルトのメールとコンテンツの背景色を設定できます。また、デフォルトのフォントを選択したり、カスタムフォントを追加したり、リンクの色を編集したりすることもできます。

![メールとコンテンツの背景色、デフォルトのフォント名、デフォルトのリンク色を編集するオプションを含む基本的なスタイルオプション][2] 

## カスタムフォント

カスタムフォントを使用すると、さまざまなメールプラットフォーム間でブランディングの一貫性を保つために、Web フォントを手動で追加できます。セクションごとに1 つのカスタムフォントを追加できます。 

カスタムフォントを追加する前に、カスタムフォントファイルが次の要件を満たしていることを確認します。

- カスタムフォントファイルを提供するサーバでCORS を有効にする必要があります。これは通常、IT チームによって管理されます。 
  - カスタムフォントファイルにはヘッダーが必要です。 `Access-Control-Allow-Origin: *`
- ファイルURL は、CSS ファイル(WOFF、OTF などではない) を指している必要があります。
- カスタムフォント名は、CSS ファイル内のフォントフェイスの名前と一致する必要があります

カスタムフォントを追加するには:

1. **スタイルセクションの**デフォルトのフォント名**の下にカスタムフォント**を追加をクリックします。
2. **Font Name**フィールドに、カスタムフォントソースファイルに表示されるのと同じフォント名を入力します。名前が大文字に変換され、正しくスペースが空いていることを確認します。 
3. **Font URL** フィールドに対応するURL を入力します。
4. 保存する前に、プレビューにカスタムフォントが表示されることを確認します。 
5. カスタムフォントをデフォルトの電子メールフォントとして使用するには、**Save**をクリックします。 

{% alert important %}
Gmail はカスタムフォントをサポートしていないため、カスタムフォントがデフォルトのシステムフォントとして表示される場合があります。その他の電子メールプラットフォームの場合は、電子メールメッセージを送信する前にカスタムフォントが正しく表示されることを確認します。
{% endalert %}

カスタムフォントプロバイダーは、受信者から個人データを収集する場合があることに注意してください。使用する前に、フォントプロバイダーのポリシーを確認してください。

メールキャンペーンで別のカスタムフォントを使用するには、[メールテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/)または[コンテンツブロック]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/)を作成するオプションがあります。フォントの選択肢がウェブセーフであり、メールプラットフォームでサポートされていることを確認してください。 

### フォールバックフォント 

デフォルトのフォント選択が受信トレイプロバイダまたはオペレーティングシステムでサポートされていない場合、フォールバックフォントはタイトル、ヘッダー、および本文テキストに使用されます。デフォルトでは、グローバルスタイル設定が保存されると、Braze は自動的にArial をフォールバックフォントとして設定します。また、デフォルトのフォントファミリのオプションとして、serif またはsans serif を追加することもできます。

![][11]

最大17 個のフォールバックフォントを追加できます。最初に選択されたフォールバックフォントが最初に試行されたフォントになります。フォールバックフォントは、新しく作成されたテンプレート、メールキャンペーン、およびキャンバスコンポーネントにのみ適用されます。フォールバックフォントは、フォールバックフォントが指定される前に作成されたメッセージに対して自動的には設定されません。ブランド全体の一貫性を維持するために、メールメッセージに類似したフォールバックフォントを選択することを強くお勧めします。

## タイトルのスタイル指定

ここでは、フォントサイズ、フォントの色、およびテキストの配置を編集して、メールタイトルのスタイルを調整できます。これは、メインヘッダとセカンダリヘッダに適用されます。 

![][9]

必要に応じて、ドラッグアンドドロップエディターテーマのデフォルトスタイルをオーバーライドできます。**Override default style**をクリックして、タイトルスタイルの選択を適用します。これには、異なるフォントとリンクカラーの設定を含めることができます。

## 段落のスタイル指定

デフォルトの段落スタイルを設定するには、**段落スタイル**に移動し、**フォントサイズ**を入力し、**フォントの色**を選択してフォントの色を選択します。また、**Padding Top**、{<span=>Padding Right<<span=}、{<span=>Padding Bottom<<span=}、および**Padding Left** の値を編集して、本文のブロックスタイルを調整することもできます。これは、段落ブロックを囲む4 つの領域すべての間隔に適用されます。

![][7]

## リストのスタイル指定

メッセージングにリストを追加する場合、**リストスタイル**セクションでは、リストのスタイルの一貫性が作成されます。これには、以下のような詳細が含まれます。 

- フォントサイズ
- 文字色
- フォントの太さ
- 線の高さ
- 配置
- 文字の方向
- 文字間隔
- リスト項目の間隔
- リスト項目のインデント (字下げ)
- リストのタイプ
- リストスタイルのタイプ

**List Type**は、番号または箇条書きのいずれかに設定できます。**List Style Type**では、リストのスタイルを追加でカスタマイズできます。たとえば、リストタイプを常に箇条書きに設定し、各箇条書き項目を正方形に設定できます。  

![][10]

## ボタンのスタイル指定

**Button Styling**セクションでは、ボタンの次のデフォルトスタイルを編集できます。
\- 背景色
-ォントサイズ
\- ォントの色
\- 境界線の半径
\- 境界線の色
\- 境界線の太さ
\- ボタンパディング

![][12]

他のすべてのスタイルセクションと同様に、**Padding Top**、{<span=>Padding Right<<span=}、{<span=>Padding Bottom<<span=}、および**Padding Left** の値を編集して、ブロックスタイルを調整できます。

## メールテンプレートの幅

メールテンプレートの幅を使用して、メールキャンペーン間の整合性を調整し、幅を設定できます。 

![][13]

## コンテンツブロックの幅

メールのドラッグアンドドロップエディタでコンテンツブロック幅を設定することもできます。コンテンツブロックの幅をメールテンプレートの幅に一致させることをお勧めします。

![][14]


[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_paragraph_styling.png %}
[9]: {% image_buster /assets/img_archive/dnd_title_styling.png %}
[10]: {% image_buster /assets/img_archive/dnd_list_styling.png %}
[11]: {% image_buster /assets/img_archive/dnd_fallbacks.png %}
[12]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[13]: {% image_buster /assets/img_archive/dnd_email_template_width.png %}
[14]: {% image_buster /assets/img_archive/dnd_content_block_width.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks
