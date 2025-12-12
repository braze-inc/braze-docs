---
nav_title: Bindung von Daten
article_title: Datenaufbewahrung
alias: /data_retention/
description: "Dieser referenzierte Artikel enthält allgemeine Informationen zur Bindung von Daten bei Braze."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informationen zur Bindung von Daten durch Braze

*Zuletzt überarbeitet am 1\. April 2024*

> Dieser Artikel enthält allgemeine Informationen zur Bindung von Daten durch Braze.<br><br>Die in Braze gespeicherten Daten werden aufbewahrt und können für die Segmentierung, Personalisierung und das Targeting während der Lifetime des Kunden-Kontos verwendet werden. Das bedeutet, dass Daten wie Benutzerprofil-Attribute, angepasste Attribute, angepasste Events und Käufe für aktive Nutzer:in auf unbestimmte Zeit gespeichert werden, sofern sie nicht vom Kunden entfernt werden, und zwar für die Dauer des Vertrages.<br><br>Braze verfügt über Features, Prozesse und APIs, um automatisch gute Datenhygienepraktiken zur Einhaltung der DSGVO und anderer bewährter Praktiken zu implementieren. Diese werden im Folgenden beschrieben.

## Datenbindung durch Kunden über das Dashboard oder die API von Braze

Braze ermöglicht es seinen Kund:innen, komplette Nutzerprofile und Attribut-Daten selbst aus ihrem Workspace zu löschen.

Das heißt, Sie können: 
- Löschen von Nutzerprofilen mit dem Braze [Endpunkt Delete user API]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 
- Löschen (null) oder Ändern von Attributen in Nutzerprofilen über den Braze [Endpunkt Track user API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Verhaltensbezogene Events können nicht aus einem Nutzerprofil gelöscht werden (angepasste Events, Sitzungen, Kampagnen, Käufe). Um diese Ereignisse zu entfernen, müssen Sie das gesamte Profil der Nutzer:in löschen.

Um den Datenschutz zu gewährleisten, müssen Sie auf Anfrage des Nutzers alle personenbezogenen Daten des Nutzers löschen. Eine Anleitung finden Sie auf unserer Seite für [technische Unterstützung beim Datenschutz]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure).

{% alert note %}
Ein Nutzer:innen kann mehrere Profile haben, und Sie müssen möglicherweise mehrere Profile löschen, um alle Daten eines einzelnen Nutzers zu löschen. Befolgen Sie die Anweisungen auf der Seite der technischen Unterstützung zum Datenschutz, um alle Daten eines Nutzer:in vollständig zu löschen.
{% endalert %}

## Von Braze verwaltete Datenaufbewahrung für bestimmte Features der Serviceleistungen; Dienste

#### Braze Datenbank: Automatische Archivierung/Löschung abgewanderter Nutzer:in

Jede Woche führt Braze einen Prozess durch, um inaktive und ruhende Nutzer:innen aus den Serviceleistungen; Diensten zu entfernen. Im Allgemeinen handelt es sich dabei um Nutzer:innen, die nicht erreichbar sind (z.B. keine E-Mail-Adresse, keine Telefonnummer, kein Push-Token, die Ihre Apps nicht nutzen oder Ihre Websites nicht besuchen), die keine Aktivitäten in ihrem Nutzerprofil aufgezeichnet haben und mit denen kein Messaging oder Engagement über Braze stattgefunden hat. Dies geschieht, um die Grundsätze der DSGVO und bewährte Verfahren einzuhalten. Mehr über diesen Prozess erfahren Sie auf unserer Seite [Definitionen der Nutzerarchivierung]({{site.baseurl}}/user_archival/).

{% alert note %}
Kunden haben die volle Kontrolle darüber, ob ein Nutzer inaktiv oder ruhend ist, und können die Archivierung von Nutzerprofilen verhindern, indem sie in regelmäßigen Abständen einen Datenpunkt aufzeichnen. Braze-Canvas bietet die Möglichkeit, dies automatisch zu tun, so dass Sie diese Funktion für einige oder alle Ihrer inaktiven oder ruhenden Nutzer:innen effektiv ausschalten können.
{% endalert %}

#### Daten zu Kampagnen und Canvas-Interaktionen 

Messaging-Interaktionsdaten beziehen sich darauf, wie ein Nutzer mit einer Kampagne oder einem Canvas, das er erhalten hat, interagiert (z.B. wenn ein Nutzer die Kampagne A öffnet oder ein Nutzer die Variante A erhält). Diese Daten werden für das Retargeting verwendet. Weitere Informationen über die Verfügbarkeit von Messaging-Interaktionsdaten finden Sie unter [Über die Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data/).

## Von Braze verwaltete Bindung von Daten

Die folgenden Richtlinien zur Bindung von Daten beziehen sich auf die Einhaltung der DSGVO und der Datenschutzbestimmungen durch Braze und betreffen die vorübergehende Speicherung von Daten, die unsere internen Systeme durchlaufen. Diese Richtlinien zur Bindung haben keine Auswirkungen auf die Serviceleistungen; Dienste von Braze und dienen der Information Ihrer Teams für Recht und Datenschutz.

#### Braze Server: Kurzfristige Bindung für Einziehungszwecke

Daten, die von Braze an bestimmte Unterauftragsverarbeiter gesendet werden, können noch bis zu 90 Tage in den internen Systemen von Braze vorhanden sein.

#### Braze Data Lake Datenaufbewahrung

Die Daten, die den Kund:innen im Braze-Dashboard zur Verfügung stehen, sind größtenteils aggregiert. Detaillierte Protokolle werden in einer separaten, von Braze erstellten Datenbank (dem "Data Lake") gespeichert. Data Lake-Daten werden für aggregierte Berichte und andere fortschrittliche Funktionen verwendet. Braze entfernt persönlich identifizierbare Daten aus den im Data Lake gespeicherten Ereignisdaten nach zwei Jahren (weitere Informationen finden Sie auf unserer Seite [Snowflake Data Retention]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention/) ).

Wenn Sie unsere APIs verwenden, um Nutzerprofile zu löschen oder Attribute von Nutzerprofilen zu löschen oder zu ändern, kann es bis zu drei Wochen dauern, bis diese Daten aus dem Data Lake von Braze gelöscht werden. Das Löschen von Daten im Data Lake hat keinen Einfluss auf die Segmentierung oder Personalisierung, sondern stellt sicher, dass die Daten aus allen Braze-Systemen entfernt werden.

#### Braze Backup Server

Wenn Daten aus Ihrer Produktionsinstanz gelöscht werden, verbleiben die Daten sechs Monate lang auf den Backup-Servern von Braze und werden dann gemäß unseren internen Verfahren gelöscht.
