---
nav_title: Nift
article_title: Nift
description: "Cet article de référence présente le partenariat entre Braze et Nift, une plateforme bilatérale qui aide les entreprises à acquérir, engager et fidéliser leurs clients."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) aide les entreprises à acquérir, engager et fidéliser leurs clients. La plateforme bilatérale aide les partenaires à remercier leurs clients avec des cartes-cadeaux Nift. Remercier les clients augmente leur valeur à vie et génère des revenus supplémentaires.

_Cette intégration est maintenue par Nift._

## À propos de l'intégration

L'intégration entre Braze et Nift vous permet de déclencher automatiquement des "remerciements" contenant des cadeaux Nift à des moments clés du cycle de vie du client et d'identifier les clients qui ont utilisé leur cadeau. Les cartes-cadeaux Nift peuvent être utilisées pour accéder à des produits et services fournis par des marques qui s'appuient sur la technologie de mise en relation de Nift pour acquérir de nouveaux clients de manière rentable à l'échelle.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Nift | Un compte Nift est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les autorisations relatives aux données de l'utilisateur. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Se connecter à Braze dans Nift

Rendez-vous sur votre [tableau de bord Nift](https://www.gonift.com/users/sign_in), naviguez vers **Comptes** > **Intégrations** > **Braze**, et cliquez sur **Connecter**.

### Étape 2 : Ajouter les informations de connexion de Braze

Sur la page **Lier votre compte Braze**, indiquez votre clé API REST Braze et sélectionnez votre endpoint Braze, qui dépendra de l'URL Braze de [votre instance]({{site.baseurl}}/api/basics/#endpoints).

Vous pouvez modifier le nom du paramètre ID du client dans le lien de recommandation envoyé à vos clients. Nift l'utilisera pour marquer vos clients comme traités dans Braze lorsqu'ils ont choisi un cadeau de l'une de nos marques.

Cliquez sur **Lier le compte**.

![" Page d'intégration du service Nift demandant à l'utilisateur la clé API de Braze et l'URL du tableau de bord de Braze ".]({% image_buster /assets/img/nift/link_your_braze_account.png %}).

## Utilisation de l'intégration

Pour utiliser l'intégration, distribuez le lien de recommandation dans vos messages. Lorsque votre client utilise le lien de recommandation et sélectionne un cadeau de l'une de nos marques, Nift le marque comme traité dans Braze.

Après l'intégration avec Braze, Nift poussera automatiquement les événements vers l'enregistrement Braze du client existant avec les données suivantes :

- Nom de l'événement : `nift_processed`
- Heure : Le moment où le client a choisi/utilisé le cadeau



