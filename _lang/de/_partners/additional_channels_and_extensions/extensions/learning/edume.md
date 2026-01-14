---
nav_title: eduMe
article_title: eduMe
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und eduMe, einem mobilfunkbasierten Trainingstool, das es Ihnen erlaubt, Connected-Content von Braze zu nutzen, um Ihren Nutzer:innen in Ihren Kampagnen Zugang zu eduMe-Kursen und -Lektionen zu geben."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com) ist ein mobiles Trainingstool, das Ihren Mitarbeitern das Wissen vermittelt, das sie für den Erfolg benötigen, wann immer sie es brauchen und wo immer sie sind. 

_Diese Integration wird von eduMe verwaltet._

## Über die Integration

Die Integration von Braze und eduMe nutzt den [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) von Braze, um Ihren Nutzer:innen in Ihren Kampagnen Zugang zu eduMe-Kursen und -Lektionen zu geben. Der Fortschritt von Einzelpersonen und Gruppen kann dann über die eduMe-Berichtsfunktionalität getrackt werden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| eduMe-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein eduMe-Konto. |
| eduMe API-Schlüssel | Sie müssen einen API-Schlüssel bei Ihrer eduMe-Kontaktperson für Kundenerfolg anfragen. Dieser Schlüssel wird in Ihrem Braze Connected-Content-Aufruf verwendet. |
| eduMe Link Signiergeheimnis | Sie müssen Ihren Ansprechpartner für Kundenerfolg bei eduMe anfragen, um einen Link einzurichten, mit dem Sie sich für Ihre Organisation anmelden können. Dieses Geheimnis wird verwendet, um nahtlose Links in Connected-Content zu ermöglichen. Sie müssen nichts mit diesem Geheimnis anfangen. |
| eduMe Gruppen- und Inhalts-IDs | Diese Bezeichner werden benötigt, um Ihre Connected-Content-Aufrufe einzurichten. Wenden Sie sich an Ihren eduMe Kunden:in, wenn Sie Hilfe bei der Beschaffung dieser Bezeichner benötigen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Erstellen Sie Ihren Connected-Content-Aufruf

Um einem Nutzer:innen Zugang zu einem Kurs, einer Lektion oder einer eNPS-Umfrage zu geben und seinen Fortschritt anhand Ihrer internen ID in eduMe zu verfolgen, folgen Sie dem API-Aufruf in diesem Beispiel:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Ersetzen Sie `YOUR-EDUME-API-KEY` durch Ihren eduMe API-Schlüssel.<br><br>
2. Ersetzen Sie `EDUME-CONTENT-LINK-AND-CONTENT-ID` durch den entsprechenden String für den Inhaltslink und den Bezeichner für das Modul, die Lektion oder die Umfrage. Diese Bezeichner finden Sie in Ihrem eduMe-Konto.
  - Kurs: `getCourseLink?moduleId=12087`
  - Lektion: `getLessonLink?lessonId=25805`
  - eNPS-Umfrage: `getSurveyLink?surveyId=654`<br><br>
3. Nutzer:innen, die über diesen Link zu eduMe gelangen, werden einem eduMe Team oder einer Gruppe Ihrer Wahl hinzugefügt. Ersetzen Sie `groupId` durch die entsprechende Team ID oder eduMe Gruppen ID. In der Regel werden Sie die Team ID verwenden, außer bei Kursen, die eine Einschreibung erfordern. In diesem Fall sollten Sie die Gruppen ID verwenden.<br><br>
4. Fügen Sie ein geeignetes Feld ein, auf das Sie das Feld `externalUserId` abbilden können. Das Beispiel für den Aufruf von Connected-Content verwendet das Feld `driver_id`, obwohl Ihr Feld wahrscheinlich anders aussehen wird. Diese ID wird in den eduMe-Berichten verfügbar sein, so dass Sie sie mit Ihren Systemen in Verbindung bringen können.<br><br>
5. Schließlich können Sie Ihre Nachrichten nach Bedarf anpassen und testen. Wir empfehlen Ihnen, mindestens eine Testnachricht zu versenden, auf die eduMe-Inhalte zuzugreifen, die Lektion oder den Kurs abzuschließen und zu überprüfen, ob die eduMe Analytics aufgezeichnet werden. 

