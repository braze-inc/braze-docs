---
nav_title: Crowdin
article_title: Crowdin
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Crowdin, une plateforme logicielle basée sur le nuage qui vous permet d'automatiser la traduction de vos modèles de courrier électronique et de vos blocs de contenu en Brésil."
alias: /fr/partners/crowdin/
page_type: partenaire
search_tag: Partenaire
---

# Crowdin

> Crowdin est un logiciel basé sur le nuage pour la gestion des traductions. En utilisant Crowdin, vous pouvez traduire vos applications Android et iOS, votre site Web, vos captures d'écran et tout autre contenu. La traduction peut se faire par l'intermédiaire de votre équipe, d'une agence de traduction ou par l'intermédiaire de moteurs de traduction automatiques.

L'intégration de Braze et Crowdin vous permet de traduire des modèles d'e-mail et des blocs de contenu. Vous pouvez également synchroniser le contenu de votre compte Braze vers votre projet Crowdin et ajouter des traductions vers Braze.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                                                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Crowdin                  | Un [compte Crowdin](https://accounts.crowdin.com/register) est requis pour profiter de ce partenariat.                                                                                                                                                                                                                     |
| Projet de traduction Crowdin    | Pour connecter votre compte Braze à Crowdin ou à Crowdin Enterprise, vous devrez d'abord vous inscrire et créer un projet de traduction.                                                                                                                                                                                   |
| Braze clé API REST              | Une clé API Braze REST avec tous les modèles et les autorisations de blocs de contenu. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__                                                                                   |
| Point de terminaison REST Braze | Votre URL de terminaison REST à l'exclusion de "https://". Par exemple, si votre endpoint est `https://rest.fra-01.braze.eu`, vous fournirez `de repos à Crowdin. ra-01.braze.eu`.<br><br>Votre point de terminaison dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Configurez l'application Braze dans Crowdin/Crowdin Enterprise

#### Crowdin
Pour configurer l'application Braze dans Crowdin, suivez ces étapes:

1. Rendez-vous sur l'application [Braze sur la place de marché](https://crowdin.com/resources#marketplace/braze).
2. Cliquez sur **Installer** pour l'ajouter à votre compte.
3. Ouvrez le projet que vous avez créé pour votre localisation de contenu Braze.
4. Allez dans l'onglet **Paramètres > Intégrations**.
5. Dans la section **Applications** , cliquez sur l'application Braze.
6. Dans la boîte de dialogue, fournissez vos identifiants Braze (Braze REST API Key et Braze REST Endpoint).
7. Cliquez sur **Connectez-vous avec Braze Connector**.

#### Entreprise Crowdin
Pour configurer l'application Braze dans Crowdin Enterprise, suivez ces étapes :

1. Allez sur la page d'accueil **Espace de travail** > **Place de marché**.
2. Cliquez sur **Installer** sur l'application Braze pour l'ajouter à votre organisation.
3. Ouvrez le projet que vous avez créé pour votre localisation de contenu Braze.
4. Allez dans **Applications > Personnalisées**.
5. Cliquez sur l'application Braze.
6. Dans la boîte de dialogue, fournissez vos identifiants Braze (Braze REST API Key et Braze REST Endpoint).
7. Cliquez sur **Connectez-vous avec Braze Connector**.

### Étape 2 : Ajoutez votre contenu à Crowdin/Crowdin Enterprise

Une fois que vous aurez fourni vos identifiants Braze, vous verrez deux panneaux. Sélectionnez le contenu souhaité sur le panneau de droite pour synchroniser les fichiers à traduire depuis votre compte Braze et cliquez sur **Synchroniser vers Crowdin**.

En mode Éditeur dans Crowdin, le contenu synchronisé à partir de votre compte Braze peut être affiché à vos traducteurs comme une liste de chaînes ou comme un aperçu de fichier.

!\[Aperçu du courriel de l'éditeur Crowdin\]\[2\]

### Étape 3 : Ajouter des traductions à Braze

Dès que les traductions sont terminées, ouvrez l'application Braze dans Crowdin, sélectionnez les fichiers traduits (pour chaque fichier, vous pouvez choisir soit toutes les langues cibles ou seulement les langues spécifiques) dans le panneau de gauche, et cliquer sur **Synchroniser pour Braze**.

!\[Synchroniser les traductions à Braze\]\[3\]
[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %} [2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %} [3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
