/*
    Core logic/payment flow:
    https://stripe.com/docs/payments/accept-a-payment
*/

// Get Stripe public key and client secret from the template
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Initialize Stripe
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Custom styling for the card element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create the card element
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle real-time validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submission and payment confirmation
var form = document.getElementById('payment-form');
form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Disable submit button to prevent multiple clicks
    form.querySelector("button[type='submit']").disabled = true;

    stripe.confirmCardPayment(client_secret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.first_name.value + ' ' + form.surname.value,
                email: form.email.value,
                phone: form.phone_number.value,
            }
        }
    }).then(function (result) {
        if (result.error) {
            // Show error in #card-errors
            var errorDiv = document.getElementById('card-errors');
            errorDiv.textContent = result.error.message;
            // Re-enable submit button
            form.querySelector("button[type='submit']").disabled = false;
        } else if (result.paymentIntent.status === 'succeeded') {
            // Payment successful, submit form to Django to finalize order
            form.submit();
        }
    });
});
