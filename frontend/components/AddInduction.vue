// Add Induction page 

<template>
  <div class="add-item">
    <header class="navigation">
      <a href="/home" class="home-link">Home Page</a>
      <div class="title">
        <h1>Add Induction Item</h1>
      </div>
      <div class="avatar">
        <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
        <button @click="logout" class="logout-button">Logout</button>
      </div>
    </header>
    <div class="form-item induction-name">
      <label for="induction-name">Induction Name</label>
      <input
        id="induction-name"
        autocomplete="off"
        type="text"
        v-model="inductionName"
      >
    </div>
    <div class="form-item description">
      <label for="description">Description</label>
      <input
        id="description"
        autocomplete="off"
        type="text"
        v-model="description"
      >
    </div>
    <div class="form-item">
      <button @click="addItem">
        Add Item
      </button>
    </div>
    <div v-if="errorMessage" class="error-notification">
      <p>{{ errorMessage }}</p>
    </div>
    <div v-if="successMessage" class="success-notification">
      <p>{{ successMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'AddInductionItem',
  data() {
    return {
      inductionName: '', // Induction Name
      description: '', // Induction Description
      errorMessage: '', // Error Message
      successMessage: '', // Success Message
      selectedUserId: null,
      selectedEquipmentName: null,
      selectedCategory: null,
      completionDate: '',
      completionStatus: '',
      userids: [],
      equipment: [],
      categories: []
    };
  },
  mounted() {
    this.fetchUserIds();
    this.fetchEquipment();
    this.fetchCategories();
  },
  methods: {
    fetchCategories() {
      axios.get('http://127.0.0.1:8000/Category/')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    },
    fetchEquipment() {
      axios.get('http://127.0.0.1:8000/Equipment/')
        .then(response => {
          this.equipment = response.data;
        })
        .catch(error => {
          console.error('Error fetching equipment:', error);
        });
    },
    fetchUserIds() {
      axios.get('http://127.0.0.1:8000/databaseUser/')
        .then(response => {
          this.userids = response.data;
        })
        .catch(error => {
          console.error('Error fetching user IDs:', error);
        });
    },
    addItem() {
      if (!this.selectedUserId) {
        this.errorMessage = 'Please select a user ID.';
        return;
      }

      if (!this.description.trim()) {
        this.errorMessage = 'Please fill in the description.';
        return;
      }

      const induction = {
        userID: this.selectedUserId,
        equipment: this.selectedEquipmentName,
        category: this.selectedCategory,
        dateCompleted: this.completionDate,
        completionStatus: this.completionStatus,
        name: this.inductionName,
        description: this.description
      };

      axios.post('http://127.0.0.1:8000/Induction/create', induction)
        .then(response => {
          console.log('Item added!', response.data);
          this.successMessage = 'Induction item added successfully!';
          this.errorMessage = '';
        })
        .catch(error => {
          console.error('Error adding induction.', error);
          this.errorMessage = 'Failed to add induction. Please try again!';
          this.successMessage = '';
        });
    }
  }
});
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


.completion-date{
  margin-bottom: 1em;
  margin-top: 5em;
}

.user-id {
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