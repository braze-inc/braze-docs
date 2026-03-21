---
nav_title: Hinweise
article_title: Best Practices für Hinweise
description: "Informationen, Richtlinien und Beispiele für Hinweistypen, die in der Braze-Dokumentation verwendet werden."
page_order: 2
noindex: true
---

# Best Practices für Hinweise

> Dieses Dokument enthält Informationen, allgemeine Richtlinien und Beispiele für Hinweistypen, die in der Braze-Dokumentation verwendet werden.

## Hinweistypen {#alert-types}

Hinweise kategorisieren Informationen, die Leser:innen beachten sollten. Es gibt vier Hinweistypen, die in unserer Dokumentation verwendet werden können:

* Wichtig  
* Hinweis  
* Tipp  
* Warnung

## Wann Sie einen Hinweis verwenden sollten {#when-to-use-an-alert}

Verwenden Sie Hinweise, um die Aufmerksamkeit der Leser:innen auf wichtige Informationen zu lenken. Halten Sie den Inhalt kurz und prägnant. Wir möchten sicherstellen, dass die Informationen bei den Leser:innen hängen bleiben.

In der folgenden Tabelle finden Sie Definitionen für jeden Hinweistyp:

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 20%;"><col style="width: 80%;"></colgroup>
<thead>
<tr><th>Hinweistyp</th><th>Definition</th></tr>
</thead>
<tbody>
<tr><td>Wichtig</td><td>Enthält wesentliche Informationen, die von den Leser:innen beachtet werden <strong>sollten</strong>, wie z. B.: <ul><li>Veraltete Features</li><li>Auswirkungen auf die Abrechnung</li><li>Informationen zu relevanten Updates</li><li>Dringende Feature-Einschränkungen (z. B. Beta-Features)</li><li>Andere wichtige Informationsdetails</li></ul></td></tr>
<tr><td>Hinweis</td><td>Enthält einmalige Informationen, die Leser:innen kennen sollten, wie z. B.: <ul><li>Feature-Einschränkungen</li><li>Formatierungshinweise</li><li>Hilfreiche Anmerkungen</li><li>Informationen, die von einem Wichtig-Hinweis herabgestuft wurden, weil der Schweregrad des Inhalts gesunken ist (z. B. ein langjähriger Wichtig-Hinweis, der zu einem Standard-Hinweis wird)</li></ul></td></tr>
<tr><td>Tipp</td><td>Enthält ergänzendes Wissen und Empfehlungen, die Leser:innen kennen sollten, wie z. B.: <ul><li>Zusätzliche Artikel zur Fehlerbehebung</li><li>Schritte und Abkürzungen, die die Benutzerfreundlichkeit erhöhen (z. B. zusätzliche Anpassungen für In-App-Nachrichten)</li></ul></td></tr>
<tr><td>Warnung</td><td>Enthält wesentliche Informationen, die Leser:innen unbedingt beachten müssen, und kann Folgendes umfassen: <ul><li>Irreversible Konsequenzen (z. B. Löschung von Kampagnen und Canvas)</li><li>Feature-brechendes Verhalten</li><li>Datenverlust</li><li>Andere wichtige Warnungen</li></ul></td></tr>
</tbody>
</table>
{:/}

**Best Practices für Hinweise**  
Hier finden Sie allgemeine Richtlinien und Best Practices für Hinweise.

Als allgemeine Faustregel sollten Sie Hinweise nicht für Inhalte verwenden, die für die Artikelstruktur wesentlich sind (wie Feature-Einführungen, Einrichtungsanweisungen und Schritte zur Nutzung eines Features). Im Zweifelsfall konsultieren Sie das Team während des Peer-Reviews.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup>
<thead>
<tr><th>Richtlinie</th><th>Beispiel</th></tr>
</thead>
<tbody>
<tr><td>Erklären Sie die Informationen im Hinweis in einer klaren, prägnanten Aussage.</td><td>{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}<br><br> <a href="{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">Hinweis in Schritt 4: Filter zu Ihrem Segment hinzufügen</a></td></tr>
<tr><td>Erwägen Sie bei Hinweisen, die für verschiedene Abschnitte desselben Artikels gelten, einen neuen Abschnitt zu erstellen, der diese Details erfasst, um sich wiederholende Inhalte zu vermeiden.</td><td>{% multi_lang_include currents/property_details_dispatch_state_source.md %}<br><br> <a href="{{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">Eigenschaftsdetails in Nachrichten-Engagement-Events</a></td></tr>
<tr><td>Gliedern Sie die Informationen innerhalb des Hinweises in kurze Absätze oder Listen.</td><td>{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}<br><br> <a href="{{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">Wichtig-Hinweis in „Ihre E-Mail-Liste importieren"</a></td></tr>
<tr><td>Berücksichtigen Sie zusätzliche Formatierungen, die die Darstellung des Hinweises beeinflussen können (Code-Snippets, Schritte, umgebende Bilder und mehr).</td><td>{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}<br><br> <a href="{{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">Tipp-Hinweis mit Code-Snippet in „Preissenkungsbenachrichtigungen"</a></td></tr>
<tr><td>Fügen Sie einen Zeilenumbruch für Hinweise ein, die einen Artikel beginnen.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_5.png %}" alt="Beispiel eines Hinweises am Anfang eines Artikels."><br><br> <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">Content-Card-Implementierungsleitfaden</a></td></tr>
<tr><td>Wenn Sie über Beta-Features schreiben, fügen Sie einen Wichtig-Hinweis ein, der den Beta-Status und die zugehörigen Braze-Kontaktinformationen hervorhebt. Platzieren Sie diesen Beta-Hinweis nach dem Übersichtstext und vor der ersten Hauptüberschrift.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_6.png %}" alt="Beispiel eines Wichtig-Hinweises für ein Beta-Feature."></td></tr>
<tr><td>Vermeiden Sie nach Möglichkeit die Verwendung von zwei oder mehr Hinweisen hintereinander. Organisieren Sie stattdessen die Informationen neu oder integrieren Sie sie in den Text.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_7.png %}" alt="Ein Beispiel für zwei Hinweise nebeneinander – das sollten Sie vermeiden."></td></tr>
<tr><td>Wenn Ihr Hinweis zu lang wird, erwägen Sie, einen neuen Abschnitt zu erstellen, der die Informationen als Liste enthält. Anstatt beispielsweise Schritte zur Fehlerbehebung in einen Hinweis aufzunehmen, erstellen Sie einen Abschnitt zur Fehlerbehebung oder stellen Sie einen Link zu einem verwandten Artikel bereit.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_8.png %}" alt="Beispiel eines neuen Inhaltsabschnitts."></td></tr>
</tbody>
</table>
{:/}

## Hinweisbeispiele {#alert-examples}

In den folgenden Beispielen erfahren Sie, wie und warum jeder Hinweistyp in unserer Dokumentation verwendet wird.

### Wichtig-Hinweis {#important-alert}

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

* **Artikel:** [Web-Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **Anwendungsfall:** Enthält eine wesentliche Feature-Einschränkung, die Leser:innen bei der Einrichtung ihres Web-Push kennen sollten.
* **Begründung für den Hinweis:** Verwenden Sie einen Wichtig-Hinweis anstelle eines einfachen Hinweises, da die Bedeutung des Inhalts für Leser:innen bei der Einrichtung ihres Web-Push größer ist.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

* **Artikel:** [E-Mail-Einstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **Anwendungsfall:**
  - Bietet eine wichtige Feature-Einschränkung bezüglich der Möglichkeit, abrechenbare E-Mails zu verdoppeln
  - Leitet Leser:innen bei Bedarf an ihren Customer-Success-Manager weiter
* **Begründung für den Hinweis:** Der Wichtig-Hinweis wird hier verwendet, um Details über die BCC-Adressen in den E-Mail-Einstellungen zu kommunizieren. Diese Informationen werden am besten mit einem Wichtig-Hinweis anstelle eines Warnungs-Hinweises dargestellt, da das Auslassen dieser Informationen das Feature nicht irreversibel beeinträchtigt (wie Feature-Bruch oder permanenter Datenverlust).

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **Artikel:** [Erweiterte Kampagneneinstellungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Anwendungsfall:** Enthält eine dringende Feature-Einschränkung bezüglich der Benachrichtigungspriorität. Leitet Leser:innen zu neuen verfügbaren Informationen weiter.
* **Begründung für den Hinweis:** Der Wichtig-Hinweis eignet sich hier am besten, um Leser:innen zu aktuellen Informationen weiterzuleiten und hervorzuheben, dass der Abschnitt nur für bestimmte Nutzer:innen gilt. Er ist zudem nach der Abschnittsüberschrift platziert, sodass die Nutzer:innen den Wichtig-Hinweis beachten müssen, bevor sie den Rest des Abschnitts lesen.

### Hinweis {#note-alert}

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **Artikel:** [Eine Content-Card erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **Anwendungsfall:** Enthält zusätzliche Informationen, die Leser:innen kennen sollten, wenn sie mehr über Content-Cards erfahren.
* **Begründung für den Hinweis:** Dieser Hinweis bietet Hintergrundinformationen darüber, wie Braze ältere Content-Cards für Nutzer:innen rotiert. Dies sind hilfreiche, ergänzende Informationen für Leser:innen und erfordern keinen Wichtig- oder Tipp-Hinweis.

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **Artikel:** [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **Anwendungsfall:** Enthält allgemeine Informationen, die Leser:innen kennen sollten. Bietet einen Artikel, um mehr über verwandte Inhalte (Zeitattribute) zu erfahren.
* **Begründung für den Hinweis:** Diese Informationen werden am besten mit einem Hinweis anstelle eines Wichtig-Hinweises vermittelt, da der Inhalt darauf abzielt, allgemeine Informationen bereitzustellen. Das Ignorieren dieser Informationen würde die Benutzerfreundlichkeit dieses Features nicht beeinträchtigen.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

* **Artikel:** [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Anwendungsfall:** Enthält allgemeine Informationen, die Leser:innen kennen sollten. Leitet für weitere Informationen an den Braze-Kontakt weiter.
* **Begründung für den Hinweis:** Dieser Hinweis bietet zusätzliche Informationen zur Datenspeicherung, die für Leser:innen bei der Verwaltung ihrer angepassten Attribute hilfreich sein können. Der Inhalt erfordert jedoch keine stärkere Hervorhebung der Wichtigkeit, sodass ein Hinweis hier angemessen ist.

### Tipp-Hinweis {#tip-alert}

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **Artikel:** [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Anwendungsfall:** Enthält ein Tool, mit dem Leser:innen ihre Nachrichtenlänge und SMS-Segment-Anzahl verstehen können. Bietet Informationen, die für das Verständnis von Textlimits hilfreich sein können.
* **Begründung für den Hinweis:** Dies ist ein längerer Tipp-Hinweis, da er einen Bereich zum Eingeben von Text bietet, um zu sehen, wie viele Segmente eine Nachricht versendet. Der Tipp-Hinweis ist hier die beste Option, da es sich um einen hilfreichen Generator handelt, den Leser:innen bei der Einrichtung ihrer SMS-Nachrichten nutzen können.

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **Artikel:** [KPIs für tägliche App-Deinstallationen nach Datum exportieren]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Anwendungsfall:** Bietet Ratschläge zur Fehlerbehebung bei der Verwendung dieses Endpunkts.
* **Begründung für den Hinweis:** Der Tipp-Hinweis bietet zusätzliche Unterstützung für Leser:innen. Verwenden Sie einen Tipp-Hinweis anstelle eines einfachen Hinweises, da der Fokus des Inhalts darauf liegt, Leser:innen durch Bereitstellung des Artikels zur Fehlerbehebung zu unterstützen.

### Warnungs-Hinweis {#warning-alert}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

* **Artikel:** [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Anwendungsfall:** Weist darauf hin, was Leser:innen bei der Erstellung ihrer Nutzerprofile in Braze nicht tun sollten.
* **Begründung für den Hinweis:** Der Warnungs-Hinweis wird verwendet, um Leser:innen davor zu warnen, eine external_id zuzuweisen, bevor Nutzer:innen eindeutig identifiziert wurden. Diese Informationen werden am besten mit einem Warnungs-Hinweis anstelle eines Wichtig-Hinweises vermittelt, da sie irreversible Konsequenzen für das Nutzerprofil beinhalten.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **Artikel:** [Segment für Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Anwendungsfall:** Warnt Leser:innen bei der Erstellung von Currents-Konnektoren. Enthält die Konsequenzen einer fehlerhaften Erstellung dieser Konnektoren.
* **Begründung für den Hinweis:** Der Warnungs-Hinweis eignet sich hier am besten, um die Einschränkungen der Braze Segment Currents-Integration zu beschreiben. Verwenden Sie einen Warnungs-Hinweis anstelle eines Wichtig-Hinweises, da die fehlerhafte Erstellung von mehr als einem gleichen Currents-Konnektor zu Datenverlust führen kann.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **Artikel:** [Ein Canvas erstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Anwendungsfall:** Listet die Informationen auf, die dazu führen können, dass das Feature nicht funktioniert. Beschreibt, wie die beabsichtigte Zielgruppe die Kampagne möglicherweise nicht erhält oder das Canvas nicht betritt.
* **Begründung für den Hinweis:** Der Warnungs-Hinweis wird hier verwendet, um darauf hinzuweisen, wie das Feature möglicherweise fehlerhaft funktioniert. Diese Informationen werden am besten mit einem Warnungs-Hinweis anstelle eines Wichtig-Hinweises vermittelt, da die Informationen kritisch sind und zum Bruch der Canvas-Zustellung führen können.