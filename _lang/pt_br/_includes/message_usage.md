# Painel de uso de mensagens

> O dashboard de uso de mensagens fornece insights de autoatendimento sobre o uso de créditos de SMS, RCS e WhatsApp para uma visão abrangente do uso histórico e atual em comparação com as atribuições do contrato. Essas percepções podem reduzir sua confusão e ajudá-lo a fazer ajustes para prevenir riscos de excedente.

O **Message Usage** dashboard é dividido em três seções:
- [Visão Geral do Uso de Crédito](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

Acesse o dashboard indo para **Configurações** > **Faturamento** > **Uso de Mensagens**.

## Visão geral do uso de créditos de mensagem

**Visão Geral do Uso de Créditos de Mensagem** fornece uma visão geral do uso em todos os canais que utilizam créditos. Você pode ver como está seu ritmo em relação ao seu limite de crédito total e encontrar detalhes sobre seu contrato ativo e seu período de contrato.

Esta página é exibida se você estiver em um contrato de créditos de mensagens. Os canais que usam créditos de mensagem são mostrados na **Visão geral do contrato de créditos**.

{% alert note %}
Se você comprou o WhatsApp, mas não está em um contrato de créditos de mensagem, ainda verá o consumo de créditos para o WhatsApp, porque é assim que os contratos legados do WhatsApp são cobrados. Isso difere do SMS legado, que consome créditos apenas quando você está em um contrato de créditos de mensagem.
{% endalert %}

**Visão Geral do Uso de Créditos de Mensagem** os dados são limitados ao período do contrato, que é exibido na **visão geral do contrato de créditos**. Você não pode filtrar em um intervalo de datas fora do **período de Créditos**.

### Uso de créditos de mensagem sobre o contrato

O **Gráfico de Uso de Créditos de Mensagem** mostra seu uso durante o período de tempo selecionado. A granularidade deste gráfico depende do período de tempo selecionado. Exporte opções de exportação selecionando o menu no canto superior direito do gráfico.

![Painel de visão geral do uso de créditos de mensagens com seções para uso de crédito, visão geral do contrato de crédito e consumo de crédito ao longo do contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS e RCS

**SMS/MMS/RCS Uso de créditos** mostra o detalhamento do uso do canal SMS, MMS e RCS. As colunas na tabela de dados geralmente exigem que você tenha adquirido Créditos de Mensagens (embora o Braze ainda ofereça suporte temporário a modelos de cobrança mais antigos), e as colunas **Taxa de Crédito** e **Créditos** indicam a respectiva taxa do país e os créditos consumidos. Além disso, os azulejos de alto nível indicarão o consumo total de SMS e, quando relevante, MMS ao longo do intervalo de datas selecionado.

Os filtros estão disponíveis, permitindo que você filtre por **país** ou tipo de SMS e RCS.

![SMS/MSS/RCS Uso de créditos com blocos para dados de alto nível e uma seção para consumo por conta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

Ao contrário do **Visão Geral do Uso de Créditos de Mensagem**, esta seção contém dados históricos de períodos contratuais anteriores. 

{% alert note %}
É possível selecionar um intervalo de datas que contenha tanto o uso de não créditos quanto o uso de créditos de mensagem. Neste caso, o consumo que ocorreu fora dos créditos de mensagem será exibido `—` (nulo) nas colunas **Relação de créditos** e **Créditos**.
{% endalert %}

![SMS/MMS/RCS Tabela de uso de créditos com valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp

**Uso de Créditos do WhatsApp** mostra a divisão de uso para o canal do WhatsApp. Os azulejos exibem o uso total de crédito do WhatsApp, que pode ser detalhado na **Uso por conta** seção, aplicando filtros para limitar os resultados da tabela de dados a um espaço de trabalho.

### Filtros

Você pode filtrar seus dados por:
- País
- Conta do WhatsApp Business
- Espaço de trabalho da Braze
- Tipo de categoria de conversa
- Região

![Uso de créditos do WhatsApp com um bloco para o total de créditos consumidos e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Coisas para saber

{% alert important %}
Os dados mostrados no **Uso de Mensagens** dashboard estão no nível do contrato e não estão restritos a uma empresa de dashboard individual ou espaço de trabalho. Estes dados refletem o uso de todos os espaços de trabalho dentro do seu dashboard e, potencialmente, em todos os dashboards (se você tiver múltiplos).
{% endalert %}

- Os dados subjacentes são fornecidos em uma cadência diária, com as tabelas de dados atualizadas às 3h, 9h, 12h e 18h EST. 
- Braze segue a metodologia padrão de arredondamento: os números são arredondados para cima até a décima mais próxima.

