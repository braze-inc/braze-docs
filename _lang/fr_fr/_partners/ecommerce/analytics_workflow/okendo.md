---
nav_title: Okendo
article_title: "Okendo"
description: "Apprenez à intégrer Okendo avec Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) est une plateforme unifiée de marketing client qui fournit des outils pour cultiver l'engagement, développer le bouche-à-oreille et maximiser la valeur vie client afin de mobiliser vos clients pour une croissance plus rapide et plus efficace.

*Cette intégration est maintenue par Okendo.*

## À propos de l'intégration

L'intégration de Braze avec Okendo fonctionne sur plusieurs produits de la plateforme d'Okendo, notamment les évaluations, la fidélisation, les recommandations, les enquêtes et les quiz. Okendo envoie des événements personnalisés et des attributs clients à Braze, qui peuvent être utilisés pour personnaliser et déclencher des messages.  

## Conditions préalables

| Condition            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Compte Okendo         | Un compte Okendo est nécessaire pour bénéficier de ce partenariat.        |
| Clé d'API REST Braze     | Une clé API Braze REST avec des autorisations `users.track`. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze    | [L'URL de votre endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mise en place du connecteur Braze dans Okendo

1. Dans Okendo, allez dans **Paramètres** > **Intégrations** > **E-mail & SMS** > **Braze**
2. Ajoutez le point de terminaison de l'API et la clé API aux paramètres d'**intégration**.

### Étape 2 : Configurez votre identifiant

Le champ `external_id` est utilisé pour identifier l'utilisateur associé à chaque événement. Basculez sur **Utiliser l'ID du client Shopify pour l'identification de l'utilisateur de Braze** afin d'associer le champ aux ID des clients Shopify. Sinon, basculez-la pour l'associer à l'adresse e-mail de chaque utilisateur.

## Synchronisation des événements et des attributs d'Okendo avec Braze

### Événements personnalisés

{% alert note %}
Pour des exemples de données d'événements, reportez-vous à la [documentation d'Okendo](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c).
{% endalert %}

#### Événements de révision

- Revue Okendo Créée
- Demande de révision d'Okendo

#### Événements de recommandation

- Envoi d'une recommandation à Okendo
- Abonné aux recommandations d'Okendo
- Invitation à la recommandation d'Okendo
- Coupon de recommandation Okendo reçu
- Coupon de recommandation Okendo reçu
- Rejet de la recommandation d'Okendo

#### Événements de fidélisation

- Inscription au programme Okendo Loyalty
- Points de fidélité Okendo attribués
- Points de fidélité Okendo échangés
- Changement du niveau de loyauté d'Okendo
- Ajustement des points de fidélité Okendo

#### Enquête

- Enquête soumise par Okendo

#### Quiz

- Quiz Okendo soumis

### Attributs personnalisés

Okendo envoie les données du profil utilisateur sous forme d'attributs personnalisés dans Braze, qui peuvent être utilisés pour créer des segments d'audience. En voici quelques exemples :

- Questions de profil posées dans les enquêtes et lors de la soumission d'un examen, telles que l'âge, la date d'anniversaire, le type de peau et la couleur des cheveux.
- Indicateurs d'évaluation tels que la _note moyenne d'évaluation_ et le _sentiment moyen d'évaluation_
- Indicateurs de fidélisation tels que le _solde de points_ et le _niveau VIP_
- Indicateurs de recommandation tels que le _nombre de recommandations réussies_ et le _chiffre d'affaires total des recommandations_.  
- Score Net Promoter Score collecté à partir d'une enquête

## Utilisation de Braze avec les produits Okendo

En fonction du produit Okendo, vous devez effectuer des étapes supplémentaires pour utiliser Braze et Okendo ensemble. Reportez-vous aux articles suivants pour plus de détails :

- [Intégration des évaluations dans Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Intégration de la fidélisation avec Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Intégration des recommandations avec Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Intégration des enquêtes avec Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Intégration des jeux-questionnaires dans Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Pour obtenir de l'aide sur la configuration de l'intégration, contactez l'équipe d'assistance d'Okendo.
{% endalert %}
