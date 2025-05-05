---
nav_title: Zeotap Symphony
description: "Cet article de référence décrit le partenariat entre Braze et Zeotap, une plateforme de données clients de nouvelle génération qui fournit une fonction de résolution d'identité, des informations et un enrichissement."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Symphonie Zoetap

L'intégration de Braze et Zoetap Symphony vous permet de créer des orchestrations en temps réel et de lancer des campagnes d'e-mail et de notification push.

- Envoyez les prénoms et les noms de famille via Zeotap, en fonction desquels les utilisateurs peuvent envoyer des e-mails personnalisés via Braze.
- Envoyez des custom events ou un événement d'achat en temps réel via Zeotap, en fonction desquels les utilisateurs peuvent créer des déclencheurs de campagne au sein de Braze pour cibler leurs clients

{% alert note %}
Pour créer des campagnes de marketing par e-mail, intégrez les e-mails bruts à Zeotap en les mappant à `Email Raw` dans le catalogue Zeotap.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Nom du client | Ceci est le nom de votre client pour votre compte Braze. Vous pouvez le trouver en accédant à la console Braze. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| instance | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Intégration

Cette section fournit des informations sur les deux méthodes que vous pouvez intégrer avec Braze :

### Méthode 1
Dans cette méthode, vous devez effectuer les tâches suivantes :
1. Intégrez le SDK Braze à votre site web ou application.
2. Intégrez Braze avec Zeotap via Symphony.

- `User traits` doit être mappé aux champs Braze respectifs sous l'onglet **Données à envoyer**. Le mappage des attributs `Event` et `Purchase` entraîne la duplication d’événements dans Braze.
- Mappez `External ID` à l’ID `User ID` qui a été configuré lors de la configuration du SDK Braze.

Lorsque l'intégration est correctement configurée, vous pouvez créer des campagnes d'e-mail et de notification push basées sur des attributs personnalisés envoyés à Braze via Symphony.

### Méthode 2
Dans cette méthode, vous pouvez intégrer Braze à Zeotap via Symphony.

- Cette méthode ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze telles que l'envoi de messages in-app, le fil d'actualité, les cartes de contenu ou les notifications push.
- Zeotap recommande de mapper le paramètre `hashed email` disponible à `External ID` dans le catalogue Zeotap.

Lorsque l'intégration est correctement configurée, vous ne pouvez créer des campagnes d'e-mail qu'en fonction des attributs personnalisés envoyés à Braze via Symphony.

## Flux de données vers Braze et identifiants pris en charge

Les données circuleront de Zeotap à Braze en utilisant l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Les points suivants résument le flux de données :

1. Zeotap envoie des attributs de profil utilisateur, des attributs personnalisés, des événements personnalisés et des champs d'achat.
2. Vous mappez tous les champs pertinents du catalogue Zeotap aux champs Braze sous l'onglet **Données à envoyer**.
3. Les données sont ensuite téléchargées vers Braze.

Vous pouvez trouver des détails sur les différents attributs dans la section [Données à envoyer](#data-to-send-tab).

## Configuration de destination

Après avoir appliqué des filtres ou ajouté une condition pour vos utilisateurs dans Symphony, vous pouvez les activer dans Braze sous **Envoyer vers des destinations**. Une nouvelle fenêtre dans laquelle vous pouvez configurer votre destination s'ouvre. Vous pouvez utiliser une destination existante de la liste des **Destinations Disponibles** ou en créer une nouvelle.

#### Ajouter une nouvelle destination
Effectuez les étapes suivantes pour ajouter une nouvelle destination :
1. Sélectionnez **Ajouter une nouvelle destination**.
2. Rechercher **Braze**.
3. Ajoutez le **Nom du client**, la **clé API** et l'**instance** et enregistrez la destination.

La destination est créée et mise à disposition sous **Destinations disponibles**.

#### Ajouter des entrées au niveau du flux de travail
Après avoir créé une destination, vous devez ensuite ajouter des entrées au niveau du flux de travail, comme mentionné ci-dessous.
1. Choisissez la destination dans la liste des destinations disponibles en utilisant la fonctionnalité de recherche.
2. Les champs **Nom du client**, **clé API** et **instance** sont automatiquement remplis en fonction de la valeur que vous avez entrée lors de la création de la destination.
3. Entrez le **Nom de l'audience** que vous souhaitez créer pour ce nœud de flux de travail. Ceci est envoyé en tant que **attribut personnalisé** à Braze.
4. Mappez le catalogue vers la destination sous l'onglet **Données à envoyer**. Vous pouvez trouver des détails sur la façon d'effectuer le mappage ci-dessous.

#### Onglet Données à envoyer
L'onglet **Données à envoyer** vous permet de mapper les champs du catalogue Zeotap aux champs Braze qui peuvent être envoyés à Braze. Le mappage peut être effectué de l'une des manières suivantes :
- **Mappage statique** \- Il y a certains champs que Zeotap mappe automatiquement aux champs Braze pertinents comme les champs de l’e-mail, du téléphone, du prénom, du nom de famille, etc.<br>
- **Sélection déroulante** \- Mapper les champs pertinents ingérés dans Zeotap aux champs Braze fournis dans le menu déroulant.<br>![Diverses caractéristiques d'utilisateur définies dans Zeotap, telles que la langue, la ville, la date d’anniversaire, et plus encore.][3]{: style="max-width:70%;"}<br>
- **Entrée de données personnalisées** \- Ajoutez des données personnalisées mappées au champ Zeotap pertinent et envoyez-les à Braze.<br>![Sélection de "loyalty_points" comme caractéristique utilisateur dans Zeotap.][4]{: style="max-width:70%;"}

## Attributs pris en charge
Vous pouvez trouver les détails de tous les champs Braze dans cette section.

| Champ Braze | Type de mappage | Description |
| --- | --- | --- |
| ID externe | Sélection déroulante | Ceci est le `User ID` persistant que vous avez défini par Braze pour suivre les utilisateurs sur différents appareils et plateformes. Nous vous recommandons de mapper `User ID` à `External ID` ; sinon, Zeotap peut envoyer un e-mail en tant qu'alias d'utilisateur.<br><br>Zeotap recommande de mapper le `hashed email` disponible dans le catalogue Zeotap au `External ID`.|
| e-mail | Mappage statique | Ceci est mappé à `Email Raw` dans le catalogue Zeotap. |
| Téléphone | Mappage statique | Ceci est mappé à `Mobile Raw` dans le catalogue Zeotap.<br><br>• Braze accepte les numéros de téléphone au format `E.164`. Zeotap ne réalise aucune transformation. Par conséquent, vous devez ingérer les numéros de téléphone dans le format prescrit. Pour plus d'informations, consultez la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| Prénom | Mappage statique | Ceci est mappé à `First Name` dans le catalogue Zeotap. |
| Nom de famille | Mappage statique | Ceci est mappé à `Last Name` dans le catalogue Zeotap. |
| Sexe | Mappage statique | Ceci est mappé à `Gender` dans le catalogue Zeotap. |
| Nom de l'événement personnalisé | Mappage statique | Ceci est mappé à `Event Name` dans le catalogue Zeotap.<br><br>Les deux noms d'événements personnalisés et horodatages d'événements personnalisés doivent être mappés pour capturer des événements personnalisés dans Braze. L'événement personnalisé ne peut pas être traité si l'un des deux n'est pas mappé. Pour plus d'informations, consultez la section sur l'[objet d'événement]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Horodatage de l'événement personnalisé | Mappage statique | Ce champ est mappé sur le champ `Event Timestamp` dans le catalogue Zeotap.<br><br>Les deux noms d'événements personnalisés et horodatages d'événements personnalisés doivent être mappés pour capturer des événements personnalisés dans Braze. L'événement personnalisé ne peut pas être traité si l'un des deux n'est pas mappé. Pour plus d'informations, consultez la section sur l'[objet d'événement]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Abonnement aux e-mails | Sélection déroulante | Intégrez un champ `Email Marketing Preference` et créez une correspondance avec ce dernier.<br><br>Zeotap envoie les trois valeurs suivantes :<br>• `opted_in` - Indique que l'utilisateur s'est explicitement inscrit pour la préférence de marketing par e-mail<br>• `unsubscribed` - Indique que l'utilisateur a explicitement refusé les e-mails<br>• `subscribed` - Indique que l'utilisateur n'a ni opté pour ni opté contre. |
| Abonnement aux notifications push | Sélection déroulante | Intégrez un champ `Push Marketing Preference` et établissez une correspondance avec ce dernier.<br><br>Zeotap envoie les trois valeurs suivantes :<br>• `opted_in` - Indique que l'utilisateur s'est explicitement inscrit à la préférence de marketing push<br>• `unsubscribed` - Indique que l'utilisateur a explicitement refusé les messages push.<br>• `subscribed` - Indique que l'utilisateur n'a ni opté pour ni opté contre |
| Activation du suivi d'ouverture des e-mails | Sélection déroulante | Cartographiez le champ `Marketing Preference` pertinent.<br><br>Lorsqu'il est défini sur vrai, il permet d'ajouter un pixel de suivi ouvert à tous les futurs e-mails envoyés à cet utilisateur. |
| Suivi des clics sur les e-mails activé | Sélection déroulante | Cartographiez le champ `Marketing Preference` pertinent.<br><br>Lorsqu'il est défini sur vrai, il active le suivi des clics pour tous les liens dans tous les futurs e-mails envoyés à cet utilisateur. |
| ID du produit | Sélection déroulante | • Identifiant pour une action d'achat `(Product Name/Product Category)`. Pour plus de détails, consultez la section sur[l'objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/).<br>• Intégrez l'attribut pertinent au catalogue Zeotap et établissez une correspondance avec ce dernier.<br><br>`Product ID`, `Currency`, et `Price` doivent être mappés obligatoirement pour capturer les événements d'achat dans Braze. L'événement d'achat ne peut pas se dérouler si l'un des trois est manqué. Pour plus d'informations, consultez l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-object). |
| Devise | Sélection déroulante | • Attribut de devise pour l'action d'achat.<br>• Le format pris en charge est `ISO 4217 Alphabetic Currency Code`.<br>• Intégrer correctement les données de devise formatées dans le catalogue Zeotap et établir une correspondance avec ces dernières.<br><br>`Product ID`, `Currency`, et `Price` doivent être mappés obligatoirement pour capturer les événements d'achat dans Braze. L'événement d'achat ne peut pas se dérouler si l'un des trois est manqué. |
| Prix | Sélection déroulante | • Attribut de prix pour l'action d'achat.<br>• Intégrez l'attribut pertinent au catalogue Zeotap et établissez une correspondance avec ce dernier.<br><br>`Product ID`, `Currency`, et `Price` doivent être mappés obligatoirement pour capturer les événements d'achat dans Braze. L'événement d'achat ne peut pas se dérouler si l'un des trois est manqué. |
| Quantité | Sélection déroulante | • Attribut de quantité pour l'action d'achat.<br>• Intégrez l'attribut pertinent au catalogue Zeotap et établissez une correspondance avec ce dernier. |
| Pays | Sélection déroulante | Établissez une correspondance avec le champ de catalogue `Country` que vous intégrez. |
| Ville | Sélection déroulante | Établissez une correspondance avec le champ de catalogue `City` que vous intégrez. |
| Langue | Sélection déroulante | • Le format accepté est la norme `ISO-639-1` (par exemple, en).<br>• Intégrez la langue correctement formatée et établissez une correspondance avec cette dernière. |
| Date de naissance | Sélection déroulante | Établissez une correspondance avec le champ `Date of Birth` que vous intégrez. |
| attribut personnalisé | Entrée de données personnalisées | Mappez tout attribut utilisateur à une entrée de données personnalisées, qui est ensuite envoyée à Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Affichage des données sur la console Braze

Après avoir cartographié les attributs pertinents à envoyer et à publier dans le flux de travail, les événements commencent à circuler vers Braze en fonction des critères définis. Vous pouvez rechercher par ID d'e-mail ou ID externe sur la console Braze.

![][2]

Divers attributs relèvent de différentes sections du tableau de bord utilisateur dans Braze.
- L'onglet **Profil** contient les attributs de l'utilisateur.
- L'onglet **personnalisé** contient les attributs personnalisés définis par l'utilisateur.
- L'onglet **Custom Events** contient l'événement personnalisé défini par l'utilisateur.
- L'onglet **Achats** contient les achats effectués par l'utilisateur sur une période de temps.

## Création de campagne

Les utilisateurs peuvent créer des campagnes dans Braze et activer les utilisateurs en temps réel ou en fonction de l'heure programmée. Les campagnes peuvent être déclenchées en fonction des actions effectuées par l'utilisateur (événement personnalisé, achat) ou des attributs de l'utilisateur.

[1]: {% image_buster /assets/img/zeotap/zeotap5.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap6.jpg %}
[3]: {% image_buster /assets/img/zeotap/zeotap7.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap8.png %}