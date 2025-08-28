---
nav_title: OneTrust
article_title: OneTrust
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und OneTrust, einem Anbieter von Datenschutz- und Sicherheitssoftware, die es Ihnen erlaubt, mit dem OneTrust Workflow Builder Sicherheitsworkflows für Ihr Produkt zu erstellen."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) ist ein Anbieter von Datenschutz- und Sicherheitssoftware, die Ihnen die Transparenz bietet, die Sie benötigen, um Ihre Vertrauenslandschaft besser zu verstehen, die Ihnen leistungsstarke Insights nutzt und die Ihnen durch Automatisierung einen Vorsprung vor der Konkurrenz verschafft. 

_Diese Integration wird von OneTrust gepflegt._

## Über die Integration

Die Integration von Braze und OneTrust erlaubt es Ihnen, den OneTrust Workflow Builder zu verwenden, um Sicherheits-Workflows für Ihr Produkt zu erstellen.
## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| OneTrust-Konto | Ein [OneTrust-Konto](https://www.onetrust.com/), um von dieser Partnerschaft zu profitieren. |
| Braze API-Schlüssel | Ein REST API-Schlüssel von Braze mit den erforderlichen Berechtigungen für den Endpunkt, den Ihre OneTrust-Aktion verwenden wird.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die folgende Integration bietet eine Anleitung zum Erstellen eines Workflows zum Update der Benutzer:innen und zum Löschen von Benutzern. Weitere Einzelheiten zu zusätzlich unterstützten Endpunkten von Braze finden Sie unter [Andere unterstützte Aktionen](#Other-supported-actions).

### Hinzufügen von Braze Zugangsdaten zu OneTrust

Navigieren Sie im Menü OneTrust **Integrationen** zu **Zugangsdaten** > Button **Neu hinzufügen**, um den Bildschirm **System auswählen** aufzurufen. Suchen Sie hier **Braze** und klicken Sie dann auf den Button **Weiter**.

Folgen Sie den Aufforderungen auf dem Bildschirm **Zugangsdaten eingeben** und geben Sie die folgenden Informationen ein. Speichern Sie Ihre Zugangsdaten, wenn Sie fertig sind.
  - Zugangsdaten-Name
  - Setzen Sie den Konnektor auf **Internet App**
  - Hostname: `<your-braze-instance-url>`
  - **Anfrage-Header**:
    - **Autorisierung**: Träger
    - **Content-Typ**: application/json
  - Token: `<your-braze-api-key>`

### Braze als System hinzufügen

#### Schritt 1: Einen Arbeitsablauf erstellen

{% tabs %}
{% tab Nutzer:innen Update %}
1. Navigieren Sie im Menü OneTrust-Integrationen zu **Galerie** > **Braze** > **Hinzufügen**, um einen neuen Workflow zu erstellen.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Geben Sie einen Namen und eine E-Mail für die Benachrichtigung im Modal des Workflows an. Klicken Sie auf den Button **Erstellen**. Bei der Erstellung werden Sie zum Workflow Builder weitergeleitet. Ihr Braze-Workflow wird mit API-Aufrufen und Aktionen bestückt, die für die Bearbeitung von Löschanfragen verwendet werden können. <br><br>
3. Wählen Sie im Workflow Builder die Aktion, die Sie im Workflow triggern möchten.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab Nutzer:in löschen %}

1. Navigieren Sie im Menü OneTrust-Integrationen zu **Galerie** > **Braze** > **Hinzufügen**, um einen neuen Workflow zu erstellen.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Geben Sie einen Namen und eine E-Mail für die Benachrichtigung im Modal des Workflows an. Klicken Sie auf den Button **Erstellen**. Bei der Erstellung werden Sie zum Workflow Builder weitergeleitet. Ihr Braze-Workflow wird mit API-Aufrufen und Aktionen bestückt, die für die Bearbeitung von Löschanfragen verwendet werden können. <br><br>
3. Wählen Sie im Workflow Builder die Aktion, die Sie im Workflow triggern möchten.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Schritt 2: Aktion auswählen
{% tabs %}
{% tab Nutzer:innen Update %}

1. Wenn Sie fertig sind, klicken Sie auf **Fertig** und wählen Sie **Aktion hinzufügen**. Beachten Sie, dass die von Ihnen gewählte Aktion davon abhängt, welche Art von Einstellung aktualisiert werden soll und welchen Endpunkt Sie bevorzugen.
- Um die globalen Abo-Einstellungen eines Nutzers zu aktualisieren, wählen Sie die Aktion **POST User Tracking - Attribute**.
- Um die Einstellungen einer Nutzer:innen Abo-Gruppe zu aktualisieren, wählen Sie die Aktion **POST User Track - Attribute** oder die Aktion **POST Set Users Subscription Group Status**.<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Wählen Sie die gewünschte Aktion, wählen Sie Ihre zuvor erstellten Braze-Zugangsdaten aus und klicken Sie auf **Weiter**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab Nutzer:in löschen %}

1. Wenn Sie fertig sind, klicken Sie auf **Fertig** und wählen Sie **Aktion hinzufügen**.
- Um einen Nutzer:innen aus Braze zu löschen, wählen Sie die Aktion **POST User Delete Action**.
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Wählen Sie die gewünschte Aktion, wählen Sie Ihre zuvor erstellten Braze-Zugangsdaten aus und klicken Sie auf **Weiter**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Schritt 3: Update Anfrage Körper
{% tabs %}
{% tab Nutzer:innen Update %}

1. Aktualisieren Sie den Textkörper, um alle notwendigen dynamischen Werte aufzunehmen. Stellen Sie sicher, dass der Text der Aktion mit dem [Endpunkt`/users/track` ](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) und dem [Endpunkt`/subscription/status/set` ](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) übereinstimmt.
2. Passen Sie den Workflow mit zusätzlichen Parametern oder bedingter Logik an die Anforderungen Ihres Unternehmens an.
3. Wenn Sie mit der Bearbeitung fertig sind, klicken Sie auf **Fertig stellen** und dann auf **Aktivieren**, um den Workflow zu aktivieren.

{% alert note %}
Wenn Sie die OneTrust-Workflows verwenden, um die Einstellungen für Abo-Gruppen in Braze zu aktualisieren, muss die `subscription_group_id` mit der ID übereinstimmen, die von Braze bei der Erstellung der Abo-Gruppe festgelegt wurde. Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie im Braze-Dashboard auf die Seite **Abo-Gruppe** navigieren.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab Nutzer:in löschen %}

1. Aktualisieren Sie den Textkörper, um alle notwendigen dynamischen Werte aufzunehmen. Stellen Sie sicher, dass der Text der Aktion mit dem [Endpunkt`/users/delete` ]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) übereinstimmt.
2. Wenn Sie mit der Bearbeitung fertig sind, wählen Sie **Fertig stellen** und dann **Aktivieren**, um den Workflow zu aktivieren.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Update des Workflows für die Anfrage von Daten
1. Wählen Sie im Menü **Automatisierung der Datenschutzrechte** die Option **Workflows** aus. 
2. Wählen Sie den Workflow aus, den Sie mit der Braze Integration aktualisieren möchten. 
3. Wählen Sie den Button **Bearbeiten**, um die Bearbeitung zu aktivieren.
4. Wählen Sie dann den Workflow-Schritt aus, zu dem Sie die Integration von Braze hinzufügen möchten, und klicken Sie auf **Verbindung hinzufügen**.
5. Fügen Sie den zuvor erstellten Braze-Workflow als Systemunteraufgabe hinzu.

{% endtab %}
{% endtabs %}

## Andere unterstützte Aktionen

Zusätzlich zu den Aktionen **POST User Tracking - Attribute**, **POST Set Users Subscription Group Status** und **POST User Delete** unterstützt Braze weitere Endpunkte, die zur Erstellung angepasster Workflows und als Unteraufgaben innerhalb bestehender Workflows verwendet werden können. 

Um eine vollständige Liste der unterstützten Aktionen zu sehen:
1. Klicken Sie in OneTrust in Ihrem **Integrationsmenü** auf **Systeme**. 
2. Wählen Sie das **Braze-System**.
3. Navigieren Sie zum Tab **Aktionen**.

![]({% image_buster /assets/img/onetrust/onetrust7.png %})


