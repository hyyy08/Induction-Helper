<template>
  
  <header class="navigation">
      <a href="/home" class="home-link">Home Page</a>
      <div class="avatar">
        <button class="logout-button" @click="logout">Logout</button>
      </div>
  </header>
  
  
  <div class="new-student-container">
    <h1>Add New Student</h1>
    
      <label class="file-label">
        <input type="file" @change="onFileChange" accept="image/*" capture="camera">
        <span>Browse...</span>
      </label>
      
      <button class="process-button" @click="processImage">Process Image</button>
    
    <div>
      <label class ="form-labels">
        <label>First Name</label>
        <input v-model="firstName" type="text">
        <label>Last Name</label>
        <input v-model="lastName" type="text">
        <label>Student Number</label>
        <input v-model="studentNumber" type="text">
        <label>Email</label>
        <input v-model="email" type="email">
        <button class="submit-button" @click="submitData" :disabled="!isFormValid">Submit</button>
        <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p>
      </label>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import imageCompression from 'browser-image-compression';

export default {
  data() {
    return {
      file: null,
      ocrResult: null,
      firstName: '',
      lastName: '',
      studentNumber: '',
      email: '',
      errorMessage: ''
    };
  },
  computed: {
    baseUrl() {
      return window.location.hostname === '127.0.0.1' ? 'http://127.0.0.1:8000' : 'http://192.168.1.16:8000';
    },
    isFormValid() {
      return this.firstName && this.lastName && this.studentNumber && this.email;
    }
  },
  methods: {
    async onFileChange(e) {
      const file = e.target.files[0];
      if (file) {
        try {
          const options = {
            maxSizeMB: 1,
            maxWidthOrHeight: 1024,
            useWebWorker: true
          };
          const compressedFile = await imageCompression(file, options);
          this.file = compressedFile;
        } catch (error) {
          console.error('Error compressing image:', error);
          alert('There was an error compressing the image.');
        }
      }
    },
    async processImage() {
      if (!this.file) {
        alert('Please upload or capture an image.');
        return;
      }
      const formData = new FormData();
      formData.append('image', this.file);

      try {
        const response = await axios.post(`${this.baseUrl}/ocr/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.ocrResult = response.data;
        this.firstName = this.ocrResult.firstName;
        this.lastName = this.ocrResult.lastName;
        this.studentNumber = this.ocrResult.studentNumber;
        this.email = `${this.studentNumber}@student.curtin.edu.au`;
        this.errorMessage = '';  // Reset error message
      } catch (error) {
        console.error('Error processing image:', error);
        alert('There was an error processing the image.');
      }
    },
    async submitData() {
      const userData = {
        userID: this.studentNumber,
        email: this.email,
        firstName: this.firstName,
        lastName: this.lastName
      };

      try {
        const response = await axios.post(`${this.baseUrl}/databaseUser/create/`, userData);
        alert('User created successfully!');
        this.errorMessage = '';  // Reset error message
      } catch (error) {
        if (error.response && error.response.data && error.response.data.error) {
          this.errorMessage = error.response.data.error;
        } else {
          console.error('Error submitting data:', error);
          alert('There was an error submitting the data.');
        }
      }
    }
  }
};
</script>

<style scoped>

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #B8CFB0;
  font-size: 16px;
  height: 5em;
}


.new-student-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

h1 {
  text-align: center;
  margin-bottom: 2rem;
}

.file-label {
  position: relative;
  display: inline-block;
  padding: 1rem;
  background-color: #5cb85c;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.file-label input[type="file"] {
  position: absolute;
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  z-index: -1;
}

.file-label span {
  font-size: 1rem;
}

.form-label {
  align-items: center;
  font-weight: bold;
  margin-bottom: .5rem;
}

input {
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  width: 100%;
  box-sizing: border-box;
  margin-bottom: 1.5rem; /* Added margin to increase the gap between fields */
}

.process-button {
  background-color: #5cb85c;
  align-self: center;
}

button {
  padding: 1rem;
  background-color: #5cb85c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #4cae4c;
}

button:disabled {
  background-color: #d3d3d3;
  cursor: not-allowed;
}

.submit-button {
  align-self: center;
  max-width: 200px;
  margin: 2rem auto 0;
  display: block;
}

/* Additional responsive adjustments */
@media (max-width: 768px) {
  .new-student-container {
    padding: 1rem;
  }
}
</style>