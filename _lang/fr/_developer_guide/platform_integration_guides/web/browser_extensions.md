---
nav_title: Extensions de navigateur
article_title: Intégration des extensions de navigateur pour le Web
platform: Web
page_order: 20
page_type: reference
description: "Cet article décrit comment utiliser le SDK Braze pour le Web dans vos extensions de navigateur (Google Chrome, Firefox)."

---

# Intégration de l’extension de navigateur

Intégrez le SDK Braze pour le Web au sein de votre extension de navigateur pour collecter l’analytique et afficher des messages détaillés aux utilisateurs. Cela inclut les **Extensions Google Chrome** et les **Modules Firefox**.

## Ce qui est pris en charge

En général, puisque les extensions sont simplement composées d’HTML et de JavaScript, vous pouvez utiliser Braze pour les éléments suivants :

* **Analytique** : Capturez des événements personnalisés, des attributs et identifiez même les utilisateurs récurrents au sein de votre extension. Utilisez ces caractéristiques de profil pour alimenter les communications multicanales.
* **Messages in-app** : Déclenchez des messages in-app lorsque les utilisateurs agissent au sein de votre extension en utilisant notre messagerie HTML native ou personnalisée .
* **Cartes de contenu** : Ajoutez un flux de cartes natives à votre extension pour l’onboarding ou le contenu promotionnel.
* **Notification push pour le Web** : Envoyez des notifications en temps opportun, même lorsque votre page Web n’est pas actuellement ouverte.

## Ce qui n’est pas pris en charge

* Les services de traitement Manifest v3 ne sont pas compatibles avec l’importation de modules conçus pour les environnements web.

## Types d’extensions

Braze peut être inclus dans les parties suivantes de votre extension :

| Secteur | Détails | Ce qui est pris en charge |
|--------|-------|------|
| Fenêtre contextuelle | La [fenêtre contextuelle][1] est une boîte de dialogue qui peut être affichée aux utilisateurs lorsque vous cliquez sur l’icône de votre extension dans la barre d’outils du navigateur.| Analytique, messages in-app et cartes de contenu |
| Scripts en arrière-plan | Les [scripts en arrière-plan][2] (Manifest v2 uniquement) permettent à votre extension d’inspecter et d’interagir avec la navigation de l’utilisateur ou de modifier des pages Web (par exemple, comment les bloqueurs publicitaires détectent et changent le contenu des pages). | Analytique, messages in-app et cartes de contenu.<br><br>Les scripts en arrière-plan ne sont pas visibles des utilisateurs, donc en ce qui concerne la messagerie, vous devez communiquer à l’aide des onglets du navigateur ou de votre fenêtre contextuelle lors de l’affichage des messages. |
| Pages d’options | La [page d’options][3] permet à vos utilisateurs de basculer des paramètres au sein de l’extension. Il s’agit d’une page HTML autonome qui ouvre un nouvel onglet. | Analytique, messages in-app et cartes de contenu |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## Autorisations

Aucune autorisation supplémentaire n’est requise dans votre `manifest.json` lors de l’intégration du SDK Braze (`braze.min.js`) en tant que fichier local associé à votre extension. 

Cependant, si vous utilisez le [gestionnaire de balises Google][8] ou faites référence au SDK Braze à partir d’une URL externe, ou si vous avez défini une politique de sécurité du contenu stricte pour votre extension, vous devrez ajuster les paramètres [`content_security_policy`][6] dans votre `manifest.json` pour autoriser des sources de script à distance.

## Démarrage

{% alert tip %}
Avant de commencer, assurez-vous que vous avez lu le [guide de configuration initial du SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) pour le Web pour en savoir plus sur notre intégration JavaScript en général.  <br><br>Vous pouvez également mettre en signet la [référence SDK pour JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) pour plus de détails sur toutes les méthodes SDK et les options de configuration différentes.
{% endalert %}

Pour intégrer le SDK Braze pour le Web, vous devez d’abord télécharger une copie de la dernière bibliothèque JavaScript. Vous pouvez le faire à l’aide de NPM ou directement depuis le [CDN (réseau de diffusion de contenu) de Braze][7].

Sinon, si vous préférez utiliser le [gestionnaire de balises Google][8] ou utiliser une copie hébergée à l’extérieur du SDK Braze, gardez à l’esprit que le chargement de ressources externes nécessite de régler le paramètre [`content_security_policy`][6] dans votre `manifest.json`.

Une fois téléchargé, assurez-vous de copier le fichier `braze.min.js` dans le répertoire de votre extension.

### Fenêtres contextuelles d’extension {#popup}

Pour ajouter Braze à une fenêtre contextuelle d’extension, reportez-vous au fichier JavaScript local dans votre `popup.html`, comme vous le feriez sur un site Internet normal. Si vous utilisez Google Tag Manager, vous pouvez ajouter Braze en utilisant nos [modèles Google Tag Manager][8] à la place.

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Script d’arrière-plan (Manifeste v2 uniquement) {#background-script}

Pour utiliser Braze dans le script en l’arrière-plan de votre extension, ajoutez la bibliothèque Braze à votre `manifest.json` dans le tableau `background.scripts`. La variable `braze` sera alors disponible dans votre contexte de script en arrière-plan.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### Pages d’options {#options-page}

Si vous utilisez une page d’options (à l’aide des propriétés de manifeste `options` ou `options_ui`), vous pouvez inclure Braze comme vous le feriez dans les [`popup.html`instructions](#popup).

## Initialisation

Une fois le SDK inclus, vous pouvez initialiser la bibliothèque comme d’habitude. 

Étant donné que les cookies ne sont pas pris en charge dans les extensions de navigateur, vous pouvez les désactiver en initialisant avec `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Pour plus d’informations sur les options d’initialisation que nous prenons en charge, consultez la page [référence du SDK pour le Web][10].

## Notification push

Les boîtes de dialogue contextuelle d’extension ne permettent pas de demander des notifications push (elles ne disposent pas de barre d’URL dans la navigation). Pour vous enregistrer et demander une autorisation de notification push dans la boîte de dialogue contextuelle d’une extension, vous devrez utiliser un contournement par un domaine alternatif, tel que décrit dans [domaine alternatif de notification push][11].

[1]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups
[2]: https://developer.chrome.com/extensions/background_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[6]: https://developer.chrome.com/extensions/contentSecurityPolicy
[7]: https://js.appboycdn.com/web-sdk/latest/braze.min.js
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/
[10]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
