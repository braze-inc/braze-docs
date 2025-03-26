---
nav_title: OneTrust
article_title: OneTrust
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und OneTrust, einem Anbieter von Datenschutz- und Sicherheitssoftware, die es Ihnen ermöglicht, den OneTrust Workflow Builder zur Erstellung von Sicherheitsworkflows für Ihr Produkt zu verwenden."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) ist ein Anbieter von Datenschutz- und Sicherheitssoftware, die Ihnen den Überblick verschafft, den Sie brauchen, um Ihre Vertrauenslandschaft besser zu verstehen, die Ihnen die Möglichkeit gibt, aussagekräftige Erkenntnisse zu nutzen, und die Ihnen durch Automatisierung einen Vorsprung vor der Konkurrenz verschafft. 

Die Integration von Braze und OneTrust ermöglicht es Ihnen, den OneTrust Workflow Builder zu verwenden, um Sicherheits-Workflows für Ihr Produkt zu erstellen.
## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| OneTrust-Konto | Ein [OneTrust-Konto](https://www.onetrust.com/), um von dieser Partnerschaft zu profitieren. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den erforderlichen Berechtigungen für den Endpunkt, den Ihre OneTrust-Aktion verwenden wird.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Hartlöt-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die folgende Integration bietet eine Anleitung zur Erstellung eines Workflows zur Aktualisierung der Benutzerzustimmung und eines Workflows zum Löschen von Benutzern. Weitere Einzelheiten zu zusätzlich unterstützten Braze-Endpunkten finden Sie unter [Andere unterstützte Aktionen](#Other-supported-actions).

### Braze-Anmeldeinformationen zu OneTrust hinzufügen

Navigieren Sie im OneTrust **Integrationsmenü** zu **Zugangsdaten** > **Neu hinzufügen**, um den Bildschirm **System auswählen** aufzurufen. Suchen Sie hier **Braze** und klicken Sie dann auf die Schaltfläche **Weiter**.

Folgen Sie den Aufforderungen auf dem Bildschirm **Zugangsdaten eingeben** und geben Sie die folgenden Informationen ein. Speichern Sie Ihre Anmeldedaten, wenn Sie fertig sind.
  - Bezeichnung
  - Stellen Sie den Verbindungstyp auf **Web App** ein
  - Hostname: `<your-braze-instance-url>`
  - **Kopfzeile der Anfrage**:
    - **Autorisierung**: Träger
    - **Inhalt-Typ**: application/json
  - Token: `<your-braze-api-key>`

### Braze als System hinzufügen

#### Schritt 1: Einen Arbeitsablauf erstellen

{% tabs %}
{% tab Update der Benutzerzustimmung %}
1. Navigieren Sie im OneTrust-Integrationsmenü zu **Gallery** > **Braze** > **Add**, um einen neuen Workflow zu erstellen.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Geben Sie einen Namen und eine Benachrichtigungs-E-Mail im Workflow-Modal an. Klicken Sie auf die Schaltfläche **Erstellen**. Bei der Erstellung werden Sie zum Workflow Builder weitergeleitet. Ihr Braze-Workflow wird mit API-Aufrufen und Aktionen bestückt, die zur Bearbeitung von Löschanträgen verwendet werden können. <br><br>
3. Wählen Sie im Workflow Builder die Aktion, die Sie im Workflow auslösen möchten.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab Benutzer-Löschung %}

1. Navigieren Sie im OneTrust-Integrationsmenü zu **Gallery** > **Braze** > **Add**, um einen neuen Workflow zu erstellen.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Geben Sie einen Namen und eine Benachrichtigungs-E-Mail im Workflow-Modal an. Klicken Sie auf die Schaltfläche **Erstellen**. Bei der Erstellung werden Sie zum Workflow Builder weitergeleitet. Ihr Braze-Workflow wird mit API-Aufrufen und Aktionen bestückt, die zur Bearbeitung von Löschanträgen verwendet werden können. <br><br>
3. Wählen Sie im Workflow Builder die Aktion, die Sie im Workflow auslösen möchten.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Schritt 2: Aktion auswählen
{% tabs %}
{% tab Update der Benutzerzustimmung %}

1. Wenn Sie fertig sind, klicken Sie auf **Fertig** und wählen Sie **Aktion hinzufügen**. Beachten Sie, dass die von Ihnen gewählte Aktion davon abhängt, welche Art von Einstellung aktualisiert werden soll und welchen Endpunkt Sie bevorzugen.
- Um die globalen Abonnementeinstellungen eines Benutzers zu aktualisieren, wählen Sie die Aktion **POST Benutzerspur - Attribute**.
- Um die Einstellungen der Abonnementgruppe eines Benutzers zu aktualisieren, wählen Sie die Aktion **POST User Track - Attributes** oder die Aktion **POST Set Users Subscription Group Status**.<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Wählen Sie die gewünschte Aktion, wählen Sie Ihre zuvor erstellten Braze-Anmeldedaten und klicken Sie auf **Weiter**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab Benutzer-Löschung %}

1. Wenn Sie fertig sind, klicken Sie auf **Fertig** und wählen Sie **Aktion hinzufügen**.
- Um einen Benutzer aus Braze zu löschen, wählen Sie die Aktion **POST User Delete Action**.
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Wählen Sie die gewünschte Aktion, wählen Sie Ihre zuvor erstellten Braze-Anmeldedaten und klicken Sie auf **Weiter**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Schritt 3: Körper der Anfrage aktualisieren
{% tabs %}
{% tab Update der Benutzerzustimmung %}

1. Aktualisieren Sie den Textkörper, um alle erforderlichen dynamischen Werte aufzunehmen. Vergewissern Sie sich, dass der Körper der Aktion mit dem [Endpunkt`/users/track` ](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) und dem [Endpunkt`/subscription/status/set` ](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) übereinstimmt.
2. Passen Sie den Workflow mit zusätzlichen Parametern oder bedingter Logik an die Bedürfnisse Ihres Unternehmens an.
3. Wenn Sie die Bearbeitung abgeschlossen haben, klicken Sie auf **Fertig stellen** und dann auf **Aktivieren**, um den Workflow zu aktivieren.

{% alert note %}
Wenn Sie die OneTrust-Workflows verwenden, um die Einstellungen der Abonnementgruppe in Braze zu aktualisieren, muss die `subscription_group_id` mit der ID übereinstimmen, die von Braze bei der Erstellung der Abonnementgruppe festgelegt wurde. Sie können auf die `subscription_group_id` einer Abonnementgruppe zugreifen, indem Sie auf die Seite **Abonnementgruppe** im Braze-Dashboard navigieren.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab Benutzer-Löschung %}

1. Aktualisieren Sie den Textkörper, um alle erforderlichen dynamischen Werte aufzunehmen. Vergewissern Sie sich, dass der Körper der Aktion mit dem [Endpunkt`/users/delete` ]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) übereinstimmt.
2. Wenn Sie mit der Bearbeitung fertig sind, wählen Sie **Fertig stellen** und dann **Aktivieren**, um den Workflow zu aktivieren.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Aktualisieren Sie den Arbeitsablauf für die Beantragung von Daten
1. Wählen Sie im Menü **Automatisierung der Datenschutzrechte** die Option **Workflows**. 
2. Wählen Sie den Workflow, den Sie mit der Braze-Integration aktualisieren möchten. 
3. Wählen Sie die Schaltfläche **Bearbeiten**, um die Bearbeitung zu aktivieren.
4. Wählen Sie dann den Workflow-Schritt, dem Sie die Braze-Integration hinzufügen möchten, und klicken Sie auf **Verbindung hinzufügen**.
5. Fügen Sie den zuvor erstellten Braze-Workflow als Systemunteraufgabe hinzu.

{% endtab %}
{% endtabs %}

## Andere unterstützte Aktionen

Zusätzlich zu den Aktionen **POST User track - Attributes**, **POST Set Users Subscription Group Status** und **POST User Delete** unterstützt Braze weitere Endpunkte, die zur Erstellung benutzerdefinierter Workflows und als Unteraufgaben innerhalb bestehender Workflows verwendet werden können. 

Um eine vollständige Liste der unterstützten Aktionen zu sehen:
1. Klicken Sie in OneTrust in Ihrem **Integrationsmenü** auf **Systeme**. 
2. Wählen Sie das **Braze-System**.
3. Navigieren Sie zur Registerkarte **Aktionen**.

![][7]

[1]: {% image_buster /assets/img/onetrust/onetrust.png %}
[2]: {% image_buster /assets/img/onetrust/onetrust2.png %}
[3]: {% image_buster /assets/img/onetrust/onetrust3.png %}
[4]: {% image_buster /assets/img/onetrust/onetrust4.png %}
[5]: {% image_buster /assets/img/onetrust/onetrust5.png %}
[6]: {% image_buster /assets/img/onetrust/onetrust6.png %}
[7]: {% image_buster /assets/img/onetrust/onetrust7.png %}
[8]: {% image_buster /assets/img/onetrust/onetrust8.png %}
[9]: {% image_buster /assets/img/onetrust/onetrust9.png %}
[10]: {% image_buster /assets/img/onetrust/onetrust10.png %}
