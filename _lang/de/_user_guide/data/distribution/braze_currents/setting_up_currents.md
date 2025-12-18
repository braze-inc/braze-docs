---
nav_title: Currents einrichten
article_title: Currents einrichten
page_order: 0
page_type: tutorial
description: "Diese Anleitung führt Sie durch die Integration und Konfiguration von Braze-Currents."
tool: Currents
search_rank: 8
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"} Einrichten von Currents

> Auf dieser Seite wird der allgemeine Prozess zur Integration und Konfiguration von Braze-Currents beschrieben.

{% alert important %}
Currents sind in bestimmten Braze-Paketen enthalten. Wenden Sie sich an Ihre Vertretung von Braze, wenn Sie Fragen haben oder Zugang erhalten möchten.
{% endalert %}

## Anforderungen

Die Verwendung von Currents mit einem unserer Partner erfordert dieselben grundlegenden Parameter und Verbindungsmethoden.

Jeder Partner benötigt die Erlaubnis von Braze, Daten zu schreiben und an ihn zu senden, und Braze fragt nach dem Standort, in den diese Dateien geschrieben werden sollen, insbesondere Bucket-Namen oder Schlüssel.

Die folgenden Anforderungen sind die grundlegenden, minimalen Anforderungen für die Integration mit den meisten unserer Partner. Einige Partner verlangen zusätzliche Parameter, die in der [Dokumentation]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) des jeweiligen [Partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) aufgeführt sind, zusammen mit allen Nuancen, die mit diesen Grundanforderungen verbunden sind.

| Anforderung | Herkunft | Zugang | Beschreibung
|---|---|---|---|
| Konto bei einem Partner | Vereinbaren Sie ein Konto mit diesem Partner oder wenden Sie sich an Ihren Braze-Konto Manager:in, um Vorschläge zu erhalten. | Besuchen Sie die Website des Partners oder wenden Sie sich an den Partner, um sich zu registrieren. | Braze sendet keine Daten an einen Partner, wenn Sie nicht über Ihr Unternehmenskonto Zugriff auf diese Daten haben.
| Partner API-Schlüssel oder Token | Normalerweise das Dashboard des Partners. | Kopieren Sie sie einfach und fügen Sie sie in das dafür vorgesehene Braze-Feld ein. | Braze hat dafür ein eigenes Feld auf der Integrationsseite für diesen Partner. Wir benötigen dies, um abzubilden, wohin wir Ihre Daten senden. **Es ist wichtig, dass Sie Ihre Partner-Schlüssel oder Token auf dem neuesten Stand halten. Ungültige Zugangsdaten können dazu führen, dass Ihr Konnektor deaktiviert wird und Ereignisse ausfallen.**
| Authentifizierungscode/-schlüssel, geheimer Schlüssel, Zertifizierungsdatei | Kontaktieren Sie eine Vertretung für Ihr Konto bei diesem Partner. Kann auch im Dashboard des Partners vorhanden sein. | Kopieren Sie die Schlüssel und fügen Sie sie in das vorgesehene Braze-Feld ein. Generieren Sie `.json` oder andere Zertifizierungsdateien und laden Sie sie an die entsprechende Stelle in Braze hoch. | Braze hat dafür ein eigenes Feld auf der Integrationsseite für diesen Partner. Damit erhalten Sie die Zugangsdaten für Braze und autorisieren uns, Dateien auf Ihr Partner-Konto zu schreiben. **Es ist wichtig, dass Sie Ihre Authentifizierungsdaten auf dem neuesten Stand halten. Ungültige Zugangsdaten können dazu führen, dass Ihr Konnektor deaktiviert wird und Events gelöscht werden.**
| Bucket, Ordnerpfad | Einige Partner organisieren und sortieren Daten nach Buckets. Dies sollte im Dashboard des Partners zu finden sein. | Wenn dies erforderlich ist, stellen Sie sicher, dass Sie den Bucket-Namen oder den Dateipfad genau in den vorgesehenen Bereich in Braze kopieren. Wir wollen nicht, dass Ihre Daten verloren gehen! | Obwohl dies für einige Partner erforderlich ist, ist es wichtig, es richtig zu machen, wenn Sie es brauchen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Es ist wichtig, dass Sie Ihre Partner-Schlüssel, Partner-Tokens und Authentifizierungsdaten auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Currents einrichten

### Schritt 1: Wählen Sie Ihren Partner

Braze-Currents erlaubt Ihnen die Integration durch Datenspeicherung unter Verwendung von Flat Files oder zu unseren Partnern für Verhaltensanalysen und Kundendaten unter Verwendung von gebündelten JSON-Payloads zu einem bestimmten Endpunkt.  

Bevor Sie mit der Integration beginnen, sollten Sie entscheiden, welche Integration für Ihre Zwecke am besten geeignet ist. Wenn Sie beispielsweise bereits mParticle und Segmente verwenden und Daten zu Braze streamen möchten, wäre es am besten, eine gebündelte JSON-Nutzlast zu verwenden. Wenn Sie die Daten lieber selbst manipulieren möchten oder ein komplexeres System zur Datenanalyse haben, ist es vielleicht am besten, die Datenspeicherung zu verwenden[(Braze verwendet diese Methode]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!)

### Schritt 2: Offene Currents

Gehen Sie zu **Partnerintegrationen** > **Datenexport**, um zu beginnen. Sie gelangen auf die Seite zur Verwaltung der Currents-Integration.

![Currents-Seite im Braze-Dashboard]({% image_buster /assets/img_archive/currents-main-page.png %})

### Schritt 3: Ihren Partner hinzufügen

Fügen Sie einen Partner hinzu, der manchmal auch als „Currents-Konnektor“ bezeichnet wird, indem Sie das Dropdown-Menü oben auf dem Bildschirm auswählen.

Für jeden Partner sind andere Konfigurationsschritte erforderlich. Um die einzelnen Integrationen zu aktivieren, sehen Sie sich unsere Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) an und folgen Sie den Anweisungen auf den jeweiligen Seiten.

### Schritt 4: Events konfigurieren

Wählen Sie die Ereignisse, die Sie an diesen Partner weitergeben möchten, indem Sie eine der verfügbaren Optionen ankreuzen. Eine Auflistung dieser Events finden Sie in unseren Bibliotheken [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) und [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Bei Bedarf erfahren Sie mehr über unsere Events in unserem Artikel [Semantik der Zustellung von Events]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Schritt 5: Feldtransformationen einrichten

Sie können Transformationen des Feldes „Currents“ verwenden, um ein Zeichenfolgenfeld zu entfernen oder mit einem Hash zu versehen.

- **Entfernen:** Ersetzt das String-Feld durch `[REDACTED]`. Dies ist hilfreich, wenn Ihr Partner Ereignisse mit fehlenden oder leeren Feldern ablehnt.
- **Hash:** Wendet einen SHA-256-Hashing-Algorithmus auf das String-Feld an.

Wenn Sie ein Feld für eine dieser Transformationen auswählen, wird diese Transformation auf alle Ereignisse angewendet, in denen dieses Feld vorkommt. Wenn Sie zum Beispiel `email_address` für die Hash-Funktion auswählen, wird das Feld `email_address` in den Ereignissen E-Mail-Versand, E-Mail-Öffnung, E-Mail-Bounce und Statusänderung der Abo-Gruppe gehasht.

![Hinzufügen von Feldtransformationen]({% image_buster /assets/img/current3.png %})

### Schritt 6: Testen Sie Ihre Integration

{% alert important %}
Currents verwirft Events mit übermäßig großen Nutzdaten von mehr als 900 KB.
{% endalert %}

Bevor Sie testen, sollten Sie sich unsere [Currents-Beispieldaten auf GitHub](https://github.com/Appboy/currents-examples) ansehen. Wenn Sie zum Testen bereit sind, wählen Sie unten eine Option aus:

#### Versenden von Test-Ereignissen

Um Ihre Integration zu testen, können Sie **Test-Ereignisse** auswählen, um je ein Ereignis aus jedem der von Ihnen ausgewählten Ereignistypen an diesen Current zu senden. Ausführliche Informationen zu den einzelnen Ereignistypen finden Sie in unseren Bibliotheken [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) und [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

![Die Seite "Currents Test" auf dem Braze-Dashboard.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Testen von Currents-Konnektoren

Die Test-Currents-Konnektoren sind kostenlose Versionen unserer bestehenden Konnektoren, die zum Testen und Ausprobieren verschiedener Ziele verwendet werden können. Test-Currents haben:

- Keine Begrenzung der Anzahl der Test-Currents-Konnektoren, die Sie erstellen können.
- insgesamt maximal 10.000 Events pro gleitendem Zeitraum von sieben Tagen. Diese Ereignissumme wird stündlich auf dem Dashboard aktualisiert.

Wenn Ihre Test-Currents Konnektoren das Sende-Limit erreicht haben, sendet Ihr Konnektor bis zum nächsten Sieben-Tage-Zeitraum keine Events mehr.

Um Ihren Currents-Konnektor zu upgraden, bearbeiten Sie die Integration im Dashboard und wählen Sie **Test-Integration upgraden**.

## Currents aktualisieren

{% multi_lang_include updating_currents.md %}

## IP-Allowlisting

Braze sendet Currents-Daten von den aufgeführten IPs:

{% multi_lang_include data_centers.md datacenters='ips' %}
