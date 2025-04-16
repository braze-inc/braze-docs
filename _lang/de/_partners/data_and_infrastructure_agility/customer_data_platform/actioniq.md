---
nav_title: ActionIQ
article_title: ActionIQ
description: "Dieser Referenzartikel behandelt die Integration von Braze und ActionIQ.  Diese Integration ermöglicht es Marken, ihre ActionIQ-Daten direkt mit Braze zu synchronisieren und zuzuordnen."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

>  



## Über die Integration

 

- 
- Leiten Sie die von ActionIQ verfolgten Ereignisse in Echtzeit an Braze weiter, um personalisierte und gezielte Kampagnen auszulösen.
- 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| ActionIQ-Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein ActionIQ-Konto. |
| Braze REST API Schlüssel |   <br><br> |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrationen

### Zugehörigkeit zum Publikum

Diese Integration wird verwendet, um die ActionIQ-Zielgruppenmitgliedschaft mit Braze zu synchronisieren, indem benutzerdefinierte Attribute erstellt werden, die angeben, ob ein Braze-Profil zu einem Segment gehört. Jede ActionIQ-Zielgruppe entspricht einem eindeutigen booleschen benutzerdefinierten Attribut.

Die Standardbenennungskonvention für das erstellte benutzerdefinierte Attribut lautet: `AIQ_<Audience ID>_<Split ID>`.


1. 
2. 
3. 
4.  
5. Nachdem das Segment erstellt wurde, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.



#### Anforderungen

  

Richten Sie in ActionIQ eine Braze-Verbindung ein, indem Sie Ihren REST-API-Schlüssel und den REST-Endpunkt von Braze angeben. 

Um mit den Verbrauchern auf der Braze-Plattform übereinzustimmen, müssen die folgenden Identifikatoren in Ihrer Aktivierungseinstellung enthalten sein:
- `braze_id`
- `external_id`

### Events

  

#### Anforderungen

  

Die Ereignisintegration sendet die folgenden Informationen an Braze:
- Event-Name
- Kennung des Verbrauchers (entweder `braze_id` oder `external_id`)
- Zeitstempel
- Ereigniseigenschaften, die durch zusätzliche Attribute in der Exporteinstellung aufgefüllt werden

### Ausgelöste Kampagnen

 

 

#### Anforderungen

 


- Kennung des Verbrauchers (entweder `braze_id` oder `external_id`)
- Kampagnen-ID


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/