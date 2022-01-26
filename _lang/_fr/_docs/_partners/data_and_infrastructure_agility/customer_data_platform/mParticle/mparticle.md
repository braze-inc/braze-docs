---
nav_title: mParticule
article_title: mParticule
page_order: 0
alias: /fr/partners/mparticle/
description: "Cet article décrit le partenariat entre Braze et mParticle, une plateforme de données client qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partenaire
search_tag: Partenaire
---

# mParticule

{% include video.html id="Njhqwd36gZM" align="right" %}

> La plate-forme de données client de mParticule vous permet d'en faire plus avec vos données. Les marketeurs sophistiqués utilisent mParticle pour orchestrer les données à travers toute leur pile de croissance, ce qui leur permet de gagner dans les moments clés du voyage des clients.

L'intégration de Braze et mParticle vous permet de contrôler de manière transparente le flux d'informations entre les deux systèmes :
- [Synchroniser les cohortes mParticule à Braze](#cohort-import) pour la campagne de Braze et la segmentation de Canvas.
- [Importer des données d'événement sur les deux plates-formes](#data-import). Cela peut se faire par le biais de l'intégration du kit mParticle et de l'intégration du serveur à serveur si vous voulez piquer les données du backend.
- [Connectez des données à mParticule à travers les courants]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), ce qui la rend utilisable sur toute la pile de croissance.

## Pré-requis

| Exigences         | Libellé                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| compte mParticule | Un [compte mParticle](https://app.mparticle.com/login) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Importation de cohortes

Utilisez le partenariat de Braze et mParticule pour configurer votre intégration et importer des cohortes mParticle directement dans Braze pour le reargeting, créer une boucle complète de données d'un système à l'autre. Toute intégration que vous avez configurée comptera dans le volume de données de votre compte.

#### Transférer des audiences

mParticle offre trois façons de définir les attributs d'appartenance à une cohorte, contrôlés par le paramètre de configuration "[Envoyer les segments comme](#send_settings)". Le traitement de chaque option est décrit ci-dessous:

- __Attribut unique__ (par défaut) : mParticle créera un seul attribut personnalisé appelé `Adhésion au segment`. La valeur de cet attribut est une liste d'identifiants d'audience mParticle qui correspondent à l'utilisateur. Ces identifiants d'audience peuvent être trouvés dans le tableau de bord mParticule sous __Audiences__. Par exemple, si un public mPartiticle "Ibiza dreamers" a un ID d'audience de "11036", vous serez en mesure de segmenter ces utilisateurs par l'ID d'audience "11036". !\[mParticle segment membership\]\[6\]<br><br>
- __Un attribut par segment__: mParticle créera un attribut personnalisé pour chaque public auquel appartient un utilisateur. !\[mParticle custom attribute\]\[7\]<br><br>
- __Un seul attribut et un attribut par segment__

#### Étape 1 : Créer un public dans mParticule {#send_settings}

Pour créer un public dans mParticle, accédez à __Audiences > Espace de travail unique > + Nouvelle audience__. Ici vous devez fournir les champs suivants :

- __Clé API__: Trouvé dans la __console de développement __ de Braze__ sous __Paramètres__.</li>
- __Système d'exploitation à clé API__: Sélectionnez le système d'exploitation auquel correspond votre clé API Braze. Cette sélection limitera les types de jetons push envoyés lors d'une mise à jour du public.
- __Envoyer des segments comme__: La méthode d'envoi des audiences au Brésil : Single Attribute, Un Attribut par Segment, ou les deux.
- __Groupe d'applications REST API key__: Braze REST API key with full permissions. Ceci peut être créé dans le tableau de bord __Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__
- __Type d’identité externe__: Le type d’identité utilisateur mParticle à transférer en tant qu’ID externe au Brésil. Nous vous recommandons de laisser cette valeur à la valeur par défaut, ID client.
- __Type d’identité d’e-mail__: le type d’identité de l’utilisateur mParticle à transmettre en tant que courriel à Braze.
- __Instance Braze__: Spécifiez à quelle instance vos données Braze seront transmises à</ul>

Enfin __Économisez__ votre public.

Consultez cet article pour plus d'informations sur la création des publics de Braze [mParticule](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Étape 2 : Segment utilisateurs dans Braze

En Brésil, pour créer un segment de ces utilisateurs, naviguez vers **Segments** sous **Engagement** et nommez votre segment.
- __Attribut unique__: Sélectionnez `Adhésion au segment` comme filtre. Ensuite, utilisez l'option "correspondances regex" et saisissez l'ID d'audience désiré. !\[mParticle segment filter 1\]\[9\]<br><br>
- __Un attribut par segment__: Sélectionnez votre attribut personnalisé comme filtre. Ensuite, utilisez l'option "égal" et choisissez la logique appropriée. !\[mParticle segment filter 2\]\[8\]

Une fois enregistré, vous pouvez référencer ce segment pendant la création de Canvas ou de campagne dans l'étape des utilisateurs ciblés.

#### Désactivation et suppression des connexions

Comme mParticle ne maintient pas directement les segments en Brésil, il ne supprimera pas les segments lorsque la connexion mParticle correspondante sera supprimée ou désactivée. Lorsque cela se produit, mParticle ne mettra pas à jour les attributs de l'utilisateur du public dans Braze pour supprimer le public de chaque utilisateur.

### Importation des données

Les données peuvent être importées en utilisant l'intégration [du kit intégré](#embedded-kit-integration) si vous voulez connecter vos applications Web et mobiles à Braze. Vous pouvez également utiliser [l'intégration de l'API serveur](#server-api-integration) pour canaliser les données backend dans Braze.

{% alert note %}
Quelle que soit l'approche que vous choisissez, vous devez intégrer le kit embarqué [mParticle](#embedded-kit-integration).
{% endalert %}

#### Intégration de kit intégré

Le mParticle et Braze SDK seront présents sur votre application à travers l'intégration de kits embarqués. Cependant, contrairement à une intégration directe de Braze, mParticle s'occupe d'appeler la majorité du code Braze SDK pour vous. Toutes les méthodes mParticle que vous utilisez pour suivre les données utilisateur seront automatiquement mappées au SDK de Brase.

Ces mappings du SDK de mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et [Web](https://github.com/Appboy/integration-appboy) sont open source et peuvent être trouvés sur la page GitHub de [mParticle](https://github.com/mparticle-integrations).

L'intégration du SDK intégré vous permet de profiter de toute notre suite de fonctionnalités (Push, Messages, fil d'actualités dans l'application et le suivi de toutes les analyses de messages pertinents).

##### Étape 1 : Intégrer les SDK mPartiticle

Intégrez les SDK mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticule pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticule pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticule pour Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

##### Étape 2 : Intégration complète du kit d'événements Braze de mParticule

Alors que le Braze SDK n'est pas requis pour cette intégration de mParticle, le mParticle Appboy Kit suivant doit être installé pour transférer les données de votre application vers Braze.

mParticule [Le guide d'intégration du kit d'événements Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) vous guidera à travers les instructions personnalisées d'alignement mParticle et Braze en fonction de vos besoins de messagerie (Push, Suivi de la localisation, etc.).

##### Étape 3 : Configurer votre tableau de bord mParticule pour activer le kit Braze

Dans mParticle, accédez à __Configuration > Sorties > Ajouter Sortie__ et sélectionnez __Braze__ pour ouvrir la configuration du kit Braze. __Enregistrez__ une fois terminé.

!\[mParticle Event Config UI\]\[3\]

Fournir les champs suivants sur la page de configuration de Braze :
- __Clé API__: Trouvé dans la __console de développement __ de Braze__ sous __Paramètres__. Notez que les clés API seront différentes pour chaque plateforme (iOS, Android, et Web).</li>
- __Type d’identité externe__: Le type d’identité utilisateur mParticle à transférer en tant qu’ID externe au Brésil. Nous vous recommandons de laisser cette valeur à la valeur par défaut, ID client.
- __Instance de Braze__: Personnalisée
- __Point de terminaison REST personnalisé__: Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
- __Point de terminaison SDK personnalisé__: Donné par votre support ou représentant de compte Braze (par exemple, `sdk.api.braze.com`). Laissez ce paramètre vide si vous n'avez pas reçu de point de terminaison API personnalisé.
- __Point de terminaison JavaScript personnalisé__: Donné par votre support de Braze ou par votre représentant de compte. Laissez ce paramètre vide si vous n'avez pas reçu de point de terminaison JavaScript personnalisé.</ul>

#### Intégration de l'API serveur

Il s'agit d'un module complémentaire pour acheminer vos données backend vers Braze si vous utilisez les SDK côté serveur de mParticule (par exemple, Ruby, Python, etc.). Pour configurer cette intégration de serveur à serveur avec Braze, veuillez suivre la documentation de mPartique [ici](https://docs.mparticle.com/guides/platform-guide/connections/).

##### Paramètres de connexion pour votre sortie Braze

Dans mParticile, accédez à __Connexions > Connecter > [Votre plateforme souhaitée] > Connectez la sortie__ pour ajouter Braze en sortie. __Enregistrez__ une fois terminé.

!\[mParticle Connections Setting\]\[4\]

Fournir les champs suivants sur la page de sortie de Braze :
- __Groupe d'application clé REST API__: une clé API Braze REST avec toutes les autorisations. Ceci peut être créé dans le tableau de bord __Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__.
- __Point de terminaison REST personnalisé__: Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Cela devrait correspondre au __point de terminaison REST personnalisé__ fourni dans [cette étape](#step-3-configure-your-mparticle-dashboard-to-enable-the-braze-kit).

##### Mappage des données

Tous les types de données qui sont pris en charge sur mParticle ne sont pas pris en charge par Braze.
- [Les propriétés d'événement personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) supportent les objets chaîne, numérique, booléen ou date. Il ne supporte pas les tableaux ou les objets imbriqués.
- [Les attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) supportent la chaîne, les numériques, les booléens, les objets de date et les tableaux, mais ne supportent pas les objets ou les objets imbriqués.
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %} [3]: {% image_buster /assets/img_archive/mParticle_event_config.png %} [4]: {% image_buster /assets/img_archive/mParticle_connections. ng %} [6]: {% image_buster /assets/img_archive/mparticle1.png %} [7]: {% image_buster /assets/img_archive/mparticle2. ng %} [8]: {% image_buster /assets/img_archive/mparticle3.png %} [9]: {% image_buster /assets/img_archive/mparticle4.png %}