<template><p> hi
    {{users}}
    </p>
<div v-for="u in users">{{ u.email }}</div>
<br>
<div v-for="u in users">{{ u.phone }}</div>
<br>
<div v-for="u in users">{{ u.address }}</div>
<br>
<div v-for="u in users">{{ u.gender }}</div>

</template>
    <script> 
    export default{
        data(){
            return{
                users:[]
            }
        },
    methods:{
    async fetchUsers() {
        try {
          const response = await fetch('http://127.0.0.1:8000/api/users/');
           this.users = await response.json();
        } catch (error) {
          console.error(error);
        }
      }
    }, mounted(){
        this.fetchUsers();
    }
    }
    </script>
