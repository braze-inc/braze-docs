---
nav_title: ドラッグアンドドロップの電子メール環境設定センター
article_title: ドラッグアンドドロップの電子メール環境設定センター
alias: "/dnd_preference_center/"
description: "このリファレンスページでは、ドラッグアンドドロップエディタを使用してメール ユーザー設定センターを作成する方法について説明します。"
page_order: 2
---

# ドラッグアンドドロップでメール ユーザー設定センターを作成する

> ドラッグアンドドロップエディタを使用して、ユーザー設定センターを作成およびカスタマイズし、特定の種類の通信を受信するユーザーを管理することができます。1 ワークスペースにつき最大50 個のユーザー設定センターを使用できます。

## ステップ 1:メール ユーザー設定センターの作成

**Audience** > **Subscriptions** > **E メールユーザー設定センター** に移動して、ユーザー設定センターを作成します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Users**> **Subscription Groups**> **Email Preference Center** に移動します。
{% endalert %}

ここには、カスタムユーザー設定センターs の一覧が表示されます。**Create New**を選択して新しいユーザー設定センターを作成するか、既存の名前を選択して変更します。

![][1]

## ステップ 2:メール ユーザー設定センターの名前は?

プリファレンスセンター名には、英数字、ダッシュ、またはアンダースコアのみを使用できます。指定した名前によって、生成されるリキッドタグのシンタックスが決まります。 

このリキッドタグは、任意の送信メール キャンペーンs またはキャンバスステップs に含めることができ、ユーザーをユーザー設定センターに送信します。

![][2]

## ステップ 3:サブスクリプショングループs をユーザー設定センターに追加する

**Launch Editor**を選択して、ドラッグアンドドロップエディタでユーザー設定センターのデザインを開始します。

### 使用可能なサブスクリプショングループの定義

サブスクリプショングループs をユーザー設定センターに表示するには、**\+ Add サブスクリプショングループs** ボタンを選択して、目的のサブスクリプショングループs を選択できるモーダルを起動します。選択後、**Add Subscription Groups**を選択してユーザー設定センターに追加します。

選択したサブスクリプショングループs をさらに設定するには、スマートブロックを選択し、ブロックのプロパティーを調整します。
- サブスクリプショングループsの順序をAdjustする
- 追加サブスクリプショングループの追加または削除s
- 説明を含める
- **すべての**チェックボックスを追加または削除します。このチェックボックスは、このブロックに表示されるすべてのサブスクリプショングループs にユーザーをサブスクライブします
- このブロックに表示されるすべてのサブスクリプショングループs のユーザーを配信停止する** 配信停止をすべての** チェックボックスに追加または削除します

![][3]{: style="max-width:38%;"} ![][4]{: style="max-width:45%;"}

** 配信停止は、テンプレートの下部にあるすべての** ボタンから削除できず、[globally 配信停止]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) はメールを受信することからユーザーを取得します。

## ステップ 4:ドラッグアンドドロップエディタを使用したユーザー設定センターのカスタマイズ

### 一般的なスタイルの設定

**一般的なスタイル**タブから、ユーザー設定センター内の関連するすべてのブロックにアプリ横たわるように特定のスタイルを設定できます。この項で設定したスタイルは、指定したブロックで上書きする場合を除き、メッセージ内のあらゆる場所で使用されます。デザインをより簡単にするために、ページレベルのスタイルを設定アップしてから、ブロックの段階でスタイルをカスタマイズすることをお勧めします。

![][5]{: style="max-width:45%;"}

{% alert tip %}
一般的なスタイルに戻るには、個々のブロックプロパティーで"X" を選択します。次に、メッセージコンテナmessage "X"ボタン、またはエディタバックグラウンドを選択します。
{% endalert %}

## ドラッグアンドドロップユーザー設定センターコンポーネント

ドラッグアンドドロップエディタでは、2 つの主要コンポーネントを使用して、ユーザー設定センター構成を素早く簡単に行とブロック s を作成します。すべてのブロックs は行に配置する必要があります。

{% tabs %}
{% tab 行 %}

行は、セルを使用してメッセージのセクションの水平方向の構成を定義する構造単位です。

![]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

行を選択すると、列カスタマイズセクションに必要な列数を追加または削除して、異なるコンテンツ要素を並べて配置できます。

スライドして、既存の列のサイズを調整することもできます。

![]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

ベストプラクティスとして、行および列のプロパティーを書式設定してから、行内のブロックを書式設定します。間隔と配置は、さまざまな場所で調整できるため、基礎から始めると簡単に編集できます。

{% endtab %}
{% tab ブロック %}

ブロックは、メッセージで使用できるさまざまなタイプのコンテンツを表します。既存の行Segmentの内側に1 つドラッグすると、セルの幅に自動的に調整されます。

![]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

すべてのブロックには、パディング上の粒状コントロールなど、独自の設定s があります。右側のパネルは、選択したコンテンツ要素のスタイルパネルに自動的に切り替えるします。詳細については、[エディタのブロックプロパティー]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)を参照してください。

ユーザー設定センターでカスタムコード ブロックを使用している場合、ユーザーs に配信されたときに、カスタムコードでインラインフレームが生成されないことがあります。

{% endtab %}
{% endtabs %}

## ステップ 5: 確認ページをカスタマイズする

確認ページをカスタマイズするのを忘れないでください!ドラッグアンドドロップエディタウィンドウの上部にある**Confirmation Page**を選択すると、このページを編集できます。この画面は、ユーザー設定センターを使用して環境設定を更新した後、ユーザーsに表示されます。上記と同じスタイル設定機能は、このページにもアプリします。

![][9]{: style="max-width:65%;"}

## ステップ 6:ユーザー設定センターのプレビューと起動

エディタ内で**プレビュー**タブを選択することで、ユーザー設定センターをプレビューできます。ただし、テスト機能は無効です。ユーザー設定センターを編集したら、**Done**ボタンを選択してエディタを閉じることができます。

ユーザー設定センターと確定画面の両方のプレビューが表示されます。このユーザー設定センターに戻るには、**下書きとして保存**を選択します。または、問題がなければ、**ユーザー設定センターを起動**を選択します。

ユーザー設定センターを起動すると、起動後に編集できないため、名前を確認するように求められます。名前を確認すると、ユーザー設定センターが起動し、使用できる状態になります。

## ユーザー設定センターの使用

{% multi_lang_include preference_center_warning.md %}

ユーザー設定センターへのリンクをメールs に配置するには、**Copy Liquid** アイコンを選択して、目的のユーザー設定センターのLiquid タグをコピーします。

![][10]{: style="max-width:75%;"}

[ 配信停止 URL]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/#custom-footer) の挿入方法と同様に、リキッドタグをメールの任意の位置に追加します。

## エラーの処理

ユーザーがユーザー設定センターで**Save**を選択したときにエラーが発生すると、次のデフォルト エラーが表示されます。これは、エディタでカスタマイズまたはスタイル設定できません。ただし、これらのページではエラーのローカライゼーションが引き続きサポートされています。 

![&quot を示すエラーが表示されました。環境設定の保存に問題がありました。もう一度やり直してください。][11]{: style="max-width:55%;"}

[1]: {% image_buster /assets/img/preference_center/preference_center1.png %}
[2]: {% image_buster /assets/img/preference_center/preference_center2.png %}
[3]: {% image_buster /assets/img/preference_center/preference_center3.png %}
[4]: {% image_buster /assets/img/preference_center/preference_center4.png %}
[5]: {% image_buster /assets/img/preference_center/preference_center5.png %}
[6]: {% image_buster /assets/img/preference_center/preference_center6.png %}
[7]: {% image_buster /assets/img/preference_center/preference_center7.png %}
[8]: {% image_buster /assets/img/preference_center/preference_center8.png %}
[9]: {% image_buster /assets/img/preference_center/preference_center9.png %}
[10]: {% image_buster /assets/img/preference_center/preference_center10.png %}
[11]: {% image_buster /assets/img/preference_center/preference_center11.png %} 
