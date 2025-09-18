---
nav_title: Engagement des segments
article_title: Engagement des segments
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Cet article de référence décrit le partenariat entre Braze et Segment, une plateforme de données clients qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partner
search_tag: Partner

---

# Engagement des segments

> [Segment](https://segment.com) est une plateforme de données clients qui vous aide à collecter, nettoyer et activer vos données clients. Cet article de référence donnera un aperçu de la connexion entre [Braze et Segment Engage](https://segment.com/docs/destinations/braze/#Engage), et décrira les exigences et les processus pour une mise en œuvre et une utilisation correctes.

L'intégration de Braze et Segment vous permet d'utiliser [Engage](https://segment.com/docs/engage/), la segmentation d'audience intégrée à Segment, pour créer des segments d'utilisateurs sur la base des données que vous avez déjà collectées dans diverses sources. Ces audiences seront ensuite synchronisées avec Braze en tant que cohorte, ou dénotées sur le profil de l'utilisateur par le biais d'[attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) ou d'[événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) qui peuvent être utilisés pour créer des segments Braze à utiliser dans les campagnes et le reciblage Canvas.

## Prérequis

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Destination du nuage de Braze | Vous devez avoir déjà [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration Segment.<br><br>Vous devez notamment fournir le centre de données et la clé API REST corrects de Braze dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Clé d'importation des données Braze | Pour synchroniser les audiences d'Engage avec Braze sous forme de cohortes, vous devez générer une clé d'importation des données.<br><br>L'importation de cohortes est en accès anticipé, contactez votre gestionnaire de satisfaction client Braze pour avoir accès à cette fonctionnalité. |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration des destinations des cohortes

### Étape 1 : Créez une audience Engage
1. Dans Segment, accédez à l'onglet **Audiences** d’Engage, puis cliquez sur **Nouveau**.
2. Créez votre audience. Un éclair dans le coin supérieur de la page indique si l'audience se met à jour en temps réel.
3. Sélectionnez ensuite Braze comme destination.
4. Prévisualisez votre audience en cliquant sur **Vérifier et créer**. Par défaut, la segmentation interroge toutes les données historiques pour définir la valeur actuelle du trait et de l'audience calculés. Pour ne pas tenir compte de ces données, décochez la case **Historical Backfill (Remplissage historique)**.

### Étape 2 : Clé d'importation des données de votre cohorte

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Segmentation**.

Ici, vous trouverez votre endpoint REST et générerez la clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.

### Étape 3 : Connectez la destination des cohortes de Braze
Suivez [les instructions de Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) sur la configuration de la destination des cohortes pour synchroniser vos audiences Engage en tant que cohortes vers Braze.

### Étape 4 : Créer un segment Braze à partir de l'audience Engage.
Dans Braze, naviguez vers **Segments**, créez un nouveau segment et sélectionnez **Cohortes de segments** comme filtre. À partir de là, vous pouvez choisir quelle cohorte Segment vous souhaitez inclure. Une fois le segment de cohorte Segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

![][1]

## Intégration du mode cloud

### Étape 1 : Créer un segment calculé en fonction d'un trait de caractère ou d'une audience

1. Dans Segmentation, accédez à l'onglet **Traits calculés** ou **Audiences** dans **Engage**, puis cliquez sur **Nouveau.**
2. Créez votre trait de caractère ou votre audience calculée. Un éclair dans le coin supérieur de la page indique si le calcul est mis à jour en temps réel.
3. Sélectionnez ensuite **Braze** comme destination. 
4. Prévisualisez votre audience en cliquant sur **Vérifier et créer**. Par défaut, la segmentation interroge toutes les données historiques pour définir la valeur actuelle du trait et de l'audience calculés. Pour ne pas tenir compte de ces données, décochez la case **Historical Backfill (Remplissage historique)**.
5. Dans les paramètres de trait calculé ou d'audience, ajustez les paramètres de connexion en fonction de la manière dont vous souhaitez que vos données soient envoyées à Braze.

#### Traits et audiences calculés

Les [traits](https://segment.com/docs/engage/audiences/computed-traits/) et les [audiences](https://segment.com/docs/Engage/audiences/) calculés peuvent être envoyés à Braze en tant qu'événements et attributs personnalisés.
- Les traits et les audiences envoyés à l'aide de l'appel `identify` apparaîtront dans Braze sous la forme d'attributs personnalisés.
- Les caractéristiques et les audiences envoyées à l'aide de l'appel `track` apparaîtront dans Braze sous la forme d'événements personnalisés.

Vous pouvez choisir la méthode à utiliser (ou choisir d'utiliser les deux) lorsque vous connectez le trait calculé à la destination Braze.

{% tabs %}
{% tab Identifier %}

Vous pouvez envoyer des traits et des audiences calculés à Braze sous forme d'appels `identify` pour créer des attributs personnalisés dans Braze. 

Par exemple, si vous avez un trait calculé Engage pour « Article du dernier produit vu », vous trouverez le paramètre `last_product_viewed_item` dans le profil Braze de l'utilisateur sous **Attributs personnalisés**. S'il s'agit d'une audience Engage, votre audience sera répertoriée sous **Attributs personnalisés** définis comme `true`.

| Trait calculé | Audiences |
| -------------- | --------- |
| ![La section des attributs personnalisés d'un profil utilisateur indique que "last_product_viewed_item" est « Pull ».]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![La section d'attribut personnalisé dans le profil utilisateur indique "dormant_shopper" comme étant "true".]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Piste %}

Vous pouvez envoyer des traits et des audiences calculés à Braze sous forme d'appels `track` pour créer des événements personnalisés dans Braze. 

Dans la continuité de l'exemple précédent, si un utilisateur dispose d'un trait calculé pour le "Dernier produit vu", il apparaîtra sur les profils Braze des utilisateurs à l'adresse `Trait Computed` avec le nombre correspondant et l'horodatage le plus récent sous la rubrique **Événements personnalisés**. S'il s'agit d'une audience Engage,votre audience, le décompte et l'horodatage le plus récent répertoriés figureront sous **Attributs personnalisés** définis comme `true`.

| Trait calculé | Audiences |
| -------------- | --------- |
| ![La section des événements personnalisés dans le profil d'un utilisateur mentionne « Trait calculé » « 1 » fois, la dernière fois étant « il y a 20 heures ».]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![La section des attributs personnalisés du profil utilisateur indique "Audience saisie" "1" fois, la dernière fois étant "9 mars à 1h45".]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Étape 2 : Segmentation des utilisateurs à Braze

Dans Braze, pour créer un segment de ces utilisateurs, naviguez vers **Segments** sous **Engagement**, créez un nouveau segment et nommez votre segment. Ensuite, en fonction de l'appel que vous avez utilisé :
- **Identifier**: Sélectionnez l'**attribut personnalisé** comme filtre et localisez votre attribut personnalisé. Ensuite, utilisez l'option "matches regex" (trait) ou l'option "equals" (audience) et saisissez la variable appropriée.
- **Suivre** : Sélectionnez l'**événement personnalisé** comme filtre et localisez votre événement personnalisé. Ensuite, utilisez les options "plus que", "moins que" ou "exactement" et insérez la valeur souhaitée. Cela dépendra de la manière dont vous souhaitez définir votre segmentation.

Une fois enregistré, vous pouvez faire référence à ce segment lors de la création d'un canvas ou d'une campagne à l'étape du ciblage des utilisateurs.

## Temps de synchronisation

Bien que le paramètre par défaut de la connexion entre Braze et Segment Engage soit `Realtime`, certains filtres disqualifieront le persona de la synchronisation en temps réel, notamment certains filtres temporels qui limitent la taille de votre audience au moment de l'envoi du message.

## Essai du débogueur de segmentation

Le tableau de bord de Segment offre une fonctionnalité de "débogage" qui permet aux clients de vérifier si les données d'une "source" sont transférées vers une "destination" comme prévu.

Cette fonctionnalité se connecte à l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze , ce qui signifie qu'elle ne peut être utilisée que pour des utilisateurs identifiés (utilisateurs qui ont déjà un ID utilisateur pour leur profil utilisateur Braze).

Cela ne fonctionnera pas pour une intégration côte à côte Braze. Aucune donnée du serveur ne sera transmise si vous n'avez pas saisi les informations correctes de l'API REST de Braze.

[1]: {% image_buster /assets/img/segment/segment3.png %}