<template>
    <div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="email">Email:</label>
          <input type="text" id="email" v-model="studentData.email" required>
        </div>
        <br>
        <div>
          <label for="phone">Phone Number:</label>
          <input type="number" id="phone" v-model="studentData.phone" required>
        </div>
        <br>
        <div>
          <label for="address">Address:</label>
          <input type="text" id="address" v-model="studentData.address" required>
        </div>
        <br>
        <div>
          <label for="gender">Gender:</label>
          <input type="text" id="gender" v-model="studentData.gender" required>
        </div>
        <br>
        <div>
          <label for="age">Age:</label>
          <input type="number" id="age" v-model="studentData.age" required>
        </div>
        <br>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const studentData = ref({
      email: '',
      phone: null,
      address: '',
      gender:'',
      age:null
  });
  
  const submitForm = () => {
      console.log('Student data:', studentData.value);
  };
  </script>
  