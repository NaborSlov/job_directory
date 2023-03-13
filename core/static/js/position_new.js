function sendNewPosition() {
    const form = document.querySelector('#addForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const json = JSON.stringify(Object.fromEntries(formData.entries()));

        try {
            fetch('api/positions', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: json
            });

        } catch (error) {
            console.error(error)
        } finally {
            setTimeout(function () {
                window.location.replace("index");
            }, 50)

        }
    });
}

sendNewPosition();