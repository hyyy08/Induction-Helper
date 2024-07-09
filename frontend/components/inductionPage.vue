<template>
  <div class="induction-page-container">
    <header class="navigation">
      <a href="/home" class="home-link">Home Page</a>
      <div class="avatar">
        <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
        <button class="logout-button" @click="logout">Logout</button>
      </div>
    </header>

    <div class="search-section">
      <input type="text" v-model="studentId" placeholder="Enter student ID">
      <button @click="searchStudent">Search</button>
      <button @click="addInduction">Add Induction/s</button>
      <button @click="goToUserAdd">New Student</button>
    </div>

    <div v-if="filteredInductions.length" class="results-section">
      <div class="induction-header">
        <div>User Details</div>
        <div>Date Added</div>
        <div>Category</div>
        <div>Equipment Details</div>   
        <div>Status</div>
      </div>
      <div class="induction-item" v-for="induction in filteredInductions" :key="induction.userDetails.userID">
        <div class="user-details">{{ induction.userDetails.firstName }} {{ induction.userDetails.lastName }}<br>{{ induction.userDetails.email }}</div>
        <div class="date-added">{{induction.dateAdded }}</div>
        <div class="category">{{ induction.category }}</div>
        <div class="equipment-details">{{ induction.equipmentDetails.equipmentName }} - {{ induction.equipmentDetails.equipmentDescription }}</div>
        <div class="status">{{ induction.completionStatus ? 'Completed' : 'Incomplete' }}</div>
      </div>
    </div>
    <div v-else-if="hasSearched" class="results-section">
      <p>No inductions found for the entered student ID.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      studentId: '',
      inductions: [],
      filteredInductions: [],
      hasSearched: false
    };
  },
  methods: {
    goToProfile() {
      this.$router.push('/profile');
    },
    searchStudent() {
      this.hasSearched = true;
      axios.get(`http://127.0.0.1:8000/Induction/`)
        .then(response => {
          this.inductions = response.data;
          this.filteredInductions = this.inductions.filter(induction => induction.userDetails.userID === parseInt(this.studentId));
        })
        .catch(error => {
          console.error('Error fetching induction', error);
        });
    },
    addInduction() {
      this.$router.push('/studentInduction');
    },
    goToUserAdd() {
      this.$router.push('/useradd');
    },
    logout() {
      // Logic to handle logout
    }
  }
};
</script>

<style scoped>
.induction-page-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  border: grey;
}

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #B8CFB0;
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

.avatar button {
  display: inline;
  padding: 0.5rem 1rem;
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  color: black;
  transition: background-color 0.2s ease;
  text-align: center;
  border-radius: 5px;
  font-family: Roboto;
  margin-right: 1rem;
  margin-left: 1rem;
  vertical-align: middle;
}

.avatar button:hover {
  background-color: #37730C;
  color: white;
  transition: background-color 0.2s ease;
}

.search-section {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  font-size: 16px;
}

.search-section input {
  padding: 10px;
  margin-right: 10px;
  font-size: 16px;
  border: 2px solid darkgray;
  border-radius: 5px;
  transition: background-color 0.2s ease;
  font-family: Roboto;
}

.search-section input:hover {
  border-radius: 5px;
  background-color: lightgrey;
}

.search-section button {
  padding: 10px;
  margin-right: 10px;
  font-size: 1em;
  width: 80%;
  margin: 1em;
  background-color: #98BD5D; /* Light green color */
  border: none;
  color: white;
  font-size: 16px;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  transition: background-color 0.2s ease;
  font-family: Roboto;
}

.search-section button:hover {
  color: white;
  background-color: #37730C; /* Darker shade of green on hover */
}

.results-section {
  margin-top: 20px;
  background-color: #fff;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  font-size: 1em;
  font-family: Roboto;
}

.induction-header {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 80px; /* Adjusted value to increase the space between headings */
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid darkgrey;
  font-size: 1em;
}
.induction-header > div:nth-child(2) {
  padding-left: 40px; /* Adjust the padding to add spaces */
}

.induction-item {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px; /* Adjusted value to match the header spacing */
  margin-bottom: 10px;
  border-radius: 5%;
}

.user-details, .equipment-details, .category, .date-added, .status {
  word-wrap: break-word;
  overflow-wrap: break-word;
}

button {
  cursor: pointer;
}
</style>