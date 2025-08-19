---
nav_title: Crowdin
article_title: Crowdin
description: "Cet article de référence présente le partenariat entre Braze et Crowdin, une plateforme logicielle basée sur le cloud qui vous permet d'automatiser la traduction de vos modèles d'e-mails et de vos blocs de contenu dans Braze."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin est un logiciel basé sur le cloud permettant de gérer la localisation. Grâce à Crowdin, vous pouvez traduire vos applications Android et iOS, votre site web, les captures d'écran de votre boutique et d'autres contenus. La traduction peut être effectuée par votre équipe interne, par une agence de traduction ou à l'aide de moteurs de traduction automatique.

_Cette intégration est maintenue par Crowdin._

## À propos de l'intégration

L'intégration de Braze et Crowdin vous permet de traduire les modèles d'e-mail et les blocs de contenu. Vous pouvez également synchroniser le contenu de votre compte Braze avec votre projet Crowdin et ajouter des traductions dans Braze.

## Conditions préalables

| Condition| Description|
| ---| ---|
| Compte Crowdin | Un [compte Crowdin](https://accounts.crowdin.com/register) est nécessaire pour profiter de ce partenariat. |
| Projet de traduction de Crowdin | Pour connecter votre compte Braze à Crowdin ou Crowdin Enterprise, vous devez commencer à vous inscrire et à créer un projet de traduction. |
| Clé API REST de Braze | Une clé API REST Braze avec toutes les autorisations de modèles et de blocs de contenu. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Point d'endpoint du SDK de Braze | L'URL de votre endpoint SDK dépend de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Configurer l'application Braze dans Crowdin/Crowdin Enterprise

#### Crowdin
Pour configurer l'application Braze dans Crowdin, suivez les étapes suivantes :

1. Accédez à l'[application Braze sur la place de marché](https://store.crowdin.com/braze-app).
2. Cliquez sur **Installer** pour l'ajouter à votre compte.
3. Ouvrez le projet que vous avez créé pour la localisation de votre contenu Braze.
4. Allez dans **Paramètres > onglet Intégrations**.
5. Dans la section **Applications**, cliquez sur l'application Braze.
6. Dans la boîte de dialogue, indiquez vos informations d'identification Braze (clé API REST Braze et endpoint SDK Braze).
7. Cliquez sur **Se connecter avec le connecteur Braze**. 

#### Entreprise Crowdin
Pour configurer l'application Braze dans Crowdin Enterprise, suivez les étapes suivantes :

1. Allez sur la page d'accueil de l'**Espace de travail** > **Place de marché**.
2. Cliquez sur **Installer** sur l'appli Braze pour l'ajouter à votre organisation.
3. Ouvrez le projet que vous avez créé pour la localisation de votre contenu Braze.
4. Allez dans **Applications > Personnalisé.**
5. Cliquez sur l'application Braze.
6. Dans la boîte de dialogue, indiquez vos informations d'identification Braze (clé API REST Braze et endpoint SDK Braze).
7. Cliquez sur **Se connecter avec le connecteur Braze**.

### Étape 2 : Ajoutez votre contenu à Crowdin/Crowdin Enterprise

Une fois que vous avez fourni vos informations d'identification Braze, deux panneaux s'affichent. Sélectionnez le contenu souhaité pour synchroniser les fichiers à traduire depuis votre compte Braze et cliquez sur **Synchroniser avec Crowdin**.

En mode éditeur dans Crowdin, le contenu synchronisé depuis votre compte Braze peut être affiché à vos traducteurs sous la forme d'une liste de caractères ou d'un aperçu de fichier.

![Une image de ce à quoi ressemble le compositeur d'e-mail Crowdin Editor avec quelques traductions de base ajoutées.][2]

### Étape 3 : Ajouter des traductions à Braze

Dès que les traductions sont terminées, ouvrez l'appli Braze dans Crowdin, sélectionnez les fichiers traduits (pour chaque fichier, vous pouvez choisir toutes les langues cibles ou seulement certaines) dans le panneau de gauche, et cliquez sur **Synchroniser avec Braze**.

![Une image d'un utilisateur sélectionnant ses fichiers de traduction et les synchronisant avec Braze.][3]


[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
