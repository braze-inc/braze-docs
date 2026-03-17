---
nav_title: Archivage des messages
article_title: Archivage des messages
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Cet article de référence couvre l'archivage des messages, une fonctionnalité qui vous permet de sauvegarder une copie des messages envoyés aux utilisateurs."

---

# Archivage des messages

> L'archivage des messages vous permet d'enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité dans votre compartiment AWS S3, votre conteneur Azure Blob Storage ou votre compartiment Google cloud storage. <br><br> Cet article explique comment configurer l'archivage des messages, les références de charge utile JSON et répond aux questions fréquemment posées.

L'archivage des messages est disponible en tant que fonctionnalité supplémentaire. Pour commencer à archiver vos messages, veuillez contacter votre gestionnaire de la satisfaction client Braze.

## Fonctionnement

Lorsque cette fonctionnalité est activée, si vous avez connecté un compartiment de stockage dans le cloud à Braze et l'avez marqué comme destination d'exportation de données par défaut, Braze écrira un fichier JSON gzippé dans votre compartiment de stockage dans le cloud pour chaque message envoyé à un utilisateur par le biais des canaux que vous avez sélectionnés (e-mail, SMS/MMS ou push). 

Ce fichier contiendra les champs définis sous [Références de fichier](#file-references) et reflétera les messages finaux modélisés envoyés à l'utilisateur. Toutes les valeurs modélisées définies dans votre campagne (par exemple, {% raw %}`{{${first_name}}}`{% endraw %}) afficheront la valeur finale que l'utilisateur a reçue en fonction des informations de son profil. Vous pouvez ainsi conserver une copie du message envoyé pour satisfaire aux exigences de conformité, d'audit ou d'assistance à la clientèle.

Si vous configurez des identifiants pour plusieurs fournisseurs de stockage cloud, l'archivage des messages n'exportera que vers celui explicitement marqué comme destination d'exportation de données par défaut. Si aucun défaut explicite n'est fourni et qu'un compartiment AWS S3 est connecté, l'archivage des messages sera chargé dans ce compartiment.

{% alert important %}
L'activation de cette fonctionnalité aura une incidence sur la vitesse de réception/distribution de vos messages, car le téléchargement du fichier est effectué immédiatement avant l'envoi du message afin d'en préserver l'exactitude. La latence introduite par l'archivage des messages dépendra du fournisseur de stockage en nuage ainsi que du débit et de la taille des documents enregistrés.
{% endalert %}

Le JSON sera enregistré dans votre compartiment de stockage en utilisant la structure de clé suivante :

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Un fichier exemple peut ressembler à ceci :

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
L'empreinte MD5 ne peut être calculée qu'à l'aide d'une adresse e-mail, d'un jeton push ou d'un numéro de téléphone E.164 connu. Un condensé MD5 connu ne peut pas être inversé pour obtenir l'adresse e-mail, le jeton push ou le numéro de téléphone E.164.
{% endalert %}

{% alert tip %}
**Vous avez du mal à trouver vos jetons de notifications push dans vos compartiments ?**<br>
Braze met en minuscules vos jetons push avant de les hacher. Le jeton de notification push `Test_Push_Token12345` apparaît alors en minuscules (`test_push_token12345`) dans le chemin d’accès à la clé avec le hachage `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configuration de l'archivage des messages

Cette section vous guide dans la configuration de l'envoi de messages pour votre espace de travail. Avant de continuer, confirmez que votre entreprise a acheté et activé l'archivage des messages.

### Étape 1 : Connecter un compartiment de stockage Cloud

Si vous ne l'avez pas encore fait, connectez un compartiment de stockage Cloud à Braze. Pour les étapes, consultez la documentation de notre partenaire sur [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) ou [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

{% alert note %}
Il n'est pas nécessaire de configurer Currents pour l'archivage des messages, vous pouvez donc ignorer cette condition préalable dans la documentation du partenaire.
{% endalert %}

### Étape 2 : Sélectionnez les canaux pour l'archivage des messages

La page des paramètres d'**archivage des messages** contrôle quels canaux enregistreront une copie des messages envoyés dans votre bucket de stockage cloud.

Pour sélectionner des chaînes :

1. Accédez à **Paramètres** > **Archivage des messages**.
2. Sélectionnez vos chaînes.
3. Sélectionnez **Enregistrer les modifications**.

![La page d'archivage des messages propose trois canaux à sélectionner : Email, Push et SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Si vous ne voyez pas **Archivage des messages** dans **Paramètres**, confirmez que votre entreprise a acheté et activé l'archivage des messages.
{% endalert %}

## Références de fichier

Voici les références à la charge utile JSON transmise à votre compartiment de stockage cloud à chaque envoi de message. Consultez notre référentiel d'exemples de code pour [des fichiers d'exemple d'archive de messages](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab Email %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Hash of key-value pairs from Email Extras configured in the email editor,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

Ce`extras`champ contient les paires clé-valeur configurées dans le champ **« Email Extras** » lors de la rédaction d'un e-mail dans l'éditeur HTML. Les fonctionnalités supplémentaires d'e-mailing sont compatibles avec tous les fournisseurs de services d'e-mailing (y compris Sendgrid et Sparkpost) et sont incluses dans les messages archivés, quel que soit le fournisseur utilisé. Pour plus d'informations sur la configuration des options supplémentaires pour les e-mails, veuillez consulter [la section Création d'une campagne par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras). Pour renvoyer des données à Currents, consultez [Suppléments de messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version": 1 //numerical version of the JSON structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

### Variations de la structure de la charge utile

{% alert important %}
Le `payload`champ de niveau supérieur dans les archives de notifications push contient l'intégralité de la charge utile du fournisseur telle qu'elle a été envoyée à l'appareil. Dans ce JSON, les clés telles que`aps`(pour les APN) ou`notification`et`data`(pour FCM) peuvent varier considérablement en fonction du type de message, de la plateforme et de la configuration.
{% endalert %}

L'archivage des messages capture la charge utile du message elle-même, mais n'inclut pas les métadonnées de réception/distribution envoyées à FCM ou APN. Les métadonnées de réception/distribution comprennent :

- Jetons d'appareil
- Paramètres prioritaires
- Durée de vie (TTL)
- Identifiants de réduction
- En-têtes APN
- Horodatage d'expiration
- Autres champs de configuration de réception/distribution

Ces champs servent d'instructions de réception/distribution au fournisseur de services push. Ils ne sont généralement pas considérés comme faisant partie du contenu du message.

Par exemple :

- **Les notifications push iOS** peuvent présenter des structures différentes pour les notifications enrichies (où`aps.alert`est un objet contenant des champs tels que`title`et `body`) et les notifications simples (où`aps.alert`est une chaîne de caractères).
- **Les notifications push Android** (par exemple, FCM) utilisent des messages de données avec des clés personnalisées. La structure de la charge utile peut inclure différents champs facultatifs en fonction de la configuration du message, tels que des boutons poussoirs, des carrousels ou des métadonnées supplémentaires.

De plus, les envois de test à partir du tableau de bord peuvent générer des structures de charge utile différentes de celles des messages de production.

Le format de la charge utile JSON peut varier d'un message à l'autre et évoluer au fil du temps. Lors de l'analyse des charges utiles archivées, il est important de ne pas présumer d'une structure fixe ni de s'attendre à ce que les mêmes champs soient toujours présents. Mettre en œuvre une logique d'analyse flexible capable de traiter divers formats de charge utile.

{% endtab %}
{% endtabs %}

## Foire aux questions

### Quelle création de modèles n’est pas incluse dans la charge utile ?

Les modifications effectuées après que l'envoi de messages a quitté Braze ne seront pas répercutées dans le fichier enregistré dans votre compartiment de stockage sur le cloud. Cela inclut les modifications apportées par nos partenaires de réception/distribution du courrier, comme l'emballage des liens pour le suivi des clics et l'insertion de pixels de suivi.

### Quels sont les messages sous la valeur « non associé » dans le parcours de campagne ?

Lorsqu'un message est envoyé en dehors d'une campagne ou d'un Canvas, l'ID de la campagne dans le nom du fichier sera "non associé". Cela se produit lorsque vous envoyez des messages de test à partir du tableau de bord, lorsque Braze envoie des réponses automatiques par SMS/MMS ou lorsque les messages envoyés via l'API ne spécifient pas d'ID de campagne.

### Comment faire pour en savoir plus sur cet envoi ?

Vous pouvez utiliser soit le`external_id`  soit`dispatch_id`le  en conjonction avec le`user_id`  pour croiser les références du message modèle avec nos données Currents afin de trouver plus d'informations, telles que l'horodatage de sa livraison, si l'utilisateur a ouvert ou cliqué sur le message, et plus encore.

### Comment les nouvelles tentatives sont-elles traitées ?

Si votre compartiment de stockage en nuage est inaccessible, Braze effectuera jusqu'à trois tentatives avec une [gigue de backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). Les nouvelles tentatives de limitation du débit AWS S3 sont automatiquement gérées par Braze.

### Que se passe-t-il si mes identifiants ne sont pas valides ?

Si vos identifiants de stockage sur le cloud deviennent invalides à un moment donné, Braze ne pourra pas enregistrer de messages dans votre compartiment de stockage sur le cloud, et ces messages seront perdus. Nous vous recommandons de configurer vos [préférences]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) [de notification]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) pour Amazon Web Services, Google Cloud Services ou Microsoft azure (Cloud Services) afin de recevoir des alertes en cas de problèmes liés aux identifiants.

### Pourquoi l'horodatage de mon fichier d'archive `sent_at` diffère-t-il légèrement de l'horodatage de l'envoi dans Currents ?

La copie rendue est téléchargée immédiatement avant l'envoi du message à l'utilisateur. En raison des délais de téléchargement du stockage en nuage, il peut y avoir un décalage de quelques secondes entre l'horodatage `sent_at` de la copie rendue et l'heure réelle de l'envoi.

### Puis-je créer un nouveau compartiment spécifiquement pour l'archivage des messages tout en conservant le compartiment actuel utilisé pour les données de Currents ?

Non. Si vous souhaitez créer ces compartiments spécifiques, soumettez vos [commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Les données archivées sont-elles écrites dans un dossier dédié dans un compartiment existant, de la même manière que les exportations de données de Currents sont structurées ?

Les données sont écrites dans une section du compartiment ( `sent_messages` ). Reportez-vous à la section [Fonctionnement](#how-it-works) pour plus de détails.

### Puis-je utiliser l'archivage des messages pour regrouper les fichiers dans différents espaces de travail ?

Non. L'archivage des messages ne prend pas en charge le regroupement des fichiers en fonction des espaces de travail. Vous pouvez plutôt déterminer à quel espace de travail appartient l'ID de l'API de la campagne ou de l'étape du canvas, puis les regrouper en fonction de cette information.
