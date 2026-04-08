const loginForm = document.getElementById('loginForm');
const loginMessage = document.getElementById('loginMessage');

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/login', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            const errorData = await response.json(); 
            loginMessage.textContent = errorData.message || 'Network error'; 
            return; 
        }

        const data = await response.json(); 

        if (data.success) { 
            loginMessage.textContent = data.message; 
            // Redirect to the desired page (replace with actual redirect)
            window.location.href = '/dashboard'; 
        } else {
            loginMessage.textContent = data.message; 
        }
    } catch (error) {
        console.error('Error during login:', error);
        loginMessage.textContent = 'An error occurred during login.';
    }
});