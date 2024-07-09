// Add Equipment page 

<template>
  <div class="add-item">
        <header class="navigation">
            <a href="/home" class="home-link">Home Page</a>
            <div class="title">
                <h1>Add Equipment Item</h1>
            </div>
            <div class="avatar">
                <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
                <button @click="logout" class="logout-button">Logout</button>
            </div>
        </header>
    <div class="equipment-name">
      <label for="equipment-name">Equipment Name</label>
      <input
        id="equipment-name"
        autocomplete="off"
        type="text"
        v-model="equipmentName"
      >
    </div>
    <div class="description">
      <label for="description">Description</label>
      <input
        id="description"
        autocomplete="off"
        type="text"
        v-model="description"
      >
    </div>
    <div class="form-item">
      <button v-on:click="addItem">
        Add Item
      </button>
    </div>
    <div v-if="errorMessage" class="error-notification">
      <p>{{ errorMessage }}</p>
    </div>
    <div class="error-notification" v-if="errorMessage">
      <p>{{ errorMessage }}</p>
    </div>
  </div>
    <div v-if="successMessage" class="success-notification">
      <p>{{ successMessage }}</p>
    </div>
</template>

<script>
 import axios from 'axios';
import { defineComponent } from 'vue';

export default {
  name: 'AddItemForm',
  data() {
    return {
      equipmentName: '', // Separate property for Equipment Name
      description: '', // Separate property for Type of Equipment 
      errorMessage: '', // Error Message
    };
  },
  methods: {
    addItem() {
      const apiUrl = 'http://127.0.0.1:8000/Equipment/create';
      
      const equipmentData = {
        equipmentID:  this.equipmentID,
        equipmentName: this.equipmentName, 
        equipmentDescription: this.description,
      };

      if (!this.equipmentName.trim()) {
        this.errorMessage = 'Please fill in the Equipment Name.';
        return; // Error if the section is empty
      }
      
      if (!this.description.trim()) {
        this.errorMessage = 'Please fill in the Type of Equipment.';
        return; // Error if the section is empty
      }

      // Reset error message if all fields are filled
      this.errorMessage = '';

      axios.post(apiUrl, equipmentData)
      .then(response => {
        console.log('Equipment added!', response.data); 
        this.successMessage = 'Item successfully added';
        // when item added successfully
        this.equipmentID= '';
        this.equipmentName= '';
        this.description= '';
      })
      .catch(error => {
        console.error('Error adding item.', error); 
        // when item cannot be added
        this.errorMessage = 'Failed to add item. Please try again!';
      });
    }
  }
};
</script>

<style scoped>
body {
  font-family: Roboto;
}

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #B8CFB0;
  padding: 1rem;
  font-size: 16px;
  height: 5em;
}

.home-link {
    margin-right: auto;
    padding: 0.5rem 1rem;
    text-decoration: none;
    color: black;
    font-size: 16px;
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
    font-size: 1em;
    transition: background-color 0.2s ease;
}

.logout-button:hover {
    background-color: #37730C;
    color: white;
}

.title {
    flex: 1; /* Distributes remaining space equally */
    text-align: center; /* Horizontally center the text */
    font-weight: bold;
    font-size: 16px;
}

.add-item {
  margin: 0 auto;
  text-align: left;
  margin: 2em;
}

.title {
  margin-bottom: 2em;
  font-size: 1em;
}

.equipment-name {
  margin-bottom: 1em;
  margin-top: 1em;
}

.attending-students {
  margin-bottom: 1em;
}

.equipment-description {
  margin-bottom: 1em;
}

label {
  display: block;
}

input {
  width: 80%;
  padding: 0.5em;
  margin: 0 auto;
}

.form-item {
  margin: 1em 0;
}

button {
  background-color: #98bd5d; /* Green color */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  display: inline-block;
  font-size: 16px;
  margin-bottom: 1em;
  cursor: pointer;
  margin-left: 10px;
  border-radius: 5px;
  margin: 30px;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #37730c; /* Dark green color on hover */
}

.error-notification {
  position: fixed;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #ff4444; /* error in red */
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 999; /* above other content */
}

.success-notification {
  position: fixed;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #23b41e; /* success in green */
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 999; 
}
</style>
