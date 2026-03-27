---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung Push
page_order: 24
page_type: reference
description: "Diese Seite enthält Fehlerbehebungen für verschiedene Probleme im Zusammenhang mit dem Push-Messaging-Kanal."
channel: push
---

# Fehlerbehebung bei Push

> Nutzen Sie diese Seite zur Fehlerbehebung bei Problemen mit dem Push-Messaging-Kanal.

## Fehlende Push-Benachrichtigungen

Haben Sie Probleme bei der Zustellung von Push-Benachrichtigungen? Es gibt eine Reihe von Schritten, die Sie zur Fehlerbehebung unternehmen können, indem Sie Folgendes überprüfen:

- [Push-Abostatus](#push-subscription-status)
- [Segment](#segment)
- [Obergrenzen für Push-Benachrichtigungen](#push-notification-caps)
- [Rate-Limits](#rate-limits)
- [Status der Kontrollgruppe](#control-group-status)
- [Gültiges Push-Token](#valid-push-token)
- [Art der Push-Benachrichtigung](#push-notification-type)
- [Aktuelle App](#current-app)

#### Push-Abostatus

Pushes können nur an abonnierte oder Opt-in-Nutzer:innen gesendet werden. Überprüfen Sie Ihr Nutzerprofil auf dem Tab [Engagement]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) im Abschnitt **Nutzerprofil**, um zu sehen, ob Sie aktiv für Push für den Workspace registriert sind, den Sie testen. Wenn Sie für mehrere Apps registriert sind, finden Sie diese im Feld **Push registriert für** aufgelistet:

![Push registriert für]({% image_buster /assets/img_archive/trouble1.png %})

Sie können die Nutzerprofile auch über Braze-Export-Endpunkte exportieren:
- [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Beide Endpunkte geben ein Push-Token-Objekt zurück, das Push-Enablement-Informationen pro Gerät enthält.

#### Segment

Vergewissern Sie sich, dass Sie in das Segment fallen, auf das Sie Targeting betreiben (wenn es sich um eine Live-Kampagne und nicht um einen Test handelt). Im **Nutzerprofil** sehen Sie eine Liste der Segmente, in die der/die Nutzer:in derzeit fällt. Denken Sie daran, dass es sich hierbei um eine sich ständig ändernde Variable handelt, da die Segmentierung in Echtzeit aktualisiert wird.

![Liste der Segmente]({% image_buster /assets/img_archive/trouble2.png %})

Sie können auch bestätigen, dass der/die Nutzer:in Teil des Segments ist, indem Sie bei der Erstellung eines Segments die **Nutzersuche** verwenden.

![Abschnitt „Nutzersuche" mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Obergrenzen für Push-Benachrichtigungen

Prüfen Sie die globalen Frequency-Caps. Es ist möglich, dass Sie die Push-Benachrichtigung nicht erhalten haben, weil in Ihrem Workspace ein globales Frequency-Capping eingerichtet ist und Sie die Obergrenze für Push-Benachrichtigungen für den angegebenen Zeitrahmen bereits erreicht haben.

Sie können dies tun, indem Sie das [globale Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) im Dashboard überprüfen. Wenn die Kampagne so eingestellt ist, dass sie den Frequency-Capping-Regeln unterliegt, sind einige Nutzer:innen von diesen Einstellungen betroffen.

![Kampagnendetails]({% image_buster /assets/img_archive/trouble3.png %})

#### Rate-Limits

Wenn Sie für Ihre Kampagne oder Ihr Canvas ein Rate-Limit festgelegt haben, kann es sein, dass Sie keine Nachrichten mehr erhalten, weil Sie dieses Limit überschritten haben. Weitere Informationen finden Sie unter [Rate-Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Status der Kontrollgruppe

Wenn es sich um eine Kampagne mit einem einzelnen Kanal oder ein Canvas mit einer Kontrollgruppe handelt, ist es möglich, dass Sie in die Kontrollgruppe fallen.

  1. Überprüfen Sie die [Verteilung der Varianten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants), um festzustellen, ob es eine Kontrollgruppe gibt.
  2. Wenn ja, erstellen Sie ein Segment mit dem Filter [In Kampagnen-Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), [exportieren Sie das Segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) und überprüfen Sie, ob Ihre Nutzer-ID in dieser Liste enthalten ist.

#### Gültiges Push-Token
Ein Push-Token ist ein Bezeichner, den Absender verwenden, um bestimmte Geräte mit einer Push-Benachrichtigung anzusprechen. Wenn das Gerät also kein gültiges Push-Token besitzt, gibt es keine Möglichkeit, eine Push-Benachrichtigung an das Gerät zu senden. 

#### Art der Push-Benachrichtigung

Überprüfen Sie, ob Sie die richtige Art von Push-Benachrichtigung verwenden. Wenn Sie beispielsweise ein FireTV ansprechen möchten, würden Sie eine Kindle-Push-Benachrichtigung verwenden und keine Android-Push-Kampagne. Wenn Sie ein Android-Gerät targetieren möchten, verwenden Sie eine Android-Push-Benachrichtigung und keine iOS-Push-Kampagne. In den folgenden Artikeln finden Sie weitere Informationen zum Verständnis des Braze-Workflows für:
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aktuelle App

Wenn Sie Push-Sendungen mit internen Nutzer:innen testen, vergewissern Sie sich, dass der/die Nutzer:in, der/die die Push-Benachrichtigung erhalten soll, derzeit in der entsprechenden App angemeldet ist. Dies kann dazu führen, dass Nutzer:innen entweder keinen Push erhalten oder einen Push erhalten, von dem Sie glauben, dass er nicht für sie segmentiert ist.

## Klick auf eine Push-Benachrichtigung öffnet die App nicht

Wenn das Klicken auf eine Push-Benachrichtigung Ihre App nicht öffnet, überprüfen Sie je nach Plattform Folgendes.

### Android

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Kampagne so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Deeplink-Behandlung prüfen:** Überprüfen Sie in Ihrer `braze.xml`-Datei, ob `com_braze_handle_push_deep_links_automatically` auf `true` oder `false` gesetzt ist.
   - Wenn auf `true` gesetzt, behandelt das Braze SDK Deeplinks direkt und die App sollte wie erwartet geöffnet werden.
   - Wenn auf `false` gesetzt, benötigt Ihre App einen Broadcast-Receiver, der Push-Empfangs- und Öffnungs-Intents abhört und verarbeitet. Überprüfen Sie, ob dieser Receiver korrekt implementiert ist.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und stellen Sie die Logs zusammen mit Ihrer `braze.xml` und `AndroidManifest.xml` dem Braze Support zur Verfügung.

### iOS

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Kampagne so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Push-Integration prüfen:** Deeplinking von einem Push in die App wird automatisch durch die Braze [Standard-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) behandelt. Bestätigen Sie, dass die Integration korrekt implementiert ist, einschließlich einer eventuellen angepassten Delegate-Behandlung.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und stellen Sie die Logs dem Braze Support zur Verfügung.

## Push-Klicks werden unerwartet in der App geöffnet

Wenn Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Webbrowser geöffnet werden, liegt möglicherweise ein Problem mit der Konfiguration Ihrer Kampagne oder der SDK-Implementierung vor. Befolgen Sie diese Schritte zur Hilfe.

### Klickverhalten überprüfen

Überprüfen Sie in Ihrer Kampagne oder Ihrem Canvas-Schritt, dass die Option **Web-URL innerhalb der mobilen App öffnen** nicht ausgewählt ist. Ist dies der Fall, heben Sie die Auswahl auf und starten Sie erneut. 

![Das Feld „Klickverhalten" der Push-Konfiguration ist auf „Web-URL öffnen" eingestellt, wobei „Web-URL innerhalb der mobilen App öffnen" deaktiviert ist.]({% image_buster /assets/img/push_on_click.png %})

Die Standard-Interaktion für das Klickverhalten „Web-URL öffnen" unterscheidet sich je nach SDK-Version. Bei den SDK-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig ausgewählt und Web-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Web-URLs werden im Standard-Webbrowser des Geräts geöffnet.

Wenn dies nicht das Problem ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor. 

### Push-Integration doppelt prüfen

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit der Integration Ihrer Push-Benachrichtigungen oder mit den Anpassungseinstellungen liegen. Befolgen Sie diese Schritte zur Fehlerbehebung:

1. **Überprüfen Sie die Implementierung des Push-Delegaten:** Stellen Sie sicher, dass der Push-Delegat von Braze korrekt implementiert ist. Ausführliche Anweisungen finden Sie in der Integrationsanleitung für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home/).
2. **Prüfen Sie die angepasste Linkbehandlung:** Prüfen Sie, ob die App eine angepasste Handhabung für alle `https://`-Links enthält. Angepasste Konfigurationen können die Standardverhaltensweisen außer Kraft setzen. Arbeiten Sie mit Ihrem Entwickler:innen-Team zusammen, um diese Einstellungen zu überprüfen und ggf. anzupassen.
3. **Überprüfen Sie die iOS-Push-Registrierung:** Für iOS sehen Sie sich Schritt 1 der Anleitung zur Push-Integration zur [Registrierung von Push-Benachrichtigungen mit APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns) an. Stellen Sie sicher, dass Ihr Delegate-Objekt synchron zugewiesen wird, bevor die App den Start beendet. Diesen Schritt sollten Sie in der Methode `application:didFinishLaunchingWithOptions:` durchführen.
4. **Testen Sie Ihre Integration:** Nachdem Sie die Anpassungen vorgenommen haben, testen Sie das Verhalten der Push-Benachrichtigung sowohl auf iOS- als auch auf Android-Geräten, um sicherzustellen, dass das Problem behoben ist.

## Push-Titel wird auf iOS abgeschnitten, wird aber auf Android korrekt angezeigt

Wenn Ihr Push-Benachrichtigungstitel Liquid-Personalisierung enthält und auf Android vollständig angezeigt wird, aber auf iOS abgeschnitten ist, liegt dies daran, wie jede Plattform Zeilenumbruchzeichen (`\n`) im Titel-String behandelt.

Android entfernt automatisch Leerzeichen, Tabulatoren und Zeilenumbrüche aus Push-Titel-Strings. iOS tut dies nicht – wenn also eine Liquid-Variable zu einem Wert aufgelöst wird, der einen abschließenden Zeilenumbruch enthält, behandelt iOS den Zeilenumbruch als Ende des Titels und schneidet den restlichen Text ab.

Zum Beispiel könnte ein Titel wie `Regarding your flight from {% raw %}{{${city_from}}}{% endraw %} to {% raw %}{{${city_to}}}{% endraw %}` auf iOS als `Regarding your flight from` angezeigt werden, wenn die Variable `city_from` einen abschließenden Zeilenumbruch enthält.

Um dies zu beheben, wenden Sie den Liquid-Filter `strip_newlines` an und umschließen Sie den gesamten Titel mit einem `capture`-Block:

{% raw %}
```liquid
{% capture title %}Regarding your flight from {{${city_from}}} to {{${city_to}}}{% endcapture %}
{{ title | strip_newlines }}
```
{% endraw %}

## Web-Push-Benachrichtigungen funktionieren nicht wie erwartet

Wenn Sie Probleme mit Push-Benachrichtigungen in Ihrem Browser haben, müssen Sie möglicherweise die Benachrichtigungsberechtigungen Ihrer Website zurücksetzen und den Speicher Ihrer Website leeren. Befolgen Sie diese Schritte zur Hilfe.

{% tabs %}
{% tab Chrome %}

### Chrome auf dem Desktop zurücksetzen

1. Wählen Sie neben Ihrer URL im Chrome-Browser das Schieberegler-Symbol **Website-Informationen anzeigen** aus.
2. Wählen Sie unter **Benachrichtigungen** die Option **Berechtigung zurücksetzen**.
3. Öffnen Sie Chrome DevTools. Im Folgenden finden Sie die relevanten Tastenkombinationen pro Betriebssystem.

<style> 
table {
    max-width: 50%;
}
</style>

| Betriebssystem | Tastenkombinationen                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4. Navigieren Sie in DevTools zum Tab **Application**.
5. Wählen Sie in der Seitenleiste **Storage** aus.
6. Wählen Sie **Clear site data**.
7. Chrome fordert Sie auf, die Seite neu zu laden, um Ihre aktualisierten Einstellungen zu übernehmen. Wählen Sie **Reload**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

### Chrome auf Android zurücksetzen

Wenn Sie eine Benachrichtigung von Ihrer Website in Ihrem Android-Benachrichtigungsfeld sehen:

1. Tippen Sie in der Push-Benachrichtigung auf <i class="fas fa-cog" title="Einstellungen"></i> und wählen Sie **Website-Einstellungen**.
2. Tippen Sie in den **Website-Einstellungen** auf **Löschen und Zurücksetzen**.

Wenn Sie keine Benachrichtigung von Ihrer Website geöffnet haben:

1. Öffnen Sie Chrome auf Android.
2. Tippen Sie auf das Menü <i class="fas fa-ellipsis-vertical"></i>.
3. Gehen Sie zu **Einstellungen** > **Website-Einstellungen** > **Benachrichtigungen**.
4. Überprüfen Sie, dass die Benachrichtigungen auf **Vor dem Senden fragen (empfohlen)** eingestellt sind.
5. Finden Sie Ihre Website in der Liste.
6. Wählen Sie den Eintrag aus und tippen Sie auf **Löschen und Zurücksetzen**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

{% endtab %}
{% tab Firefox %}

### Firefox auf dem Desktop zurücksetzen

1. Wählen Sie neben Ihrer Website-URL entweder <i class="fa-solid fa-circle-info" alt="info icon"></i> oder <i class="fas fa-lock" alt="lock icon"></i> aus.
2. Wählen Sie unter **Berechtigungen** neben **Benachrichtigungen erhalten** das Symbol <i class="fa-solid fa-circle-xmark" title="Diese Berechtigung löschen und erneut fragen"></i>, um die Benachrichtigungsberechtigungen zu löschen.
3. Wählen Sie im gleichen Menü **Cookies und Website-Daten löschen** aus.
4. Wählen Sie im Dialogfeld zur Bestätigung Ihrer Auswahl **OK**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

### Firefox auf Android zurücksetzen

Um Push-Berechtigungen unter Android zurückzusetzen, lesen Sie diesen [Support-Artikel von Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Safari auf macOS zurücksetzen

{% alert note %}
Diese Schritte gelten ausschließlich für macOS, da Apple Web-Push für Safari unter Windows nicht unterstützt.
{% endalert %}

1. Öffnen Sie Safari.
2. Gehen Sie in der [Menüleiste auf dem Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) zu **Safari** > **Einstellungen** > **Websites** > **Benachrichtigungen**.
3. Wählen Sie Ihre Website aus der Liste aus.
4. Wählen Sie **Entfernen**, um die Benachrichtigungsberechtigungen für die Website zu löschen.
5. Gehen Sie dann zu **Datenschutz** > **Website-Daten verwalten**.
6. Wählen Sie Ihre Website aus der Liste aus.
7. Wählen Sie **Entfernen** oder, um alle Website-Daten zu löschen, **Alle entfernen**.
8. Wählen Sie **Fertig**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

{% endtab %}
{% endtabs %}

## Push-Fehlermeldungen

Ausführliche Informationen zu häufigen Push-Fehlermeldungen (wie `DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered` und andere) finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).