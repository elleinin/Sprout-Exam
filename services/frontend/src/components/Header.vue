<template>
    <div>
        <h1 v-if="isLoggedIn">Title</h1>
        <h1 v-else>Please log in...</h1>
        <hr/><br/>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Header',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>

<style>
    h1 {
        text-align: center;
    }
</style>