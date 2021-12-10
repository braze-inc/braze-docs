---
nav_title: Actions Neura
article_title: Actions Neura
alias: /fr/partners/neura_actions/
description: "Cet article décrit le partenariat entre Braze et Neura, une plate-forme d'intelligence de comportement, fournissant aux marques mobiles les outils pour accroître l'engagement et la rétention des clients."
page_type: partenaire
search_tag: Partenaire
---

# Actions Neura

> [Neura][1] aide les grandes marques mobiles à accroître l'engagement et la rétention de la clientèle avec des aperçus de comportement réels et alimentés par des AI et des campagnes avancées de segmentation et de déclenchement.

L'intégration de Neura et Braze vous permet de créer des segments et des publics avec Neura [True PersonasTM][2] et des campagnes de déclenchement pour atteindre les utilisateurs avec [Neura MomentsTM][3].

!\[Moments de disponibilité\]\[10\]{: style="border:0"}

Consultez l'intégration de [Neura Insights][4] Braze pour plus de détails sur la découverte de ces idées de comportement du monde réel.

## Pré-requis

| Exigences          | Libellé                                                                                                                                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braze clé API REST | Une clé d'API Braze REST avec les permissions `users.track`, `users.alias.new`, et `users.export.ids`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Région du serveur  | Ceci est votre point de terminaison de l'API REST Braze et peut être trouvé dans notre [documentation de l'API Braze]({{site.baseurl}}/api/basics/#endpoints).                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour commencer, assurez-vous que les SDK Braze et Neura sont correctement intégrés pour Android et iOS.

Pour intégrer le SDK Neura, ajoutez de courts extraits de code trouvés à l'étape 2 à votre [AppDelegate sur iOS][5] ou [Classe MainActivity sur Android][6]. Vous commencerez alors à recevoir [Neura MomentsMC][3] en tant qu'événements personnalisés Braze. Vous gagnerez également la possibilité de segmenter les utilisateurs en fonction de leurs habitudes de vie et de leurs modes de vie réels, [PersonasTM][2], reçus sous la forme d'attributs personnalisés Braze.

### Étape 1 : Ajouter Braze dans Neura

Dans la [console Neura][7], ajoutez une nouvelle plate-forme d'engagement mobile. Ici, il vous sera demandé de fournir les informations suivantes :

- Clé API : La clé que vous avez créée sur la plateforme Braze.
- Région : Braze gère les terminaux des serveurs dans différentes régions. Utilisez votre région comme entrée au champ "Serveur".
- ID d'application Android/iOS : Nous vous recommandons de fournir un ID d'application unique Braze pour chaque plate-forme mobile, vous permettant de segmenter les utilisateurs pour chaque plate-forme individuellement.

!\[Détails de Neura MEP en Neura\]\[12\]

### Étape 2 : Mappez les utilisateurs de Neura à Braze

Ensuite, assurez-vous que les utilisateurs de Braze et Neura sont associés les uns aux autres. Pour cela, créez un alias utilisateur étiqueté `neura_id` avec le neura_id de votre utilisateur et définissez un attribut utilisateur personnalisé avec la paire clé-valeur `neura, vrai`.

{% tabs %}
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

{% tabs %}
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

## Utiliser Neura à Braze

### Déclencher la campagne

Une fois que les deux SDK sont intégrés, vous pouvez configurer une campagne ou Canvas dans le tableau de bord Braze pour être déclenché par les Moments Neura, disponible dans la plate-forme Braze en tant qu'événements personnalisés.

!\[action-based-delivery.png\]\[13\]

### Créer un segment de Braze

Neura reconnaît des comportements réels pour chaque utilisateur. En utilisant Braze, vous pouvez créer des segments pour cibler des utilisateurs spécifiques en fonction de leur True PersonasMC, disponible sur la plateforme Braze en tant qu'attributs personnalisés.

!\[segment-creation.png\]\[14\]

Consultez le site [développeur Neura][8] pour plus de détails, tutoriels et FAQ.

{% alert note %}
Le SDK Neura nécessite d'activer les services de localisation.
{% endalert %}
[9]: {% image_buster /assets/img/moments-of-availability.png %} [10]: {% image_buster /assets/img_archive/neura-personas-moments.png %} [11]: {% image_buster /assets/img/neura-braze-api-key. ng %} [12]: {% image_buster /assets/img_archive/neura-mep-details-in-neura. ng %} [13]: {% image_buster /assets/img/action-based-delivery.png %} [14]: {% image_buster /assets/img/segment-creation.png %}

[1]: https://www.theneura.com/
[2]: https://dev.theneura.com/api-reference/persona/?ref=braze
[2]: https://dev.theneura.com/api-reference/persona/?ref=braze
[3]: https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze
[3]: https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze
[4]: {{site.baseurl}}/partners/insights/behavioral_analytics/neura_insights
[5]: https://dev.theneura.com/tutorials/ios/?ref=braze
[6]: https://dev.theneura.com/tutorials/android/?ref=braze
[7]: https://dev.theneura.com/console/
[8]: https://dev.theneura.com/?ref=braze
