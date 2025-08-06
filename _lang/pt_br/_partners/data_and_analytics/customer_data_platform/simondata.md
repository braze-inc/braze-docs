---
nav_title: Dados do Simon
article_title: Dados do Simon
description: "Use a integração entre o Braze e o Simon Data para criar e sincronizar públicos sofisticados com o Braze para orquestração, em tempo real e sem código."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Dados do Simon

> [A Simon Data](https://www.simondata.com) é uma plataforma de dados do cliente (CDP) amigável aos profissionais de marketing e confiável para as equipes de dados. Ao transformar seu data warehouse em uma potência de marketing, a Simon gera resultados de negócios e uma experiência superior para o cliente.

Use a integração entre o Braze e o Simon Data para criar e sincronizar públicos sofisticados com o Braze para orquestração, em tempo real e sem código. Com essa integração, você pode aproveitar o melhor dos recursos de priorização de campanhas e de correspondência de identidade do Simon, o suporte de agregados complexos e muito mais para elevar suas campanhas no Braze.

## Pré-requisitos

Para começar, você precisa autenticar sua conta Braze na sua conta Simon Data.

| Requisito         | Descrição                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dados do Simon          | Você deve ter uma conta existente na Simon Data para aproveitar a integração da Braze a partir da Simon Data.                                                                    |
| Chave da API REST do Braze  | Uma chave da API REST da Braze com as permissões `users.track`, `campaigns.trigger.schedule.create` e `campaigns.trigger.send`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| URL do dashboard do Braze | [Seu URL do ponto de extremidade REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Seu endpoint dependerá do URL do Braze para sua instância.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

- Disparar um Braze Canvas ou e-mail  
- Passar e manter as propriedades do segmento
- Sincronizar características e propriedades de contato

{% alert note %}  
Ao usar a integração entre o Simon e o Braze, o Simon só envia deltas em cada sincronização para o Braze, evitando custos com dados irrelevantes. Consulte [Características de sincronização e Propriedades de contato](#sync-traits-and-contact-properties) para obter mais informações.
{% endalert %}

## Integração

### Autenticar sua conta Braze no Simon

Para usar a integração da Braze, primeiro autentique sua conta Braze na Simon:

1. Na navegação à esquerda, clique em **Integrações** e role até Braze.
2. Insira sua [chave da API REST]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys) do Braze e o [URL do dashboard]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints).
3. Clique em **Salvar alterações**.

Uma conexão bem-sucedida exibe **Connected (Conectado** ) na janela.

![Tela de integração no Simon Data]({% image_buster /assets/img/simon_data/ConnecttoBraze.png %}){: style="max-width:70%"}

### Adicionar ações do Braze a fluxos ou jornadas no Simon

Depois de autenticar sua conta Braze na Simon, você poderá adicionar ações da Braze a [fluxos](https://docs.simondata.com/docs/campaigns-flows) e [jornadas](https://docs.simondata.com/docs/campaigns-journeys-two).

Há três ações disponíveis:

- **Sincronizar atributo do segmento com a Simon**: Sincronize os detalhes de seu segmento com um atributo personalizado novo ou existente no Braze.
- **Disparar um Braze Canvas**: dispare um Braze Canvas que aproveite os dados de seu segmento Simon.
- **Enviar uma campanha da Braze**: abra uma campanha completa da Braze diretamente na Simon.

![Menu suspenso mostrando a lista de ações Braze disponíveis no Simon Data.]({% image_buster /assets/img/simon_data/BrazeActions.png %}){: style="max-width:60%"}

Algumas ações só estão disponíveis para tipos de fluxo específicos ou apenas para viagens. Saiba mais em [docs.simondata.com](https://docs.simondata.com).

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

![Seleção de características de sincronização em Simon Data.]({% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %})





