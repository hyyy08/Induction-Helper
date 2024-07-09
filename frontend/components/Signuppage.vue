// sign up

<template>
    <div class = "signup-container">
        <header>
            <nav>
                <ul>
                    <li><a href="/">Home Page</a></li>
                </ul>
            </nav>
        </header>

        <main>
            <div class="form-container">
                <form @submit.prevent="submitForm">
                    <div class="avatar-container">
                        <img :src="avatarUrl" alt="User Avatar" />
                    </div>

                    <input type="email" v-model="email" placeholder="New Email" required />
                    <input type="password" v-model="password" placeholder="New Password" required />
                    <button type="submit">Update Details</button>
                </form>
            </div>
        </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: '',
            avatarUrl: 'https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o='
        };
    },
    methods: {
        submitForm() {
            // Handling the form submission
            console.log(this.email, this.password);
            // Here an API call to the backend will be made to register the user
        }
    }
};
</script>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  background-color: #ffffff; /* Adjusting the background color*/
  height: 100%;
  width: 100%;
  font-family: Roboto;
}

#app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.signup-container {
  width: 100%;
  max-width: 500px; /* Adjusting width */
  margin: auto;
  padding: 40px; /* Increasing padding */
  box-shadow: 0 2px 10px 0 rgba(0,0,0,0.1); 
  border-radius: 10px; /* Adjusting the border-radius */
  background: #ffffff; /* signup container background is white */
}

header {
  text-align: center; /* Centering the header text */
  margin-bottom: 20px; /* Space below the header */
}

header nav ul {
  list-style: none;
  padding: 0;
}

header nav ul li {
  display: inline;
  margin-right: 20px;
}

.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.avatar-container {
  margin-bottom: 50px;
  display: flex; /* Using flex to center the avatar image horizontally */
  justify-content: center; /* Centering the avatar image */
}

.avatar-container img {
  width: 150px; /* Adjusting the size */
  height: 150px;
  border-radius: 50%;
  align-items: center;
}

input {
  margin-bottom: 20px; /* Increasing bottom margin */
  padding: 15px; /* Increasing padding for larger input boxes */
  border: 2px solid darkgrey; /* Making the border thicker and lighter */
  border-radius: 5px; /* Rounded corners for input boxes */
  width: 100%; /* Adjusting width to account for padding */
  box-sizing: border-box; /* Including padding and border in the width */
  font-size: 16px;
}

button {
  padding: 15px; /* Increasing padding for a larger button */
  border: none;
  border-radius: 5px; /* Rounded corners for the button */
  background-color: #98BD5D;
  color: white;
  cursor: pointer;
  width: 100%; /* Full width button */
  font-size: 18px; /* Larger font size for the button text */
  box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* Adding shadow to the button for depth */
  border: 2px solid transparent; /* Adding border to maintain layout on hover */
  transition: background-color 0.2s; /* Transition for hover effect */
}

button:hover {
  background-color: #37730C;
  color: white;
}
</style>