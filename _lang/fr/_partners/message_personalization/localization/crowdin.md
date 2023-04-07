---
nav_title: Crowdin
article_title: Crowdin
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Crowdin, une plateforme logicielle basée sur le cloud qui vous permet d’automatiser la traduction de vos modèles d’e-mail et de vos blocs de contenu dans Braze."
alias: /partners/crowdin/
page_type: partner
search_tag: Partenaire

---

# Crowdin

> Crowdin est un logiciel basé sur le cloud pour la gestion de la localisation. Grâce à Crowdin, vous pouvez traduire vos applications Android et iOS, votre site Internet, vos captures d’écran et d’autres contenus. La traduction peut être effectuée par l’intermédiaire de votre équipe interne, d’une agence de traduction ou d’un moteur de traduction par machine.

L’intégration de Braze et de Crowdin vous permet de traduire des modèles d’e-mails et des blocs de contenu. Vous pouvez également synchroniser le contenu de votre compte Braze avec votre projet Crowdin et ajouter des traductions à Braze.

## Conditions préalables

| Condition| Description|
| ---| ---|
| Compte Crowdin | Un [compte Crowdin](https://accounts.crowdin.com/register) est requis pour profiter de ce partenariat. |
| Projet de traduction Crowdin | Pour connecter votre compte Braze à Crowdin ou à Crowdin Enterprise, vous devrez d’abord vous inscrire et créer un projet de traduction. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec toutes les autorisations pour les modèles et les blocs de contenu. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint du SDK Braze | L’URL de votre endpoint SDK dépendra de l’URL Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Configurer l’application Braze dans Crowdin/Crowdin Enterprise

#### Crowdin
Pour configurer l’application Braze dans Crowdin, procédez comme suit :

1. Allez sur l’[application Braze sur le marché](https://crowdin.com/resources#marketplace/braze).
2. Cliquez sur **Install (Installer)** pour l’ajouter à votre compte.
3. Ouvrez le projet que vous avez créé pour votre localisation de contenu Braze.
4. Accédez à l’onglet **Settings (Paramètres) > Integrations (Intégrations)**.
5. Dans la section **Applications**, cliquez sur l’application Braze.
6. Dans la boîte de dialogue, fournissez vos identifiants Braze (Clé d’API REST Braze et Endpoint SDK Braze).
7. Cliquez sur **Log in with Braze Connector (Se connecter avec le connecteur Braze)**. 

#### Entreprise Crowdin
Pour configurer l’application Braze dans Crowdin Enterprise, procédez comme suit :

1. Accédez à la page d’accueil de **Workspace (Espace de travail)** > **Marketplace (Marché)**.
2. Cliquez sur **Install (Installer)** sur l’application Braze pour l’ajouter à votre organisation.
3. Ouvrez le projet que vous avez créé pour votre localisation de contenu Braze.
4. Accédez à **Applications > Custom (Personnaliser)**.
5. Cliquez sur l’application Braze.
6. Dans la boîte de dialogue, fournissez vos identifiants Braze (Clé d’API REST Braze et Endpoint SDK Braze).
7. Cliquez sur **Log in with Braze Connector (Se connecter avec le connecteur Braze)**.

### Étape 2 : Ajouter votre contenu à Crowdin/Crowdin Enterprise

Une fois que vous avez fourni vos identifiants Braze, vous verrez deux volets. Sélectionnez le contenu souhaité pour synchroniser les fichiers à traduire depuis votre compte Braze et cliquez sur **Sync to Crowdin (Sync à Crowdin)**.

Dans le mode Éditeur de Crowdin, le contenu synchronisé de votre compte Braze peut être affiché à vos traducteurs comme une liste de chaînes de caractères ou en tant qu’aperçu de fichier.

![Une image de l’éditeur d’e-mail Crowdin avec certaines traductions de base ajoutées.][2]

### Étape 3 : Ajouter des traductions à Braze

Dès que les traductions sont terminées, ouvrez l’application Braze dans Crowdin, sélectionnez les fichiers traduits (pour chaque fichier, vous pouvez choisir soit toutes les langues cibles, soit uniquement celles spécifiques) dans le volet de gauche, puis cliquez sur **Sync to Braze (Sync à Braze)**.

![Image d’un utilisateur qui sélectionne ses fichiers de traduction et les synchronise avec Braze.][3]

[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
