---
nav_title: Segment.io Engage
article_title: Segment.io Engage
page_order: 1.3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Cet article présente le partenariat entre Braze et Segment.io, une plateforme de données client qui recueille et transfère des informations entre les différentes sources de votre pile marketing."
page_type: partner
search_tag: Partenaire

---

# Segment.io Engage

> [Segment.io](https://segment.com) est une plateforme de données client qui vous aide à collecter, nettoyer et activer vos données client. Cet article présente un aperçu de la connexion entre [Braze et Segment.io Engage](https://segment.com/docs/destinations/braze/#Engage), et décrit les exigences et les processus nécessaires pour assurer une mise en œuvre et une utilisation adaptées.

L’intégration de Braze et de Segment.io vous permet d’utiliser [Engage](https://segment.com/docs/engage/), le module de segmentation d’audience intégré de Segment.io, pour créer des segments d’utilisateurs en fonction des données que vous avez déjà collectées sur diverses sources. Des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) ou des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) seront assignés à ces utilisateurs et pourront être utilisés pour créer des segments Braze et recibler des campagnes ou des Canvas.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Segment.io | Un [compte Segment.io](https://app.segment.com/login) est requis pour profiter de ce partenariat. |
| Utiliser Braze en tant que destination | Vous devez avoir déjà [configuré Braze en tant que destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration Segment.io.<br><br>Vous devez également avoir fourni le bon centre de données Braze et la bonne clé API REST dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer une caractéristique ou une audience Segment.io calculée

1. Dans Segment.io, accédez à l’onglet **Caractéristiques** ou **Audiences calculées** dans **Engage**, puis cliquez sur **New (Nouveau)**.
2. Créer votre caractéristique ou audience calculée. Un éclair dans le coin supérieur de la page indiquera si les calculs sont mis à jour en temps réel.
3. Ensuite, sélectionnez **Braze** comme destination. 
4. Prévisualisez votre audience en cliquant sur **Vérifier et créer**. Par défaut, Segment.io interroge toutes les données historiques pour définir la valeur actuelle de la caractéristique et de l’audience calculées. Pour omettre ces données, décochez la case **Renvoi historique**.
5. Dans les paramètres de la caractéristique ou de l’audience calculée, ajustez les paramètres de connexion en fonction de la façon dont vous souhaitez que vos données soient envoyées à Braze.

#### Caractéristiques et audiences calculées

Les [caractéristiques](https://segment.com/docs/engage/audiences/computed-traits/) et [audiences calculées](https://segment.com/docs/Engage/audiences/) peuvent être envoyées à Braze en tant qu’attributs personnalisés ou événements personnalisés.
- Les caractéristiques et les audiences envoyées à l’aide de l’appel d’`identify` apparaîtront dans Braze en tant qu’attributs personnalisés.
- Les caractéristiques et les audiences envoyées à l’aide de l’appel d’`track` apparaîtront dans Braze en tant qu’événements personnalisés.

Vous pouvez choisir la méthode que vous souhaitez utiliser (ou choisir d’utiliser les deux) lorsque vous connectez la caractéristique calculée à la destination Braze.

{% tabs %}
{% tab Identify %}

Vous pouvez envoyer des caractéristiques et des audiences calculées à Braze en tant qu’appels d’`identify` pour créer des attributs personnalisés dans Braze. 

Par exemple, si vous avez une caractéristique calculée Engage pour « Dernier élément de produit visualisé », vous trouverez le `last_product_viewed_item` dans le profil Braze de l’utilisateur, sous **Attributs personnalisés**. S’il s’agit plutôt d’une audience Engage, vous trouverez votre audience dans la section **Attributs personnalisés**, définie en tant que `true`.

| Caractéristique calculée | Audiences |
| -------------- | --------- |
| ![La section Attribut personnalisé d’un profil utilisateur indique que « last_product_viewed_item » est « Sweater (sweatshirt) ».]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![La section Attribut personnalisée des profils utilisateur répertorie « dormant_shopper » comme étant « true ».]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Track %}

Vous pouvez envoyer des caractéristiques et des audiences calculées à Braze en tant qu’appels de `track` pour créer des événements personnalisés dans Braze. 

Pour poursuivre l’exemple précédent, si un utilisateur a une caractéristique calculée pour le « Dernier élément de produit visualisé », elle apparaîtra sur les profils Braze des utilisateurs comme `Trait calculé` avec le nombre correspondant et l’horodatage le plus récent sous **Événements personnalisés**. S’il s’agit plutôt d’une audience Engage, vous trouverez votre audience, le décompte et l’horodatage le plus récent dans la section **Attributs personnalisés**, définis en tant que `true`.

| Caractéristique calculée | Audiences |
| -------------- | --------- |
| ![La section Événement personnalisée des profils utilisateur répertorie la « Caractéristique calculée » « 1 » fois, la dernière fois étant « il y a 20 heures ».]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![La section Attribut personnalisée des profils utilisateur répertorie « Inscrit dans une audience » « 1 » fois, la dernière fois étant le « 9 mars à 1 h 45 ».]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Étape 2 : Utilisateurs Segment.io dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments.io** sous **Engagement**, puis créez un nouveau segment et nommez-le. Ensuite, en fonction de l’appel que vous avez utilisé :
- **Identification** : Sélectionnez **custom attribute (attribut personnalisé)** comme filtre et recherchez votre attribut personnalisé. Ensuite, utilisez l’option « expression régulière des correspondances » (caractéristique) ou l’option « égal » (audience) et saisissez la variable appropriée.
- **Suivi** : Sélectionner **custom event (événement personnalisé)** comme filtre et recherchez votre événement personnalisé. Ensuite, utilisez l’option « plus que », « moins que » ou « exactement », et saisissez la valeur souhaitée. Cela dépendra de la façon dont vous souhaitez définir votre segment.

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

## Synchronisation en temps réel

Bien que le paramètre par défaut pour la connexion entre Braze et Segment.io Engage soit `Realtime`, certains des filtres empêcheront la persona de se synchroniser en temps réel, y compris certains filtres temporels qui limitent la taille de votre audience au moment où le message a été envoyé.

## Test de débogage Segment.io

Le tableau de bord de Segment.io inclut une fonctionnalité « Débogage » qui permet aux clients de tester si les données d’une « source » sont transférées vers une « destination » comme prévu.

Cette fonctionnalité se connecte à l’[endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze, ce qui signifie qu’elle peut uniquement être utilisée pour des utilisateurs identifiés (utilisateurs qui possèdent déjà un ID utilisateur dans leur profil utilisateur Braze).

Cela ne fonctionnera pas pour une intégration côte à côte de Braze. Aucune donnée serveur ne sera transmise si vous n’avez pas saisi les bonnes informations de l’API REST de Braze.