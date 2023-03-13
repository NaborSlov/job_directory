const urlParams = new URLSearchParams(window.location.search);
const id = urlParams.get('id')
const url = `api/position/${id}`

function loadUpdatePosition() {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const position = data['data'];
            const category = document.getElementById('categorySelect')
            const category_pos = position['category']

            if (category_pos === 'worker') {
                category.value = 'worker'
            } else if (category_pos === 'employee') {
                category.value = 'employee'
            } else {
                category.value = 'specialist'
            }

            const name = document.getElementById("positionNameInput");
            name.value = position['name'];

        })
        .catch(error => console.error(error));
}

function sendNewPosition() {
    const form = document.querySelector('#addForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const form = document.getElementById("addForm");

        const formData = new FormData(form);
        let json = JSON.stringify(Object.fromEntries(formData.entries()));

        try {
            const response = fetch(url, {
                method: 'PATCH',
                headers: {
                    "Content-Type": "application/json"
                },
                body: json
            });

            console.log(response);

        } catch (error) {
            console.error(error)
        } finally {
            setTimeout(function () {
                window.location.replace("index");
            }, 50)
        }
    });
}

loadUpdatePosition();
sendNewPosition();