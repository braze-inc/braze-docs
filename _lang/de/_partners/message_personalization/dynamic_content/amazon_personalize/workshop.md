---
nav_title: Workshop
article_title: Amazon Personalisieren Workshop
alias: /partners/amazon_personalize_workshop/
description: "Dieser Referenzartikel beschreibt den Prozess der Konfiguration von Amazon Personalize und dessen Integration in Ihre Braze-Umgebung mithilfe von Connected Content."
page_type: partner
search_tag: Partner
---

# Amazon Workshop personalisieren

> Dieser Referenzartikel führt Sie durch den Prozess der Konfiguration von Amazon Personalize und der Integration in Ihre Braze-Umgebung mit Hilfe von Connected Content. Dies geschieht in einem praktischen Workshop, der Sie durch alle Schritte führt, die für die Bereitstellung und Schulung von Amazon Personalize-Lösungen und deren Integration in eine Braze-E-Mail-Kampagne erforderlich sind.

Die folgenden Beispiele werden in einer voll funktionsfähigen Beispiel-E-Commerce-Website namens Retail Demo Store eingesetzt. Die Ressourcen und der Code für dieses Lernprogramm sind im [AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) veröffentlicht. Sie können diese Referenzarchitektur-Implementierung als Vorlage für die Implementierung von Amazon Personalize in Ihrer eigenen Umgebung verwenden.

## Anforderungen

Sie müssen das [Retail Demo Store Repository](https://github.com/aws-samples/retail-demo-store/) klonen und die beschriebenen Schritte befolgen, um die Workshop-Umgebung in Ihrem AWS-Konto bereitzustellen. Sie benötigen ein AWS-Konto, um den Workshop zu absolvieren und den Integrationscode auszuführen.

## Architektur der Integration

Bevor Sie Braze so einrichten, dass es personalisierte Nachrichten an Benutzer sendet, sollten Sie sich die relevanten Komponenten ansehen, die für eine typische E-Commerce-Website erforderlich sind, wobei Sie die Architektur des Retail Demo Store als Beispiel verwenden.

![Ein Bild, das die Personalisierungsarchitektur von Braze aufschlüsselt und zeigt, wie die verschiedenen Komponenten miteinander interagieren.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. Die Web-UI des Retail Demo Store verwendet die AWS Amplify JavaScript-Bibliothek, um Trainingsereignisse an Amazon Personalize zu senden.
2. Die Datensätze von Braze-Kampagnenbenutzern werden über den Dienst Global Store User aktualisiert.
3. Wenn eine Braze-Kampagne läuft, wird eine Connected Content-Vorlage verwendet, um Empfehlungen von Personalize abzurufen und eine E-Mail-Vorlage für einen Zielbenutzer zu füllen.
4. Die Informationen aus dem Produktkatalog können auch zum Trainieren von Empfehlungsmodellen verwendet werden.

Braze sendet E-Mails an Ihre Benutzer auf der Grundlage ihres Verhaltens oder der Attribute ihrer Benutzerprofile. Diese Daten können helfen, Benutzer zu identifizieren und Benutzerprofile zu erstellen, um zu bestimmen, wann eine Nachricht oder E-Mail gesendet werden soll.

Dieser Ereignisdatenfluss erfolgt parallel zu den verhaltensbezogenen Ereignisdaten, die an Amazon Personalize gesendet werden. In diesem Workshop verwendet der Demo-Shop Amplify, um Ereignisse an Personalize zu senden. Diese Daten werden verwendet, um ein Empfehlungsmodell zu trainieren, das dann in Aufrufen von Braze Connected Content verwendet werden kann, um Inhalte für Benutzer zu personalisieren, wenn Ihre Braze-Kampagne läuft.

Braze Connected Content wird diese Empfehlungen über einen Empfehlungsdienst in AWS abrufen können. Der Workshop Retail Demo Store zeigt ein Beispiel für den Einsatz eines Empfehlungsdienstes. In einem Einsatzszenario in Ihrer eigenen Infrastruktur müssen Sie einen ähnlichen Dienst einrichten, um Objekte von Ihrem eigenen Katalogdienst zu erhalten.

## Einrichten des Workshops zur Referenzarchitektur

### Schritt 1: Stellen Sie den Retail Demo Store in Ihrem AWS-Konto bereit

![Ein Bild der verfügbaren AWS-Regionen.][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

Wählen Sie in der folgenden Tabelle eine **AWS-Region** und wählen Sie **Stack starten**. Diese Liste enthält nicht alle möglichen Regionen, in denen Sie das Projekt bereitstellen können, sondern nur die derzeit konfigurierten Regionen für die Bereitstellung mit dem Demo-Store für den Einzelhandel.

Übernehmen Sie alle Standardparameterwerte für die Vorlage. Die Bereitstellung aller Projektressourcen sollte 25-30 Minuten dauern.

### Schritt 2: Erstellen Sie Amazon Personalize-Kampagnen

Bevor Sie personalisierte Produktempfehlungen bereitstellen können, müssen Sie zunächst die maschinellen Lernmodelle trainieren und Inferenzendpunkte bereitstellen, die es Ihnen ermöglichen, Empfehlungen von Amazon Personalize zu erhalten. Die in Schritt 1 bereitgestellte CloudFormation-Vorlage enthält eine Amazon SageMaker notebook-Instanz, die ein Jupyter-Notizbuch mit detaillierten Schritt-für-Schritt-Anweisungen bereitstellt.

1. Melden Sie sich bei dem AWS-Konto an, in dem Sie die AWS CloudFormation-Vorlage in Schritt 1 bereitgestellt haben.
2. Wählen Sie in der Amazon SageMaker-Konsole **Notebook-Instanzen**.
3. Wenn Sie die Notebook-Instanz **RetailDemoStore** nicht sehen, stellen Sie sicher, dass Sie sich in derselben Region befinden, in der Sie das Projekt in Schritt 1 bereitgestellt haben.
4. Um auf die Notebook-Instanz zuzugreifen, wählen Sie **Jupyter öffnen** oder **JupyterLab öffnen**.
5. Wenn die Jupyter-Weboberfläche für die Notebook-Instanz geladen ist, wählen Sie das `workshop/1-Personalization/1.1-Personalize.ipynb` Notebook. Möglicherweise müssen Sie den Ordner `workshop` wählen, um die Unterverzeichnisse der Notizbücher zu sehen.
6. Wenn Sie das `1.1-Personalize` Notizbuch geöffnet haben, gehen Sie durch den Workshop, indem Sie jede Zelle ausführen. Sie können in der Jupyter-Symbolleiste **Ausführen** wählen, um den Code in den Zellen sequentiell auszuführen. Die Bearbeitung des Notizbuchs dauert etwa zwei Stunden.

### Schritt 3: Senden Sie personalisierte E-Mails von Braze

Wenn Sie die Amazon Personalize-Lösungen und -Kampagnen eingerichtet haben, ist Ihre Instanz des Retail Demo Store bereit, Empfehlungen für Ihre E-Mail-Kampagnen zu geben. In Schritt 1 haben Sie die Demo-Webanwendung und alle zugehörigen Services bereitgestellt, einschließlich des Empfehlungsdienstes, der für die Integration Ihrer E-Mail-Kampagnen mit Braze über Connected Content benötigt wird. Dieser nutzt die Amazon Personalize-Kampagnen, die Sie in Schritt 2 bereitgestellt haben.

Ähnlich wie der Workshop zur Personalisierung in Schritt 2 führt Sie der folgende Workshop zu Braze Messaging durch die Einrichtung der Integration von Braze und Amazon Personalize.

1. Melden Sie sich bei dem AWS-Konto an, in dem Sie die AWS CloudFormation-Vorlage in Schritt 1 bereitgestellt haben.
2. Wählen Sie in der Amazon SageMaker-Konsole **Notebook-Instanzen**.
3. Wenn Sie die Notebook-Instanz **RetailDemoStore** nicht sehen, stellen Sie sicher, dass Sie sich in der gleichen AWS-Region befinden, in der Sie das Projekt bereitgestellt haben.
4. Um auf die Notebook-Instanz zuzugreifen, wählen Sie **Jupyter öffnen** oder **JupyterLab öffnen**.
5. Wenn die Jupyter-Weboberfläche für die Notebook-Instanz geladen ist, wählen Sie das `workshop/4-Messaging/4.2-Braze.ipynb` Notebook. Möglicherweise müssen Sie den Ordner `workshop` wählen, um die Unterverzeichnisse der Notizbücher zu sehen.
6. Wenn Sie das `4.2-Braze` Notizbuch geöffnet haben, gehen Sie durch den Workshop, indem Sie jede Zelle ausführen. Sie können in der Jupyter-Symbolleiste **Ausführen** wählen, um den Code in den Zellen sequentiell auszuführen. Die Bearbeitung des Notizbuchs dauert etwa 1 Stunde.

### Schritt 4: Ressourcen aufräumen

Um zukünftige Kosten zu vermeiden, löschen Sie die AWS-Ressourcen, die das Retail Demo Store-Projekt erstellt hat, indem Sie den AWS CloudFormation-Stack löschen, den Sie in Schritt 1 erstellt haben.

[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}