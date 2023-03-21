---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Cet article de référence présente le partenariat entre Braze et Certona, une solution de personnalisation omnicanal en temps réel qui offre une personnalisation tout au long du cycle de vie du client. Utilisez Certona avec le partenaire de Contenu connecté de Braze pour insérer facilement des recommandations de contenu dans les campagnes multicanal."
page_type: partner
search_tag: Partenaire

---

# Certona

> La plateforme de Certona dirige la personnalisation au cours du cycle de vie du client. Certona s’assure que vous tirez parti de la puissance de la personnalisation à travers des campagnes d’e-mails fortement personnalisées comme des recommandations produit propulsées par machine learning.

L’intégration de Braze et de Certona tire parti des recommandations produit de machine learning de Certona dans les campagnes de Braze et les Canvas via le Contenu connecté.

## Conditions préalables

| Condition| Description|
| ---| ---|
| [Compte Certona](https://manage.certona.com/) | Un compte Certona est requis pour profiter de ce partenariat. |
| [Endpoint API REST de Certona](https://manage.certona.com/) | Cet endpoint est utilisé directement dans votre message de campagne Braze pour extraire le contenu recommandé en fonction de l’ID utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Utilisez l’API REST de Certona pour insérer du contenu personnalisé dans vos messages. Pour ce faire, ajoutez le modèle de Contenu connecté suivant dans votre éditeur de messages Braze ainsi que votre endpoint de l’API REST de Certona.

{% raw %}
```liquid
{% connected_content <INSERT_CERTONA_REST_API_KEY> :save recommendations %}
```

Définissez ensuite le contenu que vous souhaitez appeler comme les images ou le texte pertinents. Par exemple, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Image d’une campagne de notifications push avec le Contenu connecté apparenté de Certona inclus dans le corps du message.][1]

Une fois que vous avez placé ce message dans le corps de l’éditeur, prévisualisez votre appel de Contenu connecté pour vous assurer que vous avez affiché les informations correctes.

![Image montrant l’onglet « Test », encourageant les utilisateurs à tester minutieusement leur message avant de l’envoyer.][2]

[1]: {% image_buster /assets/img/certona.png %}
[2]: {% image_buster /assets/img/certona2.png %}