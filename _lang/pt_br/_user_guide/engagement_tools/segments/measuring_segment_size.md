---
nav_title: Medição do tamanho do segmento
article_title: Medição do tamanho do segmento
page_order: 9
page_type: reference
tool: 
- Segments
description: "Esta página aborda como você pode monitorar a associação e o tamanho do seu segmento."
---

# Medição do tamanho do segmento

> Esta página aborda como você pode monitorar a associação e o tamanho do seu segmento.

## Cálculo de associação de segmentos

O Braze atualiza a associação do segmento do usuário à medida que os dados são enviados de volta aos nossos servidores e processados, normalmente de forma instantânea. A associação de segmento de um usuário não será alterada até que a sessão seja processada. Por exemplo, um usuário que cair em um segmento de usuário expirado quando a sessão for iniciada será imediatamente removido do segmento de usuário expirado quando a sessão for processada.

### Cálculo do total de usuários acessíveis

Cada segmento exibe o número total de usuários que são membros desse segmento. Ao filtrar **Usuários de todos os apps**, ele também exibe alguns dos canais de envio de mensagens usados com mais frequência (como web push ou e-mail) e o número de usuários acessíveis para esses canais específicos. 

É possível que o número total de usuários seja diferente do número de usuários alcançáveis por cada canal. Além disso, nem todos os canais estão listados na tabela de usuários acessíveis. Por exemplo, os cartões de conteúdo, webhooks e WhatsApp não são mostrados no detalhamento. Isso significa que a contagem total de usuários acessíveis pode ser maior do que a soma dos usuários de cada canal exibido.

![Uma tabela que exibe o total de usuários acessíveis, divididos por usuários acessíveis por e-mail, envio de e-mail para iOS, envio de e-mail para Android, envio de e-mail pela Web, envio de e-mail para Kindle e envio de e-mail para Android China.][3]

Para que um usuário seja listado como acessível por meio de um determinado canal, ele deve ter ambos:
* Um endereço de e-mail válido ou um token por push associado ao seu perfil; e
* Aceitação ou assinatura do seu app.

Um único usuário pode pertencer a diferentes grupos de usuários acessíveis. Por exemplo, um usuário pode ter um endereço de e-mail válido e um token por push válido para Android e ter aceitação em ambos, mas não ter um token por push para iOS associado. A diferença entre o total de usuários alcançáveis e a soma dos diferentes canais é o número de usuários que se qualificaram para o segmento, mas não são alcançáveis por meio desses canais de comunicação.

## Estatísticas para o tamanho do segmento

As estatísticas estimadas são aproximadas pela amostragem de apenas uma parte do seu segmento, portanto, você deve esperar ver tamanhos estimados maiores ou menores do que o valor real, com espaços de trabalho maiores apresentando margens de erro potencialmente maiores. Para obter uma contagem precisa de usuários em seu segmento, selecione **Calculate Exact Statistics (Calcular estatísticas exatas**). A associação exata do segmento sempre será calculada antes que um segmento seja afetado por uma mensagem enviada em uma campanha ou Canva.

A Braze fornece as seguintes estatísticas sobre o tamanho do segmento. 

### Filtrar estatísticas

Para cada grupo de filtros, é possível visualizar os usuários alcançáveis estimados. Selecione **Expandir estatísticas extras do funil** para ver um detalhamento entre os canais.

![Um grupo de filtros com um filtro para um gênero que não seja desconhecido.][2]{: style="max-width:80%;"}

### Estatísticas do segmento

Para um segmento inteiro, é possível visualizar os usuários alcançáveis estimados, bem como as contagens de usuários estimadas para cada canal, na parte inferior da página. Também é possível visualizar uma contagem exata de usuários acessíveis (tanto para o segmento como um todo quanto para cada canal) selecionando **Calcular estatísticas exatas**.

Note que:
- O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.
- Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.

## Visualização do histórico do tamanho da associação do segmento

Para todos os segmentos, você pode visualizar um gráfico histórico de associação que mostra a associação estimada do segmento para cada dia. Este gráfico mostra como o tamanho de seu segmento mudou ao longo do tempo. Use o menu suspenso para filtrar a associação ao segmento por intervalo de datas.

![Use o menu suspenso Associação histórica para filtrar a associação do segmento por intervalo de datas.][1]

Como o objetivo desse gráfico é dar a você uma noção das tendências gerais de associação ao segmento, a contagem diária é uma estimativa, da mesma forma que o tamanho do segmento é uma estimativa antes de você selecionar **Calculate Exact Statistics (Calcular estatísticas exatas**). E como esse gráfico mostra estimativas, é possível que o tamanho do seu segmento apareça como "0" nesse gráfico, mesmo que o tamanho real (que pode ser determinado após a seleção de **Calculate Exact Stats**) não seja "0". É especialmente provável que o gráfico mostre uma estimativa de "0" se seu segmento for muito pequeno em relação ao tamanho da população de seu espaço de trabalho.

O Braze estima a contagem de membros do segmento consultando um subconjunto de seus usuários e, em seguida, extrapolando esses resultados para todo o seu público. Isso significa que os resultados do gráfico fornecem apenas uma estimativa do número de membros do segmento naquele dia, e espera-se que também flutue diariamente porque uma amostra diferente de usuários pode ser consultada para essa estimativa a cada dia.

{% alert note %}
Todas as estimativas podem ser maiores ou menores do que o valor mostrado em aproximadamente 1% do tamanho total da população de seu espaço de trabalho. Espaços de trabalho maiores com mais usuários têm mais probabilidade de ter estimativas que podem diferir dos cálculos exatos por um valor numérico maior, mesmo que a diferença ainda seja de 1% da população de usuários do espaço de trabalho. Isso significa que é de se esperar que haja diferenças maiores entre as estimativas e as contagens exatas entre os grandes espaços de trabalho.
{% endalert %}

### Razões para mudanças significativas

O número de associados pode mudar significativamente por vários motivos, como os apresentados nesta tabela.

| Motivo | Exemplo |
| --- | --- |
| Comportamento normal do usuário | Os usuários se inscrevem após uma campanha particularmente bem-sucedida. |
| A importação de usuários é feita por CSV | Foi importado um arquivo CSV de usuários que aumentou significativamente o número de membros do segmento. |
| Os critérios de público do segmento são modificados | As regras de público de um segmento existente (como filtros) foram alteradas, causando mudanças significativas na associação do segmento. |
| Os usuários são excluídos | Um número significativo de usuários foi excluído. |
| Uma integração com parceiros sincronizada com o Braze | Um terceiro enviou dados para a Braze que influenciaram significativamente a associação ao segmento. |
| Os usuários inativos são arquivados | Um número significativo de perfis inativos foi arquivado. Por exemplo, um grande número de usuários importados de CSV nunca registra atividades e é arquivado ao mesmo tempo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

[1]: {% image_buster /assets/img_archive/historical_membership2.png %}
[2]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[3]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}