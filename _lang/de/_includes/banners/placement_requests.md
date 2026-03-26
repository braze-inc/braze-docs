Wenn Sie [Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), sendet Ihre App eine Anfrage an Braze, um Banner-Nachrichten für jede Platzierung abzurufen.  

- Sie können bis zu **10 Platzierungen pro Aktualisierungsanfrage** anfordern.  
- Für jede Platzierung gibt Braze das **Banner mit der höchsten Priorität** zurück, für das die Nutzer:innen berechtigt sind.  
- Wenn bei einer Aktualisierung mehr als 10 Platzierungen als Anfrage gestellt werden, werden nur die ersten 10 zurückgegeben; die übrigen werden verworfen.  

Beispielsweise könnte eine App in einer Aktualisierungsanfrage drei Platzierungen anfordern: `homepage_promo`,`cart_abandonment` und `seasonal_offer`. Jede Anfrage gibt das für diese Platzierung relevanteste Banner zurück.

#### Rate-Limiting für Aktualisierungsanfragen

Wenn Sie ältere SDK-Versionen verwenden (vor Swift 13.1.0, Android 38.0.0, Internet 6.1.0, React Native 17.0.0 und Flutter 15.0.0), ist nur eine Aktualisierungsanfrage pro Benutzersitzung zulässig.

Wenn Sie neuere Mindest-SDK-Versionen verwenden (SWIFT 13.1.0+, Android 38.0.0+, Internet 6.1.0+, React Native 17.0.0+ und Flutter 15.0.0+), werden Aktualisierungsanfragen durch einen Token-Bucket-Algorithmus gesteuert, um übermäßiges Polling zu verhindern:

- Jede Benutzersitzung beginnt mit fünf Aktualisierungstoken.
- Die Token werden alle 180 Sekunden (3 Minuten) um einen Token aufgefüllt.

Jeder Aufruf `requestBannersRefresh`verbraucht ein Token. Wenn Sie versuchen, eine Aktualisierung durchzuführen, obwohl keine Tokens verfügbar sind, sendet das SDK die Anfrage nicht und protokolliert einen Fehler, bis ein Token wieder aufgefüllt ist. Dies ist für Updates während der Sitzung und Updates, die durch Ereignisse ausgelöst werden, von Bedeutung. Um dynamische Updates durchzuführen (beispielsweise nachdem eine Nutzer:in eine Aktion auf derselben Seite abgeschlossen hat), rufen Sie die Refresh-Methode auf, nachdem das angepasste Event protokolliert wurde. Beachten Sie jedoch die erforderliche Verzögerung, die Braze benötigt, um das Event zu erfassen und zu verarbeiten, bevor die Nutzer:in für eine andere Banner-Kampagne qualifiziert ist.
