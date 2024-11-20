---
nav_title: Google Tag Manager
article_title: Google Tag Manager pour le Web
platform: Web
page_order: 20
description: "Cet article explique comment utiliser Google Tag Manager pour déployer Braze sur votre site Internet."

---

# Google Tag Manager

> Cet article fournit un guide étape par étape sur la façon d’ajouter le SDK Braze pour le Web à votre site Internet à l’aide de Google Tag Manager (GTM). [Google Tag Manager](https://support.google.com/tagmanager/answer/6103696) vous permet d'ajouter, de supprimer et de modifier à distance des tags sur votre site web, sans nécessiter de code de production ni de ressources d'ingénierie.

Il existe deux tags Google Tag Manager créés par Braze, le [tag d'initialisation](#initialization-tag) et le [tag d'actions](#actions-tag).

Ces deux tags peuvent être ajoutés à votre espace de travail à partir de la [galerie communautaire de Google](https://tagmanager.google.com/gallery/#/?filter=braze) ou en recherchant Braze lors de l'ajout d'une nouvelle étiquette à partir des modèles communautaires.

![image de la recherche de la galerie]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## Mise à jour des règles de consentement des utilisateurs de Google dans l'UE

{% alert important %}
Google met à jour ses [règles de consentement des utilisateurs de l'Union européenne](https://www.google.com/about/company/user-consent-policy/) en réponse aux changements apportés à la [loi sur les marchés numériques (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), en vigueur à partir du 6 mars 2024. Ce nouveau changement oblige les annonceurs à divulguer certaines informations à leurs utilisateurs finaux dans l'EEE et au Royaume-Uni, et à obtenir d'eux les consentements nécessaires. Consultez la documentation suivante pour en savoir plus.
{% endalert %}

Dans le cadre de la politique de consentement de l'utilisateur de l'UE de Google, les attributs personnalisés booléens suivants doivent être enregistrés dans les profils utilisateurs :

- `$google_ad_user_data`
- `$google_ad_personalization`

Si vous les définissez via l'intégration GTM, les attributs personnalisés nécessitent la création d'une balise HTML personnalisée. L'exemple suivant montre comment enregistrer ces valeurs en tant que types de données booléennes (et non en tant que chaînes de caractères) :

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Pour plus d'informations, reportez-vous à la section [Synchronisation de l'audience avec Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).

## Modèle de balise d’initialisation {#initialization-tag}

Utilisez la balise d’initialisation pour ajouter le SDK Braze pour le Web à votre site Internet.

### Étape 1 : Configurer les notifications push (facultatif)

Si vous souhaitez envoyer des messages push par l'intermédiaire du Google Tag Manager, suivez d'abord les tags d'[intégration des messages push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/):
1. Configurez le service de traitement de votre site, en le plaçant dans le répertoire racine de votre site.
2. Configurez l'enregistrement du navigateur - Une fois le service de traitement configuré, vous devez définir la méthode `braze.requestPushPermission()` soit de manière native dans leur application, soit par le biais d'une balise HTML personnalisée (via le tableau de bord de GTM). Vous devrez également vous assurer que la balise est activée après l'initialisation du SDK.

### Étape 2 : Sélectionner la balise d’initialisation

Recherchez Braze dans la galerie de modèles de la communauté, puis sélectionnez la **balise d’initialisation de Braze**.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’initialisation de Braze. Les paramètres inclus sont "type d'étiquette", "clé API", "endpoint API", "version SDK", "external user ID" et "Safari web push ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Étape 3 : Configurer les paramètres

Saisissez votre clé d’identification de l’API Braze et l’endpoint du SDK, que vous trouverez dans la page **Gérer les paramètres** de votre tableau de bord. Entrez la version `major.minor` la plus récente du SDK Web. Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Vous pouvez consulter la liste des versions du SDK dans notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Étape 4 : Choisir les options d’initialisation

Choisissez parmi l'ensemble d'options d'initialisation supplémentaires décrites dans le guide [Initial setup]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze).

### Étape 5 : Vérifier et réaliser la QA

Une fois que vous avez déployé cette balise, il existe deux manières de vérifier que l’intégration est correcte :

1. En utilisant l' [outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, vous devriez voir que l'étiquette d'initialisation Braze a été déclenchée sur vos pages ou événements configurés.
2. Vous devriez voir les demandes réseau faites à Braze et la bibliothèque globale `window.braze` devrait maintenant être définie sur votre page Web.

## Modèle de balise d’actions {#actions-tag}

Le modèle de balises d’actions de Braze vous permet de déclencher des événements personnalisés, de suivre les achats, de modifier les ID utilisateur et d’arrêter ou de reprendre le traçage selon les exigences de confidentialité.

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### Modifier l’ID externe de l’utilisateur {#external-id}

Le type de balise **Modifier l’utilisateur** appelle la méthode [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). 

Utilisez cette balise chaque fois qu’un utilisateur se connecte ou est identifié de quelque manière que ce soit par son identifiant unique `external_id`.

Veillez à saisir l'ID unique de l'utilisateur actuel dans le champ **ID externe**, généralement rempli à l'aide d'une variable de couche de données envoyée par votre site web.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le "type d'étiquette" et l'"ID externe".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### Consigner un événement personnalisé {#custom-events}

Le type de balise **Événement personnalisé** appelle la méthode [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

Utilisez cette balise pour envoyer des événements personnalisés à Braze. Vous pouvez y inclure, de manière facultative, des propriétés d’événement personnalisé.

Saisissez le **nom de l'événement** en utilisant une variable ou en tapant un nom d'événement.

Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'événement.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le "type d'étiquette" (événement personnalisé), le "nom de l'événement" (clic sur un bouton) et les "propriétés d'événement".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### Événements d’e-commerce {#ecommerce}

Si votre site enregistre les achats à l'aide de l'élément de couche de données d'[événement e-commerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) standard dans Google Tag Manager, vous pouvez utiliser le type d'étiquette **E-commerce Purchase.**  Ce type d’action enregistre un « achat » séparé dans Braze pour chaque article envoyé dans la liste de `items`.

Vous pouvez également préciser les noms supplémentaires des propriétés que vous souhaitez inclure comme propriétés d’achat en spécifiant leurs clés dans la liste des Propriétés d’achat. Veuillez remarquer que Braze observe la personne `item` qui est enregistrée pour toute propriété d’achat que vous ajoutez à la liste.

Par exemple, imaginons que votre charge utile d’e-commerce contient les `items` suivants :

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Si vous souhaitez transmettre uniquement`item_brand` et `item_name` comme propriétés d’achat, il vous suffit d’ajouter ces deux champs au tableau des propriétés d’achat. Si vous ne fournissez pas de propriétés, aucune propriété d'achat ne sera envoyée dans l'appel à Braze. [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) à Braze.

### Suivre l’achat {#purchases}

Le type de balise **Achat** appelle la méthode [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase).

Utilisez cette balise pour suivre les achats avec Braze, y compris, en option, les propriétés d’achat.

Les champs **ID produit** et **Prix** sont obligatoires.

Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'achat.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le "type d'étiquette", l'"ID externe", le "prix", le "code devise", la "quantité" et les "propriétés d'achat".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### Arrêter et redémarrer le suivi {#stop-tracking}

Parfois, il se peut que vous deviez désactiver ou réactiver le suivi effectué par Braze sur votre site Internet, par exemple, après qu’un utilisateur a indiqué qu’il refusait le suivi Web pour des raisons de confidentialité.

Utilisez le type de balise **Désactiver le suivi** ou **Redémarrer le suivi** pour désactiver ou réactiver le suivi Web, respectivement. Ces deux options appellent [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) et [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

### Attributs utilisateur personnalisés {#custom-attributes}

Les attributs utilisateur personnalisés ne sont pas disponibles en raison d’une limitation dans la langue de script de Google Tag Manager. Pour enregistrer des attributs personnalisés, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Le modèle GTM ne prend pas en charge les propriétés imbriquées pour les événements ou les achats. Vous pouvez utiliser le code HTML précédent pour enregistrer les événements ou les achats qui nécessitent des propriétés imbriquées.
{% endalert %}

### Attributs utilisateur standards {#standard-attributes}

Les attributs utilisateur standards, tels que le prénom d’un utilisateur, doivent être enregistrés de la même manière que les attributs utilisateur personnalisés. Assurez-vous que les valeurs que vous transmettez pour les attributs standard correspondent au format attendu spécifié dans la documentation de la [classe User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Par exemple, l'attribut gender peut accepter l'une des valeurs suivantes : `"m" | "f" | "o" | "u" | "n" | "p"`. Par conséquent, pour définir le sexe d’un utilisateur en tant que femme, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## Intégrer des cartes de contenu

Quelques étapes supplémentaires sont nécessaires pour intégrer le canal d'envoi de messages [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) à l'aide de Google Tag Manager. Google Tag Manager fonctionne en injectant le [réseau de diffusion de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (une version de notre SDK Web) directement dans le code de votre site web, ce qui signifie que toutes les méthodes du SDK sont disponibles comme si vous aviez intégré le SDK sans Google Tag Manager, sauf lors de l'implémentation des cartes de contenu.

### Option 1 : Intégrer en utilisant GMT

Pour une intégration standard du flux de la carte de contenu, vous pouvez utiliser une étiquette **HTML personnalisée** dans Google Tag Manager. Ajoutez ce qui suit à votre balise HTML personnalisée, ce qui activera le flux de carte de contenu standard :

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuration dans Google Tag Manager d'une étiquette HTML personnalisée qui affiche le flux de la carte de contenu.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### Option 2 : Intégrer directement dans votre site Internet

Pour obtenir plus de libertés pour personnaliser l’apparence de vos cartes de contenu et leurs flux, vous pouvez intégrer directement les cartes de contenu dans votre site Internet natif. Vous pouvez suivre deux approches dans ce domaine : utiliser l’IU de flux standard ou créer une IU de flux personnalisée.

#### Flux standard

Lors de l'implémentation de l'[interface utilisateur standard]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), les méthodes de Braze doivent être précédées de `window.`. Par exemple, `braze.showContentCards` devrait être `window.braze.showContentCards` à la place.

#### IU de flux personnalisée

Pour l’habillage du [flux personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling), les étapes sont les mêmes que si vous aviez intégré le SDK sans GTM. Par exemple, si vous désirez personnaliser la largeur de votre flux de carte de contenu, vous pouvez coller ce qui suit dans votre fichier CSS :

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## Mettre à niveau et mettre à jour les modèles {#upgrading}

Pour obtenir la dernière version du SDK Web de Braze, effectuez les trois étapes suivantes dans votre tableau de bord Google Tag Manager :

1. **Mise à jour du modèle de balise**<br>Accédez à la page **Modèles** de votre espace de travail. Vous devez y voir une icône indiquant qu’une mise à jour est disponible.<br><br>![Modèles de page indiquant qu'une mise à jour est disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Cliquez sur cette icône et, après avoir révisé la modification, cliquez sur **Accepter la mise à jour**.<br><br>![Un écran comparant les anciens et les nouveaux modèles d'étiquettes avec un bouton pour "Accepter la mise à jour"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Mise à jour du numéro de version**<br>Une fois votre modèle de balise mis à jour, modifiez la balise d’initialisation Braze et mettez à jour la version SDK sur la version la plus récente`major.minor`. Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Vous pouvez consulter la liste des versions du SDK dans notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modèle d'initialisation de Braze avec un champ de saisie pour changer la version du SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **AQ et publication**<br>Vérifiez que la nouvelle version du SDK fonctionne à l'aide de l' [outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager avant de publier une mise à jour de votre conteneur d'étiquettes.

## Résolution des problèmes d’étapes {#troubleshooting}

### Activer le débogage de balise {#debugging}

Chaque modèle de balise de Braze dispose d’une case à cocher facultative **Débogage de balises GTM** qui peut être utilisée pour enregistrer les messages de débogage sur la console JavaScript de votre page Web.

![L'outil de gestion de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### Entrer dans le mode débogage

Un autre moyen de déboguer l'intégration de Google Tag Manager est d'utiliser la fonctionnalité de [prévisualisation](https://support.google.com/tagmanager/answer/6107056) de Google.

Cela permet d'identifier les valeurs envoyées par la couche de données de votre page web à chaque étiquette Braze déclenchée et d'expliquer quelles étiquettes ont été déclenchées ou non.

![La page de résumé de l'étiquette d'initialisation de Braze fournit un aperçu de l'étiquette, y compris des informations sur les tags qui ont été déclenchés.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### Activer la jounalisation verbeuse

Pour permettre à l’assistance technique de Braze de soutenir les journaux d’accès lors du test, vous pouvez activer la journalisation verbeuse sur votre intégration de Google Tag Manager. Ces journaux apparaîtront dans l'onglet **Console** des outils de développement de votre navigateur [.](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)

Dans votre intégration Google Tag Manager, accédez à votre balise d’initialisation Braze et sélectionnez **Activer la journalisation du SDK Web**.

![La page de résumé de l'étiquette d'initialisation de Braze avec l'option Activer la journalisation du SDK Web activée.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
