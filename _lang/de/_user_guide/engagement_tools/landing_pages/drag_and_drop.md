---
nav_title: Drag-and-Drop-Editor
article_title: Landing Pages per Drag-and-Drop erstellen
description: "In diesem Artikel erfahren Sie, wie Sie Landing Pages von Braze mit dem Drag-and-Drop-Editor erstellen und anpassen können."
page_order: 0
alias: /landing_pages/drag_and_drop/
---

# Ziehen und Ablegen von Landing Pages

> Mit dem Drag-and-Drop-Editor können Sie eine Landing Page erstellen und anpassen, um Ihre Zielgruppe zu vergrößern und Präferenzen direkt in Braze zu sammeln.

{% alert important %}
Die Startseiten befinden sich derzeit in der Early Access-Phase. Es gibt ein Limit von fünf Landing Pages pro Unternehmen. Endnutzer-Sitzungen, die auf Startseiten aufgezeichnet werden, zählen für die Berechnung der monatlich aktiven Nutzer:innen (MAU).
{% endalert %}

## Erstellen einer Landing Page (per Drag-and-Drop)

### Schritt 1: Erstellen Sie eine Landing Page

Gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie **Landing Page erstellen**, oder wählen Sie den Namen einer bestehenden Seite, um sie zu duplizieren oder zu ändern.

![Die Startseite „Startseiten“.][2]{: style="max-width:90%;"}

### Schritt 2: Details Ihrer Startseite einrichten

#### Allgemeine Details

Der Name und die Beschreibung der Zielseite werden für die Suche nach der Seite in Ihrem internen Arbeitsbereich verwendet. Diese werden für Ihre Kunden nicht sichtbar sein.

#### Details zur Website

Richten Sie Metatags ein, um die Darstellung Ihrer Seite auf der Browser-Registerkarte anzupassen und für Suchmaschinenergebnisse zu optimieren. Diese werden für Ihre Kunden sichtbar sein.

Wir empfehlen Ihnen, diese bewährten Verfahren zu befolgen:

| Detail | Beschreibung | Empfehlungen |
| --- | --- |
| Website-Titel | Der Titel, der auf der Browser-Registerkarte angezeigt wird. | Verwenden Sie bis zu 60 Zeichen. |
| Beschreibung der Website | Ein Textausschnitt, der in den Suchergebnissen angezeigt wird. | Verwenden Sie zwischen 140-160 Zeichen.|
| Favicon | Das Symbol, das neben dem Titel der Website auf dem Tab des Browsers erscheint. | Verwenden Sie ein Seitenverhältnis von 1:1 und einen unterstützten Dateityp wie PNG, JPEG oder ICO. |
| URL-Bezeichner | Dies ist der Link, auf den Nutzer:innen klicken werden, um zu Ihrer Landing Page zu gelangen. | Dies muss einzigartig sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 3: Startseite anpassen

Wählen Sie **Editor starten**, um mit der Gestaltung Ihrer Landing Page im Drag-and-Drop-Editor zu beginnen. Der Editor wird mit einem Standard-Template vorinstalliert, die Sie an Ihren Anwendungsfall anpassen können.

![Landing Page-Vorlage mit einem Formular für die Kundenanmeldung.][8]{: style="max-width:90%;"}

#### Blöcke ziehen und ablegen

Der Editor verwendet zwei Arten von Komponenten für die Gestaltung von Startseiten: Zeilen und Blöcke. Alle Blöcke müssen in einer Reihe platziert werden.

![Der Abschnitt „Erstellen“ des Editors enthält „Zeilen“ und „Formularblöcke“.][4]{: style="max-width:30%;"}

#### Formularblock

Verwenden Sie verschiedene Formularblockkomponenten, um angepasste und Standard-Profil-Attribute und angepasste Events zu protokollieren. Der Formularblock für Eingabefelder kann sowohl Standard- als auch benutzerdefinierte Attribute für Ihre Benutzer protokollieren, und die Formularblöcke für die Telefon- und E-Mail-Erfassung können die Telefon- und E-Mail-Felder für die Formularübertragungen Ihrer Benutzer erfassen. Button-Aktionen können als angepasste Attribute, angepasste Events oder beides bei der Formularübermittlung protokolliert werden. 

Wenn Sie einen Formularblock einfügen, müssen Sie mindestens einen Button einfügen, bei dem das Umschalten für **Formular abschicken bei Klick auf den Button** aktiviert ist. Sie sollten auch eine weitere Landing Page für den [Bestätigungsstatus](#confirmation-state) erstellen.

![Ein Formularblock, der einen neuen Kunden registriert und einen Rabattcode an dessen E-Mail sendet.][5]{: style="max-width:70%;"}

#### Stile für Seitencontainer

Auf der Registerkarte **Seitencontainer** können Sie Stile festlegen, die auf alle relevanten Komponentenblöcke in Ihrer Landing Page angewendet werden. Diese Stile werden überall auf Ihrer Seite verwendet, es sei denn, Sie setzen sie mit einem bestimmten Block außer Kraft.

Wir empfehlen, die Stile auf der Ebene der Seitencontainer einzurichten, bevor Sie die Stile auf der Blockebene anpassen. Sie können auch ein Hintergrundbild für die gesamte Seite hinzufügen.

![Der Seitencontainer mit Optionen zur Anpassung von Hintergrundbildern, Farben, Rahmendetails und der Gestaltung des Inhalts.][6]{: style="max-width:30%;"}

### Schritt 4: Vorschau Ihrer Landing Page

Auf der Registerkarte **Vorschau** des Editors können Sie eine Vorschau Ihrer Landing Page anzeigen. Nachdem Sie Ihre Landing Page als Entwurf gespeichert haben, können Sie die URL aufrufen, indem Sie zu **Landing Pages** gehen und **URL kopieren** neben Ihrer Landing Page wählen. Sie können die URL auch mit anderen Personen teilen.

![Eine Startseite mit geöffnetem Menü, um die Option „URL kopieren“ anzuzeigen.][7]{: style="max-width:90%;"}

Wenn Sie mit der Startseite zufrieden sind, wählen Sie **Startseite veröffentlichen** aus.

{% alert important %}
Der URL-Bezeichner kann nach der Veröffentlichung der Startseite nicht mehr bearbeitet werden.
{% endalert %}

## Erstellen einer Startseite zur Bestätigung {#confirmation-state}

Wenn Sie ein [Formular](#form-block) auf Ihrer Startseite einfügen, vergessen Sie nicht, eine Bestätigungsseite zu erstellen. Erstellen Sie eine weitere Landing Page für den Bestätigungsstatus und fügen Sie dann den Link in das Feld **Web-URL öffnen** der Schaltfläche ein, die das Formular absendet.

## Verlinkung zu Ihrer Startseite

Sie können in jedem Kanal einen Link zur Landing Page einfügen, indem Sie den Link in eine Braze-Nachricht oder eine Kampagne in den sozialen Medien kopieren und einfügen.

## Behandlung von Fehlern bei der Formularübermittlung

Wenn ein Benutzer einen ungültigen Formularwert eingibt (z.B. nicht akzeptierte Sonderzeichen), wird eine allgemeine Fehlermeldung angezeigt, die nicht angepasst werden kann, und er kann das Formular nicht abschicken. Sie können das Fehlerverhalten auf der Vorschau-Landeseite sehen.

## Zusammenführen von Benutzern, die von Ihrer Landing Page aus erstellt wurden

Jede Formularübermittlung auf einer Startseite erstellt ein neues anonymes Nutzerprofil in Braze. Wenn bereits ein:e Nutzer:in mit der gleichen E-Mail Adresse existiert, können Sie das neue Nutzerprofil mit dem bestehenden Profil zusammenführen, indem Sie den [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user)-Endpunkt verwenden. Um mehr über die verschiedenen Möglichkeiten zu erfahren, Nutzer:innen zu deduplizieren, lesen Sie bitte [Duplizieren]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

Die Zusammenführung von Nutzer:innen wird in Zukunft automatisch über einen Liquid-Tag erfolgen. 

## Überlegungen

Die Größe der Startseite kann bis zu 1 MB betragen.

## Berechtigungen

Sie benötigen entweder Administratorrechte oder alle der folgenden Berechtigungen, um auf Landing Pages zuzugreifen, sie zu erstellen und zu veröffentlichen:

- Startseiten aufrufen
- Entwürfe für Startseite erstellen
- Startseiten veröffentlichen

## Planebenen

Die Anzahl der veröffentlichten Startseiten und angepassten Domains, die Sie nutzen können, hängt von der Art Ihres Tarifs ab: kostenlos oder kostenpflichtig (inkrementell).

| Feature                                                                                                   | Kostenlose Nutzung     | Kostenpflichtige Nutzung (inkrementell)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Veröffentlichte Startseiten                                                                 | Fünf pro Unternehmen | 20 zusätzlich |
| Angepasste Domains          | Eine pro Unternehmen | Fünf zusätzliche |

## Häufig gestellte Fragen

### Was passiert, wenn ein Nutzer:innen seine Daten auf der Landing Page eingibt?

Wenn ein Nutzer:innen ein Formular absendet, wird ein neues Braze Nutzerprofil mit den übermittelten Nutzerdaten erstellt.

### Gibt es irgendwelche technischen Voraussetzungen für die Veröffentlichung einer Landing Page?

Nein, es gibt keine technischen Anforderungen.

### Gibt es einen HTML-Editor für Landing Pages?

Sie können den HTML-Code einer Landing Page mit dem Block Benutzerdefinierter Code bearbeiten.

### Sind Berichte für Landing Pages verfügbar?

Nein, das ist derzeit nicht verfügbar.

### Kann ich einen Webhook innerhalb einer Landing Page erstellen?

Nein, dies wird derzeit nicht unterstützt.

### Welche Features stehen auf der Roadmap für Startseiten? {#roadmap}

Wir planen die Veröffentlichung weiterer Features für Startseiten, die sich in der Entwicklung befinden. Dazu können gehören:

* Neues Liquid-Tag für die Verknüpfung einer Startseite in einem Messaging-Kanal von Braze
* Automatische Zusammenführung von Nutzer:innen, wenn eine Landing Page über einen Braze-Kanal gesendet wird
* Seite für Basisberichte
* Ziehen und Ablegen von Formularblöcken für Kontrollkästchen und Dropdowns
* Standardereignis für Tracking und Retargeting auf der Grundlage von Formularübermittlungen

Diese Funktionen sind zwar Teil unserer Roadmap, aber sie befinden sich noch in der Entwicklung und Braze kann nicht garantieren, dass einige oder alle dieser Funktionen allgemein verfügbar sein werden. Für den Zugriff auf einige oder alle der geplanten Funktionen für Landing Pages können zusätzliche Gebühren anfallen.

[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
[8]: {% image_buster /assets/img/landing_pages/template.png %}
