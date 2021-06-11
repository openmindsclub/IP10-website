<template>
  <div>
    <NavBar/>
    <router-view/>
    <Event/>
    <Conferances/>
    <Workshops/>
    <Activities/>
    <Stands/>
    <Footer/>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import Footer from './components/Footer'
import Acceuil from './views/Acceuil'
import Event from './views/Event'
import Conferances from './views/Conferances'
import Workshops from './views/Workshops'
import Activities from './views/Activities'
import Stands from './views/Stands'

export default {
  name: 'App',
  components: {
    NavBar,
    Acceuil,
    Event,
    Conferances,
    Workshops,
    Activities,
    Stands,
    Footer
  }
}
</script>

<style>

</style>
