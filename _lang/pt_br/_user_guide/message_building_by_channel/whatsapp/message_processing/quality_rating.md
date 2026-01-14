---
nav_title: Classificação de qualidade e limites de mensagens
article_title: Classificação de qualidade e limites de mensagens 
description: "Este artigo de referência aborda como o Meta influencia sua classificação de qualidade e os limites de mensagens para o canal do WhatsApp."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Classificação de qualidade e limites de mensagens

> O Meta influencia sua classificação de qualidade e [os limites de mensagens](https://developers.facebook.com/docs/whatsapp/messaging-limits) a partir do momento em que você começa a usar o canal do WhatsApp e continuará a influenciá-los em resposta ao seu uso do WhatsApp.

## Definições

| Palavra | Definição |
| --- | --- |
| Índice de qualidade | Uma classificação baseada nas mensagens recentes que seus clientes receberam nos últimos sete dias. Essa classificação é determinada pelo feedback de seus clientes, como o motivo do bloqueio de seu número de telefone e outros problemas relatados. Consulte a documentação do Meta para saber mais [sobre sua classificação de qualidade](https://www.facebook.com/business/help/896873687365001).|
| Limite de mensagens | O número máximo de conversas iniciadas pela empresa que você pode iniciar com cada um dos seus números de telefone em um período contínuo de 24 horas. |
{: .reset-td-br-1 .reset-td-br-2 }

## Integração  

Quando uma nova conta do WhatsApp Business é criada, o Meta usa uma variedade de fatores para determinar o limite de envio inicial. Você pode encontrar esse limite no Gerenciador de Negócios do WhatsApp e detalhes adicionais na página Informações sobre o número de telefone. 

Consulte a documentação do Meta para saber mais sobre como [verificar seu limite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) e [os requisitos de número de telefone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Taxa de transferência

O Meta inicia cada número de telefone comercial registrado com uma taxa de transferência de 80 mensagens por segundo. Os upgrades para 1.000 mensagens por segundo podem ser feitos automaticamente ou mediante solicitação. Informações. 

Consulte a documentação do Meta para saber mais sobre sua [taxa de transferência](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Ritmo do modelo

Os modelos de marketing criados recentemente e os modelos de marketing pausados que deixam de ser pausados estão potencialmente sujeitos ao ritmo. O critério de seleção de ritmo do Meta é orientado principalmente pelo histórico de qualidade do modelo. Quando você usa um modelo de marketing criado recentemente ou um modelo de marketing não pausado recentemente, as mensagens serão enviadas normalmente até que um limite não especificado seja atingido. Depois que esse limite for atingido, as mensagens subsequentes que usarem esse modelo serão retidas para dar tempo suficiente para o feedback do cliente. 

Consulte a documentação do Meta para saber mais sobre o [ritmo do modelo](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).