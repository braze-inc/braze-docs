---
nav_title: Diferenças entre atributos de campanha e de tela no Braze
article_title: Diferenças entre atributos de campanha e de tela no Braze
page_order: 1

page_type: reference
description: "Este artigo de ajuda compara o nome e os IDs dos atributos da campanha e da canva entre as fontes no Braze."
platform: API
---

# Como os atributos da campanha e da canva diferem entre as fontes no Braze

Os nomes e IDs da campanha, do canva e da etapa do canva estão disponíveis no Liquid, em nossa API REST e no Currents. Essas atribuições mapeiam o mesmo valor em todas as três fontes, mas podem ter nomes diferentes. Esta página é destinada a ajudar você a fazer conexões entre os três.

## Casos de uso

### Liquid

Os atributos de Campanha e Canva estão disponíveis como tags Liquid em nosso dashboard {% raw %}(como `{{campaign.${api_id}}}`){% endraw %}. Você pode usar Liquid para passar esses atributos na própria mensagem, em uma chamada de Conteúdo Conectado ou como pares de chave-valor. Isso geralmente é feito para fins de rastreamento.

### API REST

Os atributos de Campanha e Canva também estão disponíveis no [endpoint de detalhes da campanha de exportação]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) ou [endpoint de detalhes da Canva de exportação]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/). Você pode usar nossa API REST para criar mapeamentos—ou seja, uma lista de todos os nomes do canva e seus IDs correspondentes.

### Currents

Os atributos da Campanha e da Canva estão ligados a [eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) do Currents. Isso é importante para que você possa determinar com qual campanha ou componente de canva um push ou abertura de e-mail está associado.

## Atributos da campanha

| Atributo | Liquid | API REST | Currents |
| --- | --- | --- | --- |
| Nome da campanha | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| ID da campanha | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (usado como entrada para a própria chamada da API) | campaign_id |
| Nome da variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (mapear o nome da variante para o ID da variante usando o endpoint Exportar detalhes da campanha) |
| ID da Variante | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Atributos da canva

| Atributo | Liquid | API REST | Currents |
| --- | --- | --- | --- |
| Nome do canva | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| ID do canva | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (usado como entrada para a própria chamada da API) | canvas_id |
| Nome da variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| ID da Variante | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Nome da etapa | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ID da etapa | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Canal de mensagem | N/D | `steps.messages.message_variation_id.channel` | N/A (inerente ao tipo de evento, como envio de push ou abertura de e-mail) |
| ID da mensagem | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }