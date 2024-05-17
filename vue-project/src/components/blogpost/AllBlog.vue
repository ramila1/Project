<!-- <template>
    <div>
      <h1>All Blogs</h1>
      <div v-for="blog in blogs" :key="blog.id" class="blog">
        <h2>{{ blog.title }}</h2>
        <p>{{ blog.description }}</p>
        <p>Author: {{ blog.author }}</p>
        <p>Published Date: {{ blog.published_date }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const blogs = ref([]);
  
  const fetchBlogs = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/all-blogs/');
      blogs.value = response.data;
    } catch (error) {
      console.error('Error fetching blogs:', error);
    }
  };
  
  onMounted(fetchBlogs);
  </script>
  
  <style scoped>
  .blog {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
  }
  </style>
   -->