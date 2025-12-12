---
nav_title: Diferença entre lista de bloqueios e exclusão
article_title: Diferença entre lista de bloqueios e exclusão
page_order: 2

page_type: solution
description: "Este artigo de ajuda orienta sobre a diferença entre a lista de bloqueio de atribuições e a exclusão."
---

# Diferença entre lista de bloqueio e exclusão

Para entender a diferença entre colocar na lista de bloqueio e excluir atribuições no Braze, vamos analisar os resultados de cada ação:

- **Lista de bloqueio:** Se atributos personalizados, eventos ou compras estiverem na lista de bloqueio, eles permanecerão no perfil do usuário, mas nenhuma nova solicitação para o atributo será processada.
- **Exclusão:** Se atributos personalizados, eventos ou compras forem excluídos, os dados serão removidos. No entanto, a Braze ainda aceitará novas solicitações de entrada para esse atributo se ele ainda estiver sendo rastreado por meio do SDK ou tiver sido feito upload via API ou CSV.

## O que devo fazer?

Para realizar a lista de bloqueios, a Braze terá de enviar as informações de lista de bloqueios para o dispositivo de cada usuário, e essa será uma operação com uso intensivo de dados, o que, idealmente, tentamos evitar. Além disso, se a lista for muito grande (> 100 atribuições, eventos ou compras), seu app pode começar a ficar lento. 

Se não estiver mais planejando enviar atribuições para a Braze, a rota de exclusão seria a abordagem recomendada.

Independentemente de sua rota, os atributos personalizados, eventos e compras que deseja remover não aparecerão mais na página **Manage Workspace**, que os remove como filtros de segmento. Os dados de usuários permanecerão nos perfis. 