---
nav_title: Calculadora de cobrança
article_title: Calculadoras de cobrança SMS e RCS
page_order: 5
description: "Este artigo de referência cobre o que é um segmento de SMS, como eles são contados para cobrança, bem como coisas a ter em mente ao criar cópias de mensagens SMS e RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# Calculadoras de cobrança SMS e RCS

> Na Braze, as mensagens SMS são cobradas por segmento de mensagem, enquanto as mensagens RCS são cobradas por mensagem. Entender o que define um segmento de SMS e os diferentes tipos de cobrança RCS informará sua compreensão de como você será cobrado e ajudará a evitar cobranças acidentais.

## Cópia de mensagem SMS e calculadora de segmentos

As mensagens SMS são cobradas por segmento de mensagem. Entender como as mensagens SMS são divididas é fundamental para entender sua cobrança.

### O que é um segmento de SMS?

O Serviço de Mensagens Curtas (SMS) é um protocolo de comunicação padronizado que permite que dispositivos enviem e recebam mensagens de texto breves. Foi projetado para "se encaixar entre" outros protocolos de sinalização, razão pela qual o comprimento da mensagem SMS é limitado a 160 caracteres de 7 bits, como 1120 bits, ou 140 bytes. Os segmentos de mensagens SMS são os lotes de caracteres que as operadoras de telefonia usam para medir mensagens de texto. As mensagens são cobradas por segmento de mensagem, então os clientes que utilizam SMS se beneficiam muito de entender as nuances de como as mensagens serão divididas.

À medida que você cria uma campanha de SMS ou canva usando o Braze, as mensagens que você cria no criador são representativas do que seus usuários podem ver quando a mensagem é entregue em seus telefones, mas **não é indicativo de como sua mensagem será dividida em segmentos e, em última análise, como você será cobrado**. Compreender quantos segmentos serão enviados e estar ciente dos possíveis excessos que podem ocorrer é sua responsabilidade, mas fornecemos alguns recursos para facilitar isso para você. Confira nossa [calculadora de segmento](#segment-calculator).

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Detalhamento do segmento

O limite de caracteres para **um segmento de SMS independente** é de 160 caracteres ([codificação GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) ou 70 caracteres ([codificação UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) com base no tipo de codificação. No entanto, a maioria dos telefones e redes suporta concatenação, oferecendo mensagens SMS mais longas de até 1530 caracteres (GSM-7) ou 670 caracteres (UCS-2). Portanto, embora uma mensagem possa incluir vários segmentos, se não exceder esses limites de concatenação, será vista como uma mensagem e relatada como tal.

É importante **notar que, à medida que você ultrapassa o limite de caracteres do seu primeiro segmento, caracteres adicionais farão com que toda a sua mensagem seja dividida e segmentada com base em novos limites de caracteres**:
- **Codificação GSM-7**
    - Mensagens que excederem o limite de 160 caracteres agora serão segmentadas em segmentos de 153 caracteres e enviadas individualmente, depois reconstruídas pelo dispositivo do destinatário. Por exemplo, uma mensagem de 161 caracteres será enviada como duas mensagens, uma com 153 caracteres e a segunda com 8 caracteres.
- **Codificação UCS-2**
    - Se você incluir caracteres não GSM, como Emojis, script chinês, coreano ou japonês em mensagens SMS, essas mensagens terão que ser enviadas via codificação UCS-2. Mensagens que excederem o limite inicial de 70 caracteres serão concatenadas em segmentos de mensagem de 67 caracteres. Por exemplo, uma mensagem de 71 caracteres será enviada como duas mensagens, uma com 67 caracteres e a segunda com 4 caracteres.

Independentemente do tipo de codificação, cada mensagem SMS enviada pela Braze tem um limite de até 10 segmentos e é compatível com [Liquid templating]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), Emojis e links.

{% tabs %}
{% tab GSM-7 encoding %}
Número de caracteres | Quantos segmentos?
| -------------------- | ----------------- |
| 0 - 160 caracteres | 1 segmento |
| 161 - 306 caracteres | 2 segmentos |
| 307 - 459 caracteres | 3 segmentos |
| 460 - 612 caracteres | 4 segmentos |
| 613 - 765 caracteres | 5 segmentos |
| 766 - 918 caracteres | 6 segmentos |
| 919 - 1071 caracteres | 7 segmentos |
| 1072 - 1224 caracteres | 8 segmentos |
| 1225 - 1377 caracteres | 9 segmentos |
| 1378 - 1530 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
Número de caracteres | Quantos segmentos?
| -------------------- | ----------------- |
| 0 - 70 caracteres | 1 segmento |
| 71 - 134 caracteres | 2 segmentos |
| 135 - 201 caracteres | 3 segmentos |
| 202 - 268 caracteres | 4 segmentos |
| 269 - 335 caracteres | 5 segmentos |
| 336 - 402 caracteres | 6 segmentos |
| 403 - 469 caracteres | 7 segmentos |
| 470 - 536 caracteres | 8 segmentos |
| 537 - 603 caracteres | 9 segmentos |
| 604 - 670 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Coisas a ter em mente ao criar seu texto

- **Limite de caracteres por segmento**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) tem um limite de 160 caracteres para um único segmento de SMS. Para mensagens com mais de 160 caracteres, todas as mensagens serão segmentadas com um limite de 153 caracteres.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) tem um limite de 70 caracteres por segmento de mensagem. Para mensagens com mais de 70 caracteres, todas as mensagens serão segmentadas com um limite de 67 caracteres.<br><br>
- **Limite de segmento por mensagem**
    - Há uma quantidade máxima de segmentos que você pode enviar devido às limitações do meio. Não mais do que **10 segmentos** de mensagens podem ser enviados em uma única mensagem SMS da Braze.
    - Esses 10 segmentos serão limitados a 1530 caracteres (codificação GSM-7) ou 670 caracteres (codificação UCS-2).<br><br>
- **Compatível com a modelagem Liquid, Conteúdo Conectado, emojis e links**
    - A modelagem Liquid e o Conteúdo Conectado podem colocar sua mensagem em risco de ultrapassar o limite de caracteres para o seu tipo de codificação. Você pode ser capaz de usar o [filtro de truncar palavras](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) para limitar o número de palavras que seu Liquid poderia trazer para a mensagem.
    - Emojis não têm uma contagem de caracteres padrão em todos os emojis, então certifique-se de testar se suas mensagens estão segmentando e exibindo corretamente.
    - Links podem fazer uso de muitos caracteres, resultando em mais segmentos de mensagem do que o pretendido. Embora o uso de encurtadores de links seja possível, eles são melhores usados com códigos curtos. Visite nosso [FAQ de SMS]({{site.baseurl}}/sms_faq/) para saber mais.<br><br>
- **Testes**
    - Sempre teste suas mensagens SMS antes do lançamento, especialmente ao usar Liquid e Conteúdo Conectado, pois ultrapassar os limites de mensagem ou cópia pode resultar em cobranças adicionais. Nota que mensagens de teste contarão para seus limites de mensagens.

### Calculadora de segmentos de SMS {#segment-calculator}
---

{% include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Cobrança de mensagens RCS

As mensagens RCS são cobradas com base em seu conteúdo e no país em que a mensagem é entregue. Para estimar custos com precisão, é essencial entender os diferentes tipos de mensagens e como elas são cobradas.

### Tipos de cobrança RCS

Nossa plataforma suporta dois modelos de cobrança principais: um modelo global e um modelo dos Estados Unidos.

#### Modelo global (mercados não dos EUA)

As mensagens são cobradas por mensagem e classificadas como Básica ou Única.

{% tabs local %}
{% tab Basic %}

Mensagens RCS Básicas são mensagens apenas de texto de até 160 caracteres e são cobradas como uma única mensagem.

{% alert note %}
Adicionar botões ou qualquer elemento rico mudará o tipo de mensagem para uma mensagem RCS Única.
{% endalert %}

{% endtab %}
{% tab Single %}

Mensagens RCS Únicas são mensagens que têm mais de 160 caracteres OU incluem qualquer elemento rico, como botões ou mídia. Essas são cobradas como uma única mensagem, independentemente do comprimento da mensagem.

{% alert note %}
Enviar uma mensagem de texto e um arquivo de mídia separado ainda é cobrado como duas mensagens distintas.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modelo dos Estados Unidos

As mensagens são categorizadas como Ricas ou Mídia Rica.

{% tabs local %}
{% tab Rich messages %}

Mensagens ricas são mensagens apenas de texto com ou sem botões. Elas são cobradas por segmento, com cada segmento limitado a 160 bytes UTF-8, o que significa **o número de caracteres por segmento não é fixo**. Uma mensagem com apenas 160 caracteres em inglês simples é um segmento, mas uma mensagem com texto mais longo e emojis pode ser vários segmentos.

{% endtab %}
{% tab Rich media messages %}

Mensagens de mídia rica incluem um arquivo de mídia (imagem, vídeo) ou um Cartão Rico e são cobradas como uma única mensagem.

{% endtab %}
{% endtabs %}

### Criador de mensagem e dashboard de Uso de Mensagens

À medida que você cria sua mensagem, o criador de mensagem exibirá o tipo de cobrança em tempo real através de um rótulo (RCS Básico, RCS Único, Rico ou Mídia Rica), ajudando você a acompanhar os custos antes de enviar.

Seu [dashboard de Uso de Mensagens]({{site.baseurl}}/message_usage_dashboard/) refletirá esses tipos de cobrança e fornecerá o número de segmentos usados para mensagens dos EUA, proporcionando uma visão transparente do consumo de crédito de mensagens.
