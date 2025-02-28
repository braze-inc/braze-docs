---
nav_title: Fehlende Push-Benachrichtigungen
article_title: Fehlende Push-Benachrichtigungen
page_order: 3

page_type: solution
description: "Dieser Hilfeartikel führt Sie durch die Schritte zur Fehlerbehebung, die Sie unternehmen können, wenn Benutzer Ihre Push-Benachrichtigungen nicht erhalten."
channel: push
---
# Fehlende Push-Benachrichtigungen

Haben Sie Probleme bei der Zustellung von Push-Benachrichtigungen? Es gibt eine Reihe von Schritten, die Sie unternehmen können, um dieses Problem zu beheben, indem Sie die:

* [Push-Abonnementstatus](#push-subscription-status)
* [Segment](#segment)
* [Kappen für Push-Benachrichtigungen](#push-notification-caps)
* [Preisgrenzen](#rate-limits)
* [Status der Kontrollgruppe](#control-group-status)

### Push-Abonnementstatus

Überprüfen Sie Ihr Benutzerprofil auf der Registerkarte [Engagement][1] im Abschnitt **Benutzerprofil**, um zu sehen, ob Sie aktiv für Push für den Arbeitsbereich, den Sie testen, registriert sind. Wenn Sie für mehrere Apps registriert sind, werden diese im Feld **Push registriert für** aufgeführt:

![Push registriert für][2]

Sie können die Benutzerprofile auch über die Export-Endpunkte von Braze exportieren:
- [Benutzer nach Kennung][12]
- [Benutzer nach Segment][13]

Jeder der beiden Endpunkte gibt ein Push-Token-Objekt zurück, das Informationen zur Push-Aktivierung pro Gerät enthält.

### Segment

Vergewissern Sie sich, dass Sie in das Segment fallen, auf das Sie abzielen (wenn es sich um eine Live-Kampagne und nicht um einen Test handelt). Im **Benutzerprofil** sehen Sie eine Liste der Segmente, in die der Benutzer derzeit fällt. Denken Sie daran, dass sich diese Variable ständig ändert, da die Segmentierung in Echtzeit aktualisiert wird.

![Liste der Segmente][3]

### Kappen für Push-Benachrichtigungen

Überprüfen Sie die globalen Frequenzgrenzen. Es ist möglich, dass Sie die Push-Benachrichtigung nicht erhalten haben, weil in Ihrem Arbeitsbereich eine globale Frequenzbegrenzung eingerichtet ist und Sie die Obergrenze für Push-Benachrichtigungen für den angegebenen Zeitraum bereits erreicht haben.

Sie können dies tun, indem Sie [Globale Frequenzbegrenzung][4] im Dashboard aktivieren. Wenn die Kampagne so eingestellt ist, dass die Häufigkeitsbegrenzung eingehalten wird, sind eine Reihe von Benutzern von diesen Einstellungen betroffen

![Details zur Kampagne][5]

### Preisgrenzen

Wenn Sie für Ihre Kampagne oder Ihr Canvas ein Ratenlimit festgelegt haben, kann es sein, dass Sie keine Nachrichten mehr erhalten, weil Sie dieses Limit überschritten haben. Weitere Informationen finden Sie unter [Ratenbegrenzung][9].

### Status der Kontrollgruppe

Wenn es sich um eine Ein-Kanal-Kampagne oder ein Canvas mit einer Kontrollgruppe handelt, ist es möglich, dass Sie in die Kontrollgruppe fallen.

  1. Prüfen Sie in der [Variantenverteilung][6], ob es eine Kontrollgruppe gibt.
  2. Wenn ja, erstellen Sie eine Segmentfilterung für [in der Kampagnensteuerungsgruppe][7] dann [exportieren Sie das Segment][8] und überprüfen Sie, ob Ihre Benutzer-ID in dieser Liste enthalten ist.

### Gültiges Push-Token
Ein Push-Token ist eine Kennung, die Absender verwenden, um bestimmte Geräte mit einer Push-Benachrichtigung anzusprechen. Wenn das Gerät also kein gültiges Push-Token hat, gibt es keine Möglichkeit, eine Push-Benachrichtigung an das Gerät zu senden. 

### Typ der Push-Benachrichtigung

Überprüfen Sie, ob Sie die richtige Art von Push-Benachrichtigung verwenden. Wenn Sie beispielsweise einen FireTV ansprechen möchten, würden Sie eine Kindle-Push-Benachrichtigung und keine Android-Push-Kampagne verwenden. In den folgenden Artikeln finden Sie weitere Informationen zum Verständnis des Braze-Workflows für:
- [Apple Push-Benachrichtigung][10]
- [Firebase Cloud Messaging][11]

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 21\. Januar 2021_

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
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment