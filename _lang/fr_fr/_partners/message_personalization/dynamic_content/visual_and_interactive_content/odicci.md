---
nav_title: Odicci
article_title: Odicci
description: "Guide étape par étape de l'intégration d'Odicci avec Braze pour des campagnes de marketing personnalisées."
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Intégration d'Odicci à Braze

> Découvrez comment intégrer Braze à [Odicci](https://www.odicci.com/), une plateforme qui donne aux entreprises les moyens d'acquérir, d'engager et de fidéliser leurs clients grâce à des expériences omnicanales axées sur la fidélisation.

{% alert tip %}
Consultez le [Centre d'aide Odicci](https://help.odicci.com) pour obtenir des ressources supplémentaires et des FAQ.
{% endalert %}

## Cas d’utilisation

Vous pouvez connecter la plateforme Odicci à Braze pour un partage fluide/sans heurts/de façon homogène des données et la gestion des campagnes, ce qui inclut :

- Envoi automatique à Braze des données d'audience collectées dans les expériences Odicci.
- Déclencher des campagnes de marketing personnalisées en fonction des interactions avec les utilisateurs.
- Mappage des champs entre Odicci et Braze pour assurer une synchronisation précise des données.

## Exemple

Un retailing utilise les expériences gamifiées d'Odicci pour collecter des adresses e-mail en vue d'une campagne marketing.

1. Un client termine un jeu dans Odicci, en fournissant son adresse e-mail.
2. Odicci synchronise automatiquement ces données avec Braze.
3. Braze déclenche un e-mail de remerciement personnalisé et inclut un code de réduction.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis             | Description                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un récit d'Odicci            | Un compte Odicci avec accès à la section **Intégrations** est nécessaire pour profiter de ce partenariat.|
| Clé d'API REST Braze        | Une clé API REST de Braze avec les autorisations `users.track` et 'campaigns.list'. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration d'Odicci

### Étape 1 : Activez l'intégration dans Odicci

1. Connectez-vous à votre compte Odicci.
2. Accédez à la section **Paramètres > Intégrations**.
3. Recherchez l'intégration **Braze** et cliquez sur **Connecter**.

   ![Connect Braze Integration]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Saisissez votre clé API REST Braze dans le champ prévu à cet effet.
5. Enregistrez les paramètres pour activer l'intégration au niveau du compte.

### Étape 2 : Obtenez votre clé API REST de Braze

1. Connectez-vous à votre compte Braze.
2. Allez dans la **console de développement > REST API Keys**.
3. Créez une nouvelle clé API ou copiez une clé existante avec l'autorisation `users.track`.

### Étape 3 : Activer l'intégration au niveau de l'expérience

1. Créez ou ouvrez une **expérience** dans Odicci Studio.
2. Naviguez vers **Studio > Settings > Integrations.**
3. Repérez la case à cocher **Braze** et cochez-la pour activer l'intégration pour l'expérience.
4. Enregistrez vos modifications.

### Étape 4 : Champs de mappage

1. Après avoir activé l'intégration, restez dans la section **Studio > Paramètres > Intégrations**.
2. Mappez les champs de votre expérience Odicci (e.g., `Email`, `Name`) à leurs champs correspondants dans Braze.
3. Enregistrez votre configuration.

   ![Configuration du mappage des champs]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### Étape 5 : Tester l'intégration

1. Exécutez l'expérience dans Odicci pour collecter des données de test.
2. Vérifiez que les données se synchronisent correctement avec Braze en consultant le tableau de bord de Braze ou les journaux de données.
3. Assurez-vous que les champs mappés sont correctement renseignés dans Braze.

## Résolution des problèmes

Si vous rencontrez des problèmes avec l'intégration, envisagez les solutions suivantes. Pour plus d'assistance, contactez [Odicci Support.](https://help.odicci.com)

### Clé API non valide

Vérifiez à nouveau votre clé API Braze et assurez-vous qu'elle dispose des autorisations nécessaires. Ensuite, saisissez à nouveau la clé API dans les paramètres d'intégration d'Odicci.

### Les données ne sont pas synchronisées

Vérifiez que les champs de la section **Mappage des champs** sont correctement configurés. Ensuite, assurez-vous que la clé API dispose d'autorisations pour l'importation d'utilisateurs d'une donnée.

### La campagne ne se déclenche pas

Vérifiez les paramètres de la campagne Braze pour vous assurer que l'audience ou les conditions de déclenchement sont correctes.
