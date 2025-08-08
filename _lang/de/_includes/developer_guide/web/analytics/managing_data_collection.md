## Deaktivieren des Trackings von Daten

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab Standardimplementierung %}
Um das Tracking von Daten im Internet SDK zu deaktivieren, verwenden Sie die Methode [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Dadurch werden alle Daten synchronisiert, die vor dem Aufruf von `disableSDK()` aufgezeichnet wurden, und alle nachfolgenden Aufrufe des Braze Web SDK für diese Seite und zukünftige Seitenladungen werden ignoriert.
{% endtab %}

{% tab Google Tag Manager %}
Verwenden Sie den Tag-Typ **Tracking deaktivieren** oder **Tracking fortsetzen**, um das Web Tracking zu deaktivieren bzw. wieder zu aktivieren. Diese beiden Optionen rufen [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) und [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Bewährte Praktiken

Um Nutzern die Möglichkeit zu geben, das Tracking zu beenden, empfehlen wir, eine einfache Seite mit zwei Links oder Buttons zu erstellen: einen, der `disableSDK()` aufruft, wenn er angeklickt wird, und einen anderen, der `enableSDK()` aufruft, um Nutzern:in die Möglichkeit zu geben, sich wieder zu entscheiden. Mit diesen Steuerelementen können Sie das Tracking auch über andere Daten-Subprozessoren starten oder beenden.

{% alert note %}
Das Braze SDK muss nicht initialisiert werden, um `disableSDK()` aufzurufen. So können Sie das Tracking für völlig anonyme Nutzer:innen deaktivieren. Umgekehrt wird das Braze SDK nicht durch `enableSDK()` initialisiert, sodass Sie anschließend auch `initialize()` aufrufen müssen, um das Tracking zu aktivieren.
{% endalert %}

## Wiederaufnahme des Trackings von Daten

Um die Datenerfassung wieder aufzunehmen, können Sie die [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) Methode nutzen.
