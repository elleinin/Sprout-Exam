<template>
  <div id="app">
    <NavBar />
    <div class="main container">
      <Header />
      
      <router-view/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
import Header from '@/components/Header.vue'
export default {
  components: {
    NavBar,
    Header
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #fff;
  background-image: linear-gradient(to bottom right, #152032, #305fbe, #ec7787);;
}
.main {
  margin-top: 50px;
  padding-top: 30px;
  height: calc(100vh - 50px);
}

.wrapper {
  height: calc(100vh - 250px);
  width: 90vw;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.cont {
  height: 100%;
  width: 80%;
  background-color: #fff;
  color: #152032;
  border-radius: 10px;
  margin: 0px 10px;
  padding: 15px;
}
</style>