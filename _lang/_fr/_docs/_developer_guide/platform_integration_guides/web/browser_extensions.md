---
nav_title: Extensions de navigateur
article_title: Intégration des extensions de navigateur Web
platform: Web
page_order: 20
page_type: Référence
description: "Cet article décrit comment utiliser le Braze Web SDK dans vos extensions de navigateur (Google Chrome, Firefox)."
---

# Intégration de l'extension de navigateur

Intégrez le SDK Web de Braze au sein de votre extension de navigateur pour collecter les statistiques et afficher la riche messagerie aux utilisateurs! Cela inclut les **extensions Google Chrome** et **extensions Firefox**.

## Ce qui est supporté

En général, puisque les extensions sont simplement HTML et Javascript, vous pouvez utiliser Braze pour les suivants :

* **Analytics** Capturez des événements personnalisés, des attributs et même identifiez des utilisateurs répétés dans votre extension. Utilisez ces caractéristiques de profil pour alimenter la messagerie inter-canaux.
* **Messages In-App** Déclenchez les messages In-App lorsque les utilisateurs prennent des mesures dans votre extension, en utilisant notre messagerie HTML native ou personnalisée !
* **Cartes de Contenu** Ajoutez un flux de cartes natives à votre extension pour l'intégration ou le contenu promotionnel.
* **Web Push** Envoyer des notifications en temps opportun même lorsque votre page Web n'est pas ouverte actuellement.

## Types d'extension
Braze peut être inclus dans les domaines suivants de votre extension:

| Zone de stockage       | Détails du produit                                                                                                                                                                                                                                     | Ce qui est supporté                                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Page pop-up            | La page [Popup][1] est une boîte de dialogue qui peut être affichée aux utilisateurs en cliquant sur l'icône de votre extension dans la barre d'outils du navigateur.                                                                                  | Analytics, Messages In-App, Cartes de Contenu                                                                                                                                                                                                                      |
| Scripts d'arrière-plan | [Les scripts d'arrière-plan][2] permettent à votre extension d'inspecter et d'interagir avec la navigation de l'utilisateur, ou modifier les pages Web (par exemple, comment les bloqueurs de publicités détectent et modifient le contenu des pages). | Analytics, Messages In-App, Cartes de Contenu. Note : Les scripts d'arrière-plan ne sont pas visibles pour les utilisateurs, donc pour la messagerie, vous devrez communiquer avec les onglets du navigateur ou votre page popup lors de l'affichage des messages. |
| Pages d'options        | La page des options [][3] permet à vos utilisateurs de basculer les paramètres dans votre extension. C'est une page HTML autonome qui ouvre un nouvel onglet.                                                                                          | Analytics, Messages In-App, Cartes de Contenu                                                                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## Permissions

Aucune autorisation supplémentaire n'est requise dans votre manifeste `. son` lors de l'intégration du Braze SDK (`appboy.min.js`) en tant que fichier local, livré avec votre extension.

Cependant, si vous utilisez \[Google Tag Manager\]\[8\], ou référencez le SDK de Braze à partir d'une URL externe, ou ont défini une politique de sécurité de contenu stricte pour votre extension, vous devrez ajuster le paramètre [`content_security_policy`][6] dans votre manifeste `. son` pour autoriser les sources de script distantes.

## Commencer

{% alert tip %}
Avant de commencer, assurez-vous que vous avez lu le [Guide d'installation initial du SDK du Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) pour en savoir plus sur notre intégration Javascript en général.  <br><br>Vous pouvez également vouloir ajouter la [Référence JavaScript SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html) pour plus de détails sur toutes les différentes méthodes SDK et options de configuration.
{% endalert %}

Pour intégrer le Web SDK de Braze, vous devez d'abord télécharger une copie de la dernière bibliothèque Javascript. Cela peut être fait en utilisant NPM, ou téléchargez directement à partir du CDN de [Braze][7].

Alternativement, si vous préférez utiliser \[Google Tag Manager\]\[8\] ou utiliser une copie hébergée en externe du SDK, Gardez à l'esprit que le chargement des ressources externes vous demandera d'ajuster votre paramètre [`content_security_policy`][6] dans votre manifeste `. fils`.

Une fois téléchargé, assurez-vous de copier le fichier `appboy.min.js` quelque part dans le répertoire de votre extension. Par exemple, en utilisant le NPM :

```bash
npm install --save @braze/web-sdk;
cp node_modules/@braze/web-sdk/appboy.min.js /path/to/extension
```

### popups d'extension {#popup}

Ajouter Braze à une popup d'extension est facile ! Il suffit de référencer le fichier JavaScript local dans votre `popup.html`, comme vous le feriez dans un site web régulier. Si vous utilisez Google Tag Manager, vous pouvez ajouter Braze en utilisant notre \[Google Tag Manager Templates\]\[8\] à la place.

```html
<html>popup
    <title>tml</title>
    <! - Ajoute la bibliothèque Braze -->
    <script src="/relative/path/to/appboy.min.js"></script>
    <script>
    // Initialise Braze ici
    </script>
</html>
```

### Script d'arrière-plan {#background-script}

Pour utiliser Braze dans le script d'arrière-plan de votre extension, ajoutez la bibliothèque Braze à votre `manifest.json` dans le tableau `background.scripts`. Cela rendra la variable globale `appboy` disponible dans votre contexte de script en arrière-plan.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/appboy.min.js",
            "background.js"
        ],
    }
 } }
```

### Page des options {#options-page}

Si vous utilisez une page d'options (via les propriétés du manifeste `options` ou `options_ui` ), vous pouvez inclure Braze comme vous le feriez dans le popup [`. instructions` tml](#popup).

## Initialisation

Une fois le SDK inclus, vous pouvez initialiser la bibliothèque comme d'habitude.

Remarque : puisque les cookies ne sont pas pris en charge dans les extensions du navigateur, vous pouvez désactiver l'utilisation des cookies en initialisant avec `noCookies: true`.

Pour en savoir plus sur les différentes options d'initialisation que nous supportons, consultez notre [référence Web SDK][10].

```javascript
appboy.initialize("VOTRE-API-KEY-ICI", {
    baseUrl: "",
    enableLogging: true,
    noCookies: true
});
```

## Pousser

Les boîtes de dialogue d'extension Popup ne permettent pas les messages push (ils n'ont pas la barre d'URL dans la navigation). Donc, afin de s'inscrire et de demander l'autorisation Push dans la fenêtre de dialogue Popup d'une extension, vous devrez utiliser un autre domaine de contournement, tel que décrit dans notre guide\[11\] \[Domaine Push Alternatif\].
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/ [11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain

[1]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups
[2]: https://developer.chrome.com/extensions/background_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[6]: https://developer.chrome.com/extensions/contentSecurityPolicy
[7]: https://js.appboycdn.com/web-sdk/latest/appboy.min.js
[10]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initialize
