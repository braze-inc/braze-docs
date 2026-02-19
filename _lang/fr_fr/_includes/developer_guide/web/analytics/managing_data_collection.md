## Désactivation du suivi des données

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
Pour désactiver l'activité de suivi des données sur le SDK Web, utilisez la méthode [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Cela synchronisera toutes les données enregistrées avant l'appel de `disableSDK()` et fera en sorte que tous les appels ultérieurs au SDK Web de Braze pour cette page et les chargements de pages ultérieurs seront ignorés.
{% endtab %}

{% tab google tag manager %}
Utilisez le type de balise **Désactiver le suivi** ou **Redémarrer le suivi** pour désactiver ou réactiver le suivi Web, respectivement. Ces deux options appellent [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) et [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Bonnes pratiques

Pour offrir aux utilisateurs la possibilité d'arrêter le suivi, nous vous recommandons de créer une page simple avec deux liens ou boutons : l'un qui appelle `disableSDK()` lorsqu'il est cliqué, et l'autre qui appelle `enableSDK()` pour permettre aux utilisateurs d'opter pour un nouvel abonnement. Vous pouvez utiliser ces contrôles pour démarrer ou arrêter le suivi via d’autres sous-processeurs de données.

{% alert note %}
Le SDK de Braze n'a pas besoin d'être initialisé pour appeler `disableSDK()`, ce qui vous permet de désactiver le suivi pour les utilisateurs totalement anonymes. Inversement,`enableSDK()` n’initialise pas le SDK Braze, vous devez donc également appeler `initialize()` ensuite pour activer le suivi.
{% endalert %}

## Reprise du suivi des données

Pour reprendre la collecte des données, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) méthode.
