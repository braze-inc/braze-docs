---
nav_title: Selbstverwaltete benutzerdefinierte Domains
article_title: Selbstverwaltete benutzerdefinierte Domains
page_order: 0
description: "Auf dieser Seite erfahren Sie, wie Sie angepasste Domains mit Linkverkürzung verwenden, um das Aussehen Ihrer verkürzten URLs zu personalisieren."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Selbstverwaltete benutzerdefinierte Domains

> Auf dieser Seite wird erläutert, wie Sie Ihre eigenen angepassten Domains im Braze-Dashboard einrichten können. Mit benutzerdefinierten Domains können Sie einen markenspezifischen Kurzlink verwenden, der die Identität Ihrer Marke widerspiegelt, anstatt einen generischen Kurzlink oder die Braze-Domain (`brz.ai`) zu verwenden. Dies erhöht das Vertrauen der Nutzer:innen und verbessert das Engagement mit SMS-Links.

Mit Self-Service-Benutzerdefinierten Domänen können Sie Ihre eigenen benutzerdefinierten Domains für SMS, RCS und WhatsApp direkt über Ihr Braze-Dashboard konfigurieren und verwalten. Sie können problemlos bis zu 10 benutzerdefinierte Domains an einem Ort hinzufügen, überwachen und verwalten.

## Vorteile von angepassten Domains im Selbstbedienungsmodus

- **Optimierte Einrichtung:** Konfigurieren Sie Ihre Domains auf der Seite **„Unternehmenseinstellungen“**, um die Einrichtungszeit zu verkürzen.
- **Verbesserte Transparenz:** Erhalten Sie über Banner im Dashboard Realtime-Updates zum Einrichtungsstatus Ihrer Domain.
- **Proaktive Benachrichtigungen:** Erhalten Sie umgehend Benachrichtigungen, wenn Ihre benutzerdefinierte Domain verbunden ist oder wenn Konfigurationsfehler auftreten.

## Domain-Anforderungen

- Die Domains müssen Ihnen gehören und von Ihnen verwaltet werden. Dies kann über einen Domain-Registrar wie GoDaddy, Amazon Route 53 oder Google Domains erfolgen.
- Die für dieses Feature verwendete Domain muss lauten:
  - Eindeutig (unterscheidet sich von Ihrer Website-Domain)
  - Kann nicht zum Hosten von Internet-Inhalten verwendet werden.
    - Sie können auch eindeutige Subdomains verwenden. Beispielsweise könnten die `braze.com`Domains Subdomains von`sms.braze.com`oder haben`whatsapp.braze.com`.

## Angepasste Domains delegieren

Wir bitten Sie, Ihre angepasste Domain an Braze zu delegieren, damit wir eine ordnungsgemäße Weiterleitung und Infrastrukturkompatibilität mit unseren Linkverkürzungs- und Tracking-Diensten gewährleisten können. Wenn Sie Ihre Domain an Braze delegieren, kümmern wir uns automatisch um die Erneuerung des Zertifikats, um eine Unterbrechung des Dienstes zu verhindern. 

## Hinzufügen einer benutzerdefinierten Domain

1. Bitte navigieren Sie in Braze zu **„Unternehmenseinstellungen“** > **„SMS/RCS und Messaging-Apps-Domains**“.
![Seite „SMS/RCS und Messaging-Apps-Domains“ mit einer Auflistung mehrerer Domains.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Bitte wählen Sie **„Domain hinzufügen“,** um mit der Einrichtung einer neuen benutzerdefinierten Domain zu beginnen.
3\. Bitte geben Sie die von Ihnen erworbene benutzerdefinierte Domain in unser In-App-Eingabefeld ein, das unsere bestehende Validierungslogik für die korrekte Formatierung verwendet, und wählen Sie anschließend **„Weiter“** und **„Senden**“.

![Button „Domain hinzufügen“ auf der Seite „SMS/RCS- und Messaging-Apps-Domains“.]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Bitte beauftragen Sie Ihr technisches Team (z. B. Entwicklerteam oder IT-Mitarbeiter) damit, Ihre DNS-Konfiguration mit den angezeigten Cloudflare-DNS-Eintragsdaten zu aktualisieren. Ihr technisches Team muss Ihre DNS-Einträge innerhalb von 45 Tagen mit diesen Angaben aktualisieren.
  - Sollten Sie zusätzliche Zeit für das Update Ihrer DNS-Einträge benötigen, können Sie den Vorgang erneut starten und einen neuen Satz DNS-Einträge für Ihre Domain generieren.

Braze überprüft Ihre DNS-Konfiguration etwa alle 30 Minuten auf Updates.

![Abschnitt „DNS-Eintrag“ mit drei Schritten, die Sie ausführen müssen, um die Einrichtung Ihrer Domain abzuschließen.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
Ihre Domain-Fortschritte werden automatisch gespeichert. Sollten Sie den Vorgang vorzeitig beenden müssen, können Sie später fortfahren, indem Sie den ausstehenden Domain-Eintrag auf der Seite **„SMS/RCS- und Messaging-Apps-Domains“** auswählen.
{% endalert %}

### Laufende Verwaltung und Nutzung

Sobald Ihre Domain überprüft wurde, werden Ihre benutzerdefinierten Domains in der Tabelle auf der Seite **„SMS/RCS- und Messaging-Apps-Domains“** mit Statusindikatoren angezeigt. Sie können verbundene Domains sofort über mehrere Abo-Gruppen, Workspaces sowie über SMS-, RCS- und WhatsApp-Kanäle hinweg verwenden.

![Liste der benutzerdefinierten Domains und Status.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

Die Live-Überwachung benachrichtigt Sie im Braze-Dashboard, wenn bei einer Ihrer aktiven Domains ein Problem auftritt, sodass Ihre benutzerdefinierten Links weiterhin nutzbar bleiben. Sollten Sie auf Probleme stoßen, referenzieren Sie bitte die Fehlerdetails in der App oder wenden Sie sich an [den]({{site.baseurl}}/braze_support/) Braze[-Support,]({{site.baseurl}}/braze_support/) um Unterstützung zu erhalten.

## Zuweisung benutzerdefinierter Domänen zu Abo-Gruppen

Nach der Konfiguration können angepasste Domains einer oder mehreren SMS-, RCS- und WhatsApp-Abo-Gruppen zugewiesen werden.

1. Bitte gehen Sie zu **„Zielgruppe“** > **„Verwaltung der Abo-Gruppen**“.
2. Bitte suchen Sie Ihre Abo-Gruppe in der Liste und wählen Sie sie aus.
3. Wählen Sie unter **„Abo-Gruppe“** Ihre angepasste Domain als „Linkverkürzungsdomain“ aus.

![Abogruppeneinstellungen ermöglichen die Auswahl einer Link-Shorting-Domain.]({% image_buster /assets/img/custom_domain.png %})

Kampagnen, die mit aktivierter Linkverkürzung versendet werden, verwenden die zugewiesene Domain, die mit Ihrer SMS-, RCS- oder WhatsApp-Abo-Gruppe verknüpft ist.

![Vorschau des SMS-Editors mit einer verkürzten Link-Domain, die sich von der Domain im Feld "Nachricht" unterscheidet.]({% image_buster /assets/img/custom_domain2.png %})

## Häufig gestellte Fragen

### Können delegierte Domains von mehreren Abo-Gruppen gemeinsam genutzt werden?

Ja Eine einzelne Domain kann mit mehreren Abo-Gruppen verwendet werden. Wählen Sie dazu für jede Abo-Gruppe die Domain aus, mit der sie verknüpft werden soll.

### Können delegierte Domains von mehreren Workspaces gemeinsam genutzt werden?

Ja Domains können mit Abo-Gruppen in mehreren Workspaces verknüpft werden, sofern diese zu demselben Unternehmen gehören.

### Wie viele angepasste Domains kann ich hinzufügen?

Sie können bis zu 10 angepasste Domains pro Dashboard hinzufügen.

### Was geschieht, wenn ich meine DNS-Einträge nicht innerhalb von 45 Tagen aktualisiere?

Obwohl Ihre Cloudflare-DNS-Eintragsdaten nach 45 Tagen ablaufen, können Sie den Einrichtungsprozess mit derselben Domain erneut starten. Braze generiert dann eine Reihe neuer DNS-Einträge, um Ihr Einrichtungsfenster zu verlängern.

### Werde ich benachrichtigt, wenn während des DNS-Updates ein Fehler auftritt?

Ja Sollte ein Fehler auftreten, wird im Braze-Dashboard ein Banner angezeigt, das das Problem detailliert beschreibt und Schritte zu dessen Behebung enthält. 

### Ist es möglich, eine angepasste Domain über mehrere Kanäle hinweg zu verwenden?

Ja Nachdem eine angepasste Domain überprüft wurde, kann sie in allen SMS-, RCS- und WhatsApp-Abo-Gruppen in allen Workspaces innerhalb eines Dashboards verwendet werden. 

### Was kann ich tun, wenn ich Fragen habe oder weitere Unterstützung benötige?

Für detailliertere Anleitungen zum Einrichten und Verwalten benutzerdefinierter Domains, einschließlich Schritten zur Fehlerbehebung und technischen Anforderungen, [wenden Sie sich bitte an den Support]({{site.baseurl}}/braze_support/).
