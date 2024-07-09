// profile

<template>
    <div class="profile-page">
      <header class="profile-header">
        <a href="/" class="home-link">Home Page</a>
        <div class="user-actions">
          <img class="user-icon" src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
          <button class="logout-button" @click="logout">Logout</button>
        </div>
      </header>
      <div class="content">
        <ul class="details-list">
          <li v-for="(value, key) in user" :key="key" class="detail-item">
            <label :for="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }}:</label>
            <input v-if="editMode[key]" type="text" :id="key" v-model="tempDetails[key]" @keyup.enter="save(key)">
            <span v-else>{{ value }}</span>
            <button v-if="!editMode[key]" @click="edit(key)">Change</button>
            <button v-if="editMode[key]" @click="save(key)">Save</button>
            <button v-if="editMode[key]" @click="cancelEdit(key)">Cancel</button>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          email: 'example@example.com',
          firstName: 'John',
          lastName: 'Doe'
        },
        editMode: {
          email: false,
          firstName: false,
          lastName: false
        },
        tempDetails: {}
      };
    },
    methods: {
      logout() {
        // Logic to handle logout
      },
      edit(key) {
        this.tempDetails[key] = this.user[key];
        this.editMode[key] = true;
      },
      save(key) {
        this.user[key] = this.tempDetails[key];
        this.editMode[key] = false;
        // Here you would add logic to update the user detail on the server
      },
      cancelEdit(key) {
        this.editMode[key] = false;
      }
    }
  };
  </script>
  
<style scoped>
.profile-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #ffffff;
}
  
.profile-header {
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
  font-weight: bold;
  font-size: 24px;
}
  
.user-actions {
  display: flex;
  align-items: center;
}

.user-icon {
  width:50px;  
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
  
.content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  transition: background-color 0.2s ease;
}
  
.details-list {
  list-style: none;
  padding: 0;
}
  
.detail-item {
  margin: 10px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1em;
}
  
button {
  margin-left: 20px;
  padding: 5px 10px;
  background-color: #98BD5D;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-bottom: 10px;
  transition: background-color 0.2s ease;
  height: 40px;
}
  
button:hover {
  background-color: #37730C;
  color: white;
}
</style>