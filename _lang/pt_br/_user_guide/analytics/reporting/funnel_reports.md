---
nav_title: Relatórios de funil
article_title: Relatórios de funil para campanhas e Canvas
page_order: 6
page_type: reference
description: "Esta página aborda os benefícios dos relatórios de funil, como configurá-los e como interpretar seu relatório."
tool: Reports
---

# Relatórios de funil

> Os relatórios de funil oferecem um relatório visual que permite analisar as jornadas que seus clientes percorrem após receberem uma campanha ou um Canvas. ![Relatório de funil 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Se a sua campanha ou o Canvas usar um grupo de controle ou várias variantes, será possível entender como as diferentes variantes afetaram o funil de conversão em um nível mais granular e otimizar com base nesses dados.

![Relatório de funil 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Configuração de relatórios de funil

![Relatório de funil 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Você pode executar relatórios de funil para campanhas ativas e canvas existentes. Esses relatórios mostram uma série de eventos pelos quais um destinatário de campanha progride ao longo de 1 a 30 dias a partir da data em que ele entra no Canvas ou na campanha. Um usuário é considerado convertido em uma etapa do funil se ele realizar o evento na ordem especificada.

Os relatórios de funil estão disponíveis nos seguintes locais do dashboard:

- A página de **análise de dados da campanha** para uma campanha específica
- A página **Informações do Canvas** para um Canvas específico, selecionando o botão **Analisar Variantes** 

{% alert important %}
Os relatórios de funil não estão disponíveis para [campanhas de API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Etapa 1: Selecione um intervalo de datas

É possível selecionar um período de tempo para o relatório (nos últimos seis meses) e refinar os dados para ver os usuários que, ao entrarem na campanha ou no Canvas, concluíram os eventos do funil dentro de um período definido (máximo de 30 dias). No exemplo a seguir, seu funil procuraria usuários que receberam essa campanha ou Canvas nos últimos sete dias e concluíram o funil em três dias.

{% alert note %}
Se você definir o período para concluir o funil como um dia, o evento do funil deverá ocorrer dentro de 24 horas após o recebimento da mensagem. No entanto, se você selecionar vários dias, o período será contado como dias do calendário no fuso horário da empresa.
{% endalert %}

![Relatório de funil para um Canvas com "Últimos 7 dias" selecionado no menu suspenso de período de tempo.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Etapa 2: Selecionar eventos para etapas do funil

Para cada relatório de funil, o primeiro evento é quando o usuário recebe sua mensagem. A partir daí, os eventos subsequentes que você escolher afunilam o número de usuários que realizaram esses eventos, bem como os eventos anteriores. 

#### Eventos de relatório de funil disponíveis

| Campanha | Sessão iniciada, Compra efetuada, Evento personalizado realizado, Evento de engajamento com mensagem |
| Canvas | Sessão iniciada, Compra efetuada, Evento personalizado realizado, Recebeu etapa do Canvas, Interagiu com a etapa |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
O evento de relatório **Interagiu com a etapa** só pode ser usado com etapas do canva que usam os canais de envio de mensagens por e-mail ou push.
{% endalert %}

![Relatório de funil para um Canvas com um menu suspenso dos eventos de relatório disponíveis.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Os relatórios de funil permitem comparar o sucesso de suas mensagens além dos eventos de conversão ou de engajamento com mensagens que você configurou inicialmente. Portanto, se houver um evento de conversão que você não adicionou inicialmente, ainda poderá rastrear as conversões desse evento usando um funil.

Por exemplo, se você selecionar um período de relatório de 14 dias, seguido pelos eventos `Added to cart` e `Made purchase`, verá o número de usuários que adicionaram ao carrinho em 14 dias após o recebimento da mensagem e o número de usuários que adicionaram ao carrinho e fizeram uma compra em 14 dias após o recebimento da campanha.

Como outro exemplo, você pode querer ver a porcentagem de usuários que converteram em um e-mail depois de clicar nele. Para calcular isso, você pode criar um relatório em que o segundo evento é o clique no seu e-mail e o terceiro evento é a realização do seu evento de conversão.

Depois de selecionar **Criar relatório**, o relatório do funil pode levar vários minutos para ser gerado. Durante esse tempo, você pode sair do relatório e navegar para outras páginas do dashboard. Você receberá uma notificação no dashboard quando seu relatório estiver pronto.

## Interpretação do relatório do funil

No relatório do funil, é possível comparar diretamente o grupo de controle com as variantes que você configurou. Cada evento consecutivo mostrará a porcentagem de usuários anteriores que concluíram essa ação e converteram no funil.

### Componentes do relatório de funil

- **Eixo horizontal**: Exibe a porcentagem de destinatários de mensagens que realizaram essas ações. 
- **Gráfico**: Exibe o número de mensagens recebidas, o número de usuários que executaram as ações anteriores, bem como a ação escolhida, a taxa de conversão e a alteração percentual em relação ao controle.
- **Opção Regenerar**: Permite que você gere novamente o relatório e indica quando o relatório atual foi gerado pela última vez. 
- **Variantes**: Com colunas coloridas, o relatório de funil permite até 8 variantes e um grupo de controle. Por padrão, o **gráfico** mostrará apenas três variantes. Para ver mais, você pode selecionar manualmente o restante das variantes.

![Gráfico de relatório de funil.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para campanhas com múltiplas variantes**: A Braze mostrará uma tabela com métricas para cada evento e variante e a alteração percentual em relação ao controle. A taxa de conversão é o número de usuários que realizaram o evento (e os subsequentes) por destinatário de mensagem.

**Para campanhas com reelegibilidade**: Se um usuário receber a campanha mais de uma vez no período do relatório, a Braze determinará se o usuário deve ser incluído no funil com base nas ações que esse usuário realizou após a primeira vez que recebeu a campanha dentro do período.
- Note que pode haver uma discrepância entre o funil e os valores de conversão padrão, pois os usuários podem converter mais de uma vez com a reelegibilidade, mas os relatórios de funil converterão no máximo uma vez, mesmo que um usuário realize o evento mais de uma vez. 

**Para campanhas multivariantes com reelegibilidade**: Se um usuário receber várias variantes da campanha durante o período do relatório, a Braze determinará se ele deve ser incluído no funil de variantes com base nas ações que esse usuário realizou após a primeira vez que recebeu a variante da campanha. Isso significa que o mesmo usuário poderia contar para várias variantes diferentes se recebesse várias variantes durante o período do funil.

{% alert important %}
Os usuários órfãos não são rastreados nos relatórios de funil. Quando um usuário anônimo entra em um Canvas ou campanha e depois é identificado pelo método `changeUser()`, seu ID da Braze é alterado. Os relatórios de funil rastreiam apenas os eventos de acompanhamento que correspondem ao ID do usuário no momento da entrada e não levam em conta os eventos realizados pelo usuário após a alteração de seu ID. Isso significa que os eventos de conversão realizados pelo usuário após ser identificado não serão incluídos no relatório do funil.
{% endalert %}

## Perguntas frequentes

### Por que a análise de dados no Canvas é diferente do relatório de funil?

A análise de dados no nível da etapa do Canvas e os relatórios de funil usam regras de escopo diferentes para o mesmo intervalo de datas, portanto, não é esperado que coincidam. As diferenças se resumem a como cada relatório define "quais eventos contam".

**Análise de dados do Canvas (Analisar Variantes):** O intervalo de datas filtra os eventos por **quando eles ocorreram**. Se você selecionar de 1 a 7 de janeiro, verá todas as entradas e eventos de conversão que aconteceram durante essa janela — independentemente de quando o usuário entrou no Canvas. Um usuário que entrou em 1º de janeiro, mas converteu em 8 de janeiro, mostraria uma entrada e zero conversões, porque a conversão ficou fora das datas selecionadas. O período de conversão configurado na etapa do Canvas também pode se estender bem além de 14 dias, então a análise de dados no nível da etapa pode capturar conversões em um horizonte mais longo.

**Relatórios de funil:** O intervalo de datas filtra os usuários por **quando eles entraram** no Canvas. Se você selecionar de 1 a 7 de janeiro, o relatório inclui todos os usuários que entraram durante essa janela e, em seguida, rastreia suas ações por até 14 dias após a entrada (ou qualquer período que você configurar no funil). O mesmo usuário que entrou em 1º de janeiro e converteu em 8 de janeiro mostraria uma entrada e uma conversão, porque a conversão aconteceu dentro do período pós-entrada.

Além disso, os relatórios de funil exigem que os eventos ocorram na ordem especificada e contam cada usuário no máximo uma vez, enquanto a análise de dados do Canvas conta todas as conversões e engajamentos sem restrição de ordem.