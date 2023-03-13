// Функция для получения списка должностей и отображения их в таблице
function loadPositions() {
    fetch('api/positions')
        .then(response => response.json())
        .then(data => {
            const positionsTableBody = document.getElementById('positions-table-body');
            positionsTableBody.innerHTML = '';
            for (const position of data['data']) {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${position.name}</td>
                    <td>${position.category}</td>
                    <td>
                        <a class="btn btn-sm btn-primary" href="positon_update?id=${position.id}" >Редактировать</a>
                        <button class="btn btn-sm btn-danger" onclick="deletePosition(${position['id']})">Удалить</button>
                    </td>
                `;
                positionsTableBody.appendChild(tr);
            }
        })
        .catch(error => console.error(error));
}

function loadEmployers() {
    fetch('api/employers')
        .then(response => response.json())
        .then(data => {
            const positionsTableBody = document.getElementById("employees-table-body");
            positionsTableBody.innerHTML = "";
            for (const emplor of data['data']) {
                const tr = document.createElement('tr');
                const FIO = [emplor['last_name'], emplor['first_name'], emplor['patronymic']]
                tr.innerHTML = `
                    <td>${FIO.join(' ')}</td>
                    <td>${emplor['gender']}</td>
                    <td>${emplor['age']}</td>
                    <td>${emplor['position']['name'] ? emplor['position']['name'] : null}</td>
                    <td>${emplor['position']['category'] ? emplor['position']['category'] : null}</td>
                    <td>
                        <a class="btn btn-sm btn-primary" href="employer_update?id=${emplor.id}">Редактировать</a>
                        <button class="btn btn-sm btn-danger" onclick="deleteEmployer(${emplor.id})">Удалить</button>
                    </td>
                `;
                positionsTableBody.appendChild(tr)
            }
        })
        .catch(error => console.error(error));
}

function deletePosition(id) {
    fetch(`api/position/${id}`, {method: 'DELETE'})
        .then(response => response.json())
        .catch(error => console.error(error));
    loadPositions()
}

function deleteEmployer(id) {
    fetch(`api/employer/${id}`, {method: 'DELETE'})
        .then(response => response.json())
        .catch(error => console.error(error));
    loadEmployers()
}


loadPositions();
loadEmployers();
