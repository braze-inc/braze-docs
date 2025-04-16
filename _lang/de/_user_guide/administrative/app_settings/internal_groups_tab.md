---
nav_title: Interne Gruppen
article_title: Interne Gruppe
page_order: 10
page_type: reference
description: ""

---

# Interne Gruppen

>   

{% alert tip %}

{% endalert %}

## 



## 

 

1. Gehen Sie zu **Einstellungen** > **Interne Gruppen**.
2. 
3. 
4. 

|          | Beschreibung                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
|    | Dient zum Überprüfen von Ereignissen oder Protokollen von Ihrem Testgerät.                                    |
|  | Kann für Push-, E-Mail- und In-App-Nachrichten verwendet werden, um eine gerenderte Kopie der Nachricht zu versenden. |
|          | Sendet beim Senden automatisch eine Kopie der E-Mail an alle Mitglieder der Seed-Gruppe.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Hinzufügen von Testnutzer:innen

 

1. 
2. 

|                   | Beschreibung                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  |                                                                                                                                                            |
|   | Suche nach IP-Adresse. Geben Sie dann für alle Testnutzer:innen einen Namen ein. Dies ist der Name, mit dem alle [Event-Benutzerprotokolle]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) auf der Seite [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) verknüpft werden. |
|       |  Sie können nur Nutzer:innen hinzufügen, die bereits auf dem Dashboard bekannt sind.           |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Inhalt Testgruppen

Ähnlich wie beim Versenden eines Vorschautests einer Nachricht spart Ihnen die Inhaltstestgruppe Zeit und ermöglicht es Ihnen, Tests an eine vordefinierte Liste von Braze-Benutzern gleichzeitig zu senden.  Nur Gruppen, die als Content-Test-Gruppen getaggt sind, sind in der Vorschau einer Nachricht verfügbar.

{% alert note %}
[SMS-Testnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) können nur an gültige Telefonnummern in der Datenbank gesendet werden.
{% endalert %}

 Wenn Ihre Nachricht ein Liquid oder eine andere dynamische Personalisierung enthält, verwendet Braze die für jeden Nutzer:innen verfügbaren Attribute, um den Inhalt der Nachricht zu personalisieren. Für Nutzer:innen, die keine Attribute haben, verwendet Braze den eingestellten Standardwert.

Wenn Sie außerdem eine Vorschau der Nachricht als zufälliger Benutzer, angepasster Nutzer:innen oder bereits vorhandener Nutzer:innen anzeigen, können Sie stattdessen diese Vorschauversion versenden. Wenn Sie das Kontrollkästchen deaktivieren, können Sie den Versand auf der Grundlage der Attribute des jeweiligen Benutzers und nicht auf der Grundlage der Vorschauversion vornehmen.





### Seed-Gruppen

 

  

 

 

- 
-  
- 
- 

{% alert tip %}

{% endalert %}

#### Für Kampagnen



Seed-Gruppen werden für jede E-Mail-Variante einmal versendet und werden zugestellt, wenn Ihr Benutzer diese bestimmte Variante zum ersten Mal erhält. Bei geplanten Nachrichten ist dies in der Regel der erste Zeitpunkt, an dem die Kampagne startet. Bei aktionsbasierten oder API-ausgelösten Kampagnen ist dies der Zeitpunkt, an dem der erste Nutzer eine Nachricht erhält.

 

{% alert note %}

{% endalert %}



#### Für Canvas

Seed-Gruppen in Canvas funktionieren ähnlich wie bei jeder getriggerten Kampagne. Braze erkennt automatisch alle Schritte, die eine E-Mail-Nachricht enthalten, und sendet an diese, wenn Ihr Benutzer zum ersten Mal diesen bestimmten E-Mail-Schritt erreicht.

Wenn ein E-Mail-Schritt aktualisiert wurde, nachdem die Seed-Gruppe gemailt wurde, wird die Option angeboten, nur an aktualisierte Schritte zu senden, an alle Schritte oder die Seeds zu deaktivieren.

