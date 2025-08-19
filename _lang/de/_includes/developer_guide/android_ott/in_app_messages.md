{% multi_lang_include developer_guide/prerequisites/android.md %}

## Über TV- und OTT-Unterstützung

Das Android Braze SDK unterstützt von Haus aus die Anzeige von In-App-Nachrichten auf OTT-Geräten wie Android TV oder Fire Stick. Es gibt jedoch einige wesentliche Unterschiede zwischen nativen Android- und OTT In-App-Nachrichten. Für OTT Geräte:

- In-App-Nachrichten, die einen Touch-Modus erfordern, wie Slideup, sind auf OTT deaktiviert.
- Der aktuell ausgewählte oder fokussierte Artikel, z. B. ein Button oder eine Schaltfläche zum Schließen, wird hervorgehoben.
- Klicks auf den Text der In-App-Nachricht selbst, also nicht auf einen Button, werden nicht unterstützt.
