// home page

<template>
    <div class="home-page">
      <header class="home-header">
        <img class="user-icon" @click="goToProfile" src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
        <button class="logout-button" @click="logout">Logout</button>
      </header>
      <div class="card-container">
        <button class="card" @click="goToManageInductions">View Student Inductions</button>
        <button class="card" @click="goToAddEquipment">Manage Equipment</button>
        <button class="card" @click="goToCategory">Manage Category</button>
        <button class="card" @click="goToReporting">Manage Reports</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        // Space to Handle logout logic
      },
      goToManageInductions() {
        this.$router.push('/inductions');
      },
      goToAddEquipment() {
        this.$router.push('/equipment'); //Need to make a future connection here to Saya's page
      },
      goToReporting() { // Add this method
      this.$router.push('/reporting'); // Use the path you defined in router.js
      },
      goToProfile() {
      this.$router.push('/profile');
      },
      goToCategory() {
        this.$router.push('/categoryList');
      },
    }
  };
  </script>
  
<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #ffffff;
}

.home-header {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  padding: 1rem;
  box-sizing: border-box;
}
  
.user-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 1rem; /* Spacing between icon and logout button */
}
  
.logout-button {
  padding: 0.5rem 1rem;
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.2s ease;
  border-radius: 5px;
 }

.logout-button:hover {
  background-color: #37730C;
  color: white;
  border-radius: 5px;
}
  
.card-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}
  
.card {
  background-color: #98BD5D;
  color: white;
  border: none;
  padding: 1em;
  margin-bottom: 1.5em;
  cursor: pointer;
  transition: background-color 0.2s ease;
  font-size: 24px;
  width: 100%;
  max-width: 400px;
  text-align: center;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  margin: 1em;
}
  
.card:hover {
  background-color: #37730C;
  color: white;
}
</style>