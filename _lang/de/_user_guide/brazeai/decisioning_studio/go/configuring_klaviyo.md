---
nav_title: Konfigurieren Sie mit Klaviyo
article_title: Konfigurieren Sie mit Klaviyo für BrazeAI Decisioning Studio
page_order: 3
description: "Erfahren Sie, wie Sie einen Klaviyo Flow für die Verwendung mit BrazeAI Decisioning <sup>StudioTM</sup> Go einrichten."
toc_headers: h2
---

# Konfigurieren Sie mit Klaviyo für BrazeAI Decisioning Studio™ Go

> Richten Sie ein Template für Platzhalter und einen Fluss in Klaviyo ein, um Aktivierungen über BrazeAI Decisioning Studio™ Go auszulösen.

{% alert important %}
Sie müssen für jeden neuen Experimentator, den Sie einrichten, einen neuen Ablauf in Klaviyo erstellen. Wenn Sie zuvor eine Platzhalter-Bewegung für den Import Ihrer Templates erstellt haben, müssen Sie eine neue Bewegung erstellen und können die vorherige Platzhalter-Bewegung nicht wiederverwenden.
{% endalert %}

Bevor Sie einen Fluss in Klaviyo erstellen, müssen Sie die folgenden Details aus Ihrem BrazeAI Decisioning Studio™ Go Portal referenzieren:

- Name des Flusses
- Name des triggernden Ereignisses

## Erstellen eines Templates für Platzhalter in Klaviyo

BrazeAI Decisioning Studio™ Go importiert Templates, die mit bestehenden Flows in Ihrem Klaviyo-Konto verknüpft sind. Wenn Sie ein Template verwenden möchten, das mit keiner Bewegung verknüpft ist, können Sie eine Platzhalterbewegung erstellen, die die Templates enthält, die Sie verwenden möchten. Der Fluss kann als Entwurf belassen werden; er muss nicht live sein.

### Schritt 1: Richten Sie Ihren Fluss ein

{% alert note %}
Der Zweck dieses Platzhalters besteht darin, die gewünschten Inhalte in BrazeAI Decisioning Studio™ Go zu importieren. Sie müssen in einem späteren Schritt einen separaten Ablauf erstellen, den BrazeAI Decisioning Studio™ Go verwendet, um Aktivierungen zu triggern, sobald Ihr Experimentator live ist.
{% endalert %}

1. Wählen Sie in Klaviyo **Flows** aus. 
2. Wählen Sie **Bewegung erstellen** > **Von Grund auf neu erstellen**.
3. Geben Sie dem Platzhalter Flow einen Namen, den Sie wiedererkennen, und wählen Sie dann **Flow erstellen**.

![Eine Bewegung namens "OFE Platzhalter Bewegung".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Wählen Sie einen beliebigen Trigger aus und speichern Sie dann den Fluss.
5\. Wählen Sie **Bestätigen und speichern**. 

### Schritt 2: Erstellen Sie das Template für den Platzhalter

Als nächstes erstellen Sie das Template für den Platzhalter: 

1. Ziehen Sie einen **E-Mail-Knoten** per Drag-and-Drop nach dem **Auslöser**.

![Ein Flow mit einem Trigger-Knoten gefolgt von einem E-Mail-Knoten.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. Wählen Sie im Knoten **E-Mail** die Option **Template auswählen**.
3\. Wählen Sie dann die zu verwendende Vorlage aus und wählen Sie **Vorlage verwenden**.
4\. Wählen Sie **Speichern** > **Erledigt**.
5\. (Optional) Um weitere Templates für BrazeAI Decisioning Studio™ Go hinzuzufügen, fügen Sie einen weiteren **E-Mail-Knoten** hinzu und wiederholen Sie die Schritte 2-4.
6\. Lassen Sie alle E-Mails im **Entwurfsmodus** und beenden Sie den Flow.

Im BrazeAI Decisioning Studio™ Go Portal sollten Ihre Templates unter Ihrem Platzhalterfluss ausgewählt werden können.

![Ein Beispiel eines Platzhalters für ein Klaviyo Template im Decisioning Studio Go Portal.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## Einen Fluss in Klaviyo erstellen

### Schritt 1: Richten Sie den Fluss ein

1. Wählen Sie in Klaviyo **Flows** > **Flow erstellen**.
2. Wählen Sie **Bauen Sie Ihr eigenes**.
3. Geben Sie bei **Name** den Namen des Flusses aus Ihrem BrazeAI Decisioning Studio™ Go Portal ein. Wählen Sie dann **Manuell erstellen** aus.

![Die Option "Manuell erstellen" wurde für eine Beispielsendung ausgewählt.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Wählen Sie den Auslöser aus.
5\. Stimmen Sie den Namen der Metrik mit dem Namen des triggernden Ereignisses in Ihrem BrazeAI Decisioning Studio™ Go Portal ab.

![Ein Beispiel für einen Metrikennamen, der dem Namen des triggernden Ereignisses entspricht "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Wählen Sie **Speichern**.

{% alert note %}
Wenn Ihr Experimentator über eine Basis-Template verfügt, fahren Sie mit den folgenden Schritten fort. Wenn Ihr Experimentator über zwei oder mehr Basis-Templates verfügt, fahren Sie mit [Schritt 3 fort: Fügen Sie einen Trigger-Split zu Ihrem Fluss hinzu](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

### Schritt 2: Fügen Sie eine E-Mail zu Ihrem Fluss hinzu 

1. Ziehen Sie einen **E-Mail-Knoten** per Drag-and-Drop hinter den **Auslöser-Knoten**.
2. Wählen Sie in den **Details der E-Mail** **Template auswählen**.

!["Template auswählen" im Bereich "E-Mail Details".]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Suchen und wählen Sie Ihre Basis-Template aus. Sie können Ihre Vorlage anhand des Vorlagennamens im Abschnitt " **Zu verwendende Ressourcen"** des BrazeAI Decisioning Studio™ Go-Portals suchen.

![Ein Beispiel für eine Basis-Vorlage in Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Wählen Sie **Template verwenden** > **Speichern**.
5\. Geben Sie in die **Betreffzeile** {% raw %}`{{event.SubjectLine}}`{% endraw %} ein.
6\. Geben Sie für den **Namen des Absenders** und die **E-Mail Adresse des Absenders** die gewünschten Details ein.

![Ein Beispiel für Betreffzeile, Absendername und Absender-E-Mail-Adresse für "E-Mail 1".]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Wählen Sie **Erledigt**.
8\. Deaktivieren Sie das Kontrollkästchen **Kürzlich gemailte Profile überspringen** und wählen Sie dann **Speichern**.
9\. Aktualisieren Sie im Knoten E-Mail den Modus von **Entwurf** auf **Live**.

![Der Klaviyo Flow Editor zeigt einen Trigger-Knoten, der mit einem E-Mail-Knoten verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

Jetzt können Sie loslegen! Sie können jetzt Aktivierungen über BrazeAI Decisioning Studio™ Go triggern. 

### Schritt 3: Fügen Sie einen Trigger-Split zu Ihrem Ablauf hinzu 

1. Ziehen Sie einen **geteilten Trigger-Knoten** per Drag-and-Drop hinter den **Trigger-Knoten**.
2. Wählen Sie den Knoten **Trigger Split** aus und setzen Sie die **Dimension** auf **EmailTemplateID**.

![Das Flussdiagramm von Klaviyo zeigt einen Trigger-Knoten, der einen mit der Dimension EmailTemplateID konfigurierten Trigger-Split speist.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### Schritt 3.1: Ihre E-Mail-Vorlage hinzufügen

1. Im BrazeAI Decisioning Studio™ Go-Portal finden Sie die **ID der E-Mail-Vorlage** für Ihre erste Vorlage unter dem Abschnitt **Zu verwendende Ressourcen**. Geben Sie die **ID der E-Mail-Vorlage** für das Feld **Dimension** ein und wählen Sie dann **Speichern**.
2. Ziehen Sie einen **E-Mail-Knoten** per Drag-and-Drop auf den Zweig **Ja** des **Trigger-Splits**. 

![Ein Klaviyo-Flow mit einem Trigger-Split-Knoten, der einen Ja-Zweig hat, der zu einem E-Mail-Knoten führt, und einen Nein-Zweig, der zu einem anderen Trigger-Split führt.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. Wählen Sie in den **Details der E-Mail** **Template auswählen**.
4\. Suchen und wählen Sie Ihre Basis-Template aus. Sie können Ihre Vorlage anhand des Namens der Basisvorlage im Abschnitt " **Zu verwendende Ressourcen"** des BrazeAI Decisioning Studio™ Go-Portals suchen.
5\. Wählen Sie **Template verwenden** > **Speichern**.
6\. Geben Sie in die **Betreffzeile** {% raw %}`{{event.SubjectLine}}`{% endraw %} ein.
7\. Geben Sie für den **Namen des Absenders** und die **E-Mail Adresse des Absenders** die gewünschten Details ein.

![Ein ausgewähltes Template für E-Mails und Felder für die Betreffzeile, den Absendernamen und die E-Mail-Adresse des Absenders.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Wählen Sie **Erledigt**.
9\. Deaktivieren Sie das Kontrollkästchen **Kürzlich gemailte Profile überspringen** und wählen Sie dann **Speichern**.
10\. Aktualisieren Sie im Knoten E-Mail den Modus von **Entwurf** auf **Live**.

#### Schritt 3.2: Einen neuen Trigger-Split hinzufügen

Als Nächstes erstellen Sie einen neuen **Trigger-Split** und einen **E-Mail-Knoten** für jede zusätzliche Basis-Vorlage, die Ihr Experimentator verwenden wird. 

1. Ziehen Sie per Drag-and-Drop einen weiteren **geteilten Trigger-Knoten** in den Zweig **Nein** des vorherigen **geteilten Trigger-Knotens**.
2. Setzen Sie die **Dimension** auf **EmailTemplateID** und geben Sie in den **Dimensionswert** die **ID** der **E-Mail-Vorlage** ein, die Sie einrichten möchten.
3. Wählen Sie **Speichern**.

![Das Diagramm eines Klaviyo Flow Editors zeigt einen Trigger-Knoten, der zu einem Trigger-Split führt. Der Trigger-Split hat einen Ja-Zweig, der zu einem E-Mail-Knoten führt, und einen Nein-Zweig, der mit einem anderen Trigger-Split verbunden ist, der zu weiteren E-Mail-Knoten führt.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Ziehen Sie einen Knoten **E-Mail** per Drag-and-Drop in den Zweig **Ja** Ihres neuen Triggersplits.
5\. Wiederholen Sie die Schritte 1-5 in [Schritt 3.1](#step-31-add-your-email-template), um das entsprechende Template auszuwählen.
5\. Setzen Sie die **Betreffzeile** auf {% raw %}`{{event.SubjectLine}}`{% endraw %}, und deaktivieren Sie das Kontrollkästchen **Zuletzt gemailte Profile überspringen**.
6\. Wiederholen Sie diesen Vorgang, bis Sie einen **Trigger-Split-Knoten** und einen **E-Mail-Knoten** für jede Basis-Vorlage haben, die Ihr Experimentator verwendet. Ihr letzter Trigger-Split sollte nichts im Branch "Nein" enthalten.

![Ein Klaviyo-Ablauf mit mehreren Trigger Split-Knoten, die zu mehreren E-Mail-Knoten verzweigen.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7\. Aktualisieren Sie in jedem Ihrer **E-Mail-Knoten** den Modus von **Entwurf** auf **Live**.

![Die Option zum Update des Knotenstatus auf "Live".]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

Jetzt können Sie loslegen! Sie können jetzt Aktivierungen über BrazeAI Decisioning Studio™ Go triggern. 