---
nav_title: Transformação de Dados
article_title: Transformação de Dados
page_order: 0.3
layout: dev_guide
guide_top_header: "Transformação de Dados"
guide_top_text: "A Transformação de Dados do Braze permite que você construa e gerencie integrações de webhook para automatizar o fluxo de dados de plataformas externas para o Braze. Esses dados de usuário recém-integrados podem então alimentar casos de uso de marketing ainda mais sofisticados. A Transformação de Dados do Braze pode acelerar sua integração de dados, mesmo que você tenha pouca experiência em codificação, e pode ajudar a substituir a dependência da sua equipe em chamadas de API manuais, ferramentas de integração de terceiros ou até mesmo plataformas de dados de clientes."
page_type: landing
description: "Esta página de destino é o lar de artigos sobre a Transformação de Dados do Braze, incluindo como criar uma transformação de dados e casos de uso."
alias: /data_transformation/

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Criando uma Transformação
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation/
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Casos de Uso
    link: /docs/user_guide/data/unification/data_transformation/use_cases/
    image: /assets/img/braze_icons/users-01.svg
---

## Como funciona

Muitas plataformas modernas têm "webhooks", ou notificações de API em tempo real, para enviar informações sobre um novo evento ou novos dados de uma plataforma para outra. A Transformação de Dados fornece:

* Um endereço URL do Braze para receber esses webhooks.
* Capacidades para transformar a carga útil do webhook com código JavaScript para criar solicitações válidas para vários endpoints da API do Braze, incluindo Braze `/users/track` ou `/catalogs`. Por exemplo, para o destino `/users/track`, você pode escolher quais informações usar do webhook e como deseja que os dados sejam representados nos perfis de usuário do Braze como atributos de usuário, eventos ou compras.
* Registro para realizar garantia de qualidade, solucionar problemas e monitorar o desempenho de suas transformações.

O resultado final é uma integração de webhook que conecta uma plataforma de origem de sua escolha, transformando seus webhooks em atualizações do Braze.

{% details More on webhooks %}
Webhooks são notificações em tempo real enviadas via uma solicitação HTTP POST para um destino específico. Webhooks são frequentemente usados para enviar dados de um ponto a outro, onde o webhook pode passar dados sobre uma ação que ocorreu e quem estava envolvido nessa ação.

Por exemplo, uma plataforma de pesquisa pode enviar um webhook para um destino de sua escolha sempre que uma resposta de pesquisa a um formulário online for recebida. Ou, uma plataforma de atendimento ao cliente pode enviar um webhook para um destino de sua escolha sempre que um ticket de atendimento ao cliente é criado.
{% enddetails %}

## Camadas de Transformação de Dados

A tabela a seguir descreve as diferenças entre a versão gratuita e a versão pro da Transformação de Dados.

| Área | Versão Gratuita | Transformação de Dados Pro |
|----|----|----|
| Transformações ativas | Até 5 por empresa | Até 55 por empresa |
| Por mês | 300.000 solicitações recebidas por mês | 10.300.000 solicitações recebidas por mês |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para solicitar um upgrade para a Transformação de Dados Pro, entre em contato com seu gerente de conta da Braze ou selecione o **Solicitar Upgrade** botão no painel da Braze.
{% endalert %}

### Limites de taxa

O limite de taxa para Transformações de Dados da Braze é de 1.000 solicitações recebidas por minuto por espaço de trabalho. Se você tiver a Transformação de Dados Pro e precisar de um limite de taxa maior, entre em contato com seu gerente de conta da Braze.

## Perguntas frequentes

### O que é sincronizado com a Transformação de Dados da Braze?

Qualquer dado que a plataforma externa disponibiliza em um webhook pode ser sincronizado com a Braze. Quanto mais uma plataforma externa envia via webhooks, mais opções para escolher o que será sincronizado.

### Sou um profissional de marketing. Preciso de recursos de desenvolvedor para usar a Transformação de Dados do Braze?

Embora adoraríamos que os desenvolvedores usassem esse recurso também, você não precisa ser um para usá-lo! Os profissionais de marketing também podem configurar transformações com sucesso sem recursos de desenvolvedor.

### Posso ainda usar a Transformação de Dados do Braze se minha plataforma externa só fornecer um endereço de e-mail ou número de telefone como identificador?

Sim. Você pode ter suas transformações atualizando o `/users/track` endpoint com o [endereço de e-mail ou número de telefone como identificador]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address).

Isso funciona usando `email` ou `phone` como sua propriedade de identificador no código de transformação em vez de `external_id` ou `braze_id`. O exemplo [código de transformação]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) usa essa funcionalidade.

{% alert note %}
Usuários de acesso antecipado da Transformação de Dados do Braze que começaram antes de abril de 2023 podem estar familiarizados com uma `get_user_by_email` função que ajudou com esse caso de uso. Essa função foi descontinuada.
{% endalert %}

### A Transformação de Dados do Braze registra pontos de dados?

Sim, na maioria dos casos. A Transformação de Dados do Braze eventualmente cria uma `/users/track` chamada que grava os atributos, eventos e compras que você deseja. Esses registrarão pontos de dados da mesma forma que se a `/users/track` chamada fosse feita de forma independente. Você tem controle sobre quantos pontos de dados são registrados com base em como você escreve sua transformação.

### Como posso obter ajuda para configurar meu caso de uso ou com meu código de transformação?

Entre em contato com seu gerente de conta do Braze para assistência adicional.
