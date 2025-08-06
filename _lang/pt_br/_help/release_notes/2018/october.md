---
nav_title: Outubro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão de outubro de 2018."
---
# Outubro de 2018

{% comment %}
  Adicione-os em um momento posterior...
  Alternância do grupo de controle de seleção inteligente
  A caixa Intelligent Selection agora tem uma caixa de seleção que permite [ativar ou desativar o uso de um grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group). Quando ativado, o grupo de controle será 20% do tamanho do público e mudará à medida que o recurso Intelligent Selection otimizar os tamanhos de público por variante.
  Assistente de configurações de entrada de canvas (Beta)
  A interface do usuário do Canva será simplificada para evitar a perda de tarefas e os erros resultantes. As configurações de canvas, especificamente, agora serão exibidas em um assistente, semelhante ao design do assistente de campanhas. No momento, isso não está refletido em nossa documentação, pois está sendo implementado gradualmente. Volte em breve para saber mais sobre isso!
  API do grupo de inscrições (oculto)
  O Braze disponibilizou uma nova chamada GET para ativar a solicitação com base em um ID ou endereço de e-mail externo. Em seguida, serão fornecidos todos os grupos de inscrições associados a esse usuário.
{% endcomment %}

## Calcular estatísticas exatas de público para campanhas

Agora você pode acessar o **Campaign Analytics** e calcular as estatísticas exatas de seu público. Clique em **Calculate Exact Stats (Calcular estatísticas exatas** ) no rodapé da seção **Target Audiences (Públicos-alvo** ), e as estatísticas exatas do público serão preenchidas. Você terá de salvar a campanha antes de calcular (as campanhas de rascunho serão salvas como rascunhos).

## Descontinuidade do Windows 8

A Braze não oferece mais suporte ao Windows 8 a partir de 10 de outubro de 2018.

## Centro de parcerias

Agora você pode encontrar uma lista de suas integrações na plataforma Braze em **Integrações**, juntamente com as chaves e instruções de integração.

## Cálculos de análise de dados de e-mail

O Braze agora está calculando todas as análises de e-mail usando os dados de eventos do nosso parceiro de envio de e-mail (ESP) para melhorar muito a precisão das nossas análises de e-mail. Essa solução utiliza o Postgres, uma solução de banco de dados de código aberto, para garantir a integridade dos dados.

{% alert important %}
Atualmente, as aberturas exclusivas e os cliques exclusivos ainda dependem dos dados agregados fornecidos por nossos parceiros de envio de e-mail. Há um trabalho em andamento para calcular essas estatísticas de exclusividade usando a mesma infraestrutura introduzida nesta versão.
{% endalert %}

## Controles do painel do criador

Os controles do criador de mensagens foram atualizados para incluir palavras associadas aos ícones, a fim de ativar uma melhor capacidade de uso e navegação.

## Azure para Currents

Os clientes do Braze que usam o Currents agora podem ver [o Azure]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents#microsoft-azure-blob-storage) como uma possível integração.

## Expansões do campo de entrada

Agora você pode expandir as caixas de entrada para linhas de assunto de e-mail e títulos de push.
