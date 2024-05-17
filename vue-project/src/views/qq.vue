<template>
    <div class="container">
      <h2>User Form</h2>
    
      <div class="users-list">
        <h2>List of Users</h2>
        
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Phone</th>
              <th>Address</th>
              <th>Gender</th>
              <th>Age</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{ user.email }}</td>
              <td>{{ user.phone }}</td>
              <td>{{ user.address }}</td>
              <td>{{ user.gender }}</td>
              <td>{{ user.age }}</td>
              <td>
                <button @click="editBtn(user.id)">Edit</button>
                <button @click="deleteUser(user.id)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
  
      
      <div v-if="showDeleteConfirmation" class="modal-overlay">
        <div class="modal">
          <p>Are you sure you want to delete this user?</p>
          <div class="modal-buttons">
            <button @click="deleteUserConfirmed">Yes</button>
            <button @click="cancelDelete">No</button>
          </div>
        </div>
      </div>
  
      <div v-if="Object.keys(currentUser).length !== 0" class="edit-form">
        <h2>Edit User Details</h2>
        <form @submit.prevent="updateUser(currentUser.id)">
          <div class="form-group">
            <label>Email</label>
            <input type="email" v-model="currentUser.email" />
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="number" v-model="currentUser.phone" />
          </div>
          <div class="form-group">
            <label>Address</label>
            <input type="text" v-model="currentUser.address" />
          </div>
          <div class="form-group">
            <label>Gender</label>
            <input type="text" v-model="currentUser.gender" />
          </div>
          <div class="form-group">
            <label>Age</label>
            <input type="number" v-model="currentUser.age" />
          </div>
          <button type="submit">Update</button>
        </form>
      </div>
  
      <div v-else class="create-form">
        <h2>Create A New User</h2>
        <form @submit.prevent="saveUser()">
          <div class="form-group">
            <label>Email</label>
            <input type="email" v-model="newUser.email" />
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="number" v-model="newUser.phone" />
          </div>
          <div class="form-group">
            <label>Address</label>
            <input type="text" v-model="newUser.address" />
          </div>
          <div class="form-group">
            <label>Gender</label>
            <input type="text" v-model="newUser.gender" />
          </div>
          <div class="form-group">
            <label>Age</label>
            <input type="number" v-model="newUser.age" />
          </div>
          <button type="submit">Save</button>
        </form>
      </div>
  
      <div v-if="showDeleteConfirmation" class="modal-overlay">
        <div class="modal">
          <p>Are you sure you want to delete this user?</p>
          <div class="modal-buttons">
            <button @click="deleteUserConfirmed">Yes</button>
            <button @click="cancelDelete">No</button>
          </div>
        </div>
      </div>
  </div>
  </template>
  
  <script>
  import { ref, reactive, onMounted } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const users = ref([]);
      const currentUser = reactive({});
      const api = "http://127.0.0.1:8000/api/users/";
  
      const newUser = reactive({
        email: '',
        phone: '',
        address: '',
        gender: '',
        age: ''
      });
  
      const showDeleteConfirmation = ref(false);
      let currentUserToDelete = null;
  
      const getUsers = () => {
        axios.get(api)
          .then(response => {
            users.value = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      };
  
      const saveUser = () => {
        axios.post(api, newUser)
          .then(response => {
            getUsers();
            resetNewUser();
          })
          .catch(error => {
            console.log(error);
          });
      };
  
      const editBtn = (id) => {
        const user = users.value.find(s => s.id === id);
        if (user) {
          currentUser.id = user.id;
          currentUser.email = user.email;
          currentUser.phone = user.phone;
          currentUser.address = user.address;
          currentUser.gender = user.gender;
          currentUser.age = user.age;
        }
      };
  
      const updateUser = (id) => {
        axios.put(api + id + '/', currentUser)
          .then(response => {
            getUsers();
            resetCurrentUser();
          })
          .catch(error => {
            console.log(error);
          });
      };
  
      const deleteUser = (id) => {
        // Instead of directly deleting, show the confirmation modal
        currentUserToDelete = id;
        showDeleteConfirmation.value = true;
      };
  
      const deleteUserConfirmed = () => {
        axios.delete(api + currentUserToDelete + '/')
          .then(response => {
            getUsers();
            showDeleteConfirmation.value = false;
          })
          .catch(error => {
            console.log(error);
          });
      };
  
      const cancelDelete = () => {
        // Cancel deletion and hide the confirmation modal
        showDeleteConfirmation.value = false;
      };
  
      const resetNewUser = () => {
        newUser.email = '';
        newUser.phone = '';
        newUser.address = '';
        newUser.gender = '';
        newUser.age = '';
      };
  
      const resetCurrentUser = () => {
        currentUser.id = '';
        currentUser.email = '';
        currentUser.phone = '';
        currentUser.address = '';
        currentUser.gender = '';
        currentUser.age = '';
      };
  
      onMounted(() => {
        getUsers();
      });
  
      return {
        users,
        currentUser,
        newUser,
        showDeleteConfirmation,
        getUsers,
        saveUser,
        editBtn,
        updateUser,
        deleteUser,
        deleteUserConfirmed,
        cancelDelete
      };
    }
  };
  </script>
  
  
  <style scoped>
  .container {
    margin: 20px auto;
    padding: 20px;
    width: 80%;
    max-width: 800px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .users-list {
    margin-bottom: 20px;
  }
  
  .users-list table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .users-list th,
  .users-list td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .users-list th {
    background-color: #f2f2f2;
  }
  
  .edit-form,
  .create-form {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fff;
  }
  
  .edit-form h2,
  .create-form h2 {
    margin-bottom: 10px;
  }
  
  .form-group {
    margin-bottom: 10px;
  }
  .users-list h2{
    text-align: center;
  }
  .container h2{
    text-align: center;
    text-decoration: underline;
    
  }
  
  .form-group input[type="text"],
  .form-group input[type="number"],
  .form-group input[type="email"] {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }
  
  .modal p {
    margin-bottom: 20px;
  }
  
  .modal-buttons {
    display: flex;
    justify-content: center;
  }
  
  .modal-buttons button {
    margin: 0 10px;
  }
  
  </style>
  
  
  
  
  
  
  