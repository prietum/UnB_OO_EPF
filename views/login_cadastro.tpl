% rebase('layout.tpl', title='Cadastro')

%if status == 1:
<p>ERRO: Já existe um usuário com esse nome!</p>
%end

<h1>faça cadastro</h1>
<form method="post">
    <label>Nome:<br>
        <input type="text" name="nome" required>
    </label><br><br>
    <label>Senha:<br>
        <input type="text" name="senha" required>
    </label><br><br>
    <button type="submit">Cadastrar</button>
</form>
<a href="/login">Login</a>