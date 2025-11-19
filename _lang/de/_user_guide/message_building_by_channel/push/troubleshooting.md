---
nav_title: Fehlersuche
article_title: Fehlerbehebung Push
page_order: 23
page_type: reference
description: "Diese Seite enthält Fehlerbehebungen für verschiedene Probleme im Zusammenhang mit dem Push Messaging-Kanal."
channel: push
---

# Fehlerbehebung Push

> Diese Seite hilft Ihnen bei der Behebung verschiedener Probleme, die mit dem Messaging-Kanal von Push auftreten können.

## Fehlende Push-Benachrichtigungen

Haben Sie Probleme bei der Zustellung von Push-Benachrichtigungen? Es gibt eine Reihe von Schritten, die Sie zur Fehlerbehebung unternehmen können, indem Sie die:

- [Push-Abostatus](#push-subscription-status)
- [Segment](#segment)
- [Push-Benachrichtigungen Kappen](#push-notification-caps)
- [Rate-Limits](#rate-limits)
- [Status der Kontrollgruppe](#control-group-status)
- [Gültiges Push-Token](#valid-push-token)
- [Art der Push-Benachrichtigung](#push-notification-type)
- [Aktuelle App](#current-app)

#### Push-Abostatus

Pushes können nur an abonnierte oder Opt-in Nutzer:innen gesendet werden. Überprüfen Sie Ihr Nutzerprofil auf dem Tab [Engagement]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) im Abschnitt **Benutzerprofil**, um zu sehen, ob Sie aktiv für Push für den Workspace, den Sie testen, registriert sind. Wenn Sie für mehrere Apps registriert sind, finden Sie diese im Feld **Push registriert für** aufgelistet:

![Push registriert für]({% image_buster /assets/img_archive/trouble1.png %})

Sie können die Nutzerprofile auch über Braze Export-Endpunkte exportieren:
- [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Nutzer:innen nach Segmenten]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Beide Endpunkte geben ein Push-Token-Objekt zurück, das Push Enablement-Informationen pro Gerät enthält.

#### Segment

Vergewissern Sie sich, dass Sie in das Segment fallen, auf das Sie Targeting betreiben (wenn es sich um eine Live-Kampagne und nicht um einen Test handelt). Im **Nutzerprofil** sehen Sie eine Liste der Segmente, in die der Nutzer:innen derzeit fällt. Denken Sie daran, dass es sich hierbei um eine sich ständig ändernde Variable handelt, da die Segmentierung in Realtime aktualisiert wird.

![Liste der Segmente]({% image_buster /assets/img_archive/trouble2.png %})

Sie können auch bestätigen, dass der Nutzer:innen Teil des Segments ist, indem Sie bei der Erstellung eines Segments die **Benutzersuche** verwenden.

![Abschnitt Nutzer:in mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Push-Benachrichtigungen Kappen

Prüfen Sie die globalen Frequenz-Caps. Es ist möglich, dass Sie die Push-Benachrichtigung nicht erhalten haben, weil in Ihrem Workspace ein globales Frequency-Capping eingerichtet ist und Sie die Obergrenze für Push-Benachrichtigungen für den angegebenen Zeitrahmen bereits erreicht haben.

Sie können dies tun, indem Sie das [globale Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) im Dashboard aktivieren. Wenn die Kampagne so eingestellt ist, dass sie den Frequency-Capping-Regeln unterliegt, sind einige Nutzer:innen von diesen Einstellungen betroffen.

![Details zur Kampagne]({% image_buster /assets/img_archive/trouble3.png %})

#### Rate-Limits

Wenn Sie für Ihre Kampagne oder Ihr Canvas ein Rate-Limit festgelegt haben, kann es sein, dass Sie keine Nachrichten mehr erhalten, weil Sie dieses Limit überschritten haben. Weitere Informationen finden Sie unter [Rate-Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Status der Kontrollgruppe

Wenn es sich um eine Kampagne mit einem Kanal oder ein Canvas mit einer Kontrollgruppe handelt, ist es möglich, dass Sie in die Kontrollgruppe fallen.

  1. Überprüfen Sie die [Verteilung der Varianten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants), um festzustellen, ob es eine Kontrollgruppe gibt.
  2. Wenn ja, erstellen Sie einen Filter für die [Kontrollgruppe der Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), [exportieren Sie das Segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) und überprüfen Sie, ob Ihre Nutzer:innen in dieser Liste enthalten sind.

#### Gültiges Push-Token
Ein Push-Token ist ein Bezeichner, den Absender verwenden, um bestimmte Geräte mit einer Push-Benachrichtigung anzusprechen. Wenn das Gerät also kein gültiges Push-Token besitzt, gibt es keine Möglichkeit, eine Push-Benachrichtigung an das Gerät zu senden. 

#### Art der Push-Benachrichtigung

Überprüfen Sie, ob Sie die richtige Art von Push-Benachrichtigung verwenden. Wenn Sie beispielsweise ein FireTV-Gerät als Targeting verwenden möchten, würden Sie eine Kindle Push-Benachrichtigung verwenden und keine Android Push-Kampagne. Wenn Sie ein Android-Gerät targetieren möchten, verwenden Sie eine Push-Benachrichtigung für Android und keine Push-Kampagne für iOS. In den folgenden Artikeln finden Sie weitere Informationen zum Verständnis des Braze-Workflows für:
- [Apple Push-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aktuelle App

Wenn Sie Push-Sendungen mit internen Nutzern testen, vergewissern Sie sich, dass der Nutzer:in, der die Push-Benachrichtigung erhalten soll, derzeit in der entsprechenden App angemeldet ist. Dies kann dazu führen, dass Nutzer:innen entweder keinen Push erhalten oder einen Push erhalten, von dem Sie glauben, dass er nicht segmentiert ist.

## Push-Klicks öffnen unerwartet in der App

Wenn Sie Probleme damit haben, dass Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Internetbrowser geöffnet werden, liegt möglicherweise ein Problem mit der Konfiguration Ihrer Kampagne oder der Implementierung des SDK vor. Beziehen Sie sich auf diese Schritte für Hilfe.

### Überprüfen Sie das Verhalten bei einem Klick

Überprüfen Sie in Ihrer Kampagne oder im Canvas-Schritt, dass die Option **Internet-URL innerhalb der mobilen App öffnen** nicht ausgewählt ist. Ist dies der Fall, löschen Sie die Auswahl und starten Sie erneut. 

!["Verhalten bei Klick" bei der Konfiguration eines Push auf "Internet-URL öffnen" gesetzt und "Internet-URL innerhalb der mobilen App öffnen" nicht markiert.]({% image_buster /assets/img/push_on_click.png %})

Die Standard-Interaktion für das Klickverhalten "Internet-URL öffnen" unterscheidet sich je nach SDK-Version. Bei den SDK-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig ausgewählt und die Internet-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Internet-URLs werden im Standard Webbrowser des Geräts geöffnet.

Wenn dies nicht der Fall ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor. 

### Push-Integration doppelt prüfen

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit der Integration Ihrer Push-Benachrichtigungen oder mit den Anpassungseinstellungen liegen. Befolgen Sie diese Schritte zur Fehlerbehebung:

1. **Überprüfen Sie die Implementierung des Push-Delegaten:** Stellen Sie sicher, dass der Push-Delegat von Braze korrekt implementiert ist. Ausführliche Anweisungen finden Sie in der Integrationsanleitung für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home/).
2. **Prüfen Sie die angepasste Linkbehandlung:** Prüfen Sie, ob die App eine angepasste Handhabung für alle `https://` Links enthält. Angepasste Konfigurationen können die Standard-Verhaltensweisen außer Kraft setzen. Arbeiten Sie mit Ihrem Entwickler:in Team zusammen, um diese Einstellungen zu überprüfen und ggf. anzupassen.
3. **Überprüfen Sie die iOS Push-Registrierung:** Für iOS sehen Sie sich Schritt 1 der Anleitung zur Integration von [Push-Benachrichtigungen mit APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns) an. Stellen Sie sicher, dass Ihr Delegatenobjekt synchron zugewiesen wird, bevor die App den Start beendet. Diesen Schritt sollten Sie mit der Methode `application:didFinishLaunchingWithOptions:` durchführen.
4. **Testen Sie Ihre Integration:** Nachdem Sie die Anpassungen vorgenommen haben, testen Sie das Verhalten der Push-Benachrichtigung sowohl auf iOS- als auch auf Android-Geräten, um sicherzustellen, dass das Problem behoben ist.

## Web-Push-Benachrichtigungen verhalten sich nicht wie erwartet

Wenn Sie Probleme mit Push-Benachrichtigungen in Ihrem Browser haben, müssen Sie möglicherweise die Benachrichtigungsberechtigungen Ihrer Website zurücksetzen und den Speicher Ihrer Website leeren. Beziehen Sie sich auf diese Schritte für Hilfe.

{% tabs %}
{% tab Chrome %}

### Chrome auf dem Desktop zurücksetzen

1. Wählen Sie im Chrome-Browser neben Ihrer URL das Symbol für den Schieberegler **Site-Informationen anzeigen**.
2. Wählen Sie unter **Benachrichtigungen** die Option **Berechtigung zurücksetzen**.
3. Öffnen Sie Chrome DevTools. Im Folgenden finden Sie die relevanten Tastenkombinationen pro Betriebssystem.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Tastaturkürzel                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. Navigieren Sie in DevTools zum Tab **Anwendung**.
5\. Wählen Sie in der Seitenleiste **Speicher** aus.
6\. Wählen Sie **Standortdaten löschen**.
7\. Chrome fordert Sie auf, die Seite neu zu laden, um Ihre aktualisierten Einstellungen zu übernehmen. Wählen Sie **Neu laden**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

### Chrome auf Android zurücksetzen

Wenn Sie eine Benachrichtigung von Ihrer Website in Ihrem Android Benachrichtigungsfeld sehen:

1. Tippen Sie in der Push-Benachrichtigung auf <i class="fas fa-cog" title="Einstellungen"></i> und wählen Sie **Website-Einstellungen**.
2. Tippen Sie in den **Website-Einstellungen** auf **Löschen & Zurücksetzen**.

Wenn Sie keine Benachrichtigung von Ihrer Website geöffnet haben:

1. Öffnen Sie Chrome auf Android.
2. Tippen Sie auf das Menü <i class="fas fa-ellipsis-vertical"></i>.
3. Gehen Sie zu **Einstellungen** > **Website-Einstellungen** > **Benachrichtigungen**.
4. Überprüfen Sie, ob die Benachrichtigungen **vor dem Senden** auf **Fragen** eingestellt sind **(empfohlen)**.
5. Finden Sie Ihre Website in der Liste.
6. Wählen Sie den Eintrag aus und tippen Sie auf **Löschen und Zurücksetzen**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

{% endtab %}
{% tab Firefox %}

### Firefox auf dem Desktop zurücksetzen

1. Wählen Sie neben der URL Ihrer Website <i class="fa-solid fa-circle-info" alt="info icon"></i> oder <i class="fas fa-lock" alt="lock icon"></i> aus.
2. Wählen Sie unter **Berechtigungen**, neben **Benachrichtigungen erhalten**<i class="fa-solid fa-circle-xmark" title="Diese Berechtigung löschen und erneut fragen"></i> um die Berechtigungen für Benachrichtigungen zu löschen.
3. Wählen Sie im gleichen Menü **Cookies und Website-Daten löschen aus**.
4. Wählen Sie in dem Dialog zur Bestätigung Ihrer Wahl **OK** aus.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

### Firefox auf Android zurücksetzen

Um Push-Berechtigungen unter Android zurückzusetzen, referenzieren Sie diesen [Support-Artikel von Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Safari auf macOS zurücksetzen

{% alert note %}
Diese Schritte gelten nur für macOS, da Apple Web-Push für Safari unter Windows nicht unterstützt.
{% endalert %}

1. Öffnen Sie Safari.
2. Gehen Sie in der [Menüleiste auf dem Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) zu **Safari** > **Einstellungen** > **Websites** > **Benachrichtigungen**.
3. Wählen Sie Ihren Standort aus der Liste aus.
4. Wählen Sie **Entfernen**, um die Benachrichtigungsberechtigungen für die Website zu löschen.
5. Gehen Sie dann zu **Datenschutz** > **Website-Daten verwalten**.
6. Wählen Sie Ihren Standort aus der Liste aus.
7. Wählen Sie **Entfernen**, oder um alle Daten der Website zu entfernen, wählen Sie **Alle entfernen**.
8. Wählen Sie **Erledigt**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

{% endtab %}
{% endtabs %}

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

