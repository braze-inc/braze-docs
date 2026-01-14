---
nav_title: MetaRouter
article_title: MetaRouter
description: "Melhore a gestão de seus dados de cliente na Braze com a MetaRouter. Essa solução de gerenciamento de tags no lado do servidor e de alta performance oferece o máximo de conformidade e controle com opções de implementação perfeitas, seja em uma nuvem privada hospedada pelo MetaRouter ou em sua própria infraestrutura."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [O MetaRouter](https://www.metarouter.io/) eleva sua experiência no Braze ao se integrar perfeitamente como uma poderosa plataforma de gerenciamento de tags no lado do servidor. Ela permite que você orquestre uma jornada completa de dados de clientes na Braze, desde a coleta confiável de dados totalmente primários, enriquecida em até 30%, até a ativação do fluxo de dados em tempo real para jornadas personalizadas. Além disso, a MetaRouter agiliza a implementação, eliminando a necessidade de tags da Braze ou de outras tags de terceiros. Dessa forma, você tem controle granular, parâmetro por parâmetro, dos dados transferidos para a Braze.

_Essa integração é mantida pelo Metarouter._

## Recursos suportados

- As novas tentativas podem ser incorporadas.
- As solicitações são agrupadas.
- Os problemas de limite de frequência são tratados com uma nova tentativa.
- Há suporte para ID externa e IPI. A MetaRouter passa o ID anônimo e qualquer IPI (e-mail, número de telefone, nome) que os clientes desejarem.
- Você pode enviar compras no Braze e dados de eventos personalizados.
  - Há suporte para propriedades de eventos.
  - Não há suporte para propriedades de eventos aninhadas.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Requisito           | Descrição                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta do MetaRouter  | Uma [conta do MetaRouter Enterprise](https://enterprise.metarouter.io/).                                                                                |
| Chave da API REST do Braze    | Uma chave da API REST da Braze com `users.track` permissões. Para criar uma, acesse **Settings** > **API Keys** (Configurações > Chaves de API).                                                |
| Um endpoint Braze REST | [Seu URL do ponto de extremidade REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Configuração do MetaRouter

Para configurar o MetaRouter para sua integração com o Braze:

1. Acesse o MetaRouter e crie um novo cluster.
2. Escolha os eventos que deseja rastrear.
3. Instale um SDK da MetaRouter e integre os eventos ao seu site.
4. Conecte seu cluster à interface do usuário do seu site.
5. Crie um novo pipeline.
6. Verifique se o seu site está enviando eventos para o MetaRouter.

## Integração do Braze

### Etapa 1: Adicionar a integração do Braze

No Enterprise MetaRouter, selecione **Integrações** > **Nova integração** > **Braze** e, em seguida, nomeie sua integração. Em seguida, insira o URL da instância e a chave de API e selecione **Apply Changes** (Aplicar alterações).

![Adição do Braze como uma integração no MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Etapa 2: Adicionar mapeamento de eventos

Adicione o mapeamento de eventos para cada saída de identidade e, em seguida, configure os eventos que deseja enviar ao Braze. Quando terminar, selecione **Salvar como nova revisão**.

![Adicione o mapeamento de eventos para cada uma das saídas de identidade.]({% image_buster /assets/img/metarouter/img2.png %})

