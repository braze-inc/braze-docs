---
nav_title: Technische Unterstützung zum Datenschutz
article_title: Technische Unterstützung zum Datenschutz
page_order: 1
description: "Auf dieser Seite finden Sie technische Anweisungen, die es Ihnen ermöglichen, über die Braze-Plattform Anfragen von Einzelpersonen in Bezug auf ihre persönlichen Datenrechte zu verwalten."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Technische Unterstützung zum Datenschutz

Es gibt eine Reihe von Datenschutzgesetzen, die regeln, was Organisationen mit personenbezogenen Daten tun dürfen ("Datenschutzgesetze"), darunter die EU und UK General Data Protection Regulation ("GDPR"), der California Consumer Privacy Act ("CCPA") und der Health Insurance Portability and Accountability Act ("HIPAA"). Es gibt weitere nationale, bundesstaatliche und branchenspezifische Datenschutzgesetze und -vorschriften, die für Ihr Unternehmen gelten können.

Diese Datenschutzgesetze gewähren Einzelpersonen "Rechte auf Privatsphäre" über ihre persönlichen Daten. Organisationen sind verpflichtet, Anfragen von Personen, die ihre Datenschutzrechte wahrnehmen, entgegenzunehmen und zu beantworten. Die Braze-Plattform kann Sie bei der Einhaltung dieser Datenschutzgesetze unterstützen, indem sie Funktionen zur Erleichterung bestimmter Maßnahmen bereitstellt, die gemäß diesen Gesetzen erforderlich sind. Dieses Dokument enthält technische Anweisungen zur Verwendung dieser Funktionen für die Verwaltung von Anfragen zu Datenschutzrechten. Es liegt an Ihnen, zu bestimmen, welche Datenschutzgesetze für Ihr Unternehmen gelten und wie Sie diese einhalten.

## Rechtlicher Hinweis

Nichts von dem, was im Folgenden beschrieben wird, ist als Rechtsberatung durch Braze gedacht und darf auch nicht als solche angesehen werden. Wir empfehlen Ihnen, sich in Bezug auf Ihre spezielle Situation und die Anwendung der Datenschutzgesetze auf Sie und Ihre Nutzung der Braze-Dienste von Ihrem eigenen Anwalt beraten zu lassen.

## Terminologie

Für die Zwecke dieses Dokuments kann jede Bezugnahme auf personenbezogene Daten auch als Bezugnahme auf persönliche Informationen oder persönlich identifizierbare Informationen ("Persönliche Daten") verstanden werden. Der Einfachheit halber verlassen wir uns im Allgemeinen auf die Sprache der DSGVO, wenn es um die Rechte der Endnutzer geht. Die Sprache der DSGVO ist oft austauschbar oder eng an einen definierten Begriff oder ein Konzept aus anderen Datenschutzgesetzen angelehnt.

## Die Grundlagen

Die meisten Datenschutzgesetze definieren drei Hauptakteure, die an der Verarbeitung personenbezogener Daten beteiligt sind: die betroffenen Personen, die für die Datenverarbeitung Verantwortlichen und die Datenverarbeiter. Jede Gruppe hat unterschiedliche Rechte und Pflichten in Bezug auf die Verwendung persönlicher Daten:

- Eine betroffene Person ist eine Person, deren persönliche Daten von dem Datenverarbeiter oder dem für die Verarbeitung Verantwortlichen verarbeitet werden.
- Ein für die Datenverarbeitung Verantwortlicher ist eine Einrichtung, die die Zwecke und Mittel der Verarbeitung personenbezogener Daten festlegt
- Ein Datenverarbeiter ist ein Unternehmen, das personenbezogene Daten im Namen und auf Anweisung des Datenverantwortlichen verarbeitet.

In Bezug auf die Braze-Plattform:

- Bei den betroffenen Personen handelt es sich zum Beispiel um die Endnutzer Ihrer Kundenanwendung (e.g., Ihre Kunden/Klienten) oder Ihre Mitarbeiter, die Dashboard-Nutzer in Ihrer Instanz der Braze-Plattform sind.
- Sie, der Braze-Kunde, sind der für die Datenverarbeitung Verantwortliche, der entscheidet, wie und warum die persönlichen Daten der betroffenen Personen innerhalb der Braze-Plattform gesammelt und verarbeitet werden.
- Braze ist ein Datenverarbeiter, der in Ihrem Auftrag und gemäß den Anweisungen, die wir von Ihnen erhalten, persönliche Daten auf der Braze-Plattform verarbeitet.

Bei den oben genannten Begriffen handelt es sich um Begriffe aus dem GDPR, aber vergleichbare Begriffe unter dem CCPA lauten zum Beispiel so:

- "Verbraucher" für betroffene Personen.
- "Unternehmen" für die für die Datenverarbeitung Verantwortlichen.
- "Dienstanbieter" für Datenverarbeiter.

Nachfolgend finden Sie relevante Informationen zu den häufigsten Datenschutzanfragen von betroffenen Personen, einschließlich Informationen darüber, wie Sie mit Hilfe der technischen Funktionen der Braze-Plattform darauf reagieren können.

## Das Recht, informiert zu werden

Das Recht, informiert zu werden, umfasst Ihre Verpflichtung, Informationen über eine "faire Verarbeitung" bereitzustellen, in der Regel durch einen Datenschutzhinweis. Sie unterstreicht die Notwendigkeit der Transparenz darüber, wie Sie persönliche Daten verwenden.

### Braze Empfehlung

Die meisten Datenschutzgesetze betonen die Notwendigkeit von Transparenz im Zusammenhang mit der Verwendung personenbezogener Daten durch Sie. Dies liegt in der Verantwortung der für die Datenverarbeitung Verantwortlichen, die in der Regel einen Datenschutzhinweis bereithalten, der für die Nutzer ihrer Produkte und Dienstleistungen leicht zugänglich ist und die von Braze durchgeführte Verarbeitung abdeckt.

## Das Recht auf Zugang

Gemäß den Datenschutzgesetzen haben die betroffenen Personen das Recht auf Auskunft:

- Bestätigung, dass ihre persönlichen Daten verarbeitet werden,
- Zugang zu ihren persönlichen Daten, und
- Andere ergänzende Informationen, die durch das geltende Datenschutzgesetz festgelegt sind.

### Braze Empfehlung

Um personenbezogene Daten von Braze in einem maschinenlesbaren Format als Antwort auf die Zugriffsanfrage einer betroffenen Person zur Verfügung zu stellen, können Sie deren Endbenutzerprofil exportieren, indem Sie einen API-Aufruf an die [REST-APIs](https://www.braze.com/docs/api/endpoints/export/#user-export) von Braze mit entweder ihrer Benutzerkennung (von Ihnen definiert als die `external_id`, die Braze zur Verfügung gestellt wurde) und/oder ihrer Gerätekennung tätigen.

## Das Recht auf Berichtigung

Einzelpersonen haben das Recht, personenbezogene Daten zu korrigieren, wenn diese ungenau oder unvollständig sind. Wenn Sie die betreffenden personenbezogenen Daten an Dritte weitergegeben haben, halten Sie es für notwendig, diese über die Berichtigung zu informieren, sofern dies möglich ist.

### Braze Empfehlung

Für den Fall, dass eine betroffene Person Sie auffordert, Ungenauigkeiten in den von Ihnen oder von Braze in Ihrem Namen verarbeiteten personenbezogenen Daten zu berichtigen, können Sie die Braze SDKs oder die Braze [REST APIs](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) verwenden, um diese personenbezogenen Daten zu korrigieren.

## Das Recht auf Löschung

Das Recht auf Löschung ist auch als "Recht auf Vergessenwerden" oder "Recht auf Löschung" bekannt.

### Braze Empfehlung

#### Standard-Löschung 

Sobald Sie die Datenerfassung gestoppt haben, können Sie [den REST-API-Endpunkt User Deletion von Braze](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) verwenden, um einen Endbenutzer zu löschen, wodurch alle Datensätze dieses Endbenutzers aus den Services von Braze entfernt werden:

- Bei Endbenutzern, die eine external_id in den Diensten haben, können Sie diese ID verwenden, um die Daten dieses Endbenutzers zu löschen.
- Für anonyme Endbenutzer, die keine externe_id innerhalb der Services haben, können Sie die Gerätekennung dieses Endbenutzers mit dem Braze SDK abrufen und die Gerätekennung verwenden, um das mit diesem Gerät verbundene Endbenutzerprofil zu finden. Sie können dann die Benutzerlöschungs-API verwenden, um das mit diesem Endbenutzer verbundene Profil zu löschen.

Wenn Sie einen Endbenutzer aus den Braze-Diensten löschen, wird das zentralisierte Benutzerprofil von Braze für diesen Endbenutzer, wie unter `external_id` definiert, dauerhaft gelöscht. Dazu gehören strukturierte Profildaten, die Braze standardmäßig erfasst hat oder die Sie für die Erfassung der Braze-Dienste konfiguriert haben, wie z. B. Geräteinformationen, Land, Sprache und E-Mail-Adresse.

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
        <p>Kunden können benutzerdefinierte Felder für Ereigniseigenschaften und Nachrichtenextras erstellen. Diese Felder sind nicht für personenbezogene Daten vorgesehen. Daher werden diese Felder nicht in den oben beschriebenen Standard-Löschvorgang einbezogen. Wenn Sie jedoch Braze verwenden, um persönliche Daten über Ereigniseigenschaften und Nachrichtenextras einzugeben oder zu sammeln, können Sie den Löschvorgang, der durch den REST-API-Endpunkt Benutzerlöschung ausgelöst wird, so einrichten, dass er auch diese Felder umfasst, so dass die in diesen Feldern enthaltenen Daten ebenfalls gelöscht werden.</p>
        <p>Die Standardeinstellungen werden auf Unternehmensebene angewendet, aber Sie können sich dafür entscheiden, die folgenden Felder zu löschen, wenn der Löschvorgang auf der Ebene der Anwendungsgruppe/des Arbeitsbereichs ausgeführt wird:</p>
    <ul>
        <li>PROPERTIES für USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES für USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS für:</li>
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_NACHRICHTEN_WEBHOOK_SENDEN</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Zukünftige Ereignisse beim Senden von Nachrichten</li>
            </ul>
    </ul>
    <p>Auf diese Einstellungen können Sie über <b>Unternehmenseinstellungen</b> > <b>Admin-Einstellungen</b> > <b>Sicherheitseinstellungen</b> zugreifen. Die Einstellungen zum Löschen von Daten werden pro Ereignistyp oder Kategorie festgelegt. Nur ein Benutzer mit Administratoreinstellungen kann Änderungen an diesen Einstellungen vornehmen. Alternativ kann ein Administrator diese Berechtigungen auch an einen anderen Benutzer delegieren.</p>
    <p>Wenn ein Ereignistyp oder ein Nachrichtenextra so eingestellt ist, dass es in den Löschvorgang einbezogen wird, werden die Daten in diesem Feld für Benutzer, für die Sie einen Benutzerlösch-REST-API-Endpunkt ausführen, in Zukunft gelöscht. Wenn Sie diese Löschpräferenz wählen, werden außerdem beim nächsten geplanten Löschauftrag die Daten aus diesen Feldern aus allen bestehenden anonymisierten Datensätzen, die diese Felder enthalten, gelöscht. Eine Wiederherstellung der gelöschten Datenfelder ist nicht möglich.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analytik

Um die Integrität der Kampagnen- und Anwendungsnutzungsanalyse zu wahren, werden anonyme, aggregierte Daten nicht verändert, wenn ein Endnutzer gelöscht wird. Braze verringert zum Beispiel nicht die Gesamtzahl der Sitzungen einer App, wenn ein Endbenutzer gelöscht wird. Die Sitzung(en), in denen ein solcher Endnutzer die App besucht hat, wird/werden weiterhin in die Gesamtzahl der Besuche dieser App einbezogen, aber diese Daten werden in keiner Weise mit dem Profil des vergessenen Endnutzers in Verbindung gebracht, so dass sichergestellt ist, dass diese anonymisierten und aggregierten Daten nicht mit einem einzelnen Endnutzer in Verbindung gebracht werden können.

Die Analysen innerhalb der Braze-Services sind an die Braze-Endbenutzer-Kennung gebunden. Nachdem das Profil des Endbenutzers gelöscht wurde, wird die Braze-Benutzerkennung zu einer vollständig anonymisierten Kennung, da Braze nicht in der Lage ist, sie einem einzelnen Endbenutzer zuzuordnen.

#### Sobald die Löschung stattgefunden hat

Im Allgemeinen wird von Ihnen erwartet, dass Sie sich in angemessener Weise bemühen, die betroffenen Personen zu benachrichtigen, wenn Sie ihrer Bitte um Löschung ihrer persönlichen Daten nachgekommen sind. Ein gelöschter Endbenutzer kann sich zu einem späteren Zeitpunkt erneut registrieren oder mit Ihrer App oder Ihrem Service in Kontakt treten, und Braze kann ihn nicht als den gelöschten oder vergessenen Benutzer identifizieren. Die Braze Services sind nicht in der Lage, in Ihrem Namen Listen mit gelöschten Benutzerkennungen oder E-Mail-Adressen zu erstellen.

## Das Recht auf Einschränkung der Verarbeitung

Betroffene Personen können unter bestimmten Umständen das Recht haben, die Verarbeitung ihrer persönlichen Daten zu blockieren oder zu unterdrücken. Die Einschränkung der Verarbeitung bedeutet, dass eine Verarbeitung, gegen die eine betroffene Person Einspruch erhoben hat, nicht durchgeführt wird.

### Braze Empfehlung

Die Braze-Dienste unterstützen nicht die Einschränkung der Verarbeitung einzelner Kategorien von personenbezogenen Daten. Wenn Sie von einer betroffenen Person gebeten wurden, die Verarbeitung bestimmter Untergruppen der personenbezogenen Daten dieser Person einzuschränken, sollten Sie die [Braze-APIs](https://www.braze.com/docs/api/home/) verwenden, um das gesamte Profil bzw. die gesamten Profile dieses Endbenutzers zu exportieren und es dann aus Braze [zu löschen](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint). Die APIs von Braze können verwendet werden, um diese Daten wieder zu importieren, falls der Endnutzer Ihnen später erlaubt, diese speziellen Untergruppen seiner persönlichen Daten zu verarbeiten. Darüber hinaus sollten Sie Ihrem Endbenutzer empfehlen, alle Ihre Anwendungen, die das Braze SDK verwenden, zu deinstallieren oder sich abzumelden, damit keine weiteren Daten über die betroffene Person gesammelt werden.

## Das Recht auf Datenübertragbarkeit

Das Recht auf Datenübertragbarkeit ermöglicht es den betroffenen Personen, ihre persönlichen Daten für ihre eigenen Zwecke über verschiedene Dienste hinweg zu erhalten und wiederzuverwenden. Die persönlichen Daten sollten in einem strukturierten, maschinenlesbaren und allgemein gebräuchlichen Format bereitgestellt werden.

### Braze Empfehlung

Ähnlich wie beim Auskunftsrecht können Sie die [REST-API](https://www.braze.com/docs/api/endpoints/export/#user-export) von Braze verwenden, um die persönlichen Daten eines Endbenutzers zu exportieren und sie der betroffenen Person auf deren Anfrage hin zur Verfügung zu stellen.

## Das Recht auf Widerspruch

Einzelpersonen können das Recht haben, Einspruch zu erheben:

- Verarbeitung auf der Grundlage berechtigter Interessen oder der Wahrnehmung einer Aufgabe im öffentlichen Interesse/Ausübung öffentlicher Gewalt (einschließlich Profiling);
- Direktmarketing (einschließlich Profiling); und
- Verarbeitung zu Zwecken der wissenschaftlichen/historischen Forschung und Statistik.

### Braze Empfehlung

Braze bietet die Möglichkeit, ein Benutzerprofil als von SMS, E-Mails oder Push-Benachrichtigungen abgemeldet zu markieren, sowohl über unsere [REST-APIs](https://www.braze.com/docs/api/home/) als auch über die [iOS-](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android-](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) und [Web-SDKs](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Wenn Sie von betroffenen Personen Einwände gegen den Erhalt solcher Nachrichten erhalten, können Sie die APIs von Braze verwenden, um diese Endnutzer abzumelden.

Wenn dies nicht ausreicht, um die Verarbeitung der persönlichen Daten des Endnutzers durch Braze zu verhindern, sollte das Profil des Endnutzers auf die gleiche Weise gelöscht werden, wie unter dem 'Recht auf Löschung' beschrieben.

## Rechte in Bezug auf automatisierte Entscheidungsfindung und Profiling

Einige Datenschutzgesetze verhindern automatisierte Entscheidungsfindung oder Profiling unter bestimmten Umständen, insbesondere bei Entscheidungen, die "eine rechtliche Wirkung oder eine ähnlich erhebliche Auswirkung auf die betroffene Person haben", oder ermöglichen es den betroffenen Personen, sich dagegen zu entscheiden.

### Braze Empfehlung

Braze führt keine automatisierte Profilerstellung oder Entscheidungsfindung durch, die rechtliche oder gleichwertige Auswirkungen auf die betroffenen Personen hat. Wenn Sie der Meinung sind, dass Ihre eigene Nutzung der Braze-Plattform rechtliche oder gleichwertige Auswirkungen hat und Sie einen Widerspruch erhalten haben, können Sie das Benutzerprofil auf die gleiche Weise wie unter dem "Recht auf Löschung" löschen.

## Zielgerichtete Werbung

Nach den Datenschutzgesetzen einiger US-Bundesstaaten können Betroffene der Verwendung ihrer persönlichen Daten für gezielte Werbezwecke widersprechen.

### Braze Empfehlung

Bei der Erstellung von Zielgruppen für die gezielte Werbung für Ihre betroffenen Personen sollten Sie sicherstellen, dass Sie alle betroffenen Personen ausgeschlossen haben, die einer gezielten Werbung widersprochen haben, z. B. kalifornische Verbraucher, die ihr Recht auf "Nicht verkaufen oder weitergeben" gemäß dem CCPA ausgeübt haben.

Weitere Informationen zur Erstellung von Zielgruppen, die mit Plattformen von Drittanbietern synchronisiert werden können, finden Sie unter [Zielgruppensynchronisierung](https://www.braze.com/docs/partners/canvas_steps).

## Das Recht auf Nicht-Diskriminierung 

Betroffene Personen haben das Recht, ihre Datenschutzrechte ohne Diskriminierung auszuüben.

### Braze Empfehlung

Bei der Nutzung der Braze Services müssen die Kunden sicherstellen, dass sie keine betroffenen Personen diskriminieren, die ihre Datenschutzrechte wahrgenommen haben. So empfehlen wir beispielsweise, dass betroffene Personen, die von ihren Rechten auf Privatsphäre Gebrauch gemacht haben, nicht in Zielgruppen segmentiert oder anderweitig in einer Weise angesprochen werden sollten, die sie diskriminieren könnte.