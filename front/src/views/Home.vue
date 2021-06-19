<template>
  <div>
    <NavBar/>
    <Event/>
    <Conferances/>
    <Workshops/>
    <Activities/>
    <Stands/>
    <Footer/>
  </div>
</template>

<script>
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import Event from '../components/Event'
import Conferances from '../components/Conferances'
import Workshops from '../components/Workshops'
import Activities from '../components/Activities'
import Stands from '../components/Stands'

export default {
  name: 'Home',
  components: {
    NavBar,
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
