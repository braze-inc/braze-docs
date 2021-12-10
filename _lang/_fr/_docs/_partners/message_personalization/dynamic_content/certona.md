---
nav_title: Certona
article_title: Certona
alias: /fr/partners/certona/
description: "Cet article décrit le partenariat entre Braze et Certona, une solution de personnalisation omnichannel en temps réel qui offre la personnalisation tout au long du cycle de vie du client. Utilisez Certona avec le partenaire de contenu connecté de Braze pour insérer facilement des recommandations de contenu à travers des campagnes multicanaux."
page_type: partenaire
search_tag: Partenaire
---

# Certona

> La plate-forme Certona permet la personnalisation du cycle de vie du client. Des campagnes de courrier électronique hautement personnalisées aux recommandations de produits tirés de l'apprentissage automatique, Certona vous assure de profiter de la puissance de la personnalisation.

L'intégration de Braze et Certona tire parti des recommandations de produits d'apprentissage automatique de Certona dans les campagnes et les toiles de Braze par le biais de Contenus connectés.

## Pré-requis

| Exigences                                                                    | Libellé                                                                                                                                                                 |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Compte Certona](https://manage.certona.com/)                                | Un compte Certona est requis pour profiter de ce partenariat.                                                                                                           |
| [Point de terminaison de l'API REST de Certona](https://manage.certona.com/) | Ce point de terminaison est utilisé directement dans votre message de campagne Braze pour extraire le contenu recommandé en fonction de l'identifiant de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Utilisez l'API REST de Certona pour insérer du contenu personnalisé dans vos messages. Cela peut être fait en ajoutant le modèle de contenu connecté suivant à votre compositeur de message Braze avec votre point de terminaison de l'API REST Certona.

{% raw %}
```liquid
{% connected_content <INSERT_CERTONA_REST_API_KEY> :save recommendations %}
```

Ensuite, définissez le contenu que vous souhaitez appeler, tel que le texte pertinent ou les images. Par exemple, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

!\[compositeur de message Certona\]\[1\]

Une fois que vous avez mis ce message dans le corps du compositeur, prévisualisez votre appel de contenu connecté pour vous assurer que vous avez affiché les informations correctes.

!\[Certona testing\]\[2\]
[1]: {% image_buster /assets/img/certona.png %} [2]: {% image_buster /assets/img/certona2.png %}