---
nav_title: "MMS"
article_title: Sobre a MMS
page_order: 15
description: "Este artigo de referência aborda o que são mensagens MMS e os casos de uso geral do canal MMS."
page_type: reference
alias: /about_mms/
channel:
  - MMS
search_rank: 2  
---

# [![Curso de aprendizado do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"} Sobre mensagens MMS

> O MMS, também conhecido como Multimedia Message Service, é usado para enviar mensagens com recursos multimídia (JPEG, GIF, PNG) para telefones celulares.<br><br>Assim como o SMS, o MMS é um canal de mensagens de alta urgência que permite que você se comunique com os clientes imediatamente de uma forma que não é possível com nenhum outro canal. No entanto, o MMS amplia os recursos do SMS, oferecendo a possibilidade de adicionar mídia a um SMS que, de outra forma, seria apenas texto.

## Casos de uso em potencial

| Caso de uso | Explicação |
| --- | --- |
| Promoções | Alcance usuários com campanhas de SMS de alta visibilidade, mas também aproveite o aspecto de mídia do MMS para atrair compradores com o que você está oferecendo. | 
| Campanhas de reengajamento | Reengajar os clientes que optaram por receber SMS quando todos os outros canais não conseguirem trazê-los de volta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conheça o MMS

### Disponibilidade de MMS

A maioria das operadoras americanas e canadenses suporta o recebimento e a exibição de ativos multimídia nos telefones de seus clientes. Para operadoras internacionais, o Braze converterá automaticamente as mensagens MMS enviadas de um número de telefone compatível com os EUA ou Canadá, e somente para destinos que não suportam MMS. Para essas mensagens, o Braze substituirá a mídia anexada por uma URL curta adicionada ao corpo da mensagem que vincula ao arquivo.

### Grupos de assinatura

Um [grupo de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) é uma coleção de números de telefone de envio (códigos curtos, códigos longos e IDs de remetente alfanuméricos) que são usados para um tipo específico de finalidade de mensagens. Seu grupo de assinatura requer um número de telefone habilitado para MMS. Fale com seu gerente de conta Braze sobre como ativar esse recurso.

### Limites e taxa de transferência de mensagens MMS

As operadoras impõem seus próprios limites de tamanho de arquivo, o que acaba determinando o sucesso dos envios de MMS. Esses limites podem variar de acordo com a região e a operadora, portanto, para ficar mais seguro, a Braze recomenda não exceder 600 KB para o seu ativo multimídia e incluir um corpo de mensagem. Também recomendamos a realização de testes para confirmar que sua mídia pode ser entregue nas operadoras dos usuários.

A taxa de transferência de MMS é de um segmento por segundo por meio de um código longo.

#### Limites de tamanho de arquivo da operadora

| Tamanho do arquivo | Manuseio de transportadoras |
| --- | --- |
| 300 KB | Todas as operadoras devem lidar de forma confiável com mensagens MMS desse tamanho. |
| 600 KB | Esse é considerado o tamanho máximo padrão de arquivo para MMS na maioria das operadoras. |
| 1 MB |  A maioria das operadoras dos EUA e do Canadá pode processar mensagens MMS desse tamanho, embora isso possa variar de acordo com a operadora. Algumas operadoras podem permitir tamanhos de arquivo maiores do que esse. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### MMS de entrada

Quando um usuário envia uma mensagem de entrada que contém um item de mídia, o Braze expõe o URL do item de mídia no Currents e no Liquid por meio da tag Liquid {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Tipos de arquivos aceitos

O Braze aceita arquivos JPEG, GIF, PNG e VCF e permite que você anexe um único recurso multimídia à sua mensagem MMS.


