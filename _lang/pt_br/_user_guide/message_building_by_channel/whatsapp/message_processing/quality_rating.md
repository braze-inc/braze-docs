---
nav_title: Classificação de Qualidade e Limites de envio de mensagens
article_title: Classificação de Qualidade e Limites de envio de mensagens 
description: "Este artigo de referência cobre como o Meta influencia sua classificação de qualidade e os limites de envio de mensagens para o canal do WhatsApp."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Classificação de qualidade e envio de mensagens limites

> Meta influencia sua classificação de qualidade e [limites de envio de mensagens](https://developers.facebook.com/docs/whatsapp/messaging-limits) desde o momento em que você começa a usar o canal do WhatsApp, e continuará a influenciá-los em resposta ao seu uso do WhatsApp.

## Definições

| Termo | Definição |
| --- | --- |
| Classificação de qualidade | Uma classificação baseada nas mensagens recentes que seus clientes receberam nos últimos sete dias. Esta classificação é determinada pelo feedback dos seus clientes, como o motivo para bloquear seu número de telefone e outros problemas de relatório. Consulte a documentação da Meta para saber mais sobre sua [classificação de qualidade](https://www.facebook.com/business/help/896873687365001).|
| limite de envio de mensagens | O número máximo de conversas iniciadas por empresas que você pode começar com cada um dos seus números de telefone em um período contínuo de 24 horas. |
{: .reset-td-br-1 .reset-td-br-2 }

## Onboarding  

Quando uma nova conta do WhatsApp Business é criada, a Meta usa uma variedade de fatores para determinar o limite inicial de envio. Você pode encontrar esse limite no seu WhatsApp Business Manager e detalhes adicionais na sua página de Insights do Número de Telefone. 

Consulte a documentação da Meta para saber mais sobre [verificar seu limite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) e [requisitos de número de telefone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Throughput

A Meta inicia cada número de telefone comercial registrado com uma taxa de 80 mensagens por segundo. Upgrades para 1.000 mensagens por segundo podem acontecer automaticamente ou mediante solicitação. Informação. 

Consulte a documentação da Meta para saber mais sobre sua [taxa de throughput](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Pacing do modelos

Modelos de marketing criados recentemente e modelos de marketing pausados que são despausados estão potencialmente sujeitos a pacing. Os critérios de seleção de ritmo da Meta são principalmente impulsionados pelo histórico de qualidade do seu modelo. Quando você usa um modelo de marketing recentemente criado ou um modelo de marketing recentemente reativado, as mensagens serão enviadas normalmente até que um limite não especificado seja atingido. Após esse limite ser atingido, mensagens subsequentes usando esse modelo serão retidas para permitir tempo suficiente para o feedback do cliente. 

Consulte a documentação da Meta para saber mais sobre [ritmo de modelo](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).