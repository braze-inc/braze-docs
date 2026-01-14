---
nav_title: "Arten von Push-Benachrichtigungen"
article_title: Arten von Push-Benachrichtigungen
page_order: 1
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Arten von Push-Benachrichtigungen auf, die Sie mit Braze versenden können."
channel: push

layout: glossary_page
glossary_top_header: "Types of push notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push campaigns, but there are notes in the following descriptions that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: Internet

glossaries:
  - name: "Regulärer Push"
    description: "Die allumfassende Push-Nachricht. Diese erscheinen auf dem Gerät der Nutzerin oder des Nutzers mit einem Benachrichtigungston und einer Nachricht, die in einer Benachrichtigungsleiste oder einem Stack angezeigt wird."
    tags:
      - iOS
      - Android
      - Web
  - name: "Web-Push"
    description: "Diese Push-Nachrichten erscheinen in Web Apps oder Browsern. Sie benötigen immer noch die Erlaubnis, die Kund:in zu erreichen. Beachten Sie, dass Web-Push nicht funktioniert, wenn die:der Nutzer:in einen ausgeblendeten Browser verwendet."
    tags:
      - Web
  - name: "Push-Primer-Kampagnen"
    description: "In-App-Nachrichten Kampagnen, die dazu dienen, explizite Push-Opt-in oder -Opt-out-Signale von Nutzer:innen zu erhalten. Durch den Primer können Sie vermeiden, Push-Benachrichtigungen an Nutzer:innen zu senden, die Push über die Geräteeinstellungen deaktivieren. Für iOS sind Push-Kampagnen relevant, da Push-Benachrichtigungen im Vordergrund (z. B. Benachrichtigungen, die das Gerät aufwecken) erst dann aktiviert werden, wenn ein:e Nutzer:in sich ausdrücklich für die iOS-eigene Push-Abfrage entscheidet."
    tags:
      - iOS
      - Android
      - Web
  - name: "Push-Storys"
    description: "Push Stories sind immersive Nachrichten, die den Benutzer durch eine visuelle Reise in Form eines Karussells führen. Diese sind nur für mobile Geräte verfügbar."
    tags:
      - iOS
      - Android
  - name: "Push mit Aktions-Buttons"
    description: "Aktionsschaltflächen sind Nachrichten, die es Ihnen ermöglichen, Ihren Nutzern Optionen zu bieten und mehrere Aufrufe zum Handeln anzubieten."
    tags:
      - iOS
      - Android
      - Web
  - name: "Reichhaltige Push-Benachrichtigungen"
    description: "Rich Push Notifications sind Benachrichtigungen mit eindrucksvollen Bildern und kreativen Inhalten, die über ein einfaches Symbol und einen Aufruf zum Handeln hinausgehen können."
    tags:
      - iOS
      - Android
  - name: "Vorläufige Push-Benachrichtigungen für iOS"
    description: "Die von Apple in iOS 12 eingeführte provisorische Autorisierung erfolgt automatisch bei der Installation von iOS-Apps und ermöglicht es Marken, stille Benachrichtigungen zu senden, ohne den Nutzern eine Push-Anfrage zu zeigen. Wenn die stille Push-Benachrichtigung gesendet und in der Benachrichtigungsleiste des Geräts angezeigt wird, erhalten die Benutzer die Möglichkeit, Push-Benachrichtigungen zuzulassen oder abzubrechen."
    tags:
      - iOS
  - name: "HTML-Push-Benachrichtigungen"
    description: "HTML-Push-Benachrichtigungen sind Nachrichten, die fest in HTML codiert sind und nicht die von Braze bereitgestellten Push-Templates verwenden. Mit der Möglichkeit, HTML-Push-Benachrichtigungen zu erstellen, hat Ihr Unternehmen volle kreative Freiheit und ein einheitliches Branding, wenn es darum geht, wie diese Push-Nachrichten aussehen sollen."
    tags:
      - Android
  - name: "Benachrichtigungs-IDs &amp; Kanal-IDs"
    description: "Mit Benachrichtigungs-IDs und Kanal-IDs können Sie Push-Benachrichtigungen ersetzen oder aktualisieren, die der Benutzer bereits erhalten, aber noch nicht geöffnet hat."
    tags:
      - iOS
      - Android
  - name: "Push-Benachrichtigungen im Hintergrund oder lautlos"
    description: "Push-Benachrichtigungen, die nicht auf dem Gerät wiedergegeben werden. Wird in der Regel verwendet, um Informationspakete für Hintergrundprozesse und Deinstallationsverfolgung an die App zu senden. Ein Push-Token mit Enablement für den Hintergrund ist erforderlich, damit ein Push im Hintergrund oder im Stillen gesendet werden kann."
    tags:
      - iOS
      - Android
      - Web
  - name: "Wearable Push-Benachrichtigungen"
    description: "Diese Push-Benachrichtigungen ermöglichen es Marken, Nachrichten direkt an tragbare Geräte wie die Apple Watch zu senden."
    tags:
      - iOS

---
