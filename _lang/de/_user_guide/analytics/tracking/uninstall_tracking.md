---
nav_title: Uninstall-Tracking
article_title: Uninstall-Tracking
page_order: 6
page_type: reference
description: "Dieser referenzierte Artikel behandelt die Implementierung von Uninstall-Tracking für Statistiken auf Kampagnen- und App-Ebene."
tool: Reports

---

# Uninstall-Tracking

> Dieser Artikel zeigt Ihnen, wie Sie die Gesamtheit der App-Deinstallationen im Laufe der Zeit betrachten können, um Trends und Anomalien zu erkennen, und wie Sie Deinstallationen auf Kampagnenebene verfolgen können, um festzustellen, ob eine bestimmte Kampagne App-Installationen fördert oder verhindert.

Uninstall-Tracking in Braze liefert die folgenden Details:

1. Tägliche Deinstallationsstatistiken auf App-Ebene in einem Zeitreihendiagramm auf der **Startseite**.
2. Deinstallationsstatistiken auf Kampagnenebene in einem Zeitreihendiagramm auf der Seite **Kampagnendetails** für eine bestimmte Kampagne. Diese Statistik gibt die Anzahl der Empfänger:innen von Kampagnen an, die jeden Tag deinstallieren.

{% alert note %}
Sie müssen Opt-in für das Uninstall-Tracking in Ihrem Braze-Dashboard auswählen. Dieses Feature ist derzeit für Apps auf iOS, Android und Fire OS verfügbar.
{% endalert %}

## Funktionsweise

Braze sammelt automatisch eine Basisebene an Deinstallationsinformationen aus Ihren regelmäßigen Push-Kampagnen. Da die Häufigkeit, mit der verschiedene Nutzer Push Kampagnen erhalten, jedoch variieren kann, bieten wir Ihnen ein Uninstall-Tracking an, um eine genauere Momentaufnahme der Deinstallationsaktivitäten Ihrer Nutzer:innen zu erhalten.

## Einschalten des Uninstall-Trackings

Sie können das Tracking der Deinstallation auf der Seite **App-Einstellungen** unter **Einstellungen** für jede App, die Sie verfolgen möchten, aktivieren.

Wenn das Uninstall-Tracking für eine App aktiviert ist, werden nachts im Hintergrund Push-Nachrichten an Nutzer:innen gesendet, die in den letzten 24 Stunden keine Sitzung aufgezeichnet oder eine Push-Nachricht erhalten haben.

### Konfiguration

Um das Uninstall-Tracking für Ihre iOS-Anwendung zu konfigurieren, verwenden Sie eine [Utility-Methode][iOS-Dokumentation]. Verwenden Sie für Ihre Android-Anwendung [`isUninstallTrackingPush()`][8]. Wenn Braze ein Uninstall feststellt, sei es durch Uninstall-Tracking oder durch die normale Zustellung von Push-Kampagnen, erfassen wir den besten geschätzten Zeitpunkt des Uninstall-Vorgangs beim Nutzer oder bei der Nutzerin. Diese Zeit wird im Nutzerprofil als Standardattribut gespeichert und kann zur Definition eines Segments von Nutzer:innen für Rückgewinnungskampagnen verwendet werden.

## Segmente nach Deinstallationen filtern

Der Filter **Uninstalled** auf der Seite **Segmente** wählt Nutzer:innen aus, die Ihre App innerhalb eines bestimmten Zeitraums deinstalliert haben. Da es schwierig ist, den genauen Zeitpunkt einer Deinstallation zu bestimmen, empfehlen wir, dass Deinstallationsfilter breitere Zeitspannen haben, um sicherzustellen, dass jeder, der deinstalliert, irgendwann in das Segment fällt.

![Segmentierung deinstallieren.][5]

### Analyse auf App-Ebene

Tägliche Statistiken über Deinstallationen finden Sie auf der **Startseite**. Das Diagramm kann nach App und Segmenten aufgeschlüsselt werden, ähnlich wie andere Statistiken, die Braze bereitstellt. Wählen Sie in der **Übersicht über die Performance** Ihren Datumsbereich und, falls gewünscht, eine App aus. Blättern Sie dann zum Diagramm **Performance im Zeitverlauf** und gehen Sie wie folgt vor:

1. Wählen Sie in der Dropdown-Liste **Statistik für** **Deinstallationen** aus.
2. In der Dropdown-Liste **Aufschlüsselung** wählen Sie **Nach Segmenten**.
3. Wählen Sie in der Dropdown-Liste **Aufschlüsselung Werte** die Segmente aus, die in das Diagramm aufgenommen werden sollen.

{% alert note %}
Apps ohne Enablement des Uninstall-Trackings melden Deinstallationen nur von einer Teilmenge ihrer Nutzer:innen (denjenigen, die mit Push-Benachrichtigungen Targeting betrieben haben), so dass die tägliche Gesamtzahl der Deinstallationen höher sein kann als die angezeigte.
{% endalert %}

![Grafikauswahl deinstallieren.][2]

## Uninstall-Tracking für Kampagnen 

Das Uninstall-Tracking für Kampagnen zeigt die Anzahl der Nutzer:innen, die eine bestimmte Kampagne erhalten und anschließend Ihre App innerhalb des ausgewählten Zeitraums deinstalliert haben. Dieses Tool gibt Insights darüber, wie Kampagnen unbeabsichtigtes negatives Nutzer:innen-Verhalten fördern können und hilft dabei, die Gesamtwirksamkeit von Kampagnen zu messen.

Die Deinstallationsstatistiken für Kampagnen befinden sich auf der Seite **Campaign Analytics** für eine bestimmte Kampagne. Bei Multichannel- und multivariaten Kampagnen können die Uninstall-Vorgänge nach Kanal bzw. Variante aufgeschlüsselt werden.

![Uninstall-Vorgang auf Kampagnen-Ebene.][6]

### Funktionsweise

Braze verfolgt Deinstallationen, indem es beobachtet, wenn Push-Nachrichten, die an die Geräte der Nutzer:innen gesendet werden, entweder vom Firebase Cloud Messaging (FCM) oder vom Apple Push Notification Service (APN) ein Signal zurückgeben, dass die App nicht mehr installiert ist. Wenn das globale Uninstall-Tracking für eine bestimmte App aktiviert ist, senden wir täglich eine stille Push-Nachricht an Nutzer:innen, um festzustellen, ob sie deinstalliert haben. Dieser "stille" Push wird an alle Nutzer:innen gesendet (es sei denn, der Nutzer hat stille Pushs in seinen App-Einstellungen deaktiviert); der Push wird den Nutzer:innen jedoch nicht angezeigt. Wenn wir feststellen, dass ein:e Nutzer:in einen Uninstall vorgenommen, führen wir folgende Aktionen aus:

* Erhöht die Anzahl der Deinstallationen der App um eins.
* Erhöhen der Anzahl der Uninstall-Vorgänge für jede Kampagne, die der oder die Nutzer:in in den letzten 24 Stunden erfolgreich erhalten hat, um eins.
* Wenn ein Nutzer:in einem Zeitraum von 24 Stunden drei Kampagnen erhält und diese dann deinstalliert, erhöhen wir die Anzahl der "Deinstallationen" für alle drei Kampagnen.

Das Uninstall-Tracking unterliegt den Beschränkungen, die FCM und APNs für diese Informationen festlegen. Braze erhöht die Anzahl der Deinstallationen nur, wenn FCM oder APNs uns mitteilen, dass ein Nutzer:innen deinstalliert hat. Diese Drittsysteme behalten sich jedoch das Recht vor, uns jederzeit über Deinstallationen zu informieren. Daher sollte das Uninstall-Tracking eher zur Erkennung von Tendenzen als zur Erstellung präziser Statistiken verwendet werden.

Weitere Informationen zur Verwendung des Uninstall-Trackings finden Sie in unserem Blogbeitrag [Uninstall-Tracking: Ein Blick auf die Stärken und Grenzen der Branche][7].

## Fehlerbehebung

### Warum wird die Anzahl der Deinstallationen plötzlich so hoch?

Wenn die Deinstallation von Apps sprunghaft ansteigt, kann das daran liegen, dass Firebase Cloud Messaging (FCM) und der Apple Push Notification Service (APNS) alte Token in unterschiedlicher Häufigkeit widerrufen.

### Warum unterscheidet sich die Anzahl der Deinstallationen von Apps von den Angaben in den APNs?

Der Unterschied ist zu erwarten. APNs werden für diese Token nach einem ungenauen Zeitplan den Status 410 zurückgeben.

[1]: {% image_buster /assets/img_archive/Uninstall_Tracking2.png %} „Uninstall-Tracking Kontrollkästchen“
[2]: {% image_buster /assets/img_archive/Uninstall_Tracking_App2.png %} „Grafikauswahl deinstallieren“
[4]: {% image_buster /assets/img_archive/User_Profile.png %} „Attribut deinstallieren“
[5]: {% image_buster /assets/img_archive/Uninstall_Segment.png %} "Segmentierung deinstallieren"
[6]: {% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %}
[7]: https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/
[iOS docs]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html
