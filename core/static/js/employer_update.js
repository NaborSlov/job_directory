const urlParams = new URLSearchParams(window.location.search);
const id = urlParams.get('id')
const url = `api/employer/${id}`

function loadUpdateEmployer() {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const employer = data['data'];
            const genre = document.getElementById("genderSelect");

            if (employer['genre'] === "male") {
                genre.value = "male";
            } else {
                genre.value = "female";
            }

            const first_name = document.getElementById("first_name");
            first_name.value = employer['first_name'];
            const last_name = document.getElementById("last_name");
            last_name.value = employer['last_name'];
            const patronymic = document.getElementById("patronymic");
            patronymic.value = employer['patronymic'];
            const age = document.getElementById("age");
            age.value = employer['age'];
            const position_id = document.getElementById("positionSelect");
            position_id.value = employer['position']['id'];

        })
        .catch(error => console.error(error));
}

function sendNewEmployer() {
    const form = document.querySelector('#addForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const optionSelect = document.getElementById("optionIdSelect");
        const selectedValue = optionSelect.value;

        const formData = new FormData(form);

        const formObj = Object.fromEntries(formData.entries())
        formObj['position_id'] = parseInt(selectedValue);

        let json = JSON.stringify(formObj);

        try {
            const response = fetch(url, {
                method: 'PATCH',
                headers: {
                    "Content-Type": "application/json"
                },
                body: json
            });

            console.log(response)

        } catch (error) {
            console.error(error)
        } finally {
            setTimeout(function () {
                window.location.replace("index");
            }, 50)
        }
    });
}

loadUpdateEmployer();
sendNewEmployer();