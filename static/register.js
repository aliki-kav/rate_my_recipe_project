$(document).ready(function () {
  const registerForm = $('#register-form');

  registerForm.on('submit', async function (event) {
    event.preventDefault();
    const response = await fetch(register_url, {
      method: 'POST',
      body: new FormData(registerForm[0]),
      headers: {
        'X-CSRFToken': '{{ csrf_token }}',
      },
    });
    const data = await response.json();
    if (data.success) {
      alert('Registration successful!');
      window.location.href = login_url;
    } else {
      alert('Registration unsuccessful, email or user are already in use. Please try again.');
    }
  });
});
