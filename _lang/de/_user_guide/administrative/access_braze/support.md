---
nav_title: Braze Unterstützung
article_title: Support
description: "Auf dieser Seite finden Sie das Braze Support-Portal, über das Sie Feedback zu den Produkten von Braze abgeben können. Diese Seite ist nur für Braze Kund:innen zugänglich."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"} Braze Support

## Zugriff auf das Support-Portal

Um das Braze Support Team zu kontaktieren, navigieren Sie zum Braze-Dashboard. Wählen Sie auf dem Dashboard **Support** > **Hilfe holen**.

\![Das Dropdown-Menü "Support" mit der Option, Hilfe zu erhalten.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Abhängig von Ihren Braze-Berechtigungen und davon, ob Sie ein ausgewiesener Support-Kontakt sind, werden Sie entweder zum Braze-Supportportal weitergeleitet, wo Sie Fälle einreichen und tracken können, oder zu unserem Standard-Supportformular. Wenn Sie sich nicht sicher sind, ob Sie ein Braze-Supportkontakt sind, wenden Sie sich an den Braze-Administrator, den Braze Success Manager oder den Account Manager:in Ihres Unternehmens.

## Hinzufügen von Ansprechpartnern für den Support

Bestimmte Support-Kontakte können auf alle Support-Fälle für Ihr Unternehmen zugreifen, unabhängig davon, wer sie eingereicht hat. Sie können Nutzer:innen direkt auf der Seite **Nutzer:innen bearbeiten** als Support-Kontakt festlegen. 

1. Gehen Sie zu **Einstellungen** > **Benutzer des Unternehmens** und suchen Sie den Nutzer:innen anhand seines Namens oder seiner E-Mail Adresse.
2. Wählen Sie entweder den Namen des Nutzers:in aus oder bewegen Sie den Mauszeiger über die Zeile des Nutzernamens, um ein Menü anzuzeigen. 
3. Wählen Sie im Menü **Bearbeiten** aus, um zur Seite **Nutzer:innen bearbeiten** weitergeleitet zu werden.
4. Aktivieren Sie das Kontrollkästchen für **Diesen Nutzer:innen als designierten Support-Kontakt für das Braze Support-Portal festlegen**.

\![Das Kontrollkästchen zum Festlegen eines Nutzers:innen als Support-Kontakt.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Zugang erhalten

Nachdem ein Nutzer:innen als Support-Kontakt benannt wurde, sendet das Braze Support-Portal diesem Nutzer:innen eine Willkommens-E-Mail mit Anweisungen zum Einrichten seines Zugangs.

## Screenshots der Entwicklungskonsole zur Verfügung stellen

Wenn Sie mit dem Support kommunizieren, kann es sein, dass Sie auf Ihre Entwickler:in zugreifen müssen, um zusätzliche Informationen bereitzustellen:
- Chrome
  1. Klicken Sie mit der rechten Maustaste auf die Webseite und wählen Sie **Inspizieren**.
  2. Wählen Sie in dem sich öffnenden Fenster den Tab **Konsole** aus.
  3. Machen Sie einen Screenshot des Tabs der Konsole.<br><br>
- Firefox
  1. Klicken Sie mit der rechten Maustaste auf die Webseite und wählen Sie **Element inspizieren**.
  2. Wählen Sie in dem sich öffnenden Fenster den Tab **Konsole** aus.
  3. Machen Sie einen Screenshot des Tabs der Konsole.<br><br>
- Safari
  1. Gehen Sie in der Menüleiste am oberen Rand Ihres Bildschirms auf Safari und wählen Sie dann **Einstellungen**.
  2. Wählen Sie **Erweitert** und aktivieren Sie dann das Kontrollkästchen neben **Develop-Menü in der Menüleiste anzeigen**. Sie können dann das Fenster verlassen.
  3. Klicken Sie mit der rechten Maustaste auf die Webseite und wählen Sie **Element inspizieren**.
  4. Wählen Sie in dem sich öffnenden Fenster den Tab **Konsole** aus.
  5. Machen Sie einen Screenshot des Tabs der Konsole.

## Bewährte Praktiken für das Einreichen eines Supportfalls

### Stellen Sie so viele Informationen wie möglich zur Verfügung

Je mehr Insights Sie anbieten können, desto besser. Geben Sie Angaben wie den Workspace, die URL der Kampagne oder des Segments und alle relevanten externen IDs an. Dies kann uns helfen, Ihr Problem effizienter zu beheben.

### Stellen Sie eine Auswahl von Nutzer:innen bereit

Teilen Sie eine Stichprobe von Nutzer:innen und nicht das gesamte betroffene Segment. Die Angabe einer geringeren Anzahl von Nutzer:innen hilft uns, den Bereich einzugrenzen und unsere Untersuchungen zu beschleunigen.

### Netzwerkprotokolle anhängen (HAR-Protokolle)

Wenn Sie sich an den Support wenden, ist es hilfreich, wenn der betroffene Nutzer:innen die Netzwerkprotokolle (HAR-Protokolle) seines Browsers sammelt, während das Problem auftritt. Hier werden die Netzwerkanfragen zwischen dem Browser und dem Server für die einzelnen Komponenten einer Webseite sowie das Braze-Dashboard angezeigt, das der Nutzer:innen zu öffnen versucht.

Lassen Sie die betroffenen Nutzer:innen Folgendes tun:

1. Öffnen Sie ihre Entwickler:in-Tools. Wenn Sie Chrome verwenden, können Sie dies mit dem Tastaturkürzel `option` + `⌘` + `J` (auf macOS) tun. Wenn Sie Windows oder Linux verwenden, können Sie dies mit dem Shortcut `shift` + `CTRL` + `J` tun.
2. Wählen Sie **Netzwerk** > **Fetch/XHR** oder **XHR**.
3. Nehmen Sie eine Bildschirmaufnahme oder einen Screenshot auf, auf dem **Name**, **Status**, **Größe** und **Zeit** der Elemente zu sehen sind.<br><br>\![Der Tab "Fetch/XHR" in einem Chrome-Browser.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Hängen Sie dann die Aufnahme oder den Screenshot des Nutzers:innen an das Support-Ticket an. Diese Informationen können die Ermittlungen von Support unterstützen.

### Klären Sie erwartetes und tatsächliches Verhalten

Lassen Sie uns wissen, was Sie erwartet haben und was tatsächlich passiert ist. Dies kann uns helfen, die möglichen Ursachen des Problems einzugrenzen.

### Fügen Sie relevante Bilder hinzu

Fügen Sie einen Screenshot an, um das Problem zu verdeutlichen. Wenn Sie uns diese Bilder zur Verfügung stellen, können wir das Problem wesentlich besser verstehen und den Lösungsprozess beschleunigen.

### Beurteilen Sie die Auswirkungen

Wählen Sie den entsprechenden Schweregrad aus, damit wir die richtigen Ressourcen zur Behebung des Problems zuweisen können. 

{% alert important %}
Wenn Sie ein Problem als "kritisch" markieren, bedeutet dies, dass Ihre Produktionsinstanz ausgefallen ist und alle Arbeiten innerhalb von Braze eingestellt wurden.
{% endalert %}

## Fehlerbehebung Zugang

Wenn Sie beim Einloggen in das Braze Support Portal eine Fehlermeldung erhalten, wie z.B. `Check your entry`, vergewissern Sie sich, dass Sie dem Link in Ihrer Willkommens-E-Mail gefolgt sind, um ein Passwort für das Portal festzulegen. Wenn Sie das getan haben oder sich zuvor in das Portal einloggen konnten, erstellen Sie ein Support-Ticket.