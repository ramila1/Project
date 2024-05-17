<template>
  <div>
    <h2 class="section-title">Add New Blog</h2>
    <form @submit.prevent="addBlog">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" v-model="title" id="title" required />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea v-model="description" id="description" required></textarea>
      </div>
      <button type="submit" class="add-blog">Add Blog</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const title = ref('');
const description = ref('');
const store = useStore(); 

const user = JSON.parse(localStorage.getItem('user'));
const router = useRouter(); 

const addBlog = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/api/blog/", {
      title: title.value,
      description: description.value,
      author: user.user_id, 
    });
    title.value = '';
    description.value = '';
    store.dispatch('notifySuccess', 'Blog added successfully');
    router.push('/blog_landing'); 
  } catch (error) {
    console.error('Error adding blog:', error);
    store.dispatch('notifyError', 'Failed to add blog');
  }
};
</script>

<style scoped>
.section-title {
  color: #666;
  margin-bottom: 20px;
  font-size: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.add-blog {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}
</style>
