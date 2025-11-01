---
nav_title: Archivage des messages
article_title: Archivage des messages
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Cet article de référence traite de l'archivage des messages, une fonctionnalité qui vous permet d'enregistrer une copie des messages envoyés aux utilisateurs."

---

# Archivage des messages

> L'archivage des messages vous permet d'enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité dans votre compartiment AWS S3, votre conteneur Azure Blob Storage ou votre compartiment Google Cloud Storage. <br><br> Cet article traite de la configuration de l'archivage des messages, des références des charges utiles JSON et des questions fréquemment posées.

L'archivage des messages est une fonctionnalité supplémentaire. Pour démarrer l'archivage des messages, contactez votre gestionnaire satisfaction client Braze.

## Comment cela fonctionne-t-il ?

Lorsque cette fonctionnalité est activée, si vous avez connecté un compartiment de stockage dans le cloud à Braze et l'avez marqué comme destination d'exportation de données par défaut, Braze écrira un fichier JSON gzippé dans votre compartiment de stockage dans le cloud pour chaque message envoyé à un utilisateur par le biais des canaux que vous avez sélectionnés (e-mail, SMS/MMS ou push). 

Ce fichier contiendra les champs définis dans les [références de fichiers](#file-references) et reflétera les messages finaux envoyés à l'utilisateur. Toute valeur modèle définie dans votre campagne (par exemple, {% raw %}`{{${first_name}}}`{% endraw %}) affichera la valeur finale que l'utilisateur a reçue sur la base de ses informations de profil. Vous pouvez ainsi conserver une copie du message envoyé pour satisfaire aux exigences de conformité, d'audit ou d'assistance à la clientèle.

Si vous configurez des informations d'identification pour plusieurs fournisseurs de stockage dans le cloud, l'archivage des messages n'exportera que vers celui qui est explicitement marqué comme destination d'exportation de données par défaut. Si aucune valeur par défaut explicite n'est fournie et qu'un compartiment AWS S3 est connecté, l'archivage des messages sera téléchargé vers ce compartiment.

{% alert important %}
L'activation de cette fonctionnalité aura une incidence sur la vitesse de réception/distribution de vos messages, car le téléchargement du fichier est effectué immédiatement avant l'envoi du message afin d'en préserver l'exactitude. La latence introduite par l'archivage des messages dépendra du fournisseur de stockage en nuage ainsi que du débit et de la taille des documents enregistrés.
{% endalert %}

Le JSON sera enregistré dans votre compartiment de stockage en utilisant la structure de clé suivante :

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Un exemple de fichier peut se présenter comme suit :

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
L'empreinte MD5 ne peut être calculée qu'à l'aide d'une adresse e-mail, d'un jeton push ou d'un numéro de téléphone E.164 connu. Un condensé MD5 connu ne peut pas être inversé pour obtenir l'adresse e-mail, le jeton push ou le numéro de téléphone E.164.
{% endalert %}

{% alert tip %}
**Vous avez du mal à trouver vos jetons dans vos compartiments ?**<br>
Braze décompose vos jetons de poussée avant que nous ne les hachions. Il en résulte que le jeton `Test_Push_Token12345` est descendu à `test_push_token12345` dans le chemin de clé avec le hachage `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configuration de l'archivage des messages

Cette section vous guide dans la configuration de l'envoi de messages pour votre espace de travail. Avant de poursuivre, vérifiez que votre entreprise a acheté et activé l'archivage des messages.

### Étape 1 : Connecter un compartiment de stockage en nuage

Si vous ne l'avez pas encore fait, connectez un compartiment de stockage dans le cloud à Braze. Pour connaître la marche à suivre, consultez la documentation de nos partenaires sur [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) ou [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Étape 2 : Sélectionner les canaux pour l'envoi de messages

La page des paramètres de l'**archivage des messages** permet de contrôler les canaux qui enregistreront une copie des messages envoyés dans votre compartiment de stockage sur le cloud.

Pour sélectionner les chaînes :

1. Allez dans **Paramètres** > **Archivage des messages.**
2. Sélectionnez vos chaînes.
3. Sélectionnez **Enregistrer les modifications**.

La page d'envoi de messages comporte trois canaux de communication à sélectionner : E-mail, Push et SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Si vous ne voyez pas l'envoi **de messages** dans les **paramètres**, confirmez que votre entreprise a acheté et activé l'archivage des messages.
{% endalert %}

## Références des dossiers

Voici les références de la charge utile JSON livrée à votre compartiment de stockage en nuage chaque fois qu'un message est envoyé. Consultez notre référentiel d'exemples de code pour obtenir des [fichiers d'exemples d'archives de messages](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab Email %}

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

Le champ `extras` auquel il est fait référence dans ce payload provient des paires clé-valeur ajoutées dans le champ **Email Extras** lors de la composition d'un e-mail. Pour l'envoi de données à Currents, reportez-vous aux [suppléments de message.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)

\![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version" : 1 //numerical version of the json structure
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
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version" : 1, //numerical version of the json structure
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

{% endtab %}
{% endtabs %}

## Questions fréquemment posées

### Quels sont les modèles qui ne sont pas inclus dans la charge utile ?

Les modifications effectuées après que l'envoi de messages a quitté Braze ne seront pas répercutées dans le fichier enregistré dans votre compartiment de stockage sur le cloud. Cela inclut les modifications apportées par nos partenaires de réception/distribution du courrier, comme l'emballage des liens pour le suivi des clics et l'insertion de pixels de suivi.

### Quels sont les messages sous la valeur "non associé" dans le chemin de la campagne ?

Lorsqu'un message est envoyé en dehors d'une campagne ou d'un Canvas, l'ID de la campagne dans le nom du fichier sera "non associé". Cela se produit lorsque vous envoyez des messages de test à partir du tableau de bord, lorsque Braze envoie des réponses automatiques par SMS/MMS ou lorsque les messages envoyés via l'API ne spécifient pas d'ID de campagne.

### Comment puis-je obtenir plus d'informations sur cet envoi ?

Vous pouvez utiliser `external_id` ou `dispatch_id` en conjonction avec `user_id` pour croiser le message modèle avec nos données Currents afin d'obtenir plus d'informations telles que l'heure à laquelle le message a été envoyé, si l'utilisateur a ouvert ou cliqué sur le message, et plus encore.

### Comment les tentatives sont-elles gérées ?

Si votre compartiment de stockage en nuage est inaccessible, Braze effectuera jusqu'à trois tentatives avec une [gigue de backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). Les tentatives de relance de la limite de débit d'AWS S3 sont automatiquement prises en charge par Braze.

### Que se passe-t-il si mes données d'identification ne sont pas valides ?

Si vos identifiants de stockage sur le cloud deviennent invalides à un moment donné, Braze ne pourra pas enregistrer de messages dans votre compartiment de stockage sur le cloud, et ces messages seront perdus. Nous vous recommandons de configurer vos [préférences de notification]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) pour Amazon Web Services, Google Cloud Services ou Azure (Microsoft Cloud Services) afin de recevoir des alertes en cas de problème d'identification.

### Pourquoi l'horodatage de mon fichier d'archive `sent_at` diffère-t-il légèrement de l'horodatage de l'envoi dans Currents ?

La copie rendue est téléchargée immédiatement avant l'envoi du message à l'utilisateur. En raison des délais de téléchargement du stockage en nuage, il peut y avoir un décalage de quelques secondes entre l'horodatage `sent_at` de la copie rendue et l'heure réelle de l'envoi.

### Puis-je créer un nouveau compartiment spécifiquement pour l'archivage des messages tout en conservant le compartiment actuel utilisé pour les données de Currents ?

Non. Si vous souhaitez créer ces compartiments spécifiques, soumettez vos [commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Les données archivées sont-elles écrites dans un dossier dédié dans un compartiment existant, de la même manière que les exportations de données de Currents sont structurées ?

Les données sont écrites dans une section du compartiment ( `sent_messages` ). Pour plus de détails, reportez-vous à la section [Fonctionnement](#how-it-works).

