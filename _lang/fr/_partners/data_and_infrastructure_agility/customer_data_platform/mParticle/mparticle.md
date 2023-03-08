---
nav_title: mParticle
article_title: mParticle
page_order: 0
alias: /partners/mparticle/
description: "Cet article présente le partenariat entre Braze et mParticle, une plateforme de données client qui recueille et achemine des informations entre les différentes sources de votre pile marketing."
page_type: partner
search_tag: Partenaire

---

# mParticle

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> La plateforme de données client de mParticle vous permet de tirer le meilleur parti de vos données. Les marketeurs ingénieux utilisent mParticle pour organiser des données sur tout leur jeu d'outils de croissance, ce qui leur permet de gagner à des moments clés du parcours client.

L’intégration de Braze et de mParticle permet de contrôler de manière harmonieuse le flux d’informations entre les deux systèmes :
- [Synchroniser les audiences mParticle avec Braze](#cohort-import) pour la segmentation des campagnes et Canvas Braze.
- [Partager des données sur les deux plateformes](#data-import). Cela peut être effectué via l’intégration du kit mParticle et l’intégration serveur à serveur.
- [Envoyer des interactions d’utilisateur Braze à mParticle via Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), ce qui le rend utilisable sur tout le jeu d'outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est requis pour profiter de ce partenariat. |
| Instance de Braze | Votre instance Braze se trouve sur la [page de présentation de l'API]({{site.baseurl}}/api/basics/#endpoints). (Par exemple : US-01, US-02, etc.) |
| Clé d'identification de l'application Braze | Votre clé d’identification de l’application. <br><br>Vous pouvez y trouver ce que vous pouvez trouver dans le **Tableau de bord de Braze > Manage Settings (Gérer les paramètres) > API Key (Clé API)**. |
| Clé API REST du groupe d’apps | (Serveur à serveur) Une clé API Braze REST<br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > API Settings (Configuration API) > API Key (Clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Audiences

Utilisez le partenariat entre Braze et mParticle pour configurer votre intégration et importer des audiences mParticle directement dans Braze afin de les recibler, créant ainsi une boucle de données complète d’un système à l’autre. Toutes les intégrations que vous avez configurées seront prises en compte dans le volume de points de données de votre compte.

#### Transférer des audiences

mParticle propose trois manières de définir les attributs d’adhésion de la cohorte qui sont contrôlées par le paramètre de configuration « [Send Segments As](#send_settings) » (« Envoyer les segments en tant que »). Le traitement de chaque option est décrit dans la liste ci-dessous :

- **Attribut unique** (par défaut) : mParticle créera un attribut personnalisé unique appelé `SegmentMembership`. La valeur de cet attribut est une liste des ID d’audience mParticle qui correspondent à l’utilisateur. Ces ID d’audience sont disponibles dans le tableau de bord de mParticle sous **Audiences**. Par exemple, si une audience mParticle appelée « Ibiza dreamers » a un ID public « 11036 », vous pourrez segmenter ces utilisateurs avec l’ID d’audience « 11036 ». ![Adhésion de segment mParticle][6]<br><br>
- **Un attribut par segment** : mParticle créera un attribut boolean personnalisé pour chaque audience à laquelle un utilisateur appartient. ![Attribut personnalisé mParticle][7]<br><br>
- **Attribut unique et un seul attribut par segment**

#### Étape 1 : Créer une audience dans mParticle {#send_settings}

Pour créer une audience dans mParticle, accédez à **Audiences > Single Workspace (Espace de travail unique) > + New Audience (+ Nouvelle audience)**.

Pour connecter Braze en tant que sortie pour votre audience, vous devez fournir les champs suivants :

- **Clé API** : Se trouve dans la **Developer Console** de Braze, sous **Settings (Paramètres)**.
- **Système d’exploitation de la clé API** : Sélectionnez le système d’exploitation auquel votre clé API Braze correspond. Cette sélection limite les types de jetons de notification push transmis lorsqu’une audience est mise à jour.
- **Envoyer des segments en tant que** : La méthode permettant d’envoyer des audiences à Braze : Attribut unique, un seul attribut par segment ou les deux. 
- **Clé API REST du groupe d’apps** :  Clé API REST de Braze avec les autorisations maximales. Cela peut être créé dans le **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New Api Key** (Créer une nouvelle clé API)
- **Type d’identité externe** : Le type d’identité de l’utilisateur mParticle qui doit être transféré en tant qu’ID externe à Braze. Nous recommandons de laisser la valeur par défaut : ID client.
- **Type d’identité par e-mail** : Le type d’identité de l’utilisateur mParticle qui doit être transféré à Braze en tant qu’e-mail.
- **Instance de Braze** : Indiquez le cluster vers lequel vos données Braze seront transférées.

Pour finir, **enregistrez** votre audience. 

Vous devriez commencer à voir les audiences se synchroniser avec Braze en quelques minutes. L'adhésion à l'audience ne sera mise à jour que pour les utilisateurs avec `external_ids` (c'est-à-dire les utilisateurs qui ne sont pas anonymes).

Consultez cet article pour plus d’informations sur la création d’[audiences mParticle](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings) dans Braze.

#### Étape 2 : Segmenter des utilisateurs dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments** sous **Engagement** et nommez votre segment.
- **Attribut unique** : Sélectionnez `SegmentMembership` en tant que filtre. Ensuite, utilisez l’option « expression régulière des correspondances » et saisissez l’ID d’audience souhaité. ![Filtre de segment Mparticle « SegmentMembership » défini comme « expression régulière des correspondances » et ID de l’audience.][9]<br><br>
- **Un attribut par segment** : Sélectionnez votre attribut personnalisé en tant que filtre. Ensuite, utilisez l’option « égal » et choisissez la logique appropriée. ![Filtre de segment mParticle « in possible parisians » défini comme « égal » et « true ».][8]

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

#### Désactiver et supprimer des connexions

Étant donné que mParticle ne maintient pas directement les segments dans Braze, il ne supprimera pas les segments lorsque la connexion de l’audience mParticle correspondante est supprimée ou désactivée. Dans ce cas, mParticle ne mettra pas à jour les attributs utilisateur de l’audience dans Braze afin de supprimer l’audience pour chaque utilisateur.

Pour supprimer l'audience d'un utilisateur Braze avant la suppression, ajustez les filtres d'audience de telle manière que la taille de l'audience soit 0 avant de supprimer une audience. Une fois que le calcul de l'audience est terminé et renvoie 0 utilisateur, supprimez l'audience. Cela garantit que l'adhésion de l'audience soit mise à jour dans Braze sur `false` pour l'option d'attribut unique ou supprime l'ID d'audience du format de tableau.

## Mappage des données

Les données peuvent être mappées dans Braze en utilisant l’[intégration du kit embarqué](#embedded-kit-integration) si vous souhaitez connecter vos applications mobiles et Web à Braze via mParticle. Vous pouvez également utiliser [l'intégration de l'API de serveur à serveur](#server-api-integration) pour transmettre les données côté serveur à Braze.

Quelle que soit l'approche que vous choisissez, vous devez configurer Braze en tant que sortie :

### Configurez vos paramètres de sortie Braze

Dans mParticle, accédez à **Setup (Configuration) > Outputs (Sorties) > Add Output (Ajouter une sortie)** et sélectionnez **Braze** pour ouvrir la configuration du kit Braze. Cliquez sur **Savez (Enregistrer)** lorsque vous avez terminé.

| Nom du paramètre | Description |
| ------------ | ----------- |
| Clé d'identification de l'application Braze | Votre clé d'identification d'application Braze se trouve dans la **Developer Console de Braze** sous **Settings (Paramètres)**. Notez que les clés API varient pour chaque plateforme (iOS, Android et Web). |
| Type d’identité externe | Le type d’identité de l’utilisateur mParticle qui doit être transféré en tant qu’ID externe à Braze. Nous recommandons de laisser la valeur par défaut : ID client |
| Type d’identité par e-mail | Le type d’identité de l’utilisateur mParticle qui doit être transféré à Braze en tant qu’e-mail. Nous recommandons de laisser la valeur par défaut : E-mail |
| Instance de Braze | Le cluster vers lequel vos données Braze seront transmises ; il doit s'agir du même cluster sur lequel se trouve votre tableau de bord. |
| Activer le transfert de flux d'événements | (Serveur à serveur) Lorsqu'il est activé, tous les événements seront transmis en temps réel. Sinon, tous les événements seront transmis en bloc. Lorsque vous choisissez d'activer le transfert de flux d'événements, assurez-vous que les données que vous transmettez à Braze respectent les [limitations du débit]({{site.baseurl}}/api/basics/#api-limits). |
{: .reset-td-br-1 .reset-td-br-2}

![][10]

### Intégration du kit embarqué

Le SDK de mParticle et Braze sera présent sur votre application via l’intégration du kit embarqué. Cependant, contrairement à une intégration directe de Braze, mParticle s’occupe d’appeler la majorité des méthodes SDK de Braze pour vous. Toutes les méthodes mParticle que vous utilisez pour suivre les données utilisateur seront automatiquement mappées aux méthodes SDK de Braze. 

Ces mappages du SDK de mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et [Web](https://github.com/Appboy/integration-appboy) sont open source et disponibles sur la [page GitHub de mParticle](https://github.com/mparticle-integrations). 

L’intégration SDK du kit embarqué vous permet de profiter de notre suite complète de fonctionnalités (notifications push, messages in-app, et toutes les analyses de messages pertinentes).

{% alert note %}
Pour les cartes de contenu et les intégrations de messages in-app personnalisés, appelez directement les méthodes SDK de Braze.
{% endalert %}

#### Étape 1 : Intégrer les SDK de mParticle

Intégrez les SDK de mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticle pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle pour le Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Étape 2 : Intégration complète du kit d’événements Braze de mParticle

Bien que le SDK de Braze n'ait pas besoin d'être directement inclus dans votre site Web ou votre application pour cette intégration mParticle, le kit mParticle Appboy suivant doit être installé pour transférer les données de votre application vers Braze.

Le [guide d’intégration du kit d’événements Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle vous indiquera les instructions d’alignement personnalisées de Braze et mParticle en fonction de vos besoins en matière de messagerie (notifications push, géolocalisation, etc.).

#### Étape 3 : Paramètres de connexion de votre sortie Braze

Dans mParticle, accédez à **Connections (Connexions) > Connect (Connecter) > [Your desired platform (Votre plateforme souhaitée)] > Connect Output (Connecter la sortie)** pour ajouter Braze en tant que sortie. Cliquez sur **Save (Enregistrer)** lorsque vous avez terminé.

![][3]

Tous les paramètres de connexion ne s'appliqueront pas à toutes les plateformes et à tous les types d'intégration. Pour une décomposition des paramètres de connexion et des plateformes auxquelles ils s'appliquent, consultez [la documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Intégration de l’API serveur

Il s’agit d’un module complémentaire pour acheminer vos données de backend vers Braze si vous utilisez les SDK côté serveur de mParticle (par ex. Ruby, Python, etc.). Pour configurer cette intégration serveur à serveur avec Braze, suivez la [documentation mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
L’intégration serveur à serveur ne prend pas en charge les fonctionnalités d’interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou les notifications push. Il existe également des données collectées automatiquement, telles que les champs d’appareil, qui ne sont pas disponibles avec cette méthode. 

Optez pour une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.

Pour que les données côté serveur soient transmises à Braze, elles doivent inclure un `external_id` ; les utilisateurs anonymes ne seront pas redirigés.
{% endalert %}

#### Paramètres de connexion de votre sortie Braze

Dans mParticle, accédez à **Connections (Connexions) > Connect (Connecter) > [Your desired platform (Votre plateforme souhaitée)] > Connect Output (Connecter la sortie)** pour ajouter Braze en tant que sortie. Cliquez sur **Savez (Enregistrer)** lorsque vous avez terminé. 

![][4]

Tous les paramètres de connexion ne s'appliqueront pas à toutes les plateformes et à tous les types d'intégration. Pour une décomposition des paramètres de connexion et des plateformes auxquelles ils s'appliquent, consultez [la documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Avant d'activer les « Enriched User Attributes » (Attributs utilisateur enrichis) ou les « Enriched User Identities » (Identités utilisateur enrichies), nous vous recommandons d'examiner les [dépassements de points de données](#potential-data-point-overages) pour vous assurer que vous êtes conscient de l'impact de ces paramètres sur l'utilisation des points de données.

### Détails du mappage des données

#### Types de données
Tous les types de données ne sont pas pris en charge entre les deux plateformes.
- Les [propriétés de l’événement personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) prennent en charge les objets de chaîne de caractères, numériques, booléens ou de date. Ils ne prennent pas en charge les tableaux ou les objets imbriqués.
- Les [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) prennent en charge les objets de chaîne de caractères, numériques, booléens et de date ainsi que les matrices, mais pas les objets ou les objets imbriqués. 

#### Mappage des données

| Type de données mParticle | Type de données Braze | Description |
| ------------------- | --------------- | ----------- |
| Attributs utilisateur (réservés) | Attribut standard | Par exemple, la clé d'attribut `$FirstName` de l’utilisateur réservée de mParticle est mappée au champ d'attribut standard `first_name` de Braze. |
| Attributs utilisateur (autres) | Attribut personnalisé | Tous les attributs utilisateur transmis à mParticle qui ne relèvent pas de ses clés d'attribut utilisateur réservées sont enregistrés dans Braze en tant qu'attribut personnalisé.<br><br>Les attributs utilisateur prennent en charge les chaînes de caractères, numériques, booléens, dates et tableaux ainsi que les matrices, mais ne prennent pas en charge les objets ou les objets imbriqués. |
| Événement personnalisé | Événement personnalisé | mLes événements personnalisés Particle sont reconnus par Braze comme un événement personnalisé. Les attributs d'événement sont transmis en tant que propriétés de l'événement personnalisées.<br><br>Les attributs d'événement transmis à Braze en tant que propriétés de l'événement prennent en charge les chaînes de caractère, numériques, booléennes ou dates, mais ne prennent pas en charge les tableaux ou les objets imbriqués. |
| Événement commercial d'achat | Événement d’achat | Les événements commerciaux d'achat seront mappés aux événements d'achat de Braze. Chaque produit unique transmis dans le cadre de l'événement commercial déclenchera un événement d'achat individuel dans Braze.<br><br>En plus de certaines valeurs commerciales par défaut, les attributs de produit seront enregistrés en tant que propriétés de l'événement d'achat Braze. Pour plus d'informations sur les champs commerciaux supplémentaires qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events).<br><br>Les attributs de produit transmis à Braze en tant que propriétés de l'événement d'achat, prennent en charge les chaînes de caractères, numériques, booléennes ou dates, mais ne prennent pas en charge les tableaux ou les objets imbriqués. |
| Tous les autres événements commerciaux | Événement personnalisé | Tous les autres événements commerciaux seront mappés à des événements personnalisés. Chaque produit unique transmis dans le cadre de l'événement commercial déclenchera un événement unique dans Braze.<br><br>En plus de certaines valeurs commerciales par défaut, les attributs de produit seront enregistrés en tant que propriétés de l'événement Braze. Pour plus d'informations sur les champs commerciaux supplémentaires qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events).<br><br>Les attributs de produit transmis à Braze en tant que propriétés de l'événement, prennent en charge les chaînes de caractères, numériques, booléens ou dates, mais ne prennent pas en charge les tableaux ou les objets imbriqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Mappage de l'identité de l'utilisateur
Pour chaque sortie mParticle, vous pouvez sélectionner le type d'identité externe à envoyer à Braze en tant que fichier `external_id`. Bien que la valeur par défaut soit l'ID client, vous pouvez choisir de mapper un autre ID, tel que `MPID`, à envoyer à Braze en tant que `external_id`. Sachez que le choix d'un identifiant autre que l'ID client peut influencer la manière dont les données sont envoyées dans Braze. 

Par exemple, mappage du MPID dans votre `external_id` Braze aura les effets suivants :
- En raison de la nature du moment où le MPID est attribué, tous les utilisateurs se verront attribuer un `external_id` au démarrage de session.
- La configuration de Currents peut nécessiter un mappage supplémentaire en raison des différents types de données entre MPID et `external_id`.

### Transmission des demandes d'effacement (données des personnes concernées)

Transférez les demandes d'effacement à Braze en configurant une restitution des données des personnes concernées vers Braze. Pour transmettre les demandes d'effacement à Braze, suivez [la documentation de mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Dépassements potentiels des points de données

### Attributs utilisateur enrichis

#### Activation de l’enrichissement des attributs/identités utilisateur (serveur à serveur uniquement){#enriched}

Dans les paramètres de connexion mParticle, Braze recommande de désactiver **Include Enriched User Attributes** (Inclure les attributs utilisateur enrichis). S'il est activé, mParticle transmettra tous les attributs utilisateur disponibles (c'est-à-dire les attributs standard, les attributs personnalisés et les attributs calculés) du profil existant à Braze pour chaque événement enregistré. Cela entraînera une consommation élevée de points de données puisque mParticle enverra à Braze les mêmes attributs inchangés à chaque appel.

Par exemple, si un utilisateur ajoute son prénom, son nom et son numéro de téléphone lors de sa première session et s'inscrit ultérieurement à une newsletter en ajoutant les mêmes informations, en plus de l'e-mail, déclenchant un événement d'inscription à la newsletter :
- S'il est activé (par défaut), cinq points de données seront générés. (événement d'inscription, adresse e-mail, prénom, nom et numéro de téléphone)
- Si cette option est désactivée, deux points de données seront générés (événement d'inscription et adresse e-mail)

{% alert note %}
La désactivation de ce paramètre n’entraînera pas la vérification des données modifiées. Cependant, cela empêchera l'intégration d'envoyer tous les attributs utilisateur sur le profil de l'utilisateur qui n'ont pas été reçus sur le lot entrant d'origine ou explicitement définis comme attribut pour l'événement. Il est important de toujours vérifier que seuls les deltas sont transmis à Braze.
{% endalert %}

#### Considérations relatives à la désactivation des attributs utilisateur enrichis

Il y a quelques considérations à prendre en compte lors de la désactivation de l'option **Include Enriched User Attributes** (Inclure les attributs utilisateur enrichis) :
1. L'intégration de serveur à serveur utilise l'API d'événements mParticle pour envoyer des événements à Braze. Chaque demande est déclenchée par un événement. Lorsqu'un attribut utilisateur est modifié, comme la mise à jour d'une adresse e-mail, mais n'est pas associé à un événement spécifique (par exemple, un événement personnalisé de mise à jour de profil), la nouvelle valeur est uniquement transmise à une sortie telle que Braze en tant qu'« attribut enrichi » dans la charge utile du prochain événement déclenché par l'utilisateur. Lorsque **Include Enriched User Attributes** (Inclure les attributs utilisateur enrichis) est désactivé, cette nouvelle valeur d'attribut non associée à un événement spécifique ne sera pas transmise à Braze.
  - Pour résoudre ce problème, nous vous recommandons de créer un événement distinct « attribut utilisateur mis à jour » qui envoie uniquement le ou les attributs utilisateur spécifiques qui ont été mis à jour à Braze. Notez qu'avec cette approche, vous enregistrez toujours un point de données supplémentaire pour l'événement « attribut utilisateur mis à jour », mais la consommation de points de données sera bien inférieure à l'envoi de tous les attributs utilisateur à chaque appel avec la fonctionnalité activée.
2. Les attributs calculés sont transmis à Braze en tant qu'attribut utilisateur enrichi. Ainsi, lorsque les « attributs utilisateur enrichis » sont désactivés, ils ne seront plus transmis à Braze. Pour transmettre les attributs calculés à Braze lorsque les « attributs utilisateur enrichis » sont désactivés, un [calculated attribute feed](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) (flux d'attributs calculés) peut aider sans pousser tous les attributs. Le flux déclenchera une mise à jour en aval de Braze lorsqu'un attribut calculé est modifié. 

### Envoi de données inutiles ou en double à Braze
Braze compte un point de données chaque fois qu'un attribut est passé à Braze, même si la valeur reste inchangée. Pour cette raison, Braze recommande de ne transférer que les données nécessaires à l'action dans Braze et de s'assurer que seuls les deltas d'attributs sont transmis.

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[10]: {% image_buster /assets/img_archive/configure_settings.png %}
[5]: #embedded-kit-integration