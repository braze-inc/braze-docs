---
nav_title: Neura Insights
article_title: Neura
alias: /partners/neura/
description: "Cet article présente le partenariat entre Braze et Neura Actions and Insights, une plateforme d’intelligence comportementale qui fournit aux marques mobiles les outils nécessaires pour stimuler l’engagement et la rétention des clients."
page_type: partner
search_tag: Partenaire

---

# Neura Actions and Insights

> [Neura][1] aide les marques mobiles à augmenter leur rétention et leur engagement client grâce à des renseignements comportementaux réels optimisés par IA, soutenus par une segmentation et des déclencheurs de campagnes avancées.

{% tabs local %}
{% tab Actions %}

L’intégration de Neura et de Braze vous permet de créer des segments et des audiences avec [True Personas™](https://dev.theneura.com/api-reference/persona/?ref=braze) de Neura et de déclencher des campagnes pour atteindre des utilisateurs avec [Neura Moments™](https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze).

![Un graphique simple montrant comment True Personas et Neura Moments de Neura peuvent être utilisés ensemble pour atteindre des utilisateurs.]({% image_buster /assets/img_archive/neura-personas-moments.png %}){: style="border:0"}

{% endtab %}
{% tab Insights %}
L’intégration de Braze et Neura vous permet de tirer parti de [Neura Insights](https://www.theneura.com/neura-insights/?ref=braze) pour découvrir les relations entre le comportement réel des utilisateurs et les actions qu’ils effectuent dans votre application afin de trouver le meilleur moment pour interagir avec chaque utilisateur.

![Un graphique à bulles de Neura Insights montrant « Quand les utilisateurs sont-ils disponibles pour communiquer avec eux dans l’application ? ».]({% image_buster /assets/img/insights-bubble-graph.png %})
{% endtab %}
{% endtabs %}

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Neura | Un compte Neura est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST Braze avec des autorisations `users.track`, `users.alias.new` et `users.export.ids`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Région du serveur | Il s’agit de votre endpoint d’API REST de Braze, qui se trouve dans notre [Documentation de l’API Braze]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour commencer, assurez-vous que les SDK de Braze et Neura sont correctement intégrés pour les systèmes Android et iOS. 

{% tabs local %}
{% tab Actions %}
Pour intégrer le SDK de Neura, ajoutez les extraits de code court fournis à l’étape 2 à votre [AppDelegate sur iOS](https://dev.theneura.com/tutorials/ios/?ref=braze) ou à votre [classe MainActivity sur Android](https://dev.theneura.com/tutorials/android/?ref=braze). Vous commencerez à recevoir [Neura Moments™](https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze) en tant qu’événements personnalisés de Braze. Vous aurez également la possibilité de segmenter les utilisateurs en fonction de leur mode de vie et de leurs habitudes réelles, [True Personas™](https://dev.theneura.com/api-reference/persona/?ref=braze), reçus en tant qu’attributs personnalisés de Braze.
{% endtab %}
{% tab Insights %}
Pour intégrer le SDK de Neura, ajoutez les extraits de code court fournis à l’étape 2 à votre [AppDelegate sur iOS](https://dev.theneura.com/tutorials/ios/?ref=braze) ou à votre [classe MainActivity sur Android](https://dev.theneura.com/tutorials/android/?ref=braze). 
{% endtab %}
{% endtabs %}

### Étape 1 : Ajouter Braze dans Neura

Ajoutez une nouvelle plateforme d’engagement mobile dans la [console Neura][7]. Vous devrez fournir les informations suivantes :

- Clé API : La clé que vous avez créée sur la plateforme Braze.
- Région : Braze gère des endpoints de serveur dans différentes régions. Saisissez le nom de votre région dans le champ « Serveur ».
- ID d’application Android/iOS : Nous vous recommandons de fournir un ID d’application Braze unique pour chaque plateforme mobile, ce qui vous permet de segmenter individuellement les utilisateurs pour chaque plateforme.

![][12]

### Étape 2 : Mapper des utilisateurs de Neura vers Braze

Ensuite, assurez-vous que les utilisateurs de Braze et Neura sont mappés les uns aux autres. Pour ce faire, créez un alias d’utilisateur étiqueté comme `neura_id` avec l’ID Neura de votre utilisateurneura_id et définissez un attribut utilisateur personnalisé avec la paire clé-valeur `neura, true`.

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

Enfin, assurez-vous que l’ID externe est bien défini. De même, lorsque la méthode `changeUser` est utilisée dans Braze (dès que l’utilisateur est identifié, généralement après qu’il se connecte, pour définir l’ID utilisateur), nous vous recommandons également de définir l’ID utilisateur en tant qu’ID externe dans Neura :

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

Rendez-vous sur le [site de développement de Neura][8] pour obtenir davantage d’informations et consulter des didacticiels et des FAQ.

{% alert note %}
Vous devez avoir activé les services de localisation pour utiliser le SDK de Neura.
{% endalert %}

## Neura Actions

### Déclencher une campagne 

Une fois les deux SDK intégrés, vous pouvez configurer une campagne ou un Canvas dans le tableau de bord de Braze pour qu’ils soient déclenchés par Neura Moments, qui est disponible sur la plateforme Braze en tant qu’événements personnalisés.

![Dans une campagne Braze basée sur une action, « Perform Custom Event » (Réaliser un événement personnalisé) est défini sur « neura_user_arrived_home ». ]({% image_buster /assets/img/action-based-delivery.png %})

### Créer un segment Braze

Neura reconnaît les traits de comportement réels de chaque utilisateur. Avec Braze, vous pouvez créer des segments pour cibler des utilisateurs spécifiques en fonction de leur True Personas™, disponible sur la plateforme Braze en tant qu’attributs personnalisés.

![Dans le générateur de segments de Braze, le filtre « neura_personas » est défini sur « includes_value » et « avid_runner ».]( {% image_buster /assets/img/segment-creation.png %})

## Neura Insights

L’importation de données génériques de Neura prend en charge deux types de méthodes d’importation :

1. Exporter vos données Currents vers Amazon S3. Notre équipe du Service de support travaillera avec vous pour traduire les données à Neura.
2. Suivez les instructions pour utiliser l’[API Insights](https://dev.theneura.com/pages/how-to-use-engagement-api/?ref=braze) de Neura.

Neura boucle la boucle en envoyant des données exploitables à Braze, afin que vous puissiez utiliser les informations réelles de Neura dans Braze de manière harmonieuse.
Après avoir identifié le bon moment pour communiquer avec le bon utilisateur, vous pouvez facilement créer des campagnes et des Canvas en utilisant les actions Neura dans Braze.

![Infographie de Neura insights montrant « quels Neura Insights Moments offrent les engagements les plus réussis ? » et « quelles True Personas ont les engagements les plus réussis ? ».]({% image_buster /assets/img/insights-moments-personas.png %})

[1]: https://www.theneura.com/
[2]: https://dev.theneura.com/api-reference/persona/?ref=braze
[3]: https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze
[4]: {{site.baseurl}}/partners/insights/behavioral_analytics/neura_insights
[5]: https://dev.theneura.com/tutorials/ios/?ref=braze
[6]: https://dev.theneura.com/tutorials/android/?ref=braze
[7]: https://dev.theneura.com/console/
[8]: https://dev.theneura.com/?ref=braze
[9]: {% image_buster /assets/img/moments-of-availability.png %}
[10]: {% image_buster /assets/img_archive/neura-personas-moments.png %}
[11]: {% image_buster /assets/img/neura-braze-api-key.png %}
[12]: {% image_buster /assets/img_archive/neura-mep-details-in-neura.png %}
[13]: {% image_buster /assets/img/action-based-delivery.png %}
[14]: {% image_buster /assets/img/segment-creation.png %}
[19]: {% image_buster /assets/img/insights-bubble-graph.png %}