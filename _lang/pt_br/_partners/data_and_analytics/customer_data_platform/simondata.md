---
nav_title: SimonIA
article_title: SimonIA
description: "Use a integração Braze e SimonIA para criar e sincronizar audiências sofisticadas no Braze para orquestração, em tempo real e sem código."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon IA

> A [Simon IA][1] Plataforma de Marketing Agente ajuda equipes de marketing a alcançar verdadeira personalização um-a-um. Ela combina um CDP componível com agentes de IA que operam diretamente na Nuvem de Dados AI do Snowflake para atuar como a equipe de dados e execução de um profissional de marketing.

Use a integração Braze e Simon IA para construir e sincronizar audiências avançadas no Braze para orquestração em tempo real, sem código. Com esta integração, você pode aproveitar a resolução de identidade do Simon IA, a unificação de dados de clientes e a segmentação impulsionada por IA para potencializar campanhas Braze mais personalizadas e impactantes a montante.

## Pré-requisitos

Para começar, você precisa autenticar sua conta Braze dentro da sua conta Simon IA.

| Requisito         | Descrição                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon IA          | Você deve ter uma conta Simon IA existente para aproveitar a integração Braze a partir do Simon IA.                                                                    |
| Chave da API REST do Braze  | Uma chave da API REST da Braze com as permissões `users.track`, `campaigns.trigger.schedule.create` e `campaigns.trigger.send`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| URL do dashboard do Braze | [Seu URL do ponto de extremidade REST][3]. Seu endpoint dependerá do URL do Braze para sua instância.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

- Disparar um Braze Canvas ou e-mail  
- Passar e manter as propriedades do segmento
- Sincronizar características e propriedades de contato

{% alert note %}  
Ao usar a integração entre o Simon e o Braze, o Simon só envia deltas em cada sincronização para o Braze, evitando custos com dados irrelevantes. Consulte [Características de sincronização e Propriedades de contato](#sync-traits-and-contact-properties) para obter mais informações.
{% endalert %}

## Integração

### Autentique sua conta Braze no Simon IA

Para usar a integração da Braze, primeiro autentique sua conta Braze na Simon:

1. Na navegação à esquerda, clique em **Integrações** e role até Braze.
2. Insira sua [chave da API REST][2] do Braze e o [URL do dashboard][3].
3. Clique em **Salvar alterações**.

Uma conexão bem-sucedida exibe **Connected (Conectado** ) na janela.

![Tela de integração no Simon IA][8]{: style="max-width:70%"}

### Adicione ações Braze a Fluxos ou Jornadas no Simon IA

Depois de autenticar sua conta Braze no Simon IA, você pode adicionar ações Braze a [Fluxos][4] e [Jornadas][5].

Há três ações disponíveis:

- **Sincronizar atributo do segmento com a Simon**: Sincronize os detalhes de seu segmento com um atributo personalizado novo ou existente no Braze.
- **Disparar um Braze Canvas**: dispare um Braze Canvas que aproveite os dados de seu segmento Simon.
- **Enviar uma campanha da Braze**: abra uma campanha completa da Braze diretamente na Simon.

![Dropdown mostrando lista de ações Braze disponíveis no Simon IA.][9]{: style="max-width:60%"}

Algumas ações só estão disponíveis para tipos de fluxo específicos ou apenas para viagens. Saiba mais em [docs.simondata.com][6].

### Sincronizar características e propriedades de contato

Para minimizar o consumo de dados, você pode escolher características específicas para sincronizar por padrão, em vez de atualizar todos os campos de todos os clientes em um segmento.

{% alert note %}
Para começar a sincronização de características, envie uma solicitação no [Centro de Suporte do Simon](https://docs.simondata.com/docs/support-center). Seu gerente de conta informará quando você poderá prosseguir com as etapas seguintes.
{% endalert %}

Depois que as características de contato forem ativadas pelo gerente da sua conta:

1. Na Simon, expanda a **Admin Center** (Central de administração) na navegação à esquerda e selecione **Sync Contact Traits** (Sincronizar características de contatos).
2. Escolha **Braze**. As propriedades de contato são exibidas aqui, aninhadas por conjunto de dados.
3. Selecione os campos que você deseja sincronizar ao usar a integração entre Simon e Braze:
   1. **O número ou as características** indicam quantas características estão disponíveis para escolha nesse conjunto de dados. Você pode selecionar todos ou expandir a linha para selecionar campos individuais.
   2. Edite o **nome Downstream** se quiser que os nomes dos campos apareçam de forma diferente quando chegarem ao Braze.
   3. Se esta for a primeira vez que faz a integração com o Braze a partir do Simon, clique em **Backfill all contacts (Preencher todos os contatos**). O backfilling envia todos os pontos de dados para o Braze na primeira vez que você usa uma ação em um fluxo ou jornada para garantir que todos os seus dados estejam totalmente sincronizados. Em seguida, nas sincronizações subsequentes, somente as características que você escolher nessa tela serão enviadas ao Braze. Isso ajuda a garantir que você seja cobrado apenas pelos dados de que precisa.

![Selecionando traços de sincronização no Simon IA.][10]

[1]: https://www.simondata.com




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}

