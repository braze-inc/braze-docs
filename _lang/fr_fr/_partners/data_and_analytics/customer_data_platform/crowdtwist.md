---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "Cet article présente le partenariat entre Braze et Oracle Crowdtwist, par le biais de modèles de transformation de données Braze spécialement créés et des objets de poussée de données de Crowdtwist."
page_type: partner
search_tag: Partner

---

# Oracle Crowdtwist

> [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) est une solution de fidélisation de la clientèle native dans le cloud qui permet aux marques d'offrir des expériences clients personnalisées. Leur solution propose plus de 100 parcours d'engagement prêts à l'emploi, ce qui permet aux marketeurs d'obtenir rapidement une vue plus complète du client.

La fonctionnalité Data Push d'Oracle Crowdtwist permet de transmettre les métadonnées d'un utilisateur ou d'un événement à chaque fois qu'une mise à jour se produit dans la plateforme de Crowdtwist.

Ce guide explique comment intégrer les flux Live Push du profil utilisateur, de l'activité de l'utilisateur et de la rédemption de l'utilisateur d'Oracle Crowdtwist dans votre environnement Braze. Il existe deux autres types de Data Push qui ne sont pas explicitement traités dans cette documentation, mais dont la configuration suit les mêmes principes que ceux décrits ci-dessous. 

* [Profil utilisateur Live Push](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Comprend la création de nouveaux profils et la mise à jour des profils existants.

* [Activité de l'utilisateur en ligne/en production/instantanée](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Comprend des données sur l'achèvement des activités des utilisateurs.

* [En ligne/en production/instantanée](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Comprend des données sur l'utilisation des récompenses par les utilisateurs. 

En utilisant un modèle de transformation de données Braze, vous pouvez filtrer les éléments de la poussée de données qui ne sont pas pertinents pour Braze, et attribuer les valeurs nécessaires dans Braze afin qu'elles puissent être exploitées par les "destinations" disponibles.

Par exemple, utilisez un Data Push pour transmettre à Braze des événements et attributs personnalisés pertinents, comme lorsqu'un utilisateur change de niveau de fidélité ou échange une récompense. Vous pouvez également l'utiliser pour enregistrer des attributs personnalisés dans Braze dès que ces données sont mises à jour dans le profil utilisateur d'un membre, comme le solde de points d'un utilisateur. 

## Conditions préalables


| Condition | Description |
| --- | --- |
| Compte Oracle Crowdtwist | Un [compte Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) est nécessaire pour profiter de ce partenariat. |
| Braze Data Transformation Endpoint (Point final de transformation des données)| Cette intégration repose sur l' [outil de transformation des données de]({{site.baseurl}}/user_guide/data/data_transformation/overview) Braze. Lorsque vous créez une transformation de données, Braze génère un endpoint unique que vous pouvez ajouter comme destination pour le Data Push de Crowdtwist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Braze et Oracle Crowdtwist ont créé des [modèles de transformation de données]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) pour aider nos clients à développer leurs propres transformations de données qui exploitent les événements Profil utilisateur, Remboursement utilisateur et Activité utilisateur. 

## Étape 1 : Créer une transformation de données à partir du modèle Oracle Crowdtwist

Naviguez vers **Paramètres des données > Transformation des données > Créer des transformations > Utiliser un modèle** > et sélectionnez le modèle "BRAZE <> CROWDTWIST" de votre choix. 

Vous trouverez quatre modèles, un pour transformer les événements Profil utilisateur, Activité utilisateur et Remboursement utilisateur, et un modèle principal qui utilise une logique conditionnelle pour s'appliquer à divers événements Data Push.

Comme le montre la [documentation d'Oracle Crowdtwist sur le Data Push](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html), les objets Data Push contiennent des métadonnées différentes, de sorte que chacun nécessite son propre code de transformation pour créer les objets Braze appropriés. Le modèle principal illustre comment configurer une seule transformation de données pour accepter chacun des trois types d'objets et créer une sortie appropriée avec les valeurs de chaque objet.

## Étape 2 : Mise à jour et test du modèle

Vous trouverez ci-dessous les modèles annotés. Le corps de ces modèles est conçu pour s'appliquer à la destination `/users/track`. Les annotations sont marquées par le début de ligne `//` et le texte vert, et vous pouvez les supprimer sans affecter le fonctionnement du code de transformation. 

La transformation utilise JavaScript, qui crée un objet appelé "brazecall". C'est dans cet objet que vous créez le corps de la requête qui est envoyé à un endpoint de l'API REST de Braze. Pour obtenir des conseils sur les structures requises pour les demandes vers ces destinations, consultez les liens dans la section "destinations".    

{% alert note %}
Remarquez que les "valeurs" de chaque "clé" commencent par `payload.`. Le payload représente l'objet de données reçu d'Oracle Crowdtwist. Utilisez la notation JavaScript par points pour choisir les données qui doivent alimenter les éléments de votre objet Braze. Par exemple, lorsque vous voyez `external_id: payload.thirdPartyId`, cela signifie que l'ID externe de Braze est défini par la valeur `third_party_id` stockée dans Oracle Crowdtwist. Pour plus d'informations sur le schéma ou la composition des objets provenant d'Oracle Crowdtwist, consultez la [documentation d'Oracle](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
 Utilisez les objets envoyés par Oracle Crowdtwist pour créer des utilisateurs dans Braze. En incluant la clé `update_existing_only` avec la valeur `false`, si un objet d'attribut ou d'événement comprend un identifiant qui n'existe pas dans Braze, Braze crée un profil utilisateur avec les attributs inclus dans l'objet d'événement ou d'attribut. Si vous préférez qu'Oracle Crowdtwist ne mette à jour que les profils qui existent déjà dans Braze, définissez cet attribut sur `true` dans chaque objet d'attribut ou d'événement.
{% endalert %}

### Modèles de transformation des données
{% tabs %}
{% tab User Profile Event Template%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while "tierInfo" below is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object. 
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab User Activity Event Template %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Redemption Event Template %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Master Template %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs. 

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### Destinations

Les modèles de ce guide sont créés pour livrer à la destination " Suivi des utilisateurs ", mais vous pouvez concevoir votre modèle pour l'envoyer à n'importe quel endpoint répertorié dans le [guide Transformation des données de Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/#step-2-create-a-transformation), avec l'aide de la [documentation de l'API REST]({{site.baseurl}}/api/home) associée.

### Test

Après avoir modifié le modèle à votre convenance, vous devez vous assurer qu'il fonctionne correctement. Cliquez sur "Valider" pour obtenir un aperçu de la sortie de votre code et vérifier s'il s'agit d'une demande acceptable pour la destination choisie. 

![Capture d'écran de l'interface de transformation des données de Braze]({% image_buster /assets/img/crowdtwist_tools/screenshot.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

Lorsque vous êtes satisfait de l'objet que vous voyez dans le champ "output", cliquez sur **Activer** pour que le endpoint de transformation des données soit prêt à accepter des données. 

Vous trouverez l'URL du webhook de votre transformation de données dans le panneau latéral gauche. Copiez-le et utilisez-le pour la configuration dans le hub d'intégration d'Oracle Crowdtwist.

{% alert important %}
Les endpoints de transformation des données de Braze ont une limite de débit de 1000 requêtes par minute. Réfléchissez à la vitesse à laquelle vous souhaitez que ces données soient mises à disposition dans Braze et consultez votre gestionnaire de compte Braze si vous avez besoin d'une limite de débit plus élevée pour la transformation des données.
{% endalert %}

Les transformations de données sont un outil très dynamique et vous pouvez les concevoir à des fins qui vont au-delà de ce qui est décrit dans ce document, avec une compréhension de JavaScript et avec les conseils de notre documentation sur l'API REST. Pour obtenir de l'aide ou une résolution des problèmes concernant des modifications complexes apportées à vos modèles de transformation des données, adressez-vous à votre gestionnaire de la réussite des clients pour connaître les conseils dont vous disposez.