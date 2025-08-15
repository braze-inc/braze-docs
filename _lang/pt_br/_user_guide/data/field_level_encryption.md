---
nav_title: Criptografia do campo de identificador
article_title: Criptografia do campo de identificador
page_order: 101
alias: "/field_level_encryption/"
description: "Este artigo de referência aborda como criptografar endereços de e-mail para minimizar as informações de identificação pessoal (IPI) compartilhadas no Braze."
page_type: reference
---

# Criptografia em nível de campo do identificador

> Usando a criptografia em nível de campo do identificador, é possível criptografar perfeitamente os endereços de e-mail com o AWS Key Management Service (KMS) para minimizar as informações de identificação pessoal (IPI) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.

{% alert important %}
A criptografia em nível de campo do identificador está disponível como um recurso complementar. Para começar a usar a criptografia no nível do campo do identificador, entre em contato com o gerente da sua conta Braze.
{% endalert %}

## Como funciona?

Os endereços de e-mail devem ser criptografados e transformados em hash antes de serem adicionados ao Braze. Quando uma mensagem for enviada, será feita uma chamada para o AWS KMS para obter o endereço de e-mail descriptografado. Em seguida, o endereço de e-mail com hash será inserido nos metadados para que os eventos de entrega e engajamento sejam vinculados ao usuário original. É assim que o Braze pode rastrear a análise de dados de e-mail. O Braze redigirá todos os endereços de e-mail em texto simples que forem incluídos e não armazenará o endereço de e-mail em texto simples do usuário.

## Pré-requisitos

Para usar a criptografia em nível de campo, você deve ter acesso ao AWS KMS para [criptografar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) e [fazer hash](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) dos endereços de e-mail **antes** de enviá-los à Braze. 

Siga estas etapas para configurar seu método de autenticação de chave secreta da AWS.

1. Para recuperar o ID da chave de acesso e a chave de acesso secreta, [crie um usuário IAM e um grupo de administradores](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) na AWS com uma política de permissões para o AWS Key Management Service. O usuário do IAM deve ter as permissões [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) e [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Para saber mais, consulte [Permissões do AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Selecione **Show User Security Credentials (Mostrar credenciais de segurança do usuário** ) para revelar o ID da chave de acesso e a chave de acesso secreta. Anote essas credenciais em algum lugar ou selecione o botão **Baixar credenciais**, pois você precisará inseri-las ao conectar suas chaves do AWS KMS.
3. Você deve configurar o KMS nas seguintes regiões da AWS:
    - **Clusters Braze nos EUA:** `us-east-1`
    - **Clusters Braze na UE:** `eu-central-1`
4. No AWS Key Management Service, crie duas chaves e certifique-se de que o usuário IAM seja adicionado às permissões de uso da chave:
    - **[Criptografar/descriptografar](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Selecione o tipo de chave **Simétrica** e o uso de chave **Criptografar e descriptografar**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Selecione o tipo de chave **Simétrica** e o uso de chave **Gerar e verificar MAC**. A especificação da chave deve ser **HMAC_256**. Depois de criar a chave, anote o ID da chave HMAC em algum lugar, pois você precisará inseri-lo na Braze.

![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Etapa 1: Conecte suas chaves AWS KMS

No dashboard do Braze, acesse **Data Settings** > **Field-Level Encryption** Para suas configurações do AWS KMS, digite o seguinte:

- Acessar ID da chave
- Chave de acesso de segredo
- ID da chave HMAC (não pode ser atualizada após o salvamento)

## Etapa 2: Selecione seus campos criptografados

Em seguida, selecione **Endereço de e-mail** para criptografar o campo. 

Quando a criptografia é ativada para um campo, ele não pode ser revertido para um campo descriptografado. Isso significa que a criptografia é uma configuração permanente. Ao configurar a criptografia para o endereço de e-mail, confirme se nenhum usuário tem endereços de e-mail no espaço de trabalho. Isso garante que nenhum endereço de e-mail em texto simples seja armazenado no Braze ao ativar o recurso para o espaço de trabalho.

![]({% image_buster /assets/img/field_level_encryption.png %})

## Etapa 3: Importação e atualização de usuários

Quando a criptografia em nível de campo do identificador estiver ativada, você deverá fazer hash e criptografar o endereço de e-mail antes de adicioná-lo ao Braze. Certifique-se de colocar o endereço de e-mail em letras minúsculas antes de fazer o envio de e-mail. Consulte o [objeto de atribuições do usuário](#user-attributes-object) para obter mais detalhes.

Ao atualizar o endereço de e-mail no Braze, você deve usar o valor de e-mail com hash sempre que `email` estiver incluído. Isso inclui:

- Endpoints REST:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Adição ou atualização de usuários via CSV

{% alert note %}
Ao criar um novo usuário com um endereço de e-mail, é necessário adicionar `email_encrypted` com o valor de e-mail criptografado do usuário. Caso contrário, o usuário não será criado. Da mesma forma, se estiver adicionando um endereço de e-mail a um usuário existente que não tenha um e-mail, será necessário adicionar `email_encrypted`. Caso contrário, o usuário não será atualizado.
{% endalert %}

## Considerações

Esses recursos não são compatíveis com a criptografia em nível de campo do identificador:

- Identificação e captura de endereço de e-mail via SDK
- Formulários de captura de mensagens no app
- Relatórios sobre o domínio do destinatário, incluindo gráficos do provedor de caixa de e-mail de Insights de e-mail
- Filtro de endereços de e-mail por expressão regular
- Sincronização com o público
- Integração com o Shopify

### Objeto de atribuições do usuário

Ao usar a criptografia no nível do campo do identificador com o ponto de extremidade `/users/track`, note esses detalhes de campo para o [objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- O campo `email` deve ser o valor com hash do e-mail.
- O campo `email_encrypted` deve ser o valor criptografado do e-mail.

## Perguntas frequentes

### Qual é a diferença entre criptografia e hashing?

A criptografia é uma função bidirecional em que é possível criptografar e descriptografar dados. Se o mesmo valor de texto simples for criptografado várias vezes, o algoritmo de criptografia da AWS (AES-256-GCM) produzirá valores criptografados diferentes. O hashing é uma função unidirecional em que o texto simples é embaralhado de uma forma que não pode ser descriptografada. O hashing produz o mesmo valor todas as vezes. Isso nos permite manter estados de inscrição em vários usuários que compartilham o mesmo endereço de e-mail.

### Que endereço de e-mail devo usar em meu envio de teste?

Os endereços de e-mail em texto simples são suportados no envio de testes. Para ver a aparência de um e-mail para um usuário específico, faça o seguinte:

1. Selecione **Pré-visualizar mensagem como um usuário**.
2. Em **Test Send (Envio de teste**), selecione **Override recipients attributes (Substituir atribuições dos destinatários) com as atribuições do usuário da prévia atual**.

{%raw%}
### O que acontecerá se eu adicionar esse endereço de e-mail Liquid `{{${email_address}}}` no Braze?

O Braze renderizará o endereço de e-mail em texto simples ao enviar o e-mail. Nas prévias, exibiremos a versão criptografada do e-mail. Recomendamos usar o ID externo do usuário se estiver fazendo referência a um usuário em um URL personalizado de um clique.

`{{${email_address}}}` não é suportado atualmente no centro de preferências e nas páginas de cancelamento de inscrição.
{%endraw%}

### Que endereço de e-mail devo esperar ver no Currents?

O endereço de e-mail com hash é incluído nos eventos de envio e engajamento de e-mail.

### Que endereço de e-mail devo esperar ver no arquivamento de mensagens?

O endereço de e-mail em texto simples é incluído no arquivamento de mensagens. Eles são enviados diretamente ao provedor de armazenamento em nuvem do cliente e pode haver outros dados pessoais incluídos nos corpos dos e-mails.

### Posso usar mail-to list-unsubscribe para gerenciamento de inscrições com criptografia em nível de campo do identificador?

Não. O uso de mail-to list-unsubscribe enviaria o endereço de e-mail descriptografado em texto simples para o Braze. Com a criptografia em nível de campo do identificador ativada, oferecemos suporte ao método HTTP: baseado em URL, incluindo um clique. Também recomendamos incluir um link de cancelamento de inscrição com um clique no corpo do e-mail.

### A criptografia em nível de campo do identificador é compatível com outros identificadores, como o telefone?

Não. Atualmente, a criptografia em nível de campo do identificador é compatível apenas com endereços de e-mail.
