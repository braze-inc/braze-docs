---
nav_title: Observateur
article_title: Observateur
alias: /fr/partners/looker/
description: "Cet article décrit le partenariat entre Braze et Looker, une plate-forme d'intelligence d'affaires et d'analytique de grandes données."
page_type: partenaire
search_tag: Partenaire
---

# Observateur

> Looker, une plateforme d'intelligence d'entreprise et d'analyse de données de grande taille, vous permet d'explorer, d'analyser et de partager en temps réel des analyses métiers de façon transparente.

Looker et Braze vous permettent de transformer les expériences des clients en visualisant les données du cycle de vie du client.

## Intégration

Braze est partenaire avec Looker à travers les [Looker Blocks de première partie](#implementing-the-looker-blocks) et [les utilisateurs de Braze via REST API](#flagging-users-within-braze). Pour utiliser Looker avec Braze, nous vous recommandons d'envoyer vos données Braze à un entrepôt de données [en utilisant les courants de Braze][6], puis utilisez les Blocs Braze's Looker pour modéliser et visualiser rapidement vos données Braze dans Looker.

Braze's Looker Blocks peut réduire le fardeau de la modélisation des données et permettre aux marketeurs d'accéder rapidement et de visualiser les données.

[Voyez comment Braze utilise les courants.][1]

## Blocs de Looker disponibles

Nos Blocs de Looker aident les clients à accéder rapidement à une vue des données granulaires que nous offrons via [courants][5]. Nos blocs fournissent des visualisations préfabriquées et la modélisation des données des courants afin que les clients de Braze puissent facilement implémenter des modèles analytiques comme la rétention, évaluer la délivrance des messages, examiner plus en détail le comportement de l'utilisateur, et plus encore.

Braze dispose actuellement de deux blocs : l'Analyse de l'engagement des messages et les Blocs d'analyse des comportements des utilisateurs.

| Bloquer                                       | Libellé                                                                                                                                                                                                    | Plus d'informations                                                                                                                                                                                                                                            | Code                                                                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| __Bloc Analyses d'Engagement de Message__     | Ce bloc comprend des données autour de push, courriel, messages dans l'application, webhook, fil d'actualité, conversion, entrée sur Canvas et événements d'inscription de groupe de contrôle de campagne. | [En savoir plus sur ce Bloc de Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) de Looker. | Voir le code sur [Github](https://github.com/llooker/braze_message_engagement_block). |
| __Bloc Analyses de Comportement Utilisateur__ | Ce bloc contient des données sur les événements personnalisés, les achats, les sessions, les événements de localisation et les désinstallations.                                                           | [En savoir plus sur ce Bloc de Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) de Looker.      | Voir le code sur [Github](https://github.com/llooker/braze_retention_block).          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Implémentation des Blocs de Looker

Pour implémenter les Blocs de Looker, suivez les instructions dans les fichiers README du code Github.

- [Bloc Analytics d'engagement de message README][2]
- [Bloc de comportement utilisateur README][3]

{% alert important %}
  Braze a construit nos Blocs Looker en utilisant [Snowflake](https://www.snowflake.com/) comme entrepôt de données. Tandis que nous visons à ce que nos blocs fonctionnent avec le plus d'entrepôts de données possible, il peut y avoir des fonctions SQL qui diffèrent en termes de disponibilité, de syntaxe ou de comportement entre les dialectes.
{% endalert %}

Les deux intégrations supposent que votre [première intégration Braze][4], ainsi que votre intégration à Braze avec un [entrepôt de données][7] compatible Looker est correctement configurée pour capturer et envoyer les données nécessaires.

{% alert warning %}
Soyez conscient des différentes conventions de nommage ! Les noms personnalisés peuvent entraîner des incohérences dans les données, à moins que vous ne fassiez attention à modifier tous les noms correspondants. Si vous avez personnalisé un nom de vue/table ou de modèle, renommez chacun dans le LookML par le nom que vous avez sélectionné.
{% endalert %}

## Signaler les utilisateurs dans Braze

__Les actions de Looker__ vous permettent de signaler les utilisateurs de Braze via le point de terminaison de l'API REST à partir d'un Looker Look. __Actions__ exige qu'une dimension soit taguée avec `braze_id`. L'Action ajoutera la valeur signalée aux utilisateurs `looker_export` attribut personnalisé.

{% alert important %}
Seuls les utilisateurs existants seront signalés. Vous ne pouvez pas utiliser Pivoted Looks lorsque vous signalez des données en Brésil.
{% endalert %}

## Mettre à jour les attributs de l'utilisateur

Optionnel, n'importe quel attribut peut également être défini en utilisant un tag de `braze[]` avec le nom de l'attribut entre le `[]` c'est-à-dire si vous voulez qu'un attribut personnalisé de `segment utilisateur` soit envoyé, alors le tag serait `braze[User Segment]`.
- Notez ce qui suit :
  - L'attribut ne sera envoyé que s'il est **inclus en tant que champ dans le look**.
  - Le nom de l'attribut est sensible à la casse.
  - Les types supportés sont : `Chaînes`, `Booléens`, `Nombres` et `Dates`.
  - Les attributs par défaut peuvent également être définis tant qu'ils correspondent exactement au nom [des profils utilisateurs standards]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
  - La balise complète sera entre guillemets, donc elle devrait ressembler à des balises `: ["braze[first_name]"]`. D'autres tags peuvent également être assignés, mais seront ignorés.
  - Des informations supplémentaires peuvent être trouvées sur [Github](https://github.com/looker/actions/tree/master/src/actions/braze)

## Instructions d'installation

[Vous pouvez également trouver ces instructions et des exemples de code sur Github.](https://github.com/looker/actions/tree/master/src/actions/braze)

### Étape 1 : Créer une clé API REST

Créez une clé d'API REST avec accès à `users.track` à partir de la [console de développeur Braze][8].

!\[User/Track API\]\[11\]

### Étape 2 : Configurez une action Braze Looker

Configurez l'action Braze Looker avec la clé API, et [Braze REST Endpoint][9].

!\[Braze Looker Action\]\[12\]

### Étape 3 : Configurez le développement du Looker

Dans Looker Develop, sélectionnez les vues appropriées. Ajouter `braze_id` aux cotes balise .

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

### Étape 4 : Envoyer l'action Looker

1. Dans un aperçu avec une dimension `braze_id` sélectionnée, cliquez sur l'engrenage Paramètres ( <i class="fas fa-cog"></i> ) en haut à droite et sélectionnez `Envoyer. .`.
2. Sélectionnez une action de Braze personnalisée.
3. À partir de la liste déroulante, sélectionnez la `Clé d'utilisateur unique` appropriée pour le compte Braze (`external_id` ou `braze_id`).
4. Donne un nom à l'exportation. Si aucun n'est fourni, `LOOKER_EXPORT` sera utilisé.
5. Sous __Options avancées__, sélectionnez `Résultats dans le tableau` ou `Tous les résultats`
6. Cliquez sur `Envoyer`.

!\[Send Looker Action\]\[13\]

Si l'exportation a été correctement envoyée, alors `looker_export` devrait apparaître dans le profil de l'utilisateur comme un attribut personnalisé avec la valeur que vous avez entré dans l'Action.

!\[Attribute personnalisé in Braze from Looker\]\[14\]

### Exportation des utilisateurs de segments par Looker

Pour cibler les utilisateurs marqués, un segment Braze peut être créé qui correspond à la valeur marquée.

!\[Braze Segment by Looker Export\]\[15\]

### Limitation

- Ce processus ne fonctionne qu'avec les données qui n'ont pas été pivotées.
- Actuellement, l'API est limitée à 100 000 lignes envoyées.
- Le nombre final du drapeau d'un utilisateur peut être inférieur en raison de doublons ou de non-utilisateurs.

### Exemple d'API sortante

_Exemple de l'API sortante qui sera envoyée au point de terminaison [/user/track/][10]._

```json
{
   "api_key" : "[API_KEY]",
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : vrai,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : vrai,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      . ...
   ]
}
```
[11]: {% image_buster /assets/img/user_track_api.png %} [12]: {% image_buster /assets/img/braze-looker-action.png %} [13]: {% image_buster /assets/img/send-looker-action. ng %} [14]: {% image_buster /assets/img/custom-attributes-looker.png %} [15]: {% image_buster /assets/img/braze_segments.png %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-request
