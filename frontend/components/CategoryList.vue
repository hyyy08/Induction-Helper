<template>
    <div>
        <header class="navigation">
            <a href="/home" class="home-link">Home Page</a>
            <div class="title">
                <h1>Category List</h1>
            </div>
            <div class="avatar">
                <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
                <button @click="logout" class="logout-button">Logout</button>
            </div>
        </header>
        <div class="category-list">
            <div v-for="category in categories" :key="category.category" class="item-tile">
                <div class="category-info">
                    <h3>Category Name</h3>
                    <p>{{ category.category }}</p>
                </div>
                <div class="category-info">
                    <h3>Category Description</h3>
                    <p>{{ category.categoryDescription }}</p>
                </div>
            </div>
        </div>
        <div class="buttons">
            <button @click="navigateToAddCategory" class="add-item-btn">Add Category</button>
            <button @click="navigateToEditCategory" class="edit-item-btn">Edit Category</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            categories: [] // Initialize items as an empty array
        };
    },
    created() {
        this.fetchItems();
    },
    methods: {
        fetchItems() {
            axios.get('http://127.0.0.1:8000/Category/')
                .then(response => {
                    this.categories = response.data;
                })
                .catch(error => {
                    console.error('Error fetching category:', error);
                });
        },
        navigateToAddCategory() {
            this.$router.push('/addCategory');
        },
        navigateToEditCategory() {
            this.$router.push('/editCategory');
        },
        logout() {
            // Implement your logout logic here
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

.buttons {
    margin: 2em; 
}

.add-item-btn,
.edit-item-btn {
    margin-right: 10px;
    font-size: 1em;
    background-color: #98bd5d; /* Light green */
    border: none;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.add-item-btn:hover,
.edit-item-btn:hover {
    background-color: #37730C; /* Darker shade of green on hover */
}

.category-list {
    display: flex;
    flex-direction: column;
    gap: 10px; /* Adds space between items */
    margin: 2em 0;
}

.item-tile {
    border: 1px solid #ccc;
    padding: 5px;
    border-radius: 5px;
    transition: background-color 0.2s ease;
}

.item-tile:hover {
    background-color: #ccc;
}

.category-info {
    margin-bottom: 10px;
}

.category-info h3 {
    margin: 0;
    font-size: 1em;
    color: #37730C;
}

.category-info p {
    margin: 0;
    font-size: 0.9em;
    color: #333;
}
</style>
