---
nav_title: Alertas de campanha
article_title: Alertas de campanha
page_order: 6

page_type: reference
description: "Este artigo de referência apresenta uma visão geral dos alertas de campanha, seus benefícios e como configurá-los para ajudá-lo a ter tranquilidade."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertas de campanha

> Queremos alertar você quando algo não parecer exatamente como esperado e oferecer a tranquilidade de saber que o navio está navegando sem problemas. Os alertas de limite de campanha proporcionam tranquilidade - seja o primeiro a saber se uma campanha importante enviar mais ou menos mensagens do que o esperado.

Os alertas de campanha estão disponíveis para as seguintes campanhas:

- Campanhas programadas recorrentes
- Campanhas baseadas em ações
- Campanhas disparadas por API

## Configurando seu alerta de campanha

Navegue até a página de análise de dados de sua campanha para começar a configurar seu alerta. Ao selecionar **Configurar alerta**, você poderá especificar os limites superior e inferior do alerta, bem como os destinatários e os canais do alerta.

![Caixa de diálogo Monitoramento de Campanha com dois botões: Cancelar e Salvar.][2]

Para uma campanha recorrente programada, você pode definir limites superiores e inferiores para as mensagens enviadas cada vez que a campanha for enviada. Para uma campanha disparada, você pode definir limites superiores e inferiores para o número de mensagens enviadas por hora e por dia.

Você pode configurar um alerta de e-mail, um alerta de webhook ou ambos. Os alertas de webhook podem ser muito úteis, pois permitem que você envie um alerta para um canal do Slack. Para saber mais sobre a integração de alertas de campanha com o Slack, consulte nossa [documentação][1].

{% alert note %}
Ao definir alertas de campanha para campanhas futuras, você poderá receber atualizações antes do início e depois do término da campanha. Isso ocorre porque os alertas de campanha continuarão a ser enviados até que a campanha seja interrompida manualmente.
{% endalert %}

## Carga útil do webhook de alerta de campanha

A seguir, um exemplo de carga útil para o corpo de um webhook de alerta de campanha. Este exemplo usa um alerta configurado para ser enviado quando as mensagens enviadas caírem abaixo de 500 para um determinado envio de campanha.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

[1]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration
[2]: {% image_buster /assets/img_archive/campaign_alerts.png %}
