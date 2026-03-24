---
nav_title: "Arten von Push-Benachrichtigungen"
article_title: Arten von Push-Benachrichtigungen
page_order: 1
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Arten von Push-Benachrichtigungen auf, die Sie mit Braze versenden können."
channel: push

layout: glossary_page
glossary_top_header: "Arten von Push-Benachrichtigungen"
glossary_top_text: "Es gibt verschiedene Arten von Push-Benachrichtigungen, die Sie zur Interaktion mit Ihren Kund:innen nutzen können. Diese können nach Kanälen gefiltert und für die Anforderungen vieler verschiedener Nutzer:innen eingesetzt werden. Die meisten dieser Einstellungen können Sie in Ihren Push-Kampagnen konfigurieren. In den folgenden Beschreibungen finden Sie jedoch Hinweise darauf, ob Backend-Konfigurationen erforderlich sind und um welche es sich dabei handeln könnte."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: Internet
  - name: Android
  - name: iOS

glossaries:
  - name: "Regulärer Push"
    description: "Die allumfassende Push-Nachricht. Diese erscheinen auf dem Gerät der Nutzerin oder des Nutzers mit einem Benachrichtigungston und einer Nachricht, die in einer Benachrichtigungsleiste oder einem Stack angezeigt wird."
    tags:
      - Web
      - Android
      - iOS
  - name: "Web-Push"
    description: "Diese Push-Nachrichten erscheinen in Web Apps oder Browsern. Sie benötigen immer noch die Erlaubnis, die Kund:in zu erreichen. Beachten Sie, dass Web-Push nicht funktioniert, wenn die:der Nutzer:in einen ausgeblendeten Browser verwendet."
    tags:
      - Web
  - name: "Push-Primer-Kampagnen"
    description: "In-App-Nachrichten Kampagnen, die dazu dienen, explizite Push-Opt-in oder -Opt-out-Signale von Nutzer:innen zu erhalten. Durch den Primer können Sie vermeiden, Push-Benachrichtigungen an Nutzer:innen zu senden, die Push über die Geräteeinstellungen deaktivieren. Für iOS sind Push-Kampagnen relevant, da Push-Benachrichtigungen im Vordergrund (z. B. Benachrichtigungen, die das Gerät aufwecken) erst dann aktiviert werden, wenn ein:e Nutzer:in sich ausdrücklich für die iOS-eigene Push-Abfrage entscheidet."
    tags:
      - Web
      - Android
      - iOS
  - name: "Push-Storys"
    description: "Push Stories sind immersive Nachrichten, die den Benutzer durch eine visuelle Reise in Form eines Karussells führen. Diese sind nur für mobile Geräte verfügbar."
    tags:
      - iOS
      - Android
  - name: "Push mit Aktions-Buttons"
    description: "Aktionsschaltflächen sind Nachrichten, die es Ihnen ermöglichen, Ihren Nutzern Optionen zu bieten und mehrere Aufrufe zum Handeln anzubieten."
    tags:
      - Web
      - Android
      - iOS
  - name: "Reichhaltige Push-Benachrichtigungen"
    description: "Rich Push Notifications sind Benachrichtigungen mit eindrucksvollen Bildern und kreativen Inhalten, die über ein einfaches Symbol und einen Aufruf zum Handeln hinausgehen können."
    tags:
      - iOS
      - Android
  - name: "Vorläufige Push-Benachrichtigungen für iOS"
    description: "Die von Apple in iOS 12 eingeführte vorläufige Autorisierung erfolgt automatisch bei der Installation von iOS-Apps und macht es Marken möglich, Benachrichtigungen zu versenden, ohne dass den Nutzer:innen eine Push-Aufforderung angezeigt wird. Diese Benachrichtigungen werden unauffällig an das Benachrichtigungscenter zugestellt, wo die Nutzer:innen die Möglichkeit haben, Push-Benachrichtigungen zuzulassen oder zu unterbinden."
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
  - name: "Push-Benachrichtigungen im Hintergrund (stille Push-Benachrichtigungen)"
    description: "Eine Push-Benachrichtigung, die für den Endnutzer:in nicht sichtbar ist und in der Regel intern verwendet wird, um Features wie Uninstall-Tracking, Geofences und die Datensynchronisierung zu verwalten. Hintergrund-Push und stiller Push referenzieren dasselbe Konzept. Ein Push-Token mit Enablement ist erforderlich. Weitere Informationen finden Sie unter <a href=\"/docs/developer_guide/push_notifications/silent\">Stille Push-Benachrichtigungen</a>."
    tags:
      - Web
      - Android
      - iOS
  - name: "Wearable Push-Benachrichtigungen"
    description: "Diese Push-Benachrichtigungen ermöglichen es Marken, Nachrichten direkt an tragbare Geräte wie die Apple Watch zu senden."
    tags:
      - iOS

---
