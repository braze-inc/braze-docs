---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Cet article de référence décrit le partenariat entre Braze et Certona, une solution de personnalisation omnicanal en temps réel qui offre une personnalisation tout au long du cycle de vie du client. Utilisez Certona avec le partenaire Braze Connected Content pour insérer facilement des recommandations de contenu dans les campagnes multicanal."
page_type: partner
search_tag: Partner

---

# Certona

> La plateforme de Certona stimule la personnalisation tout au long du cycle de vie du client. Des campagnes d'e-mail hautement individualisées aux recommandations de produits alimentées par l'apprentissage automatique, Certona garantit que vous exploitez la puissance de la personnalisation.

_Cette intégration est maintenue par Certona._

## À propos de l'intégration

L'intégration de Braze et Certona exploite les recommandations de produits de machine learning de Certona dans les campagnes et Canvases de Braze via le contenu connecté.

## Conditions préalables

| Condition| Description|
| ---| ---|
| [Compte Certona](https://manage.certona.com/) | Un compte Certona est requis pour profiter de ce partenariat. |
| [Enpoint de l’API REST Certona](https://manage.certona.com/) | Cet endpoint est utilisé directement dans votre message de campagne Braze pour extraire le contenu recommandé basé sur l'ID utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Utilisez l'API REST de Certona pour insérer du contenu personnalisé dans vos messages. Cela peut être fait en ajoutant le modèle de contenu connecté suivant dans votre compositeur de message Braze avec votre endpoint API REST Certona.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Ensuite, définissez le contenu que vous souhaitez appeler, tel que le texte ou les images pertinents. Par exemple,`{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Image d'une campagne de communication avec un contenu connecté de Certona inclus dans le corps du message.]({% image_buster /assets/img/certona.png %})

Une fois que vous avez mis ce message dans le corps du compositeur, prévisualisez votre appel de contenu connecté pour vous assurer que vous avez affiché les bonnes informations.

![Une image montrant l'onglet "Test", encourageant les utilisateurs à tester minutieusement leur message avant de l'envoyer.]({% image_buster /assets/img/certona2.png %})


