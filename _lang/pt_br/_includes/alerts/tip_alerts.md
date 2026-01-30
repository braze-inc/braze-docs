{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
Você pode usar [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) nos campos **From Display Name + Address** e **Reply-To Address** para modelá-los dinamicamente com base em atributos personalizados. Isso permite que você envie de diferentes marcas, regiões ou departamentos usando uma única campanha de e-mail ou etapa do Canva.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
Você não precisa de uma etapa de Contexto para fazer referência a propriedades do evento de gatilho nas etapas de Jornada do [público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) ou [Divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Você pode fazer referência às propriedades diretamente nos grupos de filtros com o filtro **Context Variable (Variável de contexto** ). Certifique-se de selecionar o tipo de dados correto.
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
Para obter imagens para itens de disparo do catálogo, seu catálogo deve incluir um campo chamado `image_url`. Em seguida, você pode fazer referência a ele usando {%raw%}``{{ items[0].image_url }}``{%endraw%}.
{% endalert %}

{% endif %}