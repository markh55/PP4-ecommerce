document.addEventListener('DOMContentLoaded', function() {
    const avatarInput = document.getElementById('id_avatar');
    if (avatarInput) {
        avatarInput.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                document.getElementById('avatarForm').submit();
            }
        });
    }
});