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

Vous pouvez améliorer votre flux de données en mariant mParticle et Braze pour une façon transparente de contrôler le flux d'informations entre les systèmes. De plus, avec les currents, l'export de données en temps réel de Brase, vous pouvez également connecter des données à mParticule et le rendre utilisable sur toute la pile de croissance.

Si vous recherchez des informations sur l'intégration des courants avec mParticle, reportez-vous à [mParticle for Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/).

## Pré-requis

| Exigences                                      | Origine    | Accès                                                              | Libellé                                                                             |
| ---------------------------------------------- | ---------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| mParticle Account & Informations sur le Compte | mParticule | [https://app.mparticle.com/login](https://app.mparticle.com/login) | Vous devez avoir un compte mParticle actif pour utiliser leurs services avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Si vous voulez connecter vos applications Web et mobiles à Braze, vous devrez utiliser l'intégration [du kit intégré][5] ci-dessous.

Si vous avez des données d'arrière-plan en dehors de vos applications, vous voudrez utiliser l'intégration de l'API serveur pour canaliser ces données vers Braze.

Veuillez noter que peu importe l'approche, il est nécessaire d'intégrer le kit embarqué mParticle.

## Intégration de kit intégré

Grâce à l'intégration du kit embarqué, mParticle et Braze SDK seront tous deux présents sur votre application. Cependant, contrairement à une intégration directe de Braze, mParticle s'occupe d'appeler la majorité du code Braze SDK pour vous. Toutes les méthodes mParticle que vous utilisez pour suivre les données utilisateur seront automatiquement mappées au SDK de Brase. Ces mappings du SDK de mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et [Web](https://github.com/Appboy/integration-appboy) sont open source et peuvent être trouvés sur la page GitHub de [mParticle](https://github.com/mparticle-integrations).

L'intégration du SDK intégré vous permet de profiter de toute notre suite de fonctionnalités (Push, Messages, fil d'actualités dans l'application et le suivi de toutes les analyses de messages pertinents).

### 1. Intégrer les SDK mPartiticle

Intégrez les SDK mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticule pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticule pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticule pour Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

### 2. Intégration complète du kit d'événements mParticule Braze

Alors que le Braze SDK n'est pas requis pour cette intégration de mParticle, le mParticle Appboy Kit suivant doit être installé pour transférer les données de votre application vers Braze.

mParticule [Braze Event Kit Integration Guide](https://docs.mparticle.com/integrations/braze/event/#kit-integration) vous guidera à travers les instructions personnalisées d’alignement mParticle et Braze en fonction de vos besoins de messagerie (Push, Suivi de la localisation, etc.).

### 3. Configurez votre tableau de bord mParticle pour activer le kit Braze.

!\[mParticle Event Config UI\]\[3\]

| Nom                                          | Libellé                                                                                                                                                                                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clé API                                      | Trouvé dans __Console développeur__ sous __Réglages__.                                                                                                                                                                               |
| Type d’identité externe                      | Le type d'identité utilisateur mParticle à transférer en tant qu'ID externe au Brésil. Nous vous recommandons de laisser cette valeur à la valeur par défaut, ID client.                                                             |
| Instance de Braze                            | Sélectionnez __Personnalisé__.                                                                                                                                                                                                       |
| Point de terminaison du SDK personnalisé     | Donné à vous par votre support ou représentant de compte Braze (par exemple, `sdk.api.braze. om` ).<br> Si vous n'avez pas reçu de point de terminaison d'API personnalisé, laissez ce paramètre vide.                         |
| Point de terminaison REST personnalisé       | Votre point de terminaison REST (par exemple, `rest.iad.braze.com` ).<br> Si vous ne savez pas sur quelle instance Braze vous êtes, trouvez votre endpoint [ici]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Point de terminaison JavaScript personnalisé | Donné à vous par votre support ou par votre représentant de compte Braze. Si vous n'avez pas reçu de point de terminaison JavaScript personnalisé, laissez ce paramètre vide.                                                        |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Les clés API seront différentes pour chaque plateforme (iOS, Android, et Web).
{% endalert %}

## Intégration de l'API serveur

Il s'agit d'un module complémentaire pour acheminer vos données backend vers Braze si vous utilisez les SDK côté serveur mParticule (par exemple, Ruby, Python, etc.). Pour configurer cette intégration de serveur à serveur avec Braze, veuillez suivre la documentation de mPartique [ici](https://docs.mparticle.com/guides/platform-guide/connections/).

### Paramètres de connexion pour votre sortie Braze

Ces paramètres sont situés dans l'onglet __Connexions__ de mParticule sous __Connecter__. Vous devrez ajouter Braze comme une sortie.

!\[mParticle Connections Setting\]\[4\]

La clé d'API REST de groupe d'application requise pour entrer dans le tableau de bord de mParticule peut être trouvée dans la [console de développement][1] sous l'onglet __Paramètres API__.

!\[Braze Developer Console - Paramètres API\]\[2\]

Point de terminaison REST personnalisé : définissez ceci sur votre point de terminaison [REST API pertinent]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Cela devrait correspondre au champ __Point d'extrémité REST personnalisé__ dans la configuration d'événement pour Braze trouvé dans votre tableau de bord mParticle dans l'onglet __Configuration__ sous __Sorties__.

### Mappage des données

Tous les types de données qui sont pris en charge sur mParticle ne sont pas pris en charge par Braze.

- [Les propriétés d'événement personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) supportent les objets chaîne, numérique, booléen ou date. Il ne supporte pas les tableaux ou les objets imbriqués.
- [Les attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) supportent la chaîne, les numériques, les booléens, les objets de date et les tableaux, mais ne supportent pas les objets ou les objets imbriqués.
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %} [3]: {% image_buster /assets/img_archive/mParticle_event_config.png %} [4]: {% image_buster /assets/img_archive/mParticle_connections.png %}


[1]: https://dashboard.braze.com/app_settings/developer_console
[5]: #embedded-kit-integration
