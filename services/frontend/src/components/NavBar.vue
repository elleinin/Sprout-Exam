<template>
  <header>
        <nav class="navbar">
        </nav>
        <nav class="nav">
            <div class="left">
                <div><a href="/home">SPROUT SOLUTIONS TECH EXAM</a>
                </div>
            </div>
            <div class="right">
                <div><a href="/dashboard">HOME</a>
                </div>
                <div><a href="/regulars">SEE REGULAR</a></div>
                <div><a href="/contractual">SEE CONTRACTUAL</a></div>
                <div v-if="isLoggedIn"><a href="/logout">LOGOUT</a></div>
            </div>

        </nav>
    </header>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavBar',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    }
  },
});
</script>

<style scoped>
.navbar {
    position: fixed;
    height: 50px;
    width: 100%;
    background: #ec7787;
    top: 0;
    z-index: 3;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
}

.nav {
    height: 50px;
    width: 100%;
    color: white;
    top: 0;
    position: fixed;
    z-index: 5;
    display: grid;
    grid-template-areas: "left right";
    grid-template-columns: repeat(2, 1fr);
}

.nav .left {
    grid-area: left;
    margin-left: 100px;
    margin-top: 14px;
    background-color: #ec7787;
}

.nav .right {
    grid-area: right;
    height: 100%;
    width: 100%;
    top: 0;
    padding-right: 50px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
}

a {
    color: inherit;
    font-weight: 800; }

a:hover {
    color: #152032;
    transition: all 1s ease-out;
}

</style>