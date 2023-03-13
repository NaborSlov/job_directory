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
            const response = fetch('api/employers', {
                method: 'POST',
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

sendNewEmployer();
