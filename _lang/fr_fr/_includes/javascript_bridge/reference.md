Les messages in-app personnalisés et les bannières HTML personnalisés intégrés à l'application prennent en charge un « pont » JavaScript pour s'interfacer avec le SDK Braze, ce qui vous permet de déclencher des actions Braze personnalisées lorsque les utilisateurs cliquent sur des éléments contenant des liens ou interagissent avec votre contenu. Ces méthodes existent avec la variable globale `brazeBridge` ou `appboyBridge`.

{% alert important %}
Braze vous recommande d'utiliser la variable globale `brazeBridge`. La variable globale `appboyBridge` est obsolète mais continuera à fonctionner pour les utilisateurs existants. Si vous utilisez `appboyBridge`, nous vous suggérons de migrer vers `brazeBridge`. <br><br> `appboyBridge` est obsolète dans les versions suivantes du SDK :<br><br>
- Web : [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android : [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS : [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Par exemple, pour enregistrer un attribut personnalisé et un événement personnalisé, puis fermer le message, vous pouvez utiliser le code JavaScript suivant dans votre code HTML personnalisé :

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### Méthodes de pont Javascript {#bridge}

Les méthodes JavaScript suivantes sont prises en charge dans le code HTML personnalisé pour les messages in-app et les bannières intégrés à l'application :

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Vous ne pouvez pas faire référence à Liquid pour insérer <code>customAttributes</code> en méthodes JavaScript Bridge.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

### Suivi du clic de bouton

Veuillez utiliser la`brazeBridge.logClick(button_id)`méthode pour suivre les clics dans votre code HTML personnalisé.

{% alert note %}
**Bannières :** Seul`brazeBridge.logClick()`(sans arguments) est pris en charge. Les ID des boutons et le suivi des boutons personnalisés sont uniquement pris en charge pour les messages in-app.
{% endalert %}

Pour les messages in-app, il est possible de suivre par programmation les « Boutons 1 » et « Bouton 2 » et les « Clics sur le corps » en utilisant respectivement`brazeBridge.logClick('0')` ,`brazeBridge.logClick('1')` , ou `brazeBridge.logClick()`.

| Clics     | Méthode                       | Pris en charge |
| ---------- | ---------------------------- | --------- |
| Clic dans le corps | `brazeBridge.logClick()`    | Messages in-app et bannières |
| Bouton 1   | `brazeBridge.logClick('0')` | Messages in-app uniquement |
| Bouton 2   | `brazeBridge.logClick('1')` | Messages in-app uniquement |
| Suivi personnalisé des boutons |`brazeBridge.logClick('your custom name here')`| Messages in-app uniquement |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour les messages in-app, il est possible de suivre plusieurs événements de clic sur un bouton par impression. Par exemple, pour fermer un message et enregistrer un clic sur le bouton 2 :

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

Vous pouvez également suivre de nouveaux noms de boutons personnalisés (jusqu’à 100 noms uniques par campagne). Par exemple, `brazeBridge.logClick('blue button')` ou `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Lorsque vous utilisez des méthodes JavaScript dans un`onclick`attribut, veuillez encadrer les valeurs de chaîne de caractères entre guillemets simples afin d'éviter tout conflit avec l'attribut HTML entre guillemets doubles.
{% endalert %}

#### Restrictions (messages in-app uniquement)

- Vous pouvez avoir jusqu’à 100 ID de boutons uniques par campagne.
- Les ID de boutons peuvent contenir jusqu’à 255 caractères chacun.
- Les ID de boutons ne peuvent inclure que des lettres, des chiffres, des espaces, des tirets et des traits de soulignement.
