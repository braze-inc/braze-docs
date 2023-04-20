---
nav_title: Zeotap Symphony
description: "Cet article de référence présente le partenariat entre Braze et Zeotap, une plateforme de données client de nouvelle génération qui fournit des résolutions d’identité, des informations et des enrichissements."
page_type: partner
search_tag: Partenaire
page_order: 30
---

# Zoetap Symphony

L'intégration de Braze et Zoetap Symphony vous permet de créer des orchestrations en temps réel et d'exécuter des campagnes par e-mail et notification push.

- Envoyez des noms et prénoms via Zeotap, en fonction des utilisateurs qui peuvent envoyer des e-mails personnalisés via Braze.
- Envoyez des événements personnalisés ou un événement d'achat en temps réel via Zeotap, en fonction des utilisateurs qui peuvent créer des déclencheurs de campagne dans Braze pour cibler leurs clients.

{% alert note %}
Pour créer des campagnes d'e-mail marketing, intégrez les e-mails bruts à Zeotap en les mappant vers `Email Raw` dans le catalogue Zeotap.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Nom du client | Il s’agit du nom de votre client pour votre compte Braze. Vous pouvez le trouver en accédant à la console Braze. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Instance | Votre instance Braze peut être obtenue auprès de votre gestionnaire d’onboarding Braze ou est disponible sur la [page API overview]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

Cette section fournit des informations concernant les deux méthodes que vous pouvez intégrer à Braze :

### Méthode 1
Dans cette méthode, vous devez effectuer les tâches suivantes :
1. Intégrez le SDK Braze sur votre site Web ou votre application.
2. Intégrez Braze avec Zeotap à l’aide de Symphony.

- `User traits` doit être mappé aux champs Braze respectifs sous l'onglet **Data To Send (Données à envoyer)**. Si vous mappez les attributs `Event` et `Purchase`, cela entraîne la duplication des événements dans Braze.
- Mappez `External ID` vers `User ID` configuré lors du paramétrage du SDK Braze.

Lorsque l’intégration est paramétrée avec succès, vous pouvez créer des campagnes par e-mail et notification push en fonction des attributs personnalisés envoyés à Braze via Symphony.

### Méthode 2
Dans cette méthode, vous pouvez intégrer Braze avec Zeotap à l’aide de Symphony.

- Cette méthode ne prend pas en charge les fonctionnalités d’interface utilisateur de Braze, telles que les messages in-app, les fils d’actualité, les cartes de contenu ou les notifications push.
- Zeotap recommande le mappage des `hashed email` disponibles dans le catalogue Zeotap vers l’`External ID`.

Lorsque l’intégration est paramétrée avec succès, vous ne pouvez créer que des campagnes par e-mail en fonction des attributs personnalisés envoyés à Braze via Symphony.

## Flux de données vers Braze et identifiants pris en charge

Les données seront transmises de Zeotap à Braze à l’aide de l’API de [suivi des utilisateurs](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/). Les points suivants résument le flux de données :

1. Zeotap envoie des champs d’attributs de profil utilisateur, d’attributs personnalisés, d’événements personnalisés et d'achat.
2. Vous pouvez mapper tous les champs pertinents du catalogue Zeotap vers les champs Braze sous l'onglet **Data To Send (Données à envoyer)**.
3. Les données sont ensuite chargées sur Braze.

Vous trouverez des détails sur les différents attributs dans la section [Data To Send (Données à envoyer)](#data-to-send-tab).

## Configuration de la destination

Après avoir appliqué des filtres ou ajouté une condition pour vos utilisateurs dans Symphony, vous pouvez les activer dans Braze sous **Send to Destinations (Envoyer vers les destinations)**. Une nouvelle fenêtre s’ouvre dans laquelle vous pouvez configurer votre destination. Vous pouvez utiliser une destination existante dans la liste des **Available Destinations (Destinations disponibles)** ou en créer une nouvelle.

#### Ajouter une nouvelle destination
Procédez comme suit pour ajouter une nouvelle destination :
1. Cliquez sur **Add New Destination (Ajouter une nouvelle destination)**.
2. Recherchez **Braze**.
3. Ajoutez le **nom du client**, la **clé API** et l'**instance**, puis enregistrez la destination.

La destination est créée et mise à disposition dans **Available Destinations (Destinations disponibles)**.

#### Ajouter des entrées au niveau du flux de travail
Après avoir créé une destination, vous devez ensuite ajouter des entrées au niveau du flux de travail, comme indiqué ci-dessous.
1. Choisissez la destination dans la liste des destinations disponibles à l’aide de la fonctionnalité de recherche.
2. Les champs **Nom du client**, **Clé API** et **Instance** sont automatiquement renseignés en fonction de la valeur que vous avez saisie lors de la création de la destination.
3. Saisissez le **nom de l’audience** que vous souhaitez créer pour ce nœud de flux de travail. Il est envoyé à Braze en tant qu'**attribut personnalisé**.
4. Complétez le mappage du catalogue vers la destination sous l’onglet **Data To Send (Données à envoyer)**. Vous trouverez ci-dessous des détails sur la manière d’effectuer le mappage.

#### Onglet Data To Send (Données à envoyer)
L'onglet **Data To Send (Données à envoyer)** vous permet de mapper les champs du catalogue Zeotap aux champs Braze qui peuvent être envoyés à Braze. Le mappage peut être effectué de l’une des manières suivantes :
- **Mappage statique** : il existe certains champs que Zeotap mappe automatiquement aux champs Braze pertinents tels que l’e-mail, le téléphone, le prénom, le nom de famille, etc.<br>
- **Sélection déroulante** : mappe les champs pertinents ingérés dans Zeotap aux champs Braze fournis dans le menu déroulant.<br>![Diverses caractéristiques utilisateur définies dans Zeotap, telles que la langue, la ville, l'anniversaire, etc.][3]{: style="max-width:70%;"}<br>
- **Saisie de données personnalisées** : ajoute des données personnalisées mappées au champ Zeotap pertinent et les envoie à Braze.<br>![Sélectionner « loyalty_points » comme trait d'utilisateur dans Zeotap.][4]{: style="max-width:70%;"}

## Attributs pris en charge
Vous trouverez des détails sur tous les champs Braze dans cette section.

| Champ de Braze | Type de mappage | Description |
| --- | --- | --- |
| ID externe | Sélection déroulante | Il s’agit du `User ID` persistant que vous avez défini dans Braze pour suivre les utilisateurs sur les appareils et les plateformes. Nous vous recommandons de mapper `User ID` sur `External ID` ; sinon, Zeotap peut envoyer un e-mail en tant qu’alias d’utilisateur.<br><br>Zeotap vous recommande de mapper le `hashed email` disponible dans le catalogue Zeotap sur `External ID`.|
| E-mail | Mappage statique | Ceci est mappé sur `Email Raw` dans le catalogue Zeotap. |
| Téléphone | Mappage statique | Ceci est mappé sur `Mobile Raw` dans le catalogue Zeotap.<br><br>• Braze accepte les numéros de téléphone au format `E.164`. Zeotap n’effectue aucune transformation. Par conséquent, vous devez ingérer les numéros de téléphone au format prescrit. Pour plus d’informations, consultez [Numéros de téléphone utilisateur](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| Prénom | Mappage statique | Ceci est mappé sur `First Name` dans le catalogue Zeotap. |
| Nom | Mappage statique | Ceci est mappé sur `Last Name` dans le catalogue Zeotap. |
| Sexe | Mappage statique | Ceci est mappé sur `Gender` dans le catalogue Zeotap. |
| Nom d’évènement personnalisé | Mappage statique | Ceci est mappé sur `Event Name` dans le catalogue Zeotap.<br><br>Le nom de l'événement personnalisé et l'horodatage de l'événement personnalisé doivent être mappés pour capturer les événements personnalisés dans Braze. L’événement personnalisé ne peut pas être traité si l’un ou l’autre n’est pas mappé. Pour plus d’informations, consultez l’[objet Événement](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object). |
| Horodatage d’événement personnalisé | Mappage statique | Ceci est mappé sur `Event Timestamp` dans le catalogue Zeotap.<br><br>Le nom de l'événement personnalisé et l'horodatage de l'événement personnalisé doivent être mappés pour capturer les événements personnalisés dans Braze. L’événement personnalisé ne peut pas être traité si l’un ou l’autre n’est pas mappé. Pour plus d’informations, consultez l’[objet Événement](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object). |
| Abonnement aux e-mails | Sélection déroulante | Intégrez un champ `Email Marketing Preference` et mappez vers celui-ci.<br><br>Zeotap envoie les trois valeurs suivantes :<br>• `opted_in` : Indique que l’utilisateur s’est explicitement abonné à la préférence marketing par e-mail<br>• `unsubscribed` : Indique que l’utilisateur s’est explicitement désabonné des e-mails<br>• `subscribed` : Indique que l’utilisateur n’e s’est ni abonné ni désabonné. |
| Abonnement aux notifications push | Sélection déroulante | Intégrez un champ `Push Marketing Preference` et mappez vers celui-ci.<br><br>Zeotap envoie les trois valeurs suivantes :<br>• `opted_in` : Indique que l’utilisateur s’est explicitement abonné à la préférence marketing par notification push<br>• `unsubscribed` : Indique que l’utilisateur s’est explicitement désabonné des notifications push.<br>• `subscribed` : Indique que l’utilisateur n’e s’est ni abonné ni désabonné |
| Activation du suivi d’ouverture d’e-mail | Sélection déroulante | Mappez le champ `Marketing Preference` pertinent.<br><br>Lorsqu’il est défini sur « True », il permet d’ajouter un pixel de suivi d’ouverture dans tous les futurs e-mails envoyés à cet utilisateur. |
| Activer le suivi des clics des e-mails | Sélection déroulante | Mappez le champ `Marketing Preference` pertinent.<br><br>Lorsqu’il est défini sur « True », il permet d’activer le suivi de clic pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. |
| ID produit | Sélection déroulante | • Identifiant d’une action d’achat `(Product Name/Product Category)`. Pour plus de détails, consultez [Objet Propriétés d’achat](https://www.braze.com/docs/api/objects_filters/purchase_object/).<br>• Intégrez l'attribut pertinent au catalogue Zeotap et mappez vers celui-ci.<br><br>`Product ID`, `Currency` et `Price` doivent obligatoirement être mappés pour capturer les événements d’achat dans Braze. L’événement d’achat ne peut pas se dérouler si l’un des trois est manqué. Pour plus d’informations, consultez l’[objet Achat](https://www.braze.com/docs/api/objects_filters/purchase_object/#purchase-object). |
| Devise | Sélection déroulante | • Attribut de devise pour l’action d’achat.<br>• Le format pris en charge est `ISO 4217 Alphabetic Currency Code`.<br>• Intègre des données monétaires correctement formatées au catalogue Zeotap et mappe vers celles-ci.<br><br>`Product ID`, `Currency` et `Price` doivent obligatoirement être mappés pour capturer les événements d’achat dans Braze. L’événement d’achat ne peut pas se dérouler si l’un des trois est manqué. |
| Prix | Sélection déroulante | • Attribut de prix pour l’action d’achat.<br>• Intégrez l'attribut pertinent au catalogue Zeotap et mappez vers celui-ci.<br><br>`Product ID`, `Currency` et `Price` doivent obligatoirement être mappés pour capturer les événements d’achat dans Braze. L’événement d’achat ne peut pas se dérouler si l’un des trois est manqué. |
| Quantité | Sélection déroulante | • Attribut de quantité pour l’action d’achat.<br>• Intégrez l'attribut pertinent au catalogue Zeotap et mappez vers celui-ci. |
| Pays | Sélection déroulante | Mappez au champ de catalogue `Country` que vous intégrez. |
| Ville | Sélection déroulante | Mappez au champ de catalogue `City` que vous intégrez. |
| Langue | Sélection déroulante | • Le format accepté est à la norme `ISO-639-1` (par ex., en).<br>• Intègre une langue correctement formatée et mappe vers celle-ci. |
| Date de naissance | Sélection déroulante | Mappez au champ `Date of Birth` que vous intégrez. |
| Attribut personnalisé | Saisie de données personnalisée | Mappe n’importe quel attribut utilisateur à une saisie de données personnalisée qui est ensuite envoyée à Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Afficher les données sur la console Braze

Après avoir mappé les attributs pertinents à envoyer et à publier dans le flux de travail, les événements commencent à circuler vers Braze en fonction des critères définis. Vous pouvez effectuer une recherche par ID d’e-mail ou ID externe sur la console Braze.

![][2]

Différents attributs se trouvent sous différentes sections du tableau de bord de l’utilisateur dans Braze.
- L'onglet **Profile (Profil)** contient les attributs utilisateur.
- L'onglet **Custom Attributes (Attributs personnalisés)** contient les attributs personnalisés définis par l'utilisateur.
- L'onglet **Custom Events (Événements personnalisés)** contient l'événement personnalisé défini par l'utilisateur.
- L’onglet **Purchases (Achats)** contient les achats effectués sur une période donnée par l’utilisateur.

## Création de la campagne

Les utilisateurs peuvent créer des campagnes dans Braze et activer les utilisateurs en temps réel ou en fonction de l'heure planifiée. Les campagnes peuvent être déclenchées en fonction des actions effectuées par l’utilisateur (événement personnalisé, achat) ou des attributs utilisateur.

[1]: {% image_buster /assets/img/zeotap/zeotap5.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap6.jpg %}
[3]: {% image_buster /assets/img/zeotap/zeotap7.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap8.png %}