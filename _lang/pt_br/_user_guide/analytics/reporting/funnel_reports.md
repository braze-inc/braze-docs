---
nav_title: Relatórios de funil
article_title: Relatórios de funil para campanhas e telas
page_order: 6
page_type: reference
description: "Esta página aborda os benefícios dos relatórios de funil, como configurá-los e como interpretar seu relatório."
tool: Reports
---

# Relatórios de funil

> O relatório de funil oferece um relatório visual que permite analisar as jornadas dos clientes após o recebimento de uma campanha ou Canvas. Relatório de funil 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Se sua campanha ou Canvas usar um grupo de controle ou várias variantes, você poderá entender como as diferentes variantes afetaram o funil de conversão em um nível mais granular e otimizar com base nesses dados.

Relatório de funil 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Configuração de relatórios de funil

Relatório de funil 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Você pode executar relatórios de funil para campanhas ativas e Canvases existentes. Esses relatórios mostram uma série de eventos pelos quais um destinatário de campanha progride ao longo de 1 a 30 dias a partir da data em que ele entra no Canvas ou na campanha. Um usuário é considerado convertido por meio de uma etapa do funil se ele realizar o evento na ordem especificada.

Os relatórios de funil estão disponíveis nos seguintes locais do painel:

- A página **Campaign Analytics** de uma campanha específica
- A página **Detalhes do Canvas** para um Canvas específico, selecionando o botão **Analisar Variantes**  

{% alert important %}
Os relatórios de funil não estão disponíveis para [campanhas de API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Etapa 1: Selecione um intervalo de datas

Você pode selecionar um período de tempo para o relatório (nos últimos seis meses) e refinar os dados para ver os usuários que, ao entrarem na campanha ou no Canvas, concluíram os eventos do funil dentro de uma janela definida (máximo de 30 dias). No exemplo a seguir, seu funil procuraria usuários que receberam essa campanha ou Canvas nos últimos sete dias e concluíram o funil em três dias.

{% alert note %}
Se você definir a janela para concluir o funil como um dia, o evento do funil deverá ocorrer dentro de 24 horas após o recebimento da mensagem. Entretanto, se você selecionar vários dias, a janela de tempo será contada como dias do calendário no fuso horário da empresa.
{% endalert %}

Relatório de funil para um Canvas com "Últimos 7 dias" selecionado no menu suspenso de período.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Etapa 2: Selecionar eventos para as etapas do funil

Para cada relatório de funil, o primeiro evento é quando o usuário recebe sua mensagem. A partir daí, os eventos subsequentes que você escolher afunilam o número de usuários que realizaram esses eventos, bem como os eventos anteriores. 

#### Eventos de relatório de funil disponíveis

| Campanha | Sessão iniciada, Compra efetuada, Evento personalizado realizado, Evento de engajamento de mensagem
| Canvas | Iniciou sessão, Fez compra, Realizou evento personalizado, Recebeu etapa do Canvas, Interagiu com etapa
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
O evento de relatório **Interagiu com a etapa** só pode ser usado com etapas do Canvas que usam os canais de e-mail ou de mensagens push.
{% endalert %}

Relatório de funil para um Canvas com um menu suspenso dos eventos de relatório disponíveis.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Os relatórios de funil permitem que você compare o sucesso de suas mensagens além dos eventos de conversão ou eventos de engajamento de mensagens que você configurou inicialmente. Portanto, se houver um evento de conversão que você não adicionou inicialmente, ainda poderá rastrear as conversões desse evento usando um funil.

Por exemplo, se você selecionar uma janela de tempo de relatório de 14 dias, seguida pelos eventos `Added to cart` e `Made purchase`, verá o número de usuários que adicionaram ao carrinho em 14 dias após o recebimento da mensagem e o número de usuários que adicionaram ao carrinho e fizeram uma compra em 14 dias após o recebimento da campanha.

Como outro exemplo, você pode querer ver a porcentagem de usuários que converteram em um e-mail depois de clicar nele. Para calcular isso, você pode criar um relatório em que o segundo evento é o clique no seu e-mail e o terceiro evento é a realização do seu evento de conversão.

Depois de selecionar **Criar relatório**, o relatório do funil pode levar vários minutos para ser gerado. Durante esse tempo, você pode navegar do relatório para outras páginas do painel. Você receberá uma notificação no painel quando o relatório estiver pronto.

## Interpretação do relatório do funil

No relatório do funil, é possível comparar diretamente o grupo de controle com as variantes que você configurou. Cada evento consecutivo mostrará a porcentagem de usuários anteriores que concluíram essa ação e converteram no funil.

### Componentes do relatório de funil

- **Eixo horizontal**: Exibe a porcentagem de destinatários de mensagens que realizaram essas ações. 
- **Gráfico**: Exibe o número de mensagens recebidas, o número de usuários que executaram as ações anteriores, bem como a ação escolhida, a taxa de conversão e a alteração percentual em relação ao controle.
- **Opção Regenerar**: Permite que você gere novamente o seu relatório e indica quando o relatório atual foi gerado pela última vez. 
- **Variantes**: Denotado por colunas coloridas, o relatório de funil permite até 8 variantes e um grupo de controle. Por padrão, o **gráfico** mostrará apenas três variantes. Para ver mais, você pode selecionar manualmente o restante das variantes.

Gráfico de relatório de funil.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para campanhas com várias variantes**: O Braze mostrará uma tabela com métricas para cada evento e variante e a alteração percentual em relação ao controle. A taxa de conversão é o número de usuários que realizaram o evento (e os subsequentes) por destinatário da mensagem.

**Para campanhas com reelegibilidade**: Se um usuário receber a campanha mais de uma vez na janela de tempo do relatório, o Braze determinará se o usuário deve ser incluído no funil com base nas ações que esse usuário realizou após a primeira vez que recebeu a campanha dentro da janela de tempo.
- Observe que pode haver uma discrepância entre o funil e os valores de conversão padrão, pois os usuários podem converter mais de uma vez com a reelegibilidade, mas os relatórios de funil converterão no máximo uma vez, mesmo que um usuário realize o evento mais de uma vez. 

**Para campanhas multivariadas com reelegibilidade**: Se um usuário receber várias variantes da campanha durante a janela de tempo do relatório, o Braze determinará se elas devem ser incluídas no funil de variantes com base nas ações que esse usuário realizou após a primeira vez que recebeu a variante da campanha. Isso significa que o mesmo usuário poderia contar para várias variantes diferentes se recebesse várias variantes durante a janela de tempo do funil.

{% alert important %}
Os usuários órfãos não são rastreados nos relatórios de funil. Quando um usuário anônimo entra em um Canvas ou campanha e, posteriormente, é identificado pelo método `changeUser()`, sua ID Braze é alterada. Os relatórios de funil só rastreiam os eventos de acompanhamento que correspondem ao ID do usuário no momento da entrada e não levam em conta os eventos realizados pelo usuário após a alteração do ID. Isso significa que os eventos de conversão realizados pelo usuário após ser identificado não serão incluídos no relatório do funil.
{% endalert %}

