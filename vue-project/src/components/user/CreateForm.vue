I will provide you two code Signup and login code so make a refresh token and access token so write the code that is needed:
<template>
  <div class="container">
    <div class="create-form">
      <h2>Create A New User</h2>
      <form @submit.prevent="saveUser()">
        <div class="form-group">
          <label>Email</label>
          <input type="text" v-model="newUser.email" />
          <span v-if="!isValidEmail" class="warning">{{ emailWarning }}</span>
        </div>
        <div class="form-group">
          <label>Password</label>
          <input type="password" v-model="newUser.password" />
          <span v-if="passwordWarning" class="warning">{{ passwordWarning }}</span>
        </div>
        <div class="form-group">
          <label>Confirm Password</label>
          <input type="password" v-model="confirmPassword" />
        </div>
        <div class="form-group">
          <label>Phone</label>
          <input type="tel" v-model="newUser.phone" />
          <span v-if="phoneWarning" class="warning">{{ phoneWarning }}</span>
        </div>
        <div class="form-group">
          <label>Address</label>
          <input type="text" v-model="newUser.address" />
        </div>
        
        <div class="form-group">
          <label>Gender</label>
          <br>
          <select v-model="newUser.gender">
            <option value="" disabled selected>Select gender</option>
            <option v-for="gender in genders" :value="gender">{{ gender }}</option>
          </select>
          <span v-if="!isValidGender" class="warning">Please select a gender</span>
        </div>

        <div class="form-group">
          <label>Age</label>
          <input type="number" v-model="newUser.age" />
          <!-- <span v-if="!isValidAge" class="warning">Age must be between 10 and 100</span> -->
        </div>
        <button type="submit" >Save</button>
        
      </form>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; 

import { useToast } from "vue-toastification";
import '../assets/main.css';

export default {
  name: "Signup",
  setup() {

    const toast = useToast();
  
    const users = ref([]);
    const currentUser = reactive({});
    const api = "http://127.0.0.1:8000/api/users/";

    const newUser = reactive({
      email: '',
      password: '',
      phone: '',
      address: '',
      gender: '',
      age: ''
    });

    const confirmPassword = ref('');
    const passwordWarning = ref('');
    const phoneWarning = ref('');
    const isValidEmail = ref(true);
    const emailWarning = ref('');
    const isValidPhone = ref(true);
    const isValidGender = ref(true);
    const isValidAge = ref(true);
    const showToast = ref(false);
    const router = useRouter(); 

    const genders = ['Male', 'Female', 'Other'];


    const saveUser = async () => {
      
      if (!newUser.gender) {
        isValidGender.value = false;
        return;
      } else {
        isValidGender.value = true;
      }
      if (!newUser.email.includes('@') || !newUser.email.includes('gmail') || !newUser.email.includes('.com')) {
        isValidEmail.value = false;
        emailWarning.value = "Please enter a valid Gmail address";
        return;
      } else {
        isValidEmail.value = true;
      }
      
      const phoneRegx = /^\d{10}$/;
      if (!phoneRegx.test(newUser.phone)){
        phoneWarning.value = "Phone number should be 10 digits";
        return;
      }

     
      if (newUser.age <=0 || newUser.age > 200) {
        isValidAge.value = false;
         return;
       } else {
         isValidAge.value = true;
       }

      if (newUser.password !== confirmPassword.value) {
        passwordWarning.value = '';
        passwordWarning.value = "Passwords do not match";
        return;
      }

      const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8,}$/;
      if (!passwordRegex.test(newUser.password)) {
        passwordWarning.value = "Password must contain at least one uppercase letter, one lowercase letter, one special character, one number, and be at least 8 characters long.";
        return;
      }

  
      await axios.post('http://127.0.0.1:8000/api/users/', newUser)
        .then(response => {
          setTimeout(() => {
            const $toast = useToast();
            let instance = $toast.success('User is successfully added');
            router.push({ name: 'LoginForm' }); 
            instance.dismiss();
            $toast.clear();
          });
        })
        .catch(error => {
          console.log(error);
        });
    };

    const getUsers = () => {
      axios.get(api)
        .then(response => {
          users.value = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    };

    const resetNewUser = () => {
      newUser.email = '';
      newUser.password = '';
      confirmPassword.value = '';
      newUser.phone = '';
      newUser.address = '';
      newUser.gender = '';
      newUser.age = '';
    };

    onMounted(() => {
      getUsers();
    });

    return {
      users,
      currentUser,
      newUser,
      confirmPassword,
      saveUser,
      resetNewUser,
      showToast,
      passwordWarning,
      isValidEmail,
      emailWarning,
      isValidPhone,
      isValidGender,
      isValidAge,
      toast,
      genders,
      phoneWarning
    };
    
  },
};
</script>

<style>
.container {
  margin: 20px auto;
  padding: 20px;
  width: 60%;
  max-width: 800px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.create-form {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
}

.create-form h2 {
  margin-bottom: 10px;
}
.form-group select{
  width: 150px;
  height: 30px;
}
.form-group {
  margin-bottom: 10px;
}

.container h2 {
  text-align: center;
  text-decoration: underline;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group input[type="email"],
.form-group input[type="tel"],
.form-group input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.warning {
  color: red;
  font-size: 0.8em;
}
</style>
