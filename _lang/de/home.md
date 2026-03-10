---
nav_title: Home
article_title: Was gibt es Neues bei Braze?
description: "Die Braze-Versionshinweise werden monatlich veröffentlicht, damit Sie über wichtige Produktveröffentlichungen, laufende Produktverbesserungen, Braze-Partnerschaften, aktuelle SDK-Änderungen und veraltete Features auf dem Laufenden bleiben können."
page_order: 0
search_rank: 1
page_type: reference

---

# Was gibt es Neues bei Braze?

{% alert tip %}
Für weitere Informationen zu den auf dieser Seite aufgeführten Updates wenden Sie sich bitte an Ihren Account Manager oder [erstellen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Weitere Informationen zu unseren monatlichen SDK-Veröffentlichungen, Verbesserungen und wesentlichen Änderungen finden Sie in unseren [SDK-Changelogs]({{site.baseurl}}/developer_guide/changelogs).
{% endalert %}

{% details March 5, 2026 %}

## Veröffentlichung am 5\. März 2026

### Datenberichterstattung&

#### Neues Rechenzentrum

{% multi_lang_include release_type.md release="General availability" %}

Braze hat ein neues [Rechenzentrum]({{site.baseurl}}/user_guide/data/data_centers/) in Betrieb genommen: JP-01. Sie können sich bei der Einrichtung Ihres Braze-Kontos für regionsspezifische Datenzentren registrieren.

#### Kontextvariablen

{% multi_lang_include release_type.md release="General availability" %}

[Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) sind temporäre Datenelemente, die Sie erstellen und innerhalb der Reise der Nutzer:innen durch ein bestimmtes Canvas verwenden können. Jedes Mal, wenn ein Nutzer:innen den Canvas betritt - auch wenn er ihn schon einmal betreten hat - werden die Kontextvariablen auf der Grundlage der letzten Eingabedaten und der Canvas-Einstellungen neu definiert. Dieser Ansatz macht es jedem Canvas-Eintrag möglich, seinen eigenen unabhängigen Kontext beizubehalten, sodass Nutzer:innen mehrere aktive Zustände innerhalb derselben Journey haben können, während der spezifische Kontext für jeden Zustand erhalten bleibt.

#### Quellen für die Datenaufnahme von Cloud-Daten

{% multi_lang_include release_type.md release="Early access" %}

[Cloud Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) verfügt über eine neue UI, die Quellen von Synchronisierungen trennt, sodass Sie eine einzelne Quelle für beliebig viele Synchronisierungen wiederverwenden können. Dies reduziert doppelte Konfigurationen und vereinfacht die Einrichtung, wenn Sie mehrere Synchronisierungen haben. Bestehende Synchronisierungen werden automatisch und ohne Ausfallzeiten in die neue Quellen- und Synchronisierungsstruktur migriert. Um zu beginnen, navigieren Sie bitte zu **„Cloud-Datenaufnahme** > **Quellen“**, um Quellen anzuzeigen, zu bearbeiten oder zu erstellen. Wählen Sie anschließend beim Erstellen einer Synchronisierung eine Quelle aus der Dropdown-Liste aus.

#### Zusätzliche Felder für Currents- und Data Share-Ereignisse

{% multi_lang_include release_type.md release="General availability" %}

[Currents- und Data Share-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) umfassen nun die folgenden neuen Felder, um die für Analytics und nachgelagerte Systeme verfügbaren Daten zu vertiefen:

- `agentconsole.AgentExecuted`: Hinzugefügt`error`(String) – eine Beschreibung aller aufgetretenen Fehler.
- `agentconsole.ToolInvocation`: Hinzugefügt`request_id`(String) – eine eindeutige ID für die gesamte LLM-Anfrage und die vollständige Ausführung.
- `users.messages.rcs.InboundReceive`: Hinzugefügt`canvas_variation_name`(String) – Der Name der Canvas-Variante, die der Nutzer:in erhalten hat.

#### Kampagnen- und Canvas-Felder für Snowflake Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) umfasst nun zusätzliche Felder, die Informationen zu Kampagnen und Canvas aus 66 bestehenden Tabellen widerspiegeln, darunter:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV-Validierung vor dem Import und Fehlerberichterstattung

{% multi_lang_include release_type.md release="General availability" %}

[CSV-Nutzerimporte]({{site.baseurl}}/user_guide/data/user_data_collection/user_import) unterstützen nun die Validierung vor dem Import und detaillierte Fehlerberichte. Wählen Sie vor dem Importieren auf der Seite **„Nutzerimport“** **die Option „Datei vor dem Importieren validieren“** aus. Braze überprüft Ihre Datei und erstellt einen Bericht, in dem Zeilen aufgeführt werden, die vollständig fehlschlagen (Fehler), sowie Zeilen, die mit einigen übersprungenen Werten erfolgreich sind (Warnungen). Sie können den Bericht herunterladen, Ihre CSV-Datei korrigieren und erneut hochladen oder unverändert fortfahren. Nach Abschluss des Imports steht ein herunterladbarer Bericht über alle fehlgeschlagenen Zeilen zur Verfügung, der die genauen Gründe für jedes Problem enthält.

#### Diagnose-Dashboard für Messaging

{% multi_lang_include release_type.md release="Early access" %}

Das [Dashboard „Messaging Diagnostics“]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard) bietet eine detaillierte Aufschlüsselung der Ergebnisse des Nachrichtenversands, sodass Sie Trends erkennen und potenzielle Probleme in Ihrer Messaging-Konfiguration diagnostizieren können. Dieses Dashboard kann Ihnen dabei helfen, zu verstehen, warum Nachrichten aus Ihren Kampagnen oder Canvases möglicherweise nicht wie erwartet versendet wurden.

### BrazeAI<sup>TM</sup>

#### Braze-Agenten in der Agent-Konsole

{% multi_lang_include release_type.md release="General availability" %}

[Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) sind KI-gestützte Assistenten, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können. Wenn Sie einen Agenten erstellen, definieren Sie dessen Zweck und legen Sie Richtlinien für dessen Verhalten fest. Nach der Live-Schaltung kann der Agent in Braze [eingesetzt]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) werden, um personalisierte Texte zu generieren, Entscheidungen in Realtime zu treffen oder Katalogfelder zu aktualisieren.

### Orchestrierung

#### Detaillierte Berechtigungen für Nutzer:innen

{% multi_lang_include release_type.md release="Early access" %}

Braze führt [detaillierte Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) ein, eine flexiblere Methode zur Verwaltung des Zugriffs der Nutzer:innen. Weitere Informationen zum Migrationsprozess, einschließlich der Abbildung von alten Berechtigungen zu granularen Berechtigungen, finden Sie unter [Migration zu granularen Berechtigungen]({{site.baseurl}}/granular_permissions_migration/).

#### Kanal-basiertes Rate-Limiting

{% multi_lang_include release_type.md release="General availability" %}

Bei der Festlegung eines Rate-Limits für die Zustellung bei einer Multichannel-Kampagne oder Canvas können Sie zwischen einem gemeinsamen Rate-Limit und einem [kanalbasierten Rate-Limit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases) wählen. Wenn eine Multichannel-Kampagne oder Canvas ein kanalbasiertes Rate-Limiting verwendet, gelten die Rate-Limits für jeden der ausgewählten Kanäle. Sie können beispielsweise Ihre Kampagne oder Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die gesamte Kampagne oder Canvas versendet werden.

#### Canvas-Kontext-Schritt

{% multi_lang_include release_type.md release="General availability" %}

[Mit Canvas-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) können Sie eine oder mehrere Variablen für einen Nutzer:in erstellen und aktualisieren, während dieser sich durch ein Canvas bewegt. Wenn Sie zum Beispiel ein Canvas haben, das saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um jedes Mal, wenn ein Nutzer:in das Canvas eintritt, einen anderen Rabattcode zu speichern.

### Kanäle&  Touchpoints

#### Lokalisierungen in Content-Blöcken übersetzen

{% multi_lang_include release_type.md release="Early access" %}

Nachdem Sie Ihrem Workspace Sprachversionen hinzugefügt haben, können Sie innerhalb eines Content-Blocks [Zielgruppen in verschiedenen Sprachen zusammenstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

### Partnerschaften

#### Algolia – Suchempfehlungen

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) ist eine Such- und Entdeckungsplattform, die Entwicklern dabei unterstützt, schnelle, relevante und skalierbare Sucherlebnisse zu erstellen. Mit einem leistungsstarken API-First-Ansatz kombiniert Algolia fortschrittliche Ranking-Algorithmen mit KI-gestützten Insights für eine nahtlose Website-Suche, Navigation und personalisierte Inhaltserkennung.

#### Anthropic – Anbieter von KI-Modellen

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) ist ein Unternehmen, das sich mit KI-Sicherheit und -Forschung befasst und Claude entwickelt, einen KI-Assistenten der nächsten Generation, der für eine Vielzahl von Sprachaufgaben hilfreich, ehrlich und sicher ist.

#### Canva – Personalisierung von Nachrichten – Kreativstudio

[Canva]({{site.baseurl}}/partners/canva) synchronisiert Ihre Bilder in Canva direkt mit der Braze Media-Bibliothek, optimiert Ihren kreativen Workflow und hält Ihre visuellen Assets über alle Ihre Messaging-Kanäle hinweg auf dem neuesten Stand.

#### DOTS.ECO \- Rewards

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) ermöglicht es Ihnen, Nutzer:innen mit nachverfolgbaren digitalen Zertifikaten für ihren Beitrag zum Umweltschutz zu belohnen. Jedes Zertifikat kann Metadaten wie eine gemeinsam nutzbare Zertifikats-URL und eine Bild-URL enthalten, sodass Nutzer:innen ihren Wirkungsnachweis einsehen (und erneut aufrufen) können.

#### Figma – Personalisierung von Nachrichten – Kreativstudio

[Figma]({{site.baseurl}}/partners/figma) ist eine kollaborative Designplattform, die es Ihnen ermöglicht, Produkte zu entwickeln, zu entwerfen und Prototypen zu erstellen. Nutzen Sie diese Integration, um Bilder und visuelle Elemente aus Figma direkt in die Braze-Medienbibliothek zu übertragen.

#### Flybuy – Personalisierung von Nachrichten – Standort

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) von Radius Networks ist die führende Omnichannel-Standortplattform, die KI-gestützte Technologie nutzt, um die Servicegeschwindigkeit bei Abholung, Zustellung, Drive-Thru und Restaurantbesuchen zu optimieren. Durch seine integrierte Marketing Suite ermöglicht Flybuy Marken außerdem, hyper-zielgerichtete, zeitpunktbezogene Nachrichten zu übermitteln, wodurch das Engagement gefördert, der Kaufbetrag erhöht und umfassendere Treueinitiativen unterstützt werden.

#### Google Gemini – Anbieter von KI-Modellen

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) ist eine Reihe von KI-Modellen von Google, die fortschrittliche Schlussfolgerungen aus Texten, Codes und Bildern kombinieren, um Marken dabei zu unterstützen, intelligentere und personalisierte Erlebnisse zu bieten.

#### Limbik – Nachrichtenpersonalisierung – Personalisierungs-Engines

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) ist Ihre KI-Resonanzschicht – sie erstellt Prognosen darüber, wie echte Zielgruppen Nachrichten, Konzepte und KI-Ergebnisse interpretieren und darauf reagieren, bevor diese auf den Markt kommen. Basierend auf kontinuierlicher Primärforschung in über 60 Ländern und mehr als 25 Sprachen liefert Limbik von Menschen validierte synthetische Zielgruppen – digitale Populationen, die die Reaktionen realer Zielgruppen mit maschineller Geschwindigkeit und in Forschungsqualität (95 % Konfidenz, 1,5 % bis 3 % Fehlerquote) simulieren. Mit Limbik können Sie sicherstellen, dass Ihre Nachrichten unmittelbar mit den Überzeugungen und Empfindungen Ihrer Zielgruppen übereinstimmen.

#### Linkrunner – Nachrichten-Orchestrierung – Attribution

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) ist eine mobile Attributions- und Analytics-Plattform, die Ihnen dabei unterstützt, Ihre Nutzerakquisitionskampagnen zu verfolgen und zu analysieren.

#### Mailizio – Nachrichten-Orchestrierung – Templates

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, die es ermöglicht, mithilfe eines intuitiven visuellen Editors auf einfache Weise wiederverwendbare, markengerechte Inhalte zu gestalten. Durch die Integration von Mailizio in Braze können Sie Ihre Content-Blöcke und E-Mail-Templates exportieren und anschließend automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Bereitstellung von Kampagnen ermöglicht.

#### Offene Loyalität – Daten und Analysen – Loyalität

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) ist eine cloudbasierte Plattform für Kundenbindungs-Programme und Rewards-Programme, mit der Sie diese Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten – wie Punktestand, Stufenänderungen und Ablaufwarnungen – in Realtime direkt mit Braze. Auf diese Weise können Sie personalisierte Nachrichten (E-Mail, Push-Benachrichtigung, SMS) versenden, wenn sich der Treuestatus einer Nutzer:in ändert.

#### OpenAI – Anbieter von KI-Modellen

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) entwickelt fortschrittliche KI-Modelle wie GPT, die das Verstehen und Generieren natürlicher Sprache ermöglichen und Marken dabei unterstützen, sinnvolle Kundeninteraktionen aufzubauen und zu skalieren.

#### Shopgate – Kanäle

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) ist eine Mobile-Commerce- und Omnichannel-Plattform, die Händlern dabei unterstützt, Shopping-Apps zu erstellen und die Effizienz von stationären Geschäften durch Fulfillment-Tools und Clienteling zu verbessern. Clienteling bezeichnet einen personalisierten Kundenservice im Geschäft, der auf Kundendaten basiert.

#### Splio – Daten und Analysen – Kohortenimport

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) ist ein Tool zum Aufbau einer Zielgruppe, mit dem Sie die Anzahl Ihrer Kampagnen und Ihren Umsatz steigern können, ohne das Kundenerlebnis zu beeinträchtigen. Es bietet Analytics zur Verfolgung der Performance von CRM-Kampagnen sowohl online als auch offline.

### SDK

#### SDK-Updates, die zu Inkompatibilitäten führen

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Die Android-Bindung wurde von [Braze Android SDK 37.0.0 auf 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Die iOS-Bindung wurde von [Braze SWIFT SDK 13.3.0 auf 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Neue transitive NuGet-Abhängigkeiten hinzugefügt, die vom Braze Android SDK benötigt werden:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib es gab ein Update von 2.0.21.3 auf 2.3.0.1. Wenn Ihr Projekt dieses Paket explizit an eine ältere Version bindet, müssen Sie ein Update durchführen, um Wiederherstellungsfehler zu vermeiden.
    - Das Newsfeed-Feature wurde entfernt.
        - Dieses Feature wurde in Version [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0) aus dem nativen Android SDK entfernt.
        - Dieses Feature wurde in Version [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0) aus dem nativen SWIFT SDK entfernt.
    - DerBRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeDataenum-Fall wurde in BRZInAppMessageDismissalReason.WipeDataumbenannt.
- [Expo-Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Für diese Version ist die Version 19.0.0 des Braze React Native SDK erforderlich.
    - (Android) Ein Speicherleck in der Schicht für die persistente Datenpersistenz wurde behoben.
    - (Android) Unterstützung für Braze.getInitialPushPayload() hinzugefügt, um Deeplinks für Push-Benachrichtigungen zu verarbeiten, wenn die App aus einem beendeten Zustand heraus gestartet wird. Dies behebt ein Problem, bei dem Deeplinks aus Push-Benachrichtigungen unter Android nicht verarbeitet wurden, wenn die App kalt gestartet wurde.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Aktualisiert die nativen SWIFT SDK-Versionsbindungen von Braze SWIFT SDK 13.3.0 auf 14.0.1.
    - Aktualisiert die nativen Android SDK-Versionsbindungen von Braze Android SDK 40.0.2 auf 41.0.0.

{% enddetails %}

{% details February 5, 2026 %}

## Veröffentlichung am 5\. Februar 2026

### BrazeAI<sup>TM</sup>

#### Content Optimizer

{% multi_lang_include release_type.md release="Beta" %}

[Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) ist ein kontinuierlicher Canvas-Schritt zum Testen von Inhalten mit hoher Variabilität, der eine Automatisierung der Optimierung des Engagements ermöglicht. Verwenden Sie eine Drag-and-Drop-Schnittstelle, die dem Nachrichtenschritt ähnelt, um die zu testenden Komponenten zu definieren, Varianten mithilfe von KI zu generieren (oder manuell einzugeben) und diese Komponenten mithilfe von Liquid-Tags Ihrem Nachrichteninhalt zuzuordnen.

Der Content Optimizer basiert auf einem nicht-kontextuellen Multi-Armed-Bandit-Optimierer und sendet eine einzige Nachricht pro Nutzer:in, wobei er anhand von Prognosen bestimmt, welche Kombination von Komponentenvarianten zugestellt werden soll. Da im Laufe der Zeit Daten gesammelt werden, erhalten leistungsstarke Varianten automatisch eine höhere Zuweisung, während Varianten mit schlechter Performance reduziert werden. Der Content Optimizer funktioniert am besten mit wiederholt versendeten Canvases, die ein konsistentes tägliches Aufkommen an Nutzer:innen aufweisen (mindestens einige Tausend Nutzer:innen pro Tag), um eine kontinuierliche Optimierung zu ermöglichen.

### Datenberichterstattung&

#### E-Commerce empfohlene Veranstaltungen

{% multi_lang_include release_type.md release="Early access" %}

Um die empfohlenen E-Commerce-Ereignisse mit dem bestehenden Kauf-Event abzugleichen, haben wir das [Konversions-Event „Bestellung aufgeben”]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report) hinzugefügt, das dem Ereignis „Kauf tätigen” ähnelt.

### Kanäle&  Touchpoints

#### Lokalisierungen in Bannern übersetzen

{% multi_lang_include release_type.md release="Early access" %}

Nachdem Sie Ihrem Workspace Sprachversionen hinzugefügt haben, [können Sie Zielgruppen aus Nutzern:innen in verschiedenen Sprachen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales) mit einem einzigen Banner [ansprechen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales).

#### Breite für Drag-and-Drop-Content-Blöcke konfigurieren

[Passen Sie die Breite Ihres Content-Blocks an,]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) indem Sie den Button im Navigationsmenü auswählen. Die Standardbreite beträgt 100 %, sofern in Ihren globalen Einstellungen für die E-Mail-Stile nichts anderes angegeben ist. Andernfalls werden die globalen Einstellungen übernommen.

![Ein doppelseitiger Pfeil mit einer Option zur Bearbeitung der Breite.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Automatisiertes IP-Warming verwenden

{% multi_lang_include release_type.md release="Early access" %}

Nutzen Sie [automatisiertes IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming), um Ihr tägliches Versandvolumen schrittweise zu erhöhen, damit Posteingänge Ihre Versandmuster kennenlernen und ihnen vertrauen können. Braze sendet Ihre Nachrichten zuerst an Ihre engagiertesten Abonnent:innen, wodurch das tägliche Volumen in einem Tempo wachsen kann, das den bewährten Verfahren entspricht.

### Partnerschaften

#### LinkedIn – Canvas-Zielgruppensynchronisierung

Verwenden Sie [Braze Audience Sync to LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), um Nutzerdaten aus Ihrer Braze-Integration zu LinkedIn-Kundenlisten hinzuzufügen und so Werbung basierend auf Verhaltensauslösern, Segmentierung und mehr zu liefern. Alle Kriterien, die normalerweise zum Auslösen einer Nachricht (wie Push-Benachrichtigung, E-Mail, SMS und Webhook) in einem Braze-Canvas auf Basis von Benutzerdaten verwendet werden, können nun eine Anzeige für diesen Benutzer in Ihren LinkedIn-Kundenlisten auslösen.

#### Oracle Crowdtwist – Analytics für& Daten

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) ist eine führende Cloud-native Lösung zur Kundenbindung, die es Marken ermöglicht, personalisierte Kundenerlebnisse anzubieten. Ihre Lösung umfasst über 100 sofort einsatzbereite Interaktionspfade und ermöglicht Marktern eine schnelle Amortisierung, um ein umfassenderes Bild von der Kund:in zu erhalten.

#### Vollständige Geschichte – Dynamischer Content

Die Verhaltensdatenplattform [von Fullstory]({{site.baseurl}}/partners/fullstory/) unterstützt Technologieführer dabei, fundiertere Entscheidungen zu treffen. Durch das Einspeisen digitaler Verhaltensdaten in ihre Analytics-Struktur erschließt die patentierte Technologie von Fullstory das Potenzial hochwertiger Verhaltensdaten in großem Maßstab und verwandelt jeden digitalen Besuch in umsetzbare Insights. 

#### Offene Loyalität – Analytics&

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) ist eine cloudbasierte Plattform für Kundenbindungs-Programme und Rewards-Programme, mit der Sie diese Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten – wie Punktestand, Stufenänderungen und Ablaufwarnungen – in Realtime direkt mit Braze. Auf diese Weise können Sie personalisierte Nachrichten (E-Mail, Push-Benachrichtigung, SMS) versenden, wenn sich der Treuestatus einer Nutzer:in ändert.

#### DOTS.ECO \- Erweiterungen

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) ermöglicht es Ihnen, Nutzer:innen mit nachverfolgbaren digitalen Zertifikaten für ihren Beitrag zum Umweltschutz zu belohnen. Jedes Zertifikat kann Metadaten wie eine gemeinsam nutzbare Zertifikats-URL und eine Bild-URL enthalten, sodass Nutzer:innen ihren Wirkungsnachweis einsehen (und erneut aufrufen) können.

#### Mailizio – Orchestrierung der Nachrichten

[Mailizio]({{site.baseurl}}/partners/mailizio/) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, die es ermöglicht, mithilfe eines intuitiven visuellen Editors auf einfache Weise wiederverwendbare, markengerechte Inhalte zu gestalten. Durch die Integration von Mailizio in Braze können Sie Ihre Content-Blöcke und E-Mail-Templates exportieren und anschließend automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Kampagnenbereitstellung ermöglicht.

### APIs

#### Medienbibliothek POST-APIs

{% multi_lang_include release_type.md release="General availability" %}

Medienbibliotheksressourcen können nun über die API hinzugefügt werden, wodurch Kund:innen, Partner und Agenturen ihre Workflows zur Erstellung von Nachrichten stärker automatisieren können. Verwenden Sie die [API,]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) um eine Asset-Datei direkt hochzuladen oder eine Datei von einer bestehenden URL zu kopieren. Dieses Feature ermöglicht Integrations- und Automatisierungsfunktionen.

### Currents und Datenaustausch

#### Agentenkonsole-Ereignisse für Speicherziele und Datenspeicher

{% multi_lang_include release_type.md release="General availability" %}

Zwei neue [Ereignisse](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) sind nun für Speicherziele (AWS S3, GCS und Azure Blob Storage) sowie Snowflake Datashare verfügbar:`agentconsole.AgentExecuted`und `agentconsole.ToolInvocation`. Mit diesen Ereignissen können Sie die Nutzung der Agent-Konsole und Details in Ihren nachgelagerten Systemen analysieren, um die Nutzung Ihrer Agenten besser zu verstehen und optimal zu nutzen. Mit Agenten können Sie intelligente Agenten erstellen und einsetzen, die bestimmte Aufgaben in Braze ausführen können, darunter die Generierung von Inhalten in Canvases oder Katalogen und die Weiterleitung von Nutzer:innen auf verschiedene Pfade auf der Grundlage intelligenter Entscheidungen. Weitere Informationen finden Sie im [Currents-Changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Neue „Wiederholungsversuche“ für einzelne Kanäle

{% multi_lang_include release_type.md release="General availability" %}

Neue [Wiederholungsereignisse](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) sind nun für E-Mail, LINE, Push-Benachrichtigungen, SMS, Webhooks und WhatsApp-Kanäle verfügbar. Diese Ereignisse bieten Transparenz darüber, wann das Frequency-Capping dazu führt, dass eine geplante Nachricht verzögert und nicht abgebrochen wird. Wenn eine Nachricht herabgestuft oder in ihrer Häufigkeit begrenzt wird, kann sie nun innerhalb eines konfigurierten Wiederholungsfensters erneut versucht werden, wodurch Sie einen besseren Insight in die Zustellungsmuster von Nachrichten und die Auswirkungen des Frequency-Capping erhalten. Weitere Informationen finden Sie im [Currents-Changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Fügen Sie dem Ereignis „TokenStateChange“ ein neues'time_ms'Feld hinzu.

{% multi_lang_include release_type.md release="General availability" %}

Dem[`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)Ereignis wurde ein neues`time_ms`Feld hinzugefügt, das eine Granularität im Millisekundenbereich für das Tracking von Änderungen des Status des Push-Tokens bietet. Diese verbesserte Präzision unterstützt Sie dabei, den aktuellen Status eines Push-Tokens zu verstehen, wenn innerhalb derselben Sekunde mehrere Änderungen auftreten. Dadurch können Sie sich darauf verlassen, dass Sie in nachgelagerten Systemen den korrekten Status des Abos haben. Weitere Informationen finden Sie im [Currents-Changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Anonyme Nutzer:innen an Tealium-Ziele senden

{% multi_lang_include release_type.md release="General availability" %}

Ereignisse, für die keine externe ID definiert ist, können nun an [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents)-Ziele gestreamt werden. Wenn Sie in Ihrer Currents-Integration das Kontrollkästchen „Ereignisse von anonymen Nutzer:innen einschließen” auswählen, werden Ereignisse ohne externe ID an die Ziele gesendet, anstatt unterdrückt zu werden. Diese Funktion ist für nachgelagerte Analytics und Anwendungsfälle mit nicht identifizierten und anonymen Nutzer:innen von entscheidender Bedeutung.

##### Anonyme Nutzer:innen an CustomHTTP-Ziele senden

{% multi_lang_include release_type.md release="Beta" %}

Ereignisse, für die keine externe ID definiert ist, können nun an CustomHTTP-Ziele gestreamt werden. Wenn Sie in Ihrer Currents-Integration das Kontrollkästchen „Ereignisse von anonymen Nutzer:innen einschließen” auswählen, werden Ereignisse ohne externe ID an die Ziele gesendet, anstatt unterdrückt zu werden. Diese Funktion ist für nachgelagerte Analytics und Anwendungsfälle mit nicht identifizierten und anonymen Nutzer:innen von entscheidender Bedeutung.

#### E-Mail-Öffnung-Ereignis —"machine_open"Feld

Das [Ereignis „E-Mail-Öffnung“]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) generiert nun den"machine_open"Feldwert, um über die Metrik [_„Gerät geöffnet“_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens) zu berichten. 

### SDK

Die folgenden SDK Updates wurden veröffentlicht. Das SWIFT SDK v14.0.1 behebt ein Problem bei der Verarbeitung von Universal Links. Das Android SDK v40.2.0 behebt ein potenzielles Speicherleck und löst ein Problem, bei dem mehrere Sitzungen geöffnet werden, wenn transparente Aktivitäten vorhanden sind. Expo SDK v3.2.0 fügt die`forwardUniversalLinks`Option (Standard: false) hinzu, um die native SWIFT SDK-Verarbeitung von Universal Links zu konfigurieren.

#### SDK-Updates, die zu Inkompatibilitäten führen

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Benennen Sie `BrazeConfig.Builder.setIsLocationCollectionEnabled()` in `setIsAutomaticLocationCollectionEnabled()` um.
    - Benennen Sie `BrazeConfig.isLocationCollectionEnabled` in `isAutomaticLocationCollectionEnabled` um.
    - Benennen Sie `BrazeConfigurationProvider.isLocationCollectionEnabled` in `isAutomaticLocationCollectionEnabled` um.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo-Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## Veröffentlichung am 8\. Januar 2026

### Datenberichterstattung&

#### Updates zu Currents-Veranstaltungen

{% multi_lang_include release_type.md release="General availability" %}

Die folgenden Änderungen wurden in Version 4 an Currents vorgenommen:

* Änderungen am Feld „Veranstaltungstyp`users.behaviors.pushnotification.TokenStateChange`“:
    * Neues`string`Feld `push_token`hinzugefügt: Push-Token der Veranstaltung
* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Bounce`“:
    * Neues`string`Feld `push_token`hinzugefügt: Push-Token der Veranstaltung
* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Send`“:
    * Neues`string`Feld `push_token`hinzugefügt: Push-Token der Veranstaltung
* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.Click`“:
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Das Feld`user_phone_number`ist nun *optional*.
* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.InboundReceive`“:
    * Das Feld`user_id`ist nun *optional*.
* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.Rejection`“:
    * Neues`string`Feld `canvas_step_message_variation_id`hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat

Bitte referenzieren Sie das [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) für die Änderungen der einzelnen Versionen.

#### Synchronisierungsprotokolle aller Zeilen exportieren

{% multi_lang_include release_type.md release="Early access" %}

Wählen Sie im [Dashboard]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs) [„Cloud Datenaufnahme **Sync Log**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs)“ die Option zum Exportieren der Zeilenprotokolle für einen Synchronisierungslauf aus, indem Sie:

* **Zeilen mit Fehlern:** Lädt eine Datei herunter, die ausschließlich die Zeilen mit dem Status **„Fehler“** enthält.
* **Alle Zeilen:** Lädt eine Datei herunter, die alle in diesem Durchlauf verarbeiteten Zeilen enthält.

### Kanäle&  Touchpoints

#### Bringen Sie Ihren eigenen WhatsApp-Konnektor mit (BYO)

Der [Bring Your Own (BYO) WhatsApp-Konnektor]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) ermöglicht eine Partnerschaft zwischen Braze und Infobip, bei der Sie Braze Zugriff auf Ihren Infobip WhatsApp Business Manager (WABA) gewähren. Auf diese Weise können Sie die Kosten für den Versand von Nachrichten direkt über Infobip verwalten und bezahlen, während Sie Braze für die Segmentierung, Personalisierung und Orchestrierung von Kampagnen nutzen. 

#### Banner in Canvas

{% multi_lang_include release_type.md release="Early access" %}

Bitte wählen Sie **Banner** als Messaging-Kanal in einem [Nachrichtenschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) für Canvas aus. Verwenden Sie den Drag-and-Drop-Editor, um personalisierte Inline-Nachrichten zu erstellen, die unaufdringliche, kontextuelle Erlebnisse bieten und zu Beginn jeder Benutzersitzung automatisch aktualisiert werden. 

#### Dynamische BCC

{% multi_lang_include release_type.md release="General availability" %}

Bei [dynamischer BCC]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc) verwenden Sie bitte Liquid in Ihrer BCC-Adresse. Bitte beachten Sie, dass dieses Feature nur in **den E-Mail-Einstellungen** verfügbar ist und nicht in der Kampagne selbst festgelegt werden kann. Pro E-Mail-Empfänger:in ist nur eine BCC-Adresse zulässig.

#### Kanal-basierte Rate-Limits

Als Alternative zu Rate-Limits, die für eine gesamte Multichannel-Kampagne oder Canvas gelten, können Sie ein spezifisches Rate-Limit pro Kanal auswählen. In diesem Fall gelten die Rate-Limits für jeden der von Ihnen ausgewählten Kanäle. Bitte stellen Sie Ihre Kampagne oder Canvas so ein, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die gesamte Kampagne oder Canvas versendet werden. Weitere Informationen finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Partnerschaften

#### LILT – Lokalisierung

[LILT]({{site.baseurl}}/partners/lilt/) ist die umfassende KI-Lösung für Unternehmensübersetzungen und die Erstellung von Inhalten. LILT ermöglicht es globalen Unternehmen, ihre Inhalte, Produkte, Kommunikation und Support-Abläufe mit KI-Agenten und vollständig automatisierten Workflows zu skalieren und zu optimieren.

### SDK-Updates, die zu Inkompatibilitäten führen

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Entfernt den Newsfeed.
        - Dadurch werden alle UI-Elemente, Datenmodelle und Aktionen, die mit dem Newsfeed in Verbindung stehen, vollständig entfernt.
- [Web-SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9\. Dezember 2025

### Datenberichterstattung&

#### Hinzufügen von Google Tag Manager zu einer Landing Page

Um Google Tag Manager zu Ihren Landing Pages hinzuzufügen, fügen Sie im Drag-and-Drop-Editor einen angepassten Code-Block zu Ihrer Landing Page hinzu und [fügen Sie]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) anschließend [den Tag Manager-Code]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) in den Block [ein]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page).

### Orchestrierung

#### Anwendungsfall für SMS Liquid

Der Anwendungsfall [„Mit unterschiedlichen Nachrichten auf eingehende SMS-Schlüsselwörter reagieren“]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) umfasst die dynamische SMS-Schlüsselwortverarbeitung, um auf bestimmte eingehende Nachrichten mit unterschiedlichen Nachrichtentexten zu reagieren. Beispielsweise können Sie unterschiedliche Antworten senden, wenn jemand „START“ oder „JOIN“ schreibt.

#### Zulassungsliste für Connected-Content

Sie können bestimmte URLs für [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) auf die Whitelist setzen. Um auf dieses Feature zugreifen zu können, wenden Sie sich bitte an Ihren Customer-Success-Manager.

### Kanäle&  Touchpoints

#### SMS-Zeichenkodierung

Unser [SMS-Segmentrechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) verfügt nun über Zeichenkodierung. Wählen Sie **„Zeichenkodierung anzeigen“,** um den Bezeichner zu wählen, der angibt, welche Zeichen als GSM-7 oder UCS-2 kodiert sind. 

![SMS-Segmentrechner mit einer Beispiel-SMS-Nachricht im Textfeld und aktivierter Zeichenkodierung.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### WhatsApp-Nachrichten mit Optimierung

Da die MM-API für WhatsApp keine 100-prozentige Zustellbarkeit garantiert, ist es wichtig zu verstehen, wie Sie Nutzer:innen, die Ihre Nachricht möglicherweise nicht erhalten haben, über andere Kanäle erneut ansprechen können. 

Um Nutzer:innen erneut anzusprechen, empfehlen wir, ein Segment von Nutzer:innen zu erstellen, die eine bestimmte Nachricht nicht erhalten haben. Führen Sie dazu eine Filterung nach dem Fehlercode durch, der darauf hinweist, dass eine Marketing-Template-Nachricht aufgrund der von WhatsApp`131049` festgelegten Beschränkung der Marketing-Templates pro Nutzer:in nicht gesendet wurde. Dies kann mithilfe [von Braze-Currents oder SQL-Segment-Erweiterungen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels) durchgeführt werden.

### Partnerschaften

#### OtherLevels – Dynamischer Content

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) ist eine Erlebnisplattform, die generative KI einsetzt, um die Art und Weise zu verändern, wie Sportmarken, Verlage und Betreiber mit ihren Kunden in Kontakt treten. Dies geschieht durch die Transformation traditioneller Inhalte in markengerechte, personalisierte Video- und Rich-Media-Erlebnisse in großem Maßstab.

### SDK

#### SDK-Updates, die zu Inkompatibilitäten führen

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Internet SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 11\. November 2025

### Flexibilität der Daten

#### `Live Activities Push to Start Registered for App` Segmentierungsfilter

Der`Live Activities Push to Start Registered for App`Filter segmentiert Ihre Nutzer:innen danach, ob sie registriert sind, um eine Live-Aktivität über iOS-Push-Benachrichtigungen für eine bestimmte App zu starten.

#### RFM SQL-Segment-Erweiterung

Sie können eine [RFM-Segment-Erweiterung (Recency, Frequency, Monetary)]({{site.baseurl}}/rfm_segments/) erstellen, um Ihre besten Nutzer:innen anzusprechen, indem Sie deren Kaufgewohnheiten messen.

Die RFM-Analyse ist eine Marketingtechnik, die Ihre besten Nutzer:innen identifiziert, indem sie diese auf einer Skala von 0 bis 3 für jede Kategorie (Aktualität, Häufigkeit, Geldwert) bewertet, wobei 3 die beste und 0 die schlechteste Bewertung darstellt. Aktualität, Häufigkeit und Geldwerte basieren alle auf Daten aus einem bestimmten, von Ihnen gewählten Zeitraum.

#### Angepasste Attribute – Werte 

Wenn Sie einen Nutzungsbericht anzeigen, wählen Sie die [Registerkarte **„Werte“,**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) um die höchsten Werte der ausgewählten angepassten Attribute basierend auf einer Stichprobe von etwa 250.000 Nutzern anzuzeigen.

#### Synchronisierung von Protokollen und Beobachtbarkeit für die Datenaufnahme in der Cloud

{% multi_lang_include release_type.md release="General availability" %}

Über[ das Dashboard]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) „Cloud Data Ingestion (CDI) [Sync Log“]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) können Sie alle von CDI verarbeiteten Daten überwachen, überprüfen, ob die Daten erfolgreich synchronisiert wurden, und Probleme mit „falschen“ oder fehlenden Daten diagnostizieren.

#### Einführung von Feature-Flag-Regeln mit mehreren Regeln

Nutzen Sie [die Einführung von Feature-Flag-Rollouts mit mehreren Regeln]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts), um eine Abfolge von Regeln für die Bewertung von Nutzern zu definieren, die eine präzise Segmentierung und kontrollierte Feature-Veröffentlichungen ermöglicht. Diese Methode eignet sich hervorragend, um das gleiche Feature für unterschiedliche Zielgruppen bereitzustellen.

#### Abbildung der Katalogfelder für Produkte per Drag-and-Drop

In Ihren Katalogeinstellungen können Sie die **Produktblöcke** auswählen, die [auf bestimmte Felder]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) und Informationen in Ihrem Katalog [abgebildet]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) werden sollen. Auf diese Weise können Sie auswählen, welche Felder als Produkttitel, Produkt-URL und Bild-URL verwendet werden sollen.

#### Frequency-Capping für Abbruchereignisse in Currents

Bei der Verwendung von Currents können Sie nun in den `abort_type`Kanalabbruchereignissen referenzieren. Dies ist ein Bezeichner dafür, dass eine Nachricht aufgrund von Frequency-Capping abgebrochen wurde, und gibt an, welche Frequency-Capping-Regel den Abbruch verursacht hat. Dies hilft Ihnen bei der Festlegung Ihrer Regeln für das Frequency-Capping. Weitere Informationen zu bestimmten Currents-Ereignissen finden Sie im Abschnitt[ Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

### Robuste Kanäle

#### Hintergrundbilder 

{% multi_lang_include release_type.md release="General availability" %}

Sie können im Panel **„Zeigeneigenschaften“** [ein Hintergrundbild]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) für eine In-App-Nachricht oder eine Landing Page [hinzufügen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image). Schalten Sie auf **„Hintergrundbild“** um und geben Sie anschließend eine Bild-URL ein oder wählen Sie ein Bild aus der [Bibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) aus. Konfigurieren Sie abschließend den Alternativtext, die Größe, die Position und ob das Bild wiederholt werden soll, um Muster über die gesamte Zeile zu erstellen.

![Ein Hintergrundbild einer Pizza, das sich horizontal wiederholt.]({% image_buster /assets/img_archive/background_row.png %})

#### Vorschau-Link kopieren

Verwenden Sie **den Link „Vorschau kopieren“** in Ihren [Bannern]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [angepassten E-Mail-Fußzeilen]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) sowie [auf den Seiten zum Opt-in und Abmelden von E-Mails]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers), um einen teilbaren Link zu generieren, der anzeigt, wie Ihre Inhalte für einen beliebigen Nutzer:in aussehen werden.

#### WhatsApp-Nachrichten mit optimierter Zustellung

Nutzen Sie die fortschrittlichen KI-Systeme von Meta, um Ihre Marketing-Nachrichten an mehr Nutzer:innen zu übermitteln, die am ehesten darauf reagieren, und so die Zustellbarkeit und das Engagement für Ihre Nachrichten erheblich zu steigern.

[WhatsApp-Nachrichten mit optimierter Zustellung]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) werden über [die](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) neue [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) von Meta versendet, die im Vergleich zur herkömmlichen Cloud API eine überlegene Performance bietet. Diese neue Versandpipeline unterstützt Sie dabei, Nutzer:innen besser zu erreichen, die Ihre Nachrichten schätzen und erhalten möchten.

#### WhatsApp-Flows

Wenn Sie eine WhatsApp Flow-Nachricht in ein Braze-Canvas oder eine Kampagne integrieren, möchten Sie möglicherweise bestimmte Informationen erfassen und nutzen, die Nutzer:innen über den Flow übermitteln. Braze benötigt zusätzliche Informationen zur Struktur der Benutzerantwort, insbesondere zur erwarteten Form der JSON-Antwort, um das erforderliche Schema für verschachtelte angepasste Attribute (NCA) zu generieren.

Sie können Braze nun die Informationen zur Antwortstruktur bereitstellen, indem [Sie die Flow-Antwort als benutzerdefiniertes Attribut speichern]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) und einen Testversand durchführen.

#### Bearbeitbare Vorschau für Nutzer:innen

Sie können [einzelne Felder eines zufälligen oder bestehenden Nutzers bearbeiten,]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) um dynamischen Content in Ihrer Nachricht zu testen. Wählen Sie **„Bearbeiten“,** um den ausgewählten Nutzer:in in einen benutzerdefinierten Nutzer:in umzuwandeln, den Sie anpassen können.

![Das Tab „Vorschau als Nutzer:in“ mit dem Button „Bearbeiten“.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### KI und ML Automatisierung

#### BrazeAI Decisioning Studio

Sie können nun Ihre Integration mit [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) einrichten, indem Sie diese Konfigurationsartikel zu folgenden Themen zu Rate ziehen:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Neue Features für Braze-Agenten

{% multi_lang_include release_type.md release="Beta" %}

Sie können Ihren [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) nun wie folgt anpassen:

- Anwendung [der Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines), die Ihr Mitarbeiter bei seiner Antwort einhalten soll. 
- Bitte beziehen Sie sich auf einen Katalog, um Ihre Nachricht weiter zu personalisieren.
- Strukturierung der Ausgabe eines Agenten durch Angabe des [Ausgabeformats]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Adjusting the [temperature]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) for the level of deviation for your agent's performance.

### ChatGPT-Modelle mit BrazeAI Operator<sup>TM</sup>

{% multi_lang_include release_type.md release="Beta" %}

Sie können aus diesen GPT-Modellen auswählen, die Sie für verschiedene Arten von Anfragen mit [Operator]({{site.baseurl}}/user_guide/brazeai/operator) verwenden möchten:

- GPT-5 Nano
- GPT-5 mini (Standard)
- GPT-5

### Neue Braze Partnerschaften

#### StackAdapt – Werbung

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) ist eine KI-gestützte Marketingplattform, die zielgerichtete, leistungsorientierte Werbung bereitstellt. Es ermöglicht Ihnen, Daten zum Nutzerprofil aus Braze mit dem StackAdapt Data Hub zu synchronisieren. Durch die Verbindung der beiden Plattformen können Sie eine einheitliche Ansicht Ihrer Kunden erstellen und First-Party-Daten aktivieren, um die Anzeigenperformance zu verbessern.

#### Cloudinary – Dynamischer Content

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) ist eine Bild- und Videoplattform, die es Ihnen ermöglicht, Bilder und Videos in großem Umfang zu verwalten, zu bearbeiten, zu optimieren und für jede Kampagne über alle Kanäle und Customer Journeys hinweg zuzugestellt zu bekommen. Nach der Integration und Enablement ermöglicht die Medienverwaltung von Cloudinary eine dynamische, kontextuelle und personalisierte Zustellung von Assets für Ihre Braze-Kampagnen und Canvases.

#### Kameleoon – A/B-Tests

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) ist eine Optimierungslösung mit Experimentier-, KI-gestützten Funktionen für Personalisierung und Feature-Management in einer einzigen einheitlichen Plattform.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Korrigiert den Typescript-Typ für den Callback von`subscribeToInAppMessage`  und`addListener`  für `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Diese Listener geben nun ordnungsgemäß einen Callback mit dem neuen`InAppMessageEvent`Typ zurück. Zuvor waren die Methoden so kommentiert, dass sie einen`BrazeInAppMessage`Typ zurückgaben, tatsächlich wurde jedoch ein zurückgegeben`String`.
         - Falls Sie eine der beiden Abonnement-APIs verwenden, stellen Sie bitte sicher, dass das Verhalten Ihrer In-App-Nachrichten nach dem Update auf diese Version unverändert bleibt. Bitte beachten Sie unseren Beispiel-Code in `BrazeProject.tsx`.
    - Die APIs `logInAppMessageClicked`,  `logInAppMessageImpression`und  `logInAppMessageButtonClicked`akzeptieren nun ausschließlich ein`BrazeInAppMessage`  Objekt, um mit ihrer bestehenden öffentlichen Schnittstelle übereinzustimmen.
        - Zuvor akzeptierte es sowohl ein`BrazeInAppMessage`Objekt als auch ein `String`.
    - `BrazeInAppMessage.toString()` gibt nun einen für Menschen lesbaren String anstelle der JSON-Zeichenfolgenrepräsentation zurück.
        - Um die JSON-String-Repräsentation einer In-App-Nachricht zu erhalten, verwenden Sie bitte`BrazeInAppMessage.inAppMessageJsonString` .
    - Unter iOS wurde die Funktion `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]`nach verlegt`[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Diese neue Methode ist nun eine Klassenmethode anstelle einer Instanzmethode.
    - Fügt Methoden `BrazeReactUtils`Nullbarkeitsanmerkungen hinzu.
    - Die folgenden veralteten Methoden und Eigenschaften werden aus der API entfernt:
        - `getInstallTrackingId(callback:)` zugunsten von `getDeviceId`.
        - `registerAndroidPushToken(token:)` zugunsten von `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` zugunsten von `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` zugunsten von `payload_type`.
        - `PushNotificationEvent.deeplink` zugunsten von `url`.
        - `PushNotificationEvent.content_text` zugunsten von `body`.
        - `PushNotificationEvent.raw_android_push_data` zugunsten von `android`.
        - `PushNotificationEvent.kvp_data` zugunsten von `braze_properties`.
    - Aktualisiert die nativen Android SDK-Versionsbindungen [von Braze Android SDK 39.0.0 auf 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Die iOS-Bindung wurde [von Braze SWIFT SDK 12.1.0 auf 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert. Dies umfasst die Unterstützung für Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Aktualisiert die native Android-Brücke [von Braze Android SDK 39.0.0 auf 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web-SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0–40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Veröffentlichung am 14\. Oktober 2025

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) ersetzt A/B-Tests durch KI-Entscheidungsfindung, die alles personalisiert und alle Metriken maximiert: Steigern Sie den Umsatz, nicht die Klicks. Mit BrazeAI Decisioning Studio™ können Sie alle geschäftlichen KPIs optimieren. Beispiele für Anwendungsfälle und wichtige Features finden Sie in unserem speziellen Abschnitt [BrazeAI Decisioning Studio™.]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)

### Flexibilität der Daten

#### Neue Currents Veranstaltungen

Diese neuen Ereignisse wurden dem [Currents-Glossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) hinzugefügt:

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Diese neuen Felder wurden zu den folgenden Currents-Ereignissen hinzugefügt:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Unterdrückungslisten

{% multi_lang_include release_type.md release="General availability" %}

[Unterdrückungslisten]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) sind Gruppen von Nutzern:innen, die automatisch keine Kampagnen oder Canvases erhalten. Unterdrückungslisten werden durch Filter definiert, und Nutzer:innen werden in Unterdrückungslisten aufgenommen oder aus diesen entfernt, wenn sie die Filterkriterien erfüllen.

#### Zero-Copy-Personalisierung

{% multi_lang_include release_type.md release="Early access" %}

Synchronisieren Sie Canvas-Trigger mithilfe von Cloud Datenaufnahme für [eine kopierfreie Personalisierung]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Dieses Feature greift auf benutzerspezifische Informationen aus Ihrer Datenspeicher-Lösung zu und überträgt diese an einen Ziel-Canvas. Canvas-Schritte können optional Felder der Personalisierung enthalten, die nicht in den Braze-Nutzerprofilen persistent gespeichert werden.

#### Canvas-Kontextvariablen für Zielgruppen-Pfade und Decision-Split-Schritte

{% multi_lang_include release_type.md release="Early access" %}

Sie können [Kontextvariablen-Filter erstellen,]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) die zuvor in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)-Schritten deklarierte Kontextvariablen verwenden.

### Kreativität entfesseln

#### Deal-Karten für E-Mails

Verwenden Sie [Deal-Karten,]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) um wichtige Deal-Informationen direkt am Anfang des E-Mail-Textes anzugeben. Dadurch sind für die Empfänger:innen die Angebotsdetails schnell zu erfassen und entsprechende Maßnahmen zu ergreifen zulässig.

#### Templates für Banner

Wenn Sie [Ihr Banner erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), können Sie nun mit einem leeren Template beginnen, eine Braze-Vorlage verwenden oder ein gespeichertes Banner-Template auswählen.

### Robuste Kanäle

#### Unterdrückungslisten

{% multi_lang_include release_type.md release="General availability" %}
 
[Unterdrückungslisten]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/) geben Gruppen von Nutzer:innen an, die niemals Nachrichten erhalten werden. Administratoren können Unterdrückungslisten mit Segmentfiltern erstellen, um eine Nutzer:innen-Gruppe auf die gleiche Weise einzugrenzen, wie Sie es bei der Segmentierung tun würden.

#### LINE-Klick-Tracking

{% multi_lang_include release_type.md release="General availability" %}

Wenn [die LINE-Klickverfolgung]({{site.baseurl}}/line/click_tracking/) aktiviert ist, verkürzt Braze automatisch Ihre URLs, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Realtime auf. Während LINE aggregierte Klickdaten bereitstellt, bietet Braze detaillierte Nutzerinformationen, die aktuell und umsetzbar sind. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu entwickeln, beispielsweise die Segmentierung von Nutzern anhand ihres Klickverhaltens und das Triggern von Nachrichten als Reaktion auf bestimmte Klicks.

#### Klickfilterung für SMS- und RCS-Bots

{% multi_lang_include release_type.md release="General availability" %}

[Die Filterung von SMS- und RCS-Bot-Klicks]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) verbessert die Analytics für Kampagnen und die Arbeitsabläufe, indem verdächtige Bot-Klicks ausgeschlossen werden. Ein „Bot-Klick“ bezeichnet automatisierte Klicks auf verkürzte Links in SMS- und RCS-Nachrichten, beispielsweise von Webcrawlern, Android- und iOS-Link-Vorschauen oder CPaaS-Sicherheitssoftware. Dieses Feature ermöglicht eine genaue Berichterstattung, Segmentierung und Orchestrierung, um echte Nutzer:innen anzusprechen und ihr Engagement zu fördern.

#### WhatsApp-Telefonnummern übertragen

Bitte übertragen Sie eine WhatsApp Business Account (WABA)-Telefonnummer und die zugehörige Abo-Gruppe [von einem Workspace in einen anderen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) innerhalb von Braze.

#### WhatsApp Flows Antwortnachrichten und Vorschau

In einem Canvas können Sie einen WhatsApp-Nachrichtenschritt erstellen, der eine [Antwortnachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) und eine Flow-Nachricht verwendet. Sie können auch **„Vorschau des Ablaufs“** auswählen, um den Ablauf direkt in Braze in der Vorschau anzuzeigen und zu überprüfen, ob er wie erwartet funktioniert.

#### WhatsApp-Produktnachrichten

[Mit Produktnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) können Sie interaktive WhatsApp-Nachrichten versenden, die Produkte direkt aus Ihrem Meta-Katalog präsentieren.

#### Integration von Braze und WhatsApp in ein externes System

[Nutzen Sie die Leistungsfähigkeit von KI-Chatbots und Live-Agent-Übergaben]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) auf dem WhatsApp-Kanal, um Ihre Kundensupport-Abläufe zu optimieren. Durch die Automatisierung von Routineanfragen und den nahtlosen Übergang zu menschlichen Agenten bei Bedarf können Sie die Reaktionszeiten erheblich verbessern und das Kundenerlebnis insgesamt optimieren.

### KI und ML Automatisierung

#### Braze-Agenten

{% multi_lang_include release_type.md release="Beta" %}

[Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) sind KI-gestützte Assistenten, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können.

### Neue Braze Partnerschaften

#### Jasper – Templates

Die Integration [von]({{site.baseurl}}/partners/jasper/) [Jasper]({{site.baseurl}}/partners/jasper/) mit Braze ermöglicht es Ihnen, die Erstellung von Inhalten und die Durchführung von Kampagnen zu optimieren. Mit Jasper können Ihre Marketing-Teams innerhalb weniger Minuten hochwertige, markengerechte Texte erstellen. Braze unterstützt dann die Zustellung dieser Nachrichten an die richtige Zielgruppe zum optimalen Zeitpunkt. Diese Integration fördert nahtlose Arbeitsabläufe, reduziert den manuellen Aufwand und führt zu stärkeren Ergebnissen im Bereich des Engagements.

#### Swym – Kundenbindung und Retargeting

[Swym]({{site.baseurl}}/partners/swym/) unterstützt E-Commerce-Marken dabei, Kaufabsichten zu erfassen, indem es Funktionen wie Wunschlisten, „Für später speichern“, Geschenkelisten und Benachrichtigungen bei Wiederverfügbarkeit bereitstellt. Mithilfe umfangreicher, genehmigungsbasierter Daten können Sie zielgerichtete Kampagnen erstellen und personalisierte Einkaufserlebnisse bieten, die das Engagement fördern, die Konversionsrate steigern und die Kundenbindung erhöhen.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle weiteren Updates finden Sie in den entsprechenden SDK-Changelogs.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Die native Android-Brücke wurde [von Braze Android SDK 37.0.0 auf 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
        - Die erforderliche Mindestversion von GradlePluginKotlinVersion ist nun 2.1.0.
    - Die native iOS-Brücke wurde [von Braze SWIFT SDK 12.0.0 auf 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert. Dies umfasst die Unterstützung für Xcode 26.
    - Die Unterstützung für den Newsfeed wird eingestellt. Die folgenden APIs wurden entfernt:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0–17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Aktualisiert die nativen Android SDK-Versionsbindungen [von Braze Android SDK 37.0.0 auf 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Die Unterstützung für den Newsfeed wird eingestellt. Die folgenden APIs wurden entfernt:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web-SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Die native iOS-Brücke wurde [von Braze SWIFT SDK 12.0.0 auf 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert. Dies umfasst die Unterstützung für Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Veröffentlichung am 16\. September 2025

### Flexibilität der Daten

#### Braze-Datenplattform

Die Braze Data Platform ist eine umfassende, kombinierbare Sammlung von Datenfunktionen und Partnerintegrationen, die es Ihnen ermöglicht, personalisierte, wirkungsvolle Erlebnisse über den gesamten Kundenlebenszyklus hinweg zu schaffen. Erfahren Sie mehr über die drei Aufgaben im Zusammenhang mit Daten, die zu erledigen sind: 

- [Datenvereinheitlichung]({{site.baseurl}}/user_guide/data/unification)
- [Datenaktivierung]({{site.baseurl}}/user_guide/data/activation)
- [Datenverteilung]({{site.baseurl}}/user_guide/data/distribution)

#### Angepasste Bannereigenschaften

{% multi_lang_include release_type.md release="Early access" %}

Sie können benutzerdefinierte Eigenschaften aus Ihrer Banner-Kampagne verwenden, um Schlüsselwertdaten über das SDK abzurufen und das Verhalten oder das Erscheinungsbild Ihrer App anzupassen. Weitere Informationen finden Sie unter [Eigenschaften benutzerdefinierter Banner]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Token-Authentifizierung

{% multi_lang_include release_type.md release="General availability" %}

Bei der Verwendung von Braze Connected Content kann es vorkommen, dass Sie für bestimmte APIs ein Token anstelle eines Benutzernamens und eines Passworts benötigen. Braze kann Zugangsdaten speichern, die [Werte für die Token-Authentifizierungs-Header]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication) enthalten.

#### Aktionscodes

Sie können Aktionscodes über einen Schritt zum Update des Nutzerprofils speichern. Weitere Informationen finden Sie unter [Speichern von Aktionscodes in Nutzerprofilen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Kreativität entfesseln

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) ist eine öffentlich verfügbare App für Android und iOS, mit der Sie Nachrichten von Ihrem Braze-Dashboard auf Ihr Smartphone senden können. Bitte lesen Sie die Anleitung[ „Erste Schritte mit Braze Pilot“]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started), um eine Schritt-für-Schritt-Anleitung zum Herunterladen der App, zum Initialisieren der Verbindung zu Ihrem Braze-Dashboard und zum Abschließen der Einrichtung zu erhalten.

### Neue Braze Partnerschaften

#### Blings – Visuelle und interaktive Inhalte

[Blings]({{site.baseurl}}/partners/blings/) ist eine personalisierte Videoplattform der nächsten Generation, die es Ihnen ermöglicht, in Realtime interaktive und datengestützte Videoerlebnisse über verschiedene Kanäle hinweg in großem Umfang zuzugestellt.

#### Standard-Integration von Shopify mit Drittanbieter-Tools

Für Shopify-Onlineshops empfehlen wir die Verwendung der Standard-Integrationsmethode von Braze, um die Braze-SDKs auf Ihrer Website zu unterstützen.

Wir sind uns jedoch bewusst, dass Sie möglicherweise ein Tool eines Drittanbieters wie Google Tag Manager bevorzugen. Daher haben wir eine Anleitung zusammengestellt, die Ihnen die Verwendung dieses Tools erläutert. Um zu beginnen, besuchen Sie bitte[ Shopify: Tagging durch ]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/)Dritte.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Das Update aktualisiert die native Android-Brücke vom Braze Android SDK`36.0.0`auf `39.0.0`.
    - Aktualisiert die native iOS-Brücke vom Braze SWIFT SDK`12.0.0`auf `13.2.0`. Dies umfasst die Unterstützung für Xcode 26.

- [Braze SWIFT SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Update der Braze Swift SDK Bindungen, um Versionen der `13.0.0+` SemVer Bezeichnung zu benötigen. Dies erlaubt die Kompatibilität mit jeder Version des Braze SDK von `13.0.0` bis hin zu, aber nicht einschließlich, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Veröffentlichung am 19\. August 2025

### Standardisierung der Zeitzonenkonsistenz für Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

Wenn Sie am [Early Access]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) des [Canvas-Schritts]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) teilnehmen, werden alle Zeitstempel mit einem Datums-/Zeit-Typ aus den Event-Eigenschaften in aktionsbasierten Canvases stets auf [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) normalisiert. Weitere Informationen hierzu referenzieren Sie auf [Standardisierung der Zeitzonenkonsistenz]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilität der Daten

#### Selbstverwaltete angepasste Domains

{% multi_lang_include release_type.md release="General access" %}

[Mit Self-Service-Benutzerdefinierten Domänen]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) können Sie Ihre eigenen benutzerdefinierten Domänen für SMS, RCS und WhatsApp direkt über Ihr Braze-Dashboard konfigurieren und verwalten. Sie können problemlos bis zu 10 angepasste Domains an einem Ort hinzufügen, überwachen und verwalten.

#### Segment-Funnel-Statistiken

Auswählen Sie[ „Funnel-Statistiken anzeigen“,]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) um die Statistiken für diese Filtergruppe anzuzeigen und zu sehen, wie sich jeder hinzugefügte Filter auf Ihre Segment-Statistiken auswirkt. Sie sehen eine geschätzte Anzahl und einen Prozentsatz der Nutzer:innen, die bis zu diesem Zeitpunkt von allen Filtern erfasst werden. Sobald die Statistiken für eine Filtergruppe angezeigt werden, werden sie automatisch mit einem Update versehen, sobald Sie die Filter ändern. 

#### Neue Antwortfelder für`/campaigns/details`den Endpunkt für Push-Benachrichtigungen

Die`messages`Antwort für Push-Benachrichtigungen enthält nun zwei neue Felder:

- `image_url`: Eine Bild-URL für ein Android-Benachrichtigungsbild, ein iOS-Benachrichtigungsbild oder ein Web-Push-Symbolbild.
- `large_image_url`: Eine URL für ein Webbenachrichtigungsbild für Android Chrome und Windows Web-Push-Aktionen.

#### Definition von PII-Feldern

Die Auswahl und [Definition bestimmter Felder als PII-Felder]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) wirkt sich lediglich darauf aus, was Nutzer:innen auf dem Braze-Dashboard sehen können, und hat keinen Einfluss darauf, wie die Nutzerdaten in solchen PII-Feldern behandelt werden.

Bitte wenden Sie sich an Ihre Rechtsabteilung, um die Einstellungen Ihres Dashboards mit den für Ihr Unternehmen geltenden Datenschutzbestimmungen und -Richtlinien, einschließlich derjenigen zur [Datenaufbewahrung]({{site.baseurl}}/api/data_retention/), abzustimmen.

#### Weitergabe eines Download-Links für den Berichts-Builder

Sie können [einen Dashboard-Link]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) zum Bericht [freigeben,]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) indem Sie **„Freigeben“** und anschließend **„Link freigeben“** oder **„E-Mail senden oder einen Zeitplan für das Mailen erstellen“** auswählen.

### Kreativität entfesseln

#### Angepasste Kopfzeilen für E-Mails mit Drag-and-Drop-Funktion

Verwenden Sie`<head>`Tags, um CSS und Metadaten in Ihre E-Mail-Nachricht einzufügen. Beispielsweise können Sie diese Tags verwenden, um ein Stylesheet oder ein Favicon hinzuzufügen. Liquid wird in`<head>`Tags unterstützt.

### Robuste Kanäle

#### Unscharfe Best Practices

Wir haben einen [Abschnitt mit bewährten Verfahren]({{site.baseurl}}) hinzugefügt, um Ihnen dabei zu helfen, Ihre unklare Opt-out-Nachricht sorgfältig zu konfigurieren und Ihren Abonnent:innen ein klares, konformes und positives Erlebnis zu bieten.

#### WhatsApp-Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) ist eine Erweiterung des bestehenden WhatsApp-Kanals, mit der Sie interaktive und dynamische Messaging-Erlebnisse schaffen können. 

#### WhatsApp-eingehende Anfragen zu Produkten

Nutzer:innen können auf Ihre Produkt- oder Katalognachricht mit [Fragen zum Produkt]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions) antworten. Diese werden als eingehende Nachrichten empfangen und können anschließend mit einem Aktions-Pfad sortiert werden.

Darüber hinaus extrahiert Braze die Produkt-ID und die Katalog-ID aus diesen Fragen. Wenn Sie also die Automatisierung von Antworten durchführen oder Fragen an ein anderes Team (z. B. den Kundensupport) weiterleiten möchten, können Sie diese Angaben hinzufügen.

### KI und ML Automatisierung

#### Neue Artikel zu Anwendungsfällen von BrazeAI™

Wir haben neue Anwendungsfallartikel hinzugefügt, um Ihnen dabei zu helfen, BrazeAI™ optimal zu nutzen. Diese Leitfäden zeigen praktische Möglichkeiten auf, wie Sie KI in Ihren Strategien für Engagement einsetzen können, darunter:

- [Voraussichtliche Abwanderung]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case): Identifizieren Sie Kund:innen, bei denen die Gefahr eines Abwanderns besteht, und ergreifen Sie frühzeitig Maßnahmen.
- [Vorhersagbare Ereignisse]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case): Antizipieren Sie wichtige Aktionen der Nutzer:innen und gestalten Sie Erlebnisse in Realtime.
- [Empfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Liefern Sie relevantere Inhalte und Produkte auf Grundlage des Kundenverhaltens.

#### MCP-Server

{% multi_lang_include release_type.md release="Beta" %}

Der [Braze MCP-Server]({{site.baseurl}}/user_guide/brazeai/mcp_server/), eine sichere und schreibgeschützte Verbindung, ermöglicht es KI-Tools wie Claude und Cursor, auf nicht PII-bezogene Braze-Daten zuzugreifen, um Fragen zu beantworten, Trends zu analysieren und Insights zu gewinnen, ohne die Daten zu verändern.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Erweitert die Funktionalität von, `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`um bei „optionalen” Authentifizierungsfehlern zu triggern.
        - Die Delegate-Methode`BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`wird nun sowohl für „Erforderliche“ als auch für „Optionale“ Authentifizierungsfehler getriggert.
        - Wenn Sie nur „erforderliche“ SDK-Authentifizierungsfehler behandeln möchten, fügen Sie eine Überprüfung hinzu, die sicherstellt, dass  innerhalb Ihrer Implementierung`BrazeSDKAuthError.optional` dieser Delegatenmethode false ist.
    - Korrigiert die Verwendung von Enablement`Braze.Configuration.sdkAuthentication`, damit es bei Enablement wirksam wird.
        - Zuvor wurde der Wert dieser Konfiguration vom SDK nicht verwendet, und der Token wurde stets an Anfragen angehängt, sofern er vorhanden war.
        - Wenn diese Konfiguration aktiviert ist, fügt das SDK das SDK-Authentifizierungstoken nur noch an ausgehende Netzwerkanfragen an.
    - Die Setter für alle Eigenschaften von`Braze.FeatureFlag`  und alle Eigenschaften von`Braze.Banner`  wurden erstellt`private`. Die Eigenschaften dieser Klassen sind nun schreibgeschützt.
    - Entfernt die`Braze.Banner.id`Eigenschaft, die in Version`11.4.0` veraltet war.
        - Verwenden Sie stattdessen, um die ID für Tracking`Braze.Banner.trackingId` einer Kampagne eines Banners zu lesen.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Aktualisiert die nativen Android SDK-Versionsbindungen von [Braze Android SDK 36.0.0 auf 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Aktualisiert die nativen SWIFT SDK-Versionsbindungen von [Braze SWIFT SDK 12.0.0 auf 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Das`sdkAuthenticationError`Ereignis triggert nun sowohl bei „erforderlichen“ als auch bei „optionalen“ Authentifizierungsfehlern.
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Unterstützung für .NET 9.0 für die iOS- und Android-Bindungen wurde hinzugefügt.
        - Dadurch wird die Unterstützung für .NET 8.0 entfernt.
        - Hierfür ist [mindestens iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0) erforderlich.
    - Die Android-Bindung von [Braze Android 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) erhielt ein Update [auf 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Die iOS-Bindung wurde von [Braze SWIFT SDK 10.0.0 auf 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Diese Version enthält APIs für das Banner-Feature, wird jedoch derzeit von diesem SDK nicht vollständig unterstützt. Sollten Sie Banners in Ihrer .NET MAUI-App verwenden wollen, wenden Sie sich bitte an Ihren Kundensupport-Manager, bevor Sie die Integration durchführen.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Die interne iOS-Implementierung der`enableSdk`Methode wurde mit einem Update aktualisiert, um nun : `_requestEnableSDKOnNextAppRun`anstelle von zu verwenden`setEnabled`, das im SWIFT SDK als veraltet markiert wurde.
    - Durch den Aufruf dieser Methode ist es nicht mehr erforderlich, die App neu zu starten, damit die Änderung wirksam wird. Das SDK wird nun aktiviert, sobald diese Methode ausgeführt wird.
    - Das Update der native Android-Brücke erfolgte vom [Braze Android SDK`36.0.0`auf`37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Veröffentlichung am 22\. Juli 2025

### Export von Sicherheitsereignissen mit Amazon S3

Sie können [Sicherheitsereignisse]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/) automatisch [zu Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), einem Cloud-Speicheranbieter, [exportieren]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), wobei ein täglicher Job um Mitternacht UTC ausgeführt wird. Nach der Einrichtung ist es nicht mehr erforderlich, Sicherheitsereignisse manuell aus dem Dashboard zu exportieren.

### Flexibilität der Daten

#### CSV-Import

{% multi_lang_include release_type.md release="General availability" %}

Sie können den CSV-Import verwenden, um Benutzerattribute und angepasste Events in Braze wie `first_name`, `last_destination_searched`, und aufzuzeichnen `trip_booked`und zu aktualisieren. Um loszulegen, siehe [CSV-Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### API-Nutzungswarnungen

{% multi_lang_include release_type.md release="General availability" %}

API-Nutzungswarnungen bieten wichtige Einblicke in Ihre API-Nutzung und ermöglichen es Ihnen, unerwarteten Datenverkehr proaktiv zu erkennen. Durch die Einrichtung dieser Benachrichtigungen zum Tracking wichtiger API-Anfragevolumina können Sie Realtime-Benachrichtigungen erhalten und Probleme beheben, bevor sie sich auf Ihre Marketingkampagnen auswirken.

#### Rate-Limits für die Workspace-API

Mit den API-Rate-Limits für Workspaces können Sie eine maximale Anzahl von API-Anfragen festlegen, die ein Workspace an einen bestimmten Endpunkt senden kann, z. B. an`/users/track`  oder SDK-Daten. Sie können auch Rate-Limits auf eine Gruppe von Workspaces anwenden, was bedeutet, dass die Beschränkung für alle Workspaces in dieser Gruppe gilt.

#### Neue Currents Veranstaltungen

Diese neuen Ereignisse wurden dem Currents-Glossar hinzugefügt:

- [Banner Abbruchereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Banner Klick-Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Banner Impressionen Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Banner Angezeigte Veranstaltungen]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook-Ausfallereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Standardzeitbereich für Analytics für Kampagnen

Standardmäßig wird für [**die Kampagnen-Analytics**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) der Zeitraum der letzten 90 Tage ab dem aktuellen Zeitpunkt angezeigt. Dies bedeutet, dass, wenn die Kampagne vor mehr als 90 Tagen gestartet wurde, die Analytics für den angegebenen Zeitraum den Wert „0“ anzeigen. Um alle Analytics für ältere Kampagnen anzuzeigen, passen Sie bitte den Berichtszeitraum an.

#### Aktualisiertes Verhalten für den Schritt „Canvas-Experiment-Pfad“

Wenn Ihr Canvas ein aktives oder laufendes [Experiment]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) enthält und Sie den aktiven Canvas aktualisieren (auch wenn dies nicht im Schritt „Experiment-Pfad“ erfolgt), wird das laufende Experiment beendet. Um das Experiment neu zu starten, können Sie den bestehenden Experiment-Pfad trennen und einen neuen starten, oder Sie duplizieren das Canvas und starten ein neues Canvas. 

Weitere Informationen finden Sie unter [Bearbeiten von Leinwänden nach dem Start]({{site.baseurl}}/post-launch_edits/).

#### Eine schnellere Rate-Limit-Einstellung ist für`/users/export/ids`den Endpunkt verfügbar.

Sie können die [Rate-Limits für den Endpunkt /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) auf 40 Anfragen pro Sekunde erhöhen, indem Sie die folgenden Anforderungen erfüllen:

- Für Ihren Workspace ist das Standard-Rate-Limit (250 Anfragen pro Minute) aktiviert. Bitte wenden Sie sich an Ihren Braze-Account Manager, um weitere Unterstützung beim Entfernen bereits bestehender Rate-Limits zu erhalten.
- Ihre Anfrage enthält denfields_to_exportParameter, um alle Felder aufzulisten, die Sie erhalten möchten.

#### Neue Übersetzung für E-Mail-Templates-Endpunkte

{% multi_lang_include release_type.md release="Early access" %}

Verwenden Sie diese Endpunkte, um Übersetzungen und Sprachversionen für E-Mail-Templates anzuzeigen und Updates durchzuführen:

- [ERHALTEN: Die Quellübersetzungen anzeigen]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [ERHALTEN: Eine bestimmte Übersetzung und Lokalisierung für den E-Mail-Template-Endpunkt anzeigen]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [ERHALTEN: Alle Übersetzungen und Sprachversionen für ein E-Mail-Template anzeigen]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: Bitte führen Sie ein Update der Übersetzungen für ein E-Mail-Template durch.]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Kreativität entfesseln

#### Landing Pages

Sie können Ihre Landing Page [responsiv]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) gestalten[,]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) indem Sie Spalten auf kleineren Bildschirmen vertikal stapeln. Um dies zu aktivieren, fügen Sie bitte eine Spalte in die Zeile ein, die Sie responsiv gestalten möchten, und schalten Sie anschließend im Abschnitt **„Spalten anpassen“** die Option **„Auf kleineren Bildschirmen vertikal stapeln“** um.

### Robuste Kanäle

#### Bot-Filter für E-Mails

{% multi_lang_include release_type.md release="General availability" %}

Richten Sie in Ihren [E-Mail-Einstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) einen Bot-Filter ein, um alle mutmaßlichen Maschinen- oder Bot-Klicks auszuschließen. Ein "Bot-Klick" in E-Mails bezieht sich auf einen Klick auf Hyperlinks innerhalb einer E-Mail, die von einem automatisierten Programm generiert wurde. Indem Sie diese Bot-Klicks filtern, können Sie Nachrichten absichtlich triggern und an Empfänger:in zustellen, die engagiert sind.

#### Produktblöcke per Drag-and-Drop verschieben

{% multi_lang_include release_type.md release="Early access" %}

Mit dem [Drag-and-Drop-Editor]({{site.baseurl}}/dnd_product_blocks/) können Sie Produktblöcke schnell zu Ihren Nachrichten hinzufügen und konfigurieren, um Produkte nahtlos zu präsentieren, ohne dass Sie dafür angepassten Liquid-Code erstellen müssen. Das Drag-and-Drop-Feature für Produktblöcke ist derzeit nur für E-Mails verfügbar.

#### Text für Landing Pages und In-App-Nachrichten

Mit Span-Text können Sie Textblöcken bestimmte Formatierungen zuweisen, ohne dass Sie dafür benutzerdefinierten Code für Ihre [Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) und [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks) benötigen. Markieren Sie dazu den Text, den Sie formatieren möchten, und wählen Sie dann **„Mit Span umbrechen“ als Formatierung** aus. 

#### Bitte klicken Sie hier, um WhatsApp zu öffnen.

[Anzeigen, die zu WhatsApp weiterleiten,]({{site.baseurl}}/whatsapp_use_cases/) sind eine effektive Methode, um sowohl neue als auch bestehende Kund:innen über Meta-Anzeigen auf Facebook, Instagram oder anderen Plattformen zu gewinnen. Nutzen Sie diese Anzeigen, um für Ihre Produkte und Serviceleistungen zu werben und gleichzeitig die Nutzer:innen auf Ihre Präsenz auf WhatsApp aufmerksam zu machen. 

### Neue Braze Partnerschaften

#### Shopify Visitory API – E-Commerce

Braze sammelt über In-Browser-Nachrichten Informationen über Besucher, wie z.B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden dann an Shopify gesendet. Diese Daten helfen Händlern, die Besucher ihres Shops zu erkennen und ein personalisiertes Einkaufserlebnis zu schaffen.

#### Okendo – E-Commerce

Die Integration von Braze und [Okendo]({{site.baseurl}}/partners/okendo/) ist für mehrere Produkte der Okendo-Plattform verfügbar, darunter Bewertungen, Treueprogramme, Empfehlungen, Umfragen und Quizze. Okendo übermittelt angepasste Events und Benutzerattribute an Braze, die zur Personalisierung und zum Triggern von Nachrichten verwendet werden können.

#### Lemnisk – Customer Data Platform (CDP)

Die Integration von Braze und [Lemnisk]({{site.baseurl}}/partners/lemnisk/) ermöglicht es Marken und Unternehmen, das volle Potenzial von Braze auszuschöpfen, indem sie als CDP-gesteuerte Intelligence-Ebene fungiert, die Nutzerdaten plattformübergreifend in Realtime vereinheitlicht und die gesammelten Informationen und Verhaltensweisen der Nutzer:innen in Realtime an Braze sendet.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Web SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Die`Banner.html`Eigenschaften und`logBannerImpressions``logBannerClick`Methoden wurden entfernt. Verwenden Sie stattdessen[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner), das automatisch das Tracking für Impressionen und Klicks übernimmt.
    - Die Unterstützung für das veraltete Newsfeed-Feature wurde eingestellt. Dies umfasst die Entfernung der Feed-Klasse und der damit verbundenen Methoden.
    - Die Felder „created“ und „categories“, die von älteren Newsfeed-Karten verwendet wurden, wurden aus[`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)den Unterklassen entfernt.
    - Das Feld „linkText“ wurde ebenfalls aus der Unterklasse[`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) „Card“ und ihrem Konstruktor entfernt.
    - Die Definitionen wurden präzisiert und es gab ein Update der Typen, um darauf hinzuweisen, dass bestimmte SDK-Methoden explizit „undefined“ zurückgeben, wenn das SDK nicht initialisiert ist, wodurch die Typisierungen an das tatsächliche Laufzeitverhalten angepasst wurden. Dies könnte zu neuen TypeScript-Fehlern in Projekten führen, die auf den vorherigen (unvollständigen) Typisierungen basierten.
    - Die Darstellung von In-App-Nachrichten mit`CENTER_CROP``cropType`(wie beispielsweise`FullScreenMessage`  im Standard) erfolgt nun über ein`<img>`  -Tag anstelle von ,`<span>` um die Barrierefreiheit zu verbessern. Dies kann bestehende CSS-Anpassungen für die`.ab-center-cropped-img`Klasse oder ihre untergeordneten Elemente beeinträchtigen.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Die interne iOS-Implementierung der`enableSdk`Methode wurde aktualisiert, um setEnabled`_requestEnableSDKOnNextAppRun`: anstelle von zu verwenden, das im SWIFT SDK als veraltet markiert wurde.
        - Durch den Aufruf dieser Methode ist es nicht mehr erforderlich, die App neu zu starten, damit die Änderung wirksam wird. Das SDK wird nun aktiviert, sobald diese Methode ausgeführt wird.
    - Das Update auf die native Android-Brücke [von Braze Android SDK 36.0.0 auf 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) wurde durchgeführt.
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1–12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
