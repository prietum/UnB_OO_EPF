% rebase('layout.tpl', title = 'Criar Tamagotchi')

<h1>Criar seu Tamagotchi</h1>

<form action="/pet/create" method="post">
    <label>Nome do Tamagotchi:</label>
    <input type="text" name="nome" required>

    <button type="submit">Criar</button>
</form>