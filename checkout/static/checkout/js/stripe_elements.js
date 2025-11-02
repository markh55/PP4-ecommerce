/*
    Core logic/payment flow for Stripe checkout
    https://stripe.com/docs/payments/accept-a-payment
*/

$(document).ready(function() {
    // Get Stripe public key and client secret from the template
    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    var clientSecret = $('#id_client_secret').text().slice(1, -1);

    // Debug: Log to console to verify keys are loading
    console.log('Stripe Public Key:', stripePublicKey ? 'Loaded' : 'MISSING');
    console.log('Client Secret:', clientSecret ? 'Loaded' : 'MISSING');

    // Check if keys exist before initializing
    if (!stripePublicKey || !clientSecret) {
        console.error('Stripe keys are missing!');
        var errorDiv = document.getElementById('card-errors');
        errorDiv.textContent = 'Payment system configuration error. Please contact support.';
        document.querySelector("button[type='submit']").disabled = true;
    } else {
        // Initialize Stripe
        var stripe = Stripe(stripePublicKey);
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

        // Create and mount the card element
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
        var submitting = false;

        form.addEventListener('submit', function (ev) {
            ev.preventDefault();

            // Prevent double submission
            if (submitting) {
                return;
            }
            submitting = true;

            // Disable card element and submit button
            card.update({ 'disabled': true });
            var submitButton = form.querySelector("button[type='submit']");
            submitButton.disabled = true;

            // Show loading overlay
            $('#loading-overlay').fadeIn(100);

            // Gather form data
            var saveInfo = $('#id-save-info').is(':checked');
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

            var postData = {
                'csrfmiddlewaretoken': csrfToken,
                'client_secret': clientSecret,
                'save_info': saveInfo,
            };

            var url = '/checkout/cache_checkout_data/';

            // Post to cache_checkout_data view before confirming payment
            $.post(url, postData)
                .done(function () {
                    // Confirm the card payment with Stripe
                    stripe.confirmCardPayment(clientSecret, {
                        payment_method: {
                            card: card,
                            billing_details: {
                                name: $.trim(form.first_name.value) + ' ' + $.trim(form.surname.value),
                                email: $.trim(form.email.value),
                                phone: $.trim(form.phone_number.value),
                            }
                        },
                    }).then(function (result) {
                        if (result.error) {
                            // Display error to user
                            var errorDiv = document.getElementById('card-errors');
                            var html = `
                                <span class="icon" role="alert">
                                    <i class="fas fa-times"></i>
                                </span>
                                <span>${result.error.message}</span>
                            `;
                            errorDiv.innerHTML = html;

                            // Re-enable form elements
                            card.update({ 'disabled': false });
                            submitButton.disabled = false;
                            submitting = false;

                            // Hide loading overlay
                            $('#loading-overlay').fadeOut(100);
                        } else {
                            if (result.paymentIntent.status === 'succeeded') {
                                // Payment successful - submit the form to Django
                                form.submit();
                            }
                        }
                    });
                })
                .fail(function (xhr, status, error) {
                    // Display error without reloading page
                    var errorDiv = document.getElementById('card-errors');
                    errorDiv.textContent = 'There was an error processing your payment. Please try again.';

                    // Re-enable form elements
                    card.update({ 'disabled': false });
                    submitButton.disabled = false;
                    submitting = false;

                    // Hide loading overlay
                    $('#loading-overlay').fadeOut(100);

                    // Log error for debugging
                    console.error('Cache checkout data error:', error);
                });
        });
    }
});