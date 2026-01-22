---
nav_title: Wie Braze Currents verwendet
article_title: Wie Braze Currents verwendet
page_order: 6
page_type: tutorial
description: "Dieser Currents-Artikel führt Sie durch die grundlegenden Schritte zur Einrichtung der richtigen Dateneingabe für Ereignisdaten sowie zur Übertragung dieser Daten in eine Datenbank und ein Business-Intelligence (BI)-Tool."
tool: Currents
 
---

# Wie Braze Currents verwendet

> Braze verwendet Currents! Das stimmt, wir mögen unser eigenes Produkt so sehr, dass wir es in Verbindung mit einigen [unserer Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) verwenden.

Wir filtern unsere Daten aus unseren E-Mail- und Push-Kampagnen in ein Business Insights-Tool, Looker, aber der Weg dorthin ist interessant. Wir verwenden eine leicht umgekehrte Version der ETL-Methode (Extract, Transform, Load) – wir ändern lediglich die Reihenfolge in ELT (Extract, Load, Transform)!

## Schritt 1: Event-Daten eingeben und aggregieren

Nachdem wir Kampagnen mit einem unserer Engagement-Tools (wie Kampagnen oder Canvas) eingeführt haben, verfolgen wir die Daten der Ereignisse mit unserem eigenen System sowie mit dem unserer E-Mail Partner. Einige dieser Daten werden im Dashboard zusammengefasst und angezeigt, aber wir sind daran interessiert, tiefer einzutauchen!

## Schritt 2: Event-Daten an einen Partner für die Datenspeicherung senden

Wir haben Currents eingerichtet, um Braze-Ereignisdaten zur Speicherung und Extraktion an Amazon S3 zu senden. Wir wissen, dass Sie [Athena](https://aws.amazon.com/athena/) verwenden können, um auf S3 aufzusetzen und Abfragen durchzuführen. Das ist eine großartige kurzfristige Lösung. Aber wir wollten eine langfristige Lösung mit einer relationalen Datenbank und einem Business-Intelligence/Analytics-Tool. (Das empfehlen wir auch für Sie.)

Wir betrachten S3 als unseren Schlüssel zum Schloss! Dadurch eröffnen sich so viele Möglichkeiten, unsere Daten zu verschieben, zu drehen und zu analysieren, indem wir sie dorthin übertragen, wo wir sie benötigen. Wir achten jedoch darauf, unsere Daten in S3 nicht zu transformieren, da wir eine ganz bestimmte Struktur dafür haben.

## Schritt 3: Transformation von Ereignisdaten mit einer relationalen Datenbank

Aus S3 wählen wir ein Warehouse (in unserem Fall [Snowflake-Datenfreigabe](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) oder Snowflake Reader-Konten). Dort transformieren wir sie und verschieben sie dann zu Looker, wo wir Blöcke eingerichtet haben, die unsere Daten strukturieren und organisieren.

Snowflake ist nicht die einzige Lagerhausoption. Weitere Optionen sind [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) und mehr!

### Snowflake Reader-Konten

Snowflake Reader Accounts bieten Nutzern:innen Zugriff auf die gleichen Daten und Funktionen wie [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), ohne dass ein Snowflake-Konto oder eine Kundenbeziehung zu Snowflake erforderlich ist. Mit den Reader-Konten erstellt Braze ein Konto und stellt Ihnen Zugangsdaten zur Verfügung, mit denen Sie sich anmelden und auf Ihre Daten zugreifen können. Dies führt dazu, dass die gemeinsame Nutzung von Daten und die Abrechnung der Nutzung vollständig von Braze übernommen wird. 

Wenn Sie mehr erfahren möchten, wenden Sie sich an Ihren Customer-Success-Manager.

#### Zusätzliche Ressourcen
Hilfreiche Ressourcen zur Überwachung der Nutzung finden Sie in den Artikeln Snowflake [Ressourcenmonitore](https://docs.snowflake.com/en/user-guide/resource-monitors.html) und [Anzeigen der Guthabenverwendung im Lager](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Schritt 4: Verwenden Sie ein Business-Intelligence (BI)-Tool, um Ihre Daten zu bearbeiten.

Schließlich verwenden wir ein BI-Tool, um unsere Daten zu analysieren, sie in Charts und andere visuelle Tools umzuwandeln und vieles mehr. Dazu verwenden wir [Looker und Looker Blocks](https://www.marketplace.looker.com/), damit wir nicht jedes Mal ETL oder ELT durchführen müssen, wenn die Daten von Currents übertragen werden.

Fühlen Sie sich inspiriert, dasselbe zu tun? Schauen Sie sich die folgende Dokumentation an, um mehr über diese zu erfahren und wie Sie sie zum Aufbau Ihrer Datenbank verwenden können!

- [Block „Nutzerverhalten“](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Block „Nachrichten-Engagement“](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

