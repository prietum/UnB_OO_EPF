% rebase('layout.tpl', title='Login')

% print("status=",status)
% print("type(status)=",type(status))

<h1>faça login</h1>

%if status == '1':
    <p>ERRO: Nome de usuário errado!</p>
%elif status == '2':
    <p>Seu cadastro foi feito com sucesso!</p>
%elif status == '3':
    <p>ERRO: Senha errada!</p>
%end

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
