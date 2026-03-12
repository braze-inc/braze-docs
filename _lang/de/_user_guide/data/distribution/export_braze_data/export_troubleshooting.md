---
nav_title: Fehlerbehebung beim Export
article_title: Fehlerbehebung beim Exportieren
page_order: 10
page_type: reference
description: "Dieser Referenzartikel behandelt häufige Szenarien der Fehlerbehebung für Exporte in CSV- und API-Workflows."
---

# Fehlerbehebung beim Export

> Diese Seite behandelt häufige Szenarien der Fehlerbehebung für Exporte in CSV- und API-Workflows.  

Bitte verwenden Sie die Tabs, um auszuwählen, ob Sie in den **Standard-S3-Bucket von Braze** oder zu einem **Cloud-Speicher-Partner** exportieren möchten.

{% sdktabs %}
{% sdktab Default export %}

Wenn Sie keinen Speicherpartner als Standard-Exportziel festgelegt haben, verwendet Braze seinen eigenen Amazon S3-Bucket, um Ihre Exportdateien zu speichern. Die Dateien in dieser Konfiguration sind temporär und verfallen nach vier Stunden.  

## CSV-Exporte  
Wenn Sie eine CSV-Datei aus dem Dashboard exportieren, sendet Braze einen Download-Link per E-Mail an die angemeldete Nutzer:in. Dieser Link verweist auf eine ZIP-Datei, die im S3-Bucket von Braze gehostet wird. Die ZIP-Datei enthält mehrere kleinere Dateien, die zusammen Ihren Export bilden.  

Sie müssen im Braze-Dashboard angemeldet sein, um den Link nutzen zu können, und die Datei ist nur vier Stunden lang verfügbar. Danach ist der Link nicht mehr funktionsfähig und die Daten werden gelöscht. Sollten bei sehr umfangreichen Exporten (über 500.000 Nutzer:innen) wiederholt Fehler auftreten, kann der Export fehlschlagen. In diesem Fall empfehlen wir, den Export in kleinere Gruppen oder Felder aufzuteilen oder die Einrichtung eines Partners in Betracht zu ziehen.  

### Häufige Fehler

- Sollten Sie einen`AccessDenied`Fehler feststellen, ist die Datei möglicherweise bereits abgelaufen oder Sie haben versucht, die Öffnung durchzuführen, bevor sie bereit war. Größere Berichte benötigen mehr Zeit für die Erstellung. Bitte warten Sie einige Minuten und versuchen Sie es erneut.  
- Ein`ExpiredToken`Fehler bedeutet, dass das vierstündige Zeitfenster abgelaufen ist. Führen Sie den Export erneut aus, um einen neuen Link zu generieren.  
- Die Nachricht `Looks like the file doesn't exist anymore`wird in der Regel angezeigt, wenn die E-Mail gesendet wird, die Datei jedoch noch nicht vollständig auf S3 hochgeladen wurde. In der Regel lässt sich das Problem durch einige Minuten Wartezeit beheben.  
- Apostrophe am Anfang bestimmter Felder (wie `-`, `=`,`+` oder `@`) werden erwartet. Beispielsweise`-1943`wird`'-1943`in der CSV-Datei zu. Braze tut dies, um zu verhindern, dass Tabellenkalkulationsprogramme die Daten falsch interpretieren. Dies gilt nicht für JSON-Exporte, die etwa vom [Endpunkt`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) zurückgegeben werden.  

## API-Exporte  
Wenn Sie über die Export-APIs ohne Cloud-Speicher exportieren, speichert Braze die Dateien in seinem S3-Bucket. Sie erhalten keine E-Mail. Stattdessen enthält die API-Antwort eine temporäre Download-URL. Der Export erfolgt als ZIP-Datei, die mehrere JSON-Dateien enthält, wobei jede Datei einen Nutzer:in pro Zeile enthält.  

Ähnlich wie CSV-Exporte verfallen auch Links aus der API nach vier Stunden. Wenn Sie zu früh einen Klick auf den Link durchführen, können Fehler auftreten, da die Datei noch nicht bereit ist. Sie können in Ihrer Anfrage`callback_endpoint` eine E-Mail-Adresse angeben, falls Sie von Braze benachrichtigt werden möchten, sobald die Datei verfügbar ist.  

Umfangreiche API-Exporte können ebenfalls zu Zeitüberschreitungen führen. Sollte dies der Fall sein, versuchen Sie bitte, kleinere Anfragen zu stellen oder einen Speicherpartner hinzuzuziehen, um das Volumen zu bewältigen.  

### Häufige Fehler  
- `AccessDenied` oder `ExpiredToken`bedeutet in der Regel, dass der Link abgelaufen oder noch nicht verfügbar war. Bitte führen Sie den Export erneut durch oder warten Sie etwas länger.  

{% endsdktab %}

{% sdktab Cloud storage connected %}

Wenn Sie einen Speicherpartner (wie Amazon S3, Google Cloud Storage oder Azure Blob) verbinden und ihn auf der **Technologie**-Partnerseite im Braze-Dashboard als Ihr Standard-Exportziel markieren, schreibt Braze Ihre Exporte direkt in Ihren Bucket. Diese Konfiguration ist in der Regel für umfangreichere Exporte zuverlässiger.  

## CSV-Exporte  
Bei CSV-Exporten sendet Ihnen Braze einen Download-Link per E-Mail zu. Dieser Link läuft nach einer kurzen Zeitspanne ab (in der Regel nach etwa vier Stunden). Wenn Sie einen Speicherpartner verbunden und als Standard-Exportziel festgelegt haben, liefert Braze auch eine Kopie des Exports an Ihren verbundenen Bucket. Diese Kopie wird in Ihrer eigenen Infrastruktur gespeichert, wobei Ablauf und Bindung Ihren Speicherrichtlinien entsprechen.  

Im Cloud-Speicher werden CSV-Exporte in einer CSV-Datei zusammengefasst. Die ZIP-Datei enthält mehrere kleinere CSV-Dateien. Umfangreiche Exporte werden häufig in Teile aufgeteilt (beispielsweise jeweils etwa 5.000 Nutzer:innen), wobei die Größe der Teile variieren kann. Kleinere Dateien bedeuten nicht, dass Daten fehlen. Sollte der per E-Mail versandte Link nicht funktionieren, die Kopie in Ihrem Speicher jedoch erfolgreich sein, können Sie Ihre Daten jederzeit direkt aus Ihrem Bucket abrufen.  

### Häufige Fehler

- `AccessDenied` bedeutet, dass Braze nicht in Ihren Bucket schreiben konnte. Bitte überprüfen Sie erneut, ob Ihre Zugangsdaten und Berechtigungen weiterhin gültig sind.  
- `ExpiredToken` wird angezeigt, wenn Braze den Zugriff auf Ihren Bucket verloren hat. Bitte aktualisieren Sie Ihre Zugangsdaten im Braze-Dashboard.  
- Sollten einige Dateien kleiner als erwartet erscheinen, ist dies ein normales Verhalten. Der Exportvorgang teilt Dateien aus Gründen der Stabilität absichtlich auf.  
- Apostrophe am Anfang bestimmter Felder (wie `-`, `=`,`+` oder `@`) werden erwartet. Beispielsweise`-1943`wird`'-1943`in der CSV-Datei zu. Braze tut dies, um zu verhindern, dass Tabellenkalkulationsprogramme die Daten falsch interpretieren. Dies gilt nicht für JSON-Exporte, die etwa vom [Endpunkt`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) zurückgegeben werden.  

## API-Exporte  
Wenn Sie Daten über die APIs mit einem verbundenen Speicherpartner exportieren, werden die Exportdateien in Ihren Bucket geschrieben. Es wird keine E-Mail versendet. Die zugrunde liegenden Objekte werden in Ihrem Speicher aufbewahrt und unterliegen Ihren Bindungseinstellungen, auch wenn die von Braze zurückgegebenen Download-URLs möglicherweise weiterhin zeitlich begrenzt sind. Jede ZIP-Datei enthält JSON-Objekte, eines pro Zeile. Umfangreiche Exporte können in mehrere ZIP-Dateien anstatt in eine einzige ZIP-Datei aufgeteilt werden, was diese Methode für umfangreiche Exporte im Allgemeinen zuverlässiger macht.  

### Häufige Fehler

- `AccessDenied` Dies tritt ein, wenn Braze nicht in Ihren Bucket schreiben kann oder die Objekte anschließend gelöscht wurden. Bitte überprüfen Sie die Berechtigungen und stellen Sie sicher, dass keine externen Programme Dateien löschen.  
- `ExpiredToken` bedeutet, dass die Zugangsdaten von Braze für Ihren Bucket veraltet sind. Bitte aktualisieren Sie diese im Dashboard.  
- Sollten Dateien fehlen oder kleiner als erwartet sein, überprüfen Sie bitte zunächst, ob Objekte außerhalb von Braze gelöscht werden. Es wird erwartet, dass die Dateigrößen kleiner ausfallen werden.  

{% endsdktab %}
{% endsdktabs %}