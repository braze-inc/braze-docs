---
nav_title: Ändern von angepassten Attributen oder Ereignisdatentypen
article_title: Ändern von angepassten Attributen oder Ereignisdatentypen
page_order: 1

page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie den Datentyp eines angepassten Attributs oder eines angepassten Events ändern können und welche Auswirkungen dies hat."
---

# Ändern des Typs der angepassten Attribute oder Event-Daten

Um den Datentyp eines angepassten Attributs oder Ereignisses zu ändern, navigieren Sie vom Braze-Dashboard aus zu **Dateneinstellungen** und wählen Sie entweder **angepasste Attribute** oder **angepasste Events**.

![Tab "Angepasste Attribute" zum Bearbeiten von Attributen oder Daten]({% image_buster /assets/img/change_custom_attribute.png %})

Wenn Sie den Datentyp eines angepassten Attributs oder Ereignisses ändern müssen (z.B. von `time` auf `string`), sollten Sie Folgendes beachten:

- Relevante Filter in Segmenten, Kampagnen, Canvase oder anderen Standorten, die das geänderte Attribut oder Ereignis verwenden, werden nicht automatisch aktualisiert. Bevor Sie Attribute ändern können, müssen Sie alle Kampagnen oder Canvase stoppen, die die Attribute in Segmenten oder Filtern verwenden, und die Attribute aus Filtern entfernen, die auf sie referenzieren.
- Nutzerdaten werden nicht rückwirkend aktualisiert. Wenn sich das geänderte Attribut vor der Änderung des Datentyps in einem Nutzerprofil befand, dann ist dieser Wert immer noch der alte Datentyp. Dies kann dazu führen, dass Nutzer:innen aus den Segmenten herausfallen, die das geänderte Attribut enthalten. Der Filter sucht aktiv nach dem neuen Datentyp, aber wenn ein Profil noch den vorherigen Datentyp hat, wird dieser Nutzer:in nun aus dem Segment ausgeschlossen. Diese Nutzer:innen müssen aktualisiert werden, damit sie in die richtigen Segmente zurückfallen. Sie können dies mit dem [Endpunkt `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) tun.
- Neue Daten werden nicht akzeptiert, wenn sie nicht dem neuen Datentyp entsprechen. So wird beispielsweise ein API-Aufruf an den Endpunkt `users/track`, der den vorherigen Datentyp für ein geändertes Attribut enthält, nicht akzeptiert. Sie müssen den neuen Datentyp aufrufen.

{% alert important %}
Die Möglichkeit, die automatische Erkennung am Update des Datentyps für angepasste Attribute zu hindern, befindet sich derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten.
{% endalert %}

_Zuletzt aktualisiert am 8\. Februar 2024_

