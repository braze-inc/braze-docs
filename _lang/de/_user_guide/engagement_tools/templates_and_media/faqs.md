---
nav_title: FAQ
article_title: Medienbibliothek FAQ
page_order: 5
page_type: FAQ
tool: Media
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zur Medienbibliothek in Braze."

---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zur Medienbibliothek in Braze.

### Gibt es Speicherplatzbeschränkungen für Bilder in der Medienbibliothek?

Nein, es gibt keine Speicherlimits für Assets in der Medienbibliothek. Es gibt jedoch Größenbeschränkungen für Assets (maximal 5 MB).

### Gibt es Verfallsdaten für hochgeladene Assets?

Nein, die in die Medienbibliothek hochgeladenen Assets bleiben während der gesamten Dauer Ihres Vertrags mit Braze erhalten.

### Kann ich Video-Assets hochladen?

Nein, die Medienbibliothek unterstützt keine Videodateien. Wir empfehlen, diese extern oder auf einer Plattform wie YouTube zu hosten.

### Kann ich alle Bildtypen zuschneiden?

Nein, die Medienbibliothek unterstützt das Zuschneiden von GIF-Bildern nicht.

### Wie kann ich ein vorhandenes Bild zuschneiden?

Sie können ein vorhandenes Bild zuschneiden, indem Sie das Bild aus der Medienbibliothek auswählen und auf **Crop & Save New Image** klicken. 

![Vorschau eines Bildes in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Sie werden dann zu einem Zuschneide-Composer weitergeleitet, in dem Sie den Verhältnistyp auswählen und den Namen des neuen Bildes bearbeiten können. Wenn Sie **Save** auswählen, kann Ihr neues Bild verwendet werden.

![Fenster zum Zuschneiden und Speichern von Bildern der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Beim Hochladen meines Bildes kommt es immer wieder zu einem Timeout. Was kann ich dagegen tun?

Das kann aus verschiedenen Gründen passieren, aber eine gängige Lösung besteht darin, Ihr Bild vor dem Hochladen zu optimieren. Das bedeutet, dass Sie Ihr Bild durch einen Bildoptimierer wie [ImageOptim](https://imageoptim.com/mac) laufen lassen.

Wenn Ihr Bild in Photoshop (oder einer ähnlichen Software) erstellt wurde und viele Ebenen hat, kann das Zusammenführen und Reduzieren der Ebenenanzahl ebenfalls helfen.

### Ich sehe einen „Unerwarteten Fehler" beim Hochladen eines Bildes, obwohl es unter 5 MB groß ist und ein unterstütztes Format hat. Was ist das Problem?

Das kann hauptsächlich zwei Gründe haben:

1. **Ungültige Metadaten in der Datei:** Die Software, die Braze zur Bildverarbeitung verwendet, kann Dateien mit ungültigen oder inkompatiblen Metadaten ablehnen. In einigen Fällen kann die Datei auch so verarbeitet werden, dass sie das 5-MB-Limit überschreitet. Versuchen Sie, ein anderes Bild zu verwenden (z. B. das Bild aus Ihrem Bildbearbeitungsprogramm erneut exportieren oder speichern) oder ein Bild aus einer anderen Quelle.
2. **Sonderzeichen im Dateinamen:** Dateinamen, die Sonderzeichen enthalten (wie `&` oder `%`), können dazu führen, dass der Upload fehlschlägt. Benennen Sie die Datei so um, dass sie nur Buchstaben, Zahlen, Bindestriche oder Unterstriche enthält, und versuchen Sie dann erneut, sie hochzuladen.

### Warum kann ich nicht jedes beliebige Bild in die Push-Composer hochladen?

Das liegt daran, dass die meisten Composer Beschränkungen für das zulässige Bildseitenverhältnis haben.