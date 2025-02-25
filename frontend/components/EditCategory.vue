// Edit Category page

<template>
    <div class="edit-item">
        <header class="navigation">
            <a href="/home" class="home-link">Home Page</a>
            <div class="title">
                <h1>Edit Category Item</h1>
            </div>
            <div class="avatar">
                <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
                <button @click="logout" class="logout-button">Logout</button>
            </div>
        </header>
        <div class="category-name">
            <label for="category-name">Category Name</label>
            <input id="category-name" autocomplete="off" type="text" v-model="categoryName">
        </div>
        <div class="description">
            <label for="description">Description</label>
            <input id="description" autocomplete="off" type="text" v-model="description">
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

export default {
    name: 'EditCategory',
    data() {
        return {
            categoryId: '', // ID of the category item to edit
            categoryName: '',// Separate property for Category Name
            description: '', // Separate property for Type of Category
            errorMessage: '', // Error Message
        };
    },
    methods: {
        fetchData() {
            // Fetch data of the selected Category item from API and populate the form fields
            axios.get(`http://127.0.0.1:8000/Category/${this.categoryId}`)
                .then(response => {
                    const { name, description } = response.data;
                    this.categoryName = name;
                    this.description = description;
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    this.errorMessage = 'Failed to fetch data. Please try again!';
                });
        },
        updateItem() {
            // Update the category item with the new data
            axios.put(`http://127.0.0.1:8000/Category/${this.categoryId}`, {
                name: this.categoryName,
                description: this.description
            })
                .then(response => {
                    console.log('Item updated!', response.data);
                    // when item updated successfully
                })
                .catch(error => {
                    console.error('Error updating item.', error);
                    // when item cannot be updated
                    this.errorMessage = 'Failed to update item. Please try again!';
                });
        }
    },
    created() {
        // Fetch data when the component is created
        this.fetchData();
    },
    mounted() {
        // Get category item ID from route params or props
        this.categoryId = this.$route.params.categoryId; // using Vue Router
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

.category-name {
    margin-bottom: 1em;
    margin-top: 5em;
}

.description {
    margin-bottom: 1em;
}

label {
    display: block;
    margin-left: 2em;
}

input {
    width: 80%;
    padding: 0.5em;
    margin: 0 auto;
    font-size: 1em;
    margin-left: 2em;
}

.form-item {
    margin: 1em 0;
}

button {
    background-color: #89b93c;    /* Green color */
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
    background-color: #37730c;    /* Dark green color on hover */
}

.error-notification {
    position: fixed;
    bottom: 50px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #ff4444;    /* error in red */
    color: white;
    font-size: 1em;
    padding: 10px 20px;
    border-radius: 5px;
    z-index: 999;    /* above other content */
}
</style>
