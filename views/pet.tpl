%rebase('layout.tpl', title=f"Pet - {pet['nome']}")

<h2>Seu Pet: {{pet['nome']}}</h2>

<div id="petscreen">
<pre id="petrender">
    %if pet['felicidade'] > 7:
   ,,          ,,  
   | \        / |  
   |__\_ ,, _/__|  
 .'             '. 
´                 `
|     ^     ^     |
|   ~//  ▼  //~   |
|    ~ `-^-´ ~    |
|                 |
 '._____________.' 
    %elif pet['felicidade'] <= 3:
   ,,          ,,  
   | \        / |  
   |__\_ ,, _/__|  
 .'             '. 
´     ´     `     `
|     /     \     |
|   ~    ▼    ~   |
|    ~  .^.  ~    |
|                 |
 '._____________.' 
    %else:
   ,,          ,,  
   | \        / |  
   |__\_ ,, _/__|  
 .'             '. 
´                 `
|     O     O     |
|   ~    ▼    ~   |
|    ~ `-^-´ ~    |
|                 |
 '._____________.' 
    %end
</pre>        

<div id="petstatus">
    <div id="psttl">
        <p>🍖: {{pet['fome']}}</p>
        <p>🔋: {{pet['energia']}}</p>
        <p>💗: {{pet['vida']}}/{{pet['vidamax']}}</p>
    </div>
    <div id="psttr">
        <p>😀: {{pet['felicidade']}}</p>
        <p>🚿: {{pet['sujeira']}}</p>
        <p>💪: {{pet['qi']}}</p>
    </div>
    
</div>

<div id="acoes">
    <div class="acao"><a href="/pet/comer">🍴 Alimentar</a>
    <span class="tooltiptext">
    → 50% +1 🍖, 50% +2 🍖<br>
    → 50% -1 🚿
    </span>
    </div>

    <div class="acao"><a href="/pet/brincar" class="acao">🎉 Brincar</a>
    <span class="tooltiptext">
    → 50% +1 😀, 50% +2 😀<br>
    → 100% -1 🔋<br>
    → 50% -1 🚿
    </span>
    </div>

    <div class="acao"><a href="/pet/dormir" class="acao">💤 Dormir</a>
    <span class="tooltiptext">
    → 50% +1 🔋, 50% +2 🔋<br>
    → 100% -1 🍖<br>
    → 50% -1 🚿
    </span>
    </div>

    <div class="acao"><a href="/pet/treinar" class="acao">👊 Treinar</a>
    <span class="tooltiptext">
    → 100% -1 😀<br>
    → 100% -1 🔋<br>
    → 100% -1 🚿<br>
    → 100% -1 🍖<br>
    → 100% -10 💗<br>
    → 100% +1 💪
    </span>
    </div>

    <div class="acao"><a href="/pet/banhar" class="acao">🚿 Banhar</a>
    <span class="tooltiptext">
    100% +1 🚿<br>
    50% -1 🔋<br>
    50% -1 😀
    </span>
    </div>

    <div class="acao"><a href="/pet/curar" class="acao">💊 Curar</a>
    <span class="tooltiptext">
    → 100% +10 💗<br>
    → 50% -1 😀, 50% -2 😀
    </span>
    </div>

    <a href="/pet" class="acao">🆔 Renomear</a>

</div>
</div>