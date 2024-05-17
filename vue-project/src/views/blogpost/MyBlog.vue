<template>
  <div>
    <h1>My Blogs</h1>
    <div v-for="blog in myBlogs" :key="blog.id" class="blog">
      <h2>{{ blog.title }}</h2>
      <p>{{ blog.description }}</p>
      <p>Published Date: {{ blog.published_date }}</p>
      <div>
        <button @click="editBlog(blog)">Edit</button>
        <button @click="confirmDelete(blog)">Delete</button>
      </div>
    </div>
    <div v-if="editMode">
      <h2>Edit Blog</h2>
      <form @submit.prevent="updateBlog">
        <div class="form-group">
          <label for="edit-title">Title</label>
          <input type="text" v-model="editForm.title" id="edit-title" required />
        </div>
        <div class="form-group">
          <label for="edit-description">Description</label>
          <textarea v-model="editForm.description" id="edit-description" required></textarea>
        </div>
        <button type="submit">Update Blog</button>
        <button @click="cancelEdit">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';

const myBlogs = ref([]);
const user = JSON.parse(localStorage.getItem('user'));
const editForm = ref({
  id: null,
  title: '',
  description: ''
});
const editMode = ref(false);
const store = useStore(); 

const fetchMyBlogs = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/user-blogs/${user.user_id}/`);
    myBlogs.value = response.data;
  } catch (error) {
    console.error('Error fetching user blogs:', error);
  }
};

onMounted(fetchMyBlogs);

const editBlog = (blog) => {
  editForm.value.id = blog.id;
  editForm.value.title = blog.title;
  editForm.value.description = blog.description;
  editMode.value = true;
};

const updateBlog = async () => {
  try {
    const response = await axios.patch(`http://127.0.0.1:8000/api/blog/${editForm.value.id}/`, {
      title: editForm.value.title,
      description: editForm.value.description,
    });
    const updatedBlogIndex = myBlogs.value.findIndex(blog => blog.id === editForm.value.id);
    if (updatedBlogIndex !== -1) {
      myBlogs.value[updatedBlogIndex] = response.data;
    }
    editMode.value = false;
  } catch (error) {
    console.error('Error updating blog:', error);
  }
};

const cancelEdit = () => {
  editForm.value.id = null;
  editForm.value.title = '';
  editForm.value.description = '';
  editMode.value = false;
};

const confirmDelete = async (blog) => {
  const confirmDelete = confirm(`Are you sure you want to delete the blog "${blog.title}"?`);
  if (confirmDelete) {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/blog/${blog.id}/`);
      myBlogs.value = myBlogs.value.filter(item => item.id !== blog.id);
      store.dispatch('notifySuccess', 'Blog deleted successfully');
    } catch (error) {
      console.error('Error deleting blog:', error);
      store.dispatch('notifyError', 'Failed to delete blog');
    }
  }
};
</script>

<style scoped>
.blog {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px 0;
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
