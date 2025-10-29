document.addEventListener('DOMContentLoaded', () => {

    const formAluguel = document.getElementById('formAluguel');
    const inputCliente = document.getElementById('cliente');
    const inputEndereco = document.getElementById('endereco');
    const inputItens = document.getElementById('itens');
    const listaAlugueis = document.getElementById('listaAlugueis');

    const getAlugueis = () => {
        return JSON.parse(localStorage.getItem('alugueis')) || [];
    };

    const saveAlugueis = (alugueis) => {
        localStorage.setItem('alugueis', JSON.stringify(alugueis));
    };

    const renderAlugueis = () => {
        listaAlugueis.innerHTML = '';
        const alugueis = getAlugueis();

        if (alugueis.length === 0) {
            listaAlugueis.innerHTML = '<p>Nenhum aluguel cadastrado ainda.</p>';
            return;
        }

        alugueis.forEach(aluguel => {
            const card = document.createElement('div');
            card.className = 'aluguel-card';
            card.dataset.id = aluguel.id;

            card.innerHTML = `
                <h3>${aluguel.cliente}</h3>
                <p><strong>Endereço:</strong> ${aluguel.endereco || 'Não informado'}</p>
                <p><strong>Itens:</strong> ${aluguel.itens || 'Não informado'}</p>
                <button class="btn-delete" title="Excluir aluguel">&times;</button>
            `;
            listaAlugueis.appendChild(card);
        });
    };

    formAluguel.addEventListener('submit', (e) => {
        e.preventDefault();

        const cliente = inputCliente.value.trim();
        const endereco = inputEndereco.value.trim();
        const itens = inputItens.value.trim();

        if (!cliente) {
            alert('Por favor, informe o nome do cliente.');
            return;
        }

        const novoAluguel = {
            id: Date.now(),
            cliente,
            endereco,
            itens
        };

        const alugueis = getAlugueis();
        alugueis.push(novoAluguel);
        saveAlugueis(alugueis);

        formAluguel.reset();
        renderAlugueis();
    });

    listaAlugueis.addEventListener('click', (e) => {
        if (e.target.classList.contains('btn-delete')) {
            const card = e.target.closest('.aluguel-card');
            const idParaDeletar = Number(card.dataset.id);

            let alugueis = getAlugueis();
            alugueis = alugueis.filter(aluguel => aluguel.id !== idParaDeletar);
            saveAlugueis(alugueis);

            renderAlugueis();
        }
    });

    renderAlugueis();
});