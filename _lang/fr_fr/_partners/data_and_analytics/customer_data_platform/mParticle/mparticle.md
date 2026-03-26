---
nav_title: mParticle de Rokt
article_title: mParticle de Rokt
alias: /partners/mparticle/
description: "Cet article de référence présente le partenariat entre Braze et mParticle, une plateforme de données client qui collecte et achemine les données entre les sources de votre pile marketing."
page_type: partner
search_tag: Partner

---

# mParticle de Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> La plateforme de données client de mParticle vous permet d'en faire plus avec vos données. Les marketeurs avertis utilisent mParticle pour orchestrer les données dans leur suite d'outils de croissance, et ainsi être performants dans les moments clés du parcours client.

L'intégration de Braze et mParticle vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes :
- Synchronisez les audiences mParticle avec Braze pour les campagnes Braze et la segmentation Canvas.
- Partagez les données entre les deux plateformes. Cela peut se faire grâce à l'intégration du kit mParticle et à l'intégration de serveur à serveur.
- [Envoyez les interactions des utilisateurs de Braze à mParticle par l'intermédiaire de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), afin de les rendre exploitables dans l'ensemble des outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est nécessaire pour profiter de ce partenariat. |
| Instance de Braze | Votre instance Braze se trouve sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints) (par exemple, `US-01` ou `US-02`). |
| Clé d'identification de l'application Braze | Votre clé d'identifiant d'application. <br><br>Vous la trouverez dans **Gérer les paramètres** > **Clé API** dans le tableau de bord de Braze. |
| Clé API REST de l'espace de travail | (De serveur à serveur) Une clé API REST de Braze<br><br>Celle-ci peut être créée dans la **Console de développement** > **Paramètres API** > **Clé API** dans le tableau de bord de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Audiences

Utilisez le partenariat entre Braze et mParticle pour configurer votre intégration et importer les audiences mParticle directement dans Braze pour le reciblage, créant ainsi une boucle complète de données d'un système à l'autre. 

Toute intégration que vous mettez en place enregistrera des points de données. Si vous avez des questions sur les subtilités des points de données de Braze, votre Account Manager Braze peut y répondre.

#### Transférer des audiences

mParticle propose trois façons de définir les attributs d'appartenance à une cohorte, contrôlées par le paramètre de configuration « [Send Segments As](#send_settings) ». Reportez-vous aux sections suivantes pour le traitement de chaque option :

- [Attribut de chaîne de caractères unique](#string)
- [Attribut de tableau unique](#array)
- [Un attribut par segment](#per-segment)
- [Attribut de tableau unique et attribut de chaîne de caractères unique](#both-1)
- [Attribut de tableau unique et un attribut par segment](#both-2)
- [Attribut de chaîne de caractères unique et un attribut par segment](#both-3)
- [Attribut de tableau unique, attribut de chaîne de caractères unique et un attribut par segment](#multi)

##### Attribut de chaîne de caractères unique {#string}

mParticle créera un attribut personnalisé unique appelé `SegmentMembership`. La valeur de cet attribut est une chaîne de caractères d'ID d'audience mParticle séparés par des virgules et correspondant à l'utilisateur. Vous trouverez ces ID d'audience dans le tableau de bord mParticle, sous **Audiences**.

Par exemple, si une audience mParticle « Ibiza dreamers » a un ID d'audience de « 11036 », vous pouvez segmenter ces utilisateurs avec le filtre `SegmentMembership` — `matches regex` — `11036`.

Bien qu'il s'agisse de l'option par défaut dans mParticle, la plupart des utilisateurs optent pour l'utilisation d'[attributs de tableau unique](#array) pour une meilleure expérience de filtrage lors de la création de segments dans Braze.

{% alert important %}
Cette solution n'est pas recommandée si vous avez plus de quelques audiences, car les attributs personnalisés peuvent comporter jusqu'à 255 caractères. Vous ne pourrez donc pas stocker des dizaines ou des centaines d'audiences sur un profil utilisateur avec cette méthode. Si vous avez un grand nombre de cohortes par utilisateur, nous vous recommandons vivement la configuration « un attribut par segment ».
{% endalert %}

![Appartenance à la segmentation mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Attribut de tableau unique {#array}

mParticle crée un attribut de tableau personnalisé dans Braze pour chaque utilisateur, intitulé `SegmentMembershipArray`. La valeur de cet attribut est un tableau d'ID d'audience mParticle correspondant à l'utilisateur.

Par exemple, si un utilisateur est membre de trois audiences mParticle dont les ID d'audience sont « 13053 », « 13052 » et « 13051 », vous pouvez segmenter les utilisateurs qui correspondent à l'une de ces audiences à l'aide du filtre `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
Les attributs de tableau de Braze ont une longueur maximale de 25. Si l'un de vos utilisateurs est membre de plus de 25 audiences, les informations d'appartenance seront tronquées par Braze. Pour contourner ce problème, contactez votre conseiller Braze afin d'augmenter le seuil de longueur maximale de tableau.
{% endalert %}

##### Un attribut par segment {#per-segment}

mParticle créera un attribut personnalisé booléen pour chaque audience à laquelle un utilisateur appartient. Par exemple, si une audience mParticle s'appelle « Possible Parisians », vous pouvez segmenter ces utilisateurs avec le filtre `In Possible Parisians` — `equals` — `true`.

![Attribut personnalisé mParticle]({% image_buster /assets/img_archive/mparticle2.png %})

##### Attribut de tableau unique et attribut de chaîne de caractères unique {#both-1}

mParticle enverra les attributs tels que décrits à la fois pour l'attribut de tableau unique et l'attribut de chaîne de caractères unique.

##### Attribut de tableau unique et un attribut par segment {#both-2}

mParticle enverra les attributs tels que décrits à la fois pour l'attribut de tableau unique et un attribut par segment.

##### Attribut de chaîne de caractères unique et un attribut par segment {#both-3}

mParticle enverra les attributs tels que décrits à la fois pour l'attribut de chaîne de caractères unique et un attribut par segment.

##### Attribut de tableau unique, attribut de chaîne de caractères unique et un attribut par segment {#multi}

mParticle enverra les attributs tels que décrits pour l'attribut de tableau unique, l'attribut de chaîne de caractères unique et un attribut par segment.

#### Étape 1 : Créer une audience dans mParticle {#send_settings}

Pour créer une audience dans mParticle :

1. Naviguez vers **Audiences** > **Single Workspace** > **+ New Audience**.
2. Pour connecter Braze en tant que sortie pour votre audience, vous devez fournir les champs suivants :

| Nom du champ               | Description                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API                  | Vous la trouverez dans le tableau de bord de Braze sous **Paramètres** > **Clés API**.<br><br>Si vous utilisez l'ancienne navigation, vous trouverez les clés API dans **Console de développement** > **Paramètres API**. |
| Système d'exploitation de la clé API | Sélectionnez le système d'exploitation auquel correspond votre clé API Braze. Cette sélection limitera les types de jetons push transmis lors d'une mise à jour de l'audience.                          |
| Envoyer les segments sous forme de         | La méthode d'envoi des audiences à Braze. Pour plus de détails, reportez-vous à la section [Transférer des audiences](#forwarding-audiences).                                                          |
| Clé API REST de l'espace de travail   | Clé API REST de Braze avec toutes les autorisations. Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**.                                                        |
| Type d'identité externe   | Le type d'identité de l'utilisateur mParticle à transmettre comme ID externe à Braze. Nous vous recommandons de laisser la valeur par défaut, Customer ID.                                          |
| Type d'identité e-mail      | Le type d'identité de l'utilisateur mParticle à transmettre comme e-mail à Braze.                                                                                                            |
| Instance Braze           | Indiquez vers quel cluster vos données Braze seront transmises.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3. Enfin, **enregistrez** votre audience.

Vous devriez commencer à voir les audiences se synchroniser avec Braze dans les minutes qui suivent. L'appartenance à l'audience ne sera mise à jour que pour les utilisateurs disposant d'`external_ids` (c'est-à-dire pas pour les utilisateurs anonymes). Pour plus d'informations sur la création d'audiences mParticle pour Braze, consultez la documentation mParticle sur les [paramètres de configuration](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Étape 2 : Segmenter les utilisateurs dans Braze

Dans Braze, pour créer un segment de ces utilisateurs, naviguez vers **Segments** sous **Engagement** et nommez votre segment. Voici deux exemples de segments en fonction de l'option que vous avez sélectionnée pour **Envoyer les segments sous**. Pour plus de détails sur chaque option, consultez la rubrique [Transférer des audiences](#forwarding-audiences).

- **Attribut de tableau unique :** Sélectionnez `SegmentMembershipArray` comme filtre. Ensuite, utilisez l'option « includes value » et saisissez l'ID de l'audience souhaitée. ![Le filtre de segment mParticle « SegmentMembershipArray » défini sur « includes value » avec l'ID de l'audience.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Un attribut par segment :** Sélectionnez votre attribut personnalisé comme filtre. Ensuite, utilisez l'option « equals » et choisissez la logique appropriée. ![Le filtre de segment mParticle « in possible parisians » défini sur « equals » et « true ».]({% image_buster /assets/img_archive/mparticle3.png %})

Une fois enregistré, vous pouvez faire référence à ce segment lors de la création d'un Canvas ou d'une campagne, à l'étape de ciblage des utilisateurs.

#### Désactiver et supprimer des connexions

Étant donné que mParticle ne gère pas directement les segments dans Braze, il ne supprimera pas les segments lorsque la connexion à l'audience mParticle correspondante est supprimée ou désactivée. Dans ce cas, mParticle ne mettra pas à jour les attributs des utilisateurs de l'audience dans Braze pour retirer l'audience de chaque utilisateur.

Avant de supprimer une audience, ajustez les filtres d'audience pour ramener la taille de l'audience à 0. Une fois que le calcul de l'audience est terminé et renvoie 0 utilisateur, supprimez l'audience. L'appartenance à l'audience sera alors mise à jour dans Braze à `false` pour l'option d'attribut unique, ou l'ID de l'audience sera supprimé du format de tableau.

## Mappage des données

Les données peuvent être mappées vers Braze à l'aide de l'[intégration du kit embarqué](#embedded-kit-integration) si vous souhaitez connecter vos applications mobiles et web à Braze par l'intermédiaire de mParticle. Vous pouvez également utiliser l'[intégration API serveur à serveur](#server-api-integration) pour transmettre des données côté serveur à Braze.

Quelle que soit l'approche choisie, vous devez configurer Braze en tant que sortie :

### Configurer vos paramètres de sortie Braze

Dans mParticle, naviguez vers **Setup > Outputs > Add Outputs** et sélectionnez **Braze** pour ouvrir la configuration du kit Braze. **Enregistrez** lorsque vous avez terminé.

| Nom du paramètre | Description |
| ------------ | ----------- |
| Clé d'identification de l'application Braze | Vous trouverez votre clé d'identification de l'application Braze dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. Notez que les clés API seront différentes pour chaque plateforme (iOS, Android et Web). |
| Type d'identité externe | Le type d'identité de l'utilisateur mParticle à transmettre comme ID externe à Braze. Nous vous recommandons de laisser la valeur par défaut, Customer ID. |
| Type d'identité e-mail | Le type d'identité de l'utilisateur mParticle à transmettre sous forme d'e-mail à Braze. Nous vous recommandons de laisser la valeur par défaut, Email. |
| Instance Braze | Le cluster vers lequel vos données Braze seront transférées ; il doit s'agir du même cluster que celui sur lequel se trouve votre tableau de bord. |
| Activer le transfert du flux d'événements | (De serveur à serveur) Lorsque cette option est activée, tous les événements sont transmis en temps réel. Dans le cas contraire, tous les événements seront transmis en bloc. Lorsque vous choisissez d'activer le transfert du flux d'événements, assurez-vous que les données que vous transmettez à Braze respectent les [limites de débit]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Intégration du kit embarqué

Les SDK mParticle et Braze seront présents dans votre application grâce à l'intégration du kit embarqué. Cependant, contrairement à une intégration Braze directe, mParticle se charge d'appeler la majorité des méthodes du SDK Braze à votre place. Les méthodes mParticle que vous utilisez pour suivre les données des utilisateurs seront automatiquement mappées aux méthodes du SDK Braze. 

Ces mappages du SDK mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et le [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) sont en open source et peuvent être consultés sur [la page GitHub de mParticle](https://github.com/mparticle-integrations). 

L'intégration SDK du kit embarqué vous permet de profiter de notre suite complète de fonctionnalités (push, messages in-app et tout le suivi analytique des messages).

{% alert note %}
Pour les cartes de contenu et les intégrations de messages in-app personnalisées, appelez directement les méthodes du SDK Braze.
{% endalert %}

#### Étape 1 : Intégrer les SDK mParticle

Intégrez les SDK mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticle pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle pour le Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Étape 2 : Finaliser l'intégration du kit d'événements Braze de mParticle

Bien qu'il ne soit pas nécessaire d'inclure directement le SDK Braze dans votre site web ou votre application pour cette intégration mParticle, le kit mParticle Appboy suivant doit être installé pour transmettre les données de votre application à Braze.

Le [guide d'intégration du kit d'événements Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle vous accompagnera dans les instructions d'alignement personnalisé de mParticle et Braze en fonction de vos besoins en matière d'envoi de messages (push, suivi de localisation, etc.).

#### Étape 3 : Paramètres de connexion pour votre sortie Braze

Dans mParticle, accédez à **Connections** > **Connect** > **[la plateforme de votre choix]** > **Connect Output** pour ajouter Braze en tant que sortie. Sélectionnez ensuite **Save**.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Tous les paramètres de connexion ne s'appliquent pas à toutes les plateformes et à tous les types d'intégration. Pour connaître les paramètres de connexion et les plateformes auxquelles ils s'appliquent, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Intégration de l'API serveur

Il s'agit d'un module complémentaire permettant d'acheminer vos données backend vers Braze si vous utilisez les SDK côté serveur de mParticle (par exemple, Ruby, Python, etc.). Pour mettre en place cette intégration de serveur à serveur avec Braze, suivez les instructions disponibles dans la [documentation de mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
L'intégration serveur à serveur ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou les notifications push. Il existe également des données saisies automatiquement, telles que des champs au niveau de l'appareil, qui ne sont pas disponibles par le biais de cette méthode. 

Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.

Pour que les données côté serveur soient transmises à Braze, elles doivent inclure un `external_id` ; les utilisateurs anonymes ne seront pas transmis.
{% endalert %}

#### Paramètres de connexion pour votre sortie Braze

Dans mParticle, accédez à **Connections > Connect > [la plateforme de votre choix] > Connect Output** pour ajouter Braze en tant que sortie. **Enregistrez** lorsque vous avez terminé. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

Tous les paramètres de connexion ne s'appliquent pas à toutes les plateformes et à tous les types d'intégration. Pour connaître les paramètres de connexion et les plateformes auxquelles ils s'appliquent, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Avant d'activer les options « Enriched User Attributes » ou « Enriched User Identities », nous vous recommandons de consulter la section [Surcharges de points de données](#potential-data-point-overages) afin de comprendre l'impact de ces paramètres sur l'utilisation des points de données.

### Détails du mappage des données

#### Types de données
Tous les types de données ne sont pas pris en charge par les deux plateformes.
- Les [propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date. Elles ne prennent pas en charge les tableaux ni les objets imbriqués.
- Les [attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) prennent en charge les chaînes de caractères, les nombres, les booléens, les objets de date et les tableaux, mais pas les objets ni les objets imbriqués. 

{% alert note %}
Braze ne prend pas en charge les horodatages antérieurs à l'année 0 ou postérieurs à l'année 3000 dans les attributs personnalisés de type `Time`. Braze ingérera ces valeurs lorsqu'elles seront envoyées par mParticle, mais la valeur sera stockée sous forme de chaîne de caractères.
{% endalert %}

#### Mappage des données

| Type de données mParticle | Type de données Braze | Description |
| ------------------- | --------------- | ----------- |
| Attributs de l'utilisateur (réservés) | Attribut standard | Par exemple, la clé d'attribut utilisateur réservée `$FirstName` de mParticle est mappée au champ d'attribut standard `first_name` de Braze. |
| Attributs de l'utilisateur (autres) | Attribut personnalisé | Tout attribut utilisateur transmis à mParticle qui n'entre pas dans le cadre des clés d'attribut utilisateur réservées est enregistré dans Braze en tant qu'attribut personnalisé.<br><br>Les attributs utilisateur prennent en charge les chaînes de caractères, les nombres, les booléens, les dates et les tableaux, mais pas les objets ni les objets imbriqués. |
| Événement personnalisé | Événement personnalisé | Les événements personnalisés mParticle sont reconnus par Braze comme des événements personnalisés. Les attributs d'événements sont transmis en tant que propriétés d'événements personnalisés.<br><br>Les attributs d'événement transmis à Braze en tant que propriétés d'événement prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date, mais pas les tableaux ni les objets imbriqués. |
| Événement commercial d'achat | Événement d'achat | Les événements commerciaux d'achat seront mappés aux événements d'achat de Braze. <br><br>Basculez la valeur du paramètre pour les données d'événement de commerce groupé afin d'enregistrer les achats au niveau de la commande ou du produit. Par exemple, si `false`, un événement entrant unique avec deux produits, promotions ou impressions uniques donnera lieu à au moins deux événements sortants de Braze. S'il est défini sur `true`, il en résultera un événement sortant unique avec un tableau imbriqué de produits, de promotions ou d'impressions, respectivement.<br><br>Pour plus d'informations sur les autres champs commerciaux qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Lorsque vous définissez « bundle commerce event data » sur `false`, les attributs de produit transmis à Braze en tant que propriétés d'événement d'achat prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ni les objets imbriqués.|
| Tous les autres événements commerciaux | Événement personnalisé | Tous les autres événements commerciaux seront mappés à des événements personnalisés. <br><br>Basculez la valeur du paramètre pour les données d'événement de commerce groupé afin d'enregistrer les achats au niveau de la commande ou du produit. Par exemple, si `false`, un événement entrant unique avec deux produits, promotions ou impressions uniques donnera lieu à au moins deux événements sortants de Braze. S'il est défini sur `true`, il en résultera un événement sortant unique avec un tableau imbriqué de produits, de promotions ou d'impressions, respectivement.<br><br>En plus de certaines valeurs commerciales par défaut, les attributs des produits seront enregistrés en tant que propriétés d'événement de Braze. Pour plus d'informations sur les autres champs commerciaux qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Lorsque vous définissez « bundle commerce event data » sur `false`, les attributs de produit transmis à Braze en tant que propriétés d'événement prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ni les objets imbriqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Mappage de l'identité de l'utilisateur
Pour chaque sortie mParticle, vous pouvez sélectionner le type d'identité externe à envoyer à Braze en tant que `external_id`. Bien que la valeur par défaut soit Customer ID, vous pouvez choisir de mapper un autre ID, tel que `MPID`, pour l'envoyer à Braze en tant que `external_id`. Sachez que le choix d'un identifiant autre que Customer ID peut influencer la manière dont les données sont envoyées dans Braze. 

Par exemple, le mappage de MPID à votre `external_id` Braze aura les effets suivants :
- En raison du moment où le MPID est attribué, tous les utilisateurs se verront assigner un `external_id` dès le début de la session.
- La configuration de Currents peut nécessiter un mappage supplémentaire en raison des différences de types de données entre MPID et `external_id`.

### Transmission des requêtes d'effacement (requêtes des personnes concernées)

Transmettez les requêtes d'effacement à Braze en configurant une sortie de requête de la personne concernée vers Braze. Pour transmettre les requêtes d'effacement à Braze, suivez les instructions fournies dans la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Surcharges potentielles de points de données

### Attributs de l'utilisateur enrichis

#### Activation de l'enrichissement des attributs/identités des utilisateurs (serveur à serveur uniquement) {#enriched}

Dans les paramètres de connexion de mParticle, Braze recommande de désactiver l'option **Include Enriched User Attributes**. Si cette option est activée, mParticle transmet à Braze tous les attributs utilisateur disponibles (tels que les attributs standard, les attributs personnalisés et les attributs calculés) du profil existant pour chaque événement enregistré. Il en résulte une consommation élevée de points de données, car mParticle envoie à Braze les mêmes attributs inchangés à chaque appel.

Par exemple, si un utilisateur ajoute son prénom, son nom et son numéro de téléphone lors de sa première session, puis s'inscrit plus tard à une newsletter en ajoutant les mêmes informations ainsi qu'un e-mail, ce qui déclenche un événement d'inscription à la newsletter :
- Si cette option est activée (par défaut), cinq points de données seront comptabilisés (événement d'inscription, adresse e-mail, prénom, nom de famille et numéro de téléphone).
- Si cette option est désactivée, deux points de données seront comptabilisés (événement d'inscription et adresse e-mail).

{% alert note %}
Désactiver ce paramètre ne vérifiera pas si les données ont changé. Cela empêchera toutefois l'intégration d'envoyer tous les attributs du profil utilisateur qui n'ont pas été reçus dans le lot entrant initial ou qui n'ont pas été explicitement définis en tant qu'attributs pour l'événement. Il reste important de vérifier que seuls les deltas sont transmis à Braze.
{% endalert %}

#### Points à considérer lors de la désactivation des attributs enrichis de l'utilisateur

Quelques points méritent votre attention lorsque vous désactivez l'option **Include Enriched User Attributes** :
1. L'intégration serveur à serveur utilise l'API des événements mParticle pour envoyer des événements à Braze. Chaque requête est déclenchée par un événement. Lorsqu'un attribut utilisateur est modifié, comme la mise à jour d'une adresse e-mail, mais qu'il n'est pas associé à un événement spécifique (par exemple, un événement personnalisé de mise à jour du profil), la nouvelle valeur n'est transmise à une sortie comme Braze qu'en tant qu'« attribut enrichi » dans la charge utile du prochain événement déclenché par l'utilisateur. Lorsque l'option **Include Enriched User Attributes** est désactivée, cette nouvelle valeur d'attribut non associée à un événement spécifique ne sera pas transmise à Braze.
  - Pour résoudre ce problème, nous vous recommandons de créer un événement séparé « user attribute updated » qui n'envoie à Braze que le ou les attributs utilisateur spécifiques qui ont été mis à jour. Notez qu'avec cette approche, vous enregistrez toujours un point de données supplémentaire pour l'événement « user attribute updated », mais l'utilisation des points de données sera bien moindre que l'envoi de tous les attributs utilisateur à chaque appel lorsque la fonctionnalité est activée.
2. Les attributs calculés sont transmis à Braze en tant qu'attributs d'utilisateur enrichis. Lorsque l'option « Enriched User Attributes » est désactivée, ces attributs ne sont plus transmis à Braze. Pour transmettre des attributs calculés à Braze lorsque les « Enriched User Attributes » sont désactivés, un [flux d'attributs calculés](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) peut vous aider sans pousser tous les attributs. Le flux envoie une mise à jour en aval à Braze lorsqu'un attribut calculé est modifié. 

## Résolution des problèmes

### Résolution des problèmes de notifications push iOS avec le kit d'événements Braze

Si les notifications push ne fonctionnent pas lorsque vous utilisez le kit d'événements Braze (intégration du kit embarqué) sur iOS, vérifiez les points suivants :
1. **Transfert des jetons push :** Confirmez que mParticle transmet bien les jetons push à Braze. Dans votre tableau de bord mParticle, vérifiez que la connexion du kit Braze a le push activé et que le bon certificat push Apple est configuré dans le tableau de bord de Braze.
2. **Ordre d'initialisation du kit :** Le kit Braze doit être initialisé avant que votre application ne demande les autorisations push. Si les autorisations push sont demandées avant que le kit ne soit actif, le jeton push peut ne pas être transmis à Braze. Vérifiez que le SDK mParticle est démarré tôt dans le cycle de vie de votre application.
3. **Method swizzling :** Le kit Apple de mParticle utilise le method swizzling pour transmettre automatiquement les jetons push et gérer les événements de notification push. Si vous avez désactivé le swizzling ou qu'un autre SDK interfère, les jetons push peuvent ne pas atteindre Braze. Vérifiez que le swizzling est activé dans votre configuration mParticle.
4. **Gestion manuelle des jetons :** Si vous gérez les jetons push manuellement (par exemple, en implémentant `application:didRegisterForRemoteNotificationsWithDeviceToken:`), assurez-vous de transmettre le jeton à mParticle en l'assignant à la propriété du jeton de notification push, par exemple : `MParticle.sharedInstance().pushNotificationToken = deviceToken`. Le kit le transmettra ensuite à Braze.
5. **Incohérence d'environnement :** Confirmez que l'environnement du certificat APNs (développement vs. production) correspond au build de votre application. Pour plus de détails, consultez la [résolution des problèmes de push iOS]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/ios/).

### Envoi de données inutiles ou en double à Braze
Braze comptabilise un point de données chaque fois qu'un attribut est transmis, même si la valeur reste inchangée. C'est pourquoi Braze recommande de ne transmettre que les données nécessaires aux actions dans Braze et de s'assurer que seuls les deltas des attributs sont envoyés.