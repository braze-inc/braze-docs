---
nav_title: Nift
article_title: Nift
description: "Cet article de référence décrit le partenariat entre Braze et Nift, une plateforme bilatérale qui aide les entreprises à acquérir, engager et fidéliser des clients."
alias: /partners/nift/
page_type: partner
search_tag: Partenaire

---

# Nift

> [Nift](https://gonift.com/) aide les entreprises à acquérir, engager et fidéliser des clients. La plateforme bilatérale aide les partenaires à remercier leurs clients à l’aide des cartes-cadeaux Nift. Remercier les clients augmente leur valeur à vie et génère des revenus supplémentaires.

L’intégration de Braze et Nift vous permet de déclencher automatiquement des messages de « remerciements » contenant des cadeaux Nift à des moments clés du cycle de vie du client, ainsi que d’identifier les clients qui ont utilisé leur cadeau. Les cartes-cadeaux Nift peuvent être utilisées pour accéder aux produits et aux services fournis par les marques qui s’appuient sur la technologie de mise en relation de Nift pour acquérir de nouveaux clients de manière rentable et à grande échelle.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Nift | Un compte Nift est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec toutes les autorisations pour les données utilisateur. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Connecter Braze dans Nift

Rendez-vous sur votre [tableau de bord Nift][2], accédez à **Accounts (Comptes)** > **Integrations (Intégrations)** > **Braze** et cliquez sur **Connect (Connecter)**.

### Étape 2 : Ajouter des identifiants Braze

Sur la page **Link your Braze Account (Lier votre compte Braze)**, fournissez votre clé API REST de Braze et sélectionnez votre endpoint Braze, qui dépendra de l’URL Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints).

Vous pouvez modifier le nom du paramètre ID client dans le lien de recommandation envoyé à vos clients. Nift l’utilisera pour marquer vos clients comme ayant été traités dans Braze lorsqu’ils auront sélectionné un cadeau de l’une de nos marques.

Cliquez sur **Link Account (Lier le compte)**.

![Page d’intégration du service Nift demandant à l’utilisateur la clé d’API Braze et l’URL du Tableau de bord de Braze.][5]

## Comment utiliser l’intégration

Pour utiliser l’intégration, distribuez le lien de recommandation dans votre communication. Lorsque votre client utilise le lien de recommandation et sélectionne un cadeau de l’une de nos marques, Nift l’indiquera comme ayant étant traité dans Braze.

Après l’intégration à Braze, Nift transmettra automatiquement les événements de notification push au dossier Braze du client existant avec les données suivantes :

- Nom de l’événement : `nift_processed`
- Date : Heure à laquelle le client a sélectionné/used le cadeau


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.gonift.com/users/sign_in
[5]: {% image_buster /assets/img/nift/link_your_braze_account.png %}
[6]: {% image_buster /assets/img/nift/braze_account_linked.png %}