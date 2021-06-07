<template>
  <div class="hero-acceuil">
    <div>
      <!-- text presentation -->
      
    </div>
    <!-- cote gauche -->
    <div>
      <!-- TODO:add omc logos -->
      <div></div>
      <!-- truc du milieu a gauche -->
      <div>
        <!--  Install party ecriture normal -->
        <div></div>
        <!-- install party le magnifique logo  -->
        <div></div>
      </div>
      <!-- reseau soc ,ect (les icnoes ) -->
      <div></div>
    </div>
  </div>
</template>

<script>
import Button from "../components/Button";
export default {
  name: "Acceuil",
  component: {
    Button,
  },
};
</script>


<style scoped >
img {
  width: 100vw;
  height: 100%;
}
.hero-acceuil {
  /* Use "linear-gradient" to add a darken background effect to the image (photographer.jpg). This will make the text easier to read */
  background-image: url("../assets/Index_background_3.jpg");

  /* Set a specific height */
  height: 100vh;
  width: 100%;
  /* Position and center the image to scale nicely on all screens */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
Button {
    text-align: end;
}
</style>
