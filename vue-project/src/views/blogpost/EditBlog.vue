<!-- <template>
    <div v-if="blog">
      <h2 class="section-title">Edit Blog</h2>
      <form @submit.prevent="updateBlog">
        <div class="form-group">
          <label for="title">Title</label>
          <input type="text" v-model="title" id="title" required />
        </div>
        <div class="form-group">
          <label for="description">Description</label>
          <textarea v-model="description" id="description" required></textarea>
        </div>
        <button type="submit" class="edit-blog">Update Blog</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRoute, useRouter } from 'vue-router';
  
  export default {
    name: 'EditBlog',
    setup() {
      const route = useRoute();
      const router = useRouter();
      const blog = ref(null);
      const title = ref('');
      const description = ref('');
  
      const getBlog = () => {
        const blogId = route.params.id;
        axios.get(`http://127.0.0.1:8000/api/blog/${blogId}/`)
          .then(response => {
            blog.value = response.data;
            title.value = blog.value.title;
            description.value = blog.value.description;
          })
          .catch(error => {
            console.log(error);
          });
      };
  
      const updateBlog = () => {
        const blogId = route.params.id;
        axios.put(`http://127.0.0.1:8000/api/blog/${blogId}/`, {
          title: title.value,
          description: description.value,
        })
        .then(() => {
          router.push('/my-blogs');
        })
        .catch(error => {
          console.log(error);
        });
      };
  
      onMounted(() => {
        getBlog();
      });
  
      return {
        blog,
        title,
        description,
        updateBlog,
      };
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
  
  .edit-blog {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  </style>
   -->