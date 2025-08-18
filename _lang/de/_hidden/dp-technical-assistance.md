---
nav_title: Technische Unterstützung zum Datenschutz
article_title: Datenschutz Technische Unterstützung in den Braze Diensten
page_order: 1
description: "Diese Seite enthält technische Anweisungen, die es Ihnen ermöglichen, über die Braze Dienste Anfragen von Einzelpersonen in Bezug auf ihre Rechte an personenbezogenen Daten zu verwalten."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Datenschutz Technische Unterstützung in den Braze Diensten

Es gibt eine Reihe von Datenschutzgesetzen, die regeln, was Unternehmen mit personenbezogenen Daten tun dürfen ("Datenschutzgesetze"). Dazu zählen die DSGVO, der California Consumer Privacy Act ("CCPA") und der Health Insurance Portability and Accountability Act ("HIPAA"). Es gibt weitere nationale, bundesstaatliche und branchenspezifische Datenschutzgesetze und -vorschriften, die für Ihr Unternehmen gelten können.

Diese gewähren Einzelpersonen Persönlichkeitsrechte in Bezug auf ihre persönlichen Daten. Unternehmen sind verpflichtet, Anfragen von Personen, die ihre Datenschutzrechte ausüben, entgegenzunehmen und zu beantworten. Die Braze Dienste können Sie bei der Einhaltung dieser Datenschutzgesetze unterstützen, indem sie Features zur Verfügung stellen, die bestimmte, nach diesen Gesetzen vorgeschriebene Maßnahmen erleichtern. Dieses Dokument enthält technische Anweisungen zur Verwendung dieser Funktionen für die Verwaltung von Anfragen zu Datenschutzrechten. Es liegt an Ihnen, zu bestimmen, welche Datenschutzgesetze für Ihr Unternehmen gelten und wie Sie diese einhalten.

## Rechtlicher Hinweis

Nichts von dem, was im Folgenden beschrieben wird, ist als Rechtsberatung durch Braze gedacht und darf auch nicht als solche angesehen werden. Wir empfehlen Ihnen, sich in Bezug auf Ihre spezielle Situation und die Anwendung der Datenschutzgesetze auf Sie und Ihre Nutzung der Braze-Dienste von Ihrem eigenen Anwalt beraten zu lassen.

## Terminologie

In Sinne des vorliegenden Dokuments können Bezugnahmen auf personenbezogene Daten auch als Bezugnahmen auf persönliche Daten oder persönlich identifizierbare Informationen ("Persönliche Daten") verstanden werden. Der Einfachheit halber werden im Allgemeinen die Begriffe der DSGVO verwendet, wenn es um Endnutzerrechte geht. Die Begriffe der DSGVO entsprechen an vielen Stellen den Begriffen und Konzepten anderer Datenschutzgesetze.

## Die Grundlagen

Die meisten Datenschutzgesetze unterscheiden drei Hauptakteure, die an der Verarbeitung personenbezogener Daten beteiligt sind: die betroffenen Personen, die für die Datenverarbeitung Verantwortlichen und die Datenverarbeiter. Jede Gruppe hat unterschiedliche Rechte und Pflichten in Bezug auf die Verwendung persönlicher Daten:

- Eine betroffene Person ist eine Person, deren persönliche Daten von dem Datenverarbeiter oder dem für die Verarbeitung Verantwortlichen verarbeitet werden.
- Ein für die Datenverarbeitung Verantwortlicher ist eine Einrichtung, die die Zwecke und Mittel der Verarbeitung personenbezogener Daten festlegt
- Ein Datenverarbeiter ist ein Unternehmen, das personenbezogene Daten im Namen und auf Anweisung des Datenverantwortlichen verarbeitet.

In Bezug auf die Braze Dienste:

- Die betroffenen Personen sind z.B. die Endnutzer Ihrer Kundenanwendung (e.g., Ihre Kunden/Klienten) oder Ihre Mitarbeiter, die Dashboard-Nutzer in Ihrer Instanz der Braze Dienste sind.
- Sie, der Braze-Kunde, sind der für die Datenverarbeitung Verantwortliche, der entscheidet, wie und warum die persönlichen Daten der betroffenen Personen im Rahmen der Braze Serviceleistungen; Dienste; Dienste erhoben und verarbeitet werden.
- Braze ist ein Datenverarbeiter, der in Ihrem Auftrag und gemäß den Anweisungen, die wir von Ihnen erhalten, personenbezogene Daten in den Braze Diensten verarbeitet.

Bei den oben genannten Begriffen handelt es sich um Begriffe aus dem GDPR, aber vergleichbare Begriffe unter dem CCPA lauten zum Beispiel so:

- "Verbraucher" für betroffene Personen
- "Unternehmen" für die für die Datenverarbeitung Verantwortlichen
- "Dienstanbieter" für Datenverarbeiter

Im Folgenden finden Sie wichtige Informationen zu den häufigsten Anfragen von betroffenen Personen zu ihren Rechten auf Privatsphäre, einschließlich Informationen darüber, wie Sie über die technischen Features des Braze Dienstes auf diese Anfragen reagieren können.

## Das Recht, informiert zu werden

Das Auskunftsrecht umfasst Ihre Verpflichtung, Informationen über die "angemessene Verarbeitung" in der Regel mittels Datenschutzhinweis bereitzustellen. Es verlangt Transparenz darüber, wie Sie persönliche Daten verwenden.

### Braze Empfehlung

Die meisten Datenschutzgesetze betonen die Notwendigkeit von Transparenz im Zusammenhang mit der Verwendung personenbezogener Daten durch Sie. Dies liegt in der Verantwortung der für die Datenverarbeitung Verantwortlichen, die in der Regel einen Datenschutzhinweis bereithalten, der für die Nutzer ihrer Produkte und Dienstleistungen leicht zugänglich ist und die von Braze durchgeführte Verarbeitung abdeckt.

## Das Recht auf Zugang

Gemäß den Datenschutzgesetzen haben die betroffenen Personen das Recht,...

- ...zu erfahren, dass ihre persönlichen Daten verarbeitet werden
- Zugang zu ihren persönlichen Daten zu erhalten
- Andere ergänzende Informationen, die durch das geltende Datenschutzgesetz festgelegt sind.

### Braze Empfehlung

Um personenbezogene Daten von Braze in einem maschinenlesbaren Format als Antwort auf die Zugriffsanfrage einer betroffenen Person zur Verfügung zu stellen, können Sie deren Endbenutzerprofil exportieren, indem Sie einen API-Aufruf an die [REST-APIs](https://www.braze.com/docs/api/endpoints/export/#user-export) von Braze mit entweder ihrer Benutzerkennung (von Ihnen definiert als die `external_id`, die Braze zur Verfügung gestellt wurde) und/oder ihrer Gerätekennung tätigen.

## Das Recht auf Berichtigung

Einzelpersonen haben das Recht, personenbezogene Daten zu korrigieren, wenn diese unrichtig oder unvollständig sind. Wenn Sie die betreffenden personenbezogenen Daten an Dritte weitergegeben haben, halten Sie es für notwendig, diese über die Berichtigung zu informieren, sofern dies möglich ist.

### Braze Empfehlung

Für den Fall, dass eine betroffene Person Sie auffordert, Ungenauigkeiten in den von Ihnen oder von Braze in Ihrem Namen verarbeiteten personenbezogenen Daten zu berichtigen, können Sie die Braze SDKs oder die Braze [REST APIs](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) verwenden, um diese personenbezogenen Daten zu korrigieren.

## Das Recht auf Löschung

Das Recht auf Löschung ist auch als "Recht auf Vergessenwerden" oder "Recht auf Löschung" bekannt.

### Braze Empfehlung

#### Standardlöschung 

Sobald Sie die Datenerfassung gestoppt haben, können Sie [den Endpunkt User Deletion REST API von Braze](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) verwenden, um einen Endnutzer zu löschen. Dadurch werden alle Datensätze dieses Endnutzers aus den Serviceleistungen; Diensten von Braze entfernt:

- Für Endnutzer:innen, die eine external_id innerhalb der Braze Dienste; Dienste haben, können Sie diese ID verwenden, um die Daten dieser Endnutzer:innen zu löschen.
- Bei anonymen Endnutzern, die keine external_id innerhalb der Braze Dienste haben, können Sie den Bezeichner des Geräts dieses Endnutzers mit dem Braze SDK abrufen und den Bezeichner des Geräts verwenden, um das Profil des Endnutzers zu finden, das mit diesem Gerät verbunden ist. Mit der User Deletion API können Sie das jeweilige Profil löschen.

Wenn Sie ein Nutzerkonto löschen, wird das entsprechende Braze-Benutzerprofil mit der `external_id` dauerhaft gelöscht. Dazu gehören strukturierte Profildaten, die Braze standardmäßig erfasst hat oder die Sie für die Erfassung der Braze-Dienste konfiguriert haben, wie z. B. Geräteinformationen, Land, Sprache und E-Mail-Adresse.

Beachten Sie, dass die E-Mail-Adresse oder die Telefonnummer, die mit dem Profil des Endbenutzers verknüpft sind, von Braze trotzdem gespeichert werden könnten, da sie mit dem Profil eines anderen Endbenutzers verknüpft sein könnten. E-Mail-Adressen und Telefonnummern sind in den Braze Services nicht eindeutig. Das bedeutet, dass Ihr Team Braze so konfiguriert haben könnte, dass dieselbe E-Mail-Adresse oder Telefonnummer in mehreren Benutzerprofilen gespeichert wird. Wenn Ihr Team Braze auf diese Weise konfiguriert hat, sollten Sie sich darüber im Klaren sein, dass Sie möglicherweise alle Benutzerprofile, die eine bestimmte betroffene Person repräsentieren, löschen müssen, um der Aufforderung einer betroffenen Person zur Löschung nachzukommen, und dass Ihr Team mehrere API-Aufrufe tätigen muss, um alle Benutzerprofile zu löschen, die sich auf eine bestimmte betroffene Person beziehen.

#### Zusätzliche Überlegungen zur Löschung

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
<tbody>
  <tr>
    <td>
        <p>Kunden können benutzerdefinierte Felder für Ereigniseigenschaften und Nachrichtenextras erstellen. Diese Felder sind nicht für personenbezogene Daten vorgesehen. Daher werden diese Felder nicht in den oben beschriebenen Standard-Löschvorgang einbezogen. Wenn Sie mit Braze persönliche Daten über Ereigniseigenschaften und Nachrichtenextras eingeben oder sammeln, können Sie den Löschvorgang, der durch den REST-API-Endpunkt User Deletion ausgelöst wird, so konfigurieren, dass er auch diese Felder berücksichtigt und die darin enthaltenen Daten ebenfalls löscht.</p>
        <p>Die Standardeinstellungen werden auf Unternehmensebene angewendet. Sie können aber auch die folgenden Felder löschen, wenn der Löschvorgang auf der Ebene von Anwendungsgruppe oder Workspace erfolgt:</p>
    <ul>
        <li>PROPERTIES für USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES for USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS für:</li>
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Zukünftige Ereignisse beim Nachrichtenversand</li>
            </ul>
    </ul>
    <p>Auf diese Einstellungen können Sie über <b>Unternehmenseinstellungen</b> > <b>Admin-Einstellungen</b> > <b>Sicherheitseinstellungen</b> zugreifen. Die Einstellungen zur Datenlöschung werden je Ereignistyp oder Kategorie festgelegt. Nur ein Benutzer mit Administratoreinstellungen kann Änderungen an diesen Einstellungen vornehmen. Alternativ kann ein Administrator diese Berechtigungen auch an einen anderen Benutzer delegieren.</p>
    <p>Wenn ein Ereignistyp oder ein Nachrichtenextra so eingestellt ist, dass es in den Löschvorgang einbezogen wird, werden die Daten in diesem Feld bei Nutzern, für die Sie einen REST-API-Endpunkt User Delet ausführen, künftig gelöscht. Wenn Sie diese Löschpräferenz wählen, werden außerdem beim nächsten geplanten Löschauftrag die Daten aus diesen Feldern aus allen bestehenden anonymisierten Datensätzen, die diese Felder enthalten, gelöscht. Eine Wiederherstellung der gelöschten Datenfelder ist nicht möglich.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analytics

Um die Integrität von Analysen der Kampagnen- und Anwendungsnutzung zu wahren, werden keine anonymen aggregierten Daten verändert, wenn ein Endnutzer gelöscht wird. Braze verringert zum Beispiel nicht die Gesamtzahl der Sitzungen einer App, wenn ein Endnutzer gelöscht wird. Die Sitzung(en), in denen ein solcher Endnutzer die App besucht hat, wird/werden weiterhin in die Gesamtzahl der Besuche dieser App einbezogen, aber diese Daten werden in keiner Weise mit dem Profil des vergessenen Endnutzers in Verbindung gebracht, so dass sichergestellt ist, dass diese anonymisierten und aggregierten Daten nicht mit einem einzelnen Endnutzer in Verbindung gebracht werden können.

Die Analysen innerhalb der Braze-Services sind an die Braze-Endbenutzer-Kennung gebunden. Wenn ein Nutzerprofil gelöscht wurde, wird die Braze-Nutzerkennung vollständig anonymisiert, da Braze sie keinem bestimmten Endnutzer mehr zuordnen kann.

#### Nach der Löschung

Im Allgemeinen wird von Ihnen erwartet, dass Sie sich in angemessener Weise bemühen, die betroffenen Personen zu benachrichtigen, wenn Sie ihrer Bitte um Löschung ihrer persönlichen Daten nachgekommen sind. Ein gelöschter Endbenutzer kann sich zu einem späteren Zeitpunkt erneut registrieren oder mit Ihrer App oder Ihrem Service in Kontakt treten, und Braze kann ihn nicht als den gelöschten oder vergessenen Benutzer identifizieren. Die Braze Services sind nicht in der Lage, in Ihrem Namen Listen mit gelöschten Benutzerkennungen oder E-Mail-Adressen zu erstellen.

## Das Recht auf Einschränkung der Verarbeitung

Betroffene Personen sind unter bestimmten Umständen berechtigt, die Verarbeitung ihrer persönlichen Daten zu blockieren oder zu verhindern. Die Einschränkung der Verarbeitung bedeutet, dass eine Verarbeitung, gegen die eine betroffene Person Einspruch erhoben hat, nicht durchgeführt wird.

### Braze Empfehlung

Bei Braze ist eine Einschränkung der Verarbeitung einzelner Kategorien personenbezogener Daten nicht möglich. Wenn Sie von einer betroffenen Person gebeten wurden, die Verarbeitung bestimmter Untergruppen der personenbezogenen Daten dieser Person einzuschränken, sollten Sie die [Braze-APIs](https://www.braze.com/docs/api/home/) verwenden, um das gesamte Profil bzw. die gesamten Profile dieses Endbenutzers zu exportieren und es dann aus Braze [zu löschen](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint). Die APIs von Braze können verwendet werden, um diese Daten wieder zu importieren, falls der Endnutzer Ihnen später erlaubt, diese speziellen Untergruppen seiner persönlichen Daten zu verarbeiten. Darüber hinaus sollten Sie grundsätzlich empfehlen, alle Anwendungen, die das Braze SDK verwenden, zu deinstallieren oder sich davon abzumelden, damit keine weiteren Daten über die betroffene Person gesammelt werden.

## Das Recht auf Datenübertragbarkeit

Das Recht auf Datenübertragbarkeit ermöglicht es den betroffenen Personen, ihre persönlichen Daten für ihre eigenen Zwecke über verschiedene Dienste hinweg zu erhalten und wiederzuverwenden. Die persönlichen Daten sollten in einem strukturierten, maschinenlesbaren und gängigen Format bereitgestellt werden.

### Braze Empfehlung

Ähnlich wie beim Auskunftsrecht können Sie die [REST-API](https://www.braze.com/docs/api/endpoints/export/#user-export) von Braze verwenden, um die persönlichen Daten eines Endbenutzers zu exportieren und sie der betroffenen Person auf deren Anfrage hin zur Verfügung zu stellen.

## Widerspruchsrecht

Einzelpersonen sind berechtigt, Widerspruch einzulegen gegen:

- Verarbeitung auf der Grundlage berechtigter Interessen oder der Wahrnehmung einer Aufgabe im öffentlichen Interesse/Ausübung öffentlicher Gewalt (einschließlich Profiling);
- Direktmarketing (einschließlich Profiling); und
- Verarbeitung zu Zwecken der wissenschaftlichen/historischen Forschung und Statistik.

### Braze Empfehlung

Braze bietet die Möglichkeit, ein Benutzerprofil als von SMS, E-Mails oder Push-Benachrichtigungen abgemeldet zu markieren, sowohl über unsere [REST-APIs](https://www.braze.com/docs/api/home/) als auch über die [iOS-](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android-](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) und [Web-SDKs](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Wenn Sie von betroffenen Personen Einwände gegen den Erhalt solcher Nachrichten erhalten, können Sie die APIs von Braze verwenden, um diese Endnutzer abzumelden.

Wenn dies nicht ausreicht, um die Verarbeitung der persönlichen Daten durch Braze zu verhindern, sollte das Nutzerprofil wie unter "Recht auf Löschung" gelöscht werden.

## Rechte in Bezug auf automatisierte Entscheidungsfindung und Profiling

Einige Datenschutzgesetze verhindern automatisierte Entscheidungsfindung oder Profiling unter bestimmten Umständen, insbesondere bei Entscheidungen, die "eine rechtliche Wirkung oder eine ähnlich erhebliche Auswirkung auf die betroffene Person haben", oder ermöglichen es den betroffenen Personen, sich dagegen zu entscheiden.

### Braze Empfehlung

Braze führt keine automatisierte Profilerstellung oder Entscheidungsfindung durch, die rechtliche oder gleichwertige Auswirkungen auf die betroffenen Personen hat. Wenn Sie der Meinung sind, dass Ihre eigene Nutzung der Braze Serviceleistungen; Dienste rechtliche oder gleichwertige Auswirkungen hat und Sie einen entsprechenden Widerspruch erhalten haben, können Sie das Nutzerprofil in der gleichen Weise wie unter dem "Recht auf Löschung" löschen.

## Zielgerichtete Werbung

Nach den Datenschutzgesetzen einiger US-Bundesstaaten können Betroffene der Verwendung ihrer persönlichen Daten für gezielte Werbezwecke widersprechen.

### Braze Empfehlung

Bei der Erstellung von Zielgruppen für die gezielte Werbung für Ihre betroffenen Personen sollten Sie sicherstellen, dass Sie alle betroffenen Personen ausgeschlossen haben, die einer gezielten Werbung widersprochen haben, z. B. kalifornische Verbraucher, die ihr Recht auf "Nicht verkaufen oder weitergeben" gemäß dem CCPA ausgeübt haben.

Weitere Informationen zur Erstellung von Zielgruppen, die mit Plattformen von Drittanbietern synchronisiert werden können, finden Sie unter [Zielgruppensynchronisierung](https://www.braze.com/docs/partners/canvas_steps).

## Das Recht auf Nicht-Diskriminierung 

Betroffene Personen haben das Recht, ihre Datenschutzrechte auszuüben, ohne diskriminiert zu werden.

### Braze Empfehlung

Bei der Nutzung von Braze ist darauf zu achten, dass keine betroffenen Personen diskriminiert werden, die ihre Datenschutzrechte ausüben. So empfehlen wir beispielsweise, dass betroffene Personen, die von ihren Persönlichkeitsrechten Gebrauch machen, nicht in Zielgruppen segmentiert oder anderweitig in einer Weise angesprochen werden, die sie diskriminieren könnte.