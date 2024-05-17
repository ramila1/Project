<template>
<div class="container">
    <h2>Users Form</h2>
    <UserList :users="users" :editBtn="editBtn" :deleteUser="deleteUser" />
    <EditUser v-if="Object.keys(currentUser).length !== 0" :currentUser="currentUser" :updateUser="updateUser" />
    <CreateUser v-else :newUser="newUser" :saveUser="saveUser" />
</div>

  </template>
  
  <script>
  import { ref, reactive, onMounted } from 'vue';
  import axios from 'axios';
  import UserList from './UserList.vue';

  import EditUser from './EditForm.vue';
  import CreateUser from './ListUser.vue';
  
  export default {
    components: {
      ListUsers,
      EditUser,
      CreateUser
    },
    setup() {
      // Your existing setup logic
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
</style>


  