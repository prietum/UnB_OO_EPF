% rebase('layout.tpl', title='Login')

% print("status=",status)
% print("type(status)=",type(status))

%if status == 1:
<p>ERRO: Nome de usuário ou senha errados!</p>
%end

%if status == 2:
<p>ERRO: Seu cadastro foi feito com sucesso!</p>
%end

<h1>faça login</h1>
<form method="post">
    <label>Nome:<br>
        <input type="text" name="nome" required>
    </label><br><br>
    <label>Senha:<br>
        <input type="text" name="senha" required>
    </label><br><br>
    <button type="submit">Login</button>
</form>
<a href="/login/register">Cadastrar</a>