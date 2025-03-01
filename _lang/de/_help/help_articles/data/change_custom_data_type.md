---
nav_title: Ändern von benutzerdefinierten Attributen oder Ereignisdatentypen
article_title: Ändern von benutzerdefinierten Attributen oder Ereignisdatentypen
page_order: 1

page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie den Datentyp eines benutzerdefinierten Attributs oder eines benutzerdefinierten Ereignisses ändern können und welche Auswirkungen dies hat."
---

# Ändern von benutzerdefinierten Attributen oder Ereignisdatentypen

Um den Datentyp eines benutzerdefinierten Attributs oder Ereignisses zu ändern, navigieren Sie im Braze Dashboard zu **Dateneinstellungen** und wählen Sie entweder **benutzerdefinierte Attribute** oder **benutzerdefinierte Ereignisse**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befinden sich die Seiten **Benutzerdefinierte Ereignisse** und **Benutzerdefinierte Attribute** unter **Einstellungen verwalten**.
{% endalert %}

![Registerkarte Benutzerdefinierte Attribute zum Bearbeiten von Attributen oder Datentypen][1]

Wenn Sie den Datentyp eines benutzerdefinierten Attributs oder Ereignisses ändern müssen (z.B. `time` in `string` ändern), sollten Sie Folgendes beachten:

- Relevante Filter in Segmenten, Kampagnen, Canvases oder anderen Orten, die das geänderte Attribut oder Ereignis verwenden, werden nicht automatisch aktualisiert. Bevor Sie Attribute ändern können, müssen Sie alle Kampagnen oder Canvases stoppen, die die Attribute in Segmenten oder Filtern verwenden, und die Attribute aus Filtern entfernen, die auf sie verweisen.
- Die Benutzerdaten werden nicht rückwirkend aktualisiert. Wenn das geänderte Attribut bereits vor der Änderung des Datentyps in einem Benutzerprofil enthalten war, dann ist dieser Wert immer noch der alte Datentyp. Dies kann dazu führen, dass Benutzer aus den Segmenten herausfallen, die das geänderte Attribut enthalten. Der Filter sucht aktiv nach dem neuen Datentyp, aber wenn ein Profil noch den vorherigen Datentyp hat, wird dieser Benutzer jetzt aus dem Segment ausgeschlossen. Diese Benutzer müssen aktualisiert werden, damit sie wieder in die richtigen Segmente fallen. Sie können dies mit dem [Endpunkt`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) tun.
- Neue Daten werden nicht akzeptiert, wenn sie nicht dem neuen Datentyp entsprechen. Zum Beispiel wird ein API-Aufruf an den Endpunkt `users/track`, der den vorherigen Datentyp für ein geändertes Attribut enthält, nicht akzeptiert. Sie müssen den neuen Datentyp aufrufen.

{% alert important %}
Die Möglichkeit, die automatische Erkennung an der Aktualisierung des Datentyps für benutzerdefinierte Attribute zu hindern, befindet sich derzeit in einer frühen Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an diesem frühen Zugang interessiert sind.
{% endalert %}

_Zuletzt aktualisiert am 8\. Februar 2024_

[1]: {% image_buster /assets/img/change_custom_attribute.png %}