function loadPosition() {
    fetch('api/positions')
        .then(response => response.json())
        .then(data => {
            const positionSelect = document.getElementById('positionSelect');
            positionSelect.innerHTML = '';
            for (const position of data['data']) {
                const opt = document.createElement('option');
                opt.innerHTML = `<option value=${position.id} id="optionIdSelect">${position.name}</option>`;
                positionSelect.appendChild(opt)
            }
        })
        .catch(error => console.error(error));
}

loadPosition();