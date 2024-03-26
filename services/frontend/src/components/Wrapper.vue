<template>
  <div class="wrapper">
    <div class="cont">
    </div>
    <div class="cont">
    </div>
  </div>
</template>

<script>
// import { defineComponent } from 'vue';
// import { mapGetters, mapActions } from 'vuex';

// export default defineComponent({
//   name: 'Dashboard',
//   created: function() {
//     return this.$store.dispatch('getEmployees');
//   },
//   computed: {
//     ...mapGetters({ notes: 'stateEmployees'}),
//   }
// });
</script>

<style>
.wrapper {
  height: calc(100vh - 250px);
  width: 90vw;
  display: flex;
  flex-direction: row;
}

.cont {
  height: 100%;
  width: 80%;
  background-color: #fff;
  color: #152032;
  border-radius: 10px;
  margin: 0px 10px;
}




</style>