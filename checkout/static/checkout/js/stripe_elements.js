/* CSS and JS from https://stripe.com/docs/js */

let stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
let clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let style = {
    base: {
        iconColor: '#161616',
        color: '#161616',
        fontFamily: 'Roboto, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#b80000',
        iconColor: '#b80000'
    }
};

let cardElement = elements.create('card', {
    style: style 
});

cardElement.mount('#card-element');

cardElement.on('change', function (event) {
    let cardElementError = document.getElementById('card-element-error');
    if (event.error) {
        cardElementError.innerHTML = `
            <span><i class="fas fa-exclamation-circle"></i></span>
            <span>${event.error.message}</span>`;
    } else {
        cardElementError.textContent = " ";
    }
})

// Handle Form Submit
let form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
    loading(true);
    // Prevent default action of POST
    event.preventDefault();
    // Disable card element and submit button to prevent multiple submissions
    cardElement.update({
        'disabled': true
    })
    document.getElementById('submit').disabled = true;
    stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: cardElement,
            },
        }).then(function (result) {
            if (result.error) {
                let cardElementError = document.getElementById('card-element-error');
                cardElementError.innerHTML = `
                    <span><i class="fas fa-exclamation-circle"></i></span>
                    <span>${result.error.message}</span>`;
                // Re-enable card element and submit button to allow user to re-enter details
                cardElement.update({
                    'disabled': false
                })
                document.getElementById('submit-button').disabled = false;
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
})

// Show a spinner on payment submission
var loading = function (isLoading) {
    if (isLoading) {
        // Disable the button and show a spinner
        document.querySelector("button").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("button").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#button-text").classList.remove("hidden");
    }
};