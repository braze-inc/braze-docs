---
nav_title: Domínios personalizados
article_title: Domínios personalizados
page_order: 0
description: "Esta página aborda como usar domínios personalizados com encurtamento de links para personalizar a aparência de seus URLs encurtados."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Domínios personalizados

> Esta página aborda como usar domínios personalizados com encurtamento de links para personalizar a aparência de seus URLs encurtados e apresentar uma imagem de marca consistente. 

{% alert note %}
Entre em contato com seu gerente de conta Braze se estiver interessado em começar a usar domínios personalizados.
{% endalert %}

## Requisitos de domínio

- Os domínios devem ser adquiridos, pertencentes e gerenciados por você.
- O domínio usado para esse recurso deve ser exclusivo (ou seja, diferente do domínio do seu site) e não pode ser usado para hospedar nenhum conteúdo da Web.
  - Você também pode usar subdomínios exclusivos, como `sms.braze.com`.
- Recomendamos escolher um domínio com o menor número possível de caracteres para minimizar o comprimento de seus URLs.

### Delegação de seu domínio personalizado

Quando você delega seu domínio à Braze, nós tratamos automaticamente da renovação do certificado para evitar um lapso no serviço. 

Para delegar seu domínio ao Braze, faça o seguinte: 

1. Apresente um domínio que atenda aos requisitos acima ao seu gerente de sucesso do cliente. A Braze verificará a configuração de DNS existente para o domínio e confirmará isso:

- Não existem registros de CAA OU
- **Existem** registros do CAA, mas há um registro para {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} ou {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

2. Crie quatro novos registros A, um para cada IP, e confirme que esses são os únicos registros A existentes para o host do link de domínio:
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

## Uso de domínios personalizados

Uma vez configurados, os domínios personalizados podem ser atribuídos a um ou vários grupos de inscrições de SMS. 

![Configurações de grupos de inscrições que permitem que você selecione um domínio de encurtamento de links.]({% image_buster /assets/img/custom_domain.png %})

As campanhas enviadas com o encurtamento de links ativado usarão o domínio atribuído associado ao seu grupo de inscrições de SMS.

![Pré-visualização do criador de mensagem SMS com um domínio de link encurtado que é diferente do domínio na caixa "Mensagem".]({% image_buster /assets/img/custom_domain2.png %})

## Perguntas frequentes

### Os domínios delegados podem ser compartilhados entre vários grupos de inscrições?

Sim. Um único domínio pode ser usado com vários grupos de inscrições. Para fazer isso, selecione o domínio para cada grupo de inscrições ao qual ele deve ser associado.

### Os domínios delegados podem ser compartilhados em vários espaços de trabalho?

Sim. Os domínios podem ser associados a grupos de inscrições em vários espaços de trabalho, desde que os espaços de trabalho estejam contidos na mesma empresa.