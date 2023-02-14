---
nav_title: Amplitude pour Currents
article_title: Amplitude pour Currents
page_order: 0
description: "Cet article présente le partenariat entre Braze Currents et Amplitude, une plateforme d’aide à la décision et d’analyse de produits."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude pour Currents

> [Amplitude](https://amplitude.com/) est une plateforme d’aide à la décision et d’analyse de produits.

L'intégration bidirectionnelle Braze et Amplitude vous permet de [synchroniser vos cohortes Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/), vos caractéristiques utilisateur et vos événements dans Braze, ainsi que d'exploiter Braze Currents pour [exporter vos événements Braze vers Amplitude](#data-export-integration) afin d'effectuer des analyses plus approfondies de vos données produit et marketing.

## Conditions préalables

| Configuration requise | Description |
|---|---|
| Compte Amplitude | Un [compte Amplitude](https://amplitude.com/) est requis pour profiter de ce partenariat. |
| Currents | Pour réexporter des données dans Amplitude, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2} 

## Intégration de l’exportation de données

Les sections suivantes présentent une liste complète des événements et des propriétés de l’événement pouvant être exportés de Braze vers Amplitude. Tous les événements envoyés à Amplitude incluront l’`external_user_id` de l’utilisateur en tant qu’ID utilisateur d’Amplitude. Les propriétés de l’événement spécifiques à Braze seront envoyées sous la clé `event_properties` dans les données envoyées à Amplitude.

Braze enverra uniquement des données d’événements pour les utilisateurs dont l’`external_user_id` est défini ou pour les utilisateurs anonymes dont l’`device_id` est défini. Pour les utilisateurs anonymes, vous devrez synchroniser votre ID d'appareil Amplitude avec l'ID d'appareil Braze dans le SDK. Par exemple :
```java
amplitude.setDeviceId(Apppboy.getInstance(context).getDeviceId();)
```

Vous pouvez exporter deux types d’événements vers Amplitude : Les [événements d’engagement par message](#message-engagement-events), qui incluent les Événements de Braze directement liés à l’envoi de messages, et les [événements de comportement client](#customer-berhavior-events), qui incluent les activités d’autres applications ou sites Web, telles que des sessions, des événements personnalisés et des achats suivis sur la plateforme. Tous les événements standard sont précédés par `[Appboy]`, et tous les événements personnalisés sont précédés par `[Appboy] [Custom Event]`. Les propriétés de l’événement personnalisé et d’achat sont précédées par `[Custom event property]` and `[Purchase property]`, respectivement.

Toutes les cohortes nommées et importées dans Braze seront précédées par `[Amplitude]` et suivies de leur `cohort_id`. Cela signifie qu’une cohorte nommée « TEST_COHORT » avec le `cohort_id` « abcd1234 » sera intitulée `[Amplitude] TEST_COHORT: abcd1234` dans les filtres Braze.

Contactez votre gestionnaire de compte ou ouvrez un [cas d’assistance][support] si vous avez besoin d’accéder à des droits d’événement supplémentaires.

### Étape 1 : Configurer l’intégration Amplitude dans Braze 

Dans Amplitude, recherchez votre clé API d’exportation Amplitude.

{% alert warning %}
Assurez-vous de maintenir votre clé API Amplitude à jour. Le connecteur arrêtera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

### Étape 2 : Créer un Braze Current

Dans Braze, accédez à **Currents > > + Create Current (+ Créer un Current) > Create Amplitude Export (Créer une exportation Amplitude)**. Indiquez le nom de l’intégration, une adresse e-mail de contact, la clé API d’exportation Amplitude et une région pour Amplitude dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

{% alert note %}
Les événements envoyés de Braze Currents à Amplitude seront pris en compte dans votre quota de volume d'événements Amplitude.
{% endalert %}

![La page Braze Amplitude Currents. Cette page comprend des champs pour le nom d’intégration, l’adresse e-mail de contact, la clé API et la région US. La moitié inférieure de la page Currents répertorie les événements Currents que vous pouvez envoyer.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Consultez les [documents d’intégration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) d’Amplitude pour en savoir plus. 
{% endtab %}

## Limites de débit

Les Currents se connectent à l’API HTTP d’Amplitude, qui comporte une [Limitation du débit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 événements/seconde par appareil et une limite non documentée de 500 000 événements/jour par appareil. Si ces seuils sont dépassés, Amplitude limitera les événements enregistrés dans des Currents. Si un appareil au sein de votre intégration dépasse cette limite de débit, il se peut que les appareils apparaissent dans Amplitude avec un certain retard.

Dans des circonstances normales, les appareils ne doivent pas rapporter plus de 30 événements/seconde ou 500 000 événements/jour, et cette fréquence d’événement ne devrait se produire qu’en cas d’intégration mal configurée. Pour éviter ce type de retard, assurez-vous que votre intégration SDK rapporte des événements à une fréquence normale, tel que spécifié dans nos instructions d’intégration SDK. D’autre part, faites attention à ne pas exécuter de tests automatisés qui génèrent de nombreux événements pour un seul appareil.

## Événements de comportement client

### Événements personnalisés

```json
// <Nom d’évènement personnalisé>
{
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements d’achat

```json
// Achat
{
  "product_id": (string) ID du produit acheté (envoyé dans le champ « productId » de l’API HTTP Amplitude),
  "price": (float) prix du produit (envoyé dans le champ « price » (prix) de l’API HTTP Amplitude),
  "currency": (string) code de devise ISO 4217 alphabétique à trois lettres,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de session

```json
// Première session
{
  "session_id": (string) ID de la session,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Démarrage de la session
{
  "session_id": (string) ID de la session,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Fin de la session
{
  "session_id": (string) ID de la session,
  "duration": (float) durée de la session en secondes,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de localisation

```json
// Emplacement
{
  "longitude": (float) longitude du lieu enregistré,
  "latitude": (float) latitude du lieu enregistré,
  "altitude": (float) altitude du lieu enregistré,
  "ll_accuracy": (float) un pourcentage représentant la précision déterminée par le système d’exploitation de l’emplacement enregistré,
  "alt_accuracy": (float) précision de l’altitude du lieu enregistré,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements d’attribution d’installation

```json
// Attribution d’installation
{
  "source": (string) la source de l’attribution
}
```

## Événements d’engagement par message

### Événements de notification push

```json
// Notification push envoyée
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
// Notification push ouverte
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
// Notification Push iOS ouverte en premier plan
// Veuillez noter que cet événement n’est pas pris en charge par notre SDK Swift et est obsolète sur notre SDK Obj-C.
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
// Notification push renvoyée
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "app_id": (string) ID de l’application sur laquelle le renvoi s’est produit,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
```

### Événements par e-mail

```json
// E-mail envoyé
// Livraison des e-mails
// Ouverture des e-mails
// Clics sur les e-mails
// Renvoi d’e-mail
// Soft bounce d’e-mail
// E-mails marqués comme spam
// Désinscription des e-mails
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "url": (string) l’URL qui a été cliquée (événements e-mail cliqué uniquement),
  "user_agent": (string) description du système et du navigateur de l’utilisateur pour l’événement (événements e-mail cliqué et e-mail ouvert uniquement),
  "link_id": (string) valeur unique générée par Braze pour l’URL (événements e-mail cliqué uniquement, et nécessite l’activation de l’aliasage de lien),
  "link_alias": (string) nom d’alias défini lors de l’envoi du message (événements e-mail cliqué uniquement et nécessite l’activation de l’aliasage de lien),
  "machine_open": (string) Indicateur permettant de savoir si l’e-mail a été ouvert par un processus automatisé, comme la fonction de pré-récupération des e-mails d’Apple ou de Google. Actuellement « true » ou nul, mais une granularité supplémentaire (p. ex., « Apple » ou « Google » pour indiquer quel processus a récupéré l’e-mail) pourrait être ajoutée à l’avenir. (Événements e-mail ouverts uniquement)
}
```

### Événements d'étape de test

```json
// Entrée de direction fractionnée de l'étape expérimentale
{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "experiment_step_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "experiment_split_id": (string) ID BSON de la division d’expérience à laquelle l’utilisateur s’est inscrit,
  "experiment_split_name": (string) nom de la division d’expérience à laquelle l’utilisateur s’est inscrit,
  "in_control_group": (boolean) si l’utilisateur était inscrit dans le groupe de contrôle
}

// Conversion d’étape de test
{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "workflow_id": (string) ID Braze à usage interne du flux de travail auquel cet événement appartient,
  "experiment_step_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "experiment_split_id": (string) ID BSON de la variation de répartition du test reçue par cet utilisateur,
  "conversion_behavior_index": (int) index du comportement de conversion
}
```

### Événements SMS
```json
// SMS envoyé
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
}

// SMS envoyé à l’opérateur
// Envoi SMS
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
}

// Rejet SMS
// Échec de livraison SMS
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
  "error": (string) Message d’erreur pour le rejet ou l’échec de livraison,
  "provider_error_code": (string) Code d’erreur pour le rejet ou l’échec de livraison,
}
```



### Événements d’abonnement

```json
// Changement de l’état du groupe d’abonnement
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "email_address": (string) adresse e-mail pour cet événement,
  "subscription_group_id": (string) ID du groupe d’abonnement,
  "subscription_status": (string) statut de l’abonnement après le changement : 'Abonné' ou 'Désabonné'
}
```

### Événements de messages in-app

```json
// Impression de message in-app
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Clic des messages in-app
{
  "button_id": (string) index du bouton cliqué, s’il s’agit d’un bouton cliqué, ou ID de suivi du clic, si l’événement provient d’un appel appboyBridge.logClick,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de Webhook

```json
// Envoi de webhook
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST)
}
```

### Événements de carte de contenu

```json
// Envoi de carte de contenu
{
  "card_id": (string) ID de la carte de contenu qui a été envoyée,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST)
}
```

```json
// Impression de carte de contenu
// Clic de carte de contenu
// Rejet d’une carte de contenu
{
  "card_id": (string) ID de la carte de contenu qui a été visualisée/clicked/dismissed,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST),
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de fil d’actualité

{% alert note %}
Les fils d'actualités deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

```json
// Impression de carte de fil d’actualité
{
  "card_id": (string) ID de la carte qui a été visualisée,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Clic sur la carte de fil d’actualité
{
  "card_id": (string) ID de la carte qui a été cliquée,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Impression du fil d’actualité
{
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de désinstallation

```json
// Désinstallation
{
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite
}
```

### Événements de conversion

```json
// Événements de conversion de campagne
{
  "campaign_id": (string) ID de la campagne,
  "campaign_name": (string) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) ID de la variation du message,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST)
}
// Événements de conversion Canvas
{
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion
}
```

### Événements d’entrée Canvas

```json
// Entrée Canvas
{
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "in_control_group": (boolean) si l’utilisateur était inscrit dans le groupe de contrôle pour un Canvas
}
```

### Événements d’inscription à la campagne

```json
// Inscription au groupe de contrôle de campagne
{
  "campaign_id": (string) ID de la campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Identifiant d’envoi sous Définitions des paramètres de l’API REST)
}
```

### Événements de sortie Canvas

```json
// Sortie de canevas – Événement effectué
// Sortie de canevas – Audience correspondante
{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,,
  "app_group_api_id": (string) ID API du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,,
  "canvas_step_id": (string) ID BSON de Canvas Step à laquelle appartient cet événement,,
  "canvas_api_id": (string) ID API du Canvas auquel appartient cet événement,,
  "canvas_variation_api_id": (string) ID API de la variation de Canvas auquel appartient cet événement,,
  "canvas_step_api_id": (string) ID API de Canvas Step à laquelle appartient cet événement,,
}
```

[support]: {{site.baseurl}}/braze_support/
