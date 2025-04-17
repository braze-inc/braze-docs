---
nav_title: Voucherify und Aktionscodes Liste
article_title: Voucherify und Braze Promotion Codes Liste
page_order: 4
alias: /partners/voucherify/promotion/
description: "Dieser referenzierte Artikel beschreibt, wie Sie Voucherify Codes mit Braze Promo Codes Snippet teilen können."
page_type: partner
search_tag: Partner
---

# Voucherify und Braze Aktionscodes Liste

> Zusätzlich zum Connected-Content und den angepassten Attributen können Sie Voucherify Codes mit dem Braze Promo Codes Snippet teilen. Exportieren Sie zunächst Codes aus Voucherify, importieren Sie Codes in Braze und fügen Sie ein E-Mail-Snippet hinzu, um Codes aus der Aktionscodes-Liste zu ziehen. 

_Diese Integration wird von Voucherify gepflegt._

## Schritt 1: Exportieren Sie eindeutige Codes von Voucherify

Navigieren Sie in Voucherify zu Ihrer Voucherify-Kampagne. Wählen Sie dann **Exportieren in CSV** und bearbeiten Sie die CSV-Datei. Entfernen Sie den Namen der Spalte, so dass nur noch die Liste der Codes übrig bleibt.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## Schritt 2: Erstellen Sie eine Liste mit Aktionscodes

Gehen Sie zu **Dateneinstellungen** > **Aktionscodes** und klicken Sie auf **Aktionscode-Liste erstellen**.

Sie können den Namen der Voucherify Kampagne verwenden, um die Liste zu benennen und die Konsistenz der Daten zu überprüfen.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

Als nächstes fügen Sie das Code Snippet hinzu, das auf die Codes aus der Liste referenziert. Es wird mit einem eindeutigen Code gefüllt, wenn die Nachricht gesendet wird.

### Zusätzliche Einstellungen

Sie können auch Attribute für Codes festlegen, wie z.B. Listenablauf und Schwellenwertwarnungen. Beachten Sie jedoch, dass Voucherify die Logik hinter Ihren Codes unabhängig von den Listeneinstellungen verwaltet.

![Ablauf der Liste]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## Schritt 3: CSV-Datei hochladen

Laden Sie die CSV-Datei mit den Voucherify Codes hoch.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

Bestätigen Sie, dass die Liste nur Codes enthält (keine Spaltenüberschriften) und klicken Sie auf **Upload starten**. Wenn der Import abgeschlossen ist, klicken Sie auf **Liste speichern**, um die Details der Liste zu bestätigen.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## Schritt 4: Verwenden Sie Code Snippet in Braze Kampagnen

Um Codes aus der Liste in einer Kampagne von Braze zu verwenden, kopieren Sie das Snippet und fügen es in den Text der E-Mail ein.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

Fügen Sie das Code Snippet hinzu, um einen Code aus der Liste anzuzeigen.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

Sobald die Nachricht mit dem Code gesendet wurde, kann derselbe Code nicht mehr verwendet werden.

