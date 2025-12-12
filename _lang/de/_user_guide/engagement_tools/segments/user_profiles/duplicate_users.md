---
nav_title: Doppelte Benutzer
article_title: Doppelte Benutzer
description: "Erfahren Sie, wie Sie doppelte Benutzer in Ihrem Braze-Dashboard finden und zusammenführen können."
page_order: 0
---

# Doppelte Benutzer

> Erfahren Sie, wie Sie doppelte Benutzer finden und zusammenführen, damit Sie die Effektivität Ihrer Kampagnen und Canvases maximieren können.

{% alert tip %}
Wie Sie doppelte Benutzer mit der Braze REST API zusammenzuführen, erfahren Sie im [Post: Benutzer zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Individuelle Zusammenführung

Wenn eine Benutzersuche doppelte Profile ergibt, können Sie jedes Profil einzeln aus dem Profil des Benutzers im Braze Dashboard zusammenführen.

### Schritt 1: Suche nach einem doppelten Profil

Wählen Sie in Braze **Audience** > **User Search**.

![Die Kachel "Nutzersuche" wird im Navigationsmenü hervorgehoben.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Geben Sie eine eindeutige Kennung für das doppelte Profil ein, z. B. eine E-Mail-Adresse oder Telefonnummer, und wählen Sie dann **Suchen**.

![Die Seite "Nutzersuche" im Braze-Dashboard.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Schritt 2: Duplikate zusammenführen

Um die Zusammenführung zu starten, wählen Sie **Duplikate zusammenführen**.

![Eines der doppelten Profile der Nutzer:in.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Wählen Sie, welches Benutzerprofil Sie behalten und welches Sie zusammenführen möchten, und wählen Sie dann **Profile zusammenführen**. Wiederholen Sie diesen Vorgang, bis Sie alle doppelten Profile zusammengeführt haben.

![Die individuelle Zusammenführungsseite für ein dupliziertes Profil.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Doppelte Benutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}

## Massenhafte Zusammenführung

Wenn Sie doppelte Benutzer stapelweise zusammenführen, sucht Braze nach Profilen mit übereinstimmenden Merkmalen (wie einer E-Mail-Adresse) und deren Daten in dem zuletzt aktualisierten Profil mit einer `external_id` zusammen. Wenn es keine Profile mit einem `external_id` gibt, wird stattdessen das zuletzt aktualisierte Profil ohne `external_id` verwendet.

### Schritt 1: Auf "Zielgruppe verwalten" gehen

Gehen Sie im Braze-Dashboard auf **Zielgruppe** > **Zielgruppe verwalten**.

![Die Kachel "Zielgruppe verwalten" wird im Navigationsmenü hervorgehoben.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Schritt 2: Vorschau der Ergebnisse (optional)

Um eine Vorschau der Ergebnisse zu erhalten, bevor Sie die Duplikate zusammenführen, gehen Sie auf **Doublettenliste erstellen**.

![Die Seite "Zielgruppe verwalten" mit der hervorgehobenen Option "Liste der Duplikate generieren".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze erstellt Ihre Vorschau und sendet sie als CSV-Datei an Ihre E-Mail-Adresse.

![Eine E-Mail von Braze mit einem Link zur generierten CSV-Datei.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

Im folgenden Beispiel verwendet Braze die externe Benutzer-ID, um doppelte Profile zu erkennen und zu entscheiden, welches beibehalten werden soll. Wenn diese Profile zusammengeführt werden, verwendet Braze das Profil mit der externen ID als neues primäres Benutzerprofil.

{% tabs local %}
{% tab example csv file %}
| E-Mail Adresse | Externe ID | Telefonnummer | Braze ID | Bezeichner für Regel | Zu behaltendes Profil | Zusammenzuführendes Profil |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99 | (555) 123-4567 | 65fcaa547f470494d1370 | email | TRUE | FALSE |
| alex@company.com | | (555) 987-6543 | 65fcaa547f47d004d1348 | email | FALSE | TRUE |
| alex@company.com | | (555) 321-0987 | 65fcaa547f47d0049135c | email | FALSE | TRUE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Zusammenführungsverhalten

Braze füllt leere Felder im beibehaltenen Profil mit Werten aus dem zusammengeführten Profil. Eine Liste der Felder, die ausgefüllt werden, finden Sie unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Schritt 3: Doubletten zusammenführen

Wenn Sie mit den Ergebnissen der Vorschau zufrieden sind, gehen Sie auf**Alle Doubletten zusammenführen**.

{% alert warning %}
Doppelte Benutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}

![Die Seite "Zielgruppe verwalten" mit markierter Option "Alle Duplikate zusammenführen".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## Regelbasierte Zusammenführung

Sie können Regeln verwenden, um zu steuern, wie doppelte Profile bei der Zusammenführung behandelt werden, damit stets das relevanteste Benutzerprofil erhalten bleibt. Wenn Sie Regeln festgelegt haben, behält Braze die Profile, die Ihren Kriterien entsprechen.

### Schritt 1: Regeln aufstellen

1. Gehen Sie auf **Zielgruppe** > **Zielgruppe verwalten** > **Regeln bearbeiten**.
2. Wählen Sie im Abschnitt **Beizubehaltende Profile** des Bereichs **Regeln bearbeiten** den **Identifikator** für die Profile, die beim Zusammenführen von Duplikaten beibehalten werden sollen. Dies kann die E-Mail-Adresse oder die Telefonnummer sein.
3. Im Abschnitt **Verknüpfungen auflösen** wählen Sie die Kriterien aus, die bestimmen, wie Verknüpfungen zwischen Profilen mit übereinstimmenden Kriterien von **Profil zu behalten** aufgelöst werden sollen. Sie können Folgendes auswählen:<br>
- **Beheben Sie Verknüpfungen wie**: Erstellungsdatum, Aktualisierungsdatum, Letzte Sitzung
- **Prioritäten setzen**: Neueste, Älteste

![Das Panel "Regeln bearbeiten" mit Abschnitten zum Auswählen von Optionen für "Profil beibehalten" und "Verknüpfungen auflösen".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Sie könnten zum Beispiel das Profil mit der Telefonnummer behalten. Wenn mehrere Benutzer dieselbe Telefonnummer haben, können Sie Verbindungen über das Feld **Aktualisierungsdatum** auflösen und dem zuletzt aktualisierten Benutzer Priorität einräumen.

### Schritt 2: Vorschau der Ergebnisse (optional)

Nachdem Sie Ihre Regeln gespeichert haben, können Sie eine Vorschau auf deren Funktionsweise anzeigen, indem Sie **Liste der Duplikate erstellen** wählen. Braze erstellt Ihre Vorschau und sendet sie als CSV-Datei an Ihre E-Mail-Adresse, aus der hervorgeht, welche Benutzer beibehalten und zusammengeführt würden, wenn Ihre Regeln angewendet würden. 

### Schritt 3: Duplikate zusammenführen

Wenn Sie mit den Ergebnissen der Vorschau zufrieden sind, kehren Sie zur Seite **Zielgruppe verwalten** zurück und gehen Sie auf **Alle Doubletten zusammenführen**.

{% alert warning %}
Doppelte Benutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}

## Geplante Zusammenführung

Ähnlich wie bei der regelbasierten Zusammenführung können Sie bei der zeitgesteuerten Zusammenführung die Zusammenführung von Nutzerprofilen auf täglicher Basis anhand vorkonfigurierter Regeln automatisieren.

![Die Seite "Zielgruppe verwalten" mit dem Button "Zeitplan".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Nach dem Einschalten des Features weist Braze automatisch einen Zeitschlitz zu, um den Zusammenführungsprozess täglich um ca. 12 Uhr in der Zeitzone des Nutzer:innen durchzuführen. Sie können die geplante Zusammenführung jederzeit deaktivieren. Braze benachrichtigt die Administratoren Ihres Workspace 24 Stunden vor der geplanten Zusammenführung und gibt Ihnen eine Erinnerung und Zeit, um die Konfiguration zu überprüfen.

{% alert warning %}
Doppelte Benutzerprofile können nach dem Zusammenführen nicht wiederhergestellt werden.
{% endalert %}
