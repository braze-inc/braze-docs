---
nav_title: Attribut-Trigger
article_title: Attribut Auslöser
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Dieser Referenzartikel gibt Ihnen einen Überblick über Attribut-Trigger und wie Sie diese verwenden können, um aktionsbasierte Nachrichten an Nutzer:innen zu senden."
tool:
  - Campaigns

---

# Attribut-Trigger

> Mit Attribut-Triggern können Sie aktionsbasierte Nachrichten senden, wenn sich der Abonnementstatus eines Nutzers oder einer Nutzerin oder angepasste Attributwerte ändern. 

Attributauslöser sind für die folgenden Szenarien verfügbar:

- Aktualisierungen des Abonnementstatus.
- Boolesche, ganzzahlige, String- oder Datumswerte für benutzerdefinierte Attribute ändern sich in einen beliebigen Wert.
- Boolesche, ganzzahlige oder String-Attributwerte ändern sich in einen bestimmten Wert.

Um mit der Verwendung von Attributauslösern zu beginnen, erstellen Sie eine Kampagne oder eine Canvas-Komponente und wählen Sie **Aktionsbasierte Zustellung** als Zustellungsmethode. Wählen Sie dann den Attribut-Trigger aus, den Sie verwenden möchten.

!["Aktionsbasierte Zustellung" mit einer Dropdown-Liste zum Auswählen eines Auslösers.]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Abo-Status aktualisieren

Verwenden Sie den Trigger `Update Subscription Status`, um Nutzer:innen anzusprechen, wenn ihr Abo-Satus aktualisiert wird. 

Sie können beispielsweise Nutzer:innen ansprechen, wenn sich ihr E-Mail- oder Push-Abonnementstatus in „Angemeldet“ ändert, und ihnen für die Anmeldung danken. Sie können auch einen Webhook an Ihre Systeme senden, wenn sich ein:e Nutzer:in von der E-Mail abmeldet, so dass Ihre internen Systeme mit den neuesten Informationen zum Abonnementstatus auf dem Laufenden sind.

{% alert important %}
Dieser Auslöser gilt nicht, wenn ein neuer Benutzer mit dem globalen E-Mail-Standardstatus `subscribed` erstellt wird und anschließend eine Anfrage zur Aktualisierung des Status auf `subscribed` erfolgt, da sich der Abonnementstatus nicht geändert hat.
{% endalert %}

### Status der Abonnementgruppe aktualisieren

Verwenden Sie den Auslöser `Update Subscription Group Status`, um Nutzer:innen anzusprechen, wenn ihr Abonnementgruppenstatus für E-Mail, SMS oder WhatsApp aktualisiert wird. 

So können Sie beispielsweise Nutzer mit einer Willkommens-SMS ansprechen, wenn sie sich für Ihr Programm anmelden. Sie können auch die Quelle der Aktualisierung angeben, um genauer zu steuern, wann eine Nachricht ausgelöst wird. 

Die verfügbaren Aktualisierungsquellen variieren je nach Kanal:
- Canvas-Schritt „Nutzeraktualisierung“
- CSV-Import
- List-Unsubscribe
- Präferenz-Center
- REST API
- SDK
- Shopify (E-Mail, SMS)
- Eingehende Nachricht (SMS)

So können Sie beispielsweise Ihre Begrüßungs-SMS nur senden, wenn die Aktualisierung von der REST-API kommt und nicht von einer eingehenden Nachricht, da Braze bereits automatisch auf bestimmte eingehende SMS reagiert.

### Benutzerdefinierten Attributwert ändern

Bei einem Änderungsattribut wird zuerst der Trigger und dann das Zielgruppenkriterium bewertet. Dies unterscheidet sich von der Standardeinstellung, bei der zuerst die Publikums-Kriterien ausgewertet werden und dann der Auslöser. Um eine Race-Condition zu vermeiden, stellen Sie sicher, dass das Attribut, das als Trigger verwendet wird, nicht dasselbe ist wie das Attribut, das zur Qualifizierung Ihrer Zielgruppe verwendet wird.

#### Jede neue Wertoption

Verwenden Sie den Auslöser `Change Custom Attribute Value` mit der Option `any new value`, um Nutzer:innen anzusprechen, wenn sich ein boolescher, ganzzahliger, String- oder Datumswert in einen beliebigen neuen Wert ändert.

Stellen Sie Nutzer:innen zum Beispiel gezielt zusammen, wenn sich die Anzahl ihrer Rewards-Punkte ändert, um ihnen mitzuteilen, wie viele Punkte sie jetzt haben. In diesem Beispiel nehmen wir an, dass ein Nutzer:innen 85 Rewardspunkte hat und Sie eine Kampagne eingerichtet haben, die triggert, wenn sich das Attribut Rewardspunkte auf einen neuen Wert ändert. Wenn sich der Wert des Attributs Rewardspunkte dieses Nutzers:innen auf einen neuen Wert ändert (z.B. 83, 84, 86, usw.), wird die Kampagne getriggert.

Betrachten Sie den nächsten Anwendungsfall mit einer Benachrichtigung über ein Stufen-Update. Vielleicht möchten Sie Nutzer:innen benachrichtigen, wenn sich ihre Rewards-Stufe ändert. Um diesen Anwendungsfall zu realisieren, richten Sie eine Kampagne ein, die durch `Change Custom Attribute Value` ausgelöst wird, und stellen Sie sie so ein, dass sie ausgelöst wird, wenn sich das angepasste Attribut Rewards Tier auf einen neuen Wert ändert.

{% alert important %}
Attribut-Trigger sind derzeit nicht für Array-Attribute verfügbar.
{% endalert %}

![Ein Trigger "Angepassten Attribut-Wert ändern" für die "AA_current_rewards_tier", die sich auf einen beliebigen Wert ändert.]({% image_buster /assets/img_archive/any_value.png %})

Sie können Liquid auch verwenden, um den Nachrichtentext mit der neuen Rewards-Stufe des Kunden anzupassen und den Kunden mit weiteren Informationen über die Änderung zu versorgen.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

#### Spezifischer Wert

Verwenden Sie den Trigger `Change Custom Attribute Value` mit der Option `specific value`, um Nutzer:innen anzusprechen, wenn sich ein angepasstes boolesches, ganzzahliges oder String-Attribut auf einen bestimmten Wert ändert. 

Stellen Sie Nutzer:innen zum Beispiel gezielt zusammen, wenn ihre Rewards-Stufe in die beste Stufe wechselt. Für dieses Beispiel nehmen wir an, dass die beste Rewards-Stufe Super VIP ist. Sie können eine Kampagne einrichten, die triggert, wenn sich das angepasste Attribut der Rewards-Stufe eines Nutzers:innen in `Super VIP` ändert, so dass Sie dem Nutzer:innen dazu gratulieren können, dass er ein Super-VIP geworden ist.

![Ein "Change Custom Attribute Value"-Trigger für die "AA_current_rewards_tier", der auf den spezifischen Wert "super vip" ändert.]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Attribut-Trigger für bestimmte benutzerdefinierte Attributwerte sind für benutzerdefinierte Array- und Datumsattribute nicht verfügbar.
- Der Trigger für die Änderung von angepassten Attributwerten wird nicht ausgelöst, wenn der Wert des angepassten Attributs auf Null aktualisiert wird.  
- Der Auslöser für die Änderung von benutzerdefinierten Attributwerten wird nur ausgelöst, wenn sich der Wert eines benutzerdefinierten Attributs ändert. Wenn der aktuelle Wert eines angepassten Attributs erneut an Braze gesendet wird (e.g der Wert für das Attribut Lieblingsfarbe ist rot und Sie senden den Wert rot erneut an Braze), wird der Trigger für die Änderung der angepassten Attributwerte nicht ausgelöst.
- Der Auslöser für die Änderung von benutzerdefinierten Attributwerten gilt auch für neu angelegte Benutzer.
{% endalert %}

