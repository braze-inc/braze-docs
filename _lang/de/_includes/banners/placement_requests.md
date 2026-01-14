Wenn Sie [Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), sendet Ihre App eine Anfrage an Braze, um Banner-Nachrichten für jede Platzierung abzurufen.  

- Sie können bis zu **10 Vermittlungen pro Nutzer**: **in** anfragen.  
- Für jede Platzierung gibt Braze das **Banner mit der höchsten Priorität** zurück, das der Nutzer:in erhalten kann.  
- Wenn in einer Sitzung mehr als 10 Vermittlungen angefragt werden, werden nur die ersten 10 zurückgegeben; der Rest wird verworfen.  

Eine App könnte zum Beispiel während einer einzigen Sitzung drei Anfragen für die Platzierung stellen: `homepage_promo`, `cart_abandonment`, und `seasonal_offer`. Jede Anfrage liefert das relevanteste Banner für diese Platzierung.
