---
nav_title: Jebbit
article_title: Jebbit
description: "Cet article de référence présente le partenariat entre Braze et Jebbit, un PaaS qui vous permet de transmettre à Braze, en temps réel, les e-mails et attributs des utilisateurs provenant de vos campagnes Jebbit en tant que données utilisateur."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) est un PaaS qui vous permet de créer des expériences engageantes pour les utilisateurs afin de capturer des données first-party.

_Cette intégration est maintenue par Jebbit._

## À propos de l'intégration

L'intégration de Braze et Jebbit vous permet de transmettre à Braze, en temps réel, les e-mails et les attributs des utilisateurs de vos campagnes Jebbit en tant que données utilisateur. Ces données peuvent ensuite être utilisées pour piloter des initiatives marketing telles que des campagnes d'e-mail personnalisées et des déclencheurs. 

## Conditions préalables

| Condition | Description |
|---|---|
|Compte Jebbit | Un compte Jebbit est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les autorisations relatives aux données de l'utilisateur. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
|Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Lors de la requête d'intégration à Jebbit, indiquez si des délais contraignants doivent être respectés. En outre, assurez-vous que vous avez mappé les attributs de vos expériences Jebbit que vous souhaitez transmettre à Braze.

### Étape 1 : Fournir les informations d'identification de l'API

Fournissez vos identifiants API à Jebbit dans un fichier texte via une requête de fichier Dropbox.
Soumettez votre fichier en utilisant l'[URL Dropbox](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Étape 2 : Confirmer la soumission du test

Un ingénieur Jebbit affecté à votre intégration effectuera un test de soumission de Jebbit à Braze, afin que vous puissiez voir comment les données se présenteront dans votre environnement Braze. C'est la dernière étape de l'activation de l'intégration. Maintenant que vos données Jebbit sont configurées, utilisez-les pour piloter vos initiatives marketing.

{% alert note %}
L'ID de l'attribut que vous avez défini dans Jebbit correspond au nom du champ de l'attribut dans Braze.
{% endalert %}

## Personnalisation

Nous prenons actuellement en charge les endpoints de [données de l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/) en particulier, mais les requêtes pour d'autres endpoints peuvent être prises en charge.

Les noms des champs d'attribut peuvent également être personnalisés selon vos préférences.

Si vous souhaitez obtenir des attributs supplémentaires de Jebbit dans Braze, mappez le nouvel attribut dans votre compte Jebbit. L'attribut s'affichera automatiquement dans Braze au fur et à mesure que vous collecterez des données pour cet attribut.

