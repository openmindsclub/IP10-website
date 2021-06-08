<template>
  <div>
    <NavBar/>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import Acceuil from './views/Acceuil'
export default {
  name: 'App',
  components: {
    NavBar,
    Acceuil
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
