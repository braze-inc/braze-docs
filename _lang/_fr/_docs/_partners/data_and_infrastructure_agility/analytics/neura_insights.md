---
nav_title: Aperçus du Neura
article_title: Aperçus du Neura
page_order: 0
alias: /fr/partners/neura_insights/
description: "Cet article décrit le partenariat entre Braze et Neura Insights, une plateforme d’analyse qui vous permet de découvrir les relations entre le comportement réel de chaque utilisateur et les actions qu’il prend dans votre application afin de trouver le meilleur moment pour s’engager avec chaque utilisateur."
page_type: partenaire
search_tag: Partenaire
---

# Aperçus du Neura

> [Neura][1] aide les principales marques mobiles à accroître l'engagement de la clientèle & la rétention avec des aperçus de comportement du monde réel et une segmentation avancée de la campagne &.

*Tirez parti de [Neura Insights][2] pour découvrir les relations entre le comportement réel de chaque utilisateur et les actions qu’il prend dans votre application afin de trouver le meilleur moment pour s’engager avec chaque utilisateur.*

!\[Bubble Graph\]\[9\]

## Détails de l'intégration

Pour intégrer le SDK Neura vous ajoutez simplement quelques lignes de code à votre [AppDelegate sur iOS][3] ou [La classe MainActivity sur Android][4].

Tout d'abord, trouvez votre App ID dans la section "Console Développeur" du tableau de bord Braze et créez une nouvelle clé API avec `utilisateurs. rack`, `users.alias.new` et `users.export.ids` permissions.

!\[neura-braze-api-key.png\]\[10\]

Complétez la section Plateforme d'engagement mobile de votre demande dans la [console Neura][5], comme suit:

**Clé API :** Insérez la clé que vous avez créée sur la plateforme Braze.

**Région :** Braze gère les extrémités du serveur dans différentes régions. Utilisez votre région comme entrée au champ "Serveur".

**Identifiant d'application Android/iOS :** Nous vous recommandons de fournir un ID d'application unique Braze pour chaque plate-forme mobile, vous permettant de segmenter individuellement les utilisateurs pour chaque plateforme.

!\[Détails de Neura MEP en Neura\]\[11\]

Enfin, assurez-vous que les utilisateurs de Braze et Neura sont mappés : Créez un alias utilisateur étiqueté `neura_id` avec le neura_id de votre utilisateur Définissez un attribut utilisateur personnalisé avec la paire clé-valeur `neura, vrai`

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

Set External ID: Similaire à quand la méthode changeUser doit être appelée dans Braze (dès que l'utilisateur est identifié, généralement après la connexion, afin de définir l'identifiant de l'utilisateur), nous vous recommandons également de définir l'ID de l'utilisateur comme ID externe dans Neura :

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

## Envoi des données d'engagement à Neura

L'importation générique de données de Neura permet deux types de méthodes d'importation :

1. Exporter vos données de courant vers Amazon S3. Notre équipe de succès client travaillera avec vous pour traduire les données en Neura.

2. Suivez les instructions pour utiliser Neura [Insights API][6].

Neura ferme la boucle en renvoyant des données réalisables au Brésil, de sorte que vous pouvez exécuter de façon transparente les aperçus du monde réel de Neura directement au Brésil. Après avoir identifié le bon moment d'engagement pour le bon utilisateur, créez facilement des campagnes et des toiles avec [Neura Actions in Braze][7].

!\[insights-moments-personas.png\]\[12\]

Consultez le site [développeur Neura][8] pour plus de détails, tutoriels et FAQ.

{% alert note %}
Le SDK Neura nécessite d'activer les services de localisation.
{% endalert %}
[9]: {% image_buster /assets/img/insights-bubble-graph.png %} [10]: {% image_buster /assets/img/neura-braze-api-key. ng %} [11]: {% image_buster /assets/img_archive/neura-mep-details-in-neura.png %} [12]: {% image_buster /assets/img/insights-moments-personas.png %}


[1]: https://www.theneura.com/
[2]: https://www.theneura.com/neura-insights/?ref=braze
[3]: https://dev.theneura.com/tutorials/ios/?ref=braze
[4]: https://dev.theneura.com/tutorials/android/?ref=braze
[5]: https://dev.theneura.com/console/
[6]: https://dev.theneura.com/pages/how-to-use-engagement-api/?ref=braze
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura
[8]: https://dev.theneura.com/?ref=braze
