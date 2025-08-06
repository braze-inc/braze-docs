---
nav_title: Julho
page_order: 6
noindex: true
page_type: update
description: "Este artigo contém notas de versão de julho de 2016."
---

# Julho de 2016

## Filtragem do registro de erros do console do desenvolvedor por tipo de erro

Esse upgrade facilita o uso do registro de mensagens de erro no console do desenvolvedor para solucionar problemas com as integrações do Braze. Esta é uma atualização de usabilidade que permite filtrar o registro de erros de mensagens por tipo e facilita muito a localização e a identificação de problemas de integração específicos.

## Adicionado registro de data e hora para o envio do último push de rastreamento de desinstalação

O Braze detecta desinstalações enviando um push silencioso para os apps de um cliente para ver quais dispositivos respondem. Esse recurso adiciona um registro de data e hora discreto que indica quando o rastreamento de desinstalação foi executado pela última vez. Esse registro de data e hora pode ser encontrado na página Configurações, onde o rastreamento de desinstalação está configurado. Saiba mais sobre o [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

![Desinstalar a caixa de seleção de rastreamento]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## Adicionados aprimoramentos de teste de webhook

Agora você pode testar o envio de uma mensagem de webhook ao vivo do Braze antes de configurar uma campanha ativa. O envio de uma mensagem de teste permitirá verificar se as mensagens e os pontos de extremidade do servidor foram configurados corretamente em um ambiente seguro de sandbox. Saiba mais sobre [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Adição da variação de mensagens recebidas à exportação CSV dos destinatários da campanha

Adicionamos uma coluna que indica a variação da mensagem recebida à exportação CSV dos destinatários da campanha. Saiba mais sobre como [exportar dados]({{site.baseurl}}/user_guide/data/export_braze_data/) do Braze.

## Limite aproximado do número de impressões

Quando uma mensagem no app tiver recebido um determinado número de impressões, o Braze deixará de permitir que os usuários se tornem elegíveis para receber a mensagem. Saiba mais sobre como definir [limites aproximados para impressões]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap).

![Limite de impressão IAM]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})

