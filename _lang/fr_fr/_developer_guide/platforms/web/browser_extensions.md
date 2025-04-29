---
nav_title: Extensions de navigateur
article_title: Intégration des extensions de navigateur pour le Web
platform: Web
page_order: 20
page_type: reference
description: "Cet article décrit comment utiliser le SDK Braze pour le Web dans vos extensions de navigateur (Google Chrome, Firefox)."

---

# Extension de navigateur

> Cet article décrit comment utiliser le SDK Braze pour le Web dans vos extensions de navigateur (Google Chrome, Firefox).

Intégrez le SDK Braze pour le Web au sein de votre extension de navigateur pour collecter l’analyse et afficher des messages détaillés aux utilisateurs. Cela comprend les **extensions de Google Chrome** et les **modules complémentaires de Firefox**.

## Ce qui est pris en charge

En général, comme les extensions sont composées de HTML et de JavaScript, vous pouvez utiliser Braze pour ce qui suit :

* **Analyses** : Capturez des événements personnalisés, des attributs et identifiez même les utilisateurs récurrents au sein de votre extension. Utilisez ces caractéristiques de profil pour permettre les messages cross-canaux.
* **Messages in-app :** Déclenchez des messages in-app lorsque les utilisateurs agissent au sein de votre extension en utilisant notre messagerie HTML native ou personnalisée .
* **Cartes de contenu**: Ajoutez un flux de cartes natives à votre extension pour l’onboarding ou le contenu promotionnel.
* **Web Push**: Envoyez des notifications en temps opportun, même lorsque votre page Web n’est pas actuellement ouverte.

## Ce qui n’est pas pris en charge

* Les services de traitement ne sont pas pris en charge par le SDK Web de Braze, mais cette question sera examinée à l'avenir.

## Types d’extensions

Braze peut être inclus dans les parties suivantes de votre extension :

| Secteur | Détails | Ce qui est pris en charge |
|--------|-------|------|
| Fenêtre contextuelle | La page [Popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) est une boîte de dialogue qui peut être affichée aux utilisateurs lorsqu'ils cliquent sur l'icône de votre extension dans la barre d'outils du navigateur.| Analytique, messages in-app et cartes de contenu |
| Scripts en arrière-plan | Les [scripts d'arrière-plan](https://developer.chrome.com/extensions/background_pages) (Manifest v2 uniquement) permettent à votre extension d'inspecter et d'interagir avec la navigation de l'utilisateur ou de modifier les pages web (par exemple, comment les bloqueurs de publicité détectent et modifient le contenu des pages). | Analytique, messages in-app et cartes de contenu.<br><br>Les scripts en arrière-plan ne sont pas visibles des utilisateurs, donc en ce qui concerne la messagerie, vous devez communiquer à l’aide des onglets du navigateur ou de votre fenêtre contextuelle lors de l’affichage des messages. |
| Pages d’options | La [page des options](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) permet à vos utilisateurs de basculer les paramètres de votre extension. Il s’agit d’une page HTML autonome qui ouvre un nouvel onglet. | Analytique, messages in-app et cartes de contenu |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Autorisations

Aucune autorisation supplémentaire n’est requise dans votre `manifest.json` lors de l’intégration du SDK Braze (`braze.min.js`) en tant que fichier local associé à votre extension. 

Toutefois, si vous utilisez [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), ou si vous faites référence au SDK de Braze à partir d'une URL externe, ou si vous avez défini une politique de sécurité du contenu stricte pour votre extension, vous devrez ajuster le paramètre [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) dans votre site `manifest.json` pour autoriser les sources de scripts à distance.

## Démarrage

{% alert tip %}
Avant de commencer, assurez-vous que vous avez lu le [guide de configuration initial]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) du SDK pour le Web pour en savoir plus sur notre intégration JavaScript en général.  <br><br>Vous pouvez également mettre en signet la [référence du SDK JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) pour obtenir tous les détails sur les différentes méthodes et options de configuration du SDK.
{% endalert %}

Pour intégrer le Braze Web SDK, vous devez d'abord télécharger une copie de la dernière bibliothèque JavaScript. Cela peut se faire en utilisant NPM ou en le téléchargeant directement depuis le [réseau de diffusion de contenu de Braze](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Si vous préférez utiliser [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) ou utiliser une copie du SDK de Braze hébergée à l'extérieur, gardez à l'esprit que le chargement de ressources externes vous obligera à ajuster les paramètres de votre SDK dans votre . [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) dans votre `manifest.json`.

Une fois téléchargé, assurez-vous de copier le fichier `braze.min.js` dans le répertoire de votre extension.

### Fenêtres contextuelles d’extension {#popup}

Pour ajouter Braze à une fenêtre contextuelle d’extension, reportez-vous au fichier JavaScript local dans votre `popup.html`, comme vous le feriez sur un site Internet normal. Si vous utilisez Google Tag Manager, vous pouvez ajouter Braze en utilisant nos [modèles Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) à la place.

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

Si vous utilisez une page d’options (à l’aide des propriétés de manifeste `options` ou `options_ui`), vous pouvez inclure Braze comme vous le feriez dans les [instructions `popup.html`](#popup).

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

Pour plus d'informations sur les options d'initialisation prises en charge, consultez la [référence du SDK Web.](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)

## Notification push

Les boîtes de dialogue contextuelle d’extension ne permettent pas de demander des notifications push (elles ne disposent pas de barre d’URL dans la navigation). Ainsi, pour enregistrer et demander l'autorisation de pousser dans la boîte de dialogue Popup d'une extension, vous devrez utiliser un domaine alternatif, comme décrit dans [Domaine alternatif de poussée]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).

