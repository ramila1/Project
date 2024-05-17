<template>
    <div class="container">
      <h2>Users Form</h2>
      <div class="users-list">
        <div class="add-button">
        <h2>List of Users</h2>
        <button @click="showCreateForm = true">Add</button>
        </div>
        <br>
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
        <div v-if="Object.keys(currentStudent).length !== 0" class="edit-form">
      <h2>Edit Student Details</h2>
      <form @submit.prevent="updateStudent(currentStudent.id)">
        <div class="form-group">
          <label>Email</label>
          <input type="email" v-model="currentStudent.email" />
        </div>
        <div class="form-group">
          <label>Phone</label>
          <input type="number" v-model="currentStudent.phone" />
        </div>
        <div class="form-group">
          <label>Address</label>
          <input type="text" v-model="currentStudent.address" />
        </div>
        <div class="form-group">
          <label>Gender</label>
          <input type="text" v-model="currentStudent.gender" />
        </div>
        <div class="form-group">
          <label>Age</label>
          <input type="number" v-model="currentStudent.age" />
        </div>
        <button type="submit">Update</button>
      </form>
    </div>

    <div v-if="showCreateForm" class="create-form">
        
      <h2>Create A New Student</h2>
      <form @submit.prevent="saveStudent()">
        <div class="form-group">
          <label>Email</label>
          <input type="email" v-model="newStudent.email" />
        </div>
        <div class="form-group">
          <label>Phone</label>
          <input type="number" v-model="newStudent.phone" />
        </div>
        <div class="form-group">
          <label>Address</label>
          <input type="text" v-model="newStudent.address" />
        </div>
        <div class="form-group">
          <label>Gender</label>
          <input type="text" v-model="newStudent.gender" />
        </div>
        <div class="form-group">
          <label>Age</label>
          <input type="number" v-model="newStudent.age" />
        </div>
        <button type="submit">Save</button>
      </form>
    </div>
  </div>
</template>
    
        <div v-if="showCreateForm" class="create-form">
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
    
        
        const selectedUser = reactive({});
        const showCreateForm = ref(false);
        const showEditForm = ref(false);
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
              clearNewUser();
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
              clearCurrentUser();
            })
            .catch(error => {
              console.log(error);
            });
        };
    
        const deleteUser = (id) => {
          axios.delete(api + id + '/')
            .then(response => {
              getUsers();
            })
            .catch(error => {
              console.log(error);
            });
        };
    
        const clearNewUser = () => {
          newUser.email = '';
          newUser.phone = '';
          newUser.address = '';
          newUser.gender = '';
          newUser.age = '';
        };
    
        const clearCurrentUser = () => {
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
          showCreateForm,
          getUsers,
          saveUser,
          editBtn,
          updateUser,
          deleteUser
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
    .users-list h2{
      text-align: center;
    }
    
    .users-list th {
      background-color: #f2f2f2;
    }
    
    .add-button button{
      margin-left: 750px;
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
    
    .form-group label {
      display: block;
      margin-bottom: 5px;
    }
    
    .form-group input[type="text"],
    .form-group input[type="number"],
    .form-group input[type="email"] {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    
    .form-group input[type="text"]:focus,
    .form-group input[type="number"]:focus,
    .form-group input[type="email"]:focus {
      outline: none;
      border-color: #007bff;
    }
    
    .form-group button {
      padding: 8px 16px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .form-group button:hover {
      background-color: #0056b3;
    }
    </style>
    





<template>
  <div class="container">
    <header class="header">
      <h1 class="header-title">Admin Dashboard</h1>
      <button @click="goToAddUser" class="add-user">Add User</button>
    </header>
    <div class="users-list">
      <h2 class="section-title">List of Users</h2>

      <table class="table">
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
          <tr v-for="user in filteredUsers" :key="user.id">
            <td>{{ user.email }}</td>
            <td>{{ user.phone }}</td>
            <td>{{ user.address }}</td>
            <td>{{ user.gender }}</td>
            <td>{{ user.age }}</td>
            <td>

      <button @click="editUser(user.id)" class="edit-user">Edit</button>
      <button @click="deleteUser(user.id)" class="delete-user">Delete</button>


            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showDeleteConfirmation" class="modal-overlay">
      <div class="modal">
        <p>Are you sure you want to delete this user?</p>
        <div class="modal-buttons">
          <button @click="deleteUserConfirmed" class="delete-user">Yes</button>
          <button @click="cancelDelete" class="edit-user">No</button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useToast } from "vue-toastification";

export default {
  name: 'UserList',

  setup() {
    const toast = useToast();
    const router = useRouter();
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

    const goToAddUser = () => {
      router.push('/create-user');
    };

    const editUser = (id) => {
      router.push({ name: 'EditUser', params: { userId: id } });
    };

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

    const deleteUserConfirmed = () => {
      const userToDelete = users.value.find(user => user.id === currentUserToDelete);
      if (userToDelete) {
        userToDelete.deleted = true;
        let deletedUsers = JSON.parse(localStorage.getItem('deletedUsers')) || [];
        deletedUsers.push(userToDelete.id);
        localStorage.setItem('deletedUsers', JSON.stringify(deletedUsers));
        showDeleteConfirmation.value = false;
        const $toast = useToast();
        let instance = $toast.success('User is successfully deleted');
        router.push({ name: 'UserList' }); 
        instance.dismiss();
        $toast.clear();
      }
    };

    const deleteUser = (id) => {
      currentUserToDelete = id;
      showDeleteConfirmation.value = true;
    };

    const cancelDelete = () => {
      showDeleteConfirmation.value = false;
    };


    const filteredUsers = computed(() => {
      let deletedUsers = JSON.parse(localStorage.getItem('deletedUsers')) || [];
      return users.value.filter(user => !user.deleted && !deletedUsers.includes(user.id));
    });

    const deletedUsers = computed(() => {
      let deletedUsers = JSON.parse(localStorage.getItem('deletedUsers')) || [];
      return users.value.filter(user => user.deleted && deletedUsers.includes(user.id));
    });

    onMounted(() => {
      getUsers();
    });

    return {
      users,
      newUser,
      showDeleteConfirmation,
      getUsers,
      goToAddUser,
      editUser,
      deleteUser,
      deleteUserConfirmed,
      cancelDelete,
      filteredUsers,
      deletedUsers,
      toast
    };
  }
};
</script>

<style scoped>
.container {
  margin: 20px auto;
  padding: 20px;
  max-width: 900px; 
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.header-title {
  color: #333;
  font-size: 28px; 
}

.section-title {
  color: #666;
  margin-bottom: 20px; 
  font-size: 20px; 
}

.table {
  width: 100%;
  border-collapse: collapse;
}

.table th {
  padding: 16px 12px; 
  border-bottom: 1px solid #ddd;
}

.table td {
  padding: 16px; 
  border-bottom: 1px solid #ddd;
}

.table th {
  background-color: #f2f2f2;
}



.add-user {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px; 
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px; 
}

.edit-user {
  background-color: #6c757d;
  color: #fff;
  padding: 10px 20px; 
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px; 
  margin-left: 10px;
  margin-right: 10px;
}

.delete-user {
  background-color: #dc3545;
  color: #fff;
  padding: 10px 20px; 
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px; 
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
  padding: 24px; 
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

.toast {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #64f1af;
  color: #fff;
  padding: 12px 24px; 
  border-radius: 4px;
  z-index: 999;
}
</style>