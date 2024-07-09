<template>
  <div class="induction-page-container">
    <header>
      <div class="navigation">
        <a href="/home">Home Page</a>
        <div class="avatar">
          <img class="user-icon" @click="goToProfile" src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
          <button @click="logout">Logout</button>
        </div>
      </div>
    </header>

    <div class="add-item">
      <div class="title">
        <h1 for="title">Add Induction Item</h1>
      </div>
      <div class="form-item">
        <label for="user-id">User ID</label>
        <select id="userid" v-model="selectedUserId"> 
          <option v-for="userid in userids" :key="userid.userID">{{ userid.userID }}</option>
        </select>
      </div>
      <div class="form-item">
        <label for="equipment-id">Equipment Name</label>
        <select id="equipment-id" v-model="selectedEquipmentName">
          <option v-for="equipment in equipments" :key="equipment.equipmentID">{{ equipment.equipmentName }}</option>
        </select>
      </div>
      <div class="form-item">
        <label for="category">Category</label>
        <select id="category" v-model="selectedCategory">
          <option v-for="category in categories" :key="category">{{ category.category }}</option>
        </select>
      </div>
      <div class="form-item">
        <label for="completion-date">Completion Date</label>
        <input type="date" id="completion-date" v-model="completionDate">
      </div>
      <div class="form-item">
        <label for="completion-status">Completion Status</label>
        <select id="completion-status" v-model="completionStatus">
          <option value="true">Completed</option>
          <option value="false">Not Completed</option>
        </select>
      </div>

      <div class="form-item">
        <button @click="addInduction">Save</button>
      </div>

      <p v-if="errorMessage" class="error-notification">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success-notification">{{ successMessage }}</p>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import { defineComponent } from 'vue';

  export default defineComponent({
    data() {
      return {
        selectedUserId: '',
        selectedEquipmentName: '',
        completionStatus: false,
        equipments: [],
        selectedCategory: '',
        categories: [],
        userids: [],
        completionDate: null,
        errorMessage: '',
        successMessage: ''
      };
    },
    mounted() {
      this.fetchUserids();
      this.fetchEquipments();
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
  fetchEquipments() {
    axios.get('http://127.0.0.1:8000/Equipment/')
      .then(response => {
        this.equipments = response.data;
      })
      .catch(error => {
        console.error('Error fetching equipments:', error);
      });
  },
  fetchUserids() {
    axios.get('http://127.0.0.1:8000/databaseUser/')
      .then(response => {
        this.userids = response.data;
      })
      .catch(error => {
        console.error('Error fetching userids:', error);
      });
  },
  goToProfile() {
    this.$router.push('/profile');
  },
  logout() {
    // Logout functionality comes here
  },
  addInduction() {
    const apiUrl = 'http://127.0.0.1:8000/Induction/create';

    const induction = {
      userID: this.selectedUserId,
      equipmentName: this.selectedEquipmentName,
      category: this.selectedCategory,
      dateCompleted: this.completionDate,
      completionStatus: this.completionStatus,
    };

    // Logging the data to be sent
    console.log('Induction data:', induction);

    if (!this.selectedUserId || !this.selectedEquipmentName || !this.selectedCategory) {
      this.errorMessage = 'Please fill in all fields.';
      return;
    }

    axios.post(apiUrl, induction)
      .then(response => {
        this.successMessage = 'Induction saved successfully!';
        // Clear the form
        this.selectedUserId = '';
        this.selectedCategory = '';
        this.selectedEquipmentName = '';
        this.completionDate = null;  // should be null to match data type
        this.completionStatus = false;  // should be false to match data type
        this.errorMessage = '';
      })
      .catch(error => {
        console.error('Error adding induction.', error);
        this.errorMessage = 'Failed to add induction. Please try again!';
      });
  }
}
  });
</script>

<style scoped>
.induction-page-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
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

.avatar img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 1rem;
}

.add-item {
  margin-top: 20px;
  background-color: #fff;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.title {
    flex: 1; /* Distributes remaining space equally */
    text-align: center; /* Horizontally center the text */
    font-weight: bold;
    font-size: 16px;
}
.form-item {
  margin-bottom: 1em;
}

.form-item label {
  display: block;
  margin-bottom: 0.5em;
}

.form-item input,
.form-item select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  cursor: pointer;
  background-color: #89b93c;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 1em;
}

button:hover {
  background-color: #3d5b0d;
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

.error-notification {
  position: fixed;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #ff4444;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 999;
}

.success-notification {
  position: fixed;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #23b41e;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 999; 
}

</style>