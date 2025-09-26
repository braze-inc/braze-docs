---
nav_title: Merkury
article_title: Merkury
description: "Este artigo de referência descreve a parceria entre o Braze e a Merkury, uma plataforma de identidade corporativa para seus apps, que permite que você aproveite o `MerkuryID` para aumentar as taxas de reconhecimento de visitantes do site para os clientes do Braze."
page_type: partner
search_tag: Partner

---

# Merkury

> A [Merkury](https://merkury.merkleinc.com/) é a plataforma de identidade corporativa da Merkle que ajuda as marcas a maximizar o engajamento, a experiência e a receita do consumidor com recursos de identidade primários sem cookies. O `MerkuryID` unifica os registros de clientes e prospects conhecidos e desconhecidos de uma marca, as visitas ao site/app e os dados do consumidor em um único ID de pessoa persistente.

_Essa integração é mantida pela Merkury._

## Sobre a integração

A integração entre Braze e Merkury permite que você aproveite o `MerkuryID` para aumentar as taxas de reconhecimento de visitantes do site para os clientes Braze. Ao reconhecer os visitantes que são assinantes de e-mail da marca, a Merkury atualiza o perfil da Braze para incluir o endereço de e-mail do assinante. Os recursos de reconhecimento aprimorados do `MerkuryID` melhoram as oportunidades de engajamento e personalização e aumentam imediatamente as quantidades de envio de e-mail de abandono de site e a receita associada. 

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta da Merkle | É necessário ter uma conta da Merkle para usar essa parceria. |
| ID do cliente da Merkle | Obtenha seu ID de cliente com um representante da Merkle. |
| Tag da Merkury | Coloque a tag da Merkury da Merkle no seu site. |
| Endpoint do Braze REST e do SDK | Seu URL do endpoint REST ou SDK. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Isso pode ser criado no **Dashboard da Braze > Console de desenvolvedor > Chave da API REST > Criar nova chave de API**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
As solicitações do conector de identidade da Merkury para a Braze operam dentro das especificações do limite de frequência da API da Braze. Entre em contato com a Braze ou com seu gerente de conta da Merkle se tiver alguma dúvida.<br><br>A Merkury enviará pelo menos uma solicitação ao final de uma sessão qualificada.
{% endalert %}

## Integração lado a lado de SDK

Usa a tag Merkury do lado do cliente da Merkle para capturar dispositivos Braze e os encaminha para o endpoint do conector de identidade Merkury para identificação.

### Etapa 1: configure a tag do SDK para Web da Braze

Você deve ter o [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) implantado em seu site para usar essa integração.

### Etapa 2: implante a tag da Merkury da Merkle

Implemente a tag da Merkury no seu site. Isso fará o conector de identidade da Merkury ficar disponível nele. Um guia detalhado com instruções será fornecido pelo seu gerente de conta da Merkle.

### Etapa 3: Criar atributos personalizados

Os campos a seguir serão preenchidos pelo conector de identidade Merkury e precisam ser criados no Braze como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes).

| Nome do atributo | Tipo de dados | Descrição |
| --- | --- | --- |
| `hmid` | String | ID da Merkury da Merkle |
| `confidence_score` | Número | Nível de confiança da identificação da Merkury (de 1 a 8; quanto menor, melhor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 4: Forneça à Merkle o universo de e-mail do usuário

A Merkle recomenda uma exportação de segmentação de seu universo de e-mails permitidos. Isso pode ser acompanhado por exportações diárias de usuários ativos permitidos.

Os campos a seguir são obrigatórios:

- `braze_id`
- `external_id`
- endereço de e-mail

Consulte seu representante Braze para obter mais informações.

