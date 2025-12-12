---
nav_title: Grupo de controle global
article_title: Relatório de grupo de controle global
page_type: reference
description: "Esta página aborda as métricas de relatório encontradas na página Relatórios do Grupo de Controle Global no painel."
tool: 
  - Reports

---

# Relatório do Grupo de Controle Global

> O Relatório do Grupo de Controle Global permite comparar o seu grupo com uma amostra de tratamento. Sua amostra de tratamento é uma seleção aleatória de usuários sem controle, aproximadamente o mesmo número de usuários que o seu controle, gerada usando o método Random Bucket Number.

## Visualização de um relatório

Para visualizar um relatório do seu [Grupo de Controle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) no painel, navegue até **Analytics** > **Global Control Group Report**. 

Em seguida, selecione o parâmetro com o qual deseja executar o relatório (sessões ou um evento personalizado específico) e selecione **Run Report (Executar relatório**).

\![]({% image_buster /assets/img/control_group/control_group6.png %})

## Configuração de seu relatório

Ao gerar o relatório, escolha um evento - sessões ou qualquer evento personalizado - para comparar os grupos de tratamento e controle. Em seguida, escolha um período de tempo para o qual deseja visualizar os dados. Lembre-se de que, se você salvou vários experimentos de grupos de controle em períodos diferentes, evite incluir dados de mais de um experimento no seu relatório.

Lembre-se de que as métricas de porcentagem em seu relatório são arredondadas. Por exemplo, nos casos em que o número de conversões é uma porcentagem muito baixa do seu grupo de controle ou tratamento geral, a taxa de conversão pode ser arredondada para 0%.

Por fim, como em vários outros relatórios em nossa plataforma, esse relatório exibe uma porcentagem de [confiança]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) para sua métrica de mudança de controle. Observe que, nos casos em que a taxa de conversão entre o controle e o tratamento é idêntica, é de se esperar uma confiança de 0%; isso indica que há 0% de chance de haver uma diferença no desempenho entre os dois grupos. 

### Tamanho dos grupos

Antes de maio de 2024, o Grupo de Controle Global foi excluído do arquivo do usuário, mas o grupo de amostra de tratamento não foi. A partir de maio de 2024, ambos os grupos serão excluídos do arquivamento de usuários. Isso pode fazer com que o seu grupo de amostra de tratamento e o Grupo de Controle Global tenham tamanhos significativamente diferentes. Na próxima vez que você redefinir o Grupo de Controle Global, essa discrepância será resolvida e você verá tamanhos de grupo semelhantes.

{% alert note %}
Cada espaço de trabalho tem no máximo um Grupo de Controle Global e um grupo de amostra de tratamento. O grupo de amostra de tratamento é o mesmo grupo de usuários, independentemente da configuração do relatório do Controle Global.
{% endalert %}

## Métricas de relatório

| Métrico | Definição | Cálculo |
| -- | -- | -- |
| Mudança de controle | Isso calcula o aumento entre a taxa de conversão dos grupos de tratamento e de controle. | ((Taxa de conversão do tratamento - taxa de conversão do controle) ÷ taxa de conversão do controle) * 100 |
| Incremental Uplift | A diferença no total de eventos entre os grupos de tratamento e controle. Essa métrica busca responder à pergunta: "Quantos eventos de conversão a mais o grupo de tratamento alcançou?". | Total de eventos para o tratamento - total de eventos para o controle |
| Porcentagem de elevação incremental | A porcentagem do total de eventos do seu tratamento que pode ser atribuída ao seu tratamento (em comparação com o comportamento natural do usuário). Isso é calculado dividindo-se o aumento incremental (número) pelo número total de eventos do seu grupo de tratamento. | Aumento incremental (número) ÷ Total de eventos para o grupo de tratamento |
| Taxa de conversão | A porcentagem estimada de usuários no seu grupo de controle ou tratamento que concluem o evento selecionado durante o período de tempo selecionado. Isso é calculado adicionando o número de eventos do período de tempo e dividindo-o pela soma de usuários dentro do grupo a cada dia. Isso só pode ser aproximado porque o tamanho do grupo flutua regularmente à medida que novos usuários entram no Grupo de Controle Global e os eventos são eventos totais - e não únicos. Se o número de conversões for muito pequeno e seus grupos de controle ou de tratamento forem muito grandes, a taxa de conversão poderá ser arredondada para 0%. Se o número de eventos for muito alto, por exemplo, nos casos em que um usuário pode fazer mais de um evento por dia, a taxa de conversão poderá ser superior a 100%. | Soma do número de eventos para esses usuários durante esse período de tempo ÷ soma dos usuários no grupo a cada dia |
| Tamanho estimado do grupo | O número estimado de usuários nos grupos de controle e tratamento durante o período de tempo selecionado. | O tamanho máximo de associação que os grupos de controle e tratamento atingiram durante o período de tempo escolhido para o relatório. |
| Número total de eventos | O número total de vezes que o evento selecionado ocorreu durante o período de tempo escolhido. Isso não é exclusivo (por exemplo, se um usuário realizar um evento duas vezes durante o período de tempo, o evento será incrementado duas vezes). | Soma do número de vezes que um evento ocorreu a cada dia durante o período de tempo escolhido. |
| Eventos por usuário | O número médio estimado de vezes que os usuários em cada grupo concluíram seus eventos de conversão durante o período de tempo selecionado. | Total de eventos ÷ tamanho estimado do grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

