---
nav_title: Google Tag Manager
article_title: Google Tag Manager pour le Web
platform: Web
page_order: 20
description: "Cet article explique comment utiliser Google Tag Manager pour déployer Braze sur votre site Internet."

---

# Google Tag Manager

Cet article fournit un guide étape par étape sur la façon d’ajouter le SDK Braze pour le Web à votre site Internet à l’aide de Google Tag Manager.

[Google Tag Manager][2] vous permet d’ajouter, de supprimer et de modifier à distance des balises sur votre site Internet sans avoir besoin d’une version de code de production ou de ressources d’ingénierie.

## Modèles de balises Braze

Braze a construit deux modèles Google Tag Manager : la [balise d’initialisation](#initialization-tag) et la [balise d’actions](#actions-tag).

Ces deux balises peuvent être ajoutées à votre espace de travail depuis la [galerie communautaire de Google][15] ou en recherchant Braze lors de l’ajout d’une nouvelle balise à partir des modèles de la communauté.

![image d’une recherche dans la galerie][3]

### Modèle de balise d’initialisation {#initialization-tag}

Utilisez la balise d’initialisation pour ajouter le SDK Braze pour le Web à votre site Internet.

#### Étape 1 : Sélectionner la balise d’initialisation

Recherchez Braze dans la galerie de modèles de la communauté, puis sélectionnez la **balise d’initialisation de Braze**.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’initialisation de Braze. Les paramètres inclus sont les suivants : « type de balise », « clé API », « endpoint de l’API », « version du SDK », « ID d’utilisateur externe » et « ID de notification push pour le Web de Safari ».][4]

#### Étape 2 : Configurer les paramètres

Saisissez votre clé d’identification de l’API Braze et l’endpoint du SDK, que vous trouverez dans la page **Manage Settings** du tableau de bord.

#### Étape 3 : Choisir les options d’initialisation

Choisissez parmi l’ensemble d’options d’initialisation supplémentaires et facultatives décrites dans le guide de [configuration initiale][7].

#### Étape 4 : Vérifier et réaliser la QA

Une fois que vous avez déployé cette balise, il existe deux manières de vérifier que l’intégration est correcte :

1. À l’aide du mode de débogage de Google Tag Manager, vous devriez voir que la balise d’initialisation de Braze a été déclenchée sur vos pages ou vos événements configurés.
2. Vous devriez voir les demandes réseau faites à Braze et la bibliothèque globale `window.braze` devrait maintenant être définie sur votre page Web.

### Modèle de balises d’actions {#actions-tag}

Le modèle de balises d’actions de Braze vous permet de déclencher des événements personnalisés, de suivre les achats, de modifier les ID utilisateur et d’arrêter ou de reprendre le traçage selon les exigences de confidentialité.

![][5]

#### Modifier l’ID externe de l’utilisateur {#external-id}

Le type de balise **Modifier l’utilisateur** appelle la [`changeUser`méthode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). 

Utilisez cette balise chaque fois qu’un utilisateur se connecte ou est identifié de quelque manière que ce soit par son identifiant unique `external_id`.

Veillez à saisir l’ID unique de l’utilisateur actuel dans le champ **ID externe de l’utilisateur**, généralement rempli à l’aide d’une variable de couche de données envoyée par votre site Internet.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont « type de balise » et « ID externe de l’utilisateur ».][8]

#### Enregistrer les événements personnalisés {#custom-events}

Le type de balise **Événement personnalisé** appelle la [`logCustomEvent`méthode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

Utilisez cette balise pour envoyer des événements personnalisés à Braze. Vous pouvez y inclure, de manière factultative, des propriétés de l’événement personnalisées.

Saisissez le **Nom de l’événement** en utilisant une variable ou en tapant un nom d’événement.

Utilisez le bouton **Ajouter une ligne** pour ajouter les propriétés de l’événement.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le « type de balise » (événement personnalisé), « nom d’événement » (clic de bouton) et les « propriétés de l’événement ».][9]

#### Suivi des achats {#purchases}

Le type de balise **Achat** appelle la [`logPurchase`méthode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase).

Utilisez cette balise pour suivre les achats, y compris les propriétés d’achat, et les envoyer à Braze.

Les champs **Product ID (ID produit)** et **Price (Prix)** sont obligatoires.

Utilisez le bouton **Add Row (Ajouter une ligne)** pour ajouter les propriétés d’achat.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont les suivants : « type de balise », « ID externe », « prix », « code de devise », « quantité » et « propriétés d’achat ».][10]

#### Arrêter et reprendre le suivi {#stop-tracking}

Parfois, il se peut que vous deviez désactiver ou réactiver le suivi effectué par Braze sur votre site Internet, par exemple, après qu’un utilisateur a indiqué qu’il refusait le suivi Web pour des raisons de confidentialité.

Utilisez le type de balise **Désactiver le suivi** ou **Redémarrer le suivi** pour désactiver ou réactiver le suivi Web, respectivement.

#### Attributs utilisateur personnalisés {#custom-attributes}

Les attributs utilisateur personnalisés ne sont pas disponibles en raison d’une limitation dans la langue de script de Google Tag Manager. Pour enregistrer des attributs personnalisés, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Le modèle GTM ne prend pas en charge les propriétés imbriquées pour les événements ou les achats. Vous pouvez utiliser le code HTML précédent pour enregistrer les événements ou les achats qui nécessitent des propriétés imbriquées.
{% endalert %}

#### Attributs utilisateur par défaut {#standard-attributes}

Les attributs utilisateur par défaut, tels que le prénom d’un utilisateur, doivent être enregistrés de la même manière que les attributs utilisateur personnalisés. Assurez-vous que les valeurs que vous transmettez pour les attributs par défaut correspondent au format attendu spécifié dans le document [Classe d’utilisateur][16].

Par exemple, l’attribut genre peut accepter l’un des éléments suivants comme valeurs : "m" | "f"" | "o" | "u" | "n" | "p". Par conséquent, pour définir le sexe d’un utilisateur en tant que femme, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## Étapes de résolution des problèmes {#troubleshooting}

### Activer le débogage des balises {#debugging}

Chaque modèle de balise de Braze dispose d’une case à cocher facultative **Débogage de balises GTM** qui peut être utilisée pour enregistrer les messages de débogage sur la console JavaScript de votre page Web.

![][12]

### Entrer dans le mode débogage

Une autre manière de vous aider à déboguer votre intégration Google Tag Manager est en utilisant le [Mode Prévisualisation][14] de Google.

Il permet d’identifier les valeurs envoyées à partir de la couche de données de votre page Web vers chaque balise de Braze déclenchée et d’expliquer également quelles balises étaient ou non déclenchées.

![La page de résumé de la balise d’initialisation Braze fournit un aperçu de la balise, y compris des informations sur les balises déclenchées.][13]


[2]: https://support.google.com/tagmanager/answer/6103696
[3]: {% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %}
[4]: {% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %}
[5]: {% image_buster /assets/img/web-gtm/gtm-actions-tag.png %}
[6]: {{ site.baseurl }}/user_guide/administrative/app_settings/manage_app_group/app_group_management/#app-group-management
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze
[8]: {% image_buster /assets/img/web-gtm/gtm-change-user.png %}
[9]: {% image_buster /assets/img/web-gtm/gtm-custom-event.png %}
[10]: {% image_buster /assets/img/web-gtm/gtm-purchase.png %}
[12]: {% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %}
[13]: {% image_buster /assets/img/web-gtm/gtm-debug-mode.png %}
[14]: https://support.google.com/tagmanager/answer/6107056
[15]: https://tagmanager.google.com/gallery/#/?filter=braze
[16]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html
