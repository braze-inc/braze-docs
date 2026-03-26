---
nav_title: Nutzerprofil-Lebenszyklus
article_title: Nutzerprofil-Lebenszyklus
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt den Nutzerprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, wie ein Nutzerprofil identifiziert und referenziert werden kann."

---

# Nutzerprofil-Lebenszyklus

> Dieser Artikel beschreibt den Nutzerprofil-Lebenszyklus von Braze und die verschiedenen Möglichkeiten, ein Nutzerprofil zu identifizieren und zu referenzieren. Wenn Sie Ihren Kundenlebenszyklus besser verstehen möchten, sehen Sie sich stattdessen unseren Braze-Lernkurs zur [Abbildung von Nutzer:innen-Lebenszyklen](https://learning.braze.com/mapping-customer-lifecycles) an.

Alle persistenten Daten, die mit einer Nutzer:in verbunden sind, werden in deren Nutzerprofil gespeichert. Nachdem ein Nutzerprofil erstellt wurde – entweder über die API oder nachdem eine Nutzer:in vom SDK erkannt wurde – können Sie diesem Profil eine Reihe von Parametern zuweisen, um die Nutzer:in zu identifizieren und zu referenzieren.

Diese Parameter umfassen:

* `braze_id` (zugewiesen von Braze)
* `external_id`
* `email`
* `phone`
* Beliebig viele angepasste Nutzer-Aliasse, die Sie festlegen

## Anonyme Nutzer:innen-Profile

Jede Nutzer:in ohne eine zugewiesene `external_id` wird als [anonyme:r Nutzer:in]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) bezeichnet. Das können zum Beispiel Nutzer:innen sein, die Ihre Website besucht, sich aber nicht angemeldet haben, oder Nutzer:innen, die Ihre mobile App heruntergeladen, aber kein Profil erstellt haben.

Wenn eine Nutzer:in zunächst vom SDK erkannt wird, wird ein anonymes Nutzerprofil mit einer zugehörigen `braze_id` erstellt – einem eindeutigen, gerätespezifischen Bezeichner, der von Braze automatisch zugewiesen wird und nicht bearbeitet werden kann. Dieser Bezeichner kann verwendet werden, um das Nutzerprofil über die [API]({{site.baseurl}}/api/endpoints/user_data/) zu aktualisieren.

## Identifizierte Nutzer:innen-Profile

Sobald eine Nutzer:in in Ihrer App erkennbar ist (durch Angabe einer Nutzer-ID oder E-Mail-Adresse), empfehlen wir, dem Nutzerprofil mit der Methode `changeUser` ([Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)) eine `external_id` zuzuweisen. Mit einer `external_id` können Sie dasselbe Nutzerprofil über mehrere Geräte hinweg identifizieren.

Zu den weiteren Vorteilen der Verwendung einer `external_id` gehören:

- Bieten Sie eine konsistente Nutzererfahrung über mehrere Geräte und Plattformen hinweg (senden Sie z. B. keine Benachrichtigungen für inaktive Nutzer:innen an das Android-Tablet, wenn diese die iPhone-App regelmäßig nutzen).
- Verbessern Sie die Genauigkeit Ihrer Analytics, indem Sie sicherstellen, dass Nutzer:innen nicht jedes Mal ein neues Nutzerprofil erstellen, wenn sie die App deinstallieren und neu installieren oder auf einem anderen Gerät installieren.
- Ermöglichen Sie den Import von Nutzerdaten aus Quellen außerhalb der App mithilfe der [Endpunkte für Nutzerdaten]({{site.baseurl}}/api/endpoints/user_data/) und das Targeting von Nutzer:innen mit transaktionsbezogenen Nachrichten über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/).
- Suchen Sie nach einzelnen Nutzer:innen mithilfe unserer Test-[Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) in der Segmentierung und auf der Seite [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

### Überlegungen zu externen IDs

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### Risiko der Verwendung einer E-Mail oder einer gehashten E-Mail als externe ID

Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID von Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit zu berücksichtigen.

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko des Missbrauchs:** Wenn eine böswillige Nutzer:in ihren Webbrowser so verändert, dass die E-Mail-Adresse einer anderen Person als externe ID gesendet wird, könnte sie möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.

### Was passiert, wenn Sie anonyme Nutzer:innen identifizieren

Wenn Sie anonyme Nutzer:innen identifizieren, kann eines von zwei Szenarien eintreten:

1) **Eine anonyme Nutzer:in wird zu einer neuen identifizierten Nutzer:in:** <br>Wenn die `external_id` noch nicht in Braze existiert, wird die anonyme Nutzer:in zu einer neu identifizierten Nutzer:in und behält alle Attribute und den Verlauf des anonymen Profils bei.

2) **Eine anonyme Nutzer:in wird als bereits existierende Nutzer:in erkannt:** <br>Wenn die `external_id` bereits in Braze vorhanden ist, wurde diese Nutzer:in zuvor auf andere Weise im System identifiziert, etwa über ein anderes Gerät (wie ein Tablet) oder importierte Nutzerdaten.

Mit anderen Worten: Sie haben bereits ein Nutzerprofil für diese Nutzer:in. In diesem Fall wird Braze Folgendes tun:
1. Das anonyme Nutzerprofil verwaisen lassen
2. [Bestimmte Felder des Nutzerprofils]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior), die noch nicht im identifizierten Nutzerprofil vorhanden sind, aus dem anonymen Profil zusammenführen
3. Das anonyme Profil aus Ihrer Nutzerbasis entfernen, damit die Nutzerzahlen nicht aufgebläht werden

Wenn sowohl die anonyme Nutzer:in als auch die bekannte Nutzer:in einen Vornamen haben, wird der Vorname der bekannten Nutzer:in beibehalten. Wenn die bekannte Nutzer:in einen Nullwert hat und die anonyme Nutzer:in einen Wert, wird der Wert der anonymen Nutzer:in in das Profil der bekannten Nutzer:in übernommen, sofern der Wert unter diese [spezifischen Felder des Nutzerprofils]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) fällt.

{% alert important %}
Nicht alle Daten werden aus dem anonymen Profil zusammengeführt. Push-Token und der Nachrichtenverlauf werden übertragen, und angepasste Attribute, angepasste Events sowie der Kaufverlauf aus dem anonymen Profil werden nur dann in die identifizierte Nutzer:in übernommen, wenn diese Felder im identifizierten Nutzerprofil noch nicht vorhanden sind. Bei widersprüchlichen Daten werden die Werte der identifizierten Nutzer:in beibehalten. Unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) finden Sie die vollständige Liste der Felder, die übertragen bzw. nicht übertragen werden.
{% endalert %}

Informationen zum Festlegen einer `external_id` für ein Nutzerprofil finden Sie in unserer Dokumentation ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

{% alert note %}
Verwaiste Nutzer:innen sind nicht berechtigt, Nachrichten zu empfangen.
{% endalert %}

## Nutzer-Aliasse

Um Nutzer:innen mit anderen Bezeichnern als der Braze `external_id` zu referenzieren, können Sie Nutzer-Aliasse für ein Nutzerprofil festlegen. Jeder Alias, der für ein Nutzerprofil festgelegt wird, wirkt zusätzlich zur `braze_id` oder `external_id` der Nutzer:in und ersetzt diese nicht. Die Anzahl der Aliasse, die Sie für ein Nutzerprofil festlegen können, ist unbegrenzt.

Jeder Alias funktioniert als Schlüssel-Wert-Paar, das aus zwei Teilen besteht: einem `alias_label`, das den Schlüssel des Alias definiert, und einem `alias_name`, das den Wert definiert. Ein `alias_name` für ein einzelnes Label muss in Ihrer Nutzerbasis eindeutig sein (genau wie bei der `external_id`). Wenn Sie versuchen, ein zweites Nutzerprofil mit einer bereits existierenden Kombination aus Label und Name zu aktualisieren, wird das Nutzerprofil nicht aktualisiert.

### Aktualisieren von Nutzer-Aliassen

Ein Alias kann mit einem neuen Namen für ein bestimmtes Label aktualisiert werden, nachdem er entweder über unsere [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) festgelegt oder ein neuer Name über das SDK übermittelt wurde. Der Nutzer-Alias wird dann beim Exportieren der Daten dieser Nutzer:in sichtbar sein.

![Zwei verschiedene Nutzerprofile für separate Nutzer:innen mit demselben Nutzer-Alias-Label, aber unterschiedlichen Alias-Namen]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Anonyme Nutzer:innen taggen

Mit Nutzer-Aliassen können Sie auch anonyme Nutzer:innen mit einem Bezeichner versehen. Wenn eine Nutzer:in Ihrer E-Commerce-Website beispielsweise ihre E-Mail-Adresse mitteilt, sich aber noch nicht registriert hat, kann die E-Mail-Adresse als Alias für diese anonyme Nutzer:in verwendet werden. Diese Nutzer:innen können dann über ihre Aliasse exportiert oder über die API referenziert werden.

### Verhalten von Aliassen bei anonymen Nutzer:innen-Profilen

Wenn ein anonymes Nutzerprofil mit einem Alias zu einem späteren Zeitpunkt mit einer `external_id` erkannt wird, wird es wie ein normales identifiziertes Nutzerprofil behandelt, behält aber seinen bestehenden Alias bei und kann weiterhin über diesen referenziert werden.

### Suche nach einem Nutzer-Alias

Wenn Sie den Alias-Namen und das Label einer Nutzer:in kennen, können Sie die Nutzer:in unter **Nutzer:innen suchen** im Format `alias_label:alias_name` finden. Wenn Sie beispielsweise ein Alias-only-Profil mit dem Namen `alias_name: bobby_alias` und dem Label `alias_label: m4pzOndtA-CnO0u` haben, können Sie diese Nutzer:in finden, indem Sie `m4pzOndtA-CnO0u:bobby_alias` eingeben.

Wenn Sie diese Informationen nicht kennen, können Sie den Endpunkt [`Export user profile by identifier`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) aufrufen und den Nutzer-Alias in der API-Antwort finden.

### Aliasse für bekannte Nutzer:innen-Profile festlegen

Ein Nutzer-Alias kann auch für ein bekanntes Nutzerprofil festgelegt werden, um eine bekannte Nutzer:in über eine andere extern bekannte ID zu referenzieren. Eine Nutzer:in kann beispielsweise eine Business-Intelligence-Tool-ID (wie eine Amplitude-ID) haben, auf die Sie in Braze verweisen möchten.

Informationen zum Festlegen eines Nutzer-Alias finden Sie in unserer Dokumentation für jede Plattform ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

![Ein Flussdiagramm des Nutzerprofil-Lebenszyklus in Braze. Wenn changeUser() für eine anonyme Nutzer:in aufgerufen wird, wird diese zu einer identifizierten Nutzer:in und die Daten werden in das identifizierte Nutzerprofil migriert. Die identifizierte Nutzer:in hat eine Braze-ID und eine externe ID. Wenn zu diesem Zeitpunkt für eine zweite anonyme Nutzer:in changeUser() aufgerufen wird, werden Nutzerdatenfelder, die bei der identifizierten Nutzer:in noch nicht vorhanden sind, zusammengeführt. Wenn die identifizierte Nutzer:in einen Alias zu ihrem bestehenden Nutzerprofil hinzugefügt hat, sind keine Daten betroffen, aber sie wird zu einer identifizierten Nutzer:in mit Alias. Wenn eine dritte anonyme Nutzer:in mit demselben Alias-Label wie die identifizierte Nutzer:in, aber einem anderen Alias-Namen, dann changeUser() aufruft, werden alle Felder, die bei der identifizierten Nutzer:in nicht vorhanden sind, zusammengeführt und das Alias-Label im Profil der identifizierten Nutzer:in bleibt erhalten.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Sie fragen sich, wie das beim Nutzerprofil-Lebenszyklus Ihrer Kund:innen aussehen könnte? Unter [Best Practices]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) finden Sie hilfreiche Tipps zur Datenerfassung.
{% endalert %}

## Fortgeschrittener Anwendungsfall

Sie können über unser SDK und unsere API mithilfe der [Nutzerdaten-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) einen neuen Nutzer-Alias für bestehende identifizierte Nutzerprofile festlegen. Nutzer-Aliasse können jedoch nicht über die API für ein bestehendes unbekanntes Nutzerprofil festgelegt werden.

Die Nutzer-Aliasse werden dabei ebenfalls zusammengeführt. Wenn jedoch sowohl die zu verwaisende Nutzer:in als auch die Zielnutzer:in einen Alias mit demselben Label besitzen, wird nur der Alias der Zielnutzer:in beibehalten.

Die Deinstallation und Neuinstallation einer App erzeugt eine neue anonyme `braze_id` für diese Nutzer:in.

### Fehlerbehebung mit Nutzer-IDs

Alle Nutzer-IDs können verwendet werden, um Nutzer:innen in Ihrem Dashboard zu Testzwecken zu finden und zu identifizieren. Um Ihre Nutzer:in im Braze-Dashboard zu finden, lesen Sie [Testnutzer:innen hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
Braze sperrt bzw. blockiert Nutzer:innen mit mehr als 5.000.000 Sitzungen („Dummy-Nutzer:innen") und nimmt deren SDK-Events nicht mehr auf, da diese in der Regel auf eine fehlerhafte Integration zurückzuführen sind. Sollten Sie feststellen, dass dies bei einer legitimen Nutzer:in der Fall ist, wenden Sie sich bitte an Ihren Braze Account Manager.
{% endalert %}