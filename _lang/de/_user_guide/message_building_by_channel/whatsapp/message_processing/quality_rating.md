---
nav_title: Qualitätsbewertung und Messaging-Limits
article_title: Qualitätsbewertung und Grenzen der Nachrichtenübermittlung 
description: "In diesem Referenzartikel erfahren Sie, wie Meta Ihre Qualitätsbewertung und die Messaging-Limits für den WhatsApp-Kanal beeinflusst."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Qualitätsbewertung und Messaging-Limits

> Meta beeinflusst Ihre Qualitätsbewertung und Ihre [Nachrichtenlimits](https://developers.facebook.com/docs/whatsapp/messaging-limits) von dem Moment an, in dem Sie den WhatsApp-Kanal zu nutzen beginnen, und wird diese auch weiterhin als Reaktion auf Ihre WhatsApp-Nutzung beeinflussen.

## Definitionen

| Text | Definition |
| --- | --- |
| Bewertung der Qualität | Eine Bewertung, die auf den jüngsten Nachrichten basiert, die Ihre Kunden in den letzten sieben Tagen erhalten haben. Diese Bewertung wird durch die Rückmeldungen Ihrer Kunden bestimmt, wie z.B. der Grund für die Sperrung Ihrer Telefonnummer und andere Probleme, die Sie melden. Sehen Sie sich die Dokumentation von Meta an, um mehr [über Ihre Qualitätsbewertung](https://www.facebook.com/business/help/896873687365001) zu erfahren.|
| Messaging-Limit | Die maximale Anzahl von geschäftlich initiierten Gesprächen, die Sie mit jeder Ihrer Telefonnummern innerhalb eines 24-Stunden-Zeitraums führen können. |
{: .reset-td-br-1 .reset-td-br-2 }

## Onboarding  

Wenn ein neues WhatsApp Business-Konto erstellt wird, verwendet Meta eine Reihe von Faktoren, um das anfängliche Sendelimit zu bestimmen. Sie finden dieses Limit in Ihrem WhatsApp Business Manager und weitere Details auf der Seite Einblicke in Ihre Telefonnummern. 

Lesen Sie die Dokumentation von Meta, um mehr über die [Überprüfung Ihres Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) und die [Anforderungen an die Telefonnummer](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) zu erfahren.

## Durchsatz

Meta startet jede registrierte Geschäftsrufnummer mit einem Durchsatz von 80 Nachrichten pro Sekunde. Upgrades auf 1.000 Nachrichten pro Sekunde können automatisch oder auf Anfrage erfolgen. Informationen. 

Sehen Sie sich die Dokumentation von Meta an, um mehr über Ihren [Durchsatz](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput) zu erfahren.

## Template-Platzierung

Vor Kurzem erstellte Marketing-Templates und Marketing-Templates, die pausiert wurden und wieder aktiviert werden, unterliegen möglicherweise dem Tempo. Das Auswahlkriterium von Meta für das Tempo hängt in erster Linie von der Qualität Ihrer Template ab. Wenn Sie eine kürzlich erstellte Marketingvorlage oder eine kürzlich nicht pausierte Marketingvorlage verwenden, werden die Nachrichten normal versendet, bis ein nicht spezifizierter Schwellenwert erreicht ist. Wenn dieser Schwellenwert erreicht ist, werden nachfolgende Nachrichten, die diese Vorlage verwenden, zurückgehalten, um genügend Zeit für das Feedback der Kunden zu haben. 

Lesen Sie die Dokumentation von Meta, um mehr über das [Tempo von Templates](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing) zu erfahren.