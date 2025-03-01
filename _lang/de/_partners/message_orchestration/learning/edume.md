---
nav_title: eduMe
article_title: eduMe
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und eduMe, einem mobilen Schulungstool, mit dem Sie Braze Connected Content nutzen können, um Ihren Benutzern in Ihren Braze-Kampagnen Zugriff auf eduMe-Kurse und -Lektionen zu geben."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com) ist ein mobiles Trainingstool, das Ihren Mitarbeitern das Wissen vermittelt, das sie brauchen, um erfolgreich zu sein, wann immer sie es brauchen und wo immer sie sind. 

Die Integration von Braze und eduMe nutzt Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), um Ihren Benutzern den Zugang zu eduMe-Kursen und -Lektionen in Ihren Braze-Kampagnen zu ermöglichen. Die Fortschritte des Einzelnen und der Gruppe können dann über die eduMe-Berichtsfunktion verfolgt werden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| eduMe-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein eduMe-Konto. |
| eduMe API-Schlüssel | Sie müssen einen API-Schlüssel von Ihrem eduMe-Kundenbetreuer anfordern. Dieser Schlüssel wird in Ihrem Aufruf von Braze Connected Content verwendet. |
| eduMe Link Signiergeheimnis | Sie müssen Ihren Ansprechpartner für Kundenerfolg bei eduMe bitten, ein Link-Signaturgeheimnis für Ihre Organisation einzurichten. Dieses Geheimnis wird verwendet, um nahtlose Links in Connected Content zu ermöglichen. Sie müssen nichts mit diesem Geheimnis anfangen. |
| eduMe Gruppen- und Inhalts-IDs | Diese Kennungen werden benötigt, um Ihre Connected Content-Aufrufe einzurichten. Wenden Sie sich an Ihren eduMe-Kundendienst, wenn Sie Hilfe bei der Beschaffung dieser Kennungen benötigen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Erstellen Sie Ihren Aufruf für Connected Content

Um einem Benutzer Zugriff auf einen Kurs, eine Lektion oder eine eNPS-Umfrage zu geben und seinen Fortschritt anhand Ihrer internen Benutzer-ID in eduMe zu verfolgen, folgen Sie dem API-Aufruf in diesem Beispiel:

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
2. Ersetzen Sie `EDUME-CONTENT-LINK-AND-CONTENT-ID` durch den entsprechenden Linkstring zum Inhalt und die Kennung des Moduls, der Lektion oder der Umfrage. Diese Kennungen können Sie in Ihrem eduMe-Konto finden.
  - Kurs: `getCourseLink?moduleId=12087`
  - Lektion: `getLessonLink?lessonId=25805`
  - eNPS-Umfrage: `getSurveyLink?surveyId=654`<br><br>
3. Benutzer, die über diesen Link zu eduMe gelangen, werden einem eduMe-Team oder einer eduMe-Gruppe Ihrer Wahl hinzugefügt. Ersetzen Sie `groupId` durch die entsprechende Team-ID oder eduMe-Gruppen-ID. Normalerweise verwenden Sie die Team-ID, außer bei Kursen, für die eine Einschreibung erforderlich ist. In diesem Fall sollten Sie die Gruppen-ID verwenden.<br><br>
4. Fügen Sie ein entsprechendes Feld ein, dem das Feld `externalUserId` zugeordnet wird. Das Beispiel für den Aufruf von Connected Content verwendet das Feld `driver_id`, obwohl Ihr Feld wahrscheinlich anders aussehen wird. Diese ID wird in eduMe-Berichten verfügbar sein, so dass Sie sie mit Ihren Systemen in Beziehung setzen können.<br><br>
5. Und schließlich können Sie Ihre Nachricht nach Bedarf anpassen und testen. Wir empfehlen Ihnen, mindestens eine Testnachricht zu versenden, auf die eduMe-Inhalte zuzugreifen, die Lektion oder den Kurs abzuschließen und zu überprüfen, ob die eduMe-Analysen aufgezeichnet werden. 
