// Task list page

<template>
    <div>
        <header class="navigation">
            <a href="/" class="home-link">Home Page</a>
            <div class="title">
                <h1>Task List</h1>
            </div>
            <div class="avatar">
                <img src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=" alt="User Avatar">
                <button @click="logout" class="logout-button">Logout</button>
            </div>
        </header>
        <div class="grid-container">
            <div v-for="item in items" :key="item.task" class="item-tile" @click="navigateToEquipment(item.task)">
                {{ item.task }}
            </div>
        </div>
        <div class="buttons">
            <button @click="navigateToAddTask" class="add-item-btn">Add Item</button>
            <button @click="navigateToEditTask" class="edit-item-btn">Edit Item</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [] // Initialize items as an empty array
        };
    },
    methods: {
        navigateToAddTask() {  
            // redirect to the 'add task' page here
            // new item is added to the backend and then fetched
            fetch('/api/addTaskItems', {
                method: 'POST', // use POST method to add new items
                body: JSON.stringify({ task: 'New Task Item' }), // Replace with actual item data
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                // Fetch the updated list of items from the backend
                fetch('/api/taskItems')
                    .then(response => response.json())
                    .then(data => {
                        // Update the items array with the fetched data
                        this.items = data.items;
                    })
                    .catch(error => {
                        console.error('Error fetching items:', error);
                    });
            })
            .catch(error => {
                console.error('Error adding item:', error);
            });
        },
        navigateToEditTask(taskItems) {
            // Navigate to the edit task page and pass the task item as a parameter
            this.$router.push({ path: '/edit-task', query: { taskItems } });
            console.log("Edit Item clicked");
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
    position: absolute;
    bottom: 20px;
    left: 20px;    
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

.grid-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 2em;
    margin-top: 5em;
}

.item-tile {
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
    transition: background-color 0.2s ease;
}

.item-tile:hover {
    background-color: #ccc;
}
</style>