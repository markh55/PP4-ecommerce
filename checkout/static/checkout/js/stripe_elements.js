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
card.on('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submission and payment confirmation
var form = document.getElementById('payment-form');
form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Show loading overlay
    $('#loading-overlay').fadeToggle(100);

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
            // Re-enable card element if stripe wasn't able to process
            card.update({ 'disabled': false});
            // Hide loading overlay
            $('#loading-overlay').fadeToggle(100);
            // Show temporary error message
            $('#status-message').text('Payment failed. Please try again.').fadeIn().delay(2000).fadeOut();
        } else if (result.paymentIntent.status === 'succeeded') {
            // Show success message
            $('#status-message').text('Payment successful! Redirecting...').fadeIn();
            // Submit the form so Django can save the order
            setTimeout(function() {
            form.submit();
        }, 800);
        }
    });
});
