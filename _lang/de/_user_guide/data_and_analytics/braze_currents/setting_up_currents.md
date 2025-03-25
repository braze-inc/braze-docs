---
nav_title: Currents einrichten
article_title: Currents einrichten
page_order: 0
page_type: tutorial
description: "Diese Anleitung führt Sie durch die Integration und Konfiguration von Braze-Currents."
tool: Currents
search_rank: 8
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currents einrichten

> Auf dieser Seite wird der allgemeine Prozess zur Integration und Konfiguration von Braze-Currents beschrieben.

{% alert important %}
Currents sind in bestimmten Braze-Paketen enthalten. Wenden Sie sich an Ihre Vertretung von Braze, wenn Sie Fragen haben oder Zugang erhalten möchten.
{% endalert %}

## Anforderungen

Die Verwendung von Currents mit einem unserer Partner erfordert dieselben grundlegenden Parameter und Verbindungsmethoden.

Jeder Partner benötigt die Erlaubnis von Braze, Daten zu schreiben und an ihn zu senden, und Braze fragt nach dem Standort, in den diese Dateien geschrieben werden sollen, insbesondere Bucket-Namen oder Schlüssel.

Die folgenden Anforderungen sind die grundlegenden, minimalen Anforderungen für die Integration mit den meisten unserer Partner. Einige Partner verlangen zusätzliche Parameter, die in der [Dokumentation des jeweiligen Partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) aufgeführt sind, zusammen mit allen Nuancen, die mit diesen Grundanforderungen verbunden sind.

| Anforderung | Herkunft | Zugang | Beschreibung
|---|---|---|---|
| Konto bei einem Partner | Vereinbaren Sie ein Konto mit diesem Partner oder wenden Sie sich an Ihren Braze-Konto Manager:in, um Vorschläge zu erhalten. | Besuchen Sie die Website des Partners oder wenden Sie sich an den Partner, um sich zu registrieren. | Braze sendet keine Daten an einen Partner, wenn Sie nicht über Ihr Unternehmenskonto Zugriff auf diese Daten haben.
| Partner API-Schlüssel oder Token | Normalerweise das Dashboard des Partners. | Kopieren Sie sie einfach und fügen Sie sie in das dafür vorgesehene Braze-Feld ein. | Braze hat dafür ein eigenes Feld auf der Integrationsseite für diesen Partner. Wir benötigen dies, um abzubilden, wohin wir Ihre Daten senden. **Es ist wichtig, dass Sie Ihre Partner-Schlüssel oder Token auf dem neuesten Stand halten. Ungültige Zugangsdaten können dazu führen, dass Ihr Konnektor deaktiviert wird und Events ausfallen.**
| Authentifizierungscode/-schlüssel, geheimer Schlüssel, Zertifizierungsdatei | Kontaktieren Sie eine Vertretung für Ihr Konto bei diesem Partner. Kann auch im Dashboard des Partners vorhanden sein. | Kopieren Sie die Schlüssel und fügen Sie sie in das vorgesehene Braze-Feld ein. Generieren Sie `.json` oder andere Zertifizierungsdateien und laden Sie sie an die entsprechende Stelle in Braze hoch. | Braze hat dafür ein eigenes Feld auf der Integrationsseite für diesen Partner. Damit erhalten Sie die Zugangsdaten für Braze und autorisieren uns, Dateien auf Ihr Partner-Konto zu schreiben. **Es ist wichtig, dass Sie Ihre Authentifizierungsdaten auf dem neuesten Stand halten. Ungültige Zugangsdaten können dazu führen, dass Ihr Konnektor deaktiviert wird und Events gelöscht werden.**
| Bucket, Ordnerpfad | Einige Partner organisieren und sortieren Daten nach Buckets. Dies sollte im Dashboard des Partners zu finden sein. | Wenn dies erforderlich ist, stellen Sie sicher, dass Sie den Bucket-Namen oder den Dateipfad genau in den vorgesehenen Bereich in Braze kopieren. Wir wollen nicht, dass Ihre Daten verloren gehen! | Obwohl dies für einige Partner erforderlich ist, ist es wichtig, es richtig zu machen, wenn Sie es brauchen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Es ist wichtig, dass Sie Ihre Partner-Schlüssel, Partner-Tokens und Authentifizierungsdaten auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Currents einrichten

### Schritt 1: Wählen Sie Ihren Partner

Braze-Currents erlaubt Ihnen die Integration durch Datenspeicherung unter Verwendung von Flat Files oder zu unseren Partnern für Verhaltensanalysen und Kundendaten unter Verwendung von gebündelten JSON-Payloads zu einem bestimmten Endpunkt.  

Bevor Sie mit der Integration beginnen, sollten Sie entscheiden, welche Integration für Ihre Zwecke am besten geeignet ist. Wenn Sie beispielsweise bereits mParticle und Segmente verwenden und Daten zu Braze streamen möchten, wäre es am besten, eine gebündelte JSON-Nutzlast zu verwenden. Wenn Sie die Daten lieber selbst manipulieren möchten oder ein komplexeres System zur Datenanalyse haben, ist es vielleicht am besten, die Datenspeicherung zu verwenden[(Braze verwendet diese Methode]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!)

### Schritt 2: Offene Currents

Gehen Sie zu **Partnerintegrationen** > **Datenexport**, um zu beginnen. Sie gelangen auf die Seite zur Verwaltung der Currents-Integration.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Integrationen** > Currents.
{% endalert %}

![Currents-Seite im Braze-Dashboard]({% image_buster /assets/img_archive/currents-main-page.png %})

### Schritt 3: Ihren Partner hinzufügen

Fügen Sie einen Partner hinzu, der manchmal auch als „Currents-Konnektor“ bezeichnet wird, indem Sie das Dropdown-Menü oben auf dem Bildschirm auswählen.

Für jeden Partner sind andere Konfigurationsschritte erforderlich. Um die einzelnen Integrationen zu aktivieren, sehen Sie sich unsere Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) an und folgen Sie den Anweisungen auf den jeweiligen Seiten.

### Schritt 4: Events konfigurieren

Wählen Sie die Events, die Sie an diesen Partner weitergeben möchten, indem Sie eine der verfügbaren Optionen ankreuzen. Eine Auflistung dieser Events finden Sie in unseren Bibliotheken [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) und [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Bei Bedarf erfahren Sie mehr über unsere Events in unserem Artikel [Semantik der Zustellung von Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/).

### Schritt 5: Feldtransformationen einrichten

Sie können Transformationen des Feldes „Currents“ verwenden, um ein Zeichenfolgenfeld zu entfernen oder mit einem Hash zu versehen.

- **Entfernen:** Ersetzt das String-Feld durch `[REDACTED]`. Dies ist hilfreich, wenn Ihr Partner Ereignisse mit fehlenden oder leeren Feldern ablehnt.
- **Hash:** Wendet einen SHA-256-Hashing-Algorithmus auf das String-Feld an.

Wenn Sie ein Feld für eine dieser Transformationen auswählen, wird diese Transformation auf alle Ereignisse angewendet, in denen dieses Feld vorkommt. Wenn Sie zum Beispiel `email_address` für die Hash-Funktion auswählen, wird das Feld `email_address` in den Ereignissen E-Mail-Versand, E-Mail-Öffnung, E-Mail-Bounce und Statusänderung der Abo-Gruppe gehasht.

![Hinzufügen von Feldtransformationen]({% image_buster /assets/img/current3.png %})

### Schritt 6: Testen Sie Ihre Integration

Sie können Ihre Integration testen oder sich die Beispieldaten von Currents in unserem [GitHub-Repository](https://github.com/Appboy/currents-examples) für Currents-Beispiele ansehen.

{% alert important %}
Currents verwirft Events mit übermäßig großen Nutzdaten von mehr als 900 KB.
{% endalert %}

#### Testen von Currents-Konnektoren

Die Test-Currents-Konnektoren sind kostenlose Versionen unserer bestehenden Konnektoren, die zum Testen und Ausprobieren verschiedener Ziele verwendet werden können. Test-Currents haben:

- Keine Begrenzung der Anzahl der Test-Currents-Konnektoren, die Sie erstellen können.
- insgesamt maximal 10.000 Events pro gleitendem Zeitraum von sieben Tagen. Diese Gesamtzahl der Events wird stündlich auf dem Dashboard aktualisiert.

Wenn Ihre Test-Currents Konnektoren das Sende-Limit erreicht haben, sendet Ihr Konnektor bis zum nächsten Sieben-Tage-Zeitraum keine Events mehr.

Um Ihren Test Currents-Konnektor zu upgraden, bearbeiten Sie die Integration im Dashboard und wählen Sie **Upgrade**.

## Aktualisieren von Currents

{% multi_lang_include updating_currents.md %}

## IP-Allowlisting

Braze sendet Currents-Daten von den aufgeführten IPs.

| Für die Instanzen `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` und `US-07`: |
|---|
| `127.0.0.1`
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| Für die Instanzen `EU-01` und `EU-02`: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88` 

| Zur Instanz `US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`
