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

> La plateforme de données client de mParticle vous permet d'en faire plus avec vos données. Les marketeurs avertis utilisent mParticle pour orchestrer les données dans leur suite d’outils de croissance, et ainsi être performants dans les moments clés du parcours client.

L'intégration de Braze et mParticle vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes :
- Synchronisez les audiences mParticle avec Braze pour les campagnes Braze et la segmentation Canvas.
- Partager les données entre les deux plateformes. Cela peut se faire grâce à l'intégration du kit mParticle et à l'intégration de serveur à serveur.
- [Envoyez les interactions des utilisateurs de Braze à mParticle par l'intermédiaire de Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), afin de les rendre exploitables dans l'ensemble de l'outil de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est nécessaire pour profiter de ce partenariat. |
| instance Braze | Votre instance Braze se trouve sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints) (par exemple, `US-01` ou `US-02`). |
| Clé d'identification de l'application Braze | L'identifiant de votre application est essentiel. <br><br>Vous trouverez cette clé dans le **tableau de bord de Braze > Gérer les paramètres > Clé API**. |
| Clé API REST de l'espace de travail | (De serveur à serveur) Une clé API REST de Braze<br><br>Elle peut être créée dans le **tableau de bord Braze > Console de développement > Paramètres API > Clé API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Audiences

Utilisez le partenariat entre Braze et mParticle pour configurer votre intégration et importer les audiences mParticle directement dans Braze pour le reciblage, créant ainsi une boucle complète de données d'un système à l'autre. Toute intégration que vous mettez en place sera prise en compte dans le volume de points données de votre compte.

#### Transférer des audiences

mParticle propose trois façons de définir les attributs d'appartenance à une cohorte, contrôlées par le paramètre de configuration "[Send Segments As" (Envoyer les segments en tant que](#send_settings)). Reportez-vous aux sections suivantes pour le traitement de chaque option :

- [Attribut d'une seule chaîne de caractères](#string)
- [Attribut de tableau unique](#array)
- [Un attribut par segmentation](#per-segment)
- [Attribut de tableau unique et attribut de chaîne de caractères unique](#both-1)
- [À la fois un attribut de tableau unique et un attribut par segment](#both-2)
- [Attribut d'une seule chaîne de caractères et un attribut par segment](#both-3)
- [Un seul attribut de tableau, un seul attribut de chaîne de caractères et un attribut par segment.](#multi)

##### Attribut d'une seule chaîne de caractères {#string}

mParticle créera un attribut personnalisé unique appelé `SegmentMembership`. La valeur de cet attribut est une chaîne de caractères d'ID d'audience mParticle séparés par des virgules et correspondant à l'utilisateur. Vous trouverez ces ID d'audience dans le tableau de bord mParticle, sous **Audiences**.

Par exemple, si une audience mParticle "Ibiza dreamers" a un ID d'audience de "11036", vous pouvez segmenter ces utilisateurs avec le filtre `SegmentMembership` - `matches regex` - `11036`.

Bien qu'il s'agisse de l'option par défaut dans mParticle, la plupart des utilisateurs de Braze optent pour l'utilisation d'[attributs de tableau unique](#array) pour l'expérience de filtrage lors de la création de segments dans Braze.

{% alert important %}
Cette solution n'est pas recommandée si vous avez plus de quelques audiences, car les attributs personnalisés peuvent comporter jusqu'à 255 caractères. Vous ne pourrez donc pas stocker des dizaines ou des centaines d'audiences sur un profil utilisateur à l'aide de cette méthode. Si vous avez un grand nombre de cohortes par utilisateur, nous vous recommandons vivement la configuration "un attribut par segment".
{% endalert %}

![Appartenance à la segmentation mParticle][6]

##### Attribut de tableau unique {#array}

mParticle crée un attribut de tableau personnalisé dans Braze pour chaque utilisateur, intitulé `SegmentMembershipArray`. La valeur de cet attribut est un tableau d'ID d'audience mParticle correspondant à l'utilisateur.

Par exemple, si un utilisateur est membre de trois audiences mParticle dont les ID d'audience sont "13053", "13052" et "13051", vous pouvez segmenter les utilisateurs qui correspondent à l'une de ces audiences à l'aide du filtre `SegmentMembershipArray` - `includes value` - `13051`.

{% alert note %}
Les attributs des réseaux de Braze ont une longueur maximale de 25. Si l'un de vos utilisateurs est membre de plus de 25 audiences, les informations relatives à l'adhésion seront tronquées par Braze. Pour contourner ce problème, contactez votre représentant Braze pour augmenter votre seuil de longueur maximale de réseau.
{% endalert %}

##### Un attribut par segmentation {#per-segment}

mParticle créera un attribut personnalisé booléen pour chaque audience à laquelle un utilisateur appartient. Par exemple, si une audience mParticle s'appelle "Parisiens possibles", vous pouvez segmenter ces utilisateurs avec le filtre `In Possible Parisians` - `equals` - `true`.

![Attribut personnalisé mParticle][7]

##### Attribut de tableau unique et attribut de chaîne de caractères unique {#both-1}

mParticle enverra les attributs tels qu'ils sont décrits à la fois dans un tableau de chaînes de caractères et dans une chaîne de caractères.

##### À la fois un attribut de tableau unique et un attribut par segment {#both-2}

mParticle enverra les attributs tels qu'ils sont décrits à la fois dans un tableau unique d'attributs et dans un attribut par segment.

##### Attribut d'une seule chaîne de caractères et un attribut par segment {#both-3}

mParticle enverra les attributs tels qu'ils sont décrits à la fois par une seule chaîne de caractères et par un attribut par segment.

##### Un seul attribut de tableau, un seul attribut de chaîne de caractères et un attribut par segment. {#multi}

mParticle enverra les attributs tels que décrits par un seul attribut tableau chaînes de caractères, un seul attribut chaîne de caractères et un attribut par segmentation.

#### Étape 1 : Créez une audience dans mParticle {#send_settings}

Pour créer une audience dans mParticle :

1. Naviguez vers **Audiences** > **Espace de travail unique** > **\+ Nouvelle audience.**
2. Pour connecter Braze en tant que sortie pour votre audience, vous devez fournir les champs suivants :

| Nom du champ               | Description                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clé API                  | Vous les trouverez dans le tableau de bord de Braze sous **Paramètres** > **Clés API**.<br><br>Si vous utilisez l'ancienne interface, vous trouverez les clés API dans **Console de développement** > **Paramètres API**. |
| Système d'exploitation de la clé API | Sélectionnez le système d'exploitation auquel correspond votre clé API Braze. Cette sélection limitera les types de jetons push transmis lors d'une mise à jour de l'audience.                          |
| Envoyez les segments sous forme de         | La méthode d'envoi des audiences à Braze. Pour plus de détails, reportez-vous à la section [Transférer des audiences](#forwarding-audiences).                                                          |
| Clé API REST de l'espace de travail   | Clé API REST de Braze avec toutes les autorisations. Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.                                                        |
| Type d'identité externe   | Le type d'identité de l'utilisateur mParticle à transmettre comme ID externe à Braze. Nous vous recommandons de laisser la valeur par défaut, ID de client.                                          |
| Type d'identité e-mail      | Le type d'identité de l'utilisateur mParticle à transmettre comme e-mail à Braze.                                                                                                            |
| instance Braze           | Indiquez vers quel cluster vos données Braze seront transmises.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. Enfin, **enregistrez** votre audience.

Vous devriez commencer à voir les audiences se synchroniser avec Braze dans les minutes qui suivent. La composition de l'audience ne sera mise à jour que pour les utilisateurs disposant de `external_ids` (c'est-à-dire pas pour les utilisateurs anonymes). Pour plus d'informations sur la création de l'audience mParticle de Braze, consultez la documentation mParticle sur les [paramètres de configuration](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Étape 2 : Segmentation des utilisateurs à Braze

Dans Braze, pour créer un segment de ces utilisateurs, naviguez vers **Segments** sous **Engagement** et nommez votre segment. Voici deux exemples de segments en fonction de l'option que vous avez sélectionnée pour **Envoyer les segments sous.** Pour plus de détails sur chaque option, consultez la section [Transférer des audiences](#forwarding-audiences.)

- **Attribut de tableau unique :** Sélectionnez `SegmentMembershipArray` comme filtre. Ensuite, utilisez l'option "inclut la valeur" et saisissez l'ID de l'audience souhaitée. ![Le filtre de segment mParticle "TableauadhésionSegment" doit être défini sur "inclut la valeur" avec l'ID de l'audience.][11]<br><br>
- **Un attribut par segment :** Sélectionnez votre attribut personnalisé comme filtre. Ensuite, utilisez l'option "est égal" et choisissez la logique appropriée. ![Le filtre de segments mParticle "dans les Parisiens possibles" est défini sur "est égal" et "vrai".][8]

Une fois enregistré, vous pouvez faire référence à ce segment lors de la création d'un canvas ou d'une campagne à l'étape du ciblage des utilisateurs.

#### Désactiver et supprimer des connexions

Étant donné que mParticle ne gère pas directement les segments dans Braze, il ne supprimera pas les segments lorsque la connexion à l'audience mParticle correspondante est supprimée ou désactivée. Lorsque cela se produit, mParticle ne met pas à jour les attributs des utilisateurs de l'audience dans Braze pour supprimer l'audience de chaque utilisateur.

Avant de supprimer l'audience d'un utilisateur de Braze, ajustez les filtres d'audience pour définir la taille de l'audience sur 0 avant de la supprimer. Une fois que le calcul de l'audience est terminé et que le nombre d'utilisateurs est nul, supprimez l'audience. Ensuite, l'appartenance à l'audience sera mise à jour dans Braze sur `false` pour l'option d'attribut unique ou l'ID de l'audience sera supprimé du format de tableau.

## Mappage des données

Les données peuvent être mappées vers Braze à l'aide de l'[intégration du kit embarqué](#embedded-kit-integration) si vous souhaitez connecter vos applications mobiles et web à Braze par l'intermédiaire de mParticle. Vous pouvez également utiliser l'[intégration API serveur à serveur](#server-api-integration) pour transmettre des données côté serveur à Braze.

Quelle que soit l'approche choisie, vous devez configurer Braze en tant que sortie :

### Configurez vos paramètres de sortie de Braze

Dans mParticle, naviguez vers **Configuration > Sorties > Ajouter des sorties** et sélectionnez **Braze** pour ouvrir la configuration du kit Braze. **Enregistrez** lorsque vous avez terminé.

| Nom du paramètre | Description |
| ------------ | ----------- |
| Clé d'identification de l'application Braze | Vous trouverez votre clé d'identification de l'application Braze dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API.** Notez que les clés API seront différentes pour chaque plateforme (iOS, Android et Web). |
| Type d'identité externe | Le type d'identité de l'utilisateur mParticle à transmettre comme ID externe à Braze. Nous vous recommandons de laisser la valeur par défaut, ID du client. |
| Type d'identité e-mail | Le type d'identité de l'utilisateur mParticle à transmettre sous forme d'e-mail à Braze. Nous vous recommandons de laisser la valeur par défaut, E-mail, |
| instance Braze | Le cluster vers lequel vos données Braze seront transférées ; il doit s'agir du même cluster que celui sur lequel se trouve votre tableau de bord. |
| Activer le transfert des flux d'événements | (De serveur à serveur) Lorsque cette option est activée, tous les événements sont transmis en temps réel. Si ce n'est pas le cas, tous les événements seront transmis en bloc. Lorsque vous choisissez d'activer la transmission de flux d'événements, assurez-vous que les données que vous transmettez à Braze respectent les [limites de débit]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][10]

### Intégration de kits embarqués

Les SDK mParticle et Braze seront présents dans votre application grâce à l'intégration du kit embarqué. Cependant, contrairement à une intégration Braze directe, mParticle se charge d'appeler la majorité des méthodes du SDK Braze pour vous. Les méthodes mParticle que vous utilisez pour suivre les données des utilisateurs seront automatiquement mappées aux méthodes du SDK de Braze. 

Ces mappages du SDK de mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et le [Web](https://github.com/Appboy/integration-appboy) sont en open source et peuvent être trouvés sur [la page GitHub de mParticle.](https://github.com/mparticle-integrations) 

L'intégration SDK du kit embarqué vous permet de profiter de notre suite complète de fonctionnalités (push, messages in-app, et tout le suivi analytique des messages pertinents).

{% alert note %}
Pour les cartes de contenu et les intégrations de messages in-app personnalisées, appelez directement les méthodes du SDK Braze.
{% endalert %}

#### Étape 1 : Intégrer les SDK mParticle

Intégrez les SDK mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticle pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle pour le Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Étape 2 : Achever l'intégration du kit d'événements de Braze de mParticle

Bien qu'il ne soit pas nécessaire d'inclure directement le SDK Braze dans votre site Web ou votre application pour cette intégration mParticle, le kit mParticle Appboy suivant doit être installé pour transmettre les données de votre application à Braze.

Le [guide d'intégration du kit d'événement Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle vous guidera dans les instructions d'alignement personnalisé de mParticle et de Braze en fonction de vos besoins en matière d'envoi de messages (Push, suivi d'emplacement/localisation, etc.).

#### Étape 3 : Paramètres de connexion pour votre sortie Braze

Dans mParticle, accédez à **Connexions > Connecter > [Votre plateforme souhaitée] > Connecter la sortie** pour ajouter Braze en tant que sortie. **Enregistrez** lorsque vous avez terminé.

![][3]

Tous les paramètres de connexion ne s'appliquent pas à toutes les plateformes et à tous les types d'intégration. Pour connaître les paramètres de connexion et les plateformes auxquelles ils s'appliquent, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Intégration de l'API du serveur

Il s'agit d'un module complémentaire permettant d'acheminer vos données vers Braze si vous utilisez les SDK côté serveur de mParticle (par exemple, Ruby, Python, etc.). Pour mettre en place cette intégration de serveur à serveur avec Braze, suivez les instructions disponibles dans la [documentation de mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
L'intégration serveur à serveur ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou les notifications push. Il existe également des données saisies automatiquement, telles que des champs au niveau de l'appareil, qui ne sont pas disponibles par le biais de cette méthode. 

Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.

Pour que les données côté serveur soient transmises à Braze, elles doivent inclure un `external_id` ; les utilisateurs anonymes ne seront pas transmis.
{% endalert %}

#### Paramètres de connexion pour votre sortie Braze

Dans mParticle, accédez à **Connexions > Connecter > [Votre plateforme souhaitée] > Connecter la sortie** pour ajouter Braze en tant que sortie. **Enregistrez** lorsque vous avez terminé. 

![][4]

Tous les paramètres de connexion ne s'appliquent pas à toutes les plateformes et à tous les types d'intégration. Pour connaître les paramètres de connexion et les plateformes auxquelles ils s'appliquent, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Avant d'activer les options "Attributs d'utilisateur enrichis" ou "Identités d'utilisateur enrichies", nous vous recommandons d'examiner les [dépassements de points de données](#potential-data-point-overages) afin de vous assurer que vous êtes conscient de l'impact de ces paramètres sur l'utilisation des points de données.

### Détails du mappage des données

#### Types de données
Tous les types de données ne sont pas pris en charge par les deux plateformes.
- Les [propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date. Il ne prend pas en charge les tableaux ou les objets imbriqués.
- Les [attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) prennent en charge les chaînes de caractères, les nombres, les booléens, les objets de date et les tableaux, mais pas les objets ni les objets imbriqués. 

{% alert note %}
Braze ne prend pas en charge les horodatages antérieurs à l'année 0 ou postérieurs à l'année 3000 dans les attributs personnalisés de type `Time`. Braze ingère ces valeurs lorsqu'elles sont envoyées par mParticle, mais la valeur est stockée sous la forme d'une chaîne de caractères.
{% endalert %}

#### Mappage des données

| Type de données mParticle | Type de données Braze | Description |
| ------------------- | --------------- | ----------- |
| Attributs de l'utilisateur (réservés) | Attribut standard | Par exemple, la clé d'attribut utilisateur réservée `$FirstName` de mParticle est mappée au champ d'attribut standard `first_name` de Braze. |
| Attributs de l'utilisateur (autres) | Attribut personnalisé | Tout attribut utilisateur transmis à mParticle qui n'entre pas dans le cadre des clés d'attribut utilisateur réservées est enregistré dans Braze en tant qu'attribut personnalisé.<br><br>Les attributs utilisateurs prennent en charge les chaînes de caractères, les nombres, les booléens, les dates et les tableaux, mais pas les objets ni les objets imbriqués. |
| Événement personnalisé | Événement personnalisé | Les événements personnalisés mParticle sont reconnus par Braze comme des événements personnalisés. Les attributs d'événements sont transmis en tant que propriétés d'événements personnalisés.<br><br>Les attributs d'événement transmis à Braze en tant que propriétés d'événement prennent en charge les objets de type chaîne, numérique, booléen ou date, mais pas les tableaux ni les objets imbriqués. |
| Événement commercial d’achat | Achat d'un événement | Les événements commerciaux d'achat seront mappés aux événements d'achat de Braze. <br><br>Basculer la valeur du paramètre pour les données d'événement de commerce groupé afin d'enregistrer les achats au niveau de la commande ou du produit. Par exemple, si `false`, un événement entrant unique avec deux produits, promotions ou impressions uniques donnera lieu à au moins deux événements sortants de Braze. S'il est défini sur `true`, il en résultera un événement sortant unique avec un tableau imbriqué de produits, de promotions ou d'impressions, respectivement.<br><br>Pour plus d'informations sur les autres champs commerciaux qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Lorsque vous définissez "bundle commerce event data" comme `false`, les attributs de produit transmis à Braze en tant que propriétés d'événement d'achat prennent en charge les objets de type chaîne, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ou les objets imbriqués.|
| Tous les autres événements commerciaux | Événement personnalisé | Tous les autres événements commerciaux seront mappés à des événements personnalisés. <br><br>Basculer la valeur du paramètre pour les données d'événement de commerce groupé afin d'enregistrer les achats au niveau de la commande ou du produit. Par exemple, si `false`, un événement entrant unique avec deux produits, promotions ou impressions uniques donnera lieu à au moins deux événements sortants de Braze. S'il est défini sur `true`, il en résultera un événement sortant unique avec un tableau imbriqué de produits, de promotions ou d'impressions, respectivement.<br><br>En plus de certaines valeurs commerciales par défaut, les attributs des produits seront enregistrés en tant que propriétés d'événement de Braze. Pour plus d'informations sur les autres champs commerciaux qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Lorsque vous définissez "bundle commerce event data" comme `false`, les attributs de produit transmis à Braze en tant que propriétés d'événement prennent en charge les objets de type chaîne, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ou les objets imbriqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Mappage de l'identité de l'utilisateur
Pour chaque sortie de mParticle, vous pouvez sélectionner le type d'identité externe à envoyer à Braze en tant que `external_id`. Bien que la valeur par défaut soit l'ID du client, vous pouvez choisir de mapper un autre ID, tel que `MPID`, pour l'envoyer à Braze en tant que `external_id`. Sachez que le choix d'un identifiant autre que l'ID client peut influencer la manière dont les données sont envoyées dans Braze. 

Par exemple, le mappage de MPID à votre paramètre Braze `external_id` aura pour effet :
- En raison de la nature de l'attribution du MPID, tous les utilisateurs se verront attribuer une adresse `external_id` au début de la session.
- La configuration actuelle peut nécessiter un mappage supplémentaire en raison des différences de types de données entre MPID et `external_id`.

### Transmission des requêtes d'effacement (requêtes des personnes concernées).

Transmettez les requêtes d'effacement à Braze en configurant une sortie de requête de la personne concernée vers Braze. Pour transmettre les requêtes d'effacement à Braze, suivez les instructions fournies dans la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Surcharges potentielles de points de données

### Attributs de l'utilisateur enrichis

#### Activation de l'enrichissement des attributs/identités des utilisateurs (serveur à serveur uniquement) {#enriched}

Dans les paramètres de connexion de mParticle, Braze recommande de désactiver l'option **Inclure les attributs d'utilisateur enrichis**. Si cette option est activée, mParticle transmet à Braze tous les attributs utilisateur disponibles (tels que les attributs standard, les attributs personnalisés et les attributs calculés) du profil existant pour chaque événement journal des utilisateurs. Il en résultera une forte consommation de points de données, car mParticle enverra à Braze les mêmes attributs inchangés à chaque appel.

Par exemple, si un utilisateur ajoute son prénom, son nom et son numéro de téléphone lors de sa première session et qu'il s'inscrit ensuite à une lettre d'information en ajoutant les mêmes informations, en plus de son e-mail, cela déclenche un événement d'inscription à la lettre d'information :
- Si cette option est activée (par défaut), cinq points de données seront enregistrés. (événement d'inscription, adresse e-mail, prénom, nom de famille et numéro de téléphone)
- Si cette option est désactivée, deux points de données seront enregistrés (événement d'inscription et adresse e-mail).

{% alert note %}
Si vous désactivez ce paramètre, il ne sera pas vérifié si les données ont changé. Elle empêchera toutefois l'intégration d'envoyer tous les attributs du profil utilisateur qui n'ont pas été reçus dans le lot entrant initial ou qui n'ont pas été explicitement définis en tant qu'attributs pour l'événement. Il est important de vérifier que seuls les deltas sont transmis à Braze.
{% endalert %}

#### Considérations relatives à la désactivation des attributs enrichis de l'utilisateur

Il y a quelques considérations à prendre en compte lorsque vous désactivez l'option **Inclure les attributs d'utilisateur enrichis :**
1. L'intégration serveur à serveur utilise l'API des événements mParticle pour envoyer des événements à Braze. Chaque requête est déclenchée par un événement. Lorsqu'un attribut utilisateur est modifié, comme la mise à jour d'une adresse e-mail, mais qu'il n'est pas associé à un événement personnalisé (par exemple, un événement personnalisé de mise à jour du profil), la nouvelle valeur n'est transmise à une sortie comme Braze qu'en tant qu'"attribut enrichi" dans la charge utile du prochain événement déclenché par l'utilisateur. Lorsque l'option **Inclure les attributs utilisateur enrichis** est désactivée, cette nouvelle valeur d'attribut non associée à un événement spécifique ne sera pas transmise à Braze.
  - Pour résoudre ce problème, nous vous conseillons de créer un événement séparé "Attribut utilisateur mis à jour" qui n'envoie à Braze que le ou les attributs utilisateur spécifiques qui ont été mis à jour. Notez qu'avec cette approche, vous enregistrez toujours un point de données supplémentaire pour l'événement "mise à jour de l'attribut utilisateur", mais la consommation de points de données sera bien inférieure à l'envoi de tous les attributs utilisateur lors de chaque appel pour lequel la fonctionnalité est activée.
2. Les attributs calculés sont transmis à Braze en tant qu'attributs d'utilisateur enrichis. Lorsque l'option "Attributs d'utilisateur enrichis" est désactivée, ces attributs ne sont plus transmis à Braze. Pour transmettre des attributs calculés à Braze lorsque les "attributs utilisateur enrichis" sont désactivés, un [flux d'attributs calculés](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) pourrait aider sans pousser tous les attributs. Le flux envoie une mise à jour en aval à Braze lorsqu'un attribut calculé est modifié. 

### Envoi de données inutiles ou en double à Braze
Braze compte un point de données chaque fois qu'un attribut est transmis à Braze, même si la valeur reste inchangée. C'est pourquoi Braze recommande de ne transmettre que les données nécessaires à l'action au sein de Braze et de s'assurer que seuls les deltas des attributs sont transmis.

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[10]: {% image_buster /assets/img_archive/configure_settings.png %}
[11]: {% image_buster /assets/img_archive/mparticle5.png %}
[5]: \#embedded-kit-integration
