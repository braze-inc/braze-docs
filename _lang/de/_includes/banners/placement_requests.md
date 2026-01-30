Wenn Sie [Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), sendet Ihre App eine Anfrage an Braze, um Banner-Nachrichten für jede Platzierung abzurufen.  

- Sie können bis zu **10 Platzierungen pro Aktualisierungsanfrage** anfordern.  
- Für jede Platzierung gibt Braze das **Banner mit der höchsten Priorität** zurück, das der Nutzer:in erhalten kann.  
- Wenn bei einer Aktualisierung mehr als 10 Platzierungen angefragt werden, werden nur die ersten 10 zurückgegeben; der Rest wird verworfen.  

Eine App könnte zum Beispiel in einer Aktualisierungsanfrage drei Platzierungen anfordern: `homepage_promo`, `cart_abandonment`, und `seasonal_offer`. Jede Anfrage liefert das relevanteste Banner für diese Platzierung.

#### Rate-Limiting für Aktualisierungsanfragen

Bei älteren SDK-Versionen (vor Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 und Flutter 15.0.0) ist nur eine Anfrage zur Aktualisierung pro Nutzer:innen erlaubt.

Bei neueren SDK-Versionen (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ und Flutter 15.0.0+) werden die Anfragen zur Aktualisierung durch einen Token Bucket-Algorithmus gesteuert, um übermäßiges Polling zu verhindern:

- Jede Nutzer:innen-Sitzung beginnt mit fünf Token für die Aktualisierung.
- Die Token werden alle 180 Sekunden (3 Minuten) um einen Token aufgefüllt.

Jeder Aufruf von `requestBannersRefresh` verbraucht ein Token. Wenn Sie eine Aktualisierung versuchen, während keine Token verfügbar sind, führt das SDK die Anfrage nicht aus und protokolliert einen Fehler, bis ein Token nachgefüllt wird. Dies ist wichtig für Updates mitten in der Sitzung und für ereignisgesteuerte Updates. Um dynamische Updates zu implementieren (z. B. nachdem ein Nutzer eine Aktion auf derselben Seite abgeschlossen hat), rufen Sie die Refresh-Methode auf, nachdem das angepasste Event protokolliert wurde. Beachten Sie jedoch die notwendige Verzögerung, damit Braze das Event aufnehmen und verarbeiten kann, bevor sich der Nutzer für eine andere Banner-Kampagne qualifiziert.
