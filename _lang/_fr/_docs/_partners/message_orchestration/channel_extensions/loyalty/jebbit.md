---
nav_title: Jebbit
article_title: Jebbit
page_order: 4
description: "Cet article décrit le partenariat entre Braze et Jebbit, un PaaS qui vous permet de passer des courriels et des attributs d'utilisateurs de vos campagnes Jebbit en tant que données utilisateur à Braze en temps réel."
alias: /fr/partners/jebbit/
page_type: partenaire
search_tag: Partenaire
---

# Jebbit

> [Jebbit](https://www.jebbit.com/) est une PaaS qui vous permet de construire des expériences engageantes pour les utilisateurs de saisir des données de premier groupe.

L'intégration de Braze et Jebbit vous permet de passer des courriels et des attributs utilisateurs de vos campagnes Jebbit en tant que données utilisateur à Braze en temps réel. Ces données peuvent ensuite être utilisées pour stimuler des initiatives de marketing telles que des campagnes de courriel personnalisées et des déclencheurs.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Jebbit                   | Un compte Jebbit est requis pour profiter de ce partenariat.                                                                                                                                                                   |
| Braze clé API REST              | Une clé API Braze REST avec toutes les autorisations de données utilisateur. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL Braze pour [votre instance](https://www.braze.com/docs/api/basics/#endpoints).                                                                     |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Lorsque vous demandez une intégration avec Jebbit, communiquez si des délais durs doivent être respectés. De plus, assurez-vous que vous avez les attributs associés à votre ou vos expériences Jebbit que vous aimeriez passer à Braze.

### Étape 1 : Fournir les identifiants API

Fournissez vos identifiants API à Jebbit dans un fichier texte via une demande de fichier Dropbox. Soumettez votre fichier en utilisant l'URL [Dropbox](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx) suivante.

### Étape 2 : Confirmer la soumission du test

Un ingénieur Jebbit assigné à votre intégration poussera une soumission de test de Jebbit à Braze, pour que vous puissiez voir à quoi ressembleront les données dans votre environnement Braze. C'est la dernière étape de l'activation de l'intégration. Maintenant que vos données Jebbit sont configurées, utilisez-les pour mener vos initiatives de marketing.

{% alert note %}
L'ID d'attribut que vous avez défini dans Jebbit est la façon dont le nom du champ d'attribut sera affiché en Brésil.
{% endalert %}

## Personnalisation

Nous supportons actuellement les points de terminaison [des données utilisateur]({{site.baseurl}}/api/endpoints/user_data/) de manière spécifique, mais les requêtes pour différents points de terminaison peuvent être prises en charge. Les noms des champs d'attributs peuvent également être personnalisés selon vos préférences.

Si vous voulez des attributs supplémentaires de Jebbit au Brésil, mappez le nouvel attribut dans votre compte Jebbbit. L'attribut s'affichera automatiquement dans Braze lorsque vous collecterez des données pour cet attribut.
