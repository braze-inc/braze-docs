{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) は、**From Display Name + Address** と**Reply-To Address** フィールド s を使用して、カスタム属性s に基づいてこれらをダイナミックなします。これにより、単一のメール キャンペーンまたはキャンバスステップを使用して、さまざまなブランド、地域、または部門から送信できます。
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
コンテキストステップは、[Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)または[Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップsのトリガー実行イベントのプロパティを参照するために必要ではありません。フィルターグループ内のプロパティーは、**コンテキスト変数**フィルターを使用して直接的に参照できます。正しいデータタイプを選択してください。
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
カタログ トリガーアイテムの"画像 s をプルインするには、カタログに`image_url` という名前のフィールドが含まれている必要があります。その後、{%raw%}``{{ items[0].image_url }}``{%endraw%} を使用して参照できます。
{% endalert %}

{% endif %}