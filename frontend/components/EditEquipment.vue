// Add Equipment page 

<template>
  <div class="edit-item">
    <header class="navigation">
      <a href="/home" class="home-link">Home Page</a>
      <div class="title">
        <h1>Edit Equipment Item</h1>
      </div>
      <div class="avatar">
        <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
        <button @click="logout" class="logout-button">Logout</button>
      </div>
    </header>
    <div class="form-item equipment-name">
      <label for="equipment-name">Equipment Name</label>
      <select id="equipment-name" v-model="selectedEquipmentName" @change="fetchData" class="equipment-dropdown">
        <option v-for="name in equipmentNames" :key="name" :value="name">{{ name }}</option>
      </select>
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
      <button @click="updateItem">
        Update Item
      </button>
    </div>
    <div v-if="errorMessage" class="error-notification">
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'EditEquipment',
  data() {
    return {
      equipmentNames: [], // List of equipment names
      selectedEquipmentName: '', // Selected equipment name
      description: '', // Description of the equipment
      errorMessage: '', // Error message
    };
  },
  methods: {
    fetchEquipmentNames() {
      // Fetch the list of equipment names from API
      axios.get('http://127.0.0.1:8000/Equipment/')
        .then(response => {
          console.log('Equipment names fetched:', response.data);
          this.equipmentNames = response.data.map(item => item.equipmentName);
          if (this.equipmentNames.length > 0) {
            this.selectedEquipmentName = this.equipmentNames[0]; // Set the default selected value
            this.fetchData(); // Fetch data for the default selected equipment name
          }
        })
        .catch(error => {
          console.error('Error fetching equipment names:', error);
          this.errorMessage = 'Failed to fetch equipment names. Please try again!';
        });
    },
    fetchData() {
      // Fetch data of the selected equipment item from API and populate the form fields
      if (this.selectedEquipmentName) {
        axios.get(`http://127.0.0.1:8000/Equipment/${this.selectedEquipmentName}`)
          .then(response => {
            console.log('Response data:', response.data);
            const equipment = response.data;
            if (equipment) {
              this.description = equipment.equipmentDescription;
              console.log('Equipment data fetched:', equipment);
            } else {
              this.description = '';
            }
          })
          .catch(error => {
            console.error('Error fetching data:', error);
            this.errorMessage = 'Failed to fetch data. Please try again!';
          });
      }
    },
    updateItem() {
      // Update the equipment item with the new data
      if (this.selectedEquipmentName) {
        axios.put(`http://127.0.0.1:8000/Equipment/${this.selectedEquipmentName}`, {
          equipmentName: this.selectedEquipmentName,
          equipmentDescription: this.description
        })
          .then(response => {
            console.log('Item updated!', response.data);
            this.errorMessage = 'Item updated successfully!';
          })
          .catch(error => {
            console.error('Error updating item.', error);
            this.errorMessage = 'Failed to update item. Please try again!';
          });
      } else {
        this.errorMessage = 'No equipment selected for update.';
        console.error('No equipment selected for update.');
      }
    }
  },
  created() {
    // Fetch the list of equipment names when the component is created
    this.fetchEquipmentNames();
  },
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

.edit-item {
  margin: 0 auto;
  text-align: left;
  margin: 2em;
}

.equipment-name {
  margin-bottom: 1em;
  margin-top: 5em;
}

.description {
  margin-bottom: 1em;
}

label {
  display: block;
}

input {
  width: 80%;
  padding: 0.5em;
  margin: 0 auto;
  font-size: 1em;
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
  font-size: 1em;
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
  font-size: 1em;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 999; /* above other content */
}

.equipment-dropdown {
  width: 100%; /* Make dropdown width 100% of its container */
  padding: 0.5em;
  font-size: 1em;
}


</style>
