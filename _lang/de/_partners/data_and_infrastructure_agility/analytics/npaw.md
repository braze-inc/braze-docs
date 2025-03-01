---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und NPAW, einer intelligenten Datenanalyseplattform, die führenden Online-Medienexperten verwertbare Erkenntnisse liefert."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), auch bekannt als _Nice People at Work_, ist eine intelligente Datenanalyseplattform, die führenden Online-Medienexperten verwertbare Erkenntnisse liefert. Mit der YOUBORA-Tool-Suite von NPAW können Braze-Kunden jetzt eine prädiktive und robuste KI nutzen, um das Kundenverhalten besser zu verstehen und das Engagement auf allen Plattformen zu fördern.

# Voraussetzungen

| Anforderung   |Herkunft| Beschreibung |
| --------------|------|-------------|
| YOUBORA API-Schlüssel |[YOUBORA Einstellungen](https://youbora.nicepeopleatwork.com/users/login)|Ein API-Schlüssel, der bei der Benutzeranmeldung generiert wird und unter **Einstellungen** zu finden ist |
| ID |[Einstellungen löten](https://dashboard.braze.com/sign_in) | YOUBORA bietet Ihnen die Möglichkeit, die Software mit Braze über eine ***Braze-ID***, eine ***externe Benutzer-ID***oder eine ***Benutzer-ID*** |
| Endpunkt |[Einstellungen löten](https://dashboard.braze.com/sign_in)| Ein vollständig anpassbarer URL-Endpunkt, der über Ihr Braze Dashboard konfiguriert werden kann. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# Integration von Analysen

## Zugriff auf die Seite mit den Integrationen

Nachdem Sie sich bei Ihrem YOUBORA-Tool-Suite-Konto angemeldet haben, navigieren Sie zur Seite Integrationen, indem Sie die Option **Integrationen** aus dem Dropdown-Kontomenü auswählen.

![NPAW dropdown]({% image_buster /assets/img/npaw_dropdown.png %})

## Konfigurieren Sie Ihre Integration

Sobald Sie die Seite Integration aufgerufen haben, scrollen Sie nach unten, bis Sie
siehe die Option **Braze-Integration**. Nachdem Sie darauf geklickt haben, erweitert sich das Fenster und bietet eine Reihe von Parametern an, die Sie ausfüllen müssen:

![NPAW-Integration]({% image_buster /assets/img/npaw_integration.png %})

Füllen Sie die Details mit den entsprechenden Informationen aus, die Sie in der Rubrik Nebeneinkünfte finden:
* Der **Name des Connectors** ist eine **alphanumerische** Zeichenfolge, die in Zukunft als Referenz für diese Integration verwendet wird. Dieser Wert kann auf jeden beliebigen Wert gesetzt werden, solange er **nur** Buchstaben und Zahlen enthält.
* Die **Benutzer-ID** ist die ID, die Sie zuvor gewählt haben, um Ihre YOUBORA-Software mit Ihrem Braze-Konto zu verknüpfen. Wenn Sie sich beispielsweise dafür entscheiden, die Verknüpfung über Ihre **Braze ID** durchzuführen, wählen Sie **Braze ID** aus dem Dropdown-Menü, um den Wert dem richtigen Feld zuzuweisen.
* Der **API-Schlüssel** ist Ihr YOUBORA tools suite API-Schlüssel, den Sie zuvor im Abschnitt **API** unter **Einstellungen** finden.
* **Endpunkt** ist der anpassbare URL-Endpunkt, der zuvor in Ihrem Braze Dashboard eingerichtet wurde.

Wenn Sie alle Felder ausgefüllt haben, klicken Sie einfach auf die Schaltfläche **Verbinden**, um eine Verbindung herzustellen und die vorgenommenen Änderungen zu speichern.

## Verwendung Ihrer NPAW-Integration

Wenn Sie die Konfiguration Ihrer Integration mit Braze abgeschlossen haben, navigieren Sie zum Produkt **Benutzer** und wählen Sie den **Probenmanager** im **Abschnittsmanager**.

Nachdem Sie eine Probe im **Probenmanager** erstellt haben, können Sie nun auf das Symbol mit dem dreifachen Punkt auf der rechten Seite klicken, um alle Benutzer innerhalb Ihrer Probe an Braze zu senden.

![NPAW sample manager]({% image_buster /assets/img/npaw_sample_manager.png %})

Nachdem Sie Ihre Benutzer an Braze geschickt haben, können Sie nun Maßnahmen ergreifen und Kampagnen auf Benutzersegmente ausrichten, um inaktive Benutzer wieder einzubinden, Ihre treuesten Benutzer zu kontaktieren oder jede beliebige Aktion für jedes Benutzersegment durchzuführen!
