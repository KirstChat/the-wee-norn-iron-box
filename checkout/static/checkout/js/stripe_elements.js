/* CSS and JS from https://stripe.com/docs/js */

var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
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

var cardElement = elements.create('card', {
    style: style 
});

cardElement.mount('#card-element');

cardElement.on('change', function (event) {
    var cardElementError = document.getElementById('card-element-error');
    if (event.error) {
        cardElementError.innerHTML = `
            <span><i class="fas fa-exclamation-circle"></i></span>
            <span>${event.error.message}</span>`;
    } else {
        cardElementError.textContent = " ";
    }
})

// Handle Form Submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
    loading(true);
    // Prevent default action of POST
    event.preventDefault();
    // Disable card element and submit button to prevent multiple submissions
    cardElement.update({
        'disabled': true
    })
    document.getElementById('submit-button').disabled = true;

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };

    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: cardElement,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.contact_number.value),
                    address: {
                        line1: $.trim(form.address_line_1.value),
                        line2: $.trim(form.address_line_2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.contact_number.value),
                address: {
                    line1: $.trim(form.address_line_1.value),
                    line2: $.trim(form.address_line_2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            }
        }).then(function (result) {
            if (result.error) {
                var cardElementError = document.getElementById('card-element-error');
                cardElementError.innerHTML = `
                    <span><i class="fas fa-exclamation-circle"></i></span>
                    <span>${result.error.message}</span>`;
                // Re-enable card element and submit button to allow user to re-enter details
                loading(false);
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
    }).fail(function () {
        location.reload();
    })
})

// Show a spinner on payment submission
// Code from Stripe Docs: https://stripe.com/docs/payments/integration-builder
var loading = function (isLoading) {
    if (isLoading) {
        // Disable the button and show a spinner
        document.querySelector('button').disabled = true;
        document.querySelector('#spinner').classList.remove('hidden');
        document.querySelector('#button-text').classList.add('hidden');
    } else {
        document.querySelector('button').disabled = false;
        document.querySelector('#spinner').classList.add('hidden');
        document.querySelector('#button-text').classList.remove('hidden');
    }
};