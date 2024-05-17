<template>
  <h2 class="text-2xl font-semibold text-gray-800 mb-6">Edit User Details</h2>
  <form @submit.prevent="updateUser(currentUser.id)">
    <div class="form-group mb-4">
      <label class="block text-gray-700">Email</label>
      <input type="email" v-model="currentUser.email" class="input" placeholder="Enter email address" />
      <span v-if="!isValidEmail" class="text-red-500">{{ emailWarning }}</span>
    </div>
    <div class="form-group mb-4">
      <label class="block text-gray-700">Phone</label>
      <input type="tel" v-model="currentUser.phone" class="input" placeholder="Enter phone number" />
      <span v-if="phoneWarning" class="text-red-500">{{ phoneWarning }}</span>
    </div>
    <div class="form-group mb-4">
      <label class="block text-gray-700">Address</label>
      <input type="text" v-model="currentUser.address" class="input" placeholder="Enter address" />
      <span v-if="!isValidAddress" class="text-red-500">Please enter the address</span>
    </div>

    <div class="form-group mb-4">
      <label class="block text-gray-700">Gender</label>
      <select v-model="currentUser.gender" class="input">
        <option value="" disabled>Select gender</option>
        <option v-for="gender in genders" :key="gender" :value="gender">{{ gender }}</option>
      </select>
      <span v-if="!isValidGender" class="text-red-500">{{ genderWarning }}</span>
    </div>

    <div class="form-group mb-4">
      <label class="block text-gray-700">Age</label>
      <input type="number" v-model="currentUser.age" class="input" placeholder="Enter age" />
      <span v-if="!isValidAge" class="text-red-500">Age must be greater than 0</span>
    </div>

    <div class="flex justify-between">
      <button type="submit" class="btn-primary mr-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Update</button>
      <button type="button" @click="$emit('close')" class="btn-secondary bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded">Cancel</button>
    </div>
  </form>

</template>

<script>
import { reactive, onMounted, ref } from 'vue';
import axios from 'axios';
import { useToast } from "vue-toastification";

export default {
  name: 'EditUser',
  props: {
    userId: {
      type: String,
      required: true
    }
  },
  setup(props, { emit }) {
    const toast = useToast();
    const currentUser = reactive({});
    const showToast = ref(false);
    const toastMessage = ref('');
    const api = "http://127.0.0.1:8000/api/users/";

    const phoneWarning = ref('');
    const isValidEmail = ref(true);
    const emailWarning = ref('');
    const isValidPhone = ref(true);
    const isValidGender = ref(true);
    const isValidAge = ref(true);
    const isValidAddress = ref(true); // New validation for address
    const genderWarning = ref('');

    const genders = ['Male', 'Female', 'Other'];

    const getUser = (id) => {
      axios.get(api + id + '/')
        .then(response => {
          Object.assign(currentUser, response.data);
        })
        .catch(error => {
          console.log(error);
        });
    };

    const updateUser = (id) => {
      if (!currentUser.gender) {
        isValidGender.value = false;
        genderWarning.value = "Please choose the gender";
        return;
      } else {
        isValidGender.value = true;
      }

      if (!currentUser.email.includes('@') || !currentUser.email.includes('gmail') || !currentUser.email.includes('.com')) {
        isValidEmail.value = false;
        emailWarning.value = "Please enter a valid Gmail address";
        return;
      } else {
        isValidEmail.value = true;
      }

      const phoneRegx = /^\d{10}$/;
      if (!phoneRegx.test(currentUser.phone)) {
        phoneWarning.value = "Phone number should be 10 digits";
        return;
      }

      if (!currentUser.address) { // Check if address is empty
        isValidAddress.value = false;
        return;
      } else {
        isValidAddress.value = true;
      }

      if (currentUser.age <= 0 || currentUser.age > 200) {
        isValidAge.value = false;
        return;
      } else {
        isValidAge.value = true;
      }

      axios.put(api + id + '/', currentUser)
        .then(response => {
          emit('user-updated', response.data);
          setTimeout(() => {
            toast.success('User is successfully edited');
          });
        })
        .catch(error => {
          console.log(error);
        });
    };

    onMounted(() => {
      getUser(props.userId);
    });

    return {
      currentUser,
      updateUser,
      showToast,
      toastMessage,
      toast,
      phoneWarning,
      emailWarning,
      isValidEmail,
      isValidAge,
      genders,
      isValidGender,
      isValidPhone,
      isValidAddress, // Added isValidAddress
      genderWarning
    };
  }
};
</script>

<style scoped>
/* No custom styles needed, Tailwind CSS classes handle the styling */
</style>
