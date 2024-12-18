---
nav_title: Migration vers Firebase Cloud Messaging
article_title: "Migration vers l'API d'envoi de messages de Firebase Cloud"
platform: Android
page_order: 29
description: "Cet article explique comment migrer de l'API obsolète Cloud Messaging de Google vers Firebase Cloud Messaging (FCM)."
channel:
  - push
search_rank: 3
---

# Migration vers l'API d'envoi de messages de Firebase Cloud

> Découvrez comment migrer de l'API obsolète Cloud Messaging de Google vers l'API Firebase Cloud Messaging (FCM), laquelle est entièrement prise en charge. Pour plus d’informations, consultez la [FAQ de Google sur Firebase (2023)](https://firebase.google.com/support/faq#fcm-23-deprecation).

{% alert important %}
Si c'est la première fois que vous configurez l'intégration push pour Android, consultez plutôt [Intégration push standard pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration).
{% endalert %}

## Limite de débit

L'API Firebase Cloud Messaging (FCM) présente une limite de débit par défaut de 600 000 requêtes par minute. Si vous atteignez cette limite, Braze réessaiera automatiquement dans quelques minutes. Pour demander une augmentation, contactez le [service d'assistance de Firebase.](https://firebase.google.com/support)

## Migration vers l’API FCM

### Étape 1 : Vérifiez votre ID de projet

D’abord, ouvrez Google Cloud. Sur la page d'accueil de votre projet, vérifiez le numéro figurant dans le champ **Project ID** \- vous le comparerez ensuite à celui de votre projet Firebase.

![La page d'accueil du projet Google Cloud avec l'"ID du projet" en surbrillance.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

Ensuite, ouvrez la console Firebase, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu Paramètres ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Dans l'onglet **Général**, vérifiez que l'**ID du projet** correspond à celui indiqué dans votre projet Google Cloud.

![La page "Settings" du projet Firebase avec l'"ID du projet" en surbrillance.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### Étape 2 : Vérifiez votre ID d'expéditeur

Tout d'abord, ouvrez Braze, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres des applications**.

![Le menu Paramètres s'ouvre dans Braze avec « Paramètres des applications » en surbrillance.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

Dans les **paramètres de notification push** de votre application Android, vérifiez le numéro du champ **ID de l’expéditeur de Firebase Cloud Messaging**. Vous le comparerez ensuite à celui de votre projet Firebase.

![Formulaire pour les paramètres de notifications push.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

Ensuite, ouvrez la console Firebase, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu Paramètres ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez l'**envoi de messages dans le nuage**. Sous **Cloud Messaging API (Legacy)**, vérifiez que l'**ID de l'expéditeur** correspond à celui répertorié dans votre tableau de bord Braze.

![La page Messagerie Cloud du projet Firebase avec l'ID de l'expéditeur mis en évidence.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### Étape 3 : Activez l'API d'envoi de messages de Firebase Cloud.

Dans Google Cloud, sélectionnez le projet utilisé par votre application Android, puis activez l'[API Firebase Cloud Messaging](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![API Firebase Cloud Messaging activée]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Étape 4 : Créer un compte de service

Ensuite, créez un nouveau compte de service, afin que Braze puisse effectuer des appels API autorisés lors de l'enregistrement des jetons FCM. Dans Google Cloud, sélectionnez **Service Accounts (Comptes de service)**, puis choisissez votre projet. Sur la page **Comptes de service**, sélectionnez **Créer un compte de service**.

![Page d'accueil du compte de service d'un projet avec l'option "Créer un compte de service" en surbrillance.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Saisissez un nom de compte de service, un ID et une description, puis sélectionnez **Create and continue (Créer et continuer)**.

![Le formulaire "Détails du compte de service".]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

Dans le champ **Rôle**, recherchez et sélectionnez **Firebase Cloud Messaging API Admin** dans la liste des rôles. Pour un accès plus restrictif, créez un [rôle personnalisé](https://cloud.google.com/iam/docs/creating-custom-roles) avec l'autorisation `cloudmessaging.messages.create`, puis choisissez-le dans la liste. Lorsque vous avez terminé, sélectionnez **Terminé**.

{% alert warning %}
Veillez à sélectionner _Firebase Cloud Messaging **API** Admin_, et non _Admin Firebase Cloud Messaging_.
{% endalert %}

![Formulaire « Grant this service account access to project » (Accorder à ce compte de service l'accès au projet) avec « Admin API Firebase Cloud Messaging » sélectionné comme rôle.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Étape 5 : Vérifier les autorisations (facultatif)

Pour vérifier les autorisations dont dispose votre compte de service, ouvrez Google Cloud, puis accédez à votre projet et sélectionnez **MESSAGE IN-APP**. Sous **View By Principals (Vue par principes)**, sélectionnez **Excess Permissions (Autorisations excédentaires)**.

![L'onglet "Vue par principes" avec le nombre de permissions excédentaires listées pour chaque principal.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

Vous pouvez à présent consulter les autorisations actuelles attribuées au rôle que vous avez sélectionné.

![La liste des autorisations actuelles attribuées au rôle sélectionné.]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### Étape 6 : Générer des identifiants JSON

Ensuite, générez les identifiants JSON pour votre compte de service FCM. Dans Google Cloud IAM & Admin, sélectionnez **Service Accounts (Comptes de service)**, puis choisissez votre projet. Recherchez le compte de service FCM [que vous avez créé précédemment](#step-4-create-a-service-account), puis sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Manage Keys (Gérer les clés)**.

![Page d'accueil du compte de service du projet avec le menu "Actions" ouvert.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Sélectionnez **Ajouter une clé** > **Créer une nouvelle clé**.

{% alert note %}
La création d'une nouvelle clé ne supprime pas les anciennes. Si vous supprimez accidentellement votre nouvelle clé en sélectionnant **Revert Credentials**, Braze utilisera vos anciennes clés comme sauvegarde.
{% endalert %}

![Le compte de service sélectionné avec le menu "Ajouter une clé" ouvert.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Choisissez **JSON**, puis sélectionnez **Create (Créer)**. Si vous avez créé votre compte de service en utilisant un ID de projet Google Cloud différent de votre ID de projet FCM, vous devrez mettre à jour manuellement la valeur attribuée à l'adresse `project_id` dans votre fichier JSON.

N'oubliez pas l'endroit où vous avez téléchargé la clé : vous en aurez besoin à l'étape suivante.

![Le formulaire de création d'une clé privée avec "JSON" sélectionné.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Les clés privées peuvent présenter un risque de sécurité si elles sont compromises. Conservez vos identifiants JSON dans un emplacement/localisation sécurisé pour l'instant : vous supprimerez votre clé après l'avoir téléchargée sur Braze.
{% endalert %}

### Étape 7 : Téléchargez vos informations d'identification JSON vers Braze.

Dans Braze, sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres des applications**.

![Le menu Paramètres s'ouvre dans Braze avec « Paramètres des applications » en surbrillance.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Sous **Paramètres de notification push**, sélectionnez **Télécharger un fichier JSON**, puis choisissez le fichier [que vous avez généré précédemment](#step-6-generate-json-credentials). Lorsque vous avez terminé, sélectionnez **Enregistrer.**

![Formulaire des paramètres de notification push avec la clé privée mise à jour dans le champ « Firebase Cloud Messaging Server Key » (Clé du serveur Firebase Cloud Messaging).]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Les clés privées peuvent présenter un risque de sécurité si elles sont compromises. Maintenant que votre clé est téléchargée sur Braze, supprimez de votre ordinateur le fichier [que vous avez généré précédemment](#step-6-generate-json-credentials).
{% endalert %}

### Étape 8 : Testez vos nouvelles informations d'identification (facultatif)

Dès que vous avez téléchargé vos identifiants sur Braze, vous pouvez commencer à envoyer des notifications push à l'aide de vos nouveaux identifiants. Pour tester vos nouveaux identifiants, envoyez une notification push réelle ou de test à votre appli à l'aide de FCM ou de Braze. Si la notification push passe, tout fonctionne. Si ce n'est pas le cas :

- [Vérifiez votre ID d'expéditeur](#step-2-verify-your-sender-id)
- [Vérifiez vos autorisations](#step-5-verify-permissions-optional)
- Examinez les erreurs de notification push dans le [journal d'activité de votre message.]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)

Si vous rencontrez toujours des difficultés, reportez-vous à la section [Réinitialisation de vos données d'identification](#reverting-your-credentials).

## Réinitialisation de vos identifiants

Vous pouvez à tout moment supprimer vos nouvelles informations d'identification et restaurer vos anciennes informations d'identification. Dès que vos identifiants sont restaurés, vous pouvez commencer à envoyer des notifications push en utilisant vos anciens identifiants à la place.

Dans Braze, sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres des applications**. Sous **Paramètres de notification push**, sélectionnez **Rétablir les informations d'identification**.

{% alert warning %}
Si vous supprimez vos nouvelles données d'identification, vous ne pourrez pas les restaurer ultérieurement. Vous devrez [générer de nouveaux identifiants](#step-6-generate-json-credentials) et les [charger à nouveau](#step-7-upload-your-json-credentials-to-braze) dans Braze.
{% endalert %}

![Formulaire « Paramètres de notifications push » avec le bouton « Rétablir les identifiants » en surbrillance.]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## Foire aux questions (FAQ) {#faq}

### Comment puis-je savoir si mes nouvelles informations d'identification fonctionnent ?

Vos nouveaux identifiants commencent à fonctionner dès que vous les téléchargez sur Braze. Pour les tester, sélectionnez **Tester les informations d'identification**. Si vous obtenez une erreur, vous pouvez toujours [rétablir vos identifiants](#reverting-your-credentials).

### Dois-je migrer vers la FCM pour mes applications non utilisées ou mes applications de développement ?

Non. Toutefois, vos applications inutilisées et vos applications de développement continueront d'afficher un message in-app vous demandant de procéder à la migration. Pour supprimer ce message, vous pouvez soit télécharger de nouvelles informations d'identification, soit supprimer ces applications de votre espace de travail. Si vous choisissez de supprimer ces apps, veillez à vérifier d'abord auprès de votre équipe au cas où quelqu'un les utiliserait.

### Où puis-je consulter les messages d'erreur ?

Vous pouvez consulter les erreurs de notification push dans le [journal d'activité de votre message.]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)

### Avant la migration, dois-je mettre à jour mon application ou mon SDK ?

Non. Il vous suffit de télécharger vos nouvelles informations d'identification sur Braze.

### Dois-je d'abord supprimer mes anciens identifiants ?

Non. Si vous devez supprimer vos nouvelles données d'identification, [vous pouvez utiliser vos anciennes données d'identification](#reverting-your-credentials).

### Après la migration, pourquoi y a-t-il encore un message d'avertissement dans Braze ?

Vous continuerez à voir ce message in-app s'il y a au moins une application Android dans votre espace de travail que vous devez encore migrer. Veillez à migrer toutes vos applications Android vers l'API FCM entièrement prise en charge par Google.

### Après la migration, combien de temps dois-je attendre avant d'envoyer à nouveau des notifications push ?

Après la migration, vous pouvez commencer à envoyer des notifications push en utilisant vos nouvelles informations d'identification immédiatement.

### Que se passe-t-il si j'ai créé mon compte de service en utilisant un projet différent de mon projet FCM ?

Si vous avez créé votre compte de service en utilisant un ID de projet Google Cloud différent de votre ID de projet FCM, vous devrez mettre à jour manuellement la valeur attribuée à l'adresse `project_id` dans votre fichier JSON après en avoir [créé un nouveau.](#step-6-generate-json-credentials)
