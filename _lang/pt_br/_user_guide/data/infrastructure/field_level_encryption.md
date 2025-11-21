---
nav_title: Criptografia em nível de campo do identificador
article_title: Criptografia em nível de campo do identificador
page_order: 2
alias: "/field_level_encryption/"
description: "Este artigo de referência aborda como criptografar endereços de e-mail para minimizar as informações de identificação pessoal (PII) compartilhadas no Braze."
page_type: reference
---

# Criptografia em nível de campo do identificador

> Usando a criptografia em nível de campo do identificador, você pode criptografar perfeitamente os endereços de e-mail com o AWS Key Management Service (KMS) para minimizar as informações de identificação pessoal (PII) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.

{% alert important %}
A criptografia em nível de campo do identificador está disponível como um recurso complementar. Para começar a usar a criptografia no nível do campo do identificador, entre em contato com o gerente da sua conta Braze.
{% endalert %}

## Como funciona

Os endereços de e-mail devem ser criptografados e com hash antes de serem adicionados ao Braze. Quando uma mensagem for enviada, será feita uma chamada para o AWS KMS para obter o endereço de e-mail descriptografado. Em seguida, o endereço de e-mail com hash será inserido nos metadados para que os eventos de entrega e engajamento sejam vinculados ao usuário original. É assim que o Braze pode rastrear a análise de e-mail. O Braze redigirá todos os endereços de e-mail em texto simples que forem incluídos e não armazenará o endereço de e-mail em texto simples do usuário.

## Pré-requisitos

Para usar a criptografia em nível de campo do identificador, você deve ter acesso ao AWS KMS para [criptografar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) e fazer [hash](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) dos endereços de e-mail **antes de** enviá-los ao Braze. 

Siga estas etapas para configurar seu método de autenticação de chave secreta do AWS.

1. Para recuperar o ID da chave de acesso e a chave de acesso secreta, [crie um usuário IAM e um grupo de administradores](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) no AWS com uma política de permissões para o AWS Key Management Service. O usuário do IAM deve ter as permissões [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) e [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Para obter mais detalhes, consulte [Permissões do AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Selecione **Show User Security Credentials (Mostrar credenciais de segurança do usuário** ) para revelar o ID da chave de acesso e a chave de acesso secreta. Anote essas credenciais em algum lugar ou selecione o botão **Download Credentials (Baixar credenciais** ), pois você precisará inseri-las ao conectar suas chaves do AWS KMS.
3. Você deve configurar o KMS nas seguintes regiões do AWS:
    - **Clusters Braze US:** `us-east-1`
    - **Brasagem de clusters da UE:** `eu-central-1`
4. No AWS Key Management Service, crie duas chaves e certifique-se de que o usuário IAM seja adicionado às permissões de uso da chave:
    - **[Criptografar/descriptografar](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Selecione **Symmetric** key type (tipo de chave **simétrica** ) e **Encrypt and Decrypt** key usage (uso de chave de criptografia **e descriptografia** ).
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Selecione **Symmetric** key type (Tipo de chave **simétrica** ) e **Generate and Verify MAC** key usage ( **Gerar e verificar** o uso da chave **MAC** ). A especificação principal deve ser **HMAC_256**. Depois de criar a chave, anote o ID da chave HMAC em algum lugar, pois você precisará inseri-lo no Braze.

\![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Etapa 1: Conecte suas chaves do AWS KMS

No painel do Braze, vá para **Data Settings (Configurações de dados** ) > **Field-Level Encryption (Criptografia em nível de campo**). Nas configurações do AWS KMS, digite o seguinte:

- ID da chave de acesso
- Chave de acesso secreta
- ID da chave HMAC (não pode ser atualizada após o salvamento)

## Etapa 2: Selecione seus campos criptografados

Em seguida, selecione **Email address (Endereço de e-mail** ) para criptografar o campo. 

Quando a criptografia é ativada para um campo, ele não pode ser revertido para um campo descriptografado. Isso significa que a criptografia é uma configuração permanente. Ao configurar a criptografia para o endereço de e-mail, confirme se nenhum usuário tem endereços de e-mail no espaço de trabalho. Isso garante que nenhum endereço de e-mail em texto simples seja armazenado no Braze ao ativar o recurso para o espaço de trabalho.

\![]({% image_buster /assets/img/field_level_encryption.png %})

## Etapa 3: Importar e atualizar usuários

Quando a criptografia em nível de campo do identificador estiver ativada, você deverá fazer hash e criptografar o endereço de e-mail antes de adicioná-lo ao Braze. Certifique-se de colocar o endereço de e-mail em letras minúsculas antes de fazer o hash. Consulte o [objeto de atributos do usuário](#user-attributes-object) para obter mais detalhes.

Ao atualizar o endereço de e-mail no Braze, você deve usar o valor de e-mail com hash sempre que `email` estiver incluído. Isso inclui:

- Pontos de extremidade REST:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Adição ou atualização de usuários via CSV

{% alert note %}
Ao criar um novo usuário com um endereço de e-mail, é necessário adicionar `email_encrypted` com o valor de e-mail criptografado do usuário. Caso contrário, o usuário não será criado. Da mesma forma, se você estiver adicionando um endereço de e-mail a um usuário existente que não tenha um e-mail, deverá adicionar `email_encrypted`. Caso contrário, o usuário não será atualizado.
{% endalert %}

## Considerações

Esses recursos não são compatíveis com a criptografia em nível de campo do identificador:

- Identificação e captura de endereço de e-mail via SDK
- Formulários de captura de mensagens de e-mail no aplicativo
- Relatórios sobre o domínio do destinatário, incluindo gráficos do provedor de caixa de correio do Email Insights
- Filtro de endereço de e-mail por expressão regular
- Sincronização com o público
- Integração com o Shopify

### Objeto de atributos do usuário

Ao usar a criptografia no nível do campo do identificador com o ponto de extremidade `/users/track`, observe esses detalhes de campo para o [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- O campo `email` deve ser o valor com hash do e-mail.
- O campo `email_encrypted` deve ser o valor criptografado do e-mail.

## Perguntas frequentes

### Qual é a diferença entre criptografia e hashing?

A criptografia é uma função bidirecional em que é possível criptografar e descriptografar dados. Se o mesmo valor de texto simples for criptografado várias vezes, o algoritmo de criptografia da AWS (AES-256-GCM) produzirá valores criptografados diferentes. O hashing é uma função unidirecional em que o texto simples é embaralhado de uma forma que não pode ser descriptografada. O hashing produz o mesmo valor todas as vezes. Isso nos permite oferecer suporte à manutenção de estados de assinatura entre vários usuários que compartilham o mesmo endereço de e-mail.

### Qual endereço de e-mail devo usar em meu envio de teste?

Os endereços de e-mail em texto simples são compatíveis com o envio de testes. Para ver a aparência de um e-mail para um usuário específico, faça o seguinte:

1. Selecione **Preview message as a user (Visualizar mensagem como um usuário**).
2. Em **Test Send (Envio de teste**), selecione **Override recipients attributes (Substituir atributos dos destinatários) com os atributos do usuário de visualização atual**.

{%raw%}
### O que acontecerá se eu adicionar esse endereço de e-mail Liquid `{{${email_address}}}` no Braze?

O Braze renderizará o endereço de e-mail em texto simples ao enviar o e-mail. Nas visualizações, exibiremos a versão criptografada do e-mail. Recomendamos usar o ID externo do usuário se estiver fazendo referência a um usuário em um URL personalizado de um clique.

`{{${email_address}}}` não é suportado atualmente no centro de preferências e nas páginas de cancelamento de assinatura.
{%endraw%}

### Que endereço de e-mail devo esperar ver no Currents?

O endereço de e-mail com hash é incluído nos eventos de entrega de e-mail e engajamento.

### Que endereço de e-mail devo esperar ver no arquivamento de mensagens?

O endereço de e-mail em texto simples é incluído no arquivamento de mensagens. Eles são enviados diretamente ao provedor de armazenamento em nuvem do cliente e pode haver outros dados pessoais incluídos nos corpos dos e-mails.

### Posso usar mail-to list-unsubscribe para gerenciamento de assinaturas com criptografia em nível de campo do identificador?

Não. O uso de mail-to list-unsubscribe enviaria o endereço de e-mail descriptografado em texto simples para o Braze. Com a criptografia em nível de campo do identificador ativada, oferecemos suporte ao método HTTP: baseado em URL, incluindo um clique. Também recomendamos incluir um link de cancelamento de assinatura com um clique no corpo do e-mail.

### A criptografia em nível de campo do identificador é compatível com outros identificadores, como o telefone?

Não. Atualmente, a criptografia em nível de campo do identificador é compatível apenas com endereços de e-mail.
