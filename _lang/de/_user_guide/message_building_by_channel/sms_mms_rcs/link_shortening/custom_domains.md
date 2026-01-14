---
nav_title: Angepasste Domains zur Selbstbedienung
article_title: Angepasste Domains zur Selbstbedienung
page_order: 0
description: "Auf dieser Seite erfahren Sie, wie Sie angepasste Domains mit Linkverkürzung verwenden, um das Aussehen Ihrer verkürzten URLs zu personalisieren."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Angepasste Domains zur Selbstbedienung

> Auf dieser Seite erfahren Sie, wie Sie Ihre eigenen angepassten Domains im Braze-Dashboard einrichten können. Mit angepassten Domains können Sie anstelle eines generischen verkürzten Links oder der Braze-Domain (`brz.ai`) einen markenspezifischen verkürzten Link verwenden, der die Identität Ihrer Marke widerspiegelt - und damit das Vertrauen der Nutzer:innen und das Engagement der Kampagnen mit SMS-Links verbessert.

Mit angepassten Domains zur Selbstbedienung können Sie Ihre eigenen angepassten Domains für SMS, RCS und WhatsApp konfigurieren und verwalten - direkt von Ihrem Braze-Dashboard aus. Sie können ganz einfach bis zu 10 angepasste Domains an einem Ort hinzufügen, überwachen und verwalten.

## Vorteile von angepassten Domains im Selbstbedienungsbereich

- **Rationalisierte Einrichtung:** Konfigurieren Sie Ihre Domains auf der Seite **Unternehmenseinstellungen**, um die Einrichtungszeit zu verkürzen.
- **Verbesserte Transparenz:** Erhalten Sie über Banner im Dashboard Realtime-Updates zum Status der Einrichtung Ihrer Domain.
- **Proaktive Benachrichtigungen:** Lassen Sie sich sofort benachrichtigen, wenn Ihre angepasste Domain verbunden ist oder wenn Konfigurationsfehler auftreten.

## Domain-Anforderungen

- Die Domains müssen Ihnen gehören und von Ihnen verwaltet werden. Dies kann über einen Domain-Registrar wie GoDaddy, Amazon Route 53 oder Google Domains erfolgen.
- Die Domain, die für dieses Feature verwendet wird, muss sein:
  - Eindeutig (anders als die Domain Ihrer Website)
  - Kann nicht zum Hosten von Webinhalten verwendet werden
    - Sie können auch eindeutige Subdomains verwenden. Die Domain `braze.com` könnte zum Beispiel die Subdomains `sms.braze.com` oder `whatsapp.braze.com` haben.

## Angepasste Domains delegieren

Wir verlangen von Ihnen, dass Sie Ihre angepasste Domain an Braze delegieren, damit wir das richtige Routing und die Kompatibilität der Infrastruktur mit unseren Diensten für Linkverkürzung und Click Tracking gewährleisten können. Wenn Sie Ihre Domain an Braze delegieren, kümmern wir uns automatisch um die Erneuerung des Zertifikats, um eine Unterbrechung des Dienstes zu verhindern. 

## Hinzufügen einer angepassten Domain

1. Gehen Sie in Braze zu **Unternehmenseinstellungen** > **SMS/RCS und Messaging Apps Domains**.
!["SMS/RCS und Messaging Apps Domains" Seite mit mehreren Domains aufgelistet.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Wählen Sie **Domain hinzufügen**, um eine neue angepasste Domain einzurichten.
3\. Geben Sie die angepasste Domain, die Sie erworben haben, in unsere In-App-Eingabe ein, die unsere bestehende Validierungslogik für die korrekte Formatierung verwendet, und wählen Sie dann **Weiter** und **Absenden**.

!["Domain hinzufügen" Button auf der Seite "SMS/RCS und Messaging Apps Domains".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Lassen Sie Ihr technisches Team (z.B. das Entwicklerteam oder die IT-Abteilung) Ihre DNS-Konfiguration mit den angezeigten Details des Cloudflare DNS-Eintrags aktualisieren. Ihr technisches Team muss Ihre DNS-Einträge innerhalb von 45 Tagen mit diesen Angaben aktualisieren.
  - Wenn Sie mehr Zeit für das Update Ihrer DNS-Einträge benötigen, können Sie den Prozess neu starten und einen neuen Satz DNS-Einträge für Ihre Domain erstellen.

Braze fragt Ihre DNS-Konfiguration etwa alle 30 Minuten ab, um nach Updates zu suchen.

!["DNS-Eintrag" mit 3 Schritten, die Sie ausführen müssen, um die Einrichtung Ihrer Domain abzuschließen.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
Der Fortschritt Ihrer Domains wird automatisch gespeichert. Wenn Sie den Vorgang abbrechen müssen, können Sie ihn später wieder aufnehmen, indem Sie auf der Seite **Domains für SMS/RCS- und Messaging-Apps** den Eintrag für die ausstehende Domain auswählen.
{% endalert %}

### Laufende Verwaltung und Nutzung

Nachdem Ihre Domain überprüft wurde, erscheinen Ihre angepassten Domains in der Tabelle auf der Seite **SMS/RCS und Messaging Apps Domains** mit Statusanzeigen. Sie können verbundene Domains sofort über mehrere Abo-Gruppen, Workspaces und über SMS-, RCS- und WhatsApp-Kanäle hinweg nutzen.

![Liste der angepassten Domains und Status.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

Die Live-Überwachung alarmiert Sie im Braze-Dashboard, wenn auf einer Ihrer aktiven Domains ein Problem auftritt, so dass Ihre angepassten Links nutzbar bleiben. Wenn Sie Probleme haben, sehen Sie sich die Fehlerdetails in der App an oder wenden Sie sich an den Braze [Support]({{site.baseurl}}/braze_support/), um Hilfe zu erhalten.

## Angepasste Domains verwenden

Nach der Konfiguration können angepasste Domains einer oder mehreren SMS-, RCS- und WhatsApp Abo-Gruppen zugewiesen werden.

![Abo-Gruppen Einstellungen, die es Ihnen erlauben, eine Link-Shortening Domain auszuwählen.]({% image_buster /assets/img/custom_domain.png %})

Kampagnen, die mit aktivierter Linkverkürzung versendet werden, verwenden die zugewiesene Domain, die mit Ihrer SMS-, RCS- oder WhatsApp Abo-Gruppe verbunden ist.

![SMS Nachrichten-Editor Vorschau mit einer verkürzten Link Domain, die sich von der Domain im Feld "Nachricht" unterscheidet.]({% image_buster /assets/img/custom_domain2.png %})

## Häufig gestellte Fragen

### Können delegierte Domains von mehreren Abo-Gruppen gemeinsam genutzt werden?

Ja Eine einzelne Domain kann mit mehreren Abo-Gruppen verwendet werden. Wählen Sie dazu für jede Abo-Gruppe die Domain aus, mit der sie verknüpft werden soll.

### Können delegierte Domains von mehreren Workspaces gemeinsam genutzt werden?

Ja Domains können mit Abo-Gruppen in mehreren Workspaces verknüpft werden, sofern diese zu demselben Unternehmen gehören.

### Wie viele angepasste Domains kann ich hinzufügen?

Sie können bis zu 10 angepasste Domains pro Dashboard hinzufügen.

### Was passiert, wenn ich meine DNS-Einträge nicht innerhalb von 45 Tagen aktualisiere?

Obwohl Ihre Cloudflare DNS-Datensätze nach 45 Tagen ablaufen, können Sie den Einrichtungsprozess mit derselben Domain neu starten und Braze wird eine Reihe neuer DNS-Datensätze generieren, um Ihr Einrichtungsfenster zu verlängern.

### Werde ich benachrichtigt, wenn während des DNS-Updates ein Fehler auftritt?

Ja Wenn ein Fehler auftritt, erhalten Sie im Braze-Dashboard einen Hinweis auf das Problem und die Schritte zu seiner Behebung. 

### Kann ich eine angepasste Domain für mehrere Kanäle verwenden?

Ja Nachdem eine angepasste Domain überprüft wurde, kann sie in allen SMS-, RCS- und WhatsApp-Abo-Gruppen in allen Workspaces innerhalb eines Dashboards verwendet werden. 

### Was ist, wenn ich Fragen habe oder weitere Unterstützung benötige?

Ausführlichere Anleitungen zur Einrichtung und Verwaltung angepasster Domains, einschließlich Fehlerbehebung und technischer Anforderungen, erhalten [Sie vom Support]({{site.baseurl}}/braze_support/).