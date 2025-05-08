---
nav_title: Grupo de controle global 
article_title: Relatório do grupo de controle global
page_type: reference
description: "Este artigo de referência aborda as métricas de relatório encontradas na página Relatórios do grupo de controle global no dashboard."
tool: 
  - Reports

---

# Relatório do grupo de controle global

> O Relatório do grupo de controle global permite comparar o seu grupo com uma amostra do grupo de tratamento. Sua amostra de tratamento é uma seleção aleatória de usuários sem controle, aproximadamente o mesmo número de usuários do seu controle, gerada usando o método Random Bucket Number.

Para visualizar um relatório do seu [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) no dashboard, acesse **Análise de dados** > **Relatório do grupo de controle global**. 

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essa página pode ser encontrada em **Dados**.
{% endalert %}

Em seguida, selecione o parâmetro com o qual deseja executar o relatório (sessões ou um evento personalizado específico) e clique em **Run Report (Executar relatório**).

![][6]

## Sobre seu relatório

Ao gerar o relatório, escolha um evento - sessões ou qualquer evento personalizado - para comparar os grupos de tratamento e de controle. Em seguida, escolha um período para o qual deseja visualizar os dados. Lembre-se de que, se tiver salvo vários experimentos de grupos de controle em diferentes períodos de tempo, evite incluir dados de mais de um experimento no relatório.

Lembre-se de que as métricas de porcentagem em seu relatório são arredondadas. Por exemplo, nos casos em que o número de conversões é uma porcentagem muito baixa do seu grupo de controle ou de tratamento geral, a taxa de conversão pode ser arredondada para 0%.

Por fim, como em vários outros relatórios em nossa plataforma, esse relatório exibe uma porcentagem de [confiança]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#understanding-confidence) para sua métrica de mudança de controle. Observe que, nos casos em que a taxa de conversão entre o grupo de controle e o de tratamento é idêntica, é de se esperar uma confiança de 0%; isso indica que há 0% de chance de haver uma diferença de performance entre os dois grupos.

### Tamanho dos grupos

Antes de maio de 2024, o grupo de controle global foi excluído do arquivo do usuário, mas o grupo de amostra do grupo de tratamento não foi. A partir de maio de 2024, ambos os grupos serão excluídos do arquivamento de usuários. Isso pode fazer com que o seu grupo de amostra do grupo de tratamento e o grupo de controle global tenham tamanhos significativamente diferentes. Na próxima vez que você redefinir o Grupo de Controle Global, essa discrepância será resolvida e você verá tamanhos de grupo semelhantes.

## Métricas de relatório

| Métrico | Definição | Cálculo |
| -- | -- | -- |
| Desvio em relação ao grupo de controle | Calcula o aumento entre a taxa de conversão dos grupos de tratamento e de controle. | ((Taxa de conversão do tratamento – taxa de conversão do controle) ÷ taxa de conversão do controle) * 100 |
| Aumento incremental | A diferença no total de eventos entre os grupos de tratamento e de controle. Essa métrica busca responder à pergunta: "Quantos eventos de conversão a mais o grupo de tratamento alcançou?". | Total de eventos para o tratamento - total de eventos para o controle |
| Porcentagem de aumento incremental | A porcentagem do total de eventos do seu tratamento que pode ser atribuída ao seu tratamento (versus o comportamento natural do usuário). Isso é calculado dividindo-se o aumento incremental (número) pelo número total de eventos de seu grupo de tratamento. | Aumento incremental (número) ÷ Total de eventos para o grupo de tratamento |
| Taxa de conversão | Em média, a porcentagem de usuários no seu grupo de controle ou de tratamento que concluem o evento selecionado todos os dias durante o período de tempo escolhido. Se o número de conversões for muito pequeno e os grupos de controle ou de tratamento forem muito grandes, a taxa de conversão poderá ser arredondada para 0%. | Média da porcentagem de usuários que realizam o evento selecionado todos os dias durante o período de tempo escolhido. |
| Estimativa do tamanho do grupo | O número estimado de usuários nos grupos de controle e tratamento durante o período de tempo selecionado. | O tamanho máximo de associação que os grupos de controle e de tratamento atingiram durante o período escolhido para o relatório. |
| Total de eventos | O número total de vezes que o evento selecionado ocorreu durante o período de tempo escolhido. Não é exclusivo (por exemplo, se um usuário executar um evento duas vezes durante o período de tempo, o evento será incrementado duas vezes). | Soma do número de vezes que um evento ocorreu a cada dia durante o período de tempo escolhido. |
| Eventos por usuário | O número médio estimado de vezes que os usuários em cada grupo concluíram seus eventos de conversão durante o período de tempo selecionado. | Total de eventos ÷ tamanho estimado do grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[6]: {% image_buster /assets/img/control_group/control_group6.png %}