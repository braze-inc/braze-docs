---
nav_title: Visão geral
article_title: Visão Geral da Transformação de Dados do Braze
page_order: 0
page_type: reference
alias: /data_transformation/
description: "Este artigo de referência fornece uma visão geral da Transformação de Dados da Braze, perguntas frequentes e limitações do produto."
---

# Visão geral da transformação de dados do Braze

> A Transformação de Dados do Braze permite que você crie e gerencie integrações de webhook para automatizar o fluxo de dados de plataformas externas para o Braze. Esses dados de usuários recém-integrados podem então impulsionar casos de uso de marketing ainda mais sofisticados. A Braze Data Transformation pode agilizar sua integração de dados, mesmo que você tenha pouca experiência em codificação, e pode ajudar a substituir a dependência da sua equipe de chamadas manuais de API, ferramentas de integração de terceiros ou até mesmo plataformas de dados do cliente.

## Como funciona?

Muitas plataformas modernas têm “webhooks”, ou notificações de API em tempo real, para enviar informações sobre um novo evento ou novos dados de uma plataforma para outra. Transformação de Dados fornece:

* Um endereço URL da Braze para receber esses webhooks.
* Funcionalidades para transformar a carga útil do webhook com código JavaScript para criar solicitações válidas para vários endpoints da API Braze, incluindo Braze `/users/track` ou `/catalogs`. Por exemplo, para o `/users/track` destino, você pode escolher quais informações usar do webhook e como deseja que os dados sejam representados nos perfis de usuário do Braze como atributos de usuário, eventos ou compras.
* Registro para realizar garantia de qualidade, solucionar problemas e monitorar a performance de suas transformações.

O resultado final é uma integração de webhook que conecta uma plataforma de origem de sua escolha, transformando seus webhooks em atualizações do Braze.

{% details Mais sobre webhooks %}
Webhooks são notificações em tempo real enviadas via uma solicitação HTTP POST para um destino específico. Webhooks são frequentemente usados para enviar dados de um ponto a outro, nos quais o webhook pode transmitir dados sobre uma ação que ocorreu e quem esteve envolvido nessa ação.

Por exemplo, uma plataforma de pesquisa pode enviar um webhook para um destino de sua escolha sempre que uma resposta a um formulário online for recebida. Ou, uma plataforma de atendimento ao cliente pode enviar um webhook para um destino de sua escolha sempre que um tíquete de atendimento ao cliente for criado.
{% enddetails %}

## Camadas de Transformação de Dados

A tabela a seguir descreve as diferenças entre a versão gratuita e a versão profissional do Data Transformation.

| Área | Versão Gratuita | Data Transformation Pro |
|----|----|----|
| Transformações ativas | Até 5 por empresa | Até 55 por empresa |
| Por mês | 300.000 solicitações recebidas por mês | 10.300.000 solicitações recebidas por mês |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para solicitar um fazer upgrade para Data Transformation Pro, entre em contato com o seu gerente de conta da Braze ou selecione o botão **Request Upgrade** no dashboard da Braze.
{% endalert %}

### Limites de taxa

O limite de frequência para as transformações de dados do Braze é de 1.000 solicitações de entrada por minuto por espaço de trabalho. Se você tem o Data Transformation Pro e precisa de um limite de frequência maior, entre em contato com o seu gerente de conta da Braze.

## Perguntas frequentes

### O que é sincronizado com a Transformação de Dados do Braze?

Quaisquer dados que a plataforma externa disponibilize em um webhook podem ser sincronizados com a Braze. Quanto mais uma plataforma externa envia via webhooks, mais opções para escolher o que é sincronizado.

### Sou um profissional de marketing. Preciso de recursos de desenvolvedor para usar o Braze Data Transformation?

Embora adoraríamos que os desenvolvedores usassem esse recurso também, você não precisa ser um para usá-lo! Os profissionais de marketing também podem configurar transformações com sucesso sem recursos de desenvolvedores.

### Ainda posso usar a Braze Data Transformation se minha plataforma externa fornecer apenas um endereço de e-mail ou número de telefone como identificador?

Sim. Você pode ter suas transformações atualizando o `/users/track` endpoint com o [e-mail ou número de telefone como um identificador]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address).

Isso funciona usando `email` ou `phone` como sua propriedade identificadora no código de transformação em vez de `external_id` ou `braze_id`. O exemplo [código de transformação]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) usa esta funcionalidade.

{% alert note %}
Os usuários de acesso antecipado do Braze Data Transformation que começaram antes de abril de 2023 podem estar familiarizados com uma função `get_user_by_email` que ajudou com este caso de uso. Essa função foi descontinuada.
{% endalert %}

### A transformação de dados do Braze consome pontos de dados?

Na maioria dos casos, sim. O Braze Data Transformation eventualmente cria uma `/users/track` chamada que grava os atributos, eventos e compras que você deseja. Eles consumirão pontos de dados da mesma forma como se a `/users/track` chamada fosse feita independentemente. Você tem controle sobre quantos pontos de dados serão escritos com base em como você escreve sua transformação.

### Como posso obter ajuda para configurar meu caso de uso ou com meu código de transformação?

Entre em contato com o gerente de conta da Braze para obter assistência adicional.


