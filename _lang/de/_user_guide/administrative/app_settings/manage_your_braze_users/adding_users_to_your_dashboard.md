---
nav_title: "Nutzer:innen"
article_title: Braze-Benutzer verwalten
page_order: 0
page_type: reference
description: "In diesem Artikel wird die Nutzerverwaltung in Ihrem Firmenkonto einschließlich Hinzufügen, Sperren und Löschen von Personen erläutert."

---

# Braze-Benutzer verwalten

> Hier erfahren Sie, wie die Nutzerverwaltung in Ihrem Firmenkonto einschließlich Hinzufügen, Sperren und Löschen von Personen funktioniert.

{% alert note %}
Mehrere Abschnitte auf dieser Seite verweisen auf die Seite **Benutzer des Unternehmens**. Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, heißt **Company Users** **Benutzer verwalten** und befindet sich unter Ihrem Kontosymbol.
{% endalert %}

## Hinzufügen von Braze-Benutzern

Sie benötigen Administratorrechte, um Personen zu Ihrem Braze-Konto hinzuzufügen. 

Um einen neuen Benutzer hinzuzufügen:

1. Gehen Sie zu **Einstellungen** > **Firmenbenutzer**.
2. Klicken Sie auf **\+ Neuen Benutzer hinzufügen**.
3. Geben Sie die erforderlichen Informationen ein, einschließlich E-Mail, Abteilung und [Benutzerrolle]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
Die im Profil eines Benutzers angegebene Abteilung bestimmt, welche Arten von Mitteilungen er von Braze erhält. Auf diese Weise erhält jeder nur die Mitteilungen und Benachrichtigungen, die für seine Nutzung von Braze relevant sind.
{% endalert %}

\![Felder für Nutzer:in.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. Für Benutzer, die keine Administratoren sind, wählen Sie die [Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) auf Unternehmens- und Arbeitsbereichsebene aus, die dieser Benutzer haben soll.

\![Berechtigungen auf Workspace-Ebene mit einem Abschnitt für angepasste Berechtigungsfelder.]({% image_buster /assets/img/add_new_user_3.png %})

### Anforderungen an die E-Mail-Adresse

In einer [Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) verwendete E-Mail Adressen müssen eindeutig sein. Das bedeutet, dass Sie eine Fehlermeldung erhalten, wenn Sie versuchen, eine E-Mail-Adresse hinzuzufügen, die bereits mit einem Benutzer verknüpft ist, der in diesem Fall Zugriff auf einen Arbeitsbereich des Unternehmens hatte oder noch hat. 

Wenn Ihr Team Google Mail verwendet und Sie Probleme beim Hinzufügen einer E-Mail-Adresse haben, können Sie einen Alias erstellen, indem Sie ein Pluszeichen (+) wie "+1" oder "+test" zur E-Mail-Adresse hinzufügen. Zum Beispiel kann `contractor@braze.com` einen Alias von `contractor+1@braze.com` haben. E-Mails an `contractor+1@braze.com` werden weiterhin an `contractor@braze.com` zugestellt, aber der Alias wird als eindeutige E-Mail-Adresse erkannt.

### Kann ich die E-Mail-Adresse für mein Braze-Konto ändern?

Aus Sicherheitsgründen können Benutzer die mit ihrem Braze-Konto verknüpfte E-Mail-Adresse nicht ändern. Wenn ein Benutzer seine E-Mail-Adresse aktualisieren möchte, sollte ein Administrator für ihn [ein neues Konto](#adding-braze-users) mit seiner bevorzugten E-Mail-Adresse erstellen.

## Personen in Braze sperren

Wenn Sie einen Benutzer sperren, wird sein Konto in einen inaktiven Zustand versetzt, in dem er sich nicht mehr anmelden kann, die mit seinem Konto verbundenen Daten jedoch erhalten bleiben. Nur Administratoren können Braze-Benutzer suspendieren oder ihre Suspendierung aufheben.

Um einen Benutzer zu sperren, gehen Sie zu **Einstellungen** > **Firmenbenutzer**, suchen Sie seinen Benutzernamen und wählen Sie <i class="fa-solid fa-user-lock"></i> **Sperren**.

\![Option, um einen Nutzer:in zu sperren.]({% image_buster /assets/img_archive/suspend_user.png %})

Administratoren können einen Benutzer auch sperren, indem sie seinen Namen in der Liste auswählen und in der Fußzeile auf **Benutzer sperren** klicken.

\![Nutzer:innen bei der Bearbeitung der Benutzerdetails suspendieren.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Zuweisung von Nutzer:innen und Verantwortlichkeiten

{% multi_lang_include permissions.md content="Differences" %}

## Löschung von Braze-Benutzern

Um einen Benutzer zu löschen, gehen Sie zu **Einstellungen** > **Firmenbenutzer**, suchen Sie seinen Benutzernamen und wählen Sie <i class="fa fa-trash-can"></i> **Benutzer löschen**.

\![Nutzer:in löschen]({% image_buster /assets/img_archive/delete_user_new.png %})

Mit der Löschung gehen folgende Daten verloren:

- Alle Attribute, die der Benutzer hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Benutzer-ID
- Geschlecht
- Land
- Sprache
- Andere ähnliche Daten

Braze speichert die folgenden Kontodaten:

- Benutzerdefinierte Attribute oder Testdaten, die mit ihrem Konto verbunden sind
- Kampagnen oder Canvases, die sie erstellt haben (der Name des Benutzers erscheint jedoch nicht darin, z. B. in der Spalte **Zuletzt bearbeitet von** )

### Auswirkungen des Löschens eines Dashboard Nutzers:innen

Wenn ein Nutzer:innen des Dashboards gelöscht wird, hat dies keine nennenswerten Auswirkungen auf die von ihm im Dashboard erstellten Assets, wie Kampagnen, Segmente und Canvase. Beachten Sie jedoch, dass im Feld **Erstellt von** für diese Assets anstelle der E-Mail Adresse des gelöschten Nutzers:innen ein Wert "null" angezeigt wird.

Wenn anschließend ein neuer Dashboard-Benutzer mit der gleichen E-Mail Adresse wie der gelöschte Nutzer:innen angelegt wird, wird Braze die vom gelöschten Nutzer:innen angelegten Assets nicht erneut mit dem neuen Nutzer:innen verknüpfen. Der neue Nutzer:innen des Dashboards fängt bei Null an und wird nicht als Ersteller von bestehenden Assets im Dashboard anerkannt.

## Fehlersuche

### "E-Mail ist bereits vergeben", wenn Sie versuchen, eine Nutzer:in hinzuzufügen

Wenn Sie versuchen, einen neuen Nutzer hinzuzufügen und die Fehlermeldung erhalten, dass die E-Mail bereits vergeben ist, Sie den Nutzer:innen aber nicht in Ihrer E-Mail-Liste finden können, existiert dieser Nutzer:innen höchstwahrscheinlich in einer anderen Instanz desselben Braze-Dashboard-Clusters.

Um diesen neuen Nutzer:innen zu erstellen, können Sie einen der folgenden Schritte ausführen:

1. Löschen Sie den Nutzer:innen aus der anderen Instanz, bevor Sie ihn in der neuen Instanz anlegen können, oder
2. Erstellen Sie den Nutzer:in mit einem anderen E-Mail String (z.B. `testing+01@braze.com`) oder einem anderen Nutzer-Alias. 

Wenn Sie die Aktivierung der Nachrichten im Posteingang nicht erhalten, wenn Sie `testing+01@braze.com` verwenden, bestätigen Sie Ihrem IT Team, dass Sie Nachrichten von dieser Art von E-Mail Adresse annehmen können. Einige Administratoren filtern Nachrichten, die an E-Mail-Adressen mit einem `+` gesendet werden.

