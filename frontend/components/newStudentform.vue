// new student 

<template>
  <div class="new-student-form-container">
    <header>
      <div class="navigation">
        <a href="/" class="home-link">Home Page</a>
        <div class="header-title">Add New Student</div>
        <div class="avatar">
          <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
          <button class="logout-button">Logout</button>
        </div>
      </div>
    </header>
    
    <div class="new-student-form-content">
      <form @submit.prevent="submitNewStudent">
        <div>
          <label for="student-id">Student ID</label>
          <input type="text" id="student-id" v-model="student.id" required>
        </div>
        <div>
          <label for="email">Email</label>
          <input type="email" id="email" v-model="student.email" required>
        </div>
        <div>
          <label for="first-name">First Name</label>
          <input type="text" id="first-name" v-model="student.firstName" required>
        </div>
        <div>
          <label for="last-name">Last Name</label>
          <input type="text" id="last-name" v-model="student.lastName" required>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // axios

export default {
  data() {
    return {
      student: {
        id: '', //student id
        email: '', //student email
        firstName: '', //student first name
        lastName: '' //student last name 
      }
    };
  },
  methods: {
    submitNewStudent() {
      console.log("Form submission attempted");
      //The URL for the API endpoint
      const apiUrl = 'http://127.0.0.1:8000/databaseUser/create/';
      
      // Preparing the data to send, mapping local model to the expected API model
      const userData = {
        userID: this.student.id,
        email: this.student.email,
        firstName: this.student.firstName,
        lastName: this.student.lastName,
        //Might need additional fields if required by the API
      };

      // Using axios to send a POST request
      axios.post(apiUrl, userData)
        .then(response => {
          // Handling the response from the server here
          console.log('User created:', response.data);
          
          // If redirection is required after successful creation:
          this.$router.push('/inductions');
          
          // Clearing the form
          this.student = { id: '', email: '', firstName: '', lastName: '' };
        })
        .catch(error => {
          // Handling the errors here,displaying the error message to the user
          console.error('There was an error creating the user:', error);
        });
    }
  }
};
</script>

<style scoped>
.new-student-form-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.new-student-form-content {
  margin-top: 32px;
}

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #B8CFB0;
  padding: 1rem;
  font-size: 24px;
  height: 5em;
}

.home-link {
  margin-right: auto;
  padding: 0.5rem 1rem;
  text-decoration: none;
  color: black;
  font-size: 16px;
}

.header-title {
  flex-grow: 1;
  text-align: center;
  font-size: 24px;
  font-weight: bold; /* Added bold font weight */
}

.avatar {
  display: flex;
  align-items: center;
}

.avatar img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 1rem;
}

.logout-button {
  padding: 0.5rem 1rem;
  background-color: transparent;
  border: none;
  color: black;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.2s ease;
}

.logout-button:hover {
  background-color: #37730C;
  color: white;
}

form {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /*aligns items at the start of the flex container*/
  gap: 1.5rem;
}

label {
  font-size: 16px;
}

input {
  padding: 16px;
  border: 1px solid black;
  border-radius: 5px;
  font-size: 16px;
  margin-top: 5px;
  width: 250%; /* Adjusted width */
}

button {
  align-self: center; /* Aligning the button to the center of the flex container */
  max-width: 200px;
  padding: 1rem;
  background-color: #98BD5D;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  font-size: 16px;
  margin-top: 24px;
}

button:hover {
  background-color: #37730c; /* Darker shade of green on hover */
  color: white;
}

/* Additional responsive adjustments */
@media (max-width: 768px) {
  .new-student-form-container {
    padding: 1rem;
  }
}
</style>
