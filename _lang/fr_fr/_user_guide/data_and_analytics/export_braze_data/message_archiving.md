---
nav_title: Archivage des messages
article_title: Archivage des messages
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Cet article de référence couvre l'archivage des messages, une fonctionnalité qui vous permet de sauvegarder une copie des messages envoyés aux utilisateurs."

---

# Archivage des messages

> L'archivage des messages vous permet de sauvegarder une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité dans votre bucket AWS S3, conteneur Azure Blob Storage ou bucket Google Cloud Storage. <br><br> Cet article traite de la configuration de l'archivage des messages, des références des charges utiles JSON et des questions fréquemment posées.

L'archivage des messages est disponible en tant que fonctionnalité supplémentaire. Pour commencer avec l'archivage des messages, contactez votre gestionnaire du succès des clients chez Braze.

## Fonctionnement

Lorsque cette fonctionnalité est activée, si vous avez connecté un seau de stockage cloud à Braze et l'avez marqué comme destination d'exportation de données par défaut, Braze écrira un fichier JSON compressé au format gzip dans votre seau de stockage cloud pour chaque message envoyé à un utilisateur via vos canaux sélectionnés (email, SMS ou push). 

Ce fichier contiendra les champs définis sous [Références de fichier](#file-references) et reflétera les messages finaux modélisés envoyés à l'utilisateur. Toutes les valeurs modélisées définies dans votre campagne (par exemple, {% raw %}`{{${first_name}}}`{% endraw %}) afficheront la valeur finale que l'utilisateur a reçue en fonction des informations de son profil. Vous pouvez ainsi conserver une copie du message envoyé pour satisfaire aux exigences de conformité, d'audit ou d'assistance à la clientèle.

Si vous configurez des identifiants pour plusieurs fournisseurs de stockage cloud, l'archivage des messages n'exportera que vers celui explicitement marqué comme destination d'exportation de données par défaut. Si aucun défaut explicite n'est fourni et qu'un compartiment AWS S3 est connecté, l'archivage des messages sera chargé dans ce compartiment.

{% alert important %}
L'activation de cette fonctionnalité aura une incidence sur la vitesse de réception/distribution de vos messages, car le téléchargement du fichier est effectué immédiatement avant l'envoi du message afin d'en préserver l'exactitude. Cela introduit une latence supplémentaire dans le pipeline d’envoi de Braze, ce qui affecte la vitesse d’envoi.
{% endalert %}

Le JSON sera enregistré dans votre compartiment de stockage en utilisant la structure de clé suivante :

`sent_messages/channel/(one of: md5, e164 phone number, email, or push token)/(campaign_id OR canvas_step_id)/DispatchId.json.gz`

Un fichier exemple peut ressembler à ceci :

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
**Vous avez du mal à trouver vos jetons de notifications push dans vos compartiments ?**<br>
Braze met en minuscules vos jetons push avant de les hacher. Le jeton de notification push `Test_Push_Token12345` apparaît alors en minuscules (`test_push_token12345`) dans le chemin d’accès à la clé avec le hachage `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configuration de l'archivage des messages

Cette section vous guide dans la configuration de l'envoi de messages pour votre espace de travail. Avant de continuer, confirmez que votre entreprise a acheté et activé l'archivage des messages.

### Étape 1 : Connecter un compartiment de stockage Cloud

Si vous ne l'avez pas encore fait, connectez un compartiment de stockage Cloud à Braze. Pour les étapes, consultez la documentation de notre partenaire sur [Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/) ou [Google Cloud Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/).

### Étape 2 : Sélectionnez les canaux pour l'archivage des messages

La page des paramètres d'**archivage des messages** contrôle quels canaux enregistreront une copie des messages envoyés dans votre bucket de stockage cloud.

Pour sélectionner des chaînes :

1. Accédez à **Paramètres** > **Archivage des messages**.
2. Sélectionnez vos chaînes.
3. Sélectionnez **Enregistrer les modifications**.

![La page d'archivage des messages propose trois canaux à sélectionner : Email, Push et SMS.][1]

{% alert note %}
Si vous ne voyez pas **Archivage des messages** dans **Paramètres**, confirmez que votre entreprise a acheté et activé l'archivage des messages.
{% endalert %}

## Références de fichier

Les éléments suivants sont des références de la charge utile JSON livrée dans votre bucket de stockage cloud chaque fois qu'un message est envoyé. Consultez notre référentiel d'exemples de code pour [des fichiers d'exemple d'archive de messages](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab E-mail %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Extra hash—for SendGrid users, this will be passed to SendGrid as Unique Arguments,
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
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

Le champ `extras` mentionné dans cette charge utile provient des paires clé-valeur ajoutées dans le champ **E-mails en option** lors de la rédaction d'un e-mail. Pour renvoyer des données à Currents, consultez [Suppléments de messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS %}

```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Notification push %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": ios/android/web/kindle,
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
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## Foire aux questions

### Quelle création de modèles n’est pas incluse dans la charge utile ?

Les modifications effectuées après que l'envoi de messages a quitté Braze ne seront pas répercutées dans le fichier enregistré dans votre compartiment de stockage sur le cloud. Cela inclut les modifications apportées par nos partenaires de réception/distribution du courrier, comme l'emballage des liens pour le suivi des clics et l'insertion de pixels de suivi.

### Quels sont les messages sous la valeur « non associé » dans le parcours de campagne ?

Lorsqu'un message est envoyé en dehors d'une campagne ou d'un Canvas, l'ID de la campagne dans le nom du fichier sera "non associé". Cela se produit lorsque vous envoyez des messages tests à partir du tableau de bord, lorsque Braze envoie des réponses automatiques SMS, ou lorsque les messages envoyés via l’API ne spécifient pas d’ID de campagne.

### Comment faire pour en savoir plus sur cet envoi ?

Vous pouvez utiliser `external_id` ou `dispatch_id` en conjonction avec `user_id` pour croiser le message modèle avec nos données Currents afin d'obtenir plus d'informations telles que l'heure à laquelle le message a été envoyé, si l'utilisateur a ouvert ou cliqué sur le message, et plus encore.

### Comment les nouvelles tentatives sont-elles traitées ?

Si votre compartiment de stockage en nuage est inaccessible, Braze effectuera jusqu'à trois tentatives avec une [gigue de backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). Les nouvelles tentatives de limitation du débit AWS S3 sont automatiquement gérées par Braze.

### Que se passe-t-il si mes identifiants ne sont pas valides ?

Si vos identifiants de stockage sur le cloud deviennent invalides à un moment donné, Braze ne pourra pas enregistrer de messages dans votre compartiment de stockage sur le cloud, et ces messages seront perdus. Nous vous recommandons de configurer la préférence de [notification des erreurs d'identification AWS]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences) afin de recevoir des alertes en cas de problèmes d'identification.

### Pourquoi l'horodatage de mon fichier d'archive `sent_at` diffère-t-il légèrement de l'horodatage de l'envoi dans Currents ?

La copie rendue est téléchargée immédiatement avant l'envoi du message à l'utilisateur. En raison des délais de téléchargement du stockage en nuage, il peut y avoir un décalage de quelques secondes entre l'horodatage `sent_at` de la copie rendue et l'heure réelle de l'envoi.

[1]: {% image_buster /assets/img/message_archiving_settings.png %}
