---
nav_title: "Sobre a MMS"
article_title: Sobre a MMS
page_order: 0
description: "Este artigo de referência aborda o que são as mensagens MMS e os casos de uso geral do canal de envio de mensagens."
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Sobre mensagens MMS

> O MMS, também conhecido como Multimedia Message Service, é usado para enviar mensagens contendo ativos multimídia (JPEG, GIF, PNG) para telefones celulares.<br><br>Assim como o SMS, o MMS é um canal de envio de mensagens de alta urgência que permite que você se comunique com os clientes imediatamente de uma forma que não é possível com nenhum outro canal. No entanto, o MMS amplia os recursos do SMS, oferecendo a possibilidade de adicionar mídia a um SMS que, de outra forma, seria apenas texto.

## Casos de uso em potencial

| Caso de uso | Explicação |
| --- | --- |
| Promoções | Alcance os usuários com campanhas de SMS de alta visibilidade, mas também aproveite o aspecto de mídia do MMS para atrair compradores com o que você está oferecendo. | 
| Campanhas de reengajamento | Reengajar os clientes que aceitaram receber SMS quando todos os outros canais não conseguirem trazê-los de volta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conheça a MMS

### Disponibilidade de MMS

A maioria das operadoras americanas e canadenses suporta o recebimento e a exibição de ativos multimídia nos telefones de seus clientes. Para operadoras internacionais, o Braze converterá automaticamente as mensagens MMS enviadas de um número de telefone compatível com os EUA ou Canadá, e somente para destinos que não sejam compatíveis com MMS. Para essas mensagens, o Braze substituirá a mídia anexada por um URL curto adicionado ao corpo da mensagem com um link para o arquivo.

### Grupos de inscrições

Um [grupo de inscrições][1] é uma coleção de números de telefone de envio (códigos curtos, códigos longos e IDs de remetente alfanuméricos) que são usados para um tipo específico de finalidade de envio de mensagens. Seu grupo de inscrições requer um número de telefone que esteja habilitado para MMS. Fale com seu gerente de conta Braze para saber como ativar esse recurso.

### Limites e taxa de transferência de mensagens MMS

Para MMS, o limite da mensagem é de 1 MB (isso inclui o ativo multimídia e o tamanho do corpo da mensagem). Por precaução, a Braze recomenda não exceder 600 KB para o seu ativo multimídia e incluir um corpo de mensagem.

A taxa de transferência de MMS é de um segmento por segundo por meio de um código longo.

### MMS de entrada

Quando um usuário envia uma mensagem de entrada que contém um item de mídia, a Braze expõe o URL do item de mídia no Currents e no Liquid por meio da tag Liquid {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Tipos de arquivos aceitos

A Braze aceita arquivos JPEG, GIF, PNG e VCF e permite anexar um único ativo multimídia à sua mensagem MMS.


[picture]: {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
