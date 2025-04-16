---
nav_title: Facebook
article_title: Canvas Audience Sync mit Facebook
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Audience Sync mit Facebook

> 

 



- 
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut reagieren.
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind.
- 

Mit dieser Funktion können Marken kontrollieren, welche spezifischen Erstanbieterdaten mit Facebook geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung
 
 In der Praxis bedeutet dies, dass Braze versucht, alle 5 Sekunden so viele Benutzer wie möglich zu verarbeiten, bevor es diese Benutzer an Facebook weiterleitet. 

 Wenn ein Braze-Kunde dieses Ratenlimit erreicht, wird Braze the Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

## Voraussetzungen

 

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten und Apps). |
| Facebook Anzeigenkonto | [Facebook][2] | Ein aktives Facebook-Anzeigenkonto, das mit dem Business Manager Ihrer Marke verbunden ist.<br><br> Vergewissern Sie sich außerdem, dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. |
| Facebook Benutzerdefinierte Zielgruppen Bedingungen | [Facebook][3] | Akzeptieren Sie die Facebook-Bedingungen für Custom Audiences für Ihre Facebook-Anzeigenkonten, die Sie mit Braze verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Mit Facebook verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Facebook**. Wählen Sie unter Facebook-Zielgruppen-Export die Option **Facebook verbinden**.



Es erscheint ein Facebook oAuth-Dialogfenster, um Braze zu autorisieren, Custom Audiences in Ihren Facebook-Anzeigenkonten zu erstellen.

![Das erste Facebook-Dialogfeld mit der Aufforderung "Verbinden als X", wobei X Ihr Facebook-Benutzername ist.][6]{: style="max-width:30%;"}  ![Das zweite Dialogfeld von Facebook, in dem Sie um die Erlaubnis gebeten werden, Anzeigen für Ihre Werbekonten zu verwalten.][5]{: style="max-width:40%;"}

Sobald Sie Braze mit Ihrem Facebook-Konto verknüpft haben, können Sie auswählen, welche Anzeigenkonten Sie mit Ihrem Braze-Arbeitsbereich synchronisieren möchten. 

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Facebook verbinden können.][7]{: style="max-width:70%;"}





 Wenn Ihr Facebook-Administrator Sie aus Ihrem Facebook Business Manager oder dem Zugriff auf die verbundenen Facebook-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die Facebook Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann die Benutzer nicht synchronisieren. 

{% alert important %}
Für Kunden, die bereits den Facebook App Review Prozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr System User Token für die Facebook Audience Komponente weiterhin gültig. Sie können das Facebook System User Token nicht über die Facebook Partnerseite bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Facebook-Systembenutzer-Token in Ihrem Braze-Arbeitsbereich zu ersetzen. 

<br><br>
{% endalert %}

### Schritt 2: Akzeptieren Sie die Servicebedingungen für Custom Audiences



- 
- 






### Schritt 3: Hinzufügen einer Facebook Audience-Komponente in Canvas Flow

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Facebook Audience**.

 

### Schritt 4: Sync-Einrichtung

 



Wählen Sie das gewünschte Facebook-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein. 

{% tabs %}
{% tab Ein neues Publikum schaffen %}

1. 
2.  
3. 



 





{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}

 

1. 
2.  
3.  

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
 
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

  

Auf der Registerkarte **Verlauf** der benutzerdefinierten Zielgruppe im Facebook Audience Manager wird die Anzahl der Nutzer angezeigt, die von Braze an die Zielgruppe gesendet wurden. Wenn ein Benutzer den Schritt erneut betritt, wird er erneut zu Facebook weitergeleitet.

![Publikumsdetails und die Registerkarte Verlauf für ein bestimmtes Facebook-Publikum, die eine Publikumsverlaufstabelle mit Spalten für die Aktivität, Aktivitätsdetails, geänderte Elemente sowie das Datum und die Uhrzeit enthält.][9]{: style="max-width:80%;"}

## Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Benutzer, die diese Komponente eingegeben haben, um mit Facebook synchronisiert zu werden. |
| Fortgefahren mit nächstem Schritt | Wie viele Benutzer sind zur nächsten Komponente weitergegangen, falls es eine gibt. Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Benutzer, die erfolgreich mit Facebook synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit Facebook bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Benutzer, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Facebook synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Facebook-Token sein oder wenn die benutzerdefinierte Zielgruppe auf Facebook gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Facebook-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}

{% endalert %}

## Häufig gestellte Fragen

### 

  

### 

Sie können die Verbindung zu Ihrem Facebook-Konto auf der Facebook-Partnerseite einfach trennen und wiederherstellen. 

### 

- Stellen Sie sicher, dass Ihr Systembenutzer-Token authentifiziert ist und Zugriff auf die gewünschten Anzeigenkonten im Facebook Business Manager hat.
- Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue benutzerdefinierte Zielgruppe eingegeben und entsprechende Felder ausgewählt haben.
- Möglicherweise haben Sie das Limit von 500 benutzerdefinierten Zielgruppen auf Facebook erreicht. 

### 

Facebook stellt diese Informationen aus Gründen des Datenschutzes nicht zur Verfügung.

### 

Zurzeit werden wertbasierte benutzerdefinierte Zielgruppen von Braze nicht unterstützt. 

### 



 

- 
- 
- 
- 



### 

Zurzeit werden wertbasierte Lookalike-Zielgruppen von Braze nicht angenommen. Wenn Sie versuchen, mit dieser Zielgruppe zu synchronisieren, kann dies zu Fehlern bei Ihrem Audience Sync-Schritt führen. Führen Sie die folgenden Schritte aus, um dieses Problem zu lösen:

1. Gehen Sie zu Ihrem Facebook Ad Manager Dashboard und wählen Sie **Zielgruppen**.
2. Wählen Sie **Zielgruppe erstellen** > **Benutzerdefinierte Zielgruppe**.
3. Wählen Sie **Kundenliste**.
4. Laden Sie Ihre CSV-Datei oder Liste ohne die Spalte **Wert** hoch. Wählen Sie **Nein, fahren Sie mit einer Kundenliste fort, die keinen Kundenwert enthält**.
5. Beenden Sie die Erstellung Ihrer benutzerdefinierten Zielgruppe.
6. Aktualisieren Sie in Braze den Schritt Facebook Audience Sync mit der von Ihnen erstellten benutzerdefinierten Zielgruppe.

###  

Um Audience Sync to Facebook zu nutzen, müssen Sie diese Nutzungsbedingungen akzeptieren. 

- 
- 

Nachdem Sie die Nutzungsbedingungen für Ihre benutzerdefinierte Facebook-Zielgruppe akzeptiert haben, gehen Sie wie folgt vor:

1. Aktualisieren Sie Ihr Facebook-Zugangstoken mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und wiederherstellen.
2. Aktivieren Sie den Schritt Facebook Audience Sync erneut, indem Sie Ihr Canvas bearbeiten und aktualisieren.



## Fehlersuche

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Fehler</th>
      <th>Beschreibung</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td> </td>
    </tr>
    <tr>
      <td></td>
      <td> </td>
      <td> </td>
    </tr>
    <tr>
      <td></td>
      <td> </td>
      <td> <br><br>  <br><br></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>   </td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>  </td>
      <td>
      </td>
    </tr>
  </tbody>
</table>

### 

 

#### 

1.  
2.  
3. 

#### 

 

1. 
- 
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- 
  - 
  - 





1. 
2. 
3. 



{:start="4"}

4.  



{:start="5"}
5\.   
6\. Aktualisieren Sie Ihr Facebook-Zugangstoken mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und wiederherstellen.
7\. Aktivieren Sie den Schritt Facebook Audience Sync erneut, indem Sie Ihr Canvas bearbeiten und aktualisieren. Braze kann dann Nutzer:innen synchronisieren, sobald sie den Schritt „Facebook-Zielgruppe“ erreichen.
8\. 

####  



1. 
2. 
3.  <br> 
4.  <br> 

{:start="5"}

5.  <br> 

#### 



1. 
2. 

[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}