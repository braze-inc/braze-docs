---
nav_title: Mentionnez-moi
article_title: Intégration de Mention Me à Braze
description: "Guide de configuration de l'intégration de Mention Me"
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mentionnez-moi

> Ensemble, [Mention Me](https://www.mention-me.com/) et Braze peuvent être votre porte d'entrée pour attirer des clients haut de gamme et favoriser une fidélité inébranlable à votre marque. En intégrant de façon fluide/sans heurts les données first-party des recommandations dans Braze, vous pouvez proposer des expériences omnicanales hautement personnalisées et ciblées sur les fans de votre marque.

_Cette intégration est maintenue par Mention Me._

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Mentionnez-moi   | Un compte [Mention Me](https://mention-me.com/login) est nécessaire pour bénéficier de ce partenariat.                                                                     |
| Une clé de l'API REST de Braze  | Une clé API REST Braze avec les autorisations `users.track` et `templates.email.create`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

* Envoyez à Braze en temps réel les données réelles et les abonnements des clients référencés par Mention Me.
* Utilisez les données relatives aux recommandations pour créer des e-mails de rappel pour les coupons.
* Améliorer les performances des autres canaux de marketing en utilisant les données de recommandation pour segmenter et cibler les clients à forte valeur ajoutée.

## Quelles données sont envoyées de Mention Me à Braze ?

Lorsque vous mettez en place cette intégration, Mention Me créera automatiquement vos attributs et attributs clients et les événements - il n'est donc pas nécessaire de le faire au préalable.

Les adresses e-mail de vos clients dans Braze seront utilisées pour lier les événements personnalisés et les attributs personnalisés. Mention Me enverra des événements et des attributs de profil de contact pour tout prospect ou client existant qui déclenche cet événement via Mention Me, quel que soit son statut d'abonnement.

Pour plus de détails, reportez-vous à la section [Attributs et événements du profil de contact.](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze)

## Intégration de Mention Me

{% alert tip %}
Pour une description complète étape par étape, reportez-vous à la [documentation de configuration de Braze de Mention Me.](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me)
{% endalert %}

Intégrer Mention Me avec Braze :

1. Dans Mention Me, accédez à la page d'[intégration de Braze](https://mention-me.com/merchant/~/integrations/braze), puis sélectionnez **Connecter**.
2. Sélectionnez **Créer une nouvelle autorisation**, puis ajoutez la [clé API que vous avez précédemment créée](#prerequisites) et sélectionnez votre instance Braze.
3. Choisissez un ou plusieurs pays avec lesquels vous souhaitez vous synchroniser.
4. Lorsque vous avez terminé, sélectionnez **Connecter**.
