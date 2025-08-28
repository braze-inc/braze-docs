---
nav_title: Workshop
article_title: Amazon Personalize Workshop
alias: /partners/amazon_personalize_workshop/
description: "Dieser referenzierte Artikel beschreibt den Prozess der Konfiguration von Amazon Personalize und der Integration in Ihre Braze-Umgebung mit Hilfe von Connected-Content."
page_type: partner
search_tag: Partner
---

# Amazon Personalize Workshop

> Dieser referenzierte Artikel führt Sie durch die Konfiguration von Amazon Personalize und dessen Integration in Ihre Braze-Umgebung mit Connected-Content. Dies geschieht in einem praktischen Workshop, der Sie durch alle Schritte führt, die erforderlich sind, um Amazon Personalize Lösungen zu implementieren und zu trainieren und sie in eine Braze E-Mail Kampagne zu integrieren.

_Diese Integration wird von Amazon Personalize gepflegt._

## Über die Integration

Die folgenden Beispiele werden auf einer voll funktionsfähigen E-Commerce-Website mit dem Namen Retail Demo Store eingesetzt. Die Ressourcen und der Code für dieses Lernprogramm sind im [AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) veröffentlicht. Sie können diese referenzierte Architektur als Vorlage für die Implementierung von Amazon Personalize in Ihrer eigenen Umgebung verwenden.

## Anforderungen

Sie müssen das [Retail Demo Store Repository](https://github.com/aws-samples/retail-demo-store/) klonen und die beschriebenen Schritte befolgen, um die Workshop-Umgebung in Ihrem AWS-Konto bereitzustellen. Sie benötigen ein AWS-Konto, um den Workshop abzuschließen und den Integrationscode auszuführen.

## Architektur der Integration

Bevor Sie Braze für das Versenden personalisierter Nachrichten an Nutzer:innen einrichten, sollten Sie sich die relevanten Komponenten ansehen, die für eine typische E-Commerce Website erforderlich sind. Als Beispiel dient die Architektur des Einzelhandels-Demo-Shops.

![Ein Bild, das die Architektur der Personalisierung von Braze aufschlüsselt und zeigt, wie die verschiedenen Komponenten miteinander interagieren.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. Das Web UI des Retail Demo Store verwendet die AWS Amplify JavaScript Bibliothek, um Trainingsereignisse an Amazon Personalize zu senden.
2. Die Nutzer:innen von Braze Kampagnen werden über den Dienst Global Store User aktualisiert.
3. Wenn eine Braze Kampagne läuft, wird eine Connected-Content-Vorlage verwendet, um Empfehlungen von Personalize abzurufen und eine E-Mail-Vorlage für einen Nutzer:innen zusammenzustellen.
4. Informationen aus Produktkatalogen können auch dazu verwendet werden, Empfehlungsmodelle zu trainieren.

Braze sendet E-Mails an Ihre Nutzer:innen auf der Grundlage ihres Verhaltens oder der Attribute ihrer Nutzerprofile. Mit Hilfe dieser Daten können Nutzer:innen identifiziert und Nutzerprofile erstellt werden, um festzustellen, wann eine Nachricht oder E-Mail gesendet werden soll.

Dieser Ereignisdatenfluss erfolgt parallel zu den Verhaltensdaten, die an Amazon Personalize gesendet werden. In diesem Workshop verwendet der Demo Shop Amplify, um Ereignisse an Personalize zu senden. Diese Daten werden verwendet, um ein Empfehlungsmodell zu trainieren, das dann in den Aufrufen von Braze Connected-Content verwendet werden kann, um die Inhalte für Nutzer:innen zu personalisieren, wenn Ihre Kampagne in Braze läuft.

Braze Connected-Content wird diese Empfehlungen über einen in AWS laufenden Empfehlungsdienst abrufen können. Der Workshop "Retail Demo Store" zeigt ein Beispiel für die Bereitstellung eines Dienstes für Empfehlungen. In einem Einsatzszenario in Ihrer eigenen Infrastruktur müssen Sie einen ähnlichen Dienst einsetzen, um Artikel aus Ihrem eigenen Katalogdienst zu erhalten.

## Einrichten des Workshops für die referenzierte Architektur

### Schritt 1: Stellen Sie den Demo Shop für den Einzelhandel in Ihrem AWS Konto bereit

![Ein Bild der verfügbaren AWS Regionen.]({% image_buster /assets/img/amazon_personalize/region.png %}){: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

Wählen Sie in der folgenden Tabelle eine **AWS Region** und wählen Sie **Stack starten**. Diese Liste enthält nicht alle möglichen Regionen, in denen Sie das Projekt einsetzen können, sondern nur die derzeit konfigurierten Regionen für den Einsatz mit dem Retail Demo Store.

Übernehmen Sie alle Standard-Parameterwerte für das Template. Die Bereitstellung aller Projektressourcen sollte 25-30 Minuten dauern.

### Schritt 2: Erstellen Sie Amazon Personalize Kampagnen

Bevor Sie personalisierte Produktempfehlungen anbieten können, müssen Sie zunächst die Modelle des maschinellen Lernens trainieren und Endpunkte für die Inferenz bereitstellen, die es Ihnen erlauben, Empfehlungen von Amazon Personalize zu erhalten. Das in Schritt 1 bereitgestellte CloudFormation Template enthält eine Amazon SageMaker notebook Instanz, die ein Jupyter-Notizbuch mit detaillierten Schritt-für-Schritt-Anweisungen bereitstellt.

1. Melden Sie sich bei dem AWS-Konto an, in dem Sie die AWS CloudFormation-Vorlage in Schritt 1 bereitgestellt haben.
2. Wählen Sie in der Amazon SageMaker-Konsole **Notebook-Instanzen**.
3. Wenn Sie die Instanz **RetailDemoStore** notebook nicht sehen, stellen Sie sicher, dass Sie sich in derselben Region befinden, in der Sie das Projekt in Schritt 1 bereitgestellt haben.
4. Um auf die Instanz des Notebooks zuzugreifen, wählen Sie **Jupyter öffnen** oder **JupyterLab öffnen**.
5. Wenn die Jupyter-Webschnittstelle für die Instanz des Notizbuchs geladen ist, wählen Sie das `workshop/1-Personalization/1.1-Personalize.ipynb` Notizbuch. Möglicherweise müssen Sie den Ordner `workshop` wählen, um die Unterverzeichnisse der Notizbücher zu sehen.
6. Wenn Sie das `1.1-Personalize` Notizbuch geöffnet haben, gehen Sie durch den Workshop, indem Sie jede Zelle ausführen. Sie können in der Jupyter-Symbolleiste **Ausführen** wählen, um den Code in den Zellen sequentiell auszuführen. Die Bearbeitung des Notizbuchs dauert etwa zwei Stunden.

### Schritt 3: Senden Sie personalisierte E-Mails von Braze

Mit den Lösungen und Kampagnen von Amazon Personalize ist Ihre Instanz des Retail Demo Store bereit, Empfehlungen für Ihre E-Mail-Kampagnen zu geben. In Schritt 1 haben Sie die Demo-Webanwendung und alle zugehörigen Dienste bereitgestellt, einschließlich des Empfehlungsdienstes, der für die Integration Ihrer E-Mail Kampagnen mit Braze über Connected-Content benötigt wird. Dieser nutzt die Amazon Personalize Kampagnen, die Sie in Schritt 2 bereitgestellt haben.

Ähnlich wie der Workshop zur Personalisierung in Schritt 2 führt Sie der folgende Workshop zum Thema Messaging von Braze durch die Einrichtung der Integration von Braze und Amazon Personalize.

1. Melden Sie sich bei dem AWS-Konto an, in dem Sie die AWS CloudFormation-Vorlage in Schritt 1 bereitgestellt haben.
2. Wählen Sie in der Amazon SageMaker-Konsole **Notebook-Instanzen**.
3. Wenn Sie die Instanz **RetailDemoStore** notebook nicht sehen, stellen Sie sicher, dass Sie sich in derselben AWS-Region befinden, in der Sie das Projekt bereitgestellt haben.
4. Um auf die Instanz des Notebooks zuzugreifen, wählen Sie **Jupyter öffnen** oder **JupyterLab öffnen**.
5. Wenn die Jupyter-Webschnittstelle für die Instanz des Notizbuchs geladen ist, wählen Sie das `workshop/4-Messaging/4.2-Braze.ipynb` Notizbuch. Möglicherweise müssen Sie den Ordner `workshop` wählen, um die Unterverzeichnisse der Notizbücher zu sehen.
6. Wenn Sie das `4.2-Braze` Notizbuch geöffnet haben, gehen Sie durch den Workshop, indem Sie jede Zelle ausführen. Sie können in der Jupyter-Symbolleiste **Ausführen** wählen, um den Code in den Zellen sequentiell auszuführen. Die Bearbeitung des Notizbuchs dauert etwa 1 Stunde.

### Schritt 4: Ressourcen aufräumen

Um künftige Kosten zu vermeiden, löschen Sie die AWS-Ressourcen, die das Retail Demo Store-Projekt erstellt hat, indem Sie den AWS CloudFormation Stack löschen, den Sie in Schritt 1 erstellt haben.


