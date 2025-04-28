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

Pushes können nur an abonnierte oder Opt-in Nutzer:innen gesendet werden. Überprüfen Sie Ihr Nutzerprofil auf dem Tab [Engagement][1] im Abschnitt **Benutzerprofil**, um zu sehen, ob Sie aktiv für Push für den Workspace, den Sie testen, registriert sind. Wenn Sie für mehrere Apps registriert sind, finden Sie diese im Feld **Push registriert für** aufgelistet:

![Push registriert für][2]

Sie können die Nutzerprofile auch über Braze Export-Endpunkte exportieren:
- [Nutzer:innen nach Bezeichner][12]
- [Nutzer:innen nach Segmenten][13]

Beide Endpunkte geben ein Push-Token-Objekt zurück, das Push Enablement-Informationen pro Gerät enthält.

#### Segment

Vergewissern Sie sich, dass Sie in das Segment fallen, auf das Sie Targeting betreiben (wenn es sich um eine Live-Kampagne und nicht um einen Test handelt). Im **Nutzerprofil** sehen Sie eine Liste der Segmente, in die der Nutzer:innen derzeit fällt. Denken Sie daran, dass es sich hierbei um eine sich ständig ändernde Variable handelt, da die Segmentierung in Realtime aktualisiert wird.

![Liste der Segmente][3]

Sie können auch bestätigen, dass der Nutzer:innen Teil des Segments ist, indem Sie bei der Erstellung eines Segments die **Benutzersuche** verwenden.

![Abschnitt „Nutzersuche“ mit einem Suchfeld.][14]{: style="max-width:80%;"}

#### Push-Benachrichtigungen Kappen

Prüfen Sie die globalen Frequenz-Caps. Es ist möglich, dass Sie die Push-Benachrichtigung nicht erhalten haben, weil in Ihrem Workspace ein globales Frequency-Capping eingerichtet ist und Sie die Obergrenze für Push-Benachrichtigungen für den angegebenen Zeitrahmen bereits erreicht haben.

Sie können dies tun, indem Sie [Globales Frequency-Capping][4] auf dem Dashboard aktivieren. Wenn die Kampagne so eingestellt ist, dass sie den Frequency-Capping-Regeln unterliegt, sind einige Nutzer:innen von diesen Einstellungen betroffen.

![Kampagne Details][5]

#### Rate-Limits

Wenn Sie für Ihre Kampagne oder Ihr Canvas ein Rate-Limit festgelegt haben, kann es sein, dass Sie keine Nachrichten mehr erhalten, weil Sie dieses Limit überschritten haben. Weitere Informationen finden Sie unter [Rate-Limiting][9].

#### Status der Kontrollgruppe

Wenn es sich um eine Kampagne mit einem Kanal oder ein Canvas mit einer Kontrollgruppe handelt, ist es möglich, dass Sie in die Kontrollgruppe fallen.

  1. Prüfen Sie unter [Variantenverteilung][6], ob es eine Kontrollgruppe gibt.
  2. Wenn ja, erstellen Sie eine Segmentierung für [in der Kontrollgruppe der Kampagne][7] dann [exportieren Sie das Segment][8] und überprüfen Sie, ob Ihre Nutzer:innen in dieser Liste enthalten ist.

#### Gültiges Push-Token
Ein Push-Token ist ein Bezeichner, den Absender verwenden, um bestimmte Geräte mit einer Push-Benachrichtigung anzusprechen. Wenn das Gerät also kein gültiges Push-Token besitzt, gibt es keine Möglichkeit, eine Push-Benachrichtigung an das Gerät zu senden. 

#### Art der Push-Benachrichtigung

Überprüfen Sie, ob Sie die richtige Art von Push-Benachrichtigung verwenden. Wenn Sie beispielsweise ein FireTV-Gerät als Targeting verwenden möchten, würden Sie eine Kindle Push-Benachrichtigung verwenden und keine Android Push-Kampagne. Wenn Sie ein Android-Gerät targetieren möchten, verwenden Sie eine Push-Benachrichtigung für Android und keine Push-Kampagne für iOS. In den folgenden Artikeln finden Sie weitere Informationen zum Verständnis des Braze-Workflows für:
- [Apple Push-Benachrichtigung][10]
- [Firebase Cloud Messaging][11]

#### Aktuelle App

Wenn Sie Push-Sendungen mit internen Nutzern testen, vergewissern Sie sich, dass der Nutzer:in, der die Push-Benachrichtigung erhalten soll, derzeit in der entsprechenden App angemeldet ist. Dies kann dazu führen, dass Nutzer:innen entweder keinen Push erhalten oder einen Push erhalten, von dem Sie glauben, dass er nicht segmentiert ist.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/
[11]: {{site.baseurl}}/developer_guide/platforms/android/push_notifications/troubleshooting/
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment
[14]: {% image_buster /assets/img_archive/user_lookup.png %}