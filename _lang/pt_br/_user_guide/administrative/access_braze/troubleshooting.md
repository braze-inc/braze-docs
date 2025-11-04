---
nav_title: Solução de problemas
article_title: Solução de problemas de acesso ao Braze
page_order: 8
page_type: reference
description: "Este artigo o orienta na solução de problemas que você pode ter ao tentar acessar o Braze."

---

# Solução de problemas de acesso ao Braze

> Este artigo ajuda a solucionar problemas que você pode ter ao tentar acessar o Braze.

## Bloqueio da conta

Então você está bloqueado em sua conta Braze - não se preocupe! Podemos ajudá-lo a voltar a participar.	

Você pode saber que tipo de bloqueio está ocorrendo pela mensagem de erro recebida:	

- [Vejo um erro sobre minha senha.](#password-error)	
- [Não vejo nenhum erro, mas o Braze ainda não me deixa entrar.](#instance-error)	
- [Estou vendo um erro sobre a suspensão da conta.](#account-suspension)	

### Erro de senha

A segurança de sua conta é importante para nós, portanto, são necessárias senhas para fazer login em sua conta Braze.	
- Verifique se você está fazendo login na [instância]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) correta [do painel do Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Verifique com o administrador de sua conta ou com o gerente de conta Braze para ter certeza.	
- Sua senha pode ter expirado, portanto, será necessário [redefini-la]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	
- Se você usa um serviço de [logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), verifique com o administrador da conta se a configuração foi concluída corretamente.	
- Se sua empresa estiver em várias instâncias do Braze, você pode estar usando o e-mail incorreto para fazer login.  	

Em caso de dúvida, você sempre pode [redefinir sua senha]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Erro de instância

Se você estiver usando a mesma máquina que costuma usar para fazer login, o Braze deverá detectar automaticamente a instância correta. No entanto, se isso não acontecer ou se você estiver fazendo login pela primeira vez, recomendamos que considere o seguinte:	

- Verifique se você está fazendo login na [instância]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) correta [do painel do Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Verifique com o administrador de sua conta ou com o gerente de conta Braze para ter certeza.
- Se sua empresa estiver em várias instâncias do Braze, você pode estar usando o e-mail incorreto para fazer login.	

### Suspensão da conta	

Isso não acontece com muita frequência, mas levamos muito a sério a suspensão e a exclusão de contas. Se você encontrar esse erro, recomendamos que entre em contato com o administrador Braze da sua empresa, com o gerente de conta Braze ou com o [Suporte][suporte].

## O painel de controle do Braze não carrega nem funciona como esperado

Primeiro, teste se o painel será carregado em um navegador diferente. Se o problema não persistir em um navegador diferente, tente o seguinte:

- **Reinicie o painel:** Faça logout, saia do navegador e tente fazer login no painel.
- **Atualize seu navegador local:** [Limpe os cookies e o cache do navegador]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies) e, em seguida, tente fazer login no painel novamente.
- **Use plug-ins compatíveis ou ferramentas de terceiros:** Bloqueadores de anúncios ou softwares de segurança podem impedir o carregamento do painel de controle do Braze. Para testar isso, desative um bloqueador de anúncios e, em seguida, faça login no painel de controle do Braze.
        \- Você também pode verificar os logs do console do navegador. Os erros relacionados a `ERR_BLOCKED_BY_CLIENT` podem indicar que o conteúdo está bloqueado por um bloqueador de anúncios.
- **Verifique a qualidade de sua conexão:** A qualidade de sua conexão pode ser ruim. Tente fazer login no painel de controle do Braze em outro dispositivo.
- **Confirme que está acessando o cluster correto:** Verifique se está fazendo login no cluster atribuído à sua empresa. Por exemplo, você pode estar atribuído à US-03, mas está fazendo login na US-01.
- **Atualize seu navegador:** Atualize seu navegador para o [navegador compatível]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers) mais recente e, em seguida, tente fazer login no painel.

Se o problema ocorrer em todos os navegadores, tente o seguinte:

- **Verifique sua conexão de rede:** Tente desativar sua VPN, se possível, ou desative e reative sua conexão de rede.
- **Reinicie seu dispositivo:** Tente fazer login no painel de controle do Braze depois de reiniciar o dispositivo.

Se tiver resolvido os problemas anteriores e o painel ainda não carregar ou não funcionar como esperado, entre em contato com [o Suporte]({{site.baseurl}}/braze_support/).

## O usuário não pertence a nenhum espaço de trabalho

Para verificar isso, acesse **Configurações** > **Usuários da empresa** e verifique as permissões do usuário no nível do espaço de trabalho. Adicione os espaços de trabalho necessários aos **Espaços de trabalho**.

## Solução de problemas como um novo usuário

Se você é um novo usuário do Braze e está tendo problemas para fazer login ou acessar sua conta pela primeira vez, siga estas etapas para resolver problemas comuns:

### Nunca recebi o e-mail de boas-vindas

- Verifique sua pasta de spam: Confirme se o e-mail de ativação da conta não foi filtrado em sua pasta de spam ou lixo eletrônico.
- Verifique seu endereço de e-mail: Peça a seu administrador que verifique o endereço de e-mail associado à sua nova conta Braze para confirmar se está correto.
- Políticas de TI: Confirme com sua equipe de TI se não há políticas em vigor que possam impedir o recebimento do e-mail de ativação.

### Recebi o e-mail, mas não consigo configurar a autenticação de dois fatores (2FA)

- Redefinir a 2FA: Se estiver tendo problemas para configurar a 2FA, o administrador pode redefinir a 2FA para sua conta de usuário nas configurações.
- Adicionar novamente o usuário: Se os problemas persistirem, o administrador poderá excluir sua conta de usuário do painel e adicioná-la novamente. Isso permite a criação de um usuário com os mesmos detalhes.

Se os problemas persistirem após essas etapas, entre em contato com [o suporte]({{site.baseurl}}/braze_support/) para obter mais assistência.