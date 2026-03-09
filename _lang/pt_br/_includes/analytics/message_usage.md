# Painel de Uso de Mensagens

> O painel de uso de mensagens fornece insights de autoatendimento sobre o uso de créditos de SMS, RCS e WhatsApp para uma visão abrangente do uso histórico e atual em comparação com as alocações contratuais. Essas percepções podem reduzir sua confusão e ajudá-lo a fazer ajustes para prevenir riscos de excedente.

O **Message Usage** dashboard é dividido em três seções:
- [Visão Geral do Uso de Crédito](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

Acesse o dashboard indo para **Configurações** > **Faturamento** > **Uso de Mensagens**.

## Visão geral do uso de créditos de mensagem

**Visão Geral do Uso de Créditos de Mensagem** fornece uma visão geral do uso em todos os canais que utilizam créditos. Você pode ver como está seu ritmo em relação ao seu limite de crédito total e encontrar detalhes sobre seu contrato ativo e seu período de contrato.

Esta página exibe se você está em um contrato de créditos de mensagens. Os canais que usam créditos de mensagem são mostrados na **Visão geral do contrato de créditos**.

{% alert note %}
Se você comprou o WhatsApp, mas não está em um contrato de créditos de mensagem, ainda verá o consumo de créditos para o WhatsApp, porque é assim que os contratos legados do WhatsApp são cobrados. Isso difere do SMS legado, que consome créditos apenas quando você está em um contrato de créditos de mensagem.
{% endalert %}

**Visão Geral do Uso de Créditos de Mensagem** os dados são limitados ao período do contrato, que é exibido na **visão geral do contrato de créditos**. Você não pode filtrar em um intervalo de datas fora do **período de Créditos**.

### Uso de créditos de mensagem sobre o contrato

O **Gráfico de Uso de Créditos de Mensagem** mostra seu uso durante o período de tempo selecionado. A granularidade deste gráfico depende do período de tempo selecionado. Exporte opções de exportação selecionando o menu no canto superior direito do gráfico.

![Visão geral do painel de uso de créditos de mensagem com seções para uso de créditos, visão geral do contrato de créditos e consumo de créditos ao longo do contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS e RCS

**Uso de Créditos SMS/MMS/RCS** mostra a divisão do uso para o canal SMS, MMS e RCS. As colunas na tabela de dados geralmente exigem que você tenha comprado Créditos de Mensagem (embora a Braze ainda suporte modelos de cobrança mais antigos temporariamente), e as colunas **Relação de Créditos** e **Créditos** indicam a respectiva taxa do país e os créditos consumidos. Além disso, os blocos de alto nível indicarão o consumo total de SMS e, quando relevante, de MMS ao longo do intervalo de datas selecionado.

Filtros estão disponíveis permitindo que você filtre por **País** ou tipo de SMS e RCS.

![Uso de Créditos SMS/MMS/RCS com blocos para dados de alto nível e uma seção para consumo por conta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

Ao contrário da **Visão Geral do Uso de Créditos de Mensagem**, esta seção contém dados históricos de períodos contratuais anteriores. 

{% alert note %}
É possível selecionar um intervalo de datas que contenha tanto o uso de não créditos quanto o uso de créditos de mensagem. Neste caso, o consumo que ocorreu fora dos créditos de mensagem será exibido `—` (nulo) nas colunas **Relação de créditos** e **Créditos**.
{% endalert %}

![Tabela de Uso de Créditos SMS/MMS/RCS com valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp

**Uso de Créditos do WhatsApp** mostra a divisão de uso para o canal do WhatsApp. Os azulejos exibem o uso total de crédito do WhatsApp, que pode ser detalhado na seção **Uso por conta**, aplicando filtros para limitar os resultados da tabela de dados a um espaço de trabalho.

### Filtros

Você pode filtrar seus dados por:
- País
- Conta do WhatsApp Business
- Espaço de trabalho da Braze
- Tipo de categoria de conversa
- Região

![Uso de Créditos do WhatsApp com um título para créditos totais consumidos e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Coisas para saber

{% alert important %}
Os dados mostrados no dashboard **Uso de Mensagens** estão no nível do contrato e não estão restritos a uma empresa de dashboard individual ou espaço de trabalho. Estes dados refletem o uso de todos os espaços de trabalho dentro do seu dashboard e, potencialmente, em todos os dashboards (se você tiver múltiplos).
{% endalert %}

- Os dados subjacentes são fornecidos em uma cadência diária, com as tabelas de dados atualizadas às 3h, 9h, 12h e 18h EST. O **Painel de Uso de Mensagens** pode levar mais de 24 horas para atualizar.
- Braze segue a metodologia padrão de arredondamento: os números são arredondados para cima até a décima mais próxima.

### Seleção de intervalo de datas

O **Painel de Uso de Mensagens** exclui a data final do intervalo selecionado dos resultados. Por exemplo, se você selecionar de 1 a 31 de outubro, as estatísticas de uso para 31 de outubro são excluídas. Para incluir o último dia do seu período desejado, estenda o intervalo em um dia. Por exemplo, para incluir todo o mês de outubro, selecione de 1 de outubro a 1 de novembro.

### Comparando com provedores de terceiros

Ao comparar os dados de uso de mensagens da Braze com provedores de terceiros (como Infobip), tenha em mente:

- **Segmentos de mensagens vs mensagens**: A Braze conta mensagens SMS por segmentos. Uma única mensagem SMS que é dividida em vários segmentos (por exemplo, devido ao comprimento) é contada como vários segmentos no Braze. Para mais informações, veja [calculadoras de cobrança de SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- **Mensagens baseadas em crédito vs não crédito**: O dashboard inclui mensagens tanto baseadas em crédito quanto não baseadas em crédito. Provedores de terceiros podem contar apenas mensagens baseadas em crédito, o que pode causar discrepâncias nos totais.
- **Entrada vs saída**: Certifique-se de que você está comparando os mesmos tipos de mensagens. Alguns dashboards de terceiros incluem tanto mensagens de entrada quanto de saída em seus totais, enquanto o Braze permite que você filtre por direção.
- **Alinhamento de intervalo de datas**: Porque o dashboard exclui a data final, comparações dia a dia podem alinhar-se mais de perto do que intervalos de datas mais longos. Se você está comparando dados para um período específico, estenda seu intervalo de datas no Braze em um dia para incluir o último dia do seu período de comparação.
