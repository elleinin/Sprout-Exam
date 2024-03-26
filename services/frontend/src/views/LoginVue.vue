<template>
    <div class="wrapper">
        <section class="cont">
            <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="username" class="form-label">Username:</label>
                <input type="text" name="username" v-model="form.username" class="form-control" />
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" name="password" v-model="form.password" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </section>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import user from '../store/modules/user';

export default defineComponent({
  name: 'Login',
  data() {
    return {
      form: {
        username: '',
        password:'',
      }
    };
  },
  methods: {
    async submit() {
      const data = {
          'username': this.form.username,
          'password': this.form.password
      };
      await user.actions.logIn(data);
      this.$router.push('/dashboard');
    }
  }
});
</script>

<style scoped>
    .cont {
        padding: 20px;
    }
</style>