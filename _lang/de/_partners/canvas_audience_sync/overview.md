---
nav_title: Über Audience Sync
article_title: Über Audience Sync
alias: /partners/about_audience_sync/
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
page_order: 0
Tool:
  - Canvas

---

# Über Audience Sync

> Mit dem Braze Audience Sync Feature können Sie die Reichweite Ihrer Kampagnen auf viele der wichtigsten sozialen und Werbetechnologien ausweiten. Mit [Braze-Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) können Marken dynamisch und sicher First-Party-Daten von Nutzern:innen mit dem Werbe-Ökosystem synchronisieren, um Marketing und Betrieb effizienter zu gestalten.

## Verfügbarkeit von Features

Alle Kund:innen von Braze haben ab sofort Zugriff auf Audience Sync mit Google und Facebook. Um zusätzliche Zielgruppen wie TikTok, Pinterest, Snapchat oder Criteo freizuschalten, müssen Sie Audience Sync Pro erwerben. Kontaktieren Sie Ihren Braze-Konto Manager:in für weitere Informationen.

## Anwendungsfälle

- Targeting hochwertiger Nutzer:innen über Owned Channels und bezahlte Kanäle, um zusätzliche Käufe oder Engagement zu fördern.
- Erstellen von Zielgruppen, die Ihren hochwertigen Nutzer:innen ähneln, um die Akquisitionskosten für neue Nutzer:innen und Konversionen zu optimieren.
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind, mit Anzeigen.
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten.

## Übersicht

<style>
table td {
    word-break: break-word;
}
</style>

| Ziel | Zeit für Ziele, die zur Zielgruppe passen | Rate-Limit | Ähnlich aussehen oder ähnlich handeln | Tipps |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | Bis zu 24 Stunden | 250.000 Anfragen pro Minute. Alle 5 Sekunden mit automatischer Wiederholung basierend auf dem Google-Feedback. | Ja | {::nomarkdown}<ul><li>Criteo unterstützt bis zu 1.000 Zielgruppen.</li><li>Die Mindestgröße der Zielgruppe liegt bei 500, die Empfehlung bei über 20.000.</li></ul>{:/} |
| [Facebook oder Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | Bis zu 24 Stunden | 190.000 Anzeigenkonten pro Stunde | Ja | {::nomarkdown}<ul><li>Facebook unterstützt bis zu 500 Zielgruppen.</li><li>Facebook verlangt Zielgruppen von mindestens 1.000 Nutzer:innen.</li></ul>{:/} |
| [Google Ads oder YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | Zwischen 6 und 12 Stunden | Batching alle 5 Sekunden mit automatischer Wiederholung basierend auf Google Feedback | Kein:e | {::nomarkdown}<ul><li><b>Kund:in passen sich an:</b> Verwenden Sie entweder eine Handy-Anzeige, eine E-Mail Adresse oder eine Telefonnummer.</li><li>Google Audiences benötigen mindestens 5.000 Nutzer:innen, um mit dem Adserving zu beginnen.</li><li>Die Zielgruppengröße wird als Null angezeigt, bis es mindestens 1.000 Nutzer:innen gibt.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 Stunden | LinkedIn verarbeitet 10 Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Braze fasst Nutzer:innen alle 5 Sekunden zusammen. | KI Prognosen für Zielgruppen | {::nomarkdown}<ul><li>Die Zielgruppe muss mindestens 300 Mitglieder umfassen, wobei das Standort-Targeting berücksichtigt wird.</li><li>LinkedIn zeigt die Übereinstimmung mit der Rate im Braze-Dashboard an.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | Zwischen 24 und 48 Stunden | Pinterest verarbeitet 7 Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Braze fasst Nutzer:innen alle 5 Sekunden zusammen. | Ja | Für die Zielgruppen von Pinterest sind mindestens 100 Nutzer:innen erforderlich. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | -- | Snapchat verarbeitet 10 Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Braze fasst Nutzer:innen alle 5 Sekunden zusammen. | Ja | Snapchat unterstützt bis zu 1.000 Zielgruppen. |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | Zwischen 24 und 48 Stunden | TikTok verarbeitet 50 Abfragen pro Sekunde und 10.000 Nutzer:innen pro Anfrage. Braze fasst Nutzer:innen alle 5 Sekunden zusammen. | Ja | {::nomarkdown}<ul><li>TikTok unterstützt bis zu 400 Zielgruppen.</li><li>Die Zielgruppen von TikTok benötigen mindestens 1.000 Nutzer:innen, um mit dem Adserving zu beginnen.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>Wenn das Rate-Limits erreicht ist, versucht Braze, die Synchronisierung 13 Stunden lang zu wiederholen.</sup>

## Funktionsweise

Um Audience Sync mit Google oder Facebook zu nutzen, verbinden Sie Ihr Anzeigenkonto, indem Sie auf der Seite **Technologie-Partner** nach dem Partner suchen.

![Facebook Technologie Partner.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google Ads Technologie Partner.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Nachdem Sie Ihr Anzeigenkonto verbunden haben, können Sie ein Canvas mit einem Audience Sync-Schritt erstellen.

![Canvas-Komponentenmenü, um den Schritt Audience Sync zur Nutzer:innen hinzuzufügen.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Als nächstes wählen Sie den Partner für die Synchronisierung der Zielgruppen aus.

![Option zum Auswählen eines Partners für die Synchronisierung Ihrer Zielgruppe im Schritt Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Für jeden Partner müssen Sie im Rahmen Ihres Audience Sync-Schrittes Folgendes konfigurieren: 

- Werbekonto
- Zielgruppe 
- Aktion zum Hinzufügen oder Entfernen von Nutzer:innen 
- Passende Felder 

Denken Sie daran, dass Braze die Nutzer:innen synchronisiert, sobald sie den Canvas-Schritt "Audience Sync" eingeben. 

Für jedes Audience Sync Ziel kann der Partner unterschiedliche Anforderungen an die Felder stellen, die wir senden können. Weitere Einzelheiten finden Sie in der Dokumentation des jeweiligen Partners. 

### Audience Sync Pro

Um einen Audience Sync Pro-Partner wie TikTok, Pinterest, Snapchat oder Criteo zu nutzen, können Sie Ihre Partner auf der Grundlage Ihrer Audience Sync Pro-Kaufkontingente im Abschnitt **Audience Sync Pro** auf der **Technologie-Partnerseite** auswählen.

![Audience Sync Pro, für das noch keine Partner ausgewählt wurden.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Wählen Sie zunächst die Partner aus, die Sie verwenden möchten, indem Sie Partner auswählen wählen. Mit jedem Kauf von Audience Sync Pro erhalten Sie 3 zugewiesene Audience Sync Pro Ziele, die in jedem Ihrer Workspaces auf Ihrem Dashboard verfügbar sind.

![Sie haben die Möglichkeit, bis zu drei Partner für die Verbindung mit Braze auszuwählen.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Nachdem Sie Ihre Audience Sync Pro Ziele ausgewählt haben, verbinden Sie Ihr ausgewähltes Partner-Anzeigenkonto, indem Sie auf die Partner-Kachel klicken.

![Ein Beispiel für Snapchat und TikTok, die als Partner für Audience Sync ausgewählt wurden.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Snapchat Zielgruppe Einstellungen mit der Nachricht synchronisieren: "Sie haben erfolgreich 1 Snapchat-Konto verbunden".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Schließlich erstellen Sie Ihren Canvas-Schritt zur Synchronisierung der Zielgruppen mit diesem Audience Sync Pro-Ziel.

### Zielgruppe Sync Fehler E-Mails

Wenn der Fehler mit der gesamten Partnerintegration zusammenhängt (z.B. ein Autorisierungsproblem), wird eine E-Mail an den Nutzer:innen gesendet, der die Integration verbunden hat. Wenn dieser Nutzer:innen nicht mehr existiert, erhalten die Administratoren die E-Mails. 

Wenn der Fehler auf Probleme mit der Komponente Audience Sync (z. B. "Zielgruppe existiert nicht") in Canvas zurückzuführen ist, wird eine E-Mail an den Nutzer:innen gesendet, der das Canvas eingerichtet hat. Wenn dieser Nutzer:in nicht mehr existiert, fällt er an den Administrator des Unternehmens zurück.

Um zu konfigurieren, wer diese E-Mails erhalten soll, wenden Sie sich an Ihren Customer-Success-Manager, um unter **Benachrichtigungseinstellungen** Empfänger:in hinzuzufügen. Da dieses Feature das derzeitige Verhalten ändert, müssen Sie die Empfänger sofort zu dieser neuen Benachrichtigungseinstellung hinzufügen, da Braze standardmäßig kein Opt-in vorsieht, und um sicherzustellen, dass keine Fehler-E-Mails verpasst werden.

## Überlegungen zum Datenschutz

{% alert important %}
Diese Dokumentation ist nicht als Rechtsberatung gedacht und darf auch nicht als solche angesehen werden. Die Verwendung von Audience Sync unterliegt bestimmten rechtlichen Anforderungen. Um sicherzustellen, dass Sie es in Übereinstimmung mit allen geltenden Gesetzen verwenden, sollten Sie sich von Ihrem Rechtsberater beraten lassen.
{% endalert %}

Beim Aufbau von Zielgruppen für das Ad Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z.B. das Recht "Nicht verkaufen oder weitergeben" gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen.

Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) erfasst haben, können Sie den Filter "Ads Tracking Enablement" verwenden. Wählen Sie den Wert `true` aus, um Nutzer:innen nur in Zielgruppen zu schicken, für die sie ein Opt-in gesetzt haben.

![Ein Canvas mit einem Eingang der Zielgruppe "Ad Tracking Enablement ist wahr".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute sammeln, sollten Sie diese in Ihre Canvas-Eingangskriterien als Filter einbeziehen:

![Ein Canvas mit einem Eingang Zielgruppe "opted_in_marketing" ist gleich "true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance/).

## Verwaltung der Zustimmung zum Ad Targeting

Als Werbetreibender sind Sie dafür verantwortlich, die Zustimmung zum Tracking oder Targeting Ihrer Nutzer:innen zu verwalten.

Um Anzeigen an Ihre Nutzer:innen zu senden, müssen Sie alle geltenden Gesetze und Vorschriften sowie die Richtlinien und Anforderungen der Anzeigenplattform einhalten. Verwenden Sie Braze nur dann zum Targeting und zur Synchronisierung von Nutzer:innen, wenn Sie deren Zustimmung eingeholt haben. 

Um Ihre Zielgruppenlisten in diesen Werbeplattformen auf dem neuesten Stand zu halten und Nutzer:innen zu entfernen, die ihre Zustimmung widerrufen haben, richten Sie ein Canvas ein, um Nutzer:innen mit einem Audience Sync-Schritt aus diesen bestehenden Zielgruppenlisten zu entfernen.


