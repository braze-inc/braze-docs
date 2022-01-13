---
nav_title: Observateur
article_title: Observateur
alias: /fr/partners/looker/
description: "Cet article décrit le partenariat entre Braze et Looker, une plate-forme d'intelligence d'affaires et d'analytique de grandes données."
page_type: partenaire
search_tag: Partenaire
---

# Observateur

> [Looker](https://looker.com/), une intelligence commerciale et une plateforme d'analyse de grandes données, vous permet d'explorer, d'analyser et de partager en temps réel des analyses métiers de manière transparente.

L'intégration de Braze et Looker permet aux utilisateurs de Braze de tirer parti de la première partie [Looker Blocks](#looker-blocks) et [Looker Actions](#looker-actions) en signalisant l'utilisateur via l'API REST. Une fois signalés, ces utilisateurs peuvent être ajoutés aux segments de [cibler](#segment-users) futures campagnes Braze ou Canvases. Pour utiliser Looker avec Braze, nous vous recommandons d'envoyer vos données Braze à un entrepôt de données [en utilisant les courants de Braze][6], puis utilisez les Blocs Braze's Looker pour modéliser et visualiser rapidement vos données Braze dans Looker.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Looker                   | Un [compte Looker](https://looker.com/) est requis pour profiter de ce partenariat.                                                                                                                          |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][1].                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Limitation

- Ce processus ne fonctionne qu'avec les données qui n'ont pas été pivotées.
- Actuellement, l'API est limitée à 100 000 lignes envoyées.
- Le nombre final du drapeau d'un utilisateur peut être inférieur en raison de doublons ou de non-utilisateurs.

## Intégration

### Blocs de Looker

Nos Blocs de Looker aident les clients à accéder rapidement à une vue des données granulaires que nous offrons via [courants][5]. Nos blocs fournissent des visualisations préfabriquées et la modélisation des données des courants afin que les clients de Braze puissent facilement implémenter des modèles analytiques comme la rétention, évaluer la délivrance des messages, examiner plus en détail le comportement de l'utilisateur, et plus encore.

Pour implémenter les Blocs de Looker, suivez les instructions dans les fichiers README du code Github.
- [Bloc d'analyse d'engagement de message README][2]
- [Bloc d'analyse du comportement utilisateur README][3]

Les deux intégrations supposent que votre [première intégration Braze][4], ainsi que votre intégration à Braze avec un [entrepôt de données][7]compatible Looker, est correctement configurée pour capturer et envoyer les données nécessaires.


{% alert important %}
Braze a construit nos Blocs Looker en utilisant [Snowflake](https://www.snowflake.com/) comme entrepôt de données. Tandis que nous visons à ce que nos blocs fonctionnent avec le plus d'entrepôts de données possible, certaines fonctions SQL peuvent différer en termes de disponibilité, de syntaxe ou de comportement entre les dialectes.
{% endalert %}

{% alert warning %}
Soyez conscient des différentes conventions de nommage ! Les noms personnalisés peuvent causer des incohérences dans les données à moins que vous ne modifiiez tous les noms correspondants. Si vous avez personnalisé un nom de vue/table ou de modèle, renommez chacun dans le LookML par le nom que vous avez sélectionné.
{% endalert %}

#### Blocs disponibles

| Bloquer                                         | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bloc d'analyse de l'engagement de message       | Ce bloc comprend des données autour de push, courriel, messages dans l'application, webhook, fil d'actualité, conversion, entrée sur Canvas et événements d'inscription de groupe de contrôle de campagne. <br><br>En savoir plus sur ce [Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), ou consultez le [code Github](https://github.com/llooker/braze_message_engagement_block). |
| Bloc d'analyse du comportement de l'utilisateur | Ce bloc contient des données sur les événements personnalisés, les achats, les sessions, les événements de localisation et les désinstallations.<br><br>En savoir plus sur ce [Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), ou consultez le [code Github](https://github.com/llooker/braze_retention_block).                                                                          |
{: .reset-td-br-1 .reset-td-br-2}

### Actions du chercheur

Les actions de Looker vous permettent de signaler les utilisateurs de Braze via le point de terminaison de l'API REST à partir d'un Looker Look. Les actions nécessitent qu'une dimension soit taguée avec `braze_id`. L'Action ajoutera la valeur signalée à l'attribut personnalisé`looker_export` de l'utilisateur.

{% alert important %}
Seuls les utilisateurs existants seront signalés. Vous ne pouvez pas utiliser Pivoted Looks lorsque vous signalez des données en Brésil.
{% endalert %}

#### Étape 1 : Mettre en place une action Braze Looker

Configurez une action Braze Looker avec votre clé API Braze REST et votre point de terminaison REST.

!\[Braze Looker Action\]\[12\]

#### Étape 2 : Configurez le développement du Looker

Dans Looker Develop, sélectionnez les vues appropriées. Ajouter `braze_id` aux cotes balise .

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

#### Étape 3 : Définir les attributs de l'utilisateur dans les tags

Optionnellement, n'importe quel attribut peut être défini en utilisant une balise `braze[]` avec le nom de l'attribut entre parenthèses. Par exemple, si vous voulez qu'un attribut personnalisé `user_segment` soit envoyé, la balise serait `braze[user_segment]`.

Notez les limitations suivantes :
- Les attributs ne seront envoyés que s'ils sont **inclus en tant que champ dans le look**.
- Les types pris en charge sont `Strings`, `Boolean`, `Numbers`, et `Dates`.
- Les noms d'attributs sont sensibles à la casse.
- Les attributs par défaut peuvent également être définis tant qu'ils correspondent exactement aux noms [du profil utilisateur standard]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
- La balise complète doit être formatée entre guillemets. Par exemple, `tags : ["braze[first_name]"]`. D'autres tags peuvent également être assignés, mais seront ignorés.
- Des informations supplémentaires peuvent être trouvées sur [Github](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Étape 4 : Envoyer l'action Looker

1. Dans un aperçu avec une dimension `braze_id` sélectionnée, cliquez sur le matériel de configuration ( <i class="fas fa-cog"></i> ) en haut à droite et sélectionnez **Envoyer. .**.
2. Sélectionnez une action de Braze personnalisée.
3. Sous **Clé Unique**, fournir la clé de mapping utilisateur principale pour le compte Braze (`external_id` ou `braze_id`).
4. Donne un nom à l'exportation. Si aucun n'est fourni, `LOOKER_EXPORT` sera utilisé.
5. Sous **Options Avancées**, sélectionnez **Résultats dans le Tableau** ou **Tous les résultats** puis **Envoyez**.<br><br>! Send Looker Action][13]<br><br>Si l'exportation a été correctement envoyée, puis `LOOKER_EXPORT` devrait apparaître dans le profil de l'utilisateur comme un attribut personnalisé avec la valeur que vous avez entré dans l'action.<br><br>!\[Attribut personnalisé dans Braze à partir du regardeur\]\[14\]

##### Exemple d'API sortante

Ce qui suit est un exemple d'un appel d'API sortant, qui sera envoyé au point de terminaison [/users/track/][10].

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

### Utilisateurs du segment dans Braze {#segment-users}

En Brésil, pour créer un segment de ces utilisateurs signalés, accédez à **Segments** sous **Engagement**, nommez votre segment, et sélectionnez **Looker_Export** comme filtre. Ensuite, utilisez l'option "Inclut la valeur" et fournissez le flag d'attribut personnalisé que vous avez assigné dans le Looker.

!\[Braze Segment by Looker Export\]\[15\]

Une fois enregistré, vous pouvez référencer ce segment pendant la création de Canvas ou de campagne dans l'étape des utilisateurs ciblés.
[11]: {% image_buster /assets/img/user_track_api.png %} [12]: {% image_buster /assets/img/braze-looker-action.png %} [13]: {% image_buster /assets/img/send-looker-action. ng %} [14]: {% image_buster /assets/img/custom-attributes-looker.png %} [15]: {% image_buster /assets/img/braze_segments.png %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-request