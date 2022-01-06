---
nav_title: Aperçus du Neura
article_title: Neura
alias: /fr/partners/neura/
description: "Cet article décrit le partenariat entre Braze et Neura Actions et Insights, une plate-forme d'intelligence de comportement, fournir aux marques mobiles les outils pour accroître l'engagement et la fidélisation des clients."
page_type: partenaire
search_tag: Partenaire
---

# Actions et Aperçus de Neura

> [Neura][1] aide les grandes marques mobiles à accroître l'engagement et la rétention des clients avec des aperçus comportementaux réels alimentés par l'AI, ainsi que la segmentation et le déclenchement de campagnes avancées.

{% tabs local %}
{% tab Actions %}

L'intégration de Neura et Braze vous permet de créer des segments et des publics avec Neura [True PersonasTM](https://dev.theneura.com/api-reference/persona/?ref=braze)) et de déclencher des campagnes de déclenchement pour atteindre les utilisateurs avec [Neura MomentsTM](https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze).

![Moments de disponibilité]({% image_buster /assets/img_archive/neura-personas-moments.png %}){: style="border:0"}

{% endtab %}
{% tab Insights %}
L'intégration de Braze et Neura vous permet de tirer parti de [Neura Insights](https://www.theneura.com/neura-insights/?ref=braze) pour découvrir les relations entre le comportement des utilisateurs dans le monde réel et les actions qu'ils prennent dans votre application pour trouver le meilleur moment pour s'engager avec chaque utilisateur.

![Graphique de bulles de vision]({% image_buster /assets/img/insights-bubble-graph.png %})
{% endtab %}
{% endtabs %}

## Pré-requis

| Exigences          | Libellé                                                                                                                                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Neura       | Un compte Neura est requis pour profiter de ce partenariat.                                                                                                                                                                                              |
| Braze clé API REST | Une clé d'API Braze REST avec les permissions `users.track`, `users.alias.new`, et `users.export.ids`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Région du serveur  | Ceci est votre point de terminaison de l'API REST Braze et peut être trouvé dans notre [documentation de l'API Braze]({{site.baseurl}}/api/basics/#endpoints).                                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour commencer, assurez-vous que les SDK Braze et Neura sont correctement intégrés pour Android et iOS.

{% tabs local %}
{% tab Actions %}
Pour intégrer le SDK Neura, ajoutez de courts extraits de code trouvés à l'étape 2 à votre [AppDelegate sur iOS](https://dev.theneura.com/tutorials/ios/?ref=braze) ou [Classe MainActivity sur Android](https://dev.theneura.com/tutorials/android/?ref=braze). Vous commencerez alors à recevoir [Neura MomentsMC](https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze) en tant qu'événements personnalisés Braze. Vous gagnerez également la possibilité de segmenter les utilisateurs en fonction de leurs habitudes de vie et de leurs modes de vie réels, [PersonasTM](https://dev.theneura.com/api-reference/persona/?ref=braze), reçus sous la forme d'attributs personnalisés Braze.
{% endtab %}
{% tab Insights %}
Pour intégrer le SDK Neura, ajoutez de courts extraits de code trouvés à l'étape 2 à votre [AppDelegate sur iOS](https://dev.theneura.com/tutorials/ios/?ref=braze) ou [Classe MainActivity sur Android](https://dev.theneura.com/tutorials/android/?ref=braze).
{% endtab %}
{% endtabs %}

### Étape 1 : Ajouter Braze dans Neura

Ajouter une nouvelle plateforme d'engagement mobile dans la [console Neura][7]. Ici, il vous sera demandé de fournir les informations suivantes :

- Clé API : La clé que vous avez créée sur la plateforme Braze.
- Région : Braze gère les terminaux des serveurs dans différentes régions. Utilisez votre région comme entrée au champ "Serveur".
- ID d'application Android/iOS : Nous vous recommandons de fournir un ID d'application unique Braze pour chaque plate-forme mobile, vous permettant de segmenter les utilisateurs pour chaque plate-forme individuellement.

!\[Détails de Neura MEP en Neura\]\[12\]

### Étape 2 : Mappez les utilisateurs de Neura à Braze

Ensuite, assurez-vous que les utilisateurs de Braze et Neura sont associés les uns aux autres. Pour cela, créez un alias utilisateur étiqueté `neura_id` avec le neura_id de votre utilisateur et définissez un attribut utilisateur personnalisé avec la paire clé-valeur `neura, vrai`.

{% tabs local %}
{% tab iOS %}
```objc
[[Appboy sharedInstance].user addAlias:NEURA_USER_ID withLabel:@"neura_id"];
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"neura" andBOOLValue:true];
```
{% endtab %}
{% tab Android %}
```java
Braze.getInstance(YOUR_ACTIVITY.this).getCurrentUser().addAlias(NEURA_USER_ID, "neura_id");
Braze.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute("neura", true);
```
{% endtab %}
{% endtabs %}

Enfin, assurez-vous que l'ID externe est défini. De la même manière que lorsque la méthode `changeUser` est appelée à Braze (dès que l'utilisateur est identifié, généralement après la connexion, pour définir l'identifiant de l'utilisateur), nous recommandons également de définir l'ID de l'utilisateur comme ID externe dans Neura :

{% tabs local %}
{% tab iOS %}
```objc
NExternalId *externalIdObj = [[NExternalId alloc] initWithExternalId:@"USER_ID"];
NeuraSDK.shared.externalId = externalIdObj;
```
{% endtab %}
{% tab Android %}
```java
mNeuraApiClient.setExternalId(USER_ID)
```
{% endtab %}
{% endtabs %}

Consultez le site [développeur Neura][8] pour plus de détails, tutoriels et FAQ.

{% alert note %}
Le SDK Neura nécessite d'activer les services de localisation.
{% endalert %}

## Actions Neura

### Déclencher la campagne

Une fois que les deux SDK sont intégrés, vous pouvez configurer une campagne ou Canvas dans le tableau de bord Braze pour être déclenché par les Moments Neura, disponible dans la plate-forme Braze en tant qu'événements personnalisés.

![livraisons basées sur l'action.png]({% image_buster /assets/img/action-based-delivery.png %})

### Créer un segment de Braze

Neura reconnaît des comportements réels pour chaque utilisateur. En utilisant Braze, vous pouvez créer des segments pour cibler des utilisateurs spécifiques en fonction de leur True PersonasMC, disponible sur la plateforme Braze en tant qu'attributs personnalisés.

![creation-segment.png]( {% image_buster /assets/img/segment-creation.png %})

## Aperçus du Neura

L'importation générique de données de Neura permet deux types de méthodes d'importation :

1. Exporter vos données de courant vers Amazon S3. Notre équipe Customer Success collaborera avec vous pour traduire les données en Neura.
2. Suivez les instructions pour utiliser Neura [Insights API](https://dev.theneura.com/pages/how-to-use-engagement-api/?ref=braze).

Neura ferme la boucle en renvoyant des données réalisables au Brésil, de sorte que vous pouvez exécuter de façon transparente les aperçus du monde réel de Neura directement au Brésil. Une fois que vous avez identifié le bon moment d'engagement pour le bon utilisateur, créez facilement des campagnes et des toiles avec Neura Actions au Brésil.

![insights-moments-personas.png]({% image_buster /assets/img/insights-moments-personas.png %})
[9]: {% image_buster /assets/img/moments-of-availability.png %} [10]: {% image_buster /assets/img_archive/neura-personas-moments. ng %} [11]: {% image_buster /assets/img/neura-braze-api-key.png %} [12]: {% image_buster /assets/img_archive/neura-mep-details-in-neura. ng %} [13]: {% image_buster /assets/img/action-based-delivery.png %} [14]: {% image_buster /assets/img/segment-creation. ng %} [19]: {% image_buster /assets/img/insights-bubble-graph.png %}

[1]: https://www.theneura.com/
[7]: https://dev.theneura.com/console/
[8]: https://dev.theneura.com/?ref=braze