---
nav_title: Gestionnaire de tags Google
article_title: Google Tag Manager pour le Web
platform: Web
page_order: 20
description: "Cet article explique comment utiliser Google Tag Manager pour déployer Braze sur votre site Web."
---

# Gestionnaire de tags Google

Cet article fournit un guide étape par étape sur la façon d'ajouter le SDK Web Braze à votre site Web en utilisant Google Tag Manager.

[Google Tag Manager][2] vous permet d'ajouter, de supprimer et de modifier à distance des tags sur votre site Web sans avoir besoin d'une version de code de production ou de ressources techniques.

## Modèles de balise Braze

Il y a deux modèles Google Tag Manager construits par Braze: le [Tag d'initialisation](#initialization-tag) et le [Tag d'actions](#actions-tag).

Les deux balises peuvent être ajoutées à votre espace de travail à partir de la [Galerie de Communauté Google][15], ou en recherchant Braze en ajoutant une nouvelle balise à partir des gabarits de la Communauté.

!\[Recherche dans la Galerie de la Communauté\]\[3\]

### Modèle de balise d'initialisation {#initialization-tag}

Utilisez la balise d'initialisation pour ajouter le SDK Web Braze à votre site Web.

#### Étape 1 : Sélectionnez le tag d'initialisation

Recherchez "Braze" dans la galerie de modèles de communauté, et sélectionnez la **balise d'initialisation de Braze** comme indiqué ci-dessous.

!\[Modèle d'étiquette d'initialisation\]\[4\]

#### Étape 2. Configurer les paramètres

Entrez votre clé d'API Braze SDK et votre point de terminaison SDK, qui peuvent être trouvés dans la page \[Settings\]\[6\] de votre tableau de bord.

#### Étape 3. Choisir les options d'initialisation

Choisissez parmi l'ensemble optionnel d'options d'initialisation supplémentaires telles que décrites dans le guide \[Initial Setup\]\[7\].

#### Étape 4 : Vérifier et QA

Une fois que vous avez déployé ce tag, il y a deux façons de vérifier une bonne intégration :

Tout d'abord, en utilisant le mode débogage du Gestionnaire de Google Tags, vous devriez voir que le Tag d'Initialisation de Braze a été déclenché sur vos pages ou événements configurés.

Deuxièmement, vous devriez voir les requêtes de réseau faites à Braze, et la bibliothèque globale `window.appboy` devrait maintenant être définie sur votre page Web.

### Modèle de tag actions {#actions-tag}

Le modèle de balise Braze Actions vous permet de déclencher des événements personnalisés, de suivre les achats, de modifier les identifiants d'utilisateur et d'arrêter ou de reprendre le suivi pour les exigences de confidentialité.

!\[Modèle de Tag Actions \]\[5\]

#### Changement de l'ID externe de l'utilisateur {#external-id}

La balise **Change User** appelle la méthode [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#changeuser).

Utilisez ce tag à chaque fois qu'un utilisateur se connecte, ou est autrement identifié avec leur identifiant unique `external_id`.

Assurez-vous de saisir l'ID unique de l'utilisateur actuel dans le champ **ID utilisateur externe** généralement peuplé en utilisant une variable de datalayer envoyée par votre site Web.

!\[Changer la balise utilisateur\]\[8\]

#### Journaliser les événements personnalisés {#custom-events}

La balise __Événement personnalisé__ appelle la méthode [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcustomevent).

Utilisez ce tag pour envoyer des événements personnalisés à Braze, y compris éventuellement des propriétés d'événement personnalisées.

Entrez le **nom d'événement** en utilisant une variable ou en tapant un nom d'événement.

Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'événement.

!\[Tag d'Événement Personnalisé\]\[9\]

#### Suivre l'achat {#purchases}

Le tag **Achat** appelle la méthode [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logpurchase).

Utilisez ce tag pour suivre l'achat vers Braze, y compris éventuellement les propriétés d'achat.

Les champs **ID du produit** et **Prix** sont requis.

Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'achat.

!\[Étiquette d'achat\]\[10\]

#### Arrêter et reprendre le suivi {#stop-tracking}

Parfois, vous pourriez être requis pour désactiver ou réactiver le suivi de Braze sur votre site web, par exemple, après qu'un utilisateur indique qu'il a choisi de ne plus suivre le web pour des raisons de confidentialité.

Utilisez le tag **Désactiver le suivi** ou **Reprendre le type de tag** pour désactiver le suivi web ou réactiver le suivi web, respectivement.

#### Attributs utilisateur personnalisés {#custom-attributes}

Les attributs utilisateur personnalisés ne sont pas disponibles en raison d'une limitation dans la langue de script du Gestionnaire de Google Tags. Pour enregistrer les attributs personnalisés, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
window.appboy.getUser().setCustomUserAttribute("nom de l'attribut", "valeur de l'attribut");
</script>
```

{% alert important %}
Le modèle GTM ne prend pas en charge les propriétés imbriquées sur les événements ou achats en ce moment. Vous pouvez utiliser le code HTML ci-dessus pour enregistrer tous les événements ou achats qui nécessitent des propriétés imbriquées.
{% endalert %}

#### Attributs par défaut de l'utilisateur {#standard-attributes}

Les attributs par défaut, tels que le prénom d'un utilisateur, doivent être enregistrés de la même manière que les attributs d'un utilisateur personnalisé. Assurez-vous que les valeurs que vous passez pour les attributs par défaut correspondent au format attendu spécifié dans la documentation de la [classe utilisateur][16].

Par exemple, l'attribut genre peut accepter n'importe lequel des valeurs suivantes en tant que valeurs: `"m" | "f" | "o" | "u" | "n" | "p"`. Par conséquent, pour définir le sexe d'un utilisateur en tant que femme, créez un tag HTML personnalisé avec le contenu suivant :

```html
<script>
window.appboy.getUser().setGender("f")
</script>
```

## Étapes de dépannage {#troubleshooting}

### Activer le débogage des tags {#debugging}

Chaque modèle de balise Braze a une case à cocher **GTM Tag Debugging** facultative qui peut être utilisée pour enregistrer les messages de débogage dans la console Javascript de votre page Web.

!\[Option de débogage du tag\]\[12\]

### Passer en mode débogage

Une autre façon d'aider à déboguer votre intégration dans Google Tag Manager est d'utiliser la fonctionnalité de [Mode Aperçu][14] de Google.

Cela aidera à identifier les valeurs qui sont envoyées depuis le datalayer de votre page Web à chaque balise Braze déclenchée, et expliquera également quelles balises ont été ou n'ont pas été déclenchées.

!\[Mode Aperçu\]\[13\]
[3]: {% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %} [4]: {% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %} [5]: {% image_buster /assets/img/web-gtm/gtm-actions-tag. ng %} [6]: {{ site.baseurl }}/user_guide/administrative/app_settings/manage_app_group/app_group_management/#app-group-management [7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze [8]: {% image_buster /assets/img/web-gtm/gtm-change-user. ng %} [9]: {% image_buster /assets/img/web-gtm/gtm-custom-event.png %} [10]: {% image_buster /assets/img/web-gtm/gtm-purchase. ng %} [12]: {% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %} [13]: {% image_buster /assets/img/web-gtm/gtm-debug-mode.png %}


[2]: https://support.google.com/tagmanager/answer/6103696
[14]: https://support.google.com/tagmanager/answer/6107056
[15]: https://tagmanager.google.com/gallery/#/?filter=braze
[16]: https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html
