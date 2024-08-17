//create by Rafael Freitas

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const valorInput = document.getElementById('valor');
    const periodoInput = document.getElementById('periodo');
    
    function validarFormulario() {
        const valor = parseFloat(valorInput.value);
        const periodo = parseInt(periodoInput.value);
        
        if (valor <= 0) {
            alert("O valor investido deve ser maior que zero.");
            return false;
        }

        if (periodo <= 0) {
            alert("O período deve ser maior que zero.");
            return false;
        }

        return true;
    }

    form.addEventListener('submit', function (event) {
        if (!validarFormulario()) {
            event.preventDefault();
        }
    });
    
    valorInput.addEventListener('input', function () {
        if (valorInput.value !== "" && parseFloat(valorInput.value) <= 0) {
            valorInput.style.borderColor = "red";
        } else {
            valorInput.style.borderColor = "";
        }
    });

    periodoInput.addEventListener('input', function () {
        if (periodoInput.value !== "" && parseInt(periodoInput.value) <= 0) {
            periodoInput.style.borderColor = "red";
        } else {
            periodoInput.style.borderColor = "";
        }
    });
});
