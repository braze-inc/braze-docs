---
nav_title: Dixa
article_title: Dixa
description: "Cet article présente le partenariat entre Braze et Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) est une plateforme de service client personnalisée pour améliorer les expériences d'assistance en unifiant les canaux de communication tels que le chat, l'e-mail, le téléphone et les réseaux sociaux en une seule interface. Elle aide les décisions à améliorer la satisfaction des clients et l'efficacité grâce au timing intelligent, à l'automatisation et aux informations sur les performances en temps réel.

L'intégration de Braze et Dixa offre une meilleure vue sur tous vos utilisateurs en fournissant aux agents du service client des données Braze en temps réel.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Dixa        | Un compte administrateur Dixa est nécessaire pour bénéficier de ce partenariat.                                                                                           |
| Une clé de l'API REST de Braze  | Une clé API REST Braze avec les autorisations `users.export.ids` et `email.status`.<br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

Surfacez les données de Braze dans la vue de l'agent du service client tout en communiquant avec vos utilisateurs sur différents canaux de communication, tels que l'e-mail, la messagerie ou le chat.

## Intégration

Vous devez être un administrateur Dixa pour configurer les intégrations dans Dixa. Pour l'intégration de Braze, dans Dixa, allez dans **Paramètres** > **Intégrations** > **Braze**.

![][1]{: style="width:450px;"}

### Étape 1 : Créer l'intégration à Dixa

Sur la page **Créer un widget Braze**, remplissez les champs obligatoires suivants pour créer l'intégration :

- **Nom du widget :** Il s'agit du nom de l'intégration qui sera utilisé ultérieurement dans la barre latérale de conversation comme titre.
- **URL DE L'API :** Il s'agit de l'URL de l'endpoint de l'API REST de Braze pour votre instance.
- **Clé API :** Il s'agit de la clé API Braze que vous avez créée dans les conditions préalables.

### Étape 2 : Configurer l'intégration

Configurez ensuite l'intégration de Braze et Dixa. Choisissez parmi les options suivantes pour ajuster l'affichage du widget Braze dans la barre latérale de conversation.

#### Afficher le widget dans la barre latérale de conversation

Ce paramètre permet d'afficher ou de masquer l'ensemble de l'intégration dans la barre latérale des conversations dans Dixa. 

Si vous êtes en train de configurer activement l'intégration, nous vous recommandons de désactiver cette option pendant que vous remplissez les champs obligatoires. Une fois la configuration terminée, vous pouvez la réactiver et les agents Dixa peuvent utiliser l'intégration.

#### Afficher les coordonnées du client

Choisissez d'afficher ou de masquer les détails de l'utilisateur. Les détails contiennent des données sur l'emplacement/localisation, l'e-mail, le numéro de téléphone, l'état de l'abonnement à l'e-mail, l'état de l'abonnement à la notification push et la durée de l'adhésion à Braze. 

#### Affichez le bouton permettant de modifier l'état de l'abonnement à l'e-mail.

Les boutons sont basés sur l'un des trois états d'abonnement de Braze : `subscribed`, `opted-in`, et `unsubscribed`. Si un utilisateur est `subscribed`, l'agent peut choisir `opt-in` ou `unsubscribe`. Lorsqu'un utilisateur est `opted-in` ou `unsubscribed`, il est seulement possible de passer de l'un à l'autre.

#### Afficher une liste d'attributs personnalisés

Choisissez d'afficher ou de masquer les attributs personnalisés de Braze de l'utilisateur.

#### Afficher une liste d'événements personnalisés

Choisissez d'afficher ou de masquer les événements personnalisés de Braze de l'utilisateur.

#### Afficher une liste d'achats

Choisissez d'afficher ou de masquer la liste des produits achetés par l'utilisateur. Ici, vous pouvez voir combien de fois il a été acheté. Pour afficher la première et la dernière date d'achat, survolez l'article. 

### Exemple d’intégration

Vous trouverez ci-dessous un exemple d'intégration :

![L'intégration de Braze et Dixa dans Dixa qui affiche l'état de l'abonnement à l'e-mail d'un utilisateur, ses attributs personnalisés, ses événements personnalisés et ses achats.][2]{: style="width:350px;"}

[1]: {% image_buster /assets/img/dixa/dixa-create-integration.png %}
[2]: {% image_buster /assets/img/dixa/dixa-braze-integration.png %}