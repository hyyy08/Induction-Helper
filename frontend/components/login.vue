<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async login() {
      this.error = ''; // Clear any existing errors
      try {
        const response = await axios.post(`http://127.0.0.1:8000/login/`, {
          email: this.email,
          password: this.password
        });
        localStorage.setItem('token', response.data.token);
        this.$router.push('/home');
      } catch (err) {
        if (err.response && err.response.status === 400) {
          this.error = 'Invalid email or password.';
        } else {
          this.error = 'An error occurred. Please try again later.';
        }
      }
    }
  }
};
</script>

<style scoped>
.error {
  color: #ff4444;
}
.title {
  margin: 2em;
  text-align: left;
  font-size: 1em;
}
.form-item {
  margin: 2em;
  text-align: left;
}
label {
  display: block;
}
input {
  width: 50%;
  padding: 0.5em;
  margin: 0 auto;
  font-size: 1em;
}
button {
  width: 10%;
  margin: 2em;
  background-color: #89b93c; /* Light green color */
  border: none;
  color: white;
  font-size: 1em;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #3d5b0d; /* Darker shade of green on hover */
}
.error-notification {
  position: fixed;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #ff4444; /* error in red */
  color: white;
  font-size: 1em;
  padding: 20px 20px;
  border-radius: 5px;
  z-index: 999; /* above other content */
}
</style>
