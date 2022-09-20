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

{% include video.html id="Njhqwd36gZM" align="right" %}

> La plateforme de données client de mParticle vous permet de tirer le meilleur parti de vos données. Les marketeurs ingénieux utilisent mParticle pour organiser des données sur toute leur pile d’outils, ce qui leur permet de gagner à des moments clés du parcours client.

L’intégration de Braze et de mParticle permet de contrôler facilement le flux d’informations entre les deux systèmes :
- [Synchroniser les cohortes mParticle avec Braze](#cohort-import) pour la segmentation des campagnes et Canvas Braze.
- [Importer des données d’événements sur les deux plateformes](#data-import). Cela peut être effectué via l’intégration du kit mParticle et l’intégration serveur à serveur si vous souhaitez inclure les données de backend. 
- [Connecter les données à mParticle via Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), ce qui le rend utilisable sur toute la pile d’outils. 

## Conditions préalables

| Configuration requise | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Importation de la cohorte

Utilisez le partenariat entre Braze et mParticle pour configurer votre intégration et importer des cohortes mParticle directement dans Braze afin de les recibler, créant ainsi une boucle de données complète d’un système à l’autre. Toutes les intégrations que vous avez configurées seront prises en compte dans le volume de points de données de votre compte.

#### Transférer des audiences

mParticle propose trois manières de définir les attributs d’adhésion de la cohorte qui sont contrôlées par le paramètre de configuration « "[Envoyer des segments en tant que](#send_settings) ». Le traitement de chaque option est décrit dans la liste ci-dessous :

- **Attribut unique** (par défaut) : mParticle créera un attribut personnalisé unique appelé `SegmentMembership`. La valeur de cet attribut est une liste des ID d’audience mParticle qui correspondent à l’utilisateur. Ces ID d’audience sont disponibles dans le tableau de bord de mParticle sous **Audiences**. Par exemple, si une audience mParticle appelée « Ibiza dreamers » a un ID public « 11036 », vous pourrez segmenter ces utilisateurs avec l’ID d’audience « 11036 ». ![Adhésion de segment mParticle][6]<br>
<br>

- **Un attribut par segment** : mParticle créera un attribut personnalisé pour chaque audience à laquelle un utilisateur appartient. ![Attribut personnalisé mParticle][7]<br>
<br>

- **Attribut unique et un seul attribut par segment**

#### Étape 1 : Créer une audience dans mParticle {#send_settings}

Pour créer une audience dans mParticle, accédez à **Audiences > Single Workspace (Espace de travail unique) > + New Audience (+ Nouvelle audience)**. Vous devez remplir les champs suivants :

- **Clé API** : Se trouve dans la **Developer Console** de Braze, sous **Settings (Paramètres)**.
- **Système d’exploitation de la clé API** : Sélectionnez le système d’exploitation auquel votre clé API Braze correspond. Cette sélection limite les types de jetons de notification push transmis lorsqu’une audience est mise à jour.
- **Envoyer des segments en tant que** : La méthode permettant d’envoyer des audiences à Braze : Attribut unique, un seul attribut par segment ou les deux. 
- **Clé API REST du groupe d’apps** :  Clé API REST de Braze avec les autorisations maximales. Cela peut être créé dans le **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New Api Key** (Créer une nouvelle clé API).
- **Type d’identité externe** : Le type d’identité de l’utilisateur mParticle qui doit être transféré en tant qu’ID externe à Braze. Nous recommandons de laisser la valeur par défaut : ID client.
- **Type d’identité par e-mail** : Le type d’identité de l’utilisateur mParticle qui doit être transféré à Braze en tant qu’e-mail.
- **Instance de Braze** : Indiquez le cluster vers lequel vos données Braze seront transférées.

Pour finir, **enregistrez** votre audience. 

Consultez cet article pour plus d’informations sur la création d’[audiences mParticle](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings) dans Braze.

#### Étape 2 : Segmenter des utilisateurs dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments** sous **Engagement** et nommez votre segment.
- **Attribut unique** : Sélectionnez `SegmentMembership` en tant que filtre. Ensuite, utilisez l’option « expression régulière des correspondances » et saisissez l’ID d’audience souhaité. ![Filtre de segment Mparticle « SegmentMembership » défini comme « expression régulière des correspondances » et ID de l’audience.][9]<br>
<br>

- **Un attribut par segment** : Sélectionnez votre attribut personnalisé en tant que filtre. Ensuite, utilisez l’option « égal » et choisissez la logique appropriée. ![Filtre de segment mParticle « in possible parisians » défini comme « égal » et « true ».][8]

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

#### Désactiver et supprimer des connexions

Étant donné que mParticle ne maintient pas directement les segments dans Braze, il ne supprimera pas les segments lorsque la connexion de l’audience mParticle correspondante est supprimée ou désactivée. Dans ce cas, mParticle ne mettra pas à jour les attributs utilisateur de l’audience dans Braze afin de supprimer l’audience pour chaque utilisateur.

### Importation des données

Les données peuvent être importées en utilisant l’[intégration du kit embarqué](#embedded-kit-integration) si vous souhaitez connecter vos applications mobiles et Web à Braze. Vous pouvez également utiliser l’[intégration d’API serveur](#server-api-integration) pour inclure les données de backend dans Braze.

{% alert note %}
Quelle que soit l’approche que vous choisissez, vous devez intégrer le [kit embarqué de mParticle](#embedded-kit-integration).
{% endalert %}

#### Intégration du kit embarqué

Le SDK de mParticle et Braze sera présent sur votre application via l’intégration du kit embarqué. Cependant, contrairement à une intégration directe de Braze, mParticle s’occupe d’appeler la majorité du code SDK de Braze pour vous. Toutes les méthodes mParticle que vous utilisez pour suivre les données utilisateur seront automatiquement mappées au SDK de Braze. 

Ces mappages du SDK de mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et [Web](https://github.com/Appboy/integration-appboy) sont open source et disponibles sur la [page GitHub de mParticle](https://github.com/mparticle-integrations). 

L’intégration SDK embarquée vous permet de profiter de notre suite complète de fonctionnalités (notifications push, messages in-app, fil d’actualité et toutes les analyses de messages pertinentes).

##### Étape 1 : Intégrer les SDK de mParticle

Intégrez les SDK de mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticle pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle pour le Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

##### Étape 2 : Intégration complète du kit d’événements Braze de mParticle

Bien que le SDK de Braze n’est pas requis pour cette intégration mParticle, le kit mParticle Appboy suivant doit être installé pour transférer les données de votre application vers Braze.

Le [guide d’intégration du kit d’événements Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle vous indiquera les instructions d’alignement personnalisées de Braze et mParticle en fonction de vos besoins en matière de messagerie (notifications push, géolocalisation, etc.).

##### Étape 3 : Configurez votre tableau de bord de mParticle pour activer le kit Braze

Dans mParticle, accédez à **Setup (Configuration) > Outputs (Sorties) > Add Output (Ajouter une sortie)** et sélectionnez **Braze** pour ouvrir la configuration du kit Braze. Cliquez sur **Savez (Enregistrer)** lorsque vous avez terminé. 

![][3]

Remplissez les champs suivants sur la page de configuration de Braze : 
- **Clé API** : Se trouve dans la **Developer Console** de Braze, sous **Settings (Paramètres)**. Notez que les clés API varient pour chaque plateforme (iOS, Android et Web).
- **Type d’identité externe** : Le type d’identité de l’utilisateur mParticle qui doit être transféré en tant qu’ID externe à Braze. Nous recommandons de laisser la valeur par défaut : ID client.
- **Instance de Braze** : Personnalisée
- **Endpoint REST personnalisé** : L’URL de votre endpoint REST. Votre endpoint dépendra de [l’URL Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
- **Endpoint SDK personnalisé** : Vous avez été fourni par votre chargé de compte ou votre conseiller Braze (par ex., `sdk.api.braze.com`). Laissez ce paramètre vide si vous n’avez pas reçu d’endpoint d’API personnalisé.
- **Endpoint Javascript personnalisé** : Vous avez été fourni par votre chargé de compte ou votre conseiller Braze. Laissez ce paramètre vide si vous n’avez pas reçu d’endpoint JavaScript personnalisé.

#### Intégration de l’API serveur

Il s’agit d’un module complémentaire pour acheminer vos données de backend vers Braze si vous utilisez les SDK côté serveur de mParticle (par ex. Ruby, Python, etc.). Pour configurer cette intégration serveur à serveur avec Braze, suivez la documentation mParticle en cliquant [ici](https://docs.mparticle.com/guides/platform-guide/connections/).

##### Paramètres de connexion de votre sortie Braze

Dans mParticle, accédez à **Connections (Connexions) > Connect (Connecter) > [Your desired platform (Votre plateforme souhaitée)] > Connect Output (Connecter la sortie)** pour ajouter Braze en tant que sortie. Cliquez sur **Savez (Enregistrer)** lorsque vous avez terminé. 

![][4]

Remplissez les champs suivants sur la page de sortie Braze : 
- **Clé API REST du groupe d’apps** : Une clé API REST de Braze avec les autorisations maximales. Cela peut être créé dans le **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New Api Key** (Créer une nouvelle clé API).
- **Endpoint REST personnalisé** : L’URL de votre endpoint REST. Votre endpoint dépendra de [l’URL Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Cela doit correspondre à l’**endpoint REST personnalisé** fourni dans [cette étape](#step-3-configure-your-mparticle-dashboard-to-enable-the-braze-kit).

##### Mappage des données

Tous les types de données pris en charge par mParticle sont également pris en charge par Braze.
- Les [propriétés d’événement personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) prennent en charge les objets de chaîne, numériques, booléens ou de date. Ils ne prennent pas en charge les matrices ou les objets imbriqués.
- Les [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) prennent en charge les objets de chaîne de caractères, numériques, booléens et de date ainsi que les matrices, mais pas les objets ou les objets imbriqués. 

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[5]: #embedded-kit-integration