---
nav_title: Best Practices bei der Datenerfassung
article_title: Best Practices bei der Datenerfassung
page_order: 3.1
page_type: reference
description: "Der folgende Artikel klärt Sie über verschiedene Methoden und bewährte Verfahren zur Erfassung neuer und bestehender Nutzer:innen-Daten auf."

---

# Best Practices bei der Datenerfassung

> Zu wissen, wann und wie Nutzerdaten für bekannte und unbekannte Nutzer:innen erfasst werden, kann eine Herausforderung darstellen, wenn man sich den Lebenszyklus des Nutzerprofils Ihrer Kund:innen vorstellt. Dieser Artikel erläutert die verschiedenen Methoden und bewährten Verfahren zur Erfassung neuer und bestehender Nutzer:innen, indem er Sie durch einen Anwendungsfall führt.

Das folgende Beispiel ist ein Anwendungsfall für die E-Mail-Erfassung, aber die Logik gilt für viele verschiedene Szenarien der Datenerfassung. In diesem Beispiel gehen wir davon aus, dass Sie bereits ein Registrierungsformular oder eine Möglichkeit zur Erfassung von Nutzer:innen integriert haben. 

Nachdem ein Nutzer Ihnen Informationen zur Verfügung gestellt hat, empfehlen wir Ihnen, zu überprüfen, ob die Daten bereits in Ihrer Datenbank vorhanden sind, und gegebenenfalls ein Nutzer-Alias-Profil zu erstellen oder das vorhandene Nutzerprofil zu aktualisieren.

Wenn ein unbekannter Nutzer:innen Ihre Website besucht und zu einem späteren Zeitpunkt ein Konto erstellt oder sich durch eine E-Mail-Registrierung identifiziert, muss das Zusammenführen von Profilen sorgfältig gehandhabt werden. Je nach der Methode, mit der Sie die Zusammenführung vornehmen, werden möglicherweise nur Alias-Nutzerdaten oder anonyme Nutzer:in überschrieben.

## Erfassen von Nutzerdaten über ein Internet-Formular

### Schritt 1: Prüfen Sie, ob der Nutzer:in existiert

Wenn ein Nutzer:innen Inhalte über ein Webformular eingibt, prüfen Sie, ob in Ihrer Datenbank bereits eine Nutzer:in mit dieser E-Mail existiert. Es gibt zwei Möglichkeiten, dies zu tun:

- **Prüfen Sie die interne Datenbank (empfohlen):** Wenn Sie über einen externen Datensatz oder eine externe Datenbank verfügen, der/die die angegebenen Nutzer:innen enthält und außerhalb von Braze existiert, referenzieren Sie diesen/diese zum Zeitpunkt der Übermittlung der E-Mail oder der Erstellung des Kontos, um zu bestätigen, dass die Informationen nicht bereits erfasst wurden.
- **[`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):** Wenn Sie `email` als Bezeichner verwenden, wird ein neues Nutzerprofil erstellt, falls die E-Mail-Adresse noch nicht vorhanden ist.

### Schritt 2: Nutzer:innen anmelden oder aktualisieren

- **Wenn ein:e Nutzer:in vorhanden ist:**
  - Legen Sie kein neues Profil an.
  - Protokollieren Sie ein angepasstes Attribut (z. B. `newsletter_subscribed: true`) im Nutzerprofil, um anzuzeigen, dass der oder die Nutzer:in seine oder ihre E-Mail über ein Newsletter-Abonnement übermittelt hat. Wenn mehrere Braze Nutzerprofile mit der gleichen E-Mail Adresse existieren, werden alle Profile exportiert.<br><br>
- **Wenn ein Nutzer:in nicht existiert:**
  - Erstellen Sie ein reines Alias-Profil über den [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Dieser Endpunkt akzeptiert ein [`user_alias`-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/) und erstellt ein reines Alias-Profil, wenn `update_existing_only` auf `false` festgelegt ist. Legen Sie die E-Mail des Nutzers oder der Nutzerin als Nutzer-Alias fest, um diese:n Nutzer:in in Zukunft zu referenzieren (da der oder die Nutzer:in keine `external_id` hat).

![Diagramm zum Update eines Nutzer:in-Profils, das nur einen Alias enthält. Ein Nutzer:in gibt seine E-Mail Adresse und ein angepasstes Attribut, seinen Code, auf einer Marketing Landing Page ein. Ein Pfeil, der von der Startseite der Erfassung zu einem Nutzerprofil mit Aliasnamen zeigt, zeigt eine Braze-API-Anfrage an den Endpunkt „Nutzer:in verfolgen“, wobei der Anfragetext den Aliasnamen, die Aliasbezeichnung, die E-Mail-Adresse und die Postleitzahl des Nutzers oder der Nutzerin enthält. Das Profil hat das Label „Nur in Braze erstellte:r Alias-Nutzer:in“ mit den Attributen aus dem Anfragetext, um die Daten anzuzeigen, die im neu erstellten Profil wiedergegeben werden.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Erfassen von Nutzer-E-Mails über ein Formular zur E-Mail-Erfassung

Verwenden Sie ein Formular zur E-Mail-Erfassung, um die Nutzer:innen aufzufordern, ihre E-Mail-Adresse anzugeben, die ihrem Nutzerprofil hinzugefügt wird. Weitere Informationen zum Einrichten dieses Formulars finden Sie unter [E-Mail-Erfassungsformular]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/).
 
## Identifizierung von Nutzer:innen, die nur über einen Bezeichner verfügen

Bei der Identifizierung von Nutzer:innen bei der Kontoerstellung können Alias-Nutzer:innen über den [Endpunkt`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) identifiziert und mit einer externen ID versehen werden, indem der oder die Alias-Nutzer:in mit dem bekannten Profil zusammengeführt wird. 

Um zu überprüfen, ob ein:e Nutzer:in nur über einen Alias verfügt, [prüfen Sie, ob der oder die Nutzer:in](#step-1-check-if-user-exists) in Ihrer Datenbank [existiert](#step-1-check-if-user-exists). 
- Wenn ein externer Datensatz existiert, können Sie den Endpunkt `/users/identify/` aufrufen. 
- Wenn der [`/users/export/id`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) eine `external_id` zurückgibt, können Sie den Endpunkt `/users/identify/` aufrufen.
- Wenn der Endpunkt nichts zurückgibt, sollte der Aufruf von `/users/identify/` nicht durchgeführt werden.

## Erfassen von Nutzerdaten, wenn nur Alias-Nutzerinformationen bereits vorhanden sind

Wenn ein:e Nutzer:in ein Konto erstellt oder sich per E-Mail-Anmeldung identifiziert, können Sie die Profile zusammenführen. Eine Liste der Felder, die zusammengeführt werden können, finden Sie unter [Verhalten bei der Zusammenführung von Updates]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).

### Zusammenführen von doppelten Nutzerprofilen

Wenn Ihre Nutzerdaten immer umfangreicher werden, können Sie doppelte Nutzerprofile über das Braze-Dashboard zusammenführen. Diese doppelten Profile müssen mit der gleichen Suchanfrage gefunden werden. Weitere Informationen über das Duplizieren von Nutzer:innen-Profilen finden Sie unter [Profile zusammenführen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles).

Sie können auch den [Endpunkt Nutzer:innen zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) verwenden, um ein Nutzerprofil mit einem anderen zusammenzuführen. 

{% alert note %}
Nachdem die Nutzerprofile zusammengeführt wurden, kann diese Aktion nicht mehr rückgängig gemacht werden.
{% endalert %}

## Zusätzliche Ressourcen
- Lesen Sie unseren Artikel über den [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) von Braze, um weitere Informationen zu erhalten.<br>
- Sehen Sie sich unsere Dokumentation zum Festlegen von Nutzer:innen und zum Aufrufen der Methode `changeUser()` für [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention) und [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) an.

