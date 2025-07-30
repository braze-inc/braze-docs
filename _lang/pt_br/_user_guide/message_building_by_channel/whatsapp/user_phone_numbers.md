---
nav_title: "Números de telefone do usuário"
article_title: Números de telefone de usuários do WhatsApp
page_order: 1.5
description: "Este artigo de referência aborda a formatação de números de telefone do WhatsApp, como importar números de telefone e como adicionar usuários a grupos de inscrições do WhatsApp."
page_type: reference
channel: 
  - WhatsApp
  
---

# Números de telefone do usuário

> Este artigo discutirá diferentes tópicos relacionados aos números de telefone dos seus usuários ou clientes.

Os números de telefone são exibidos no perfil do usuário em formatos locais, mas não estarão no formato usado para importar o número (`(724) 123 4567`).

## Importação de números telefônicos

É possível importar números de telefone fazendo [upload de um CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou [via API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) para criar um usuário.

### Formatação

É importante importar números que não sejamU.S. no formato [`E.164`](https://en.wikipedia.org/wiki/e.164) incluindo o "+" e o código do país. Qualquer número de telefone não fornecido nesse formato será interpretado como um número dos EUA.  

Se um número de telefone for coagido para o formato E.164, mas não passar na validação, o Braze não poderá enviar mensagens do WhatsApp para esse número. Todos os usuários com números de telefone que não são formatáveis sairão automaticamente de uma etapa do Canva que inclui o WhatsApp

Todos os números de U.S. devem ser números de telefone válidos, com 10 dígitos e um código de área válido. Eles podem ser inseridos sem o código `+` e o código do país, pois o Braze assumirá e mapeará todos os números telefônicos válidos de 10 dígitos como números U.S.

Todos os números internacionais devem começar com `+`, seguido do código do país e do número de telefone. (e.g `+442071838750`)

![]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

No entanto, para garantir a precisão caso esteja enviando para várias regiões com diferentes códigos de país ou de área, é recomendável usar o formato `E.164`, mesmo para números de telefone baseados em U.S.

Você pode ver as diferenças entre a formatação de números na localização e a formatação universal em `E.164` na tabela a seguir:

| País | Local | Código do país | `E.164` |
|---|---|---|---|
| EUA | `4155552671` | 1 | `+14155552671` |
| REINO UNIDO | `02071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Adição de usuários a um grupo de inscrições do WhatsApp

Para que um cliente receba uma mensagem do WhatsApp, ele deve ter um número de telefone válido e ser aceito em um grupo de inscrições. Para saber mais, consulte [Grupos de inscrições do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).


### Vários usuários com o mesmo número de telefone

Se vários usuários tiverem o mesmo número de telefone em um segmento de uma única campanha ou etapa do Canva, o Braze desduplicará o envio e enviará apenas uma mensagem para esse número de telefone. 


