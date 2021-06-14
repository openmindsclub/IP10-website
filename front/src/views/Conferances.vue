<template>
    <div id="conferences" class="hero">
        <Speakers/>
        <Sessions/>
    </div>
</template>

<script>
import Speakers from '../components/Speakers.vue'
import Sessions from '../components/Sessions.vue'
export default {
  name: "Conferances",
  components: {
      Speakers,
      Sessions
  },
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/Event_background_2.jpg");

    height: fit-content;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

    display: flex;
    flex-direction: column;
}
</style>
