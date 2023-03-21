---
nav_title: Jebbit
article_title: Jebbit
page_order: 4
description: "Cet article de référence présente le partenariat entre Braze et Jebbit, une PaaS qui vous permet de transmettre les e-mails et les attributs des utilisateurs de vos campagnes Jebbit en tant que données utilisateur à Braze en temps réel."
alias: /partners/jebbit/
page_type: partner
search_tag: Partenaire

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) est une PaaS qui vous permet de créer des expériences engageantes pour les utilisateurs afin de capturer des données first-party.

L’intégration entre Braze et Jebbit permet de transmettre les e-mails et les attributs de vos campagnes Jebbit en tant que données utilisateur à Braze en temps réel. Ces données peuvent ensuite être utilisées pour piloter des initiatives marketing telles que des campagnes et des déclencheurs d’e-mails personnalisés. 

## Conditions préalables

| Condition | Description |
|---|---|
|Compte Jebbit | Un compte Jebbit est nécessaire pour tirer parti de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec toutes les autorisations pour les données utilisateur. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
|Endpoint REST de Braze | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Lorsque vous demandez l’intégration à Jebbit, communiquez si des délais serrés doivent être respectés. De plus, assurez-vous que vous disposez des attributs mappés à votre ou vos expériences Jebbit que vous souhaitez transmettre à Braze.

### Étape 1 : Fournir les identifiants API

Fournissez vos identifiants API à Jebbit dans un fichier texte via une demande de fichier Dropbox. 
Envoyez votre fichier en utilisant l’[URL Dropbox](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx) suivant.

### Étape 2 : Confirmer l’envoi d’un test

Un ingénieur Jebbit affecté à votre intégration effectuera un envoi de test de Jebbit à Braze, afin que vous puissiez voir comment les données se présentent dans votre environnement Braze. C’est l’étape finale pour activer l’intégration. Maintenant que vos données Jebbit sont configurées, utilisez-les pour mener vos initiatives marketing.

{% alert note %}
L’ID de l’attribut que vous avez défini dans Jebbit est la façon dont le nom du champ de l’attribut sera affiché dans Braze.
{% endalert %}

## Personnalisation

Nous prenons actuellement en charge spécifiquement les endpoints des [données utilisateur]({{site.baseurl}}/api/endpoints/user_data/), mais les demandes pour des endpoints différents peuvent être prises en charge.
Les noms des champs d’attributs peuvent également être personnalisés selon vos préférences.

Si vous souhaitez obtenir des attributs supplémentaires de Jebbit à Braze, mappez le nouvel attribut sur votre compte Jebbit. L’attribut s’affiche automatiquement dans Braze lorsque vous collectez des données pour cet attribut.
