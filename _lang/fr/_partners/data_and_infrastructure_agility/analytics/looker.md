---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Cet article de référence présente le partenariat entre Braze et Looker, une plateforme d’aide à la décision et d’analyses du Big Data."
page_type: partner
search_tag: Partenaire

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> [Looker](https://looker.com/) est une plateforme d’aide à la décision et d’analyses du Big Data qui vous permet d’explorer, d’analyser et de partager de manière harmonieuse des analyses commerciales en temps réel.

L’intégration de Braze et Looker permet aux utilisateurs de Braze de tirer parti du signalement des utilisateurs de [blocs Looker](#looker-blocks) et d’[actions Looker](#looker-actions) first-party via l’API REST. Une fois signalés, ces utilisateurs peuvent être ajoutés à des segments pour [cibler](#segment-users) de futures campagnes ou Canvas de Braze. Pour utiliser Looker avec Braze, nous vous recommandons d’envoyer vos données Braze dans un [entrepôt de données utilisant Currents Braze][6], puis d’utiliser les blocs Looker de Braze pour modéliser et visualiser rapidement vos données Braze dans Looker.

## Conditions préalables

| Condition | Description |
|---|---|
|Compte Looker | Un [compte Looker](https://looker.com/) est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][1]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Limitations

- Ce processus fonctionne uniquement avec des données qui n’ont pas été réorganisées.
- L’API traite un maximum de 100 000 lignes à la fois.
- Le compte final d’un utilisateur signalé peut être inférieur en raison de doublons ou de non-utilisateurs.

## Intégration

### Blocs Looker

Nos blocs Looker aident les clients de Braze à accéder rapidement à une vue des données granulaires que nous proposons via [Currents][5]. Nos blocs fournissent des visualisations et une modélisation pré-conçues pour les données de Currents, ce qui signifie que les clients de Braze peuvent facilement mettre en œuvre des modèles analytiques comme les modèles de rétention, évaluer la délivrabilité des messages, examiner plus précisément le comportement des utilisateurs, et bien plus encore.

Pour implémenter les blocs Looker, suivez les instructions dans les fichiers README du code GitHub.
- [Bloc d’analyse de l’engagement par message README][2]
- [Bloc d’analyse du comportement utilisateur README][3]

Ces deux intégrations supposent que votre [intégration initiale à Braze][4], ainsi que votre intégration de Braze à un [entrepôt de données][7] compatible avec Looker sont configurées de manière appropriée pour collecter et envoyer les données nécessaires.


{% alert important %}
Braze a conçu ses blocs Looker en utilisant [Snowflake](https://www.snowflake.com/) comme entrepôt de données. Bien que nous ayons pour objectif de travailler avec autant d’entrepôts de données que possible pour nos blocs, certaines fonctions SQL peuvent différer en fonction de la disponibilité, de la syntaxe ou du comportement des dialectes.
{% endalert %}

{% alert warning %}
Soyez conscient des différentes conventions de noms ! Les noms personnalisés peuvent entraîner des incongruités dans les données, sauf si vous modifiez tous les noms correspondants. Si vous avez personnalisé les noms d’une vue, d’un tableau ou d’un modèle, renommez chaque nom dans le LookML conformément aux noms que vous avez choisis.
{% endalert %}

#### Blocs disponibles

| Bloc | Description |
|---|---|
| Bloc d’analyse de l’engagement par message | Ce bloc inclut des données sur les notifications push, les e-mails, les messages in-app, les Webhooks, les fils d’actualité, les conversions, les entrées dans Canvas, et les événements d’inscription des groupes de contrôle de campagne. <br><br>En savoir plus sur ce [Bloc Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), ou consulter le [Code GitHub](https://github.com/llooker/braze_message_engagement_block). |
| Bloc analytique du comportement utilisateur | Ce bloc inclut des données sur les événements personnalisés, les achats, les sessions, les événements de localisation et les désinstallations.<br><br>En savoir plus sur ce [Bloc Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), ou consulter le [Code GitHub](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2}

### Actions Looker

Les actions Looker vous permettent de marquer des utilisateurs dans Braze via l’endpoint de l’API REST d’un Looker Look. Les actions exigent qu’une dimension soit marquée avec `braze_id`. L’action ajoutera la valeur marquée à l’attribut personnalisé `looker_export` de l’utilisateur.

{% alert important %}
Seuls les utilisateurs existants seront marqués. Vous ne pouvez pas utiliser de Looks pivotants lorsque vous marquez des données dans Braze.
{% endalert %}

#### Étape 1 : Configurer une action Looker dans Braze

Configurez une action Looker dans Braze avec votre clé API REST Braze et l’endpoint REST.

![Page de configuration Looker Braze. Vous trouverez ici les champs pour la clé API Braze et l’endpoint de l’API REST Braze.][12]

#### Étape 2 : Configurer Looker Develop

Sélectionnez les vues appropriées dans Looker Develop. Ajoutez `braze_id` à la balise dimensions et validez les modifications.
Cette balise `braze_id` est utilisée pour déterminer quel champ est la clé unique.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Assurez-vous de valider les changements. L'action Looker ne fonctionnera qu'avec des paramètres de production.**

#### Étape 3 : Définir des attributs utilisateur dans les balises

Tout attribut a la possibilité d’être défini en utilisant une balise `braze[]` avec le nom de l’attribut entre parenthèses. Par exemple, si vous souhaitiez envoyer un `user_segment` d’attribut personnalisé, la balise serait `braze[user_segment]`.

Notez les restrictions suivantes :
- Les attributs ne seront envoyés que s’ils sont **inclus sous forme de champ dans le Look**.
- Les types pris en charge sont `Strings`, `Boolean`, `Numbers` et `Dates`.
- Les noms des attributs sont sensibles à la casse.
- Les attributs standard peuvent également être définis tant qu’ils correspondent aux noms exacts des [profils utilisateur standards]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
- La balise complète doit être formatée entre guillemets. Par exemple, `tags: ["braze[first_name]"]`. D’autres balises peuvent également être assignées, mais elles seront ignorées.
- Des informations supplémentaires sont disponibles sur [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Étape 4 : Envoyer l’action Looker

1. Dans un Look dont la dimension `braze_id` est sélectionnée, cliquez sur l’engrenage des paramètres (<i class="fas fa-cog"></i>) en haut à droite, puis sélectionnez **Send… (Envoyer...)**.
2. Sélectionnez l’action Braze personnalisée.
3. Sous **Unique Key (Clé unique)**, fournissez la clé primaire de mappage utilisateur pour le compte Braze (`external_id` ou `braze_id`).
4. Donnez un nom à l’exportation. Si aucun nom n’est fourni, `LOOKER_EXPORT` sera utilisé.
5. Sous **Advanced Options (Options avancées)**, cliquez sur **Results in Table (Résultats présentés dans le tableau)** ou **All Results (Tous les résultats)**, puis sur **Send (Envoyer)**.<br><br>![][13]<br><br>Si l’exportation a correctement été envoyée, alors `LOOKER_EXPORT` doit apparaître dans le profil utilisateur en tant qu’attribut personnalisé avec la valeur que vous avez saisie dans l’action.<br><br>![][14]

##### Exemple d’appel d’API sortant

Voici un exemple d’appel d’API sortant, qui sera envoyé à l’endpoint [/users/track][10].

###### En-tête
```
Authorization: Bearer [API_KEY]
```

###### Corps
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Segmenter des utilisateurs dans Braze {#segment-users}

Dans Braze, pour créer un segment avec ces utilisateurs marqués, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Looker_Export** en tant que filtre. Ensuite, utilisez l’option « includes value » et indiquez l’indicateur d’attribut personnalisé que vous avez attribué dans Looker.

![Dans le générateur de segments de Braze, le filtre « looker_export » est défini sur « includes_value » et « Looker ».][15]

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

## Résolution des problèmes
Si vous rencontrez des problèmes avec l’action Looker, ajoutez un utilisateur test à des [groupes internes][16] et vérifiez que :

* La clé API dispose des autorisations `users.track`.
* Le bon endpoint REST a été saisi, c.-à-d., `https://rest.iad-01.braze.com`.
* Une balise `braze_id` est définie dans la vue Dimension.
* Votre requête inclut l’attribut ou la dimension de l’ID sous forme de colonne.
* Les résultats de Looker n’ont pas été réorganisés.
* La clé unique a été sélectionnée correctement. Il s’agit généralement de `external_id`.
* `braze_id` dans le champ dimension est différent du `braze_id` dans l’API. `braze_id` dans le champ dimension est utilisé pour indiquer qu'il s'agit du champ `id` de l'API Braze. Dans la plupart des cas, l'envoi de `external_id` est la clé primaire.
* L’utilisateur `external_id` existe sur la plateforme Braze.
* Le champ `looker_export` est défini comme `Automatically Detect` sous `Braze Platform > Settings > Manage Settings > Custom Attributes`.
* Les changements sont mis en production. Looker Action fonctionne sur les paramètres de production.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/api/basics/#endpoints
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {% image_buster /assets/img/user_track_api.png %}
[12]: {% image_buster /assets/img/braze-looker-action.png %}
[13]: {% image_buster /assets/img/send-looker-action.png %}
[14]: {% image_buster /assets/img/custom-attributes-looker.png %}
[15]: {% image_buster /assets/img/braze_segments.png %}
[16]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/
