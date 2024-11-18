1. **Templates**> **Content Blocks**に移動します。<i class="fas fa-plus"></i>**Create Content Block**をクリックし、**Drag-and-drop Content Block**を選択します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、このページは**Engagement**> **Templates &Media**> **Content Block Library** にあります。
{% endalert %}

{% if include.location == "dnd" %}

{:start="2"}
2\.[エディタブロック]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/)をドラッグアンドドロップして、ドラッグアンドドロップコンテンツブロックを構築します。
3\.フォーマットブロックを**Rows**タブからエディタにドラッグアンドドロップして、コンテンツブロックのレイアウトを作成します。<br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. 必要に応じてコンテンツブロックをドラッグアンドドロップして、メールキャンペーンを構築します。
5. コンテンツブロックを作成したら、**Done**をクリックします。
6. コンテンツブロックに名前を付けます。この名前は、**Content Block Liquid Tag**の一部として自動入力されます。
7\. (オプション) 説明を追加します。
8. **Launch Content Block**をクリックします。

{% elsif include.location == "html" %}

{:start="2"}
2\.HTML を**HTML** タブに入力するか、**Classic** タブでコンテンツブロックをビルドします。<br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. コンテンツブロックを作成したら、**Done**をクリックします。
5. コンテンツブロックの名前を入力します。この名前は、**Content Block Liquid Tag**の一部として自動入力されます。
6\. (オプション) 説明を追加します。
7. **Launch Content Block**をクリックします。

{% endif %}