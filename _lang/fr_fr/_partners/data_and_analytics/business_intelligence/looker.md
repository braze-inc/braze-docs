---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Cet article de référence décrit le partenariat entre Braze et Looker, une plateforme d'analyse de big data et d'aide à la décision."
page_type: partner
search_tag: Partner

---

# [![Cours Braze] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/) {: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> [Looker](https://looker.com/), une plateforme d'aide à la décision et d'analyse de big data, vous permet de facilement explorer, analyser et partager des analyses commerciales en temps réel.

L'intégration de Braze et Looker permet aux utilisateurs de Braze de tirer parti du signalement des utilisateurs [Blocs Looker](#looker-blocks) et [Actions Looker](#looker-actions) via l'API REST. Ces utilisateurs signalés peuvent être ajoutés à des segments pour [cibler](#segment-users) les futures campagnes Braze ou Canvases. Pour utiliser Looker avec Braze, nous vous recommandons d'envoyer vos données Braze vers un [entrepôt de données à l'aide de Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/), puis d'utiliser les blocs Looker de Braze pour modéliser et visualiser rapidement vos données Braze dans Looker.

## Conditions préalables

| Condition | Descriptif |
|---|---|
|Compte Looker | Un [compte Looker](https://looker.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Restrictions

- Ce processus ne fonctionne qu'avec les données qui n'ont pas été pivotées.
- L'API traite un maximum de 100 000 lignes à la fois.
- Le nombre final de drapeaux d'un utilisateur peut être inférieur en raison de doublons ou de non-utilisateurs.

## Intégration

### Blocs Looker

[Nos Looker Blocks aident les clients de Braze à accéder rapidement à une vue des données granulaires que nous proposons via Currents.]({{site.baseurl}}/partners/braze_currents/about/) Nos blocs fournissent des visualisations et une modélisation prédéfinies pour les données Currents afin que les clients de Braze puissent facilement mettre en œuvre des modèles analytiques tels que la rétention, évaluer la livrabilité des messages, examiner plus en détail le comportement des utilisateurs, etc.

Pour mettre en œuvre les blocs Looker, suivez les instructions fournies dans les fichiers README du code GitHub.
- [Fichier README du bloc analytique de l'engagement des messages](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [Bloquer le fichier README pour l'analyse analytique du comportement des utilisateurs](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Les deux intégrations supposent que votre intégration [Braze initiale]({{site.baseurl}}/user_guide/onboarding_with_braze/integration/), ainsi que votre intégration Braze avec un entrepôt de [données compatible Looker](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), sont correctement configurées pour capturer et envoyer les données nécessaires.


{% alert important %}
[Braze a construit nos Looker Blocks en utilisant Snowflake comme entrepôt de données.](https://www.snowflake.com/) Bien que nous souhaitions que nos blocs fonctionnent avec autant d'entrepôts de données que possible, certaines fonctions SQL peuvent différer en termes de disponibilité, de syntaxe ou de comportement selon les dialectes.
{% endalert %}

{% alert warning %}
Soyez conscient des différentes conventions de dénomination ! Les noms personnalisés peuvent provoquer des incohérences dans les données, sauf si vous modifiez tous les noms correspondants. Si vous avez personnalisé un nom de vue/table ou de modèle, renommez-le dans LookML avec le nom que vous avez sélectionné.
{% endalert %}

#### Blocs disponibles

| Bloquer | Descriptif |
|---|---|
| Bloc analyse/analytique de l'engagement des messages | Ce bloc comprend des données autour des événements de push, d'e-mail, de messages in-app, de webhook, de conversion, d'entrée dans le Canvas et d'inscription au groupe de contrôle de la campagne. <br><br>Apprenez-en plus sur ce [bloc Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) ou consultez le code [GitHub](https://github.com/llooker/braze_message_engagement_block). |
| Bloc d'analyse du comportement des utilisateurs (if used as an adjective) | Ce bloc inclut des données relatives aux custom events, aux achats, aux sessions, aux événements d'emplacement/localisation et aux désinstallations.<br><br>Apprenez-en plus sur ce [bloc Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) ou consultez le code [GitHub](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Actions du Looker

Les Looker Actions vous permettent de signaler les utilisateurs dans Braze via l’endpoint de l'API REST à partir d'un Looker Look. Les actions nécessitent qu'une dimension soit balisée avec`braze_id`. L'action ajoutera la valeur signalée à l'`looker_export`attribut personnalisé de l'utilisateur.

{% alert important %}
Seuls les utilisateurs existants seront signalés. Vous ne pouvez pas utiliser les looks pivotés lorsque vous marquez des données dans Braze.
{% endalert %}

#### Étape 1 : Configurez une action Braze Looker

Configurez une action Braze Looker avec votre clé API Braze REST et votre endpoint REST.

![La page de configuration de Looker Braze. Ici, vous pouvez trouver des champs pour la clé API de Braze et l'endpoint de l'API REST de Braze.]({% image_buster /assets/img/braze-looker-action.png %})

#### Étape 2 : Configurer Looker Develop

Dans Looker Develop, sélectionnez les vues appropriées. Ajoutez `braze_id` à l'étiquette dimensions et validez les modifications.
Cette balise `braze_id` est utilisée pour déterminer quel champ est la clé unique.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Assurez-vous de valider les modifications. Looker Action ne fonctionnera qu'avec les paramètres de production.**

#### Étape 3 : Définir les attributs utilisateur dans les tags

N'importe quel attribut peut être défini à l'aide d'une balise `braze[]` avec le nom de l’attribut entre crochets. Par exemple, si vous souhaitez qu'un attribut `user_segment` personnalisé soit envoyé, la balise serait`braze[user_segment]`.

Notez les limites suivantes :
- Les attributs ne seront envoyés que s'ils **sont inclus en tant que champ dans l'apparence**.
- Les types pris en charge sont `Strings` `Boolean`, `Numbers` et`Dates`.
- Les noms d'attributs distinguent les majuscules et minuscules.
- Les attributs standard peuvent également être définis à condition qu'ils correspondent exactement aux noms [de profil utilisateur standard]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
- L'étiquette complète doit être mise en forme entre guillemets. Par exemple,`tags: ["braze[first_name]"]`. D'autres tags peuvent également être attribués mais seront ignorés.
- Des informations supplémentaires sont disponibles sur [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Étape 4 : Envoyer l'action Looker

1. Dans un bloc Looker dont une dimension `braze_id` est sélectionnée, cliquez sur la roue dentée (<i class="fas fa-cog"></i> ) en haut à droite, puis sélectionnez **Envoyer...**.
2. Sélectionnez l'action Braze personnalisée.
3. Sous **Clé unique**, indiquez la clé de mappage utilisateur principale pour le compte Braze (`external_id` ou `braze_id`).
4. Donnez un nom à l'exportation. Si aucun nom n'est fourni, `LOOKER_EXPORT` sera utilisé.
5. Sous **Options avancées**, sélectionnez **Résultats dans le tableau** ou **Tous les résultats**, puis **Envoyer**.<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>Si l'exportation a été correctement envoyée, elle `LOOKER_EXPORT` devrait apparaître dans le profil de l'utilisateur sous la forme d'un attribut personnalisé avec la valeur que vous avez saisie dans l'action.<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Exemple d'API sortante

Voici un exemple d'appel d'API sortant, qui sera envoyé au [`/users/track/`endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

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

### Segmentez les utilisateurs dans Braze {#segment-users}

Dans Braze, pour créer un segment de ces utilisateurs signalés, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Looker_Export** comme filtre. Ensuite, utilisez l'option « inclut la valeur » et fournissez le drapeau d'attribut personnalisé que vous avez attribué dans Looker.

![Dans le générateur de segments de Braze, le filtre "looker_export" est défini sur "includes_value" et "Looker".]({% image_buster /assets/img/braze_segments.png %})

Une fois enregistré, vous pouvez faire référence à ce segment lors de la création d'un canvas ou d'une campagne à l'étape du ciblage des utilisateurs.

## Résolution des problèmes
Si vous rencontrez des problèmes avec l'action Looker, ajoutez un utilisateur test aux [groupes internes]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/) et vérifiez les points suivants :

* La clé API possède les autorisations `users.track` nécessaires.
* L’endpoint REST correct est saisi, par exemple en tant que `https://rest.iad-01.braze.com`.
* Une balise `braze_id` est définie dans la vue dimensionnelle.
* Votre requête inclut la dimension ou l'attribut Id sous forme de colonne.
* Les résultats de Looker ne sont pas pivotés.
* La clé unique est correctement sélectionnée. Habituellement, le`external_id`.
* L’ID de Braze `braze_id` dans la dimension est différent de l’ID de Braze `braze_id` de l'API. `braze_id` dans la dimension est utilisé pour indiquer qu'il s'agit du champ `id` de l'API Braze. Dans la plupart des cas, lors de l'envoi `external_id` est la clé primaire.
* L'`external_id`utilisateur existe sur la plateforme Braze.
* Le champ `looker_export` est défini comme `Automatically Detect` sous`Braze Platform > Settings > Manage Settings > Custom Attributes`.
* Les modifications sont enregistrées dans l’environnement de production. Looker Action fonctionne sur les paramètres de production.

