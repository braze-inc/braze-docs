{% tabs %}
{% tab Android %}
Par défaut, le [SDK Android](https://github.com/braze-inc/braze-android-sdk) natif de Braze ne prend pas en charge les GIF animés pour les cartes de contenu. Toutefois, vous pouvez utiliser une bibliothèque d'images tierce pour afficher des GIF à la place. Pour plus d'informations, voir [Cartes de contenu Android : GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android).
{% endtab %}

{% tab iOS %}
Par défaut, le [SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk) ne prend pas en charge les GIF animés pour les cartes de contenu. Toutefois, vous pouvez envelopper votre propre vue ou une vue tierce dans une instance de la méthode [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider). Pour obtenir une présentation complète, consultez [Tutoriel : Prise en charge des GIF pour les cartes de contenu Swift](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
