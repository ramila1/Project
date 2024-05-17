<template>
  <div class="container">
  <h2>User Form</h2>

  <div class="users-list">
    <h2>List of Users</h2>
    <button @click="goToAddUser">Add</button>

    
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

</div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'CreateUser',
setup() {
  const router = useRouter(); // Initialize Vue Router
    
    // Your existing code...

    const goToAddUser = () => {
      router.push('/create-user'); // Navigate to the create user page
    };

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
  cancelDelete,
  goToAddUser
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









