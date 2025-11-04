---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und NPAW, einer intelligenten Analytics-Plattform, die umsetzbare Insights für führende Online-Medienschaffende liefert."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), auch bekannt als _Nice People at Work_, ist eine intelligente Analytics-Plattform, die umsetzbare Insights für führende Online-Medienschaffende liefert. Mit der YOUBORA-Tool-Suite von NPAW können die Kunden von Braze jetzt eine prädiktive und robuste KI nutzen, um das Kundenverhalten besser zu verstehen und das Engagement plattformübergreifend zu fördern.

# Voraussetzungen

| Anforderung   |Herkunft| Beschreibung |
| --------------|------|-------------|
| YOUBORA API-Schlüssel |[YOUBORA Einstellungen](https://youbora.nicepeopleatwork.com/users/login)|Ein API-Schlüssel, der bei der Registrierung der Nutzer:innen generiert wird und sich unter **Einstellungen** befindet |
| ID |[Braze Einstellungen](https://dashboard.braze.com/sign_in) | YOUBORA bietet Ihnen die Möglichkeit, die Software mit Braze über eine ***Braze ID***, eine ***externe Nutzer:in ID***, oder eine ***Nutzer:innen ID*** |
| Endpunkt |[Braze Einstellungen](https://dashboard.braze.com/sign_in)| Ein vollständig anpassbarer URL-Endpunkt, der über Ihr Braze-Dashboard konfiguriert werden kann. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# Analytics-Integration

## Zugriff auf die Seite mit den Integrationen

Nachdem Sie sich bei Ihrem YOUBORA Tool Suite Konto angemeldet haben, navigieren Sie zur Seite Integrationen, indem Sie die Option **Integrationen** aus dem Dropdown-Kontomenü auswählen.

![NPAW dropdown]({% image_buster /assets/img/npaw_dropdown.png %})

## Konfigurieren Ihrer Integration

Sobald Sie die Seite Integration aufgerufen haben, scrollen Sie nach unten, bis Sie
siehe die Option Integration von **Braze**. Nachdem Sie darauf geklickt haben, erweitert sich das Fenster und bietet Ihnen eine Reihe von Parametern an, die Sie ausfüllen müssen:

![NPAW Integration]({% image_buster /assets/img/npaw_integration.png %})

Füllen Sie die Details mit den entsprechenden Informationen aus, die Sie in der Rubrik Nebeneinkünfte finden:
* Der **Name des Konnektors** ist ein **alphanumerischer** String, der in Zukunft verwendet wird, um auf diese Integration zu referenzieren. Dieser Wert kann auf jeden beliebigen Wert gesetzt werden, solange er **nur** Buchstaben und Zahlen enthält.
* Die **Nutzer:in** ist die ID, die Sie zuvor gewählt haben, um Ihre YOUBORA Software mit Ihrem Braze-Konto zu verknüpfen. Wenn Sie beispielsweise die Verknüpfung über Ihre **Braze ID** vornehmen möchten, wählen Sie **Braze ID** aus dem Dropdown-Menü aus, um den Wert dem entsprechenden Feld zuzuweisen.
* Der **API-Schlüssel** ist Ihr YOUBORA Tools Suite API-Schlüssel, den Sie zuvor im Bereich **API** unter **Einstellungen** finden.
* **Endpunkt** ist der anpassbare URL-Endpunkt, der zuvor in Ihrem Braze-Dashboard eingerichtet wurde.

Sobald Sie alle Felder ausgefüllt haben, klicken Sie einfach auf den Button **Verbinden**, um eine Verbindung herzustellen und die Änderungen zu speichern.

## Verwendung Ihrer NPAW Integration

Wenn Sie die Integration mit Braze fertig konfiguriert haben, navigieren Sie zum Produkt **Nutzer:innen** und wählen Sie den **Manager für Proben** innerhalb des **Sections Manager** aus.

Nachdem Sie eine Probe in der **Probenverwaltung** erstellt haben, können Sie nun auf das Symbol mit dem dreifachen Punkt auf der rechten Seite klicken, um alle Nutzer:innen Ihrer Probe an Braze zu senden.

![NPAW sample manager:in]({% image_buster /assets/img/npaw_sample_manager.png %})

Nachdem Sie Ihre Nutzer:innen an Braze geschickt haben, können Sie jetzt aktiv werden und Kampagnen auf Segmente ausrichten, um inaktive Nutzer:innen wieder zu engagieren, Ihre treuesten Nutzer:innen zu kontaktieren oder eine beliebige Aktion für ein beliebiges Segment durchzuführen!
