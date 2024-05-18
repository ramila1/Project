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

    <div v-if="showEditModal" class="modal-overlay">
      <div class="modal">
        <EditUser :userId="currentUserId" @close="closeEditModal" @user-updated="updateUserList" />
      </div>
    </div>

    <h2 class="section-title">Deleted Users</h2>
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
    <tr v-for="deletedUser in deletedUsers" :key="deletedUser.id">
      <td>{{ deletedUser.email }}</td>
      <td>{{ deletedUser.phone }}</td>
      <td>{{ deletedUser.address }}</td>
      <td>{{ deletedUser.gender }}</td>
      <td>{{ deletedUser.age }}</td>
      <td>
        <button @click="restoreUser(deletedUser.id)" class="edit-user">Restore</button>
        <button @click="deleteUserPermanently(deletedUser.id)" class="delete-user">Delete</button>
      </td>
    </tr>
  </tbody>
</table>

    <router-view></router-view>
  </div>
</template>
<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { useStore } from 'vuex';
import EditUser from './EditForm.vue';
import './../../assets/main.css';

export default {
  name: 'UserList',
  components: {
    EditUser,
  },
  setup() {
    const toast = useToast();
    const router = useRouter();
    const store = useStore();
    const users = ref([]);
    const deletedUsers = ref([]);
    const showEditModal = ref(false);
    const showDeleteConfirmation = ref(false);
    const currentUserId = ref(null);
    let currentUserToDelete = null;

    const goToAddUser = () => {
      router.push('/create-user');
    };

    const editUser = (id) => {
      currentUserId.value = id;
      showEditModal.value = true;
    };

    const closeEditModal = () => {
      showEditModal.value = false;
    };

    const getUsers = () => {
      axios
        .get('http://127.0.0.1:8000/api/users/')
        .then((response) => {
          users.value = response.data.filter((user) => !user.is_deleted);
          deletedUsers.value = response.data.filter((user) => user.is_deleted);
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const deleteUserConfirmed = () => {
      const userToDelete = users.value.find((user) => user.id === currentUserToDelete);
      if (userToDelete) {
        axios
          .delete(`http://127.0.0.1:8000/api/users/${userToDelete.id}/`)
          .then(() => {
            toast.success('User is successfully deleted');
            getUsers();
            showDeleteConfirmation.value = false;
          })
          .catch((error) => {
            console.log(error);
          });
      }
    };

    const deleteUser = (id) => {
      currentUserToDelete = id;
      showDeleteConfirmation.value = true;
    };

    const cancelDelete = () => {
      showDeleteConfirmation.value = false;
    };

    const updateUserList = (updatedUser) => {
      const index = users.value.findIndex((user) => user.id === updatedUser.id);
      if (index !== -1) {
        users.value.splice(index, 1, updatedUser);
      }
      showEditModal.value = false;
    };

    const restoreUser = (id) => {
      axios
        .patch(`http://127.0.0.1:8000/api/users/${id}/restore/`)
        .then(() => {
          toast.success('User restored successfully');
          getUsers();
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const deleteUserPermanently = (id) => {
      const userToDelete = deletedUsers.value.find((user) => user.id === id);
      if (userToDelete) {
        axios
          .delete(`http://127.0.0.1:8000/api/users/${userToDelete.id}/`)
          .then(() => {
            toast.success('User permanently deleted');
            getUsers();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    };

    const filteredUsers = computed(() => {
      return users.value;
    });

    onMounted(() => {
      getUsers();
    });

    return {
      users,
      deletedUsers,
      showDeleteConfirmation,
      showEditModal,
      currentUserId,
      getUsers,
      goToAddUser,
      editUser,
      deleteUser,
      deleteUserConfirmed,
      cancelDelete,
      closeEditModal,
      updateUserList,
      restoreUser,
      deleteUserPermanently,
      filteredUsers,
      toast,
    };
  },
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

.add-user,
.edit-user,
.delete-user {
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
  margin-left: 10px;
  margin-right: 10px;
}

.delete-user {
  background-color: #dc3545;
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
</style>
