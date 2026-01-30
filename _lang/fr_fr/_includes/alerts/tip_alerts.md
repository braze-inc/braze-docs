{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
Vous pouvez utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) dans les champs **De Afficher le nom + l'adresse** et **Répondre à l'adresse** pour les modeler dynamiquement en fonction d'attributs personnalisés. Cela vous permet d'effectuer des envois à partir de différentes marques, régions ou départements à l'aide d'une seule campagne d'e-mail ou d'une seule étape du canvas.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
Vous n'avez pas besoin d'une étape Contexte pour référencer les propriétés de l'événement déclencheur dans les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) ou [Arbre]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) [décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Vous pouvez référencer les propriétés directement dans les groupes de filtres à l'aide du filtre **Variable de contexte**. Veillez à sélectionner le bon type de données.
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
Pour extraire des images pour les éléments déclencheurs du catalogue, votre catalogue doit inclure un champ nommé `image_url`. Vous pouvez ensuite y faire référence en utilisant {%raw%}``{{ items[0].image_url }}``{%endraw%}.
{% endalert %}

{% endif %}