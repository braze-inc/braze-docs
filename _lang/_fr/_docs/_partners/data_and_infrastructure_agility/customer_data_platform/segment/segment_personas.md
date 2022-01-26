---
nav_title: Segment Personas
article_title: Segment Personas
page_order: 1.3
alias: /fr/partners/segment_personas/
description: "Cet article décrit le partenariat entre Braze et Segment, une plateforme de données client qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partenaire
search_tag: Partenaire
---

# Segment Personas

> [Segment](https://segment.com) est une plate-forme de données client qui vous aide à collecter, nettoyer et activer vos données client. Cet article donnera un aperçu de la connexion entre [Braze et Segment Personas](https://segment.com/docs/destinations/braze/#personas), ainsi que décrire les exigences et les processus pour une mise en œuvre et une utilisation appropriées.

L'intégration de Braze et Segment vous permet d'utiliser [Personas](https://segment.com/docs/personas/), le constructeur d'audience intégré de Segment, pour créer des segments d'utilisateurs basés sur des données que vous avez déjà collectées à travers différentes sources. Ces utilisateurs seront ensuite assignés [des attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) ou [des événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) qui peuvent être utilisés pour créer des segments Braze à utiliser dans la campagne et le repositionnement de Canvas .

## Pré-requis

| Exigences            | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte de segment    | Un [compte de segment](https://app.segment.com/login) est requis pour tirer parti de ce partenariat.                                                                                                                                                                                                                                                                                                                                                                                  |
| Destination du Braze | Vous devez avoir déjà [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration de segment.<br><br>Cela inclut la fourniture du centre de données Braze correct et de la clé API REST dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer une caractéristique ou un public calculé pour un segment

1. Dans le segment, accédez à l'onglet __Traits calculés__ ou __Audiences__ dans __Personas__, et cliquez sur __Nouveau__.
2. Créez votre caractéristique ou votre auditoire calculé. Un éclair en haut à droite de la page indique si le calcul se met à jour en temps réel.
3. Ensuite, sélectionnez __Braze__ comme destination.
4. Aperçu de votre audience en cliquant sur  __Réviser & Créer__. Par défaut, Segment interroge toutes les données historiques pour définir la valeur courante de la caractéristique calculée et du public. Pour omettre ces données, décochez __Remplissage Historique__.
5. Dans les paramètres de caractère ou d'audience calculés, ajustez les paramètres de connexion en fonction de la façon dont vous souhaitez que vos données soient envoyées à Braze (voir ci-dessous).

#### Caractéristiques et audiences calculées

Les [traits calculés](https://segment.com/docs/personas/computed-traits/) et [audiences](https://segment.com/docs/personas/audiences/) peuvent être envoyés à Braze en tant qu'attributs personnalisés ou événements personnalisés.
- Caractéristiques et audiences envoyées à l'aide de l'appel `identifier` apparaîtra dans Braze comme attributs personnalisés.
- Les traits et les audiences envoyés en utilisant l'appel `track` apparaîtront dans Braze comme des événements personnalisés.

Vous pouvez choisir la méthode à utiliser (ou choisir d'utiliser les deux) lorsque vous connectez la caractéristique calculée à la destination de Braze.

{% tabs %}
{% tab Identify %}

Vous pouvez envoyer des caractères et des publics calculés à Braze comme `identifier` des appels pour créer des attributs personnalisés en Brésil.

Par exemple, si vous avez une caractéristique calculée par Personas pour « Dernier produit consulté », vous trouverez `last_product_viewed_item` dans le profil Braze de l'utilisateur sous __Attributs personnalisés__. Si c'était plutôt un public de Personas, vous trouverez votre public dans la liste __Attributs personnalisés__ définis comme `true`.

| Caractéristique calculée                                                                     | Audiences                                                                                 |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| ![Caractéristique calculée]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![Audience du segment]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Track %}

Vous pouvez envoyer des caractères et des publics calculés à Braze comme `suivre` des appels pour créer des événements personnalisés en Brésil.

Poursuivant l'exemple précédent, si un utilisateur a une caractéristique calculée pour « Dernier produit consulté », il apparaîtra sur les profils des utilisateurs Braze comme `Trait calculé` avec le nombre correspondant et l'horodatage le plus récent sous __Événements personnalisés__. Si c'était plutôt un public de Personas, vous trouveriez votre public, compteriez, et l'horodatage le plus récent listé sous __Attributs personnalisés__ définis comme `true`.

| Caractéristique calculée                                                                        | Audiences                                                                              |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| ![Caractéristique calculée]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![Audience du segment]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Étape 2 : Segment utilisateurs dans Braze

En Brésil, pour créer un segment de ces utilisateurs, naviguez vers **Segments** sous **Engagement**, créer un nouveau segment, et nommer votre segment. Ensuite, en fonction de quel appel vous avez utilisé :
- __Identifier__: Sélectionnez __attribut personnalisé__ comme filtre et localisez votre attribut personnalisé. Ensuite, utilisez l'option "matches regex" (trait) ou l'option "equals" (public) et saisissez la variable appropriée.
- __Track__: Sélectionnez __événement personnalisé__ comme filtre et localisez votre événement personnalisé. Ensuite, utilisez l'option "plus que", "moins que", ou "exactement", et insérez la valeur souhaitée. Cela dépendra de la façon dont vous voulez définir votre segment.

Une fois enregistré, vous pouvez référencer ce segment pendant la création de Canvas ou de campagne dans l'étape des utilisateurs ciblés.

## Temps de synchronisation

Bien que le paramètre par défaut pour la connexion Braze à Segment Personas soit `en temps réel`, il y a des filtres qui empêcheront la personne de se synchroniser en temps réel, y compris certains filtres basés sur le temps qui restreignent la taille de votre public au moment de l'envoi du message.

## Test du débogueur de segment

Le tableau de bord du segment fournit une fonctionnalité "Debugger" qui permet aux clients de vérifier si les données d'une "ource" sont transférées vers une "Destination" comme prévu.

Cette fonctionnalité se connecte aux [utilisateurs/terminaux de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), ce qui signifie qu'il ne peut être utilisé que pour les utilisateurs identifiés (utilisateurs qui ont déjà un identifiant utilisateur pour leur profil utilisateur Braze).

Cela ne fonctionnera pas pour une intégration de Braze côte à côte. Aucune donnée de serveur ne passera si vous n'avez pas saisi les informations correctes de l'API REST de Braze.