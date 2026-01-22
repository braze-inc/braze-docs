---
nav_title: Speichern von Entwürfen für Canvas
article_title: Entwürfe für Canvas speichern
alias: "/save_as_draft/"
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie einen Entwurf für ein Canvas speichern können, das bereits gestartet wurde."
page_type: reference
tool: Canvas
---

# Speichern von Entwürfen für Canvas

> Während Sie Canvases erstellen und starten, können Sie ein aktives Canvas bearbeiten und als Entwurf speichern, so dass Sie Ihre Änderungen vor dem nächsten Start testen können. 

Wenn Sie ein aktives Canvas haben, das umfangreiche Änderungen erfordert, können Sie dieses Feature nutzen, um die Änderungen zu erstellen, zu speichern und zu überprüfen, **bevor** Sie sie im aktiven Canvas einführen. 

Wie bei jedem Canvas kann jeweils nur ein Benutzer einen Entwurf bearbeiten, und ein Canvas kann jeweils nur einen Entwurf haben. Für diese Entwürfe gibt es noch keine Analysen, da die Entwurfsänderungen noch nicht eingeführt wurden.

\![Ein Beispiel für einen Canvas-Entwurf mit einem Banner, das den Nutzer:innen anzeigt, dass sie einen Canvas-Entwurf bearbeiten und die Möglichkeit haben, den aktiven Canvas anzuzeigen. In der Fußzeile haben Sie die Möglichkeit, zur Analyseansicht zurückzukehren, als Entwurf zu speichern oder den Entwurf zu starten.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Einen Entwurf erstellen

So erstellen Sie einen Entwurf:

1. Gehen Sie zu einem aktiven Canvas.
2. Wählen Sie den Button **Als Entwurf speichern** in der Fußzeile des Canvas. 

Beachten Sie, dass Änderungen am aktiven Canvas nicht vorgenommen werden können, solange ein Entwurf eines Canvas existiert. Sie können den Canvas aktualisieren, um die Änderungen zu übernehmen oder den Entwurf zu verwerfen.

## Verweis auf den aktiven Entwurf

Um auf das aktive Canvas zu verweisen, wählen Sie in der Fußzeile der Analyseansicht oder in im Canvas-Header im Entwurf **Aktives Canvas anzeigen** aus. Um zu einem aktiven Canvas zurückzukehren, wählen Sie in der Analyseansicht oder in der aktiven Canvas-Ansicht **Entwurf bearbeiten**.

Sie können nur auf Schritte verweisen, die bereits vor der Erstellung des Entwurfs eingeleitet wurden. Das heißt, wenn Sie einen Schritt oder Kanal **nach** der Erstellung des Entwurfs erstellt haben, kann in Ihrem Entwurf nicht mehr darauf verwiesen werden.

{% alert note %}
Wenn ein Content-Block in einem Canvas-Entwurf referenziert wird, wird das Canvas in der Zählung der Content-Block-Einschlüsse aufgeführt. Wenn der Content-Block jedoch in einem Entwurf eines **aktiven** Canvas referenziert wird, wird das Canvas nicht in der Zählung der Content-Blocks aufgeführt.
{% endalert %}

### Priorisierung von In-App-Nachrichten

Bei Entwürfen eines aktiven Canvas wird die Priorität der In-App-Nachricht im Canvas-Builder sofort aktualisiert, wenn ein:e Nutzer:in die Priorität ändert. Das bedeutet, dass In-App-Nachrichten auf Canvas-Ebene sofort auf das aktive Canvas angewendet werden, auch wenn ein Entwurf existiert. 

Änderungen an der Priorität von In-App-Nachrichten auf Schrittebene werden jedoch als Entwurf gespeichert und bei einem Update des Canvas übernommen. In einem Nachrichtenschritt wird beispielsweise die Prioritätssortierung aktualisiert, wenn ein:e Nutzer:in den Entwurf startet, da die Schritteinstellungen auf Schrittebene gelten.

