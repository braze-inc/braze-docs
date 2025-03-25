---
nav_title: Aufbewahrung von Daten
article_title: Aufbewahrung von Daten
alias: /data_retention/
description: "Dieser Referenzartikel enthält allgemeine Informationen zur Datenspeicherung bei Braze."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informationen zur Datenaufbewahrung von Braze

*Zuletzt überarbeitet am 1\. April 2024*

> Dieser Artikel enthält allgemeine Informationen zur Datenspeicherung bei Braze.<br><br>Die in Braze gespeicherten Daten werden aufbewahrt und können für die Segmentierung, Personalisierung und das Targeting während der gesamten Lebensdauer des Kundenkontos verwendet werden. Das bedeutet, dass Daten wie Benutzerprofilattribute, benutzerdefinierte Attribute, benutzerdefinierte Ereignisse und Käufe für aktive Benutzer auf unbestimmte Zeit gespeichert werden, es sei denn, sie werden vom Kunden für die Dauer des Vertrages entfernt.<br><br>Braze verfügt über Funktionen, Prozesse und APIs, um automatisch gute Datenhygienepraktiken für die Einhaltung von GDPR und anderen Best Practices zu implementieren. Diese werden im Folgenden beschrieben.

## Datenspeicherung durch Kunden über das Dashboard oder die API von Braze

Braze ermöglicht es seinen Kunden, komplette Benutzerprofile und Attributdaten selbst aus ihrem Arbeitsbereich zu löschen.

Das heißt, Sie können: 
- Löschen Sie Benutzerprofile mit dem [API-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) Braze [Delete user]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 
- Löschen (null) oder Ändern von Attributen in Benutzerprofilen mithilfe des Braze [Track Benutzer-API-Endpunkts]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Verhaltensereignisse können nicht aus einem Benutzerprofil gelöscht werden (benutzerdefinierte Ereignisse, Sitzungen, Kampagnen, Käufe). Um diese Ereignisse zu entfernen, müssen Sie das gesamte Benutzerprofil löschen.

Um den Datenschutz einzuhalten, müssen Sie möglicherweise alle personenbezogenen Daten eines Nutzers auf dessen Wunsch hin löschen. Eine Anleitung finden Sie auf unserer Seite für [technische Unterstützung beim Datenschutz]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure).

{% alert note %}
Ein Benutzer kann mehrere Profile haben, und Sie müssen möglicherweise mehrere Profile löschen, um alle Daten zu einem einzelnen Benutzer zu löschen. Folgen Sie den Anweisungen auf der Seite für technische Unterstützung zum Datenschutz, um alle Daten eines Benutzers vollständig zu löschen.
{% endalert %}

## Von Braze verwaltete Datenaufbewahrung für bestimmte Funktionen der Braze-Dienste

#### Braze Datenbank: Automatische Archivierung/Löschung von abgewanderten Benutzern

Braze führt jede Woche einen Prozess durch, um inaktive und ruhende Benutzer aus den Braze-Diensten zu entfernen. Im Allgemeinen handelt es sich dabei um Benutzer, die nicht erreichbar sind (z. B. keine E-Mail-Adresse, keine Telefonnummer, kein Push-Token, die Ihre Apps nicht verwenden oder Ihre Websites nicht besuchen), in deren Benutzerprofil keine Aktivitäten aufgezeichnet wurden und die keine Nachrichten erhalten haben oder mit denen Sie über Braze Kontakt aufgenommen haben. Dies geschieht, um die GDPR-Grundsätze und bewährte Verfahren einzuhalten. Mehr über diesen Prozess erfahren Sie auf unserer Seite [Definitionen der Benutzerarchivierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/).

{% alert note %}
Kunden haben die volle Kontrolle darüber, ob ein Benutzer inaktiv oder ruhend ist, und können die Archivierung von Benutzerprofilen verhindern, indem sie in regelmäßigen Abständen einen Datenpunkt aufzeichnen. Braze Canvas bietet die Möglichkeit, dies automatisch zu tun, so dass Sie diese Funktion für einige oder alle Ihrer inaktiven oder ruhenden Benutzer effektiv ausschalten können.
{% endalert %}

#### Daten zu Kampagnen und Canvas-Interaktionen 

Daten zur Interaktion mit einer Nachricht beziehen sich darauf, wie ein Benutzer mit einer Kampagne oder einem Canvas, das er erhalten hat, interagiert (z. B. wenn ein Benutzer die Kampagne A öffnet oder wenn ein Benutzer die Variante A erhält). Diese Daten werden für Retargeting verwendet. Weitere Informationen zur Verfügbarkeit von Messaging-Interaktionsdaten finden Sie unter [Über die Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data/).

## Datenspeicherung durch Braze verwaltet

Die folgenden Aufbewahrungsrichtlinien beziehen sich auf die Einhaltung der GDPR und der Datenschutzbestimmungen durch Braze und betreffen die vorübergehende Speicherung von Daten, die unsere internen Systeme durchlaufen. Diese Aufbewahrungsrichtlinien haben keinen Einfluss auf die Braze Services und dienen der Information Ihrer Rechts- und Datenschutzteams.

#### Braze Server: Kurzfristige Aufbewahrung für Einziehungszwecke

Daten, die von Braze an bestimmte Unterauftragsverarbeiter gesendet werden, können noch bis zu 90 Tage in den internen Systemen von Braze vorhanden sein.

#### Braze Data Lake Datenaufbewahrung

Die Daten, die den Kunden im Braze Dashboard zur Verfügung stehen, sind meist aggregiert. Detaillierte Protokolle werden in einer separaten, von Braze erstellten Datenbank (dem "Data Lake") gespeichert. Data Lake-Daten werden für aggregierte Berichte und andere erweiterte Funktionen verwendet. Braze entfernt persönlich identifizierbare Informationen aus den im Data Lake gespeicherten Ereignisdaten nach zwei Jahren (weitere Informationen finden Sie auf unserer Seite [Snowflake Data Retention]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention/) ).

Wenn Sie unsere APIs verwenden, um Benutzerprofile zu löschen oder Attribute von Benutzerprofilen zu löschen oder zu ändern, kann es bis zu drei Wochen dauern, bis diese Daten aus dem Data Lake von Braze gelöscht sind. Das Löschen von Daten im Data Lake wirkt sich nicht auf die Segmentierung oder Personalisierung aus, sondern stellt lediglich sicher, dass die Daten aus allen Braze-Systemen entfernt werden.

#### Braze Backup Server

Wenn Daten aus Ihrer Produktionsinstanz gelöscht werden, verbleiben die Daten sechs Monate lang auf den Backup-Servern von Braze und werden dann gemäß unseren internen Prozessen gelöscht.
