---
nav_title: コンテンツブロック
article_title: ドラッグ＆ドロップエディターのコンテンツブロック
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "このリファレンス記事では、ドラッグ＆ドロップエディターでコンテンツブロックを作成し、使用する方法について説明します。"
tool: Media

---

# ドラッグ＆ドロップ・エディター コンテンツ・ブロック

> ドラッグ＆ドロップエディターでのみ使用されるコンテンツブロックは、さまざまなチャネルで使用される[コンテンツブロックと]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)似た機能を持っています。様々なメールキャンペーンで参照できる情報を一元管理できる。これには、Eメールのヘッダーやプロモーションの吹き出しなどを、再利用可能な1つの行にまとめることも含まれる。

{% alert note %}
ドラッグ＆ドロップのコンテンツブロックは、Canvasのメールキャンペーンとメールメッセージでのみ使用できる。
{% endalert %}

## コンテンツ・ブロックを作成する

コンテンツブロックを作成するには、次の手順を実行します。

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
各コンテンツ・ブロックをドラッグ・アンド・ドロップできるのは1行に限られる。ただし、ドラッグ＆ドロップエディターのブロックを使用して、メールメッセージングに合わせてコンテンツブロックを構築したりカスタマイズしたりできます。
{% endalert %}

## コンテンツ・ブロックを使う

コンテンツブロックをメールに追加するには、エディタを使う方法とLiquidを使う方法がある。

### エディターを使ってコンテンツブロックを追加する

エディターにコンテンツブロックを追加するには、次の手順を実行します。

1. エディターの「**行」**タブに移動し、「**コンテンツ・ブロック**」を選択する。 
2. コンテンツブロックをメールエディターにドラッグ＆ドロップする。 
3. (オプション） ナビゲーションメニューのボタンを選択して、コンテンツブロックの幅を調整します。デフォルトの幅は100％である。<br><br>![幅を編集するオプションを持つ両面矢印。][1]{: style="max-width:30%;" }<br><br>

コンテンツブロックをメールエディターに追加した後、**テンプレート＆メディアで**作成した元のコンテンツブロックに影響を与えないように、コンテンツブロックを編集することができる。ドラッグ＆ドロップで追加されたコンテンツブロックは、元のコンテンツブロックにリンクされていないからだ。元のコンテンツブロックに加えた変更を表示するには、メールエディターにもう一度ドラッグします。 

1つの行ブロックに複数のコンテンツブロックを追加すると、ドラッグ＆ドロップエディターで位置ずれが発生することがある。行レベルでコンテンツ全体の整列を維持するために、別々の行ブロックを使ってみよう。

### Liquid を使用したコンテンツブロックの追加

Liquid を使用してコンテンツブロックを追加するには、次の手順を実行します。

1. メールキャンペーンに移動して、[**メール本文を編集**] を選択します。 
2. [<i class="fas fa-plus"></i> **パーソナライゼーション**] をクリックします。
3. **パーソナライズの追加]**タブを見つけ、**[パーソナライズの種類]**ドロップダウンで**[コンテンツブロック]**を選択する。
4. **属性**フィールドでコンテンツブロックの名前を選択する。[Liquid スニペット] フィールドにコンテンツブロックの Liquid タグが入力されます。 
5. リキッドのスニペットをコピーしてテキストエディタのブロックに貼り付ける。<br>![オプションが表示されている「個人用設定を追加」タブ。][2]{: style="max-width:30%;"}

メールメッセージングをプレビューすると、Liquid スニペットはドラッグ＆ドロップエディターのコンテンツブロックとして表示されます。 

{% alert important %}
コンテンツブロックが Liquid によりメールエディターに追加されると、このコンテンツブロックは [**テンプレートとメディア**] で作成した元のコンテンツブロックにリンクされます。つまり、このコンテンツブロックは、元のコンテンツブロックテンプレートへの変更を反映して更新されます。
{% endalert %}

## コンテンツブロックの更新

既存のコンテンツ・ブロックを更新するには、**コンテンツ・ブロック・**ページから元のコンテンツ・ブロックを編集するか、元のメッセージから新しいコンテンツ・ブロックにHTMLをコピーする。コンテンツブロックテンプレートを更新すると、Liquid 経由でコンテンツブロックが追加されたすべてのメールメッセージで更新が行われます。

コンテンツブロックをアーカイブするには、[**テンプレート**] > [**コンテンツブロック**] に移動し、コンテンツブロックの縦 3 点リーダーアイコン <i class="fas fa-ellipsis-vertical"></i> を選択して [**アーカイブ**] をクリックします。コンテンツブロックをアーカイブしても、メッセージにはアーカイブされたブロックのコンテンツが含まれる。ただし、アーカイブされたコンテンツ・ブロックは読み取り専用なので、編集する前にコンテンツ・ブロックのアーカイブを解除すること。 

[1]: {% image_buster /assets/img_archive/content_block_width.png %}
[2]: {% image_buster /assets/img_archive/dnd_content_block_personalization.png %}
