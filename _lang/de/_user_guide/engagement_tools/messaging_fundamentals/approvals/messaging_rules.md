---
nav_title: Messaging-Regeln
article_title: Messaging-Regeln
page_order: 1
page_type: reference
description: "Auf dieser Seite erfahren Sie, wie Sie Messaging-Regeln im Genehmigungs-Workflow für Kampagnen und Canvase mit einem großen Sendevolumen verwenden können."
---

# Messaging-Regeln

> Verwenden Sie Messaging-Regeln in Ihrem Genehmigungs-Workflow, um die Anzahl der erreichbaren Nutzer:innen zu begrenzen, bevor eine zusätzliche Genehmigung erforderlich ist. Auf diese Weise können Sie Ihre Kampagnen und Canvase überprüfen, bevor Sie eine größere Zielgruppe zusammenstellen.

## Funktionsweise

Messaging-Regeln gelten für einen Workspace und bestehen aus einem Nachrichtentyp und einer maximalen Anzahl erreichbarer Nutzer:innen.

- **Art der Nachricht:** Legt fest, auf welchen Nachrichtentyp die Regel angewendet wird: Kampagne, Canvas oder sowohl Canvas als auch Kampagnen.
- **Maximal erreichbare Nutzer:innen:** Bestimmt die Größe der Zielgruppe, für die eine zusätzliche Genehmigung erforderlich ist.

### Gemeinsame Nachrichtenarten und maximal erreichbare Nutzer:innen

Es können zwei Regeln mit der gleichen Anzahl von erreichbaren Nutzer:innen für den gleichen Nachrichtentyp existieren. Sie können zum Beispiel ein Maximum von 10.000 Nutzer:innen für Canvas und 10.000 Nutzer:innen sowohl für Canvas als auch für Kampagnen festlegen. 

### Separate Genehmiger

Zwei Regeln können das gleiche Nutzer:innen-Maximum haben, so dass Sie Ihre Regeln nach Genehmigern organisieren und trennen können. Sie erstellen zum Beispiel die folgenden zwei Regeln:

- Regel A für Canvas mit maximal 100.000 Nutzer:innen mit Genehmigern in Ihrem juristischen Team
- Regel B für Canvas mit maximal 100.000 Nutzer:innen mit Genehmigern in Ihrem Marketing Team 

### Keine überschneidenden erreichbaren Nutzer:innen

Sie können keine Regeln mit einer sich überschneidenden Anzahl von Nutzer:innen für denselben Nachrichtentyp festlegen. Die folgende Messaging-Regel **kann zum Beispiel nicht** eingestellt werden: 

- Regel C für Canvas mit maximal 10.000 Nutzer:innen 
- Regel D für Canvas mit einer Höchstzahl von 1.000.000 Nutzer:innen

## Erstellen einer Messaging-Regel

### Voraussetzungen

Nur Braze-Administratoren können Messaging-Regeln festlegen, aber jeder Braze-Nutzer:innen kann eine Messaging-Regel genehmigen (auch Nutzer:innen ohne allgemeine Genehmigungsberechtigung).

### Schritt 1: Regel hinzufügen

{% alert note %}
Sie können bis zu fünf Messaging-Regeln erstellen.
{% endalert %}

1. Gehen Sie zu **Einstellungen** > **Genehmigungs-Workflow** > **Messaging-Regeln**.
2. Wählen Sie **Regel erstellen**.
3. Geben Sie dieser Regel einen Namen (z.B. "Alle Nutzer:innen").
4. Wählen Sie bei **Nachrichtentyp** **Kampagne**, **Canvas** oder **sowohl Canvas als auch Kampagnen** aus, um die Genehmigungsregel anzuwenden.
5. Geben Sie eine Zahl für **maximal erreichbare Nutzer:innen** ein. Weitere Informationen finden Sie unter [Statistiken zur Zielgruppe]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Wählen Sie **Speichern**.

![Eine beispielhafte Messaging-Regel "Regel 1" für Kampagnen mit maximal 100.000 Nutzer:innen. Es gibt einen Nutzer:innen, der das Canvas und die zu startende Kampagne genehmigen kann.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Schritt 2: Start mit Genehmigung festlegen (optional)

Wählen Sie **Starten mit Genehmigung zulassen**. Als nächstes wählen Sie für **Mit Genehmigung von** die Genehmiger aus, die berechtigt sind, das Canvas oder die Kampagne zu genehmigen, wenn das Maximum erreicht ist.

Beachten Sie die folgenden Details zum Starten von Nachrichten mit Genehmigung:

- Wenn das Maximum erreicht ist und ein Genehmigender ausgewählt wurde, kann der Nutzer:innen mit der Genehmigungsberechtigung aus dem Dropdown-Menü **Target Audience** **Approved** auswählen.
- Wenn das Maximum erreicht ist und eine Genehmigung nicht ausgewählt wurde, wird der Start des Canvas oder der Kampagne verhindert.

![Der Schritt "Zusammenfassung" des Canvas-Workflows, der anzeigt, dass Sie eine Genehmigung zum Starten benötigen.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Häufig gestellte Fragen

### Muss ich meine Berechtigungen für die Verwendung von Messaging-Regeln neu konfigurieren?

Nein. Jeder Nutzer:innen kann, unabhängig von seinen aktuellen Berechtigungen, als Genehmigender für Targeting ausgewählt werden.

### Wie hängen die Regeln für das Messaging mit dem Schritt Targeting der Zielgruppe zusammen?

Messaging-Regeln berücksichtigen keine Details wie triggernde Ereignisse. Eine Kampagne könnte zum Beispiel alle Ihre Nutzer:innen ansprechen. Die Kampagne ist jedoch ereignisgesteuert, so dass die Zahl der Nutzer:innen, die sie tatsächlich erhalten, geringer ist.

### Ändert sich automatisch etwas, wenn die Regeln für das Messaging aktiviert werden?

Nein. Nachdem dieses Feature aktiviert wurde, müssen Sie manuell die maximale Anzahl der Nutzer:innen eingeben und die Genehmigenden auswählen, um das Feature nutzen zu können.

