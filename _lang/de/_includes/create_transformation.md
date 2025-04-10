Gehen Sie im Braze Dashboard zu **Dateneinstellungen** > **Datenumwandlung**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Transformationen** unter **Daten**.
{% endalert %}

Wählen Sie **Transformation erstellen**, um Ihre Transformation zu benennen, und wählen Sie dann Ihre Bearbeitungserfahrung.

![Transformationsdetails mit der Möglichkeit, „Template verwenden“ oder „Von Grund auf neu beginnen“ für Ihre Bearbeitungserfahrung zu wählen.]({% image_buster /assets/img/data_transformation/data_transformation10.png %})

Wählen Sie **Template verwenden**, um eine Template-Bibliothek zu durchsuchen, die auch Anwendungsfälle der Datentransformation enthält. Oder wählen Sie **Von Grund auf neu**, um eine Standard-Codevorlage zu laden. 

Wenn Sie bei Null anfangen, wählen Sie ein Ziel für Ihre Transformation. Sie können trotzdem eine Codevorlage aus der Vorlagenbibliothek einfügen.

{% details Mehr über Reiseziele %}
* **POST: Benutzer verfolgen:** Wandelt Webhooks von einer Quellplattform in Aktualisierungen des Benutzerprofils um, z. B. Attribute, Ereignisse oder Käufe.
* **PUT: Aktualisieren Sie mehrere Katalogartikel:** Wandelt Webhooks von einer Quellplattform in Aktualisierungen von Katalogartikeln um.
* **LÖSCHEN: Löschen Sie mehrere Katalogartikel:** Wandelt Webhooks von einer Quellplattform in Löschungen von Katalogartikeln um.
* **PATCH: Bearbeiten Sie mehrere Katalogartikel:** Wandelt Webhooks von einer Quellplattform in Katalogartikel-Bearbeitungen um.
* **POST: Senden Sie Nachrichten sofort über API Only:** Transformiert Webhooks von einer Quellplattform, um Sofortnachrichten an bestimmte Benutzer zu senden.
{% enddetails %}

{% alert note %}
Möchten Sie weitere Vorlagen oder Ziele anfordern? Ziehen Sie in Erwägung, eine [Produktbewertung]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) zu hinterlassen.
{% endalert %}

Nachdem Sie Ihre Transformation erstellt haben, sehen Sie die Detailansicht der Transformation. Hier können Sie unter **Webhook-Details** den zuletzt empfangenen Webhook für diese Transformation einsehen und unter **Transformationscode** ein Feld für die Eingabe Ihres Transformationscodes.

{% if include.location == "typeform" %}

![]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

Erfassen Sie Ihre **Webhook-URL** zur Verwendung im nächsten Schritt.

{% endif %}
