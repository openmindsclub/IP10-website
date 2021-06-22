<template>
  <div>
    <NavBar route="home"/>
    <Event/>
    <Conferances/>
    <Workshops/>
    <Activities/>
    <Stands/>
    <Sponsor/>
    <About/>
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
import About from '../components/About'
import Sponsor from '../components/Sponsor'

export default {
  name: 'Home',
  components: {
    NavBar,
    Event,
    Conferances,
    Workshops,
    Activities,
    Stands,
    Sponsor,
    About,
    Footer
  }
}
</script>

<style>

</style>
