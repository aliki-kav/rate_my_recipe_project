  $(document).ready(function () {
          const loginForm = $('#login_form');

          loginForm.on('submit', async function (event) {
            event.preventDefault();
            const response = await fetch(login_url, {
              method: 'POST',
              body: new FormData(loginForm[0]),
              headers: {
                'X-CSRFToken': '{{ csrf_token }}',
              },
            });
            const data = await response.json();
            if (data.success) {
              alert('Welcome back!');
              window.location.href = index_url;
            } else {
              alert('Wrong username or password provided. Please try again.');
            }
          });
        });