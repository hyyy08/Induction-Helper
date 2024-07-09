// report 

<template>
    <div class="reporting-page">
      <header class="reporting-header">
        <a href="/home" class="home-link">Home Page</a>
        <div class="header-right">
          <img class="user-icon" @click="goToProfile" src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
          <button class="logout-button">Logout</button>
        </div>
      </header>
      <div class="content">
        <button class="download-button" @click="downloadCSV">Download CSV</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    methods: {
      goToProfile() {
      this.$router.push('/profile');
      },
      downloadCSV() {
        axios({
        url: 'http://127.0.0.1:8000/export_induction_to_csv/',
        method: 'GET',
        responseType: 'blob', // important for file download
      })
      .then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'inductions.csv');
        document.body.appendChild(link);
        link.click();
      })
      .catch((error) => {
        console.error('Error downloading CSV:', error);
      });
      }
    }
  };
  </script>
  
<style scoped>
.reporting-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #ffffff;
}
 
.reporting-header {
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
  
.header-right {
  display: flex;
  align-items: center;
}
  
.user-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 1rem;
}
  
.logout-button {
  padding: 0.5rem 1rem;
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 1em;
  border-radius: 5px;
  transition: background-color 0.2s ease;
}

.logout-button:hover {
  color: white;
  background-color: #37730C;
  border-radius: 5px;
}
  
.content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
  
.download-button {
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
  height: 50px;
  width: 200px;
}
  
.download-button:hover {
  background-color: #37730C;
  color: white;
}
</style>