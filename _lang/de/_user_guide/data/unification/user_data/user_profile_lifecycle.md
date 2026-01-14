---
nav_title: Nutzerprofil-Lebenszyklus
article_title: Nutzerprofil-Lebenszyklus
page_order: 2
page_type: reference
description: "Dieser referenzierende Artikel beschreibt den Nutzerprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, wie ein Nutzerprofil identifiziert und referenziert werden kann."

---

# Nutzerprofil-Lebenszyklus

> Dieser Artikel beschreibt den Lebenszyklus von Braze-Benutzerprofilen und die verschiedenen Möglichkeiten, Benutzerprofile zu erkennen und darauf zu verweisen. Wenn Sie Ihren Kundenlebenszyklus besser verstehen wollen, sehen Sie sich stattdessen unseren Braze-Lernkurs zur [Abbildung von Nutzer:innen-Lebenszyklen](https://learning.braze.com/mapping-customer-lifecycles) an.

Alle persistenten Daten, die mit einem Benutzer verbunden sind, werden in dessen Benutzerprofil gespeichert. Wenn per API oder nach der Benutzererkennung durch das SDK ein Benutzerprofil erstellt wird, können Sie diesem eine Reihe von Parametern zuweisen, um den jeweiligen Benutzer zu erkennen und auf ihn zu verweisen. 

Diese Parameter umfassen:

* `braze_id` (zugewiesen von Braze)
* `external_id`
* `email`
* `phone`
* Beliebig viele angepasste Nutzer:innen-Aliase, die Sie festlegen

## Anonyme Nutzer:in-Profile

Jeder Nutzer:innen ohne einen bestimmten `external_id` wird als [anonymer Nutzer]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/):in bezeichnet. Das können zum Beispiel Nutzer sein, die Ihre Website besucht, sich aber nicht angemeldet haben, oder Nutzer, die Ihre mobile App heruntergeladen, aber kein Profil erstellt haben.

Wenn ein Benutzer vom SDK erkannt wird, wird zunächst ein anonymes Benutzerprofil mit einer `braze_id` erstellt – einer eindeutigen gerätespezifischen Kennung, die von Braze automatisch zugewiesen wird und nicht bearbeitet werden kann. Dieser Bezeichner kann verwendet werden, um das Nutzerprofil über die [API]({{site.baseurl}}/api/endpoints/user_data/) zu aktualisieren.

## Identifizierte Nutzer:innen-Profile

Kann ein Benutzer von Ihrer App erkannt werden (weil er eine Benutzer-ID oder E-Mail-Adresse angibt), sollten Sie seinem Profil mit der Methode `changeUser` [(Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)) eine `external_id` zuzuweisen. Denn mit einer `external_id` können Sie das Benutzerprofil auf mehreren Geräten wiedererkennen.

Zu den weiteren Vorteilen der Verwendung von `external_id` gehören folgende: 

- Sorgen Sie für eine einheitliche Benutzererfahrung auf allen Geräten und Plattformen (senden Sie also z. B. keine Benachrichtigungen an Android-Tablets passiver Benutzer, wenn diese die iPhone-App nutzen).
- Verbessern Sie die Genauigkeit Ihrer Analytics, indem Sie sicherstellen, dass Nutzer:innen nicht jedes Mal ein neues Nutzerprofil erstellen, wenn sie die App deinstallieren und neu installieren oder die App auf einem anderen Gerät installieren.
- Ermöglichen Sie den Import von Nutzerdaten aus Quellen außerhalb der App mit Hilfe der [Endpunkte für Nutzerdaten]({{site.baseurl}}/api/endpoints/user_data/) und Targeting von Nutzer:innen mit transaktionsbezogenen Nachrichten über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/).
- Suchen Sie nach einzelnen Nutzern mit den Test-[Filtern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) in der Segmentierung und unter [**Benutzer suchen**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

### Überlegungen zu externen IDs

{% alert warning %}
Weisen Sie Benutzerprofilen erst dann eine `external_id` zu, wenn Sie sie eindeutig identifizieren können. Wenn Sie einen Benutzer identifiziert haben, können Sie ihn nicht mehr in die Anonymität zurückversetzen.
<br><br>
Ein `external_id` kann über den [Endpunkt`/users/external_ids/rename` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) aktualisiert werden. Wenn Sie jedoch versuchen, während der Sitzung eines Nutzers:in ein anderes `external_id` einzustellen, wird ein neues Nutzerprofil erstellt, das mit dem neuen `external_id` verknüpft ist. Es werden keine Daten zwischen den beiden Profilen ausgetauscht.
{% endalert %} 

#### Risiko der Verwendung einer E-Mail oder einer gehashten E-Mail als externe ID

Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID von Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, dass Sie die potenziellen Risiken für den Datenschutz und die Datensicherheit berücksichtigen.

- **Erratene Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko der Ausbeutung:** Wenn ein böswilliger Nutzer:innen seinen Webbrowser so verändert, dass er die E-Mail-Adresse einer anderen Person als externe ID verwendet, kann er möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.

### Was passiert, wenn Sie anonyme Nutzer:innen identifizieren

Wenn Sie anonyme Benutzer erkennen, kann eines von zwei Szenarien eintreten:

1) **Ein anonymer Nutzer:in wird zu einem neuen Bezeichner:** <br>Wenn die `external_id` noch nicht in Braze existiert, wird der anonyme Benutzer zu einem neu erkannten Benutzer und behält alle Attribute und den Verlauf des anonymen Benutzers bei. 

2) **Ein anonymer Benutzer wird als ein bereits existierender Benutzer erkannt:** <br>Wenn die `external_id` bereits in Braze vorhanden ist, wurde dieser Benutzer bereits auf andere Weise erkannt, etwa durch ein anderes Gerät (wie ein Tablet) oder importierte Benutzerdaten. 

Mit anderen Worten: Sie haben bereits ein Nutzerprofil für diese Nutzer:in. In dieser Instanz wird Braze Folgendes tun:
1. Lassen Sie den anonymen Benutzer verwaisen.
2. Führen Sie [bestimmte Felder des Benutzerprofils]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior), die nicht bereits im Profil des erkannten Benutzers vorhanden sind, mit dem anonymen Profil zusammen.
3. Entfernen Sie das anonyme Profil aus Ihrem Benutzerverzeichnis, damit die Benutzerzahlen nicht aufgebläht werden.

Wenn sowohl der anonyme Nutzer:in als auch der bekannte Nutzer:in einen Vornamen haben, wird der Vorname des bekannten Nutzers beibehalten. Wenn der bekannte Nutzer einen Nullwert und der anonyme Nutzer einen Wert hat, wird der Wert des anonymen Nutzers:in das Profil des bekannten Nutzers übernommen, wenn der Wert unter diese [spezifischen Felder des Nutzerprofils]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) fällt.

Informationen darüber, wie Sie `external_id` gegen ein Nutzerprofil eintauschen können, finden Sie in unserer Dokumentation[(iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

## Nutzer-Aliasse

Wenn Sie auf Benutzer mit anderen Kennungen als der Braze `external_id` verweisen möchten, legen Sie entsprechende Pseudonyme für die Benutzerprofile fest. Jeder Alias, der für ein Nutzerprofil festgelegt wird, wird zusätzlich zu dem des Nutzers `braze_id` oder `external_id` verwendet und ersetzt es nicht. Die Anzahl der Aliasnamen, die Sie für ein Nutzerprofil festlegen können, ist unbegrenzt.

Diese funktionieren wie ein Schlüssel-Wert-Paar, das aus zwei Teilen besteht: einem `alias_label`, das den Schlüssel des Beinamens festlegt, und einem `alias_name`, das den Wert definiert. Ein `alias_name` für ein einzelnes Label muss in Ihrer Benutzerbasis eindeutig sein (genau wie die `external_id`). Wenn Sie versuchen, ein zweites Nutzerprofil mit einer bereits existierenden Kombination aus Bezeichnung und Name zu aktualisieren, wird das Nutzerprofil nicht aktualisiert.

### Update der Nutzer:innen-Aliase

Ein Alias kann mit einem neuen Namen für ein bestimmtes Etikett aktualisiert werden, nachdem es gesetzt wurde, indem Sie entweder unsere [Endpunkte für Nutzerdaten]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) verwenden oder einen neuen Namen über das SDK übergeben. Der Nutzer-Alias wird dann beim Exportieren der Daten des Nutzers:innen sichtbar sein.

![Zwei unterschiedliche Nutzerprofile für verschiedene Nutzer:innen mit demselben Nutzer-Alias-Label, aber unterschiedlichen Alias-Namen]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Anonyme Benutzer verschlagworten

Mit Pseudonymen können Sie auch anonyme Benutzer mit einem Bezeichner versehen. Wenn ein Nutzer Ihrer E-Commerce-Website beispielsweise seine E-Mail-Adresse mitteilt, sich aber noch nicht registriert hat, kann die E-Mail-Adresse als Alias für diesen anonymen Nutzer:in verwendet werden. Diese Benutzer können dann über ihre Pseudonyme exportiert oder über die API referenziert werden.

### Verhalten von Aliasen auf anonymen Nutzer:in-Profilen

Wenn ein anonyme:r Nutzer:in Profil mit einem Bezeichner zu einem späteren Zeitpunkt mit `external_id` erkannt wird, wird er wie ein normales identifiziertes Nutzerprofil behandelt, behält aber seinen bestehenden Bezeichner bei und kann weiterhin mit diesem referenziert werden.

### Setzen von Aliasen auf bekannte Nutzer:innen-Profile

Benutzer-Aliase können auch für bekannte Benutzerprofile eingerichtet werden, um diese mit einer externen ID zu referenzieren. Ein Benutzer kann z. B. bereits eine ID eines BI-Tools besitzen (etwa aus Amplitude), auf die Sie in Braze verweisen möchten.

Wie Sie einen Nutzer-Alias einrichten, erfahren Sie in unserer Dokumentation für jede Plattform[(iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

![Ein Flow Chart des Nutzerprofil-Lebenszyklus in Braze. Wenn changeUser() für einen anonymen Nutzer:in aufgerufen wird, wird dieser Nutzer zu einem identifizierten Nutzer und die Daten werden in sein identifiziertes Nutzerprofil migriert. Der identifizierte Nutzer:innen hat eine Braze ID und eine externe ID. Wenn zu diesem Zeitpunkt ein zweiter anonymer Benutzer changeUser() aufruft, werden Benutzerdatenfelder, die bei dem erkannten Benutzer noch nicht vorhanden sind, zusammengeführt. Wenn der Identifizierte Nutzer einen Alias zu seinem bestehenden Nutzerprofil hinzugefügt hat, sind keine Daten betroffen, aber er wird zu einem Identifizierten Nutzer mit Alias. Wenn ein dritter anonymer Nutzer mit demselben Alias-Label wie der Identifizierte Nutzer, aber einem anderen Alias-Namen, dann changeUser() aufruft, werden alle Felder, die beim Identifizierten Nutzer nicht vorhanden sind, zusammengeführt und das Alias-Label im Profil des Identifizierten Nutzers bleibt erhalten.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Sie fragen sich, wie das bei Ihren Benutzerprofilen aussehen könnte? Unter [Best Practices]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) finden Sie hilfreiche Tipps zur Erfassung von Benutzerdaten.
{% endalert %}

## Fortgeschrittener Anwendungsfall

Sie können über unser SDK und unsere API mit Hilfe der [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) einen neuen Nutzer-Alias für bestehende identifizierte Nutzerprofile festlegen. Pseudonyme für bestehende unbekannte Benutzerprofile können nicht über die API festgelegt werden.

Dabei werden auch die Nutzer:innen-Alias zusammengeführt. Wenn sowohl der zu verwaisende Benutzer als auch der Zielbenutzer einen Beinamen mit demselben Label besitzen, wird nur der des Zielbenutzers beibehalten.

Die Deinstallation und Neuinstallation einer App erzeugt eine neue anonyme `braze_id` für diesen Nutzer:in.

### Fehlerbehebung mit Nutzer:innen IDs

Um Benutzer zu Testzwecken in Ihrem Dashboard zu finden und zu erkennen, können alle Benutzer-IDs verwendet werden. Um Ihren Nutzer:innen im Braze-Dashboard zu finden, referenzieren Sie auf [Testnutzer:innen hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
Braze sperrt bzw. blockiert Benutzer mit mehr als 5.000.000 Sitzungen ("Dummy-Benutzer") und lässt ihre SDK-Ereignisse außer Acht, da sie meist auf Integrationsfehler zurückgehen. Wenn Sie feststellen, dass dies einem rechtmäßigen Nutzer:in passiert ist, wenden Sie sich an Ihren Braze-Konto Manager:in.
{% endalert %}